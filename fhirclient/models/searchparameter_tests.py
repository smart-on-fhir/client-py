#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        self.assertEqual(inst.base[0], "Patient")
        self.assertEqual(inst.code, "part-agree")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.description, "Search by url for a participation agreement, which is stored in a DocumentReference")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.expression, "DocumentReference.extension('http://example.org/fhir/StructureDefinition/participation-agreement')")
        self.assertEqual(inst.id, "example-extension")
        self.assertEqual(inst.name, "Example Search Parameter on an extension")
        self.assertEqual(inst.publisher, "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.target[0], "DocumentReference")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "reference")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example-extension")
        self.assertEqual(inst.xpath, "f:DocumentReference/f:extension[@url='http://example.org/fhir/StructureDefinition/participation-agreement']")
        self.assertEqual(inst.xpathUsage, "normal")
    
    def testSearchParameter2(self):
        inst = self.instantiate_from("searchparameter-example-reference.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter2(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter2(inst2)
    
    def implSearchParameter2(self, inst):
        self.assertEqual(inst.base[0], "Condition")
        self.assertEqual(inst.chain[0], "name")
        self.assertEqual(inst.chain[1], "identifier")
        self.assertEqual(inst.code, "subject")
        self.assertEqual(inst.contact[0].name, "[string]")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2013-10-23").date)
        self.assertEqual(inst.date.as_json(), "2013-10-23")
        self.assertEqual(inst.description, "Search by condition subject")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.expression, "Condition.subject")
        self.assertEqual(inst.id, "example-reference")
        self.assertEqual(inst.modifier[0], "missing")
        self.assertEqual(inst.name, "Example Search Parameter")
        self.assertEqual(inst.publisher, "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.purpose, "Need to search Condition by subject")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.target[0], "Organization")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "reference")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example-reference")
        self.assertEqual(inst.xpathUsage, "normal")
    
    def testSearchParameter3(self):
        inst = self.instantiate_from("searchparameter-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SearchParameter instance")
        self.implSearchParameter3(inst)
        
        js = inst.as_json()
        self.assertEqual("SearchParameter", js["resourceType"])
        inst2 = searchparameter.SearchParameter(js)
        self.implSearchParameter3(inst2)
    
    def implSearchParameter3(self, inst):
        self.assertEqual(inst.base[0], "Resource")
        self.assertEqual(inst.code, "_id")
        self.assertEqual(inst.comparator[0], "eq")
        self.assertEqual(inst.contact[0].name, "[string]")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2013-10-23").date)
        self.assertEqual(inst.date.as_json(), "2013-10-23")
        self.assertEqual(inst.derivedFrom, "http://hl7.org/fhir/SearchParameter/Resource-id")
        self.assertEqual(inst.description, "Search by resource identifier - e.g. same as the read interaction, but can return included resources")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.expression, "id")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].display, "United States of America (the)")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.name, "ID-SEARCH-PARAMETER")
        self.assertEqual(inst.publisher, "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.purpose, "Need to search by identifier for various infrastructural cases - mainly retrieving packages, and matching as part of a chain")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "token")
        self.assertEqual(inst.url, "http://hl7.org/fhir/SearchParameter/example")
        self.assertEqual(inst.useContext[0].code.code, "focus")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "positive")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "http://terminology.hl7.org/CodeSystem/variant-state")
        self.assertEqual(inst.version, "1")
        self.assertEqual(inst.xpath, "f:*/f:id")
        self.assertEqual(inst.xpathUsage, "normal")

