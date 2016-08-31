#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 on 2016-08-31.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import eligibilityresponse
from .fhirdate import FHIRDate


class EligibilityResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EligibilityResponse", js["resourceType"])
        return eligibilityresponse.EligibilityResponse(js)
    
    def testEligibilityResponse1(self):
        inst = self.instantiate_from("eligibilityresponse-example-benefits.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse1(inst2)
    
    def implEligibilityResponse1(self, inst):
        self.assertEqual(inst.benefitBalance[0].category.code, "medical")
        self.assertEqual(inst.benefitBalance[0].category.system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.benefitBalance[0].financial[0].benefitMoney.code, "SAR")
        self.assertEqual(inst.benefitBalance[0].financial[0].benefitMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.benefitBalance[0].financial[0].benefitMoney.value, 500000)
        self.assertEqual(inst.benefitBalance[0].financial[0].type.code, "benefit")
        self.assertEqual(inst.benefitBalance[0].financial[1].benefitMoney.code, "SAR")
        self.assertEqual(inst.benefitBalance[0].financial[1].benefitMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.benefitBalance[0].financial[1].benefitMoney.value, 100)
        self.assertEqual(inst.benefitBalance[0].financial[1].type.code, "copay-maximum")
        self.assertEqual(inst.benefitBalance[0].financial[2].benefitUnsignedInt, 20)
        self.assertEqual(inst.benefitBalance[0].financial[2].type.code, "copay-percent")
        self.assertEqual(inst.benefitBalance[0].network.code, "in")
        self.assertEqual(inst.benefitBalance[0].network.system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.benefitBalance[0].subCategory.code, "30")
        self.assertEqual(inst.benefitBalance[0].subCategory.display, "Health Benefit Plan Coverage")
        self.assertEqual(inst.benefitBalance[0].subCategory.system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.benefitBalance[0].term.code, "annual")
        self.assertEqual(inst.benefitBalance[0].term.system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.benefitBalance[0].unit.code, "individual")
        self.assertEqual(inst.benefitBalance[0].unit.system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.benefitBalance[1].category.code, "medical")
        self.assertEqual(inst.benefitBalance[1].category.system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.benefitBalance[1].financial[0].benefitMoney.code, "SAR")
        self.assertEqual(inst.benefitBalance[1].financial[0].benefitMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.benefitBalance[1].financial[0].benefitMoney.value, 15000)
        self.assertEqual(inst.benefitBalance[1].financial[0].type.code, "benefit")
        self.assertEqual(inst.benefitBalance[1].network.code, "in")
        self.assertEqual(inst.benefitBalance[1].network.system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.benefitBalance[1].subCategory.code, "69")
        self.assertEqual(inst.benefitBalance[1].subCategory.display, "Maternity")
        self.assertEqual(inst.benefitBalance[1].subCategory.system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.benefitBalance[1].term.code, "annual")
        self.assertEqual(inst.benefitBalance[1].term.system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.benefitBalance[1].unit.code, "individual")
        self.assertEqual(inst.benefitBalance[1].unit.system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.benefitBalance[2].category.code, "oral")
        self.assertEqual(inst.benefitBalance[2].category.system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.benefitBalance[2].financial[0].benefitMoney.code, "SAR")
        self.assertEqual(inst.benefitBalance[2].financial[0].benefitMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.benefitBalance[2].financial[0].benefitMoney.value, 2000)
        self.assertEqual(inst.benefitBalance[2].financial[0].type.code, "benefit")
        self.assertEqual(inst.benefitBalance[2].network.code, "in")
        self.assertEqual(inst.benefitBalance[2].network.system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.benefitBalance[2].subCategory.code, "F3")
        self.assertEqual(inst.benefitBalance[2].subCategory.display, "Dental Coverage")
        self.assertEqual(inst.benefitBalance[2].subCategory.system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.benefitBalance[2].term.code, "annual")
        self.assertEqual(inst.benefitBalance[2].term.system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.benefitBalance[2].unit.code, "individual")
        self.assertEqual(inst.benefitBalance[2].unit.system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.benefitBalance[3].category.code, "vision")
        self.assertEqual(inst.benefitBalance[3].category.system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.benefitBalance[3].financial[0].benefitMoney.code, "SAR")
        self.assertEqual(inst.benefitBalance[3].financial[0].benefitMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.benefitBalance[3].financial[0].benefitMoney.value, 400)
        self.assertEqual(inst.benefitBalance[3].financial[0].type.code, "benefit")
        self.assertEqual(inst.benefitBalance[3].network.code, "in")
        self.assertEqual(inst.benefitBalance[3].network.system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.benefitBalance[3].subCategory.code, "F6")
        self.assertEqual(inst.benefitBalance[3].subCategory.display, "Vision Coverage")
        self.assertEqual(inst.benefitBalance[3].subCategory.system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.benefitBalance[3].term.code, "annual")
        self.assertEqual(inst.benefitBalance[3].term.system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.benefitBalance[3].unit.code, "individual")
        self.assertEqual(inst.benefitBalance[3].unit.system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.benefitBalance[4].category.code, "vision")
        self.assertEqual(inst.benefitBalance[4].category.system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.benefitBalance[4].financial[0].benefitString, "shared")
        self.assertEqual(inst.benefitBalance[4].financial[0].type.code, "room")
        self.assertEqual(inst.benefitBalance[4].financial[1].benefitMoney.code, "SAR")
        self.assertEqual(inst.benefitBalance[4].financial[1].benefitMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.benefitBalance[4].financial[1].benefitMoney.value, 600)
        self.assertEqual(inst.benefitBalance[4].financial[1].type.code, "benefit")
        self.assertEqual(inst.benefitBalance[4].network.code, "in")
        self.assertEqual(inst.benefitBalance[4].network.system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.benefitBalance[4].subCategory.code, "49")
        self.assertEqual(inst.benefitBalance[4].subCategory.display, "Hospital Room and Board")
        self.assertEqual(inst.benefitBalance[4].subCategory.system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.benefitBalance[4].term.code, "day")
        self.assertEqual(inst.benefitBalance[4].term.system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.benefitBalance[4].unit.code, "individual")
        self.assertEqual(inst.benefitBalance[4].unit.system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/eligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertTrue(inst.inforce)
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testEligibilityResponse2(self):
        inst = self.instantiate_from("eligibilityresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse2(inst2)
    
    def implEligibilityResponse2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/eligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertTrue(inst.inforce)
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")

