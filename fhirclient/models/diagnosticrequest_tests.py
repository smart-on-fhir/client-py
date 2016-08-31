#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 on 2016-08-31.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import diagnosticrequest
from .fhirdate import FHIRDate


class DiagnosticRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DiagnosticRequest", js["resourceType"])
        return diagnosticrequest.DiagnosticRequest(js)
    
    def testDiagnosticRequest1(self):
        inst = self.instantiate_from("diagnosticrequest-example-di.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticRequest instance")
        self.implDiagnosticRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticRequest", js["resourceType"])
        inst2 = diagnosticrequest.DiagnosticRequest(js)
        self.implDiagnosticRequest1(inst2)
    
    def implDiagnosticRequest1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "24627-2")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Chest CT")
        self.assertEqual(inst.id, "di")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.reason[0].text, "Check for metastatic disease")
        self.assertEqual(inst.stage.coding[0].code, "original-order")
        self.assertEqual(inst.stage.coding[0].system, "http://hl7.org/fhir/request-stage")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticRequest2(self):
        inst = self.instantiate_from("diagnosticrequest-example-ft4.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticRequest instance")
        self.implDiagnosticRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticRequest", js["resourceType"])
        inst2 = diagnosticrequest.DiagnosticRequest(js)
        self.implDiagnosticRequest2(inst2)
    
    def implDiagnosticRequest2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "3024-7")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Free T4")
        self.assertEqual(inst.id, "ft4")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2015-08-27T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2015-08-27T09:33:27+07:00")
        self.assertEqual(inst.stage.coding[0].code, "reflex-order")
        self.assertEqual(inst.stage.coding[0].system, "http://hl7.org/fhir/request-stage")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticRequest3(self):
        inst = self.instantiate_from("diagnosticrequest-example-lipid.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticRequest instance")
        self.implDiagnosticRequest3(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticRequest", js["resourceType"])
        inst2 = diagnosticrequest.DiagnosticRequest(js)
        self.implDiagnosticRequest3(inst2)
    
    def implDiagnosticRequest3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "LIPID")
        self.assertEqual(inst.code.coding[0].system, "http://acme.org/tests")
        self.assertEqual(inst.code.text, "Lipid Panel")
        self.assertEqual(inst.contained[0].id, "fasting")
        self.assertEqual(inst.id, "lipid")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "PLAC")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "2345234234234")
        self.assertEqual(inst.note[0].text, "patient is afraid of needles")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-02T16:16:00-07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-02T16:16:00-07:00")
        self.assertEqual(inst.reason[0].coding[0].code, "V173")
        self.assertEqual(inst.reason[0].coding[0].display, "Fam hx-ischem heart dis")
        self.assertEqual(inst.reason[0].coding[0].system, "http://hl7.org/fhir/sid/icd-9")
        self.assertEqual(inst.stage.coding[0].code, "original-order")
        self.assertEqual(inst.stage.coding[0].system, "http://hl7.org/fhir/request-stage")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticRequest4(self):
        inst = self.instantiate_from("diagnosticrequest-genetics-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticRequest instance")
        self.implDiagnosticRequest4(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticRequest", js["resourceType"])
        inst2 = diagnosticrequest.DiagnosticRequest(js)
        self.implDiagnosticRequest4(inst2)
    
    def implDiagnosticRequest4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.id, "og-example1")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-05-12T16:16:00-07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-05-12T16:16:00-07:00")
        self.assertEqual(inst.stage.coding[0].code, "original-order")
        self.assertEqual(inst.stage.coding[0].system, "http://hl7.org/fhir/request-stage")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

