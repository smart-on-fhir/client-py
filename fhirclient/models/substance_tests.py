#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import substance
from .fhirdate import FHIRDate


class SubstanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Substance", js["resourceType"])
        return substance.Substance(js)
    
    def testSubstance1(self):
        inst = self.instantiate_from("substance-example-silver-nitrate-product.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance1(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance1(inst2)
    
    def implSubstance1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "chemical")
        self.assertEqual(inst.category[0].coding[0].display, "Chemical")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/substance-category")
        self.assertEqual(inst.code.coding[0].code, "333346007")
        self.assertEqual(inst.code.coding[0].display, "Silver nitrate 20% solution (product)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.description, "Solution for silver nitrate stain")
        self.assertEqual(inst.id, "f204")
        self.assertEqual(inst.identifier[0].system, "http://acme.org/identifiers/substances")
        self.assertEqual(inst.identifier[0].value, "15970")
        self.assertEqual(inst.instance[0].expiry.date, FHIRDate("2018-01-01").date)
        self.assertEqual(inst.instance[0].expiry.as_json(), "2018-01-01")
        self.assertEqual(inst.instance[0].identifier.system, "http://acme.org/identifiers/substances/lot")
        self.assertEqual(inst.instance[0].identifier.value, "AB94687")
        self.assertEqual(inst.instance[0].quantity.code, "mL")
        self.assertEqual(inst.instance[0].quantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.instance[0].quantity.unit, "mL")
        self.assertEqual(inst.instance[0].quantity.value, 100)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstance2(self):
        inst = self.instantiate_from("substance-example-amoxicillin-clavulanate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance2(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance2(inst2)
    
    def implSubstance2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "drug")
        self.assertEqual(inst.category[0].coding[0].display, "Drug or Medicament")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/substance-category")
        self.assertEqual(inst.code.coding[0].code, "392259005")
        self.assertEqual(inst.code.coding[0].display, "Amoxicillin + clavulanate potassium 875mg/125mg tablet (product)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.contained[0].id, "ingr1")
        self.assertEqual(inst.contained[1].id, "ingr2")
        self.assertEqual(inst.description, "Augmentin 875")
        self.assertEqual(inst.id, "f205")
        self.assertEqual(inst.ingredient[0].quantity.denominator.code, "mg")
        self.assertEqual(inst.ingredient[0].quantity.denominator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.ingredient[0].quantity.denominator.unit, "mg")
        self.assertEqual(inst.ingredient[0].quantity.denominator.value, 1000)
        self.assertEqual(inst.ingredient[0].quantity.numerator.code, "mg")
        self.assertEqual(inst.ingredient[0].quantity.numerator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.ingredient[0].quantity.numerator.unit, "mg")
        self.assertEqual(inst.ingredient[0].quantity.numerator.value, 875)
        self.assertEqual(inst.ingredient[1].quantity.denominator.code, "mg")
        self.assertEqual(inst.ingredient[1].quantity.denominator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.ingredient[1].quantity.denominator.unit, "mg")
        self.assertEqual(inst.ingredient[1].quantity.denominator.value, 1000)
        self.assertEqual(inst.ingredient[1].quantity.numerator.code, "mg")
        self.assertEqual(inst.ingredient[1].quantity.numerator.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.ingredient[1].quantity.numerator.unit, "mg")
        self.assertEqual(inst.ingredient[1].quantity.numerator.value, 125)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstance3(self):
        inst = self.instantiate_from("substance-example-f203-potassium.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance3(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance3(inst2)
    
    def implSubstance3(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "chemical")
        self.assertEqual(inst.category[0].coding[0].display, "Chemical")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/substance-category")
        self.assertEqual(inst.code.coding[0].code, "88480006")
        self.assertEqual(inst.code.coding[0].display, "Potassium")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.identifier[0].system, "http://acme.org/identifiers/substances")
        self.assertEqual(inst.identifier[0].value, "1234")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstance4(self):
        inst = self.instantiate_from("substance-example-f201-dust.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance4(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance4(inst2)
    
    def implSubstance4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "406466009")
        self.assertEqual(inst.code.coding[0].display, "House dust allergen")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstance5(self):
        inst = self.instantiate_from("substance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance5(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance5(inst2)
    
    def implSubstance5(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "allergen")
        self.assertEqual(inst.category[0].coding[0].display, "Allergen")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/substance-category")
        self.assertEqual(inst.code.text, "apitoxin (Honey Bee Venom)")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://acme.org/identifiers/substances")
        self.assertEqual(inst.identifier[0].value, "1463")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testSubstance6(self):
        inst = self.instantiate_from("substance-example-f202-staphylococcus.json")
        self.assertIsNotNone(inst, "Must have instantiated a Substance instance")
        self.implSubstance6(inst)
        
        js = inst.as_json()
        self.assertEqual("Substance", js["resourceType"])
        inst2 = substance.Substance(js)
        self.implSubstance6(inst2)
    
    def implSubstance6(self, inst):
        self.assertEqual(inst.code.coding[0].code, "3092008")
        self.assertEqual(inst.code.coding[0].display, "Staphylococcus Aureus")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")

