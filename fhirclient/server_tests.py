# -*- coding: utf-8 -*-


import os
import io
import json
import shutil
import server
import unittest
import models.fhirabstractbase as fabst


class TestServer(unittest.TestCase):
    
    def tearDown(self):
        if os.path.exists('metadata'):
            os.remove('metadata')
    
    def testValidConformance(self):
        shutil.copyfile('test_metadata_valid.json', 'metadata')
        mock = MockServer()
        mock.get_conformance()
        
        self.assertIsNotNone(mock.auth._registration_uri)
        self.assertIsNotNone(mock.auth._authorize_uri)
        self.assertIsNotNone(mock.auth._token_uri)
    
    def testStateConservation(self):
        shutil.copyfile('test_metadata_valid.json', 'metadata')
        mock = MockServer()
        self.assertIsNotNone(mock.conformance)
        
        fhir = server.FHIRServer(None, state=mock.state)
        self.assertIsNotNone(fhir.auth._registration_uri)
        self.assertIsNotNone(fhir.auth._authorize_uri)
        self.assertIsNotNone(fhir.auth._token_uri)
    
    def testInvalidConformance(self):
        shutil.copyfile('test_metadata_invalid.json', 'metadata')
        mock = MockServer()
        try:
            mock.get_conformance()
            self.assertTrue(False, "Must have thrown exception")
        except fabst.FHIRValidationError as e:
            self.assertTrue(4 == len(e.errors))
            self.assertEqual("date:", str(e.errors[0])[:5])
            self.assertEqual("format:", str(e.errors[1])[:7])
            self.assertEqual("rest:", str(e.errors[2])[:5])
            self.assertEqual("operation:", str(e.errors[2].errors[0])[:10])
            self.assertEqual("definition:", str(e.errors[2].errors[0].errors[0])[:11])
            self.assertEqual("reference:", str(e.errors[2].errors[0].errors[0].errors[0])[:10])
            self.assertEqual("Wrong type <class 'dict'>", str(e.errors[2].errors[0].errors[0].errors[0].errors[0])[:25])
            self.assertEqual("security:", str(e.errors[2].errors[1])[:9])
            self.assertEqual("service:", str(e.errors[2].errors[1].errors[0])[:8])
            self.assertEqual("coding:", str(e.errors[2].errors[1].errors[0].errors[0])[:7])
            self.assertEqual("Superfluous entry \"systems\"", str(e.errors[2].errors[1].errors[0].errors[0].errors[0])[:27])
            self.assertEqual("Superfluous entry \"formats\"", str(e.errors[3])[:27])


class MockServer(server.FHIRServer):
    """ Reads local files.
    """
    
    def __init__(self):
        super().__init__(None, base_uri='https://fhir.smarthealthit.org')
    
    def request_json(self, path, nosign=False):
        assert path
        with io.open(path, encoding='utf-8') as handle:
            return json.load(handle)
        
        return None
    
