#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import claimresponse
from .fhirdate import FHIRDate


class ClaimResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ClaimResponse", js["resourceType"])
        return claimresponse.ClaimResponse(js)
    
    def testClaimResponse1(self):
        inst = self.instantiate_from("claimresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClaimResponse instance")
        self.implClaimResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("ClaimResponse", js["resourceType"])
        inst2 = claimresponse.ClaimResponse(js)
        self.implClaimResponse1(inst2)
    
    def implClaimResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Claim settled as per contract.")
        self.assertEqual(inst.id, "R3500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/remittance")
        self.assertEqual(inst.identifier[0].value, "R3500")
        self.assertEqual(inst.item[0].adjudication[0].amount.code, "USD")
        self.assertEqual(inst.item[0].adjudication[0].amount.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].adjudication[0].amount.value, 135.57)
        self.assertEqual(inst.item[0].adjudication[0].code.code, "eligible")
        self.assertEqual(inst.item[0].adjudication[1].amount.code, "USD")
        self.assertEqual(inst.item[0].adjudication[1].amount.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].adjudication[1].amount.value, 10.0)
        self.assertEqual(inst.item[0].adjudication[1].code.code, "copay")
        self.assertEqual(inst.item[0].adjudication[2].code.code, "eligpercent")
        self.assertEqual(inst.item[0].adjudication[2].value, 80.0)
        self.assertEqual(inst.item[0].adjudication[3].amount.code, "USD")
        self.assertEqual(inst.item[0].adjudication[3].amount.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.item[0].adjudication[3].amount.value, 100.47)
        self.assertEqual(inst.item[0].adjudication[3].code.code, "benefit")
        self.assertEqual(inst.item[0].sequenceLinkId, 1)
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.payeeType.code, "provider")
        self.assertEqual(inst.payeeType.system, "http://hl7.org/fhir/payeetype")
        self.assertEqual(inst.paymentAmount.code, "USD")
        self.assertEqual(inst.paymentAmount.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.paymentAmount.value, 100.47)
        self.assertEqual(inst.paymentDate.date, FHIRDate("2014-08-31").date)
        self.assertEqual(inst.paymentDate.as_json(), "2014-08-31")
        self.assertEqual(inst.paymentRef.system, "http://www.BenefitsInc.com/fhir/paymentRef")
        self.assertEqual(inst.paymentRef.value, "201408-2-1569478")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the ClaimResponse</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.totalBenefit.code, "USD")
        self.assertEqual(inst.totalBenefit.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.totalBenefit.value, 100.47)
        self.assertEqual(inst.totalCost.code, "USD")
        self.assertEqual(inst.totalCost.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.totalCost.value, 135.57)

