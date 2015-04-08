#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import enrollmentrequest
from fhirdate import FHIRDate


class EnrollmentRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = enrollmentrequest.EnrollmentRequest(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testEnrollmentRequest1(self):
        inst = self.instantiate_from("enrollmentrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2ee490> instance")
    
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.isostring, "2014-08-16")
        self.assertEqual(inst.id, "22345")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/enrollmentrequest")
        self.assertEqual(inst.identifier[0].value, "EN22345")
        self.assertEqual(inst.relationship.code, "spouse")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the EnrollmentRequest.</div>")
        self.assertEqual(inst.text.status, "generated")

