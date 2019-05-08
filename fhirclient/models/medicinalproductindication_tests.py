#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import medicinalproductindication
from .fhirdate import FHIRDate


class MedicinalProductIndicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductIndication", js["resourceType"])
        return medicinalproductindication.MedicinalProductIndication(js)
    
    def testMedicinalProductIndication1(self):
        inst = self.instantiate_from("medicinalproductindication-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductIndication instance")
        self.implMedicinalProductIndication1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductIndication", js["resourceType"])
        inst2 = medicinalproductindication.MedicinalProductIndication(js)
        self.implMedicinalProductIndication1(inst2)
    
    def implMedicinalProductIndication1(self, inst):
        self.assertEqual(inst.comorbidity[0].coding[0].code, "Hipsurgery")
        self.assertEqual(inst.comorbidity[0].coding[0].system, "http://ema.europa.eu/example/comorbidity")
        self.assertEqual(inst.diseaseSymptomProcedure.coding[0].code, "Venousthromboembolismprophylaxis")
        self.assertEqual(inst.diseaseSymptomProcedure.coding[0].system, "http://ema.europa.eu/example/indicationasdisease-symptom-procedure")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.intendedEffect.coding[0].code, "PRYLX")
        self.assertEqual(inst.intendedEffect.coding[0].system, "http://ema.europa.eu/example/intendedeffect")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.population[0].ageRange.low.unit, "a")
        self.assertEqual(inst.population[0].ageRange.low.value, 18)
        self.assertEqual(inst.text.status, "generated")

