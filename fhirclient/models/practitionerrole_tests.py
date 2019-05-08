#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import practitionerrole
from .fhirdate import FHIRDate


class PractitionerRoleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PractitionerRole", js["resourceType"])
        return practitionerrole.PractitionerRole(js)
    
    def testPractitionerRole1(self):
        inst = self.instantiate_from("practitionerrole-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PractitionerRole instance")
        self.implPractitionerRole1(inst)
        
        js = inst.as_json()
        self.assertEqual("PractitionerRole", js["resourceType"])
        inst2 = practitionerrole.PractitionerRole(js)
        self.implPractitionerRole1(inst2)
    
    def implPractitionerRole1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.availabilityExceptions, "Adam is generally unavailable on public holidays and during the Christmas/New Year break")
        self.assertEqual(inst.availableTime[0].availableEndTime.date, FHIRDate("16:30:00").date)
        self.assertEqual(inst.availableTime[0].availableEndTime.as_json(), "16:30:00")
        self.assertEqual(inst.availableTime[0].availableStartTime.date, FHIRDate("09:00:00").date)
        self.assertEqual(inst.availableTime[0].availableStartTime.as_json(), "09:00:00")
        self.assertEqual(inst.availableTime[0].daysOfWeek[0], "mon")
        self.assertEqual(inst.availableTime[0].daysOfWeek[1], "tue")
        self.assertEqual(inst.availableTime[0].daysOfWeek[2], "wed")
        self.assertEqual(inst.availableTime[1].availableEndTime.date, FHIRDate("12:00:00").date)
        self.assertEqual(inst.availableTime[1].availableEndTime.as_json(), "12:00:00")
        self.assertEqual(inst.availableTime[1].availableStartTime.date, FHIRDate("09:00:00").date)
        self.assertEqual(inst.availableTime[1].availableStartTime.as_json(), "09:00:00")
        self.assertEqual(inst.availableTime[1].daysOfWeek[0], "thu")
        self.assertEqual(inst.availableTime[1].daysOfWeek[1], "fri")
        self.assertEqual(inst.code[0].coding[0].code, "RP")
        self.assertEqual(inst.code[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0286")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://www.acme.org/practitioners")
        self.assertEqual(inst.identifier[0].value, "23")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.notAvailable[0].description, "Adam will be on extended leave during May 2017")
        self.assertEqual(inst.notAvailable[0].during.end.date, FHIRDate("2017-05-20").date)
        self.assertEqual(inst.notAvailable[0].during.end.as_json(), "2017-05-20")
        self.assertEqual(inst.notAvailable[0].during.start.date, FHIRDate("2017-05-01").date)
        self.assertEqual(inst.notAvailable[0].during.start.as_json(), "2017-05-01")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2012-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2012-01-01")
        self.assertEqual(inst.specialty[0].coding[0].code, "408443003")
        self.assertEqual(inst.specialty[0].coding[0].display, "General medical practice")
        self.assertEqual(inst.specialty[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "(03) 5555 6473")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "adam.southern@example.org")
        self.assertEqual(inst.text.status, "generated")

