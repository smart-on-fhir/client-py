"""FHIR R4 (v4.0.1) model definitions.

This package contains all generated model classes for FHIR R4.
It self-registers with the version registry on import.
"""

from fhirclient._version_registry import register_version

register_version("R4", __name__)
