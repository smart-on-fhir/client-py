#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import researchelementdefinition
from .fhirdate import FHIRDate


class ResearchElementDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ResearchElementDefinition", js["resourceType"])
        return researchelementdefinition.ResearchElementDefinition(js)
    
    def testResearchElementDefinition1(self):
        inst = self.instantiate_from("researchelementdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ResearchElementDefinition instance")
        self.implResearchElementDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ResearchElementDefinition", js["resourceType"])
        inst2 = researchelementdefinition.ResearchElementDefinition(js)
        self.implResearchElementDefinition1(inst2)
    
    def implResearchElementDefinition1(self, inst):
        self.assertEqual(inst.characteristic[0].definitionCodeableConcept.text, "Diabetic patients over 65")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "population")

