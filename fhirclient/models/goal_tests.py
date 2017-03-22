#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import goal
from .fhirdate import FHIRDate


class GoalTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Goal", js["resourceType"])
        return goal.Goal(js)
    
    def testGoal1(self):
        inst = self.instantiate_from("goal-example-stop-smoking.json")
        self.assertIsNotNone(inst, "Must have instantiated a Goal instance")
        self.implGoal1(inst)
        
        js = inst.as_json()
        self.assertEqual("Goal", js["resourceType"])
        inst2 = goal.Goal(js)
        self.implGoal1(inst2)
    
    def implGoal1(self, inst):
        self.assertEqual(inst.description.text, "Stop smoking")
        self.assertEqual(inst.id, "stop-smoking")
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.outcomeCode[0].coding[0].code, "8517006")
        self.assertEqual(inst.outcomeCode[0].coding[0].display, "Ex-smoker (finding)")
        self.assertEqual(inst.outcomeCode[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.outcomeCode[0].text, "Former smoker")
        self.assertEqual(inst.startDate.date, FHIRDate("2015-04-05").date)
        self.assertEqual(inst.startDate.as_json(), "2015-04-05")
        self.assertEqual(inst.status, "achieved")
        self.assertEqual(inst.text.status, "additional")
    
    def testGoal2(self):
        inst = self.instantiate_from("goal-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Goal instance")
        self.implGoal2(inst)
        
        js = inst.as_json()
        self.assertEqual("Goal", js["resourceType"])
        inst2 = goal.Goal(js)
        self.implGoal2(inst2)
    
    def implGoal2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "dietary")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/goal-category")
        self.assertEqual(inst.description.text, "Target weight is 160 to 180 lbs.")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.priority.coding[0].code, "high-priority")
        self.assertEqual(inst.priority.coding[0].display, "High Priority")
        self.assertEqual(inst.priority.coding[0].system, "http://hl7.org/fhir/goal-priority")
        self.assertEqual(inst.priority.text, "high")
        self.assertEqual(inst.startDate.date, FHIRDate("2015-04-05").date)
        self.assertEqual(inst.startDate.as_json(), "2015-04-05")
        self.assertEqual(inst.status, "on-hold")
        self.assertEqual(inst.statusDate.date, FHIRDate("2016-02-14").date)
        self.assertEqual(inst.statusDate.as_json(), "2016-02-14")
        self.assertEqual(inst.statusReason, "Patient wants to defer weight loss until after honeymoon.")
        self.assertEqual(inst.target.detailRange.high.code, "[lb_av]")
        self.assertEqual(inst.target.detailRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.target.detailRange.high.unit, "lbs")
        self.assertEqual(inst.target.detailRange.high.value, 180)
        self.assertEqual(inst.target.detailRange.low.code, "[lb_av]")
        self.assertEqual(inst.target.detailRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.target.detailRange.low.unit, "lbs")
        self.assertEqual(inst.target.detailRange.low.value, 160)
        self.assertEqual(inst.target.dueDate.date, FHIRDate("2016-04-05").date)
        self.assertEqual(inst.target.dueDate.as_json(), "2016-04-05")
        self.assertEqual(inst.target.measure.coding[0].code, "3141-9")
        self.assertEqual(inst.target.measure.coding[0].display, "Weight Measured")
        self.assertEqual(inst.target.measure.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.text.status, "additional")

