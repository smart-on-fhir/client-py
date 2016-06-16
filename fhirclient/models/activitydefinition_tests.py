#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8522 on 2016-06-16.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import activitydefinition
from .fhirdate import FHIRDate


class ActivityDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ActivityDefinition", js["resourceType"])
        return activitydefinition.ActivityDefinition(js)
    
    def testActivityDefinition1(self):
        inst = self.instantiate_from("activitydefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition1(inst2)
    
    def implActivityDefinition1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Referral definition</div>")
        self.assertEqual(inst.text.status, "generated")

