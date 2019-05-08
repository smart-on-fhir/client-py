#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import chargeitem
from .fhirdate import FHIRDate


class ChargeItemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ChargeItem", js["resourceType"])
        return chargeitem.ChargeItem(js)
    
    def testChargeItem1(self):
        inst = self.instantiate_from("chargeitem-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ChargeItem instance")
        self.implChargeItem1(inst)
        
        js = inst.as_json()
        self.assertEqual("ChargeItem", js["resourceType"])
        inst2 = chargeitem.ChargeItem(js)
        self.implChargeItem1(inst2)
    
    def implChargeItem1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "01510")
        self.assertEqual(inst.code.coding[0].display, "Zusatzpauschale für Beobachtung nach diagnostischer Koronarangiografie")
        self.assertEqual(inst.definitionUri[0], "http://www.kbv.de/tools/ebm/html/01520_2904360860826220813632.html")
        self.assertEqual(inst.enteredDate.date, FHIRDate("2017-01-25T23:55:04+01:00").date)
        self.assertEqual(inst.enteredDate.as_json(), "2017-01-25T23:55:04+01:00")
        self.assertEqual(inst.factorOverride, 0.8)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://myHospital.org/ChargeItems")
        self.assertEqual(inst.identifier[0].value, "654321")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text, "The code is only applicable for periods longer than 4h")
        self.assertEqual(inst.note[0].time.date, FHIRDate("2017-01-25T23:55:04+01:00").date)
        self.assertEqual(inst.note[0].time.as_json(), "2017-01-25T23:55:04+01:00")
        self.assertEqual(inst.occurrencePeriod.end.date, FHIRDate("2017-01-25T12:35:00+01:00").date)
        self.assertEqual(inst.occurrencePeriod.end.as_json(), "2017-01-25T12:35:00+01:00")
        self.assertEqual(inst.occurrencePeriod.start.date, FHIRDate("2017-01-25T08:00:00+01:00").date)
        self.assertEqual(inst.occurrencePeriod.start.as_json(), "2017-01-25T08:00:00+01:00")
        self.assertEqual(inst.overrideReason, "Patient is Cardiologist's golf buddy, so he gets a 20% discount!")
        self.assertEqual(inst.performer[0].function.coding[0].code, "17561000")
        self.assertEqual(inst.performer[0].function.coding[0].display, "Cardiologist")
        self.assertEqual(inst.performer[0].function.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.performer[1].function.coding[0].code, "224542009")
        self.assertEqual(inst.performer[1].function.coding[0].display, "Coronary Care Nurse")
        self.assertEqual(inst.performer[1].function.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.priceOverride.currency, "EUR")
        self.assertEqual(inst.priceOverride.value, 40)
        self.assertEqual(inst.quantity.value, 1)
        self.assertEqual(inst.reason[0].coding[0].code, "123456")
        self.assertEqual(inst.reason[0].coding[0].display, "DIAG-1")
        self.assertEqual(inst.reason[0].coding[0].system, "http://hl7.org/fhir/sid/icd-10")
        self.assertEqual(inst.status, "billable")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Example of ChargeItem Usage in Context of the German EBM Billing code system</div>")
        self.assertEqual(inst.text.status, "generated")

