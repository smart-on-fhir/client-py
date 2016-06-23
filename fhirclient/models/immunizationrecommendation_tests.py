#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


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
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1235")
        self.assertEqual(inst.recommendation[0].date.date, FHIRDate("2015-02-09T11:04:15.817-05:00").date)
        self.assertEqual(inst.recommendation[0].date.as_json(), "2015-02-09T11:04:15.817-05:00")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].code.coding[0].code, "earliest")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].code.coding[0].display, "Earliest Date")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].code.coding[0].system, "http://hl7.org/fhir/immunization-recommendation-date-criterion")
        self.assertEqual(inst.recommendation[0].dateCriterion[0].value.date, FHIRDate("2015-12-01T00:00:00-05:00").date)
        self.assertEqual(inst.recommendation[0].dateCriterion[0].value.as_json(), "2015-12-01T00:00:00-05:00")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].code.coding[0].code, "recommended")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].code.coding[0].display, "Recommended")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].code.coding[0].system, "http://hl7.org/fhir/immunization-recommendation-date-criterion")
        self.assertEqual(inst.recommendation[0].dateCriterion[1].value.date, FHIRDate("2015-12-01T00:00:00-05:00").date)
        self.assertEqual(inst.recommendation[0].dateCriterion[1].value.as_json(), "2015-12-01T00:00:00-05:00")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].code.coding[0].code, "overdue")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].code.coding[0].display, "Past Due Date")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].code.coding[0].system, "http://hl7.org/fhir/immunization-recommendation-date-criterion")
        self.assertEqual(inst.recommendation[0].dateCriterion[2].value.date, FHIRDate("2016-12-28T00:00:00-05:00").date)
        self.assertEqual(inst.recommendation[0].dateCriterion[2].value.as_json(), "2016-12-28T00:00:00-05:00")
        self.assertEqual(inst.recommendation[0].doseNumber, 1)
        self.assertEqual(inst.recommendation[0].forecastStatus.coding[0].code, "Not Complete")
        self.assertEqual(inst.recommendation[0].forecastStatus.coding[0].display, "Not Complete")
        self.assertEqual(inst.recommendation[0].forecastStatus.coding[0].system, "http://hl7.org/fhir/immunization-recommendation-status")
        self.assertEqual(inst.recommendation[0].protocol.description, "First sequence in protocol")
        self.assertEqual(inst.recommendation[0].protocol.doseSequence, 1)
        self.assertEqual(inst.recommendation[0].protocol.series, "Vaccination Series 1")
        self.assertEqual(inst.recommendation[0].vaccineCode.coding[0].code, "14745005")
        self.assertEqual(inst.recommendation[0].vaccineCode.coding[0].display, "Hepatitis A vaccine")
        self.assertEqual(inst.recommendation[0].vaccineCode.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div>Authored by Joginder Madra</div>")
        self.assertEqual(inst.text.status, "generated")

