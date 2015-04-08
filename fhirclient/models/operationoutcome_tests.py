#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import operationoutcome
from fhirdate import FHIRDate


class OperationOutcomeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = operationoutcome.OperationOutcome(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testOperationOutcome1(self):
        inst = self.instantiate_from("operationoutcome-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e354e50> instance")
    
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.issue[0].code.coding[0].code, "code-unknown")
        self.assertEqual(inst.issue[0].code.coding[0].display, "Code Unknown")
        self.assertEqual(inst.issue[0].code.coding[0].system, "http://hl7.org/fhir/issue-type")
        self.assertEqual(inst.issue[0].code.text, "Unknown code")
        self.assertEqual(inst.issue[0].details, "The code \"W\" in the system \"http://acme.com/intranet/fhir/codesystems/gender\" is not known (source = Acme.Interop.FHIRProcessors.Patient.processGender)")
        self.assertEqual(inst.issue[0].location[0], "/Person[1]/gender[1]")
        self.assertEqual(inst.issue[0].severity, "error")
        self.assertEqual(inst.text.div, "<div>\n      \n      <p>W is not a recognized code for Gender.</p>\n    \n    </div>")
        self.assertEqual(inst.text.status, "additional")

