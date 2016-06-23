#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import enrollmentresponse
from .fhirdate import FHIRDate


class EnrollmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EnrollmentResponse", js["resourceType"])
        return enrollmentresponse.EnrollmentResponse(js)
    
    def testEnrollmentResponse1(self):
        inst = self.instantiate_from("enrollmentresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EnrollmentResponse instance")
        self.implEnrollmentResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("EnrollmentResponse", js["resourceType"])
        inst2 = enrollmentresponse.EnrollmentResponse(js)
        self.implEnrollmentResponse1(inst2)
    
    def implEnrollmentResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Dependant added to policy.")
        self.assertEqual(inst.id, "ER2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/enrollmentresponse")
        self.assertEqual(inst.identifier[0].value, "781234")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the EnrollmentResponse</div>")
        self.assertEqual(inst.text.status, "generated")

