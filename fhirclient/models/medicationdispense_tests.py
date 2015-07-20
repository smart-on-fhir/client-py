#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import medicationdispense
from .fhirdate import FHIRDate


class MedicationDispenseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicationDispense", js["resourceType"])
        return medicationdispense.MedicationDispense(js)
    
    def testMedicationDispense1(self):
        inst = self.instantiate_from("medicationdispense-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicationDispense instance")
        self.implMedicationDispense1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicationDispense", js["resourceType"])
        inst2 = medicationdispense.MedicationDispense(js)
        self.implMedicationDispense1(inst2)
    
    def implMedicationDispense1(self, inst):
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.code, "ml")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.units, "ml")
        self.assertEqual(inst.dosageInstruction[0].doseQuantity.value, 5)
        self.assertEqual(inst.dosageInstruction[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/pharmacy-core-doseType")
        self.assertEqual(inst.dosageInstruction[0].extension[0].valueCodeableConcept.coding[0].code, "440231000124106")
        self.assertEqual(inst.dosageInstruction[0].extension[0].valueCodeableConcept.coding[0].display, "Maintenance dose")
        self.assertEqual(inst.dosageInstruction[0].extension[0].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].extension[1].url, "http://hl7.org/fhir/StructureDefinition/pharmacy-core-infuseOver")
        self.assertEqual(inst.dosageInstruction[0].extension[1].valueQuantity.code, "m")
        self.assertEqual(inst.dosageInstruction[0].extension[1].valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].extension[1].valueQuantity.units, "min")
        self.assertEqual(inst.dosageInstruction[0].extension[1].valueQuantity.value, 1)
        self.assertEqual(inst.dosageInstruction[0].extension[2].url, "http://hl7.org/fhir/StructureDefinition/pharmacy-core-minDosePerPeriod")
        self.assertEqual(inst.dosageInstruction[0].extension[2].valueRatio.denominator.code, "day")
        self.assertEqual(inst.dosageInstruction[0].extension[2].valueRatio.denominator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].extension[2].valueRatio.denominator.units, "day")
        self.assertEqual(inst.dosageInstruction[0].extension[2].valueRatio.denominator.value, 1)
        self.assertEqual(inst.dosageInstruction[0].extension[2].valueRatio.numerator.code, "ml")
        self.assertEqual(inst.dosageInstruction[0].extension[2].valueRatio.numerator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].extension[2].valueRatio.numerator.units, "ml")
        self.assertEqual(inst.dosageInstruction[0].extension[2].valueRatio.numerator.value, 15)
        self.assertEqual(inst.dosageInstruction[0].extension[3].url, "http://hl7.org/fhir/StructureDefinition/pharmacy-core-maxDeliveryVolume")
        self.assertEqual(inst.dosageInstruction[0].extension[3].valueQuantity.code, "ml")
        self.assertEqual(inst.dosageInstruction[0].extension[3].valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dosageInstruction[0].extension[3].valueQuantity.units, "ml")
        self.assertEqual(inst.dosageInstruction[0].extension[3].valueQuantity.value, 15)
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].code, "394899003")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].display, "oral administration of treatment")
        self.assertEqual(inst.dosageInstruction[0].route.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dosageInstruction[0].scheduleTiming.repeat.frequency, 3)
        self.assertEqual(inst.dosageInstruction[0].scheduleTiming.repeat.period, 1)
        self.assertEqual(inst.dosageInstruction[0].scheduleTiming.repeat.periodUnits, "d")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/pharmacy-core-refillsRemaining")
        self.assertEqual(inst.extension[0].valueInteger, 0)
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/medicationdispense-validityPeriod")
        self.assertEqual(inst.extension[1].valuePeriod.end.date, FHIRDate("2012-06-10").date)
        self.assertEqual(inst.extension[1].valuePeriod.end.as_json(), "2012-06-10")
        self.assertEqual(inst.extension[1].valuePeriod.start.date, FHIRDate("2012-05-30").date)
        self.assertEqual(inst.extension[1].valuePeriod.start.as_json(), "2012-05-30")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.quantity.code, "ml")
        self.assertEqual(inst.quantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.quantity.units, "ml")
        self.assertEqual(inst.quantity.value, 100)
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.substitution.type.coding[0].code, "NoSub")
        self.assertEqual(inst.substitution.type.coding[0].display, "No substitution made or expected")
        self.assertEqual(inst.substitution.type.coding[0].system, "http://example.org/MedDispSubType")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.whenHandedOver.date, FHIRDate("2012-05-31T10:20:00+00:00").date)
        self.assertEqual(inst.whenHandedOver.as_json(), "2012-05-31T10:20:00+00:00")
        self.assertEqual(inst.whenPrepared.date, FHIRDate("2012-05-30T16:20:00+00:00").date)
        self.assertEqual(inst.whenPrepared.as_json(), "2012-05-30T16:20:00+00:00")

