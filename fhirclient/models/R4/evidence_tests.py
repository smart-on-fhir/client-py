#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-10-12.
#  2019, SMART Health IT.

from __future__ import unicode_literals
import os
import io
import unittest
import json
from . import evidence
from .fhirdate import FHIRDate


class EvidenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Evidence", js["resourceType"])
        return evidence.Evidence(js)
    
    def testEvidence1(self):
        inst = self.instantiate_from("evidence-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Evidence instance")
        self.implEvidence1(inst)
        
        js = inst.as_json()
        self.assertEqual("Evidence", js["resourceType"])
        inst2 = evidence.Evidence(js)
        self.implEvidence1(inst2)
    
    def implEvidence1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

