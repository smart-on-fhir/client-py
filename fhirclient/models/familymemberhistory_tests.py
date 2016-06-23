#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import familymemberhistory
from .fhirdate import FHIRDate


class FamilyMemberHistoryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("FamilyMemberHistory", js["resourceType"])
        return familymemberhistory.FamilyMemberHistory(js)
    
    def testFamilyMemberHistory1(self):
        inst = self.instantiate_from("familymemberhistory-example-mother.json")
        self.assertIsNotNone(inst, "Must have instantiated a FamilyMemberHistory instance")
        self.implFamilyMemberHistory1(inst)
        
        js = inst.as_json()
        self.assertEqual("FamilyMemberHistory", js["resourceType"])
        inst2 = familymemberhistory.FamilyMemberHistory(js)
        self.implFamilyMemberHistory1(inst2)
    
    def implFamilyMemberHistory1(self, inst):
        self.assertEqual(inst.condition[0].code.coding[0].code, "371041009")
        self.assertEqual(inst.condition[0].code.coding[0].display, "Embolic Stroke")
        self.assertEqual(inst.condition[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.condition[0].code.text, "Stroke")
        self.assertEqual(inst.condition[0].onsetQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.condition[0].onsetQuantity.unit, "a")
        self.assertEqual(inst.condition[0].onsetQuantity.value, 56)
        self.assertEqual(inst.id, "mother")
        self.assertEqual(inst.relationship.coding[0].code, "mother")
        self.assertEqual(inst.relationship.coding[0].system, "http://hl7.org/fhir/familial-relationship")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div>Mother died of a stroke aged 56</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testFamilyMemberHistory2(self):
        inst = self.instantiate_from("familymemberhistory-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a FamilyMemberHistory instance")
        self.implFamilyMemberHistory2(inst)
        
        js = inst.as_json()
        self.assertEqual("FamilyMemberHistory", js["resourceType"])
        inst2 = familymemberhistory.FamilyMemberHistory(js)
        self.implFamilyMemberHistory2(inst2)
    
    def implFamilyMemberHistory2(self, inst):
        self.assertEqual(inst.condition[0].code.coding[0].code, "315619001")
        self.assertEqual(inst.condition[0].code.coding[0].display, "Myocardial Infarction")
        self.assertEqual(inst.condition[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.condition[0].code.text, "Heart Attack")
        self.assertEqual(inst.condition[0].note.text, "Was fishing at the time. At least he went doing someting he loved.")
        self.assertEqual(inst.condition[0].onsetQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.condition[0].onsetQuantity.unit, "a")
        self.assertEqual(inst.condition[0].onsetQuantity.value, 74)
        self.assertEqual(inst.date.date, FHIRDate("2011-03-18").date)
        self.assertEqual(inst.date.as_json(), "2011-03-18")
        self.assertEqual(inst.id, "father")
        self.assertEqual(inst.relationship.coding[0].code, "father")
        self.assertEqual(inst.relationship.coding[0].system, "http://hl7.org/fhir/familial-relationship")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div>Father died of a heart attack aged 74</div>")
        self.assertEqual(inst.text.status, "generated")

