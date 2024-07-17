#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import medicinalproductingredient
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class MedicinalProductIngredientTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductIngredient", js["resourceType"])
        return medicinalproductingredient.MedicinalProductIngredient(js)
    
    def testMedicinalProductIngredient1(self):
        inst = self.instantiate_from("medicinalproductingredient-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductIngredient instance")
        self.implMedicinalProductIngredient1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductIngredient", js["resourceType"])
        inst2 = medicinalproductingredient.MedicinalProductIngredient(js)
        self.implMedicinalProductIngredient1(inst2)
    
    def implMedicinalProductIngredient1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.role.coding[0].code, "ActiveBase")
        self.assertEqual(inst.role.coding[0].system, "http://ema.europa.eu/example/ingredientRole")
        self.assertEqual(inst.specifiedSubstance[0].code.coding[0].code, "equixabanCompanyequixaban1")
        self.assertEqual(inst.specifiedSubstance[0].code.coding[0].system, "http://ema.europa.eu/example/specifiedSubstance")
        self.assertEqual(inst.specifiedSubstance[0].group.coding[0].code, "2")
        self.assertEqual(inst.specifiedSubstance[0].group.coding[0].system, "http://ema.europa.eu/example/specifiedSubstanceGroup")
        self.assertEqual(inst.substance.code.coding[0].code, "EQUIXABAN")
        self.assertEqual(inst.substance.code.coding[0].system, "http://ema.europa.eu/example/substance")
        self.assertEqual(inst.substance.strength[0].presentation.denominator.unit, "{tablet}")
        self.assertEqual(inst.substance.strength[0].presentation.denominator.value, 1)
        self.assertEqual(inst.substance.strength[0].presentation.numerator.unit, "mg")
        self.assertEqual(inst.substance.strength[0].presentation.numerator.value, 2.5)
        self.assertEqual(inst.text.status, "generated")

