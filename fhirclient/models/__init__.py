"""FHIR model definitions with backward-compatible import redirection.

This package installs a custom import hook (MetaPathFinder) that redirects
unversioned model imports to the active FHIR version's subpackage.

For example::

    # Legacy import (redirected to active version, default R4)
    from fhirclient.models.patient import Patient

    # Explicit versioned import (no redirection needed)
    from fhirclient.models.R4.patient import Patient

Shared base modules (fhirabstractbase, fhirdate, etc.) live directly in
this package and are NOT redirected.
"""

import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import sys

from fhirclient._version_registry import KNOWN_VERSIONS, get_active_version

# Shared base modules that live in fhirclient.models/ (not versioned).
# NOTE: This set must be kept in sync with:
#   - fhir-parser-resources/template-resource.py (shared_modules list)
_SHARED_MODULES = frozenset({
    "fhirabstractbase",
    "fhirabstractresource",
    "fhirreference",
    "fhirsearch",
    "fhirdate",
    "fhirdatetime",
    "fhirinstant",
    "fhirtime",
})


class _FHIRModelRedirectLoader(importlib.abc.Loader):
    """Loader that imports the real versioned module and exposes it under the compat name."""

    def __init__(self, real_name: str):
        self._real_name = real_name

    def create_module(self, spec):
        return None  # Use default module creation

    def exec_module(self, module):
        real_module = importlib.import_module(self._real_name)
        module.__dict__.update(real_module.__dict__)
        # Ensure the compat name is cached in sys.modules
        sys.modules[module.__name__] = module


class _FHIRModelFinder(importlib.abc.MetaPathFinder):
    """Import hook that redirects unversioned model imports to the active FHIR version.

    Intercepts imports like ``fhirclient.models.patient`` and redirects to
    ``fhirclient.models.R4.patient`` (when R4 is the active version).

    Does NOT redirect:
    - Shared base modules (fhirabstractbase, fhirdate, etc.)
    - Version subpackage imports (fhirclient.models.R4, fhirclient.models.STU3)
    - Nested imports (fhirclient.models.R4.patient) - these have a dot in the suffix
    - Already-cached modules in sys.modules
    """

    _PREFIX = "fhirclient.models."

    def find_spec(self, fullname, path, target=None):
        # Only intercept fhirclient.models.X imports
        if not fullname.startswith(self._PREFIX):
            return None

        # Get the module name after "fhirclient.models."
        suffix = fullname[len(self._PREFIX):]

        # Don't intercept nested imports (e.g., fhirclient.models.R4.patient)
        if "." in suffix:
            return None

        # Don't intercept version subpackage imports
        if suffix in KNOWN_VERSIONS:
            return None

        # Don't intercept shared module imports
        if suffix in _SHARED_MODULES:
            return None

        # Already loaded - let Python use the cached module
        if fullname in sys.modules:
            return None

        # Redirect to the active version's module
        version = get_active_version()
        real_name = f"fhirclient.models.{version}.{suffix}"

        return importlib.machinery.ModuleSpec(
            fullname,
            _FHIRModelRedirectLoader(real_name),
        )


# Install the import hook once on package load
if not any(isinstance(f, _FHIRModelFinder) for f in sys.meta_path):
    sys.meta_path.insert(0, _FHIRModelFinder())
