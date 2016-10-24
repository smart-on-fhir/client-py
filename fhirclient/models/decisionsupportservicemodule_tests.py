#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10061 on 2016-10-24.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import decisionsupportservicemodule
from .fhirdate import FHIRDate


class DecisionSupportServiceModuleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DecisionSupportServiceModule", js["resourceType"])
        return decisionsupportservicemodule.DecisionSupportServiceModule(js)
    
    def testDecisionSupportServiceModule1(self):
        inst = self.instantiate_from("decisionsupportservicemodule-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DecisionSupportServiceModule instance")
        self.implDecisionSupportServiceModule1(inst)
        
        js = inst.as_json()
        self.assertEqual("DecisionSupportServiceModule", js["resourceType"])
        inst2 = decisionsupportservicemodule.DecisionSupportServiceModule(js)
        self.implDecisionSupportServiceModule1(inst2)
    
    def implDecisionSupportServiceModule1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(inst.description, "Guideline appropriate ordering is used to assess appropriateness of an order given a patient, a proposed order, and a set of clinical indications.")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "guildeline-appropriate-ordering")
        self.assertEqual(inst.parameter[0].name, "patient")
        self.assertEqual(inst.parameter[0].type, "Patient")
        self.assertEqual(inst.parameter[0].use, "in")
        self.assertEqual(inst.parameter[1].name, "order")
        self.assertEqual(inst.parameter[1].type, "Task")
        self.assertEqual(inst.parameter[1].use, "in")
        self.assertEqual(inst.parameter[2].name, "order")
        self.assertEqual(inst.parameter[2].type, "Task")
        self.assertEqual(inst.parameter[2].use, "out")
        self.assertEqual(inst.parameter[3].name, "result")
        self.assertEqual(inst.parameter[3].type, "Basic")
        self.assertEqual(inst.parameter[3].use, "out")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Guideline Appropriate Ordering Module</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Guideline Appropriate Ordering Module")
        self.assertEqual(inst.topic[0].text, "Guideline Appropriate Ordering")
        self.assertEqual(inst.topic[1].text, "Appropriate Use Criteria")
        self.assertEqual(inst.version, "1.0.0")

