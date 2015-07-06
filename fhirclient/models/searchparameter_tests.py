#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import searchparameter
from .fhirdate import FHIRDate


class SearchParameterTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SearchParameter", js["resourceType"])
        return searchparameter.SearchParameter(js)
    
    def testSearchParameter1(self):
        inst = self.instantiate_from("searchparameter-example-extension.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter1(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter1(inst2)
    
    def implSearchParameter1(self, inst):
        self.assertEqual(inst.base, "Patient")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.description, "Search by url for a participation agreement")
        self.assertEqual(inst.id, "example-extension")
        self.assertEqual(inst.name, "Example Search Parameter on an extension")
        self.assertEqual(inst.publisher, "HL7 FHIR Project")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "token")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example-extension")
        self.assertEqual(inst.xpath, "http://example.org/fhir/StructureDefinition/participation-agreement")
    
    def testSearchParameter2(self):
        inst = self.instantiate_from("searchparameter-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter2(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter2(inst2)
    
    def implSearchParameter2(self, inst):
        self.assertEqual(inst.base, "Resource")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.description, "Search by resource identifier - e.g. same as the read interaction, but can return included resources")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.name, "Example Search Parameter")
        self.assertEqual(inst.publisher, "HL7 FHIR Project")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "token")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example")
        self.assertEqual(inst.xpath, "f:id")

