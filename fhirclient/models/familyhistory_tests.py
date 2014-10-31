#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from familyhistory import FamilyHistory
from fhirdate import FHIRDate


class FamilyHistoryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = FamilyHistory(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testFamilyHistory1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/familyhistory-example-f201-roel.json")
        self.assertIsNotNone(inst, "Must have instantiated a FamilyHistory instance")
    
        self.assertEqual(inst.note, "Both parents, both brothers and both children (twin) are still alive.")
        self.assertEqual(inst.relation[0].condition[0].type.coding[0].code, "39839004")
        self.assertEqual(inst.relation[0].condition[0].type.coding[0].display, "Diaphragmatic hernia")
        self.assertEqual(inst.relation[0].condition[0].type.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.relation[0].deceasedBoolean)
        self.assertEqual(inst.relation[0].relationship.coding[0].code, "72705000")
        self.assertEqual(inst.relation[0].relationship.coding[0].display, "Mother")
        self.assertEqual(inst.relation[0].relationship.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.relation[1].condition[0].outcome.coding[0].code, "419099009")
        self.assertEqual(inst.relation[1].condition[0].outcome.coding[0].display, "Died")
        self.assertEqual(inst.relation[1].condition[0].outcome.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.relation[1].condition[0].type.coding[0].code, "115665000")
        self.assertEqual(inst.relation[1].condition[0].type.coding[0].display, "Atopy")
        self.assertEqual(inst.relation[1].condition[0].type.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.relation[1].deceasedBoolean)
        self.assertEqual(inst.relation[1].relationship.coding[0].code, "38048003")
        self.assertEqual(inst.relation[1].relationship.coding[0].display, "Uncle")
        self.assertEqual(inst.relation[1].relationship.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.subject.display, "Roel")
        self.assertEqual(inst.subject.reference, "Patient/f201")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>subject</b>: Roel\n      </p>\n      <p>\n        <b>note</b>: Both parents, both brothers and both children (twin) are still alive.\n      </p>\n      <blockquote>\n        <p>\n          <b>relation</b>\n        </p>\n        <p>\n          <b>relationship</b>: \n          <span title=\"Codes: {http://snomed.info/sct 72705000}\">Mother</span>\n        </p>\n        <p>\n          <b>deceased[x]</b>: false\n        </p>\n        <h3>Conditions</h3>\n        <table class=\"grid\">\n          <tr>\n            <td>\n              <b>Type</b>\n            </td>\n            <td>\n              <b>Outcome</b>\n            </td>\n            <td>\n              <b>Onset[x]</b>\n            </td>\n            <td>\n              <b>Note</b>\n            </td>\n          </tr>\n          <tr>\n            <td>\n              <span title=\"Codes: {http://snomed.info/sct 39839004}\">Diaphragmatic hernia</span>\n            </td>\n            <td> </td>\n            <td> </td>\n            <td> </td>\n          </tr>\n        </table>\n      </blockquote>\n      <blockquote>\n        <p>\n          <b>relation</b>\n        </p>\n        <p>\n          <b>relationship</b>: \n          <span title=\"Codes: {http://snomed.info/sct 38048003}\">Uncle</span>\n        </p>\n        <p>\n          <b>deceased[x]</b>: true\n        </p>\n        <h3>Conditions</h3>\n        <table class=\"grid\">\n          <tr>\n            <td>\n              <b>Type</b>\n            </td>\n            <td>\n              <b>Outcome</b>\n            </td>\n            <td>\n              <b>Onset[x]</b>\n            </td>\n            <td>\n              <b>Note</b>\n            </td>\n          </tr>\n          <tr>\n            <td>\n              <span title=\"Codes: {http://snomed.info/sct 115665000}\">Atopy</span>\n            </td>\n            <td>\n              <span title=\"Codes: {http://snomed.info/sct 419099009}\">Died</span>\n            </td>\n            <td> </td>\n            <td> </td>\n          </tr>\n        </table>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testFamilyHistory2(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/familyhistory-example-mother.json")
        self.assertIsNotNone(inst, "Must have instantiated a FamilyHistory instance")
    
        self.assertEqual(inst.relation[0].condition[0].type.coding[0].code, "371041009")
        self.assertEqual(inst.relation[0].condition[0].type.coding[0].display, "Embolic Stroke")
        self.assertEqual(inst.relation[0].condition[0].type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.relation[0].condition[0].type.text, "Stroke")
        self.assertEqual(inst.relation[0].relationship.coding[0].code, "mother")
        self.assertEqual(inst.relation[0].relationship.coding[0].system, "http://hl7.org/fhir/familial-relationship")
        self.assertEqual(inst.relation[1].condition[0].type.coding[0].code, "190372001")
        self.assertEqual(inst.relation[1].condition[0].type.coding[0].display, "Type 1 Diabetes, Maturity Onset")
        self.assertEqual(inst.relation[1].condition[0].type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.relation[1].condition[0].type.text, "Diabetes Mellitus")
        self.assertEqual(inst.relation[1].relationship.coding[0].code, "brother")
        self.assertEqual(inst.relation[1].relationship.coding[0].system, "http://hl7.org/fhir/familial-relationship")
        self.assertEqual(inst.subject.display, "Peter Patient")
        self.assertEqual(inst.subject.reference, "Patient/100")
        self.assertEqual(inst.text.div, "<div>Mother died of a stroke aged 56. Brother has diabetes</div>")
        self.assertEqual(inst.text.status, "generated")

