#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


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
        self.assertEqual(inst.code, "part-agree")
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.description, "Search by url for a participation agreement, which is stored in a DocumentReference")
        self.assertEqual(inst.id, "example-extension")
        self.assertEqual(inst.name, "Example Search Parameter on an extension")
        self.assertEqual(inst.publisher, "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.target[0], "DocumentReference")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "reference")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example-extension")
        self.assertEqual(inst.xpath, "f:DocumentReference/f:extension[@url='http://example.org/fhir/StructureDefinition/participation-agreement']")
        self.assertEqual(inst.xpathUsage, "normal")
    
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
        self.assertEqual(inst.code, "_id")
        self.assertEqual(inst.contact[0].name, "[string]")
        self.assertEqual(inst.contact[0].telecom[0].system, "other")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2013-10-23").date)
        self.assertEqual(inst.date.as_json(), "2013-10-23")
        self.assertEqual(inst.description, "Search by resource identifier - e.g. same as the read interaction, but can return included resources")
        self.assertFalse(inst.experimental)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.name, "Example Search Parameter")
        self.assertEqual(inst.publisher, "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.requirements, "Need to search by identifier for various infrastructural cases - mainly retrieving packages, and matching as part of a chain")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "token")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example")
        self.assertEqual(inst.xpath, "f:*/f:id")
        self.assertEqual(inst.xpathUsage, "normal")

