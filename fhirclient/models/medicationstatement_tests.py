#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import medicationstatement
from fhirdate import FHIRDate


class MedicationStatementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = medicationstatement.MedicationStatement(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testMedicationStatement1(self):
        inst = self.instantiate_from("medicationstatement-example-tylenol.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e339190> instance")
    
        self.assertTrue(inst.dosage[0].asNeededBoolean)
        self.assertEqual(inst.dosage[0].quantity.value, 1)
        self.assertEqual(inst.dosage[0].route.coding[0].code, "394899003")
        self.assertEqual(inst.dosage[0].route.coding[0].display, "oral administration of treatment")
        self.assertEqual(inst.dosage[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosage[0].schedule.repeat.frequency, 1)
        self.assertEqual(inst.dosage[0].schedule.repeat.period, 1)
        self.assertEqual(inst.dosage[0].schedule.repeat.periodUnits, "d")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2010").date)
        self.assertEqual(inst.effectiveDateTime.isostring, "2010")
        self.assertEqual(inst.id, "tylenol")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div>\n      \n      <p>500 mg Acetaminophen tablet 1/day, PRN since 2010</p>\n    \n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedicationStatement2(self):
        inst = self.instantiate_from("medicationstatement-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e339190> instance")
    
        self.assertEqual(inst.dosage[0].quantity.code, "ml")
        self.assertEqual(inst.dosage[0].quantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosage[0].quantity.units, "ml")
        self.assertEqual(inst.dosage[0].quantity.value, 10)
        self.assertEqual(inst.dosage[0].route.coding[0].code, "394899003")
        self.assertEqual(inst.dosage[0].route.coding[0].display, "oral administration of treatment")
        self.assertEqual(inst.dosage[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-06-01T14:30:00+14:00").date)
        self.assertEqual(inst.effectiveDateTime.isostring, "2012-06-01T14:30:00+14:00")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div>\n      \n      <p>Penicillin VK 10ml suspension administered by oral route at 14:30 on 1 June 2012</p>\n      \n      <p>to patient ref: a23</p>\n    \n    </div>")
        self.assertEqual(inst.text.status, "generated")

