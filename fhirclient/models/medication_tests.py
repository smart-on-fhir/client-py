#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import medication
from .fhirdate import FHIRDate


class MedicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Medication", js["resourceType"])
        return medication.Medication(js)
    
    def testMedication1(self):
        inst = self.instantiate_from("medication-example-f001-combivent.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication1(inst)
        
        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication1(inst2)
    
    def implMedication1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "320442002")
        self.assertEqual(inst.code.coding[0].display, "Salbutamol+ipratropium bromide 100micrograms/20micrograms inhaler")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f001")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.product.form.coding[0].code, "420317006")
        self.assertEqual(inst.product.form.coding[0].display, "Inhaler (qualifier value)")
        self.assertEqual(inst.product.form.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.product.ingredient[0].amount.denominator.value, 1)
        self.assertEqual(inst.product.ingredient[0].amount.numerator.code, "ml")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.unit, "ml")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.value, 100)
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication2(self):
        inst = self.instantiate_from("medication-example-f002-crestor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication2(inst)
        
        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication2(inst2)
    
    def implMedication2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "408036003")
        self.assertEqual(inst.code.coding[0].display, "Rosuvastatin 10mg tablet")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f002")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.package.container.coding[0].code, "398124009")
        self.assertEqual(inst.package.container.coding[0].display, "drug container")
        self.assertEqual(inst.package.container.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication3(self):
        inst = self.instantiate_from("medication-example-f003-tolbutamide.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication3(inst)
        
        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication3(inst2)
    
    def implMedication3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "325267004")
        self.assertEqual(inst.code.coding[0].display, "Tolbutamide 500mg tablet")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f003")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.package.container.coding[0].code, "398124009")
        self.assertEqual(inst.package.container.coding[0].display, "drug container")
        self.assertEqual(inst.package.container.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication4(self):
        inst = self.instantiate_from("medication-example-f004-metoprolol.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication4(inst)
        
        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication4(inst2)
    
    def implMedication4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "318475005")
        self.assertEqual(inst.code.coding[0].display, "Metoprolol tartrate 50mg tablet")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f004")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.package.container.coding[0].code, "398124009")
        self.assertEqual(inst.package.container.coding[0].display, "drug container")
        self.assertEqual(inst.package.container.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication5(self):
        inst = self.instantiate_from("medication-example-f005-enalapril.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication5(inst)
        
        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication5(inst2)
    
    def implMedication5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "318851002")
        self.assertEqual(inst.code.coding[0].display, "Enalapril maleate 5mg tablet")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f005")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.package.container.coding[0].code, "398124009")
        self.assertEqual(inst.package.container.coding[0].display, "drug container")
        self.assertEqual(inst.package.container.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication6(self):
        inst = self.instantiate_from("medication-example-f201-salmeterol.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication6(inst)
        
        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication6(inst2)
    
    def implMedication6(self, inst):
        self.assertEqual(inst.code.coding[0].code, "411106009")
        self.assertEqual(inst.code.coding[0].display, "25ug Flutacisone + 250ug Salmeterol")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f201")
        self.assertFalse(inst.isBrand)
        self.assertEqual(inst.product.form.coding[0].code, "421606006")
        self.assertEqual(inst.product.form.coding[0].display, "Aerosol spray")
        self.assertEqual(inst.product.form.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.product.ingredient[0].amount.denominator.code, "PUFF")
        self.assertEqual(inst.product.ingredient[0].amount.denominator.system, "http://hl7.org/fhir/v3/orderableDrugForm")
        self.assertEqual(inst.product.ingredient[0].amount.denominator.value, 1)
        self.assertEqual(inst.product.ingredient[0].amount.numerator.code, "ug")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.value, 25)
        self.assertEqual(inst.product.ingredient[1].amount.denominator.code, "PUFF")
        self.assertEqual(inst.product.ingredient[1].amount.denominator.system, "http://hl7.org/fhir/v3/orderableDrugForm")
        self.assertEqual(inst.product.ingredient[1].amount.denominator.value, 1)
        self.assertEqual(inst.product.ingredient[1].amount.numerator.code, "ug")
        self.assertEqual(inst.product.ingredient[1].amount.numerator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.product.ingredient[1].amount.numerator.value, 250)
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication7(self):
        inst = self.instantiate_from("medication-example-f202-flucloxacilline.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication7(inst)
        
        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication7(inst2)
    
    def implMedication7(self, inst):
        self.assertEqual(inst.code.coding[0].code, "387544009")
        self.assertEqual(inst.code.coding[0].display, "Flucloxacillin")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f202")
        self.assertFalse(inst.isBrand)
        self.assertEqual(inst.product.form.coding[0].code, "385218009")
        self.assertEqual(inst.product.form.coding[0].display, "Injection")
        self.assertEqual(inst.product.form.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication8(self):
        inst = self.instantiate_from("medication-example-f203-paracetamol.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
        self.implMedication8(inst)
        
        js = inst.as_json()
        self.assertEqual("Medication", js["resourceType"])
        inst2 = medication.Medication(js)
        self.implMedication8(inst2)
    
    def implMedication8(self, inst):
        self.assertEqual(inst.code.coding[0].code, "387517004")
        self.assertEqual(inst.code.coding[0].display, "Paracetamol")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f203")
        self.assertFalse(inst.isBrand)
        self.assertEqual(inst.product.form.coding[0].code, "385055001")
        self.assertEqual(inst.product.form.coding[0].display, "Tablet")
        self.assertEqual(inst.product.form.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")

