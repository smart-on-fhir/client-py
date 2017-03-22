#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import guidanceresponse
from .fhirdate import FHIRDate


class GuidanceResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("GuidanceResponse", js["resourceType"])
        return guidanceresponse.GuidanceResponse(js)
    
    def testGuidanceResponse1(self):
        inst = self.instantiate_from("guidanceresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a GuidanceResponse instance")
        self.implGuidanceResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("GuidanceResponse", js["resourceType"])
        inst2 = guidanceresponse.GuidanceResponse(js)
        self.implGuidanceResponse1(inst2)
    
    def implGuidanceResponse1(self, inst):
        self.assertEqual(inst.contained[0].id, "outputParameters1")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://example.org")
        self.assertEqual(inst.identifier.value, "guidanceResponse1")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2017-03-10T16:02:00Z").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2017-03-10T16:02:00Z")
        self.assertEqual(inst.reasonCodeableConcept.text, "Guideline Appropriate Ordering Assessment")
        self.assertEqual(inst.requestId, "guidanceRequest1")
        self.assertEqual(inst.status, "success")
        self.assertEqual(inst.text.status, "generated")

