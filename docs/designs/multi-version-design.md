# Multi-FHIR-Version Architecture Design

## Problem Statement

The `client-py` library uses a branch-per-FHIR-version strategy: `main` carries R4 models, `develop` carries STU-3 models, and historical branches cover DSTU2. This makes it impossible to support multiple FHIR versions in a single application, forces bug fixes to shared infrastructure to be cherry-picked across branches, fragments community contributions, and multiplies CI/release overhead for each supported version.

The root cause is that ~191 generated model files and ~8 shared infrastructure files are intermixed in a single flat `fhirclient/models/` directory, creating a 1:1 coupling between git branches and FHIR versions. The shared files (client, server, auth, search, date handling) are already version-agnostic — only the generated models are version-specific.

## Architecture

### Directory Layout

```
fhirclient/
    _version_registry.py              # Version coordination
    client.py                         # Accepts fhir_version setting
    server.py                         # Version-aware capability fetch
    _utils.py                         # Version-aware bundle import
    models/
        __init__.py                   # MetaPathFinder import hook
        fhirabstractbase.py           # Shared (not versioned)
        fhirabstractresource.py       # Shared (pluggable factory dispatch)
        fhirreference.py              # Shared
        fhirsearch.py                 # Shared
        fhirdate.py                   # Shared
        fhirdatetime.py               # Shared
        fhirinstant.py                # Shared
        fhirtime.py                   # Shared
        R4/
            __init__.py               # Self-registers with version registry
            patient.py                # Generated R4 model
            observation.py            # Generated R4 model
            fhirelementfactory.py     # Generated R4 factory
            ... (192 files total)
        STU3/                         # Future: generated STU-3 models
            __init__.py
            ...
```

Shared modules live in `fhirclient/models/` and are never redirected. Generated modules live in versioned subpackages (`models/R4/`, `models/STU3/`, etc.) and use `from ..` to import shared modules and `from .` to import sibling generated modules.

### Component Details

#### 1. Version Registry (`fhirclient/_version_registry.py`)

Central coordination point for which FHIR version is active. Provides:

- **`register_version(version, module_name)`** — Called by each version subpackage's `__init__.py` on import (e.g., `register_version("R4", "fhirclient.models.R4")`). Registration is protected by `threading.Lock()`.
- **`set_default_version(version)`** / **`get_default_version()`** — Process-wide default (initially `"R4"`).
- **`set_thread_version(version)`** / **`clear_thread_version()`** — Per-thread override using `threading.local()`.
- **`get_active_version()`** — Returns thread-local override if set, otherwise the process-wide default.
- **`fhir_version_context(version)`** — Context manager that sets the thread-local version for the duration of a `with` block, restoring the previous value on exit.
- **`get_version_module(version=None)`** — Returns the module object for a version, auto-loading the subpackage on first use if needed.
- **`KNOWN_VERSIONS`** — `frozenset({"R4", "STU3", "DSTU2", "R5", "R6"})` used for input validation.
- **`FHIR_VERSION_MAP`** — Maps `CapabilityStatement.fhirVersion` strings (e.g., `"4.0.1"`) to version identifiers (e.g., `"R4"`) for auto-detection.

#### 2. Import Hook (`fhirclient/models/__init__.py`)

A `sys.meta_path` finder (`_FHIRModelFinder`) installed once on package load. It intercepts imports matching `fhirclient.models.X` and redirects them to `fhirclient.models.{active_version}.X`.

The hook does **not** redirect:
- Shared base modules (listed in `_SHARED_MODULES` frozenset)
- Version subpackage imports (e.g., `fhirclient.models.R4`)
- Nested imports (e.g., `fhirclient.models.R4.patient`) — the suffix contains a dot
- Already-cached modules in `sys.modules`

The loader (`_FHIRModelRedirectLoader`) imports the real versioned module and copies its `__dict__` into the compatibility module, then caches it in `sys.modules` under the unversioned name.

**`_SHARED_MODULES`** and the `shared_modules` list in the Jinja2 template (`fhir-parser-resources/template-resource.py`) must be kept in sync. Both locations contain cross-reference comments.

#### 3. Pluggable Factory Dispatch (`fhirclient/models/fhirabstractresource.py`)

The `_with_json_dict` classmethod previously called a hardcoded `fhirelementfactory.FHIRElementFactory.instantiate()` via a bottom-of-file import. This now calls `_get_element_factory().instantiate()`, which resolves the factory dynamically:

```python
_factory_cache: dict[str, type] = {}

def _get_element_factory():
    from fhirclient._version_registry import get_active_version
    version = get_active_version()
    if version not in _factory_cache:
        import importlib
        factory_mod = importlib.import_module(f"fhirclient.models.{version}.fhirelementfactory")
        _factory_cache[version] = factory_mod.FHIRElementFactory
    return _factory_cache[version]
```

