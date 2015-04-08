#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import coverage
from fhirdate import FHIRDate


class CoverageTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = coverage.Coverage(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testCoverage1(self):
        inst = self.instantiate_from("coverage-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2c05d0> instance")
    
        self.assertEqual(inst.dependent, 1)
        self.assertEqual(inst.id, "7546D")
        self.assertEqual(inst.identifier[0].system, "http://xyz.com/codes/identifier")
        self.assertEqual(inst.identifier[0].value, "AB9876")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-17").date)
        self.assertEqual(inst.period.end.isostring, "2012-03-17")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-03-17").date)
        self.assertEqual(inst.period.start.isostring, "2011-03-17")
        self.assertEqual(inst.plan, "11024")
        self.assertEqual(inst.subPlan, "D15C9")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the coverage</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "EHCPOL")
        self.assertEqual(inst.type.display, "extended healthcare")
        self.assertEqual(inst.type.system, "http://hl7.org/fhir/v3/ActCode")
    
    def testCoverage2(self):
        inst = self.instantiate_from("coverage-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2c05d0> instance")
    
        self.assertEqual(inst.dependent, 1)
        self.assertEqual(inst.id, "9876B1")
        self.assertEqual(inst.identifier[0].system, "http://benefitsinc.com/certificate")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-05-23").date)
        self.assertEqual(inst.period.end.isostring, "2012-05-23")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-05-23").date)
        self.assertEqual(inst.period.start.isostring, "2011-05-23")
        self.assertEqual(inst.plan, "CBI35")
        self.assertEqual(inst.sequence, 1)
        self.assertEqual(inst.subPlan, "123")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the coverage</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.code, "EHCPOL")
        self.assertEqual(inst.type.display, "extended healthcare")
        self.assertEqual(inst.type.system, "http://hl7.org/fhir/v3/ActCode")

