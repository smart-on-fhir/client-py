#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        inst = self.instantiate_from("goal-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Goal instance")
        self.implGoal1(inst)
        
        js = inst.as_json()
        self.assertEqual("Goal", js["resourceType"])
        inst2 = goal.Goal(js)
        self.implGoal1(inst2)
    
    def implGoal1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "dietary")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/goal-category")
        self.assertEqual(inst.description.text, "Target weight is 160 to 180 lbs.")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.lifecycleStatus, "on-hold")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code, "high-priority")
        self.assertEqual(inst.priority.coding[0].display, "High Priority")
        self.assertEqual(inst.priority.coding[0].system, "http://terminology.hl7.org/CodeSystem/goal-priority")
        self.assertEqual(inst.priority.text, "high")
        self.assertEqual(inst.startDate.date, FHIRDate("2015-04-05").date)
        self.assertEqual(inst.startDate.as_json(), "2015-04-05")
        self.assertEqual(inst.statusDate.date, FHIRDate("2016-02-14").date)
        self.assertEqual(inst.statusDate.as_json(), "2016-02-14")
        self.assertEqual(inst.statusReason, "Patient wants to defer weight loss until after honeymoon.")
        self.assertEqual(inst.target[0].detailRange.high.code, "[lb_av]")
        self.assertEqual(inst.target[0].detailRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.target[0].detailRange.high.unit, "lbs")
        self.assertEqual(inst.target[0].detailRange.high.value, 180)
        self.assertEqual(inst.target[0].detailRange.low.code, "[lb_av]")
        self.assertEqual(inst.target[0].detailRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.target[0].detailRange.low.unit, "lbs")
        self.assertEqual(inst.target[0].detailRange.low.value, 160)
        self.assertEqual(inst.target[0].dueDate.date, FHIRDate("2016-04-05").date)
        self.assertEqual(inst.target[0].dueDate.as_json(), "2016-04-05")
        self.assertEqual(inst.target[0].measure.coding[0].code, "3141-9")
        self.assertEqual(inst.target[0].measure.coding[0].display, "Weight Measured")
        self.assertEqual(inst.target[0].measure.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.text.status, "additional")
    
    def testGoal2(self):
        inst = self.instantiate_from("goal-example-stop-smoking.json")
        self.assertIsNotNone(inst, "Must have instantiated a Goal instance")
        self.implGoal2(inst)
        
        js = inst.as_json()
        self.assertEqual("Goal", js["resourceType"])
        inst2 = goal.Goal(js)
        self.implGoal2(inst2)
    
    def implGoal2(self, inst):
        self.assertEqual(inst.achievementStatus.coding[0].code, "achieved")
        self.assertEqual(inst.achievementStatus.coding[0].display, "Achieved")
        self.assertEqual(inst.achievementStatus.coding[0].system, "http://terminology.hl7.org/CodeSystem/goal-achievement")
        self.assertEqual(inst.achievementStatus.text, "Achieved")
        self.assertEqual(inst.description.text, "Stop smoking")
        self.assertEqual(inst.id, "stop-smoking")
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.lifecycleStatus, "completed")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcomeCode[0].coding[0].code, "8517006")
        self.assertEqual(inst.outcomeCode[0].coding[0].display, "Ex-smoker (finding)")
        self.assertEqual(inst.outcomeCode[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.outcomeCode[0].text, "Former smoker")
        self.assertEqual(inst.startDate.date, FHIRDate("2015-04-05").date)
        self.assertEqual(inst.startDate.as_json(), "2015-04-05")
        self.assertEqual(inst.text.status, "additional")

