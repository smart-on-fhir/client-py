#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from medication import Medication
from fhirdate import FHIRDate


class MedicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = Medication(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testMedication1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/medication-example-f001-combivent.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
    
        self.assertEqual(inst.code.coding[0].code, "320442002")
        self.assertEqual(inst.code.coding[0].display, "Salbutamol+ipratropium bromide 100micrograms/20micrograms inhaler")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.kind, "product")
        self.assertEqual(inst.name, "Combivent")
        self.assertEqual(inst.product.form.coding[0].code, "420317006")
        self.assertEqual(inst.product.form.coding[0].display, "Inhaler (qualifier value)")
        self.assertEqual(inst.product.form.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.product.ingredient[0].amount.denominator.value, 1)
        self.assertEqual(inst.product.ingredient[0].amount.numerator.code, "ml")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.units, "ml")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.value, 100)
        self.assertEqual(inst.product.ingredient[0].item.display, "Combivent")
        self.assertEqual(inst.product.ingredient[0].item.reference, "Medication/f001")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>name</b>: Combivent\n      </p>\n      <p>\n        <b>code</b>: \n        <span title=\"Codes: {http://snomed.info/sct 320442002}\">Salbutamol+ipratropium bromide 100micrograms/20micrograms inhaler</span>\n      </p>\n      <p>\n        <b>isBrand</b>: true\n      </p>\n      <p>\n        <b>kind</b>: product\n      </p>\n      <blockquote>\n        <p>\n          <b>product</b>\n        </p>\n        <p>\n          <b>form</b>: \n          <span title=\"Codes: {http://snomed.info/sct 420317006}\">Inhaler (qualifier value)</span>\n        </p>\n        <h3>Ingredients</h3>\n        <table class=\"grid\">\n          <tr>\n            <td>\n              <b>Item</b>\n            </td>\n            <td>\n              <b>Amount</b>\n            </td>\n          </tr>\n          <tr>\n            <td>Combivent</td>\n            <td>100 ml/1 null</td>\n          </tr>\n        </table>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication2(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/medication-example-f002-crestor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
    
        self.assertEqual(inst.code.coding[0].code, "408036003")
        self.assertEqual(inst.code.coding[0].display, "Rosuvastatin 10mg tablet")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.kind, "product")
        self.assertEqual(inst.name, "Crestor")
        self.assertEqual(inst.package.container.coding[0].code, "398124009")
        self.assertEqual(inst.package.container.coding[0].display, "drug container")
        self.assertEqual(inst.package.container.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>name</b>: Crestor\n      </p>\n      <p>\n        <b>code</b>: \n        <span title=\"Codes: {http://snomed.info/sct 408036003}\">Rosuvastatin 10mg tablet</span>\n      </p>\n      <p>\n        <b>isBrand</b>: true\n      </p>\n      <p>\n        <b>kind</b>: product\n      </p>\n      <blockquote>\n        <p>\n          <b>package</b>\n        </p>\n        <p>\n          <b>container</b>: \n          <span title=\"Codes: {http://snomed.info/sct 398124009}\">drug container</span>\n        </p>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication3(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/medication-example-f003-tolbutamide.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
    
        self.assertEqual(inst.code.coding[0].code, "325267004")
        self.assertEqual(inst.code.coding[0].display, "Tolbutamide 500mg tablet")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.kind, "product")
        self.assertEqual(inst.name, "Tolbutamide")
        self.assertEqual(inst.package.container.coding[0].code, "398124009")
        self.assertEqual(inst.package.container.coding[0].display, "drug container")
        self.assertEqual(inst.package.container.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>name</b>: Tolbutamide\n      </p>\n      <p>\n        <b>code</b>: \n        <span title=\"Codes: {http://snomed.info/sct 325267004}\">Tolbutamide 500mg tablet</span>\n      </p>\n      <p>\n        <b>isBrand</b>: true\n      </p>\n      <p>\n        <b>kind</b>: product\n      </p>\n      <blockquote>\n        <p>\n          <b>package</b>\n        </p>\n        <p>\n          <b>container</b>: \n          <span title=\"Codes: {http://snomed.info/sct 398124009}\">drug container</span>\n        </p>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication4(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/medication-example-f004-metoprolol.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
    
        self.assertEqual(inst.code.coding[0].code, "318475005")
        self.assertEqual(inst.code.coding[0].display, "Metoprolol tartrate 50mg tablet")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.kind, "product")
        self.assertEqual(inst.name, "Metoprolol")
        self.assertEqual(inst.package.container.coding[0].code, "398124009")
        self.assertEqual(inst.package.container.coding[0].display, "drug container")
        self.assertEqual(inst.package.container.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>name</b>: Metoprolol\n      </p>\n      <p>\n        <b>code</b>: \n        <span title=\"Codes: {http://snomed.info/sct 318475005}\">Metoprolol tartrate 50mg tablet</span>\n      </p>\n      <p>\n        <b>isBrand</b>: true\n      </p>\n      <p>\n        <b>kind</b>: product\n      </p>\n      <blockquote>\n        <p>\n          <b>package</b>\n        </p>\n        <p>\n          <b>container</b>: \n          <span title=\"Codes: {http://snomed.info/sct 398124009}\">drug container</span>\n        </p>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication5(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/medication-example-f005-enalapril.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
    
        self.assertEqual(inst.code.coding[0].code, "318851002")
        self.assertEqual(inst.code.coding[0].display, "Enalapril maleate 5mg tablet")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.isBrand)
        self.assertEqual(inst.kind, "product")
        self.assertEqual(inst.name, "Enalapril")
        self.assertEqual(inst.package.container.coding[0].code, "398124009")
        self.assertEqual(inst.package.container.coding[0].display, "drug container")
        self.assertEqual(inst.package.container.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>name</b>: Enalapril\n      </p>\n      <p>\n        <b>code</b>: \n        <span title=\"Codes: {http://snomed.info/sct 318851002}\">Enalapril maleate 5mg tablet</span>\n      </p>\n      <p>\n        <b>isBrand</b>: true\n      </p>\n      <p>\n        <b>kind</b>: product\n      </p>\n      <blockquote>\n        <p>\n          <b>package</b>\n        </p>\n        <p>\n          <b>container</b>: \n          <span title=\"Codes: {http://snomed.info/sct 398124009}\">drug container</span>\n        </p>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication6(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/medication-example-f201-salmeterol.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
    
        self.assertEqual(inst.code.coding[0].code, "411106009")
        self.assertEqual(inst.code.coding[0].display, "25ug Flutacisone + 250ug Salmeterol")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.isBrand)
        self.assertEqual(inst.kind, "product")
        self.assertEqual(inst.name, "Salmeterol/fluticason")
        self.assertEqual(inst.product.form.coding[0].code, "421606006")
        self.assertEqual(inst.product.form.coding[0].display, "Aerosol spray")
        self.assertEqual(inst.product.form.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.product.ingredient[0].amount.denominator.code, "PUFF")
        self.assertEqual(inst.product.ingredient[0].amount.denominator.system, "http://hl7.org/fhir/v3/orderableDrugForm")
        self.assertEqual(inst.product.ingredient[0].amount.denominator.value, 1)
        self.assertEqual(inst.product.ingredient[0].amount.numerator.code, "ug")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.product.ingredient[0].amount.numerator.value, 25)
        self.assertEqual(inst.product.ingredient[0].item.display, "flutacisone")
        self.assertEqual(inst.product.ingredient[1].amount.denominator.code, "PUFF")
        self.assertEqual(inst.product.ingredient[1].amount.denominator.system, "http://hl7.org/fhir/v3/orderableDrugForm")
        self.assertEqual(inst.product.ingredient[1].amount.denominator.value, 1)
        self.assertEqual(inst.product.ingredient[1].amount.numerator.code, "ug")
        self.assertEqual(inst.product.ingredient[1].amount.numerator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.product.ingredient[1].amount.numerator.value, 250)
        self.assertEqual(inst.product.ingredient[1].item.display, "salmeterol")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>name</b>: Salmeterol/fluticason\n      </p>\n      <p>\n        <b>code</b>: \n        <span title=\"Codes: {http://snomed.info/sct 411106009}\">25ug Flutacisone + 250ug Salmeterol</span>\n      </p>\n      <p>\n        <b>isBrand</b>: false\n      </p>\n      <p>\n        <b>kind</b>: product\n      </p>\n      <blockquote>\n        <p>\n          <b>product</b>\n        </p>\n        <p>\n          <b>form</b>: \n          <span title=\"Codes: {http://snomed.info/sct 421606006}\">Aerosol spray</span>\n        </p>\n        <h3>Ingredients</h3>\n        <table class=\"grid\">\n          <tr>\n            <td>\n              <b>Item</b>\n            </td>\n            <td>\n              <b>Amount</b>\n            </td>\n          </tr>\n          <tr>\n            <td>flutacisone</td>\n            <td>25 ug/1 PUFF</td>\n          </tr>\n          <tr>\n            <td>salmeterol</td>\n            <td>250 ug/1 PUFF</td>\n          </tr>\n        </table>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication7(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/medication-example-f202-flucloxacilline.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
    
        self.assertEqual(inst.code.coding[0].code, "387544009")
        self.assertEqual(inst.code.coding[0].display, "Flucloxacillin")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.isBrand)
        self.assertEqual(inst.kind, "product")
        self.assertEqual(inst.name, "Flucloxacillin")
        self.assertEqual(inst.product.form.coding[0].code, "385218009")
        self.assertEqual(inst.product.form.coding[0].display, "Injection")
        self.assertEqual(inst.product.form.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>name</b>: Flucloxacillin\n      </p>\n      <p>\n        <b>code</b>: \n        <span title=\"Codes: {http://snomed.info/sct 387544009}\">Flucloxacillin</span>\n      </p>\n      <p>\n        <b>isBrand</b>: false\n      </p>\n      <p>\n        <b>kind</b>: product\n      </p>\n      <blockquote>\n        <p>\n          <b>product</b>\n        </p>\n        <p>\n          <b>form</b>: \n          <span title=\"Codes: {http://snomed.info/sct 385218009}\">Injection</span>\n        </p>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testMedication8(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/medication-example-f203-paracetamol.json")
        self.assertIsNotNone(inst, "Must have instantiated a Medication instance")
    
        self.assertEqual(inst.code.coding[0].code, "387517004")
        self.assertEqual(inst.code.coding[0].display, "Paracetamol")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertFalse(inst.isBrand)
        self.assertEqual(inst.kind, "product")
        self.assertEqual(inst.name, "Paracetamol")
        self.assertEqual(inst.product.form.coding[0].code, "385055001")
        self.assertEqual(inst.product.form.coding[0].display, "Tablet")
        self.assertEqual(inst.product.form.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>name</b>: Paracetamol\n      </p>\n      <p>\n        <b>code</b>: \n        <span title=\"Codes: {http://snomed.info/sct 387517004}\">Paracetamol</span>\n      </p>\n      <p>\n        <b>isBrand</b>: false\n      </p>\n      <p>\n        <b>kind</b>: product\n      </p>\n      <blockquote>\n        <p>\n          <b>product</b>\n        </p>\n        <p>\n          <b>form</b>: \n          <span title=\"Codes: {http://snomed.info/sct 385055001}\">Tablet</span>\n        </p>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")

