#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        inst = self.instantiate_from("familymemberhistory-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a FamilyMemberHistory instance")
        self.implFamilyMemberHistory1(inst)
        
        js = inst.as_json()
        self.assertEqual("FamilyMemberHistory", js["resourceType"])
        inst2 = familymemberhistory.FamilyMemberHistory(js)
        self.implFamilyMemberHistory1(inst2)
    
    def implFamilyMemberHistory1(self, inst):
        self.assertEqual(inst.condition[0].code.coding[0].code, "315619001")
        self.assertEqual(inst.condition[0].code.coding[0].display, "Myocardial Infarction")
        self.assertEqual(inst.condition[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.condition[0].code.text, "Heart Attack")
        self.assertTrue(inst.condition[0].contributedToDeath)
        self.assertEqual(inst.condition[0].note[0].text, "Was fishing at the time. At least he went doing someting he loved.")
        self.assertEqual(inst.condition[0].onsetAge.code, "a")
        self.assertEqual(inst.condition[0].onsetAge.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.condition[0].onsetAge.unit, "yr")
        self.assertEqual(inst.condition[0].onsetAge.value, 74)
        self.assertEqual(inst.date.date, FHIRDate("2011-03-18").date)
        self.assertEqual(inst.date.as_json(), "2011-03-18")
        self.assertEqual(inst.id, "father")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.instantiatesUri[0], "http://example.org/family-member-history-questionnaire")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relationship.coding[0].code, "FTH")
        self.assertEqual(inst.relationship.coding[0].display, "father")
        self.assertEqual(inst.relationship.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
        self.assertEqual(inst.sex.coding[0].code, "male")
        self.assertEqual(inst.sex.coding[0].display, "Male")
        self.assertEqual(inst.sex.coding[0].system, "http://hl7.org/fhir/administrative-gender")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Father died of a heart attack aged 74</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testFamilyMemberHistory2(self):
        inst = self.instantiate_from("familymemberhistory-example-mother.json")
        self.assertIsNotNone(inst, "Must have instantiated a FamilyMemberHistory instance")
        self.implFamilyMemberHistory2(inst)
        
        js = inst.as_json()
        self.assertEqual("FamilyMemberHistory", js["resourceType"])
        inst2 = familymemberhistory.FamilyMemberHistory(js)
        self.implFamilyMemberHistory2(inst2)
    
    def implFamilyMemberHistory2(self, inst):
        self.assertEqual(inst.condition[0].code.coding[0].code, "371041009")
        self.assertEqual(inst.condition[0].code.coding[0].display, "Embolic Stroke")
        self.assertEqual(inst.condition[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.condition[0].code.text, "Stroke")
        self.assertEqual(inst.condition[0].onsetAge.code, "a")
        self.assertEqual(inst.condition[0].onsetAge.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.condition[0].onsetAge.unit, "yr")
        self.assertEqual(inst.condition[0].onsetAge.value, 56)
        self.assertEqual(inst.id, "mother")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relationship.coding[0].code, "MTH")
        self.assertEqual(inst.relationship.coding[0].display, "mother")
        self.assertEqual(inst.relationship.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Mother died of a stroke aged 56</div>")
        self.assertEqual(inst.text.status, "generated")

