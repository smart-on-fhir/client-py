#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


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
        inst = self.instantiate_from("schedule-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Schedule instance")
        self.implSchedule1(inst)
        
        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule1(inst2)
    
    def implSchedule1(self, inst):
        self.assertEqual(inst.comment, "Assessments should be performed before requesting appointments in this slot.")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org/scheduleid")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "45")
        self.assertEqual(inst.planningHorizon.end.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "45")
        self.assertEqual(inst.type[0].coding[0].display, "Physiotherapy")

