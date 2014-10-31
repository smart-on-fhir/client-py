#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from substance import Substance
from fhirdate import FHIRDate


class SubstanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = Substance(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testSubstance1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/substance-example-f201-dust.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
    
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>type</b>: \n        <span title=\"Codes: {http://snomed.info/sct 406466009}\">House dust allergen</span>\n      </p>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "406466009")
        self.assertEqual(inst.type.coding[0].display, "House dust allergen")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testSubstance2(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/substance-example-f202-staphylococcus.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
    
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>type</b>: \n        <span title=\"Codes: {http://snomed.info/sct 3092008}\">Staphylococcus Aureus</span>\n      </p>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "3092008")
        self.assertEqual(inst.type.coding[0].display, "Staphylococcus Aureus")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testSubstance3(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/substance-example-f203-potassium.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
    
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>type</b>: \n        <span title=\"Codes: {http://snomed.info/sct 88480006}\">Potassium</span>\n      </p>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "88480006")
        self.assertEqual(inst.type.coding[0].display, "Potassium")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")

