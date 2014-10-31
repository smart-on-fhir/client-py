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
		self.assertIsNotNone(mock._registration_uri)
		self.assertIsNotNone(mock.authorize_uri)
		self.assertIsNotNone(mock.token_uri)
	
	def testInvalidConformance(self):
		shutil.copyfile('test_metadata_invalid.json', 'metadata')
		mock = MockServer()
		with self.assertRaises(Exception):
			mock.get_conformance()
	
	def testStateConservation(self):
		shutil.copyfile('test_metadata_valid.json', 'metadata')
		mock = MockServer()
		self.assertIsNotNone(mock.conformance)
		
		fhir = server.FHIRServer(state=mock.state)
		self.assertIsNotNone(fhir._registration_uri)
		self.assertIsNotNone(fhir.authorize_uri)
		self.assertIsNotNone(fhir.token_uri)


class MockServer(server.FHIRServer):
	""" Reads local files.
	"""
	
	def request_json(self, path, nosign=False):
		assert path
		with io.open(path, encoding='utf-8') as handle:
			return json.load(handle)
		
		return None
	
