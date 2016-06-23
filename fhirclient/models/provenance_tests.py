#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import provenance
from .fhirdate import FHIRDate


class ProvenanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Provenance", js["resourceType"])
        return provenance.Provenance(js)
    
    def testProvenance1(self):
        inst = self.instantiate_from("provenance-example-sig.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance1(inst)
        
        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance1(inst2)
    
    def implProvenance1(self, inst):
        self.assertEqual(inst.activity.coding[0].code, "AU")
        self.assertEqual(inst.activity.coding[0].display, "authenticated")
        self.assertEqual(inst.activity.coding[0].system, "http://hl7.org/fhir/v3/DocumentCompletion")
        self.assertEqual(inst.agent[0].role.code, "verifier")
        self.assertEqual(inst.agent[0].role.system, "http://hl7.org/fhir/provenance-participant-role")
        self.assertEqual(inst.agent[0].userId.system, "http://acme.com/fhir/users/sso")
        self.assertEqual(inst.agent[0].userId.value, "hhd")
        self.assertEqual(inst.id, "signature")
        self.assertEqual(inst.reason[0].coding[0].code, "TREAT")
        self.assertEqual(inst.reason[0].coding[0].display, "treatment")
        self.assertEqual(inst.reason[0].coding[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.recorded.date, FHIRDate("2015-08-27T08:39:24+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2015-08-27T08:39:24+10:00")
        self.assertEqual(inst.signature[0].blob, "Li4u")
        self.assertEqual(inst.signature[0].contentType, "application/signature+xml")
        self.assertEqual(inst.signature[0].type[0].code, "1.2.840.10065.1.12.1.5")
        self.assertEqual(inst.signature[0].type[0].display, "Verification")
        self.assertEqual(inst.signature[0].type[0].system, "http://hl7.org/fhir/valueset-signature-type")
        self.assertEqual(inst.signature[0].when.date, FHIRDate("2015-08-27T08:39:24+10:00").date)
        self.assertEqual(inst.signature[0].when.as_json(), "2015-08-27T08:39:24+10:00")
        self.assertEqual(inst.text.div, "<div>procedure record authored on 27-June 2015 by Harold Hippocrates, MD Content extracted from Referral received 26-June</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProvenance2(self):
        inst = self.instantiate_from("provenance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance2(inst)
        
        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance2(inst2)
    
    def implProvenance2(self, inst):
        self.assertEqual(inst.agent[0].relatedAgent[0].target, "#a1")
        self.assertEqual(inst.agent[0].relatedAgent[0].type.text, "used")
        self.assertEqual(inst.agent[0].role.code, "author")
        self.assertEqual(inst.agent[0].role.system, "http://hl7.org/fhir/provenance-participant-role")
        self.assertEqual(inst.agent[0].userId.system, "http://acme.com/fhir/users/sso")
        self.assertEqual(inst.agent[0].userId.value, "hhd")
        self.assertEqual(inst.agent[1].id, "a1")
        self.assertEqual(inst.agent[1].role.code, "DEV")
        self.assertEqual(inst.agent[1].role.system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.entity[0].display, "CDA Document in XDS repository")
        self.assertEqual(inst.entity[0].reference, "DocumentReference/90f55916-9d15-4b8f-87a9-2d7ade8670c8")
        self.assertEqual(inst.entity[0].role, "source")
        self.assertEqual(inst.entity[0].type.code, "57133-1")
        self.assertEqual(inst.entity[0].type.display, "Referral note")
        self.assertEqual(inst.entity[0].type.system, "http://loinc.org")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.period.start.date, FHIRDate("2015-06-27").date)
        self.assertEqual(inst.period.start.as_json(), "2015-06-27")
        self.assertEqual(inst.policy[0], "http://acme.com/fhir/Consent/25")
        self.assertEqual(inst.reason[0].coding[0].code, "3457005")
        self.assertEqual(inst.reason[0].coding[0].display, "Referral")
        self.assertEqual(inst.reason[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reason[0].text, "Accepting a referral")
        self.assertEqual(inst.recorded.date, FHIRDate("2015-06-27T08:39:24+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2015-06-27T08:39:24+10:00")
        self.assertEqual(inst.text.div, "<div>procedure record authored on 27-June 2015 by Harold Hippocrates, MD Content extracted from Referral received 26-June</div>")
        self.assertEqual(inst.text.status, "generated")

