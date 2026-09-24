"""Regression tests for https://github.com/smart-on-fhir/client-py/issues/171.

The library must not use package-level (absolute) imports internally: they
break as soon as the package is consumed under a different top-level name
(e.g. vendored/renamed into another project) or in odd PYTHONPATH situations,
raising ``ModuleNotFoundError: No module named 'fhirclient'``. Relative
imports keep the library portable.
"""
import importlib
import os
import shutil
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest import mock

import fhirclient


def _import_renamed_copy(tmpdir):
    """Copy the ``fhirclient`` package to a temp dir under a different
    top-level name and import it. Returns the renamed module."""
    src = os.path.dirname(fhirclient.__file__)
    dest = os.path.join(tmpdir, "renamed_fhir")
    shutil.copytree(src, dest)
    sys.path.insert(0, tmpdir)
    return importlib.import_module("renamed_fhir")


def _drop_renamed_modules():
    for name in [m for m in sys.modules
                 if m == "renamed_fhir" or m.startswith("renamed_fhir.")]:
        del sys.modules[name]


class RenamedPackageImportTests(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="fhirclient-rename-")
        self.renamed = _import_renamed_copy(self.tmpdir)

    def tearDown(self):
        _drop_renamed_modules()
        if self.tmpdir in sys.path:
            sys.path.remove(self.tmpdir)
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_patient_property_uses_relative_import(self):
        """FHIRClient.patient's deferred import must work when the package is
        not importable as top-level ``fhirclient`` (issue #171)."""
        smart = self.renamed.client.FHIRClient(
            settings={"app_id": "x", "api_base": "https://example.org/fhir"})
        smart.server = SimpleNamespace(ready=True, state={})  # no network involved
        smart.patient_id = "123"

        patient_mod = importlib.import_module("renamed_fhir.models.patient")
        sentinel = object()
        with mock.patch.object(patient_mod.Patient, "read",
                               return_value=sentinel) as read:
            self.assertIs(smart.patient, sentinel)
        read.assert_called_once_with("123", smart.server)

    def test_execute_pagination_request_uses_relative_import(self):
        """_utils._execute_pagination_request's deferred import must work when
        the package is not importable as top-level ``fhirclient`` (#171)."""
        bundle_mod = importlib.import_module("renamed_fhir.models.bundle")
        sentinel = object()
        server = SimpleNamespace()
        with mock.patch.object(bundle_mod.Bundle, "read_from",
                               return_value=sentinel) as read_from:
            result = self.renamed._utils._execute_pagination_request(
                "https://example.org/fhir/Bundle/1", server)
        self.assertIs(result, sentinel)
        read_from.assert_called_once_with("https://example.org/fhir/Bundle/1",
                                          server)


if __name__ == "__main__":
    unittest.main()
