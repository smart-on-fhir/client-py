#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import substance
from fhirdate import FHIRDate


class SubstanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = substance.Substance(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testSubstance1(self):
        inst = self.instantiate_from("substance-example-f201-dust.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e3a67d0> instance")
    
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "406466009")
        self.assertEqual(inst.type.coding[0].display, "House dust allergen")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testSubstance2(self):
        inst = self.instantiate_from("substance-example-f202-staphylococcus.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e3a67d0> instance")
    
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "3092008")
        self.assertEqual(inst.type.coding[0].display, "Staphylococcus Aureus")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testSubstance3(self):
        inst = self.instantiate_from("substance-example-f203-potassium.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e3a67d0> instance")
    
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "88480006")
        self.assertEqual(inst.type.coding[0].display, "Potassium")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testSubstance4(self):
        inst = self.instantiate_from("substance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e3a67d0> instance")
    
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div>Apitoxin (known as Honey Bee Venom)</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.text, "apitoxin")

