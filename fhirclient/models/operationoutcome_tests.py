#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


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
        inst = self.instantiate_from("operationoutcome-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationOutcome instance")
        self.implOperationOutcome1(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome1(inst2)
    
    def implOperationOutcome1(self, inst):
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.issue[0].code.coding[0].code, "code-unknown")
        self.assertEqual(inst.issue[0].code.coding[0].display, "Code Unknown")
        self.assertEqual(inst.issue[0].code.coding[0].system, "http://hl7.org/fhir/issue-type")
        self.assertEqual(inst.issue[0].code.text, "Unknown code")
        self.assertEqual(inst.issue[0].details, "The code \"W\" in the system \"http://acme.com/intranet/fhir/codesystems/gender\" is not known (source = Acme.Interop.FHIRProcessors.Patient.processGender)")
        self.assertEqual(inst.issue[0].location[0], "/Person[1]/gender[1]")
        self.assertEqual(inst.issue[0].severity, "error")
        self.assertEqual(inst.text.status, "additional")

