#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import medicationknowledge
from .fhirdate import FHIRDate


class MedicationKnowledgeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicationKnowledge", js["resourceType"])
        return medicationknowledge.MedicationKnowledge(js)
    
    def testMedicationKnowledge1(self):
        inst = self.instantiate_from("medicationknowledge-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationKnowledge instance")
        self.implMedicationKnowledge1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationKnowledge", js["resourceType"])
        inst2 = medicationknowledge.MedicationKnowledge(js)
        self.implMedicationKnowledge1(inst2)
    
    def implMedicationKnowledge1(self, inst):
        self.assertEqual(inst.amount.unit, "mg/ml")
        self.assertEqual(inst.amount.value, 50)
        self.assertEqual(inst.code.coding[0].code, "0069-2587-10")
        self.assertEqual(inst.code.coding[0].display, "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)")
        self.assertEqual(inst.code.coding[0].system, "http://hl7.org/fhir/sid/ndc")
        self.assertEqual(inst.contained[0].id, "org4")
        self.assertEqual(inst.doseForm.coding[0].code, "385219001")
        self.assertEqual(inst.doseForm.coding[0].display, "Injection Solution (qualifier value)")
        self.assertEqual(inst.doseForm.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.synonym[0], "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)")
        self.assertEqual(inst.text.status, "generated")

