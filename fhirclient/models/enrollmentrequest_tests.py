#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import enrollmentrequest
from .fhirdate import FHIRDate


class EnrollmentRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EnrollmentRequest", js["resourceType"])
        return enrollmentrequest.EnrollmentRequest(js)
    
    def testEnrollmentRequest1(self):
        inst = self.instantiate_from("enrollmentrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EnrollmentRequest instance")
        self.implEnrollmentRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("EnrollmentRequest", js["resourceType"])
        inst2 = enrollmentrequest.EnrollmentRequest(js)
        self.implEnrollmentRequest1(inst2)
    
    def implEnrollmentRequest1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "22345")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/enrollmentrequest")
        self.assertEqual(inst.identifier[0].value, "EN22345")
        self.assertEqual(inst.relationship.code, "spouse")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the EnrollmentRequest.</div>")
        self.assertEqual(inst.text.status, "generated")

