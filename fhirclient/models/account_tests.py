#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 on 2017-03-15.
#  2017, SMART Health IT.


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
        self.assertEqual(inst.active.end.date, FHIRDate("2016-06-30").date)
        self.assertEqual(inst.active.end.as_json(), "2016-06-30")
        self.assertEqual(inst.active.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.active.start.as_json(), "2016-01-01")
        self.assertEqual(inst.balance.code, "USD")
        self.assertEqual(inst.balance.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.balance.unit, "USD")
        self.assertEqual(inst.balance.value, -1200)
        self.assertEqual(inst.coveragePeriod.end.date, FHIRDate("2016-06-30").date)
        self.assertEqual(inst.coveragePeriod.end.as_json(), "2016-06-30")
        self.assertEqual(inst.coveragePeriod.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.coveragePeriod.start.as_json(), "2016-01-01")
        self.assertEqual(inst.currency.code, "USD")
        self.assertEqual(inst.currency.display, "US Dollar")
        self.assertEqual(inst.currency.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.description, "Hospital charges")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].value, "654321")
        self.assertEqual(inst.name, "HACC Funded Billing for Peter James Chalmers")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">HACC Funded Billing for Peter James Chalmers</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.text, "patient")

