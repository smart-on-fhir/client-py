#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import referralrequest
from .fhirdate import FHIRDate


class ReferralRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ReferralRequest", js["resourceType"])
        return referralrequest.ReferralRequest(js)
    
    def testReferralRequest1(self):
        inst = self.instantiate_from("referralrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ReferralRequest instance")
        self.implReferralRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ReferralRequest", js["resourceType"])
        inst2 = referralrequest.ReferralRequest(js)
        self.implReferralRequest1(inst2)
    
    def implReferralRequest1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.authoredOn.as_json(), "2014-02-14")
        self.assertEqual(inst.description, "In the past 2 years Beverly has had 6 instances of r) sided Otitis media. She is     falling behind her peers at school, and displaying some learning difficulties.")
        self.assertEqual(inst.groupIdentifier.value, "1234")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://orionhealth.com/fhir/apps/referralids")
        self.assertEqual(inst.identifier[0].value, "ret4421")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.occurrencePeriod.end.date, FHIRDate("2014-03-14").date)
        self.assertEqual(inst.occurrencePeriod.end.as_json(), "2014-03-14")
        self.assertEqual(inst.priority, "routine")
        self.assertEqual(inst.reasonCode[0].text, "For consideration of Grommets")
        self.assertEqual(inst.serviceRequested[0].coding[0].code, "172676009")
        self.assertEqual(inst.serviceRequested[0].coding[0].display, "Myringotomy and insertion of tympanic ventilation tube")
        self.assertEqual(inst.serviceRequested[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.serviceRequested[0].text, "Insertion of grommets")
        self.assertEqual(inst.specialty.coding[0].code, "ent")
        self.assertEqual(inst.specialty.coding[0].display, "ENT")
        self.assertEqual(inst.specialty.coding[0].system, "http://orionhealth.com/fhir/apps/specialties")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Referral to Dr Dave for Beverly weaver to have grommets inserted in her r) ear</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "103696004")
        self.assertEqual(inst.type.coding[0].display, "Patient referral to specialist")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")

