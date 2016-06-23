#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import healthcareservice
from .fhirdate import FHIRDate


class HealthcareServiceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("HealthcareService", js["resourceType"])
        return healthcareservice.HealthcareService(js)
    
    def testHealthcareService1(self):
        inst = self.instantiate_from("healthcareservice-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a HealthcareService instance")
        self.implHealthcareService1(inst)
        
        js = inst.as_json()
        self.assertEqual("HealthcareService", js["resourceType"])
        inst2 = healthcareservice.HealthcareService(js)
        self.implHealthcareService1(inst2)
    
    def implHealthcareService1(self, inst):
        self.assertFalse(inst.appointmentRequired)
        self.assertEqual(inst.availabilityExceptions, "Reduced capacity is available during the Christmas period")
        self.assertEqual(inst.availableTime[0].availableEndTime.date, FHIRDate("05:30:00").date)
        self.assertEqual(inst.availableTime[0].availableEndTime.as_json(), "05:30:00")
        self.assertEqual(inst.availableTime[0].availableStartTime.date, FHIRDate("08:30:00").date)
        self.assertEqual(inst.availableTime[0].availableStartTime.as_json(), "08:30:00")
        self.assertEqual(inst.availableTime[0].daysOfWeek[0], "mon")
        self.assertEqual(inst.availableTime[0].daysOfWeek[1], "tue")
        self.assertEqual(inst.availableTime[0].daysOfWeek[2], "wed")
        self.assertEqual(inst.availableTime[0].daysOfWeek[3], "thu")
        self.assertEqual(inst.availableTime[0].daysOfWeek[4], "fri")
        self.assertEqual(inst.availableTime[1].availableEndTime.date, FHIRDate("04:30:00").date)
        self.assertEqual(inst.availableTime[1].availableEndTime.as_json(), "04:30:00")
        self.assertEqual(inst.availableTime[1].availableStartTime.date, FHIRDate("09:30:00").date)
        self.assertEqual(inst.availableTime[1].availableStartTime.as_json(), "09:30:00")
        self.assertEqual(inst.availableTime[1].daysOfWeek[0], "sat")
        self.assertEqual(inst.availableTime[1].daysOfWeek[1], "fri")
        self.assertEqual(inst.characteristic[0].coding[0].display, "Wheelchair access")
        self.assertEqual(inst.comment, "Providing Specialist psychology services to the greater Den Burg area, many years of experience dealing with PTSD issues")
        self.assertEqual(inst.contained[0].id, "DenBurg")
        self.assertEqual(inst.eligibility.coding[0].display, "DVA Required")
        self.assertEqual(inst.eligibilityNote, "Evidence of application for DVA status may be sufficient for commencing assessment")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.notAvailable[0].description, "Christmas/Boxing Day")
        self.assertEqual(inst.notAvailable[0].during.end.date, FHIRDate("2015-12-26").date)
        self.assertEqual(inst.notAvailable[0].during.end.as_json(), "2015-12-26")
        self.assertEqual(inst.notAvailable[0].during.start.date, FHIRDate("2015-12-25").date)
        self.assertEqual(inst.notAvailable[0].during.start.as_json(), "2015-12-25")
        self.assertEqual(inst.notAvailable[1].description, "New Years Day")
        self.assertEqual(inst.notAvailable[1].during.end.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.notAvailable[1].during.end.as_json(), "2016-01-01")
        self.assertEqual(inst.notAvailable[1].during.start.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.notAvailable[1].during.start.as_json(), "2016-01-01")
        self.assertEqual(inst.programName[0], "PTSD outreach")
        self.assertEqual(inst.publicKey, "*** Base64 public key goes here to be used for secure messaging ***")
        self.assertEqual(inst.referralMethod[0].coding[0].code, "phone")
        self.assertEqual(inst.referralMethod[0].coding[0].display, "Phone")
        self.assertEqual(inst.referralMethod[1].coding[0].code, "fax")
        self.assertEqual(inst.referralMethod[1].coding[0].display, "Fax")
        self.assertEqual(inst.referralMethod[2].coding[0].code, "elec")
        self.assertEqual(inst.referralMethod[2].coding[0].display, "Secure Messaging")
        self.assertEqual(inst.referralMethod[3].coding[0].code, "semail")
        self.assertEqual(inst.referralMethod[3].coding[0].display, "Secure Email")
        self.assertEqual(inst.serviceName, "Consulting psychologists and/or psychology services")
        self.assertEqual(inst.serviceType[0].type.coding[0].code, "394913002")
        self.assertEqual(inst.serviceType[0].type.coding[0].display, "Psychotherapy")
        self.assertEqual(inst.serviceType[0].type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.serviceType[1].specialty[0].coding[0].code, "47505003")
        self.assertEqual(inst.serviceType[1].specialty[0].coding[0].display, "Posttraumatic stress disorder")
        self.assertEqual(inst.serviceType[1].specialty[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.serviceType[1].type.coding[0].code, "394587001")
        self.assertEqual(inst.serviceType[1].type.coding[0].display, "Psychiatry")
        self.assertEqual(inst.serviceType[1].type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "(555) silent")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "directaddress@example.com")
        self.assertEqual(inst.text.status, "generated")

