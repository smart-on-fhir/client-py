#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        self.assertEqual(inst.class_fhir[0].name, "Western Airlines")
        self.assertEqual(inst.class_fhir[0].type.coding[0].code, "group")
        self.assertEqual(inst.class_fhir[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[0].value, "WESTAIR")
        self.assertEqual(inst.class_fhir[1].name, "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC")
        self.assertEqual(inst.class_fhir[1].type.coding[0].code, "plan")
        self.assertEqual(inst.class_fhir[1].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[1].value, "BG4352")
        self.assertEqual(inst.class_fhir[2].name, "Platinum")
        self.assertEqual(inst.class_fhir[2].type.coding[0].code, "subplan")
        self.assertEqual(inst.class_fhir[2].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[2].value, "D15C9")
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.end.date, FHIRDate("2018-12-31").date)
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.end.as_json(), "2018-12-31")
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.start.date, FHIRDate("2018-01-01").date)
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.start.as_json(), "2018-01-01")
        self.assertEqual(inst.costToBeneficiary[0].exception[0].type.coding[0].code, "retired")
        self.assertEqual(inst.costToBeneficiary[0].exception[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception")
        self.assertEqual(inst.costToBeneficiary[0].type.coding[0].code, "gpvisit")
        self.assertEqual(inst.costToBeneficiary[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-copay-type")
        self.assertEqual(inst.costToBeneficiary[0].valueMoney.currency, "USD")
        self.assertEqual(inst.costToBeneficiary[0].valueMoney.value, 20.0)
        self.assertEqual(inst.dependent, "1")
        self.assertEqual(inst.id, "7546D")
        self.assertEqual(inst.identifier[0].system, "http://xyz.com/codes/identifier")
        self.assertEqual(inst.identifier[0].value, "AB98761")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
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
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
    
    def testCoverage2(self):
        inst = self.instantiate_from("coverage-example-selfpay.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage2(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage2(inst2)
    
    def implCoverage2(self, inst):
        self.assertEqual(inst.id, "SP1234")
        self.assertEqual(inst.identifier[0].system, "http://hospitalx.com/selfpayagreement")
        self.assertEqual(inst.identifier[0].value, "SP12345678")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-17").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(inst.relationship.coding[0].code, "self")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of a Self Pay Agreement.</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "pay")
        self.assertEqual(inst.type.coding[0].display, "PAY")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-selfpay")
    
    def testCoverage3(self):
        inst = self.instantiate_from("coverage-example-ehic.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage3(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage3(inst2)
    
    def implCoverage3(self, inst):
        self.assertEqual(inst.id, "7547E")
        self.assertEqual(inst.identifier[0].system, "http://ehic.com/insurer/123456789/member")
        self.assertEqual(inst.identifier[0].value, "A123456780")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-17").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(inst.relationship.coding[0].code, "self")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the European Health Insurance Card</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "EHCPOL")
        self.assertEqual(inst.type.coding[0].display, "extended healthcare")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
    
    def testCoverage4(self):
        inst = self.instantiate_from("coverage-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Coverage instance")
        self.implCoverage4(inst)
        
        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage4(inst2)
    
    def implCoverage4(self, inst):
        self.assertEqual(inst.class_fhir[0].name, "Corporate Baker's Inc. Local #35")
        self.assertEqual(inst.class_fhir[0].type.coding[0].code, "group")
        self.assertEqual(inst.class_fhir[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[0].value, "CB135")
        self.assertEqual(inst.class_fhir[1].name, "Trainee Part-time Benefits")
        self.assertEqual(inst.class_fhir[1].type.coding[0].code, "subgroup")
        self.assertEqual(inst.class_fhir[1].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[1].value, "123")
        self.assertEqual(inst.class_fhir[2].name, "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC")
        self.assertEqual(inst.class_fhir[2].type.coding[0].code, "plan")
        self.assertEqual(inst.class_fhir[2].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[2].value, "B37FC")
        self.assertEqual(inst.class_fhir[3].name, "Includes afterlife benefits")
        self.assertEqual(inst.class_fhir[3].type.coding[0].code, "subplan")
        self.assertEqual(inst.class_fhir[3].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[3].value, "P7")
        self.assertEqual(inst.class_fhir[4].name, "Silver: Family Plan spouse only")
        self.assertEqual(inst.class_fhir[4].type.coding[0].code, "class")
        self.assertEqual(inst.class_fhir[4].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[4].value, "SILVER")
        self.assertEqual(inst.class_fhir[5].name, "Low deductable, max $20 copay")
        self.assertEqual(inst.class_fhir[5].type.coding[0].code, "subclass")
        self.assertEqual(inst.class_fhir[5].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[5].value, "Tier2")
        self.assertEqual(inst.class_fhir[6].type.coding[0].code, "sequence")
        self.assertEqual(inst.class_fhir[6].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[6].value, "9")
        self.assertEqual(inst.class_fhir[7].type.coding[0].code, "rxid")
        self.assertEqual(inst.class_fhir[7].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[7].value, "MDF12345")
        self.assertEqual(inst.class_fhir[8].type.coding[0].code, "rxbin")
        self.assertEqual(inst.class_fhir[8].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[8].value, "987654")
        self.assertEqual(inst.class_fhir[9].type.coding[0].code, "rxgroup")
        self.assertEqual(inst.class_fhir[9].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[9].value, "M35PT")
        self.assertEqual(inst.dependent, "0")
        self.assertEqual(inst.id, "9876B1")
        self.assertEqual(inst.identifier[0].system, "http://benefitsinc.com/certificate")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-05-23").date)
        self.assertEqual(inst.period.end.as_json(), "2012-05-23")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-05-23").date)
        self.assertEqual(inst.period.start.as_json(), "2011-05-23")
        self.assertEqual(inst.relationship.coding[0].code, "self")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "EHCPOL")
        self.assertEqual(inst.type.coding[0].display, "extended healthcare")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")

