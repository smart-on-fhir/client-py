# -*- coding: utf-8 -*-


import os
import io
import json
import shutil
import server
import unittest


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
    
