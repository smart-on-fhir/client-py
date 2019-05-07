#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import operationoutcome
from .fhirdate import FHIRDate


class OperationOutcomeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OperationOutcome", js["resourceType"])
        return operationoutcome.OperationOutcome(js)
    
    def testOperationOutcome1(self):
        inst = self.instantiate_from("operationoutcome-example-validationfail.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome1(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome1(inst2)
    
    def implOperationOutcome1(self, inst):
        self.assertEqual(inst.id, "validationfail")
        self.assertEqual(inst.issue[0].code, "structure")
        self.assertEqual(inst.issue[0].details.text, "Error parsing resource XML (Unknown Content \"label\"")
        self.assertEqual(inst.issue[0].expression[0], "Patient.identifier")
        self.assertEqual(inst.issue[0].location[0], "/f:Patient/f:identifier")
        self.assertEqual(inst.issue[0].severity, "error")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testOperationOutcome2(self):
        inst = self.instantiate_from("operationoutcome-example-break-the-glass.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome2(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome2(inst2)
    
    def implOperationOutcome2(self, inst):
        self.assertEqual(inst.id, "break-the-glass")
        self.assertEqual(inst.issue[0].code, "suppressed")
        self.assertEqual(inst.issue[0].details.coding[0].code, "ETREAT")
        self.assertEqual(inst.issue[0].details.coding[0].display, "Emergency Treatment")
        self.assertEqual(inst.issue[0].details.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.issue[0].details.text, "Additional information may be available using the Break-The-Glass Protocol")
        self.assertEqual(inst.issue[0].severity, "information")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testOperationOutcome3(self):
        inst = self.instantiate_from("operationoutcome-example-searchfail.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome3(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome3(inst2)
    
    def implOperationOutcome3(self, inst):
        self.assertEqual(inst.id, "searchfail")
        self.assertEqual(inst.issue[0].code, "code-invalid")
        self.assertEqual(inst.issue[0].details.text, "The \"name\" parameter has the modifier \"exact\" which is not supported by this server")
        self.assertEqual(inst.issue[0].location[0], "http.name:exact")
        self.assertEqual(inst.issue[0].severity, "fatal")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testOperationOutcome4(self):
        inst = self.instantiate_from("operationoutcome-example-exception.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome4(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome4(inst2)
    
    def implOperationOutcome4(self, inst):
        self.assertEqual(inst.id, "exception")
        self.assertEqual(inst.issue[0].code, "exception")
        self.assertEqual(inst.issue[0].details.text, "SQL Link Communication Error (dbx = 34234)")
        self.assertEqual(inst.issue[0].severity, "error")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testOperationOutcome5(self):
        inst = self.instantiate_from("operationoutcome-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome5(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome5(inst2)
    
    def implOperationOutcome5(self, inst):
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.issue[0].code, "code-invalid")
        self.assertEqual(inst.issue[0].details.text, "The code \"W\" is not known and not legal in this context")
        self.assertEqual(inst.issue[0].diagnostics, "Acme.Interop.FHIRProcessors.Patient.processGender line 2453")
        self.assertEqual(inst.issue[0].expression[0], "Patient.gender")
        self.assertEqual(inst.issue[0].location[0], "/f:Patient/f:gender")
        self.assertEqual(inst.issue[0].severity, "error")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testOperationOutcome6(self):
        inst = self.instantiate_from("operationoutcome-example-allok.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome6(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome6(inst2)
    
    def implOperationOutcome6(self, inst):
        self.assertEqual(inst.id, "allok")
        self.assertEqual(inst.issue[0].code, "informational")
        self.assertEqual(inst.issue[0].details.text, "All OK")
        self.assertEqual(inst.issue[0].severity, "information")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")

