#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import schedule
from .fhirdate import FHIRDate


class ScheduleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Schedule", js["resourceType"])
        return schedule.Schedule(js)
    
    def testSchedule1(self):
        inst = self.instantiate_from("schedule-provider-location1-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Schedule instance")
        self.implSchedule1(inst)
        
        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule1(inst2)
    
    def implSchedule1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.comment, "The slots attached to this schedule are for genetic counselling in the USS Enterprise-D Sickbay.")
        self.assertEqual(inst.id, "exampleloc1")
        self.assertEqual(inst.identifier[0].system, "http://example.org/scheduleid")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "46")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.planningHorizon.end.date, FHIRDate("2017-12-25T09:30:00Z").date)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2017-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.date, FHIRDate("2017-12-25T09:15:00Z").date)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2017-12-25T09:15:00Z")
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "General Practice")
        self.assertEqual(inst.serviceType[0].coding[0].code, "75")
        self.assertEqual(inst.serviceType[0].coding[0].display, "Genetic Counselling")
        self.assertEqual(inst.specialty[0].coding[0].code, "394580004")
        self.assertEqual(inst.specialty[0].coding[0].display, "Clinical genetics")
        self.assertEqual(inst.text.status, "generated")
    
    def testSchedule2(self):
        inst = self.instantiate_from("schedule-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Schedule instance")
        self.implSchedule2(inst)
        
        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule2(inst2)
    
    def implSchedule2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.comment, "The slots attached to this schedule should be specialized to cover immunizations within the clinic")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org/scheduleid")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "45")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.planningHorizon.end.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "General Practice")
        self.assertEqual(inst.serviceType[0].coding[0].code, "57")
        self.assertEqual(inst.serviceType[0].coding[0].display, "Immunization")
        self.assertEqual(inst.specialty[0].coding[0].code, "408480009")
        self.assertEqual(inst.specialty[0].coding[0].display, "Clinical immunology")
        self.assertEqual(inst.text.status, "generated")
    
    def testSchedule3(self):
        inst = self.instantiate_from("schedule-provider-location2-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Schedule instance")
        self.implSchedule3(inst)
        
        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule3(inst2)
    
    def implSchedule3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.comment, "The slots attached to this schedule are for neurosurgery operations at Starfleet HQ only.")
        self.assertEqual(inst.id, "exampleloc2")
        self.assertEqual(inst.identifier[0].system, "http://example.org/scheduleid")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "47")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.planningHorizon.end.date, FHIRDate("2017-12-25T09:30:00Z").date)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2017-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.date, FHIRDate("2017-12-25T09:15:00Z").date)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2017-12-25T09:15:00Z")
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "31")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "Specialist Surgical")
        self.assertEqual(inst.serviceType[0].coding[0].code, "221")
        self.assertEqual(inst.serviceType[0].coding[0].display, "Surgery - General")
        self.assertEqual(inst.specialty[0].coding[0].code, "394610002")
        self.assertEqual(inst.specialty[0].coding[0].display, "Surgery-Neurosurgery")
        self.assertEqual(inst.text.status, "generated")

