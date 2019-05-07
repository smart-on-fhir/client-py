#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import substancespecification
from .fhirdate import FHIRDate


class SubstanceSpecificationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SubstanceSpecification", js["resourceType"])
        return substancespecification.SubstanceSpecification(js)
    
    def testSubstanceSpecification1(self):
        inst = self.instantiate_from("substancesourcematerial-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceSpecification instance")
        self.implSubstanceSpecification1(inst)
        
        js = inst.as_json()
        self.assertEqual("SubstanceSpecification", js["resourceType"])
        inst2 = substancespecification.SubstanceSpecification(js)
        self.implSubstanceSpecification1(inst2)
    
    def implSubstanceSpecification1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstanceSpecification2(self):
        inst = self.instantiate_from("substanceprotein-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceSpecification instance")
        self.implSubstanceSpecification2(inst)
        
        js = inst.as_json()
        self.assertEqual("SubstanceSpecification", js["resourceType"])
        inst2 = substancespecification.SubstanceSpecification(js)
        self.implSubstanceSpecification2(inst2)
    
    def implSubstanceSpecification2(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstanceSpecification3(self):
        inst = self.instantiate_from("substancepolymer-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceSpecification instance")
        self.implSubstanceSpecification3(inst)
        
        js = inst.as_json()
        self.assertEqual("SubstanceSpecification", js["resourceType"])
        inst2 = substancespecification.SubstanceSpecification(js)
        self.implSubstanceSpecification3(inst2)
    
    def implSubstanceSpecification3(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstanceSpecification4(self):
        inst = self.instantiate_from("substancespecification-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceSpecification instance")
        self.implSubstanceSpecification4(inst)
        
        js = inst.as_json()
        self.assertEqual("SubstanceSpecification", js["resourceType"])
        inst2 = substancespecification.SubstanceSpecification(js)
        self.implSubstanceSpecification4(inst2)
    
    def implSubstanceSpecification4(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstanceSpecification5(self):
        inst = self.instantiate_from("substancereferenceinformation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceSpecification instance")
        self.implSubstanceSpecification5(inst)
        
        js = inst.as_json()
        self.assertEqual("SubstanceSpecification", js["resourceType"])
        inst2 = substancespecification.SubstanceSpecification(js)
        self.implSubstanceSpecification5(inst2)
    
    def implSubstanceSpecification5(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstanceSpecification6(self):
        inst = self.instantiate_from("substancenucleicacid-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SubstanceSpecification instance")
        self.implSubstanceSpecification6(inst)
        
        js = inst.as_json()
        self.assertEqual("SubstanceSpecification", js["resourceType"])
        inst2 = substancespecification.SubstanceSpecification(js)
        self.implSubstanceSpecification6(inst2)
    
    def implSubstanceSpecification6(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p></div>")
        self.assertEqual(inst.text.status, "generated")

