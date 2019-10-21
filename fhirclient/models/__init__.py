import os.path
import pkgutil
import importlib
from ..constants import FHIRVersion

__all__ = []

for _, name, _ in pkgutil.iter_modules([os.path.join(os.path.dirname(__file__), FHIRVersion.DEFAULT)]):
    if not name.endswith("_tests"):
        __all__.append(name)


def __getattr__(name):
    """Support lazy loading the current FHIR version submodules in Python 3 PEP-562"""
    if name in __all__:
        return importlib.import_module("." + FHIRVersion.DEFAULT + "." + name, __name__)
    raise AttributeError("module {0!r} has no attribute {1!r}".format(__name__, name))
