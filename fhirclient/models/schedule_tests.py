#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import schedule
from fhirdate import FHIRDate


class ScheduleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = schedule.Schedule(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testSchedule1(self):
        inst = self.instantiate_from("schedule-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e391cd0> instance")
    
        self.assertEqual(inst.comment, "Assessments should be performed before requesting appointments in this slot.")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.planningHorizon.end.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.planningHorizon.end.isostring, "2013-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.planningHorizon.start.isostring, "2013-12-25T09:15:00Z")
        self.assertEqual(inst.text.div, "<div>\n      Burgers UMC, South Wing, second floor Physiotherapy Schedule\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "45")
        self.assertEqual(inst.type[0].coding[0].display, "Physiotherapy")

