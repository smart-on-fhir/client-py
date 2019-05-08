#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import chargeitemdefinition
from .fhirdate import FHIRDate


class ChargeItemDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ChargeItemDefinition", js["resourceType"])
        return chargeitemdefinition.ChargeItemDefinition(js)
    
    def testChargeItemDefinition1(self):
        inst = self.instantiate_from("chargeitemdefinition-device-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ChargeItemDefinition instance")
        self.implChargeItemDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ChargeItemDefinition", js["resourceType"])
        inst2 = chargeitemdefinition.ChargeItemDefinition(js)
        self.implChargeItemDefinition1(inst2)
    
    def implChargeItemDefinition1(self, inst):
        self.assertEqual(inst.applicability[0].description, "Verify ChargeItem pertains to Device 12345")
        self.assertEqual(inst.applicability[0].expression, "%context.service.suppliedItem='Device/12345'")
        self.assertEqual(inst.applicability[0].language, "text/fhirpath")
        self.assertEqual(inst.description, "Financial details for  custom made device")
        self.assertEqual(inst.id, "device")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.currency, "EUR")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.value, 67.44)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].code, "VK")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].display, "Verkaufspreis (netto)")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].system, "http://fhir.de/CodeSystem/billing-attributes")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].type, "base")
        self.assertEqual(inst.propertyGroup[1].applicability[0].description, "Gültigkeit Steuersatz")
        self.assertEqual(inst.propertyGroup[1].applicability[0].expression, "%context.occurenceDateTime > '2018-04-01'")
        self.assertEqual(inst.propertyGroup[1].applicability[0].language, "text/fhirpath")
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].code.coding[0].code, "MWST")
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].code.coding[0].display, "Mehrwersteuersatz")
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].code.coding[0].system, "http://fhir.de/CodeSystem/billing-attributes")
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].factor, 1.19)
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].type, "tax")
        self.assertEqual(inst.propertyGroup[2].applicability[0].description, "Gültigkeit Steuersatz")
        self.assertEqual(inst.propertyGroup[2].applicability[0].expression, "%context.occurenceDateTime <= '2018-04-01'")
        self.assertEqual(inst.propertyGroup[2].applicability[0].language, "text/fhirpath")
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].code.coding[0].code, "MWST")
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].code.coding[0].display, "Mehrwersteuersatz")
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].code.coding[0].system, "http://fhir.de/CodeSystem/billing-attributes")
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].factor, 1.07)
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].type, "tax")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://sap.org/ChargeItemDefinition/device-123")
    
    def testChargeItemDefinition2(self):
        inst = self.instantiate_from("chargeitemdefinition-ebm-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ChargeItemDefinition instance")
        self.implChargeItemDefinition2(inst)
        
        js = inst.as_json()
        self.assertEqual("ChargeItemDefinition", js["resourceType"])
        inst2 = chargeitemdefinition.ChargeItemDefinition(js)
        self.implChargeItemDefinition2(inst2)
    
    def implChargeItemDefinition2(self, inst):
        self.assertEqual(inst.applicability[0].description, "Excludes billing code 13250 for same Encounter")
        self.assertEqual(inst.applicability[0].expression, "[some CQL expression]")
        self.assertEqual(inst.applicability[0].language, "text/cql")
        self.assertEqual(inst.applicability[1].description, "Applies only once per Encounter")
        self.assertEqual(inst.applicability[1].expression, "[some CQL expression]")
        self.assertEqual(inst.applicability[1].language, "text/CQL")
        self.assertEqual(inst.code.coding[0].code, "30110")
        self.assertEqual(inst.code.coding[0].display, "Allergologiediagnostik I")
        self.assertEqual(inst.code.coding[0].system, "http://fhir.de/CodingSystem/kbv/ebm")
        self.assertEqual(inst.description, "Allergologisch-diagnostischer Komplex zur Diagnostik und/oder zum Ausschluss einer (Kontakt-)Allergie vom Spättyp (Typ IV), einschl. Kosten")
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2018-06-30").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2018-06-30")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2018-04-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2018-04-01")
        self.assertEqual(inst.id, "ebm")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.currency, "EUR")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.value, 67.44)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].code, "gesamt-euro")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].display, "Gesamt (Euro)")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].system, "http://fhir.de/CodeSystem/kbv/ebm-attribute")
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].type, "base")
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].code.coding[0].code, "gesamt-punkte")
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].code.coding[0].display, "Gesamt (Punkte)")
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].code.coding[0].system, "http://fhir.de/CodeSystem/kbv/ebm-attribute")
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].factor, 633)
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].type, "informational")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://fhir.de/ChargeItemDefinition/kbv/ebm-30110")
        self.assertEqual(inst.version, "2-2018")

