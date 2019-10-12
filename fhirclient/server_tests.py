# -*- coding: utf-8 -*-


import os
import io
import json
import shutil
import unittest
from . import server
from .models.R4 import fhirabstractbase as fabst
from .constants import FHIRVersion


class TestServer(unittest.TestCase):

    def tearDown(self):
        if os.path.exists('metadata'):
            os.remove('metadata')

    def doValidStatement(self, metadata, version):
        shutil.copyfile(metadata, 'metadata')
        mock = MockServer(version=version)
        mock.get_statement()

        self.assertIsNotNone(mock.auth._registration_uri)
        self.assertIsNotNone(mock.auth._authorize_uri)
        self.assertIsNotNone(mock.auth._token_uri)

    def testValidStatement_R4(self):
        self.doValidStatement('fhirclient/fixtures/test_metadata_valid_R4.json', FHIRVersion.R4)

    def testValidStatement_STU3(self):
        self.doValidStatement('fhirclient/fixtures/test_metadata_valid_STU3.json', FHIRVersion.STU3)

    def testValidStatement_DSTU2(self):
        self.doValidStatement('fhirclient/fixtures/test_metadata_valid_DSTU2.json', FHIRVersion.DSTU2)

    def testStateConservation(self):
        shutil.copyfile('fhirclient/fixtures/test_metadata_valid_R4.json', 'metadata')
        mock = MockServer()
        self.assertIsNotNone(mock.statement)

        fhir = server.FHIRServer(None, state=mock.state)
        self.assertIsNotNone(fhir.auth._registration_uri)
        self.assertIsNotNone(fhir.auth._authorize_uri)
        self.assertIsNotNone(fhir.auth._token_uri)

    def testInvalidStatement(self):
        shutil.copyfile('fhirclient/fixtures/test_metadata_invalid_R4.json', 'metadata')
        mock = MockServer()
        try:
            mock.statement()
            self.assertTrue(False, "Must have thrown exception")
        except fabst.FHIRValidationError as e:
            self.assertEqual(4, len(e.errors))
            self.assertEqual("date:", str(e.errors[0])[:5])
            self.assertEqual("format:", str(e.errors[1])[:7])
            self.assertEqual("rest.0:", str(e.errors[2])[:7])
            self.assertEqual("operation.1:", str(e.errors[2].errors[0])[:12])
            self.assertEqual("definition:", str(e.errors[2].errors[0].errors[0])[:11])
            self.assertIn("Wrong type <", str(e.errors[2].errors[0].errors[0].errors[0])[:25])
            self.assertEqual("security:", str(e.errors[2].errors[1])[:9])
            self.assertEqual("service.0:", str(e.errors[2].errors[1].errors[0])[:10])
            self.assertEqual("coding.0:", str(e.errors[2].errors[1].errors[0].errors[0])[:9])
            self.assertEqual("Superfluous entry \"systems\"", str(e.errors[2].errors[1].errors[0].errors[0].errors[0])[:27])
            self.assertEqual("Superfluous entry \"formats\"", str(e.errors[3])[:27])


class MockServer(server.FHIRServer):
    """ Reads local files.
    """

    def __init__(self, version=None):
        super(MockServer, self).__init__(None, base_uri='https://fhir.smarthealthit.org', version=version)

    def request_json(self, path, nosign=False):
        assert path
        with io.open(path, encoding='utf-8') as handle:
            return json.load(handle)

        return None
