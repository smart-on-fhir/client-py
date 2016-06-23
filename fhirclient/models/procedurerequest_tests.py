#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import procedurerequest
from .fhirdate import FHIRDate


class ProcedureRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ProcedureRequest", js["resourceType"])
        return procedurerequest.ProcedureRequest(js)
    
    def testProcedureRequest1(self):
        inst = self.instantiate_from("procedurerequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest1(inst2)
    
    def implProcedureRequest1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "323418000")
        self.assertEqual(inst.code.coding[0].display, "Fix me up")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div>To be added</div>")
        self.assertEqual(inst.text.status, "generated")

