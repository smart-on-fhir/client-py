#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        self.assertEqual(inst.identifier[0].system, "http://example.org")
        self.assertEqual(inst.identifier[0].value, "guidanceResponse1")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.moduleUri, "http://someguidelineprovider.org/radiology-appropriateness-guidelines.html")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2017-03-10T16:02:00Z").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2017-03-10T16:02:00Z")
        self.assertEqual(inst.reasonCode[0].text, "Guideline Appropriate Ordering Assessment")
        self.assertEqual(inst.requestIdentifier.system, "http://example.org")
        self.assertEqual(inst.requestIdentifier.value, "guidanceRequest1")
        self.assertEqual(inst.status, "success")
        self.assertEqual(inst.text.status, "generated")

