#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import coverageeligibilityrequest
from .fhirdate import FHIRDate


class CoverageEligibilityRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CoverageEligibilityRequest", js["resourceType"])
        return coverageeligibilityrequest.CoverageEligibilityRequest(js)
    
    def testCoverageEligibilityRequest1(self):
        inst = self.instantiate_from("coverageeligibilityrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityRequest instance")
        self.implCoverageEligibilityRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityRequest", js["resourceType"])
        inst2 = coverageeligibilityrequest.CoverageEligibilityRequest(js)
        self.implCoverageEligibilityRequest1(inst2)
    
    def implCoverageEligibilityRequest1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "52345")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/coverageelegibilityrequest")
        self.assertEqual(inst.identifier[0].value, "52345")
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code, "normal")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityRequest</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCoverageEligibilityRequest2(self):
        inst = self.instantiate_from("coverageeligibilityrequest-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityRequest instance")
        self.implCoverageEligibilityRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityRequest", js["resourceType"])
        inst2 = coverageeligibilityrequest.CoverageEligibilityRequest(js)
        self.implCoverageEligibilityRequest2(inst2)
    
    def implCoverageEligibilityRequest2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "52346")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/coverageelegibilityrequest")
        self.assertEqual(inst.identifier[0].value, "52346")
        self.assertEqual(inst.insurance[0].businessArrangement, "NB8742")
        self.assertEqual(inst.item[0].category.coding[0].code, "69")
        self.assertEqual(inst.item[0].category.coding[0].display, "Maternity")
        self.assertEqual(inst.item[0].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code, "normal")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.purpose[1], "benefits")
        self.assertEqual(inst.servicedDate.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.servicedDate.as_json(), "2014-09-17")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityRequest</div>")
        self.assertEqual(inst.text.status, "generated")

