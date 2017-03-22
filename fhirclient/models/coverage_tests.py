#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import coverage
from .fhirdate import FHIRDate


class CoverageTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Coverage", js["resourceType"])
        return coverage.Coverage(js)
    
    def testCoverage1(self):
        inst = self.instantiate_from("coverage-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage1(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage1(inst2)
    
    def implCoverage1(self, inst):
        self.assertEqual(inst.dependent, "1")
        self.assertEqual(inst.grouping.group, "WESTAIR")
        self.assertEqual(inst.grouping.groupDisplay, "Western Airlines")
        self.assertEqual(inst.grouping.plan, "WESTAIR")
        self.assertEqual(inst.grouping.planDisplay, "Western Airlines")
        self.assertEqual(inst.grouping.subPlan, "D15C9")
        self.assertEqual(inst.grouping.subPlanDisplay, "Platinum")
        self.assertEqual(inst.id, "7546D")
        self.assertEqual(inst.identifier[0].system, "http://xyz.com/codes/identifier")
        self.assertEqual(inst.identifier[0].value, "AB98761")
        self.assertEqual(inst.network, "5")
        self.assertEqual(inst.order, 2)
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-17").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-03-17").date)
        self.assertEqual(inst.period.start.as_json(), "2011-03-17")
        self.assertEqual(inst.relationship.coding[0].code, "self")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.subscriberId, "AB9876")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "EHCPOL")
        self.assertEqual(inst.type.coding[0].display, "extended healthcare")
        self.assertEqual(inst.type.coding[0].system, "http://hl7.org/fhir/v3/ActCode")
    
    def testCoverage2(self):
        inst = self.instantiate_from("coverage-example-ehic.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage2(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage2(inst2)
    
    def implCoverage2(self, inst):
        self.assertEqual(inst.id, "7547E")
        self.assertEqual(inst.identifier[0].system, "http://ehic.com/insurer/123456789/member")
        self.assertEqual(inst.identifier[0].value, "A123456780")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-17").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(inst.relationship.coding[0].code, "self")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the European Health Insurance Card</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "EHCPOL")
        self.assertEqual(inst.type.coding[0].display, "extended healthcare")
        self.assertEqual(inst.type.coding[0].system, "http://hl7.org/fhir/v3/ActCode")
    
    def testCoverage3(self):
        inst = self.instantiate_from("coverage-example-selfpay.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage3(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage3(inst2)
    
    def implCoverage3(self, inst):
        self.assertEqual(inst.id, "SP1234")
        self.assertEqual(inst.identifier[0].system, "http://hospitalx.com/selfpayagreement")
        self.assertEqual(inst.identifier[0].value, "SP12345678")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-17").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(inst.relationship.coding[0].code, "self")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of a Self Pay Agreement.</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "pay")
        self.assertEqual(inst.type.coding[0].display, "PAY")
        self.assertEqual(inst.type.coding[0].system, "http://hl7.org/fhir/coverage-selfpay")
    
    def testCoverage4(self):
        inst = self.instantiate_from("coverage-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage4(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage4(inst2)
    
    def implCoverage4(self, inst):
        self.assertEqual(inst.dependent, "0")
        self.assertEqual(inst.grouping.classDisplay, "Silver: Family Plan spouse only")
        self.assertEqual(inst.grouping.class_fhir, "SILVER")
        self.assertEqual(inst.grouping.group, "CBI35")
        self.assertEqual(inst.grouping.groupDisplay, "Corporate Baker's Inc. Local #35")
        self.assertEqual(inst.grouping.plan, "B37FC")
        self.assertEqual(inst.grouping.planDisplay, "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC")
        self.assertEqual(inst.grouping.subClass, "Tier2")
        self.assertEqual(inst.grouping.subClassDisplay, "Low deductable, max $20 copay")
        self.assertEqual(inst.grouping.subGroup, "123")
        self.assertEqual(inst.grouping.subGroupDisplay, "Trainee Part-time Benefits")
        self.assertEqual(inst.grouping.subPlan, "P7")
        self.assertEqual(inst.grouping.subPlanDisplay, "Includes afterlife benefits")
        self.assertEqual(inst.id, "9876B1")
        self.assertEqual(inst.identifier[0].system, "http://benefitsinc.com/certificate")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-05-23").date)
        self.assertEqual(inst.period.end.as_json(), "2012-05-23")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-05-23").date)
        self.assertEqual(inst.period.start.as_json(), "2011-05-23")
        self.assertEqual(inst.relationship.coding[0].code, "self")
        self.assertEqual(inst.sequence, "9")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "EHCPOL")
        self.assertEqual(inst.type.coding[0].display, "extended healthcare")
        self.assertEqual(inst.type.coding[0].system, "http://hl7.org/fhir/v3/ActCode")

