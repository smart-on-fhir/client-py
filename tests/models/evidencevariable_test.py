#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import evidencevariable
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class EvidenceVariableTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EvidenceVariable", js["resourceType"])
        return evidencevariable.EvidenceVariable(js)
    
    def testEvidenceVariable1(self):
        inst = self.instantiate_from("evidencevariable-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EvidenceVariable instance")
        self.implEvidenceVariable1(inst)
        
        js = inst.as_json()
        self.assertEqual("EvidenceVariable", js["resourceType"])
        inst2 = evidencevariable.EvidenceVariable(js)
        self.implEvidenceVariable1(inst2)
    
    def implEvidenceVariable1(self, inst):
        self.assertEqual(inst.characteristic[0].definitionCodeableConcept.text, "Diabetic patients over 65")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

