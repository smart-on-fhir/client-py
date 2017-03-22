#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


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
        self.assertTrue(inst.active)
        self.assertFalse(inst.appointmentRequired)
        self.assertEqual(inst.availabilityExceptions, "Reduced capacity is available during the Christmas period")
        self.assertTrue(inst.availableTime[0].allDay)
        self.assertEqual(inst.availableTime[0].daysOfWeek[0], "wed")
        self.assertEqual(inst.availableTime[1].availableEndTime.date, FHIRDate("05:30:00").date)
        self.assertEqual(inst.availableTime[1].availableEndTime.as_json(), "05:30:00")
        self.assertEqual(inst.availableTime[1].availableStartTime.date, FHIRDate("08:30:00").date)
        self.assertEqual(inst.availableTime[1].availableStartTime.as_json(), "08:30:00")
        self.assertEqual(inst.availableTime[1].daysOfWeek[0], "mon")
        self.assertEqual(inst.availableTime[1].daysOfWeek[1], "tue")
        self.assertEqual(inst.availableTime[1].daysOfWeek[2], "thu")
        self.assertEqual(inst.availableTime[1].daysOfWeek[3], "fri")
        self.assertEqual(inst.availableTime[2].availableEndTime.date, FHIRDate("04:30:00").date)
        self.assertEqual(inst.availableTime[2].availableEndTime.as_json(), "04:30:00")
        self.assertEqual(inst.availableTime[2].availableStartTime.date, FHIRDate("09:30:00").date)
        self.assertEqual(inst.availableTime[2].availableStartTime.as_json(), "09:30:00")
        self.assertEqual(inst.availableTime[2].daysOfWeek[0], "sat")
        self.assertEqual(inst.availableTime[2].daysOfWeek[1], "fri")
        self.assertEqual(inst.category.coding[0].code, "8")
        self.assertEqual(inst.category.coding[0].display, "Counselling")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/service-category")
        self.assertEqual(inst.category.text, "Counselling")
        self.assertEqual(inst.characteristic[0].coding[0].display, "Wheelchair access")
        self.assertEqual(inst.comment, "Providing Specialist psychology services to the greater Den Burg area, many years of experience dealing with PTSD issues")
        self.assertEqual(inst.contained[0].id, "DenBurg")
        self.assertEqual(inst.eligibility.coding[0].display, "DVA Required")
        self.assertEqual(inst.eligibilityNote, "Evidence of application for DVA status may be sufficient for commencing assessment")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org/shared-ids")
        self.assertEqual(inst.identifier[0].value, "HS-12")
        self.assertEqual(inst.name, "Consulting psychologists and/or psychology services")
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
        self.assertEqual(inst.referralMethod[0].coding[0].code, "phone")
        self.assertEqual(inst.referralMethod[0].coding[0].display, "Phone")
        self.assertEqual(inst.referralMethod[1].coding[0].code, "fax")
        self.assertEqual(inst.referralMethod[1].coding[0].display, "Fax")
        self.assertEqual(inst.referralMethod[2].coding[0].code, "elec")
        self.assertEqual(inst.referralMethod[2].coding[0].display, "Secure Messaging")
        self.assertEqual(inst.referralMethod[3].coding[0].code, "semail")
        self.assertEqual(inst.referralMethod[3].coding[0].display, "Secure Email")
        self.assertEqual(inst.serviceProvisionCode[0].coding[0].code, "cost")
        self.assertEqual(inst.serviceProvisionCode[0].coding[0].display, "Fees apply")
        self.assertEqual(inst.serviceProvisionCode[0].coding[0].system, "http://hl7.org/fhir/service-provision-conditions")
        self.assertEqual(inst.specialty[0].coding[0].code, "47505003")
        self.assertEqual(inst.specialty[0].coding[0].display, "Posttraumatic stress disorder")
        self.assertEqual(inst.specialty[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "(555) silent")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "directaddress@example.com")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "394913002")
        self.assertEqual(inst.type[0].coding[0].display, "Psychotherapy")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type[1].coding[0].code, "394587001")
        self.assertEqual(inst.type[1].coding[0].display, "Psychiatry")
        self.assertEqual(inst.type[1].coding[0].system, "http://snomed.info/sct")

