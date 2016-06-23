#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import processresponse
from .fhirdate import FHIRDate


class ProcessResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ProcessResponse", js["resourceType"])
        return processresponse.ProcessResponse(js)
    
    def testProcessResponse1(self):
        inst = self.instantiate_from("processresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessResponse instance")
        self.implProcessResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessResponse", js["resourceType"])
        inst2 = processresponse.ProcessResponse(js)
        self.implProcessResponse1(inst2)
    
    def implProcessResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Specified coverage is currently in-force.")
        self.assertEqual(inst.id, "SR2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/processresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertEqual(inst.outcome.code, "complete")
        self.assertEqual(inst.outcome.system, "http://hl7.org/fhir/processoutcomecodes")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the ProcessResponse</div>")
        self.assertEqual(inst.text.status, "generated")

