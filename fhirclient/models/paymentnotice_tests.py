#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import paymentnotice
from fhirdate import FHIRDate


class PaymentNoticeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = paymentnotice.PaymentNotice(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testPaymentNotice1(self):
        inst = self.instantiate_from("paymentnotice-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e364550> instance")
    
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.isostring, "2014-08-16")
        self.assertEqual(inst.id, "77654")
        self.assertEqual(inst.identifier[0].system, "http://benefitsinc.com/paymentnotice")
        self.assertEqual(inst.identifier[0].value, "776543")
        self.assertEqual(inst.paymentStatus.code, "paid")
        self.assertEqual(inst.paymentStatus.system, "http://hl7.org/fhir/paymentstatus")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the PaymentNotice</div>")
        self.assertEqual(inst.text.status, "generated")

