"""Central version registry for FHIR model versions.

Coordinates which FHIR version's models are active. Supports:
- Process-wide default version (typically R4)
- Per-thread version override for multi-version apps
- Context manager for scoped version switching
- Auto-loading of version subpackages on first use

Thread Safety Note:
    The backward-compat import hook caches resolved modules in sys.modules
    under the compatibility name. This means the first thread to import
    ``fhirclient.models.patient`` "wins" for all threads using the
    compatibility path. For multi-version-per-process use, explicit versioned
    imports (``from fhirclient.models.R4.patient import Patient``) are required.
"""

import importlib
import threading
from contextlib import contextmanager
from typing import Optional

_lock = threading.Lock()
_default_version: str = "R4"
_thread_local = threading.local()
_registered_versions: dict[str, str] = {}  # version_name -> module_name


def register_version(version: str, module_name: str) -> None:
    """Register a FHIR version and its corresponding module name.

    Called by each version subpackage's ``__init__.py`` during import.

    :param version: The version identifier (e.g., "R4", "STU3")
    :param module_name: The fully qualified module name (e.g., "fhirclient.models.R4")
    """
    with _lock:
        _registered_versions[version] = module_name


def set_default_version(version: str) -> None:
    """Set the process-wide default FHIR version.

    :param version: The version identifier (e.g., "R4", "STU3")
    """
    global _default_version
    _default_version = version


def get_default_version() -> str:
    """Get the process-wide default FHIR version."""
    return _default_version


def set_thread_version(version: str) -> None:
    """Set a per-thread FHIR version override.

    :param version: The version identifier (e.g., "R4", "STU3")
    """
    _thread_local.fhir_version = version


def clear_thread_version() -> None:
    """Clear the per-thread FHIR version override."""
    if hasattr(_thread_local, "fhir_version"):
        del _thread_local.fhir_version


def get_active_version() -> str:
    """Get the currently active FHIR version.

    Returns the per-thread override if set, otherwise the process-wide default.
    """
    return getattr(_thread_local, "fhir_version", _default_version)


@contextmanager
def fhir_version_context(version: str):
    """Context manager for scoped version switching.

    Usage::

        from fhirclient._version_registry import fhir_version_context
        with fhir_version_context("STU3"):
            patient = Patient.read("123", server)

    :param version: The version identifier to use within the context
    """
    previous = getattr(_thread_local, "fhir_version", None)
    _thread_local.fhir_version = version
    try:
        yield
    finally:
        if previous is None:
            if hasattr(_thread_local, "fhir_version"):
                del _thread_local.fhir_version
        else:
            _thread_local.fhir_version = previous


def get_version_module(version: Optional[str] = None):
    """Get the module object for a specific FHIR version.

    Auto-loads the version subpackage on first use.

    :param version: The version identifier, or None for the active version
    :returns: The version's module object
    :raises ValueError: If the version is not registered and cannot be auto-loaded
    """
    version = version or get_active_version()
    if version not in _registered_versions:
        # Try to auto-load the version subpackage
        try:
            importlib.import_module(f"fhirclient.models.{version}")
        except ImportError:
            raise ValueError(
                f"FHIR version '{version}' is not registered and could not be auto-loaded"
            )
        if version not in _registered_versions:
            raise ValueError(f"FHIR version '{version}' is not registered")

    return importlib.import_module(_registered_versions[version])


# Known FHIR version identifiers.
# Add new versions here when support is added (R5, R6, etc.).
KNOWN_VERSIONS = frozenset({"R4", "STU3", "DSTU2", "R5", "R6"})

# Mapping from CapabilityStatement.fhirVersion to version identifiers.
# Add new mappings here when new FHIR versions are supported.
FHIR_VERSION_MAP: dict[str, str] = {
    "4.0.0": "R4",
    "4.0.1": "R4",
    "3.0.0": "STU3",
    "3.0.1": "STU3",
    "3.0.2": "STU3",
    # "5.0.0": "R5",  # Uncomment when R5 support is added
    # "6.0.0": "R6",  # Uncomment when R6 support is added
}