Results are cached per-version in `_factory_cache` to avoid repeated `importlib.import_module` lookups.

#### 4. Version-Aware Client (`fhirclient/client.py`)

The `FHIRClient` settings dict accepts an optional `fhir_version` key (`"R4"`, `"STU3"`, or `"auto"`), which is passed to `FHIRServer.__init__`.

The `patient` property dynamically imports the Patient class from the server's active version:

```python
version = self.server.fhir_version
patient_mod = importlib.import_module(f"fhirclient.models.{version}.patient")
Patient = patient_mod.Patient
```

#### 5. Version-Aware Server (`fhirclient/server.py`)

- **`__init__`** accepts an optional `fhir_version` parameter. Non-`"auto"` values are validated against `KNOWN_VERSIONS` and verified to have an installed model package via `importlib.util.find_spec`.
- **`fhir_version` property** returns the explicit version if set, otherwise falls back to `get_active_version()`.
- **`get_capability()`** dynamically imports the `capabilitystatement` module from the active version. When `fhir_version` is `"auto"`, it reads `CapabilityStatement.fhirVersion` and maps it to a version identifier using `FHIR_VERSION_MAP`.
- **State serialization** includes `fhir_version` only when explicitly set (not `None`). The `from_state()` method restores it.

#### 6. Version-Aware Pagination (`fhirclient/_utils.py`)

The `_execute_pagination_request` function imports `Bundle` from the server's active version:

```python
version = server.fhir_version
bundle_mod = importlib.import_module(f"fhirclient.models.{version}.bundle")
return bundle_mod.Bundle.read_from(sanitized_url, server)
```

#### 7. Code Generation Pipeline

- **`generate_models.sh`** accepts a version parameter (`R4`, `STU3`, `all`). Defaults to `R4` for backward compatibility. Uses per-version settings files (`settings_R4.py`, `settings_STU3.py`) that set `tpl_resource_target` to the versioned subdirectory and `manual_profiles = []` (shared bases are not copied into version subdirs).
- **`template-resource.py`** contains a `shared_modules` list and conditionally emits `from ..` (for shared modules) or `from .` (for sibling generated modules) in three locations: superclass imports, `elementProperties()` lazy imports, and bottom-of-file imports.
- **`template-elementfactory.py`** adds a `get_class()` classmethod for class lookup without instantiation.
- **`template-unittest.py`** uses `from fhirclient.models.{{ fhir_version }}` instead of `from fhirclient.models` for explicit versioned imports in generated tests.
- **`settings.py`** (legacy) includes `fhir_version = 'R4'` to provide the template variable.

## Thread Safety

The version registry uses `threading.local()` for per-thread version state. `register_version()` is protected by a `threading.Lock()`. The process-wide default is a simple string reference swap (atomic in CPython).

**Known limitation:** The backward-compat import hook caches resolved modules in `sys.modules` under the unversioned name. The first thread to import `fhirclient.models.patient` determines which version is cached for all threads using that import path. For multi-version use within a single process, explicit versioned imports (`from fhirclient.models.R4.patient import Patient`) are required. This is by design — `sys.modules` is process-global in Python and per-thread module isolation would require significant complexity for a narrow use case.

## Adding a New FHIR Version

To add support for a new version (e.g., R5):

1. Create `fhir-parser-resources/settings_R5.py` with `tpl_resource_target = '../fhirclient/models/R5'` and `manual_profiles = []`
2. Create `fhirclient/models/R5/__init__.py` with `register_version("R5", __name__)`
3. Add the version string to `FHIR_VERSION_MAP` in `_version_registry.py`
4. Run `./generate_models.sh R5`

No changes to client, server, import hook, or shared base classes are needed.

## Backward Compatibility

All existing import paths continue to work:

```python
# These are equivalent (when R4 is the active version):
from fhirclient.models.patient import Patient
from fhirclient.models.R4.patient import Patient
```

The `FHIRClient` API is unchanged — `fhir_version` is an optional addition to the settings dict. Omitting it defaults to R4. All 489 existing tests pass with zero modifications.

## Usage Examples

```python
# Legacy (backward compatible, defaults to R4)
from fhirclient.models.patient import Patient

# Explicit versioned import
from fhirclient.models.R4.patient import Patient as R4Patient

# Client-level version selection
smart = FHIRClient(settings={
    'app_id': 'my_app',
    'api_base': 'https://fhir.example.com/r4',
    'fhir_version': 'R4',
})

# Auto-detection from server CapabilityStatement
smart = FHIRClient(settings={
    'app_id': 'my_app',
    'api_base': 'https://fhir.example.com/',
    'fhir_version': 'auto',
})

# Context manager for scoped version switching
from fhirclient._version_registry import fhir_version_context
with fhir_version_context("STU3"):
    patient = Patient.read("123", server)
```
