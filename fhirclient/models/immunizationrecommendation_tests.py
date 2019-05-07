#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import immunizationrecommendation
from .fhirdate import FHIRDate


class ImmunizationRecommendationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImmunizationRecommendation", js["resourceType"])
        return immunizationrecommendation.ImmunizationRecommendation(js)
    
    def testImmunizationRecommendation1(self):
        inst = self.instantiate_from("immunizationrecommendation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImmunizationRecommendation instance")
        self.implImmunizationRecommendation1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImmunizationRecommendation", js["resourceType"])
        inst2 = immunizationrecommendation.ImmunizationRecommendation(js)
        self.implImmunizationRecommendation1(inst2)
    
    def implImmunizationRecommendation1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2015-02-09T11:04:15.817-05:00").date)
        self.assertEqual(inst.date.as_json(), "2015-02-09T11:04:15.817-05:00")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1235")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].code.coding[0].code, "earliest")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].code.coding[0].display, "Earliest Date")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].code.coding[0].system, "http://example.org/fhir/CodeSystem/immunization-recommendation-date-criterion")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].value.date, FHIRDate("2015-12-01T00:00:00-05:00").date)
        self.assertEqual(inst.recommendation[0].dateCriterion[0].value.as_json(), "2015-12-01T00:00:00-05:00")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].code.coding[0].code, "recommended")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].code.coding[0].display, "Recommended")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].code.coding[0].system, "http://example.org/fhir/CodeSystem/immunization-recommendation-date-criterion")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].value.date, FHIRDate("2015-12-01T00:00:00-05:00").date)
        self.assertEqual(inst.recommendation[0].dateCriterion[1].value.as_json(), "2015-12-01T00:00:00-05:00")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].code.coding[0].code, "overdue")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].code.coding[0].display, "Past Due Date")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].code.coding[0].system, "http://example.org/fhir/CodeSystem/immunization-recommendation-date-criterion")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].value.date, FHIRDate("2016-12-28T00:00:00-05:00").date)
        self.assertEqual(inst.recommendation[0].dateCriterion[2].value.as_json(), "2016-12-28T00:00:00-05:00")
        self.assertEqual(inst.recommendation[0].description, "First sequence in protocol")
        self.assertEqual(inst.recommendation[0].doseNumberPositiveInt, 1)
        self.assertEqual(inst.recommendation[0].forecastStatus.text, "Not Complete")
        self.assertEqual(inst.recommendation[0].series, "Vaccination Series 1")
        self.assertEqual(inst.recommendation[0].seriesDosesPositiveInt, 3)
        self.assertEqual(inst.recommendation[0].vaccineCode[0].coding[0].code, "14745005")
        self.assertEqual(inst.recommendation[0].vaccineCode[0].coding[0].display, "Hepatitis A vaccine")
        self.assertEqual(inst.recommendation[0].vaccineCode[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Authored by Joginder Madra</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testImmunizationRecommendation2(self):
        inst = self.instantiate_from("immunizationrecommendation-example-target-disease.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImmunizationRecommendation instance")
        self.implImmunizationRecommendation2(inst)
        
        js = inst.as_json()
        self.assertEqual("ImmunizationRecommendation", js["resourceType"])
        inst2 = immunizationrecommendation.ImmunizationRecommendation(js)
        self.implImmunizationRecommendation2(inst2)
    
    def implImmunizationRecommendation2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2015-02-09T11:04:15.817-05:00").date)
        self.assertEqual(inst.date.as_json(), "2015-02-09T11:04:15.817-05:00")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1235")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].code.coding[0].code, "30981-5")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].code.coding[0].display, "Earliest date to give")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].value.date, FHIRDate("2015-12-01T00:00:00-05:00").date)
        self.assertEqual(inst.recommendation[0].dateCriterion[0].value.as_json(), "2015-12-01T00:00:00-05:00")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].code.coding[0].code, "recommended")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].code.coding[0].display, "Recommended")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].code.coding[0].system, "http://example.org/fhir/CodeSystem/immunization-recommendation-date-criterion")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].value.date, FHIRDate("2015-12-01T00:00:00-05:00").date)
        self.assertEqual(inst.recommendation[0].dateCriterion[1].value.as_json(), "2015-12-01T00:00:00-05:00")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].code.coding[0].code, "overdue")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].code.coding[0].display, "Past Due Date")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].code.coding[0].system, "http://example.org/fhir/CodeSystem/immunization-recommendation-date-criterion")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].value.date, FHIRDate("2016-12-28T00:00:00-05:00").date)
        self.assertEqual(inst.recommendation[0].dateCriterion[2].value.as_json(), "2016-12-28T00:00:00-05:00")
        self.assertEqual(inst.recommendation[0].description, "First sequence in protocol")
        self.assertEqual(inst.recommendation[0].doseNumberPositiveInt, 1)
        self.assertEqual(inst.recommendation[0].forecastStatus.text, "Not Complete")
        self.assertEqual(inst.recommendation[0].series, "Vaccination Series 1")
        self.assertEqual(inst.recommendation[0].seriesDosesPositiveInt, 3)
        self.assertEqual(inst.recommendation[0].targetDisease.coding[0].code, "40468003")
        self.assertEqual(inst.recommendation[0].targetDisease.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Authored by Joginder Madra</div>")
        self.assertEqual(inst.text.status, "generated")

