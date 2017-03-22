#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import consent
from .fhirdate import FHIRDate


class ConsentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Consent", js["resourceType"])
        return consent.Consent(js)
    
    def testConsent1(self):
        inst = self.instantiate_from("consent-example-Emergency.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent1(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent1(inst2)
    
    def implConsent1(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].code, "CST")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[0].purpose[0].code, "ETREAT")
        self.assertEqual(inst.except_fhir[0].purpose[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.except_fhir[0].type, "permit")
        self.assertEqual(inst.except_fhir[1].actor[0].role.coding[0].code, "CST")
        self.assertEqual(inst.except_fhir[1].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[1].type, "deny")
        self.assertEqual(inst.id, "consent-example-Emergency")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-out")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testConsent2(self):
        inst = self.instantiate_from("consent-example-grantor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent2(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent2(inst2)
    
    def implConsent2(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.except_fhir[0].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[0].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].code, "CST")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[0].actor[1].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[0].actor[1].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[0].type, "permit")
        self.assertEqual(inst.id, "consent-example-grantor")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-out")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testConsent3(self):
        inst = self.instantiate_from("consent-example-notAuthor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent3(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent3(inst2)
    
    def implConsent3(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].code, "CST")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[0].type, "deny")
        self.assertEqual(inst.id, "consent-example-notAuthor")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-in")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testConsent4(self):
        inst = self.instantiate_from("consent-example-notOrg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent4(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent4(inst2)
    
    def implConsent4(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.except_fhir[0].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[0].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[0].action[1].coding[0].code, "correct")
        self.assertEqual(inst.except_fhir[0].action[1].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[0].type, "deny")
        self.assertEqual(inst.id, "consent-example-notOrg")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-in")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testConsent5(self):
        inst = self.instantiate_from("consent-example-notThem.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent5(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent5(inst2)
    
    def implConsent5(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.except_fhir[0].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[0].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[0].action[1].coding[0].code, "correct")
        self.assertEqual(inst.except_fhir[0].action[1].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[0].type, "deny")
        self.assertEqual(inst.id, "consent-example-notThem")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-in")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testConsent6(self):
        inst = self.instantiate_from("consent-example-notThis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent6(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent6(inst2)
    
    def implConsent6(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.except_fhir[0].data[0].meaning, "related")
        self.assertEqual(inst.except_fhir[0].type, "deny")
        self.assertEqual(inst.id, "consent-example-notThis")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-in")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testConsent7(self):
        inst = self.instantiate_from("consent-example-notTime.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent7(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent7(inst2)
    
    def implConsent7(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.except_fhir[0].period.end.date, FHIRDate("2015-02-01").date)
        self.assertEqual(inst.except_fhir[0].period.end.as_json(), "2015-02-01")
        self.assertEqual(inst.except_fhir[0].period.start.date, FHIRDate("2015-01-01").date)
        self.assertEqual(inst.except_fhir[0].period.start.as_json(), "2015-01-01")
        self.assertEqual(inst.except_fhir[0].type, "deny")
        self.assertEqual(inst.id, "consent-example-notTime")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-in")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testConsent8(self):
        inst = self.instantiate_from("consent-example-Out.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent8(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent8(inst2)
    
    def implConsent8(self, inst):
        self.assertEqual(inst.actor[0].role.coding[0].code, "CST")
        self.assertEqual(inst.actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.dateTime.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.dateTime.as_json(), "2015-11-18")
        self.assertEqual(inst.id, "consent-example-Out")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-out")
        self.assertEqual(inst.sourceAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testConsent9(self):
        inst = self.instantiate_from("consent-example-pkb.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent9(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent9(inst2)
    
    def implConsent9(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2016-06-16").date)
        self.assertEqual(inst.dateTime.as_json(), "2016-06-16")
        self.assertEqual(inst.except_fhir[0].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[0].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[0].securityLabel[0].code, "N")
        self.assertEqual(inst.except_fhir[0].securityLabel[0].system, "http://hl7.org/fhir/v3/Confidentiality")
        self.assertEqual(inst.except_fhir[0].type, "permit")
        self.assertEqual(inst.except_fhir[1].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[1].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[1].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[1].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[1].securityLabel[0].code, "PSY")
        self.assertEqual(inst.except_fhir[1].securityLabel[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.except_fhir[1].type, "permit")
        self.assertEqual(inst.except_fhir[2].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[2].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[2].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[2].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[2].securityLabel[0].code, "SOC")
        self.assertEqual(inst.except_fhir[2].securityLabel[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.except_fhir[2].type, "permit")
        self.assertEqual(inst.except_fhir[3].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[3].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[3].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[3].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[3].securityLabel[0].code, "N")
        self.assertEqual(inst.except_fhir[3].securityLabel[0].system, "http://hl7.org/fhir/v3/Confidentiality")
        self.assertEqual(inst.except_fhir[3].type, "permit")
        self.assertEqual(inst.except_fhir[4].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[4].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[4].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[4].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[4].securityLabel[0].code, "PSY")
        self.assertEqual(inst.except_fhir[4].securityLabel[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.except_fhir[4].type, "permit")
        self.assertEqual(inst.except_fhir[5].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[5].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[5].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[5].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[5].securityLabel[0].code, "SOC")
        self.assertEqual(inst.except_fhir[5].securityLabel[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.except_fhir[5].type, "permit")
        self.assertEqual(inst.except_fhir[6].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[6].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[6].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[6].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[6].securityLabel[0].code, "SEX")
        self.assertEqual(inst.except_fhir[6].securityLabel[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.except_fhir[6].type, "permit")
        self.assertEqual(inst.except_fhir[7].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[7].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[7].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[7].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[7].securityLabel[0].code, "N")
        self.assertEqual(inst.except_fhir[7].securityLabel[0].system, "http://hl7.org/fhir/v3/Confidentiality")
        self.assertEqual(inst.except_fhir[7].type, "permit")
        self.assertEqual(inst.except_fhir[8].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[8].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[8].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[8].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[8].securityLabel[0].code, "PSY")
        self.assertEqual(inst.except_fhir[8].securityLabel[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.except_fhir[8].type, "permit")
        self.assertEqual(inst.except_fhir[9].action[0].coding[0].code, "access")
        self.assertEqual(inst.except_fhir[9].action[0].coding[0].system, "http://hl7.org/fhir/consentaction")
        self.assertEqual(inst.except_fhir[9].actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.except_fhir[9].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[9].securityLabel[0].code, "SOC")
        self.assertEqual(inst.except_fhir[9].securityLabel[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.except_fhir[9].type, "permit")
        self.assertEqual(inst.id, "consent-example-pkb")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-out")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testConsent10(self):
        inst = self.instantiate_from("consent-example-signature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Consent instance")
        self.implConsent10(inst)
        
        js = inst.as_json()
        self.assertEqual("Consent", js["resourceType"])
        inst2 = consent.Consent(js)
        self.implConsent10(inst2)
    
    def implConsent10(self, inst):
        self.assertEqual(inst.actor[0].role.coding[0].code, "PRCP")
        self.assertEqual(inst.actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.category[0].coding[0].code, "HIPAA-Auth")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/consentcategorycodes")
        self.assertEqual(inst.dateTime.date, FHIRDate("2016-05-26T00:41:10-04:00").date)
        self.assertEqual(inst.dateTime.as_json(), "2016-05-26T00:41:10-04:00")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].code, "AUT")
        self.assertEqual(inst.except_fhir[0].actor[0].role.coding[0].system, "http://hl7.org/fhir/v3/ParticipationType")
        self.assertEqual(inst.except_fhir[0].class_fhir[0].code, "application/hl7-cda+xml")
        self.assertEqual(inst.except_fhir[0].class_fhir[0].system, "urn:ietf:bcp:13")
        self.assertEqual(inst.except_fhir[0].code[0].code, "34133-9")
        self.assertEqual(inst.except_fhir[0].code[0].system, "http://loinc.org")
        self.assertEqual(inst.except_fhir[0].code[1].code, "18842-5")
        self.assertEqual(inst.except_fhir[0].code[1].system, "http://loinc.org")
        self.assertEqual(inst.except_fhir[0].type, "permit")
        self.assertEqual(inst.id, "consent-example-signature")
        self.assertEqual(inst.identifier.system, "urn:oid:2.16.840.1.113883.3.72.5.9.1")
        self.assertEqual(inst.identifier.value, "494e0c7a-a69e-4fb4-9d02-6aae747790d7")
        self.assertEqual(inst.period.end.date, FHIRDate("2016-10-10").date)
        self.assertEqual(inst.period.end.as_json(), "2016-10-10")
        self.assertEqual(inst.period.start.date, FHIRDate("2015-10-10").date)
        self.assertEqual(inst.period.start.as_json(), "2015-10-10")
        self.assertEqual(inst.policyRule, "http://hl7.org/fhir/ConsentPolicy/opt-in")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

