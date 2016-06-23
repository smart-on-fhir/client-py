#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import detectedissue
from .fhirdate import FHIRDate


class DetectedIssueTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DetectedIssue", js["resourceType"])
        return detectedissue.DetectedIssue(js)
    
    def testDetectedIssue1(self):
        inst = self.instantiate_from("detectedissue-example-allergy.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue1(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue1(inst2)
    
    def implDetectedIssue1(self, inst):
        self.assertEqual(inst.id, "allergy")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testDetectedIssue2(self):
        inst = self.instantiate_from("detectedissue-example-dup.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue2(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue2(inst2)
    
    def implDetectedIssue2(self, inst):
        self.assertEqual(inst.category.coding[0].code, "DUPTHPY")
        self.assertEqual(inst.category.coding[0].display, "Duplicate Therapy Alert")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.date.date, FHIRDate("2013-05-08").date)
        self.assertEqual(inst.date.as_json(), "2013-05-08")
        self.assertEqual(inst.detail, "Similar test was performed within the past 14 days")
        self.assertEqual(inst.id, "duplicate")
        self.assertEqual(inst.text.status, "generated")
    
    def testDetectedIssue3(self):
        inst = self.instantiate_from("detectedissue-example-lab.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue3(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue3(inst2)
    
    def implDetectedIssue3(self, inst):
        self.assertEqual(inst.id, "lab")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testDetectedIssue4(self):
        inst = self.instantiate_from("detectedissue-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue4(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue4(inst2)
    
    def implDetectedIssue4(self, inst):
        self.assertEqual(inst.category.coding[0].code, "DRG")
        self.assertEqual(inst.category.coding[0].display, "Drug Interaction Alert")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.date.date, FHIRDate("2014-01-05").date)
        self.assertEqual(inst.date.as_json(), "2014-01-05")
        self.assertEqual(inst.id, "ddi")
        self.assertEqual(inst.mitigation[0].action.coding[0].code, "13")
        self.assertEqual(inst.mitigation[0].action.coding[0].display, "Stopped Concurrent Therapy")
        self.assertEqual(inst.mitigation[0].action.coding[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.mitigation[0].action.text, "Asked patient to discontinue regular use of Tylenol and to consult with clinician if they need to resume to allow appropriate INR monitoring")
        self.assertEqual(inst.mitigation[0].date.date, FHIRDate("2014-01-05").date)
        self.assertEqual(inst.mitigation[0].date.as_json(), "2014-01-05")
        self.assertEqual(inst.severity, "high")
        self.assertEqual(inst.text.status, "generated")

