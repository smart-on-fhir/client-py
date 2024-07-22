#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import paymentnotice
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class PaymentNoticeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PaymentNotice", js["resourceType"])
        return paymentnotice.PaymentNotice(js)
    
    def testPaymentNotice1(self):
        inst = self.instantiate_from("paymentnotice-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PaymentNotice instance")
        self.implPaymentNotice1(inst)
        
        js = inst.as_json()
        self.assertEqual("PaymentNotice", js["resourceType"])
        inst2 = paymentnotice.PaymentNotice(js)
        self.implPaymentNotice1(inst2)
    
    def implPaymentNotice1(self, inst):
        self.assertEqual(inst.amount.currency, "USD")
        self.assertEqual(inst.amount.value, 12500.0)
        self.assertEqual(inst.created.datetime, FHIRDateTime("2014-08-16").datetime)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "77654")
        self.assertEqual(inst.identifier[0].system, "http://benefitsinc.com/paymentnotice")
        self.assertEqual(inst.identifier[0].value, "776543")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.paymentDate.date, FHIRDate("2014-08-15").date)
        self.assertEqual(inst.paymentDate.as_json(), "2014-08-15")
        self.assertEqual(inst.paymentStatus.coding[0].code, "paid")
        self.assertEqual(inst.paymentStatus.coding[0].system, "http://terminology.hl7.org/CodeSystem/paymentstatus")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the PaymentNotice</div>")
        self.assertEqual(inst.text.status, "generated")

