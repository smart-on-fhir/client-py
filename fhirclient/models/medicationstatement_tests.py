#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import medicationstatement
from .fhirdate import FHIRDate


class MedicationStatementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicationStatement", js["resourceType"])
        return medicationstatement.MedicationStatement(js)
    
    def testMedicationStatement1(self):
        inst = self.instantiate_from("medicationstatement-example-tylenol.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationStatement instance")
        self.implMedicationStatement1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationStatement", js["resourceType"])
        inst2 = medicationstatement.MedicationStatement(js)
        self.implMedicationStatement1(inst2)
    
    def implMedicationStatement1(self, inst):
        self.assertTrue(inst.dosage[0].asNeededBoolean)
        self.assertEqual(inst.dosage[0].quantity.value, 1)
        self.assertEqual(inst.dosage[0].route.coding[0].code, "394899003")
        self.assertEqual(inst.dosage[0].route.coding[0].display, "oral administration of treatment")
        self.assertEqual(inst.dosage[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosage[0].schedule.repeat.frequency, 1)
        self.assertEqual(inst.dosage[0].schedule.repeat.period, 1)
        self.assertEqual(inst.dosage[0].schedule.repeat.periodUnits, "d")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2010").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2010")
        self.assertEqual(inst.id, "tylenol")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedicationStatement2(self):
        inst = self.instantiate_from("medicationstatement-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationStatement instance")
        self.implMedicationStatement2(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationStatement", js["resourceType"])
        inst2 = medicationstatement.MedicationStatement(js)
        self.implMedicationStatement2(inst2)
    
    def implMedicationStatement2(self, inst):
        self.assertEqual(inst.dosage[0].quantity.code, "ml")
        self.assertEqual(inst.dosage[0].quantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosage[0].quantity.units, "ml")
        self.assertEqual(inst.dosage[0].quantity.value, 10)
        self.assertEqual(inst.dosage[0].route.coding[0].code, "394899003")
        self.assertEqual(inst.dosage[0].route.coding[0].display, "oral administration of treatment")
        self.assertEqual(inst.dosage[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-06-01T14:30:00+14:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-06-01T14:30:00+14:00")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")

