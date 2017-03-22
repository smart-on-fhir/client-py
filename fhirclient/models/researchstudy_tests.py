#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import researchstudy
from .fhirdate import FHIRDate


class ResearchStudyTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ResearchStudy", js["resourceType"])
        return researchstudy.ResearchStudy(js)
    
    def testResearchStudy1(self):
        inst = self.instantiate_from("researchstudy-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ResearchStudy instance")
        self.implResearchStudy1(inst)
        
        js = inst.as_json()
        self.assertEqual("ResearchStudy", js["resourceType"])
        inst2 = researchstudy.ResearchStudy(js)
        self.implResearchStudy1(inst2)
    
    def implResearchStudy1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

