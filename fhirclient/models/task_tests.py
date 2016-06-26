#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8595 on 2016-06-26.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import task
from .fhirdate import FHIRDate


class TaskTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Task", js["resourceType"])
        return task.Task(js)
    
    def testTask1(self):
        inst = self.instantiate_from("task-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Task instance")
        self.implTask1(inst)
        
        js = inst.as_json()
        self.assertEqual("Task", js["resourceType"])
        inst2 = task.Task(js)
        self.implTask1(inst2)
    
    def implTask1(self, inst):
        self.assertEqual(inst.code.text, "Refill Request")
        self.assertEqual(inst.created.date, FHIRDate("2016-03-10T22:39:32-04:00").date)
        self.assertEqual(inst.created.as_json(), "2016-03-10T22:39:32-04:00")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.lastModified.date, FHIRDate("2016-03-10T22:39:32-04:00").date)
        self.assertEqual(inst.lastModified.as_json(), "2016-03-10T22:39:32-04:00")
        self.assertEqual(inst.stage.coding[0].code, "actionable")
        self.assertEqual(inst.stage.coding[0].system, "http://hl7.org/fhir/task-stage")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")

