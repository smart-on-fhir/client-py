#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-10-12.
#  2019, SMART Health IT.

from __future__ import unicode_literals
import os
import io
import unittest
import json
from . import account
from .fhirdate import FHIRDate


class AccountTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Account", js["resourceType"])
        return account.Account(js)
    
    def testAccount1(self):
        inst = self.instantiate_from("account-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Account instance")
        self.implAccount1(inst)
        
        js = inst.as_json()
        self.assertEqual("Account", js["resourceType"])
        inst2 = account.Account(js)
        self.implAccount1(inst2)
    
    def implAccount1(self, inst):
        self.assertEqual(inst.coverage[0].priority, 1)
        self.assertEqual(inst.description, "Hospital charges")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].value, "654321")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "HACC Funded Billing for Peter James Chalmers")
        self.assertEqual(inst.servicePeriod.end.date, FHIRDate("2016-06-30").date)
        self.assertEqual(inst.servicePeriod.end.as_json(), "2016-06-30")
        self.assertEqual(inst.servicePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.servicePeriod.start.as_json(), "2016-01-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">HACC Funded Billing for Peter James Chalmers</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "PBILLACCT")
        self.assertEqual(inst.type.coding[0].display, "patient billing account")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.type.text, "patient")
    
    def testAccount2(self):
        inst = self.instantiate_from("account-example-with-guarantor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Account instance")
        self.implAccount2(inst)
        
        js = inst.as_json()
        self.assertEqual("Account", js["resourceType"])
        inst2 = account.Account(js)
        self.implAccount2(inst2)
    
    def implAccount2(self, inst):
        self.assertEqual(inst.coverage[0].priority, 1)
        self.assertEqual(inst.coverage[1].priority, 2)
        self.assertEqual(inst.description, "Hospital charges")
        self.assertFalse(inst.guarantor[0].onHold)
        self.assertEqual(inst.guarantor[0].period.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.guarantor[0].period.start.as_json(), "2016-01-01")
        self.assertEqual(inst.id, "ewg")
        self.assertEqual(inst.identifier[0].system, "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].value, "654321")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Inpatient: Peter James Chalmers")
        self.assertEqual(inst.servicePeriod.end.date, FHIRDate("2016-06-30").date)
        self.assertEqual(inst.servicePeriod.end.as_json(), "2016-06-30")
        self.assertEqual(inst.servicePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.servicePeriod.start.as_json(), "2016-01-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Inpatient Admission for Peter James Chalmers Account</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "PBILLACCT")
        self.assertEqual(inst.type.coding[0].display, "patient billing account")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.type.text, "patient")

