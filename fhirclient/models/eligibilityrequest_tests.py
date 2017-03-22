#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import eligibilityrequest
from .fhirdate import FHIRDate


class EligibilityRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EligibilityRequest", js["resourceType"])
        return eligibilityrequest.EligibilityRequest(js)
    
    def testEligibilityRequest1(self):
        inst = self.instantiate_from("eligibilityrequest-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityRequest instance")
        self.implEligibilityRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityRequest", js["resourceType"])
        inst2 = eligibilityrequest.EligibilityRequest(js)
        self.implEligibilityRequest1(inst2)
    
    def implEligibilityRequest1(self, inst):
        self.assertEqual(inst.benefitCategory.coding[0].code, "medical")
        self.assertEqual(inst.benefitCategory.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.benefitSubCategory.coding[0].code, "69")
        self.assertEqual(inst.benefitSubCategory.coding[0].display, "Maternity")
        self.assertEqual(inst.benefitSubCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.businessArrangement, "NB8742")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "52346")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/elegibilityrequest")
        self.assertEqual(inst.identifier[0].value, "52346")
        self.assertEqual(inst.priority.coding[0].code, "normal")
        self.assertEqual(inst.servicedDate.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.servicedDate.as_json(), "2014-09-17")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityRequest</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testEligibilityRequest2(self):
        inst = self.instantiate_from("eligibilityrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityRequest instance")
        self.implEligibilityRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityRequest", js["resourceType"])
        inst2 = eligibilityrequest.EligibilityRequest(js)
        self.implEligibilityRequest2(inst2)
    
    def implEligibilityRequest2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "52345")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/elegibilityrequest")
        self.assertEqual(inst.identifier[0].value, "52345")
        self.assertEqual(inst.priority.coding[0].code, "normal")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityRequest</div>")
        self.assertEqual(inst.text.status, "generated")

