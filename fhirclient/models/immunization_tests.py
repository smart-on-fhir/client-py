#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import immunization
from .fhirdate import FHIRDate


class ImmunizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Immunization", js["resourceType"])
        return immunization.Immunization(js)
    
    def testImmunization1(self):
        inst = self.instantiate_from("immunization-example-refused.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization1(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization1(inst2)
    
    def implImmunization1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(inst.explanation.reasonNotGiven[0].coding[0].code, "MEDPREC")
        self.assertEqual(inst.explanation.reasonNotGiven[0].coding[0].display, "medical precaution")
        self.assertEqual(inst.explanation.reasonNotGiven[0].coding[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.id, "notGiven")
        self.assertFalse(inst.reported)
        self.assertEqual(inst.text.div, "<div>Refused Immunization Example</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.vaccineType.coding[0].code, "01")
        self.assertEqual(inst.vaccineType.coding[0].display, "DTP")
        self.assertEqual(inst.vaccineType.coding[0].system, "http://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx")
        self.assertTrue(inst.wasNotGiven)
    
    def testImmunization2(self):
        inst = self.instantiate_from("immunization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization2(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization2(inst2)
    
    def implImmunization2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(inst.expirationDate.date, FHIRDate("2015-02-15").date)
        self.assertEqual(inst.expirationDate.as_json(), "2015-02-15")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.lotNumber, "AAJN11K")
        self.assertFalse(inst.reported)
        self.assertEqual(inst.text.div, "<div>Authored by Joginder Madra</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.vaccineType.coding[0].code, "Fluvax")
        self.assertEqual(inst.vaccineType.coding[0].system, "urn:oid:1.2.36.1.2001.1005.17")
        self.assertEqual(inst.vaccineType.text, "Fluvax (Influenza)")
        self.assertFalse(inst.wasNotGiven)

