#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import organizationaffiliation
from .fhirdate import FHIRDate


class OrganizationAffiliationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OrganizationAffiliation", js["resourceType"])
        return organizationaffiliation.OrganizationAffiliation(js)
    
    def testOrganizationAffiliation1(self):
        inst = self.instantiate_from("organizationaffiliation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a OrganizationAffiliation instance")
        self.implOrganizationAffiliation1(inst)
        
        js = inst.as_json()
        self.assertEqual("OrganizationAffiliation", js["resourceType"])
        inst2 = organizationaffiliation.OrganizationAffiliation(js)
        self.implOrganizationAffiliation1(inst2)
    
    def implOrganizationAffiliation1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.code[0].coding[0].code, "provider")
        self.assertEqual(inst.code[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/organization-role")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://www.acme.org/practitioners")
        self.assertEqual(inst.identifier[0].value, "23")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2012-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2012-01-01")
        self.assertEqual(inst.specialty[0].coding[0].code, "408443003")
        self.assertEqual(inst.specialty[0].coding[0].display, "General medical practice")
        self.assertEqual(inst.specialty[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.telecom[0].system, "email")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "general.practice@example.org")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganizationAffiliation2(self):
        inst = self.instantiate_from("orgrole-example-hie.json")
        self.assertIsNotNone(inst, "Must have instantiated a OrganizationAffiliation instance")
        self.implOrganizationAffiliation2(inst)
        
        js = inst.as_json()
        self.assertEqual("OrganizationAffiliation", js["resourceType"])
        inst2 = organizationaffiliation.OrganizationAffiliation(js)
        self.implOrganizationAffiliation2(inst2)
    
    def implOrganizationAffiliation2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.code[0].coding[0].code, "member")
        self.assertEqual(inst.code[0].coding[0].display, "Member")
        self.assertEqual(inst.code[0].coding[0].system, "http://hl7.org/fhir/organization-role")
        self.assertEqual(inst.code[0].text, "Hospital member")
        self.assertEqual(inst.id, "orgrole2")
        self.assertEqual(inst.identifier[0].system, "http://example.org/www.monumentHIE.com")
        self.assertEqual(inst.identifier[0].type.text, "member hospital")
        self.assertEqual(inst.identifier[0].use, "secondary")
        self.assertEqual(inst.identifier[0].value, "hosp32")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganizationAffiliation3(self):
        inst = self.instantiate_from("orgrole-example-services.json")
        self.assertIsNotNone(inst, "Must have instantiated a OrganizationAffiliation instance")
        self.implOrganizationAffiliation3(inst)
        
        js = inst.as_json()
        self.assertEqual("OrganizationAffiliation", js["resourceType"])
        inst2 = organizationaffiliation.OrganizationAffiliation(js)
        self.implOrganizationAffiliation3(inst2)
    
    def implOrganizationAffiliation3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.code[0].coding[0].code, "provider")
        self.assertEqual(inst.code[0].coding[0].display, "Provider")
        self.assertEqual(inst.code[0].coding[0].system, "http://hl7.org/fhir/organization-role")
        self.assertTrue(inst.code[0].coding[0].userSelected)
        self.assertEqual(inst.code[0].text, "Provider of rehabilitation services")
        self.assertEqual(inst.id, "orgrole1")
        self.assertEqual(inst.identifier[0].system, "http://example.org/www.foundingfathersmemorial.com")
        self.assertEqual(inst.identifier[0].use, "secondary")
        self.assertEqual(inst.identifier[0].value, "service002")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2022-02-01").date)
        self.assertEqual(inst.period.end.as_json(), "2022-02-01")
        self.assertEqual(inst.period.start.date, FHIRDate("2018-02-09").date)
        self.assertEqual(inst.period.start.as_json(), "2018-02-09")
        self.assertEqual(inst.specialty[0].coding[0].code, "394602003")
        self.assertEqual(inst.specialty[0].coding[0].display, "Rehabilitation - specialty")
        self.assertEqual(inst.specialty[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.specialty[0].text, "Rehabilitation")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "202-109-8765")
        self.assertEqual(inst.text.status, "generated")

