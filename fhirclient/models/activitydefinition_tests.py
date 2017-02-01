#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.10959 on 2017-02-01.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import activitydefinition
from .fhirdate import FHIRDate


class ActivityDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ActivityDefinition", js["resourceType"])
        return activitydefinition.ActivityDefinition(js)
    
    def testActivityDefinition1(self):
        inst = self.instantiate_from("activitydefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition1(inst2)
    
    def implActivityDefinition1(self, inst):
        self.assertEqual(inst.category, "referral")
        self.assertEqual(inst.code.coding[0].code, "306206005")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Referral to service (procedure)")
        self.assertEqual(inst.description, "refer to primary care mental-health integrated care program for evaluation and treatment of mental health conditions now")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.participantType[0], "practitioner")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Referral definition</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testActivityDefinition2(self):
        inst = self.instantiate_from("activitydefinition-medicationorder-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition2(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition2(inst2)
    
    def implActivityDefinition2(self, inst):
        self.assertEqual(inst.category, "drug")
        self.assertEqual(inst.contained[0].id, "citalopramMedication")
        self.assertEqual(inst.contained[1].id, "citalopramSubstance")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.unit, "{tbl}")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.value, 1)
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].code, "26643006")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].display, "Oral route (qualifier value)")
        self.assertEqual(inst.dosageInstruction[0].route.text, "Oral route (qualifier value)")
        self.assertEqual(inst.dosageInstruction[0].text, "1 tablet oral 1 time daily")
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.period, 1)
        self.assertEqual(inst.dosageInstruction[0].timing.repeat.periodUnit, "d")
        self.assertEqual(inst.dynamicValue[0].expression, "3")
        self.assertEqual(inst.dynamicValue[0].path, "dispenseRequest.numberOfRepeatsAllowed")
        self.assertEqual(inst.dynamicValue[1].expression, "30 '{tbl}'")
        self.assertEqual(inst.dynamicValue[1].path, "dispenseRequest.quantity")
        self.assertEqual(inst.id, "citalopramPrescription")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")

