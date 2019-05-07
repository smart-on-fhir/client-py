#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import paymentreconciliation
from .fhirdate import FHIRDate


class PaymentReconciliationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PaymentReconciliation", js["resourceType"])
        return paymentreconciliation.PaymentReconciliation(js)
    
    def testPaymentReconciliation1(self):
        inst = self.instantiate_from("paymentreconciliation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PaymentReconciliation instance")
        self.implPaymentReconciliation1(inst)
        
        js = inst.as_json()
        self.assertEqual("PaymentReconciliation", js["resourceType"])
        inst2 = paymentreconciliation.PaymentReconciliation(js)
        self.implPaymentReconciliation1(inst2)
    
    def implPaymentReconciliation1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.detail[0].amount.currency, "USD")
        self.assertEqual(inst.detail[0].amount.value, 3500.0)
        self.assertEqual(inst.detail[0].date.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.detail[0].date.as_json(), "2014-08-16")
        self.assertEqual(inst.detail[0].identifier.system, "http://www.BenefitsInc.com/payment/2018/detail")
        self.assertEqual(inst.detail[0].identifier.value, "10-12345-001")
        self.assertEqual(inst.detail[0].type.coding[0].code, "payment")
        self.assertEqual(inst.detail[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/payment-type")
        self.assertEqual(inst.detail[1].amount.currency, "USD")
        self.assertEqual(inst.detail[1].amount.value, 4000.0)
        self.assertEqual(inst.detail[1].date.date, FHIRDate("2014-08-12").date)
        self.assertEqual(inst.detail[1].date.as_json(), "2014-08-12")
        self.assertEqual(inst.detail[1].identifier.system, "http://www.BenefitsInc.com/payment/2018/detail")
        self.assertEqual(inst.detail[1].identifier.value, "10-12345-002")
        self.assertEqual(inst.detail[1].type.coding[0].code, "payment")
        self.assertEqual(inst.detail[1].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/payment-type")
        self.assertEqual(inst.detail[2].amount.currency, "USD")
        self.assertEqual(inst.detail[2].amount.value, -1500.0)
        self.assertEqual(inst.detail[2].date.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.detail[2].date.as_json(), "2014-08-16")
        self.assertEqual(inst.detail[2].identifier.system, "http://www.BenefitsInc.com/payment/2018/detail")
        self.assertEqual(inst.detail[2].identifier.value, "10-12345-003")
        self.assertEqual(inst.detail[2].type.coding[0].code, "advance")
        self.assertEqual(inst.detail[2].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/payment-type")
        self.assertEqual(inst.disposition, "2014 August mid-month settlement.")
        self.assertEqual(inst.formCode.coding[0].code, "PAYREC/2016/01B")
        self.assertEqual(inst.formCode.coding[0].system, "http://ncforms.org/formid")
        self.assertEqual(inst.id, "ER2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/enrollmentresponse")
        self.assertEqual(inst.identifier[0].value, "781234")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.paymentAmount.currency, "USD")
        self.assertEqual(inst.paymentAmount.value, 7000.0)
        self.assertEqual(inst.paymentDate.date, FHIRDate("2014-08-01").date)
        self.assertEqual(inst.paymentDate.as_json(), "2014-08-01")
        self.assertEqual(inst.paymentIdentifier.system, "http://www.BenefitsInc.com/payment/2018")
        self.assertEqual(inst.paymentIdentifier.value, "10-12345")
        self.assertEqual(inst.period.end.date, FHIRDate("2014-08-31").date)
        self.assertEqual(inst.period.end.as_json(), "2014-08-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.period.start.as_json(), "2014-08-16")
        self.assertEqual(inst.processNote[0].text, "Due to the year end holiday the cutoff for submissions for December will be the 28th.")
        self.assertEqual(inst.processNote[0].type, "display")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the PaymentReconciliation</div>")
        self.assertEqual(inst.text.status, "generated")

