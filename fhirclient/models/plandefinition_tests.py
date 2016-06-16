#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8522 on 2016-06-16.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import plandefinition
from .fhirdate import FHIRDate


class PlanDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PlanDefinition", js["resourceType"])
        return plandefinition.PlanDefinition(js)
    
    def testPlanDefinition1(self):
        inst = self.instantiate_from("plandefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PlanDefinition instance")
        self.implPlanDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("PlanDefinition", js["resourceType"])
        inst2 = plandefinition.PlanDefinition(js)
        self.implPlanDefinition1(inst2)
    
    def implPlanDefinition1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Low Suicide Risk Order Set...</div>")
        self.assertEqual(inst.text.status, "generated")

