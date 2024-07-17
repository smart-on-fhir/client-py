#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import detectedissue
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class DetectedIssueTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DetectedIssue", js["resourceType"])
        return detectedissue.DetectedIssue(js)
    
    def testDetectedIssue1(self):
        inst = self.instantiate_from("detectedissue-example-lab.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue1(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue1(inst2)
    
    def implDetectedIssue1(self, inst):
        self.assertEqual(inst.id, "lab")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testDetectedIssue2(self):
        inst = self.instantiate_from("detectedissue-example-allergy.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue2(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue2(inst2)
    
    def implDetectedIssue2(self, inst):
        self.assertEqual(inst.id, "allergy")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testDetectedIssue3(self):
        inst = self.instantiate_from("detectedissue-example-dup.json")
        self.assertIsNotNone(inst, "Must have instantiated a DetectedIssue instance")
        self.implDetectedIssue3(inst)
        
        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue3(inst2)
    
    def implDetectedIssue3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "DUPTHPY")
        self.assertEqual(inst.code.coding[0].display, "Duplicate Therapy Alert")
        self.assertEqual(inst.code.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.detail, "Similar test was performed within the past 14 days")
        self.assertEqual(inst.id, "duplicate")
        self.assertEqual(inst.identifiedDateTime.datetime, FHIRDateTime("2013-05-08").datetime)
        self.assertEqual(inst.identifiedDateTime.as_json(), "2013-05-08")
        self.assertEqual(inst.identifier[0].system, "http://example.org")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.reference, "http://www.tmhp.com/RadiologyClinicalDecisionSupport/2011/CHEST%20IMAGING%20GUIDELINES%202011.pdf")
        self.assertEqual(inst.status, "final")
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
        self.assertEqual(inst.code.coding[0].code, "DRG")
        self.assertEqual(inst.code.coding[0].display, "Drug Interaction Alert")
        self.assertEqual(inst.code.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.id, "ddi")
        self.assertEqual(inst.identifiedDateTime.datetime, FHIRDateTime("2014-01-05").datetime)
        self.assertEqual(inst.identifiedDateTime.as_json(), "2014-01-05")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mitigation[0].action.coding[0].code, "13")
        self.assertEqual(inst.mitigation[0].action.coding[0].display, "Stopped Concurrent Therapy")
        self.assertEqual(inst.mitigation[0].action.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.mitigation[0].action.text, "Asked patient to discontinue regular use of Tylenol and to consult with clinician if they need to resume to allow appropriate INR monitoring")
        self.assertEqual(inst.mitigation[0].date.datetime, FHIRDateTime("2014-01-05").datetime)
        self.assertEqual(inst.mitigation[0].date.as_json(), "2014-01-05")
        self.assertEqual(inst.severity, "high")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")

