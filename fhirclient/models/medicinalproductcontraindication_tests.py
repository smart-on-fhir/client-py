#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import medicinalproductcontraindication
from .fhirdate import FHIRDate


class MedicinalProductContraindicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductContraindication", js["resourceType"])
        return medicinalproductcontraindication.MedicinalProductContraindication(js)
    
    def testMedicinalProductContraindication1(self):
        inst = self.instantiate_from("medicinalproductcontraindication-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductContraindication instance")
        self.implMedicinalProductContraindication1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductContraindication", js["resourceType"])
        inst2 = medicinalproductcontraindication.MedicinalProductContraindication(js)
        self.implMedicinalProductContraindication1(inst2)
    
    def implMedicinalProductContraindication1(self, inst):
        self.assertEqual(inst.comorbidity[0].coding[0].code, "Hepaticdisease")
        self.assertEqual(inst.comorbidity[0].coding[0].system, "http://ema.europa.eu/example/comorbidity")
        self.assertEqual(inst.disease.coding[0].code, "Coagulopathiesandbleedingdiatheses(exclthrombocytopenic)")
        self.assertEqual(inst.disease.coding[0].system, "http://ema.europa.eu/example/contraindicationsasdisease-symptom-procedure")
        self.assertEqual(inst.disease.text, "Hepatic disease associated with coagulopathy and clinically relevant bleeding risk")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")

