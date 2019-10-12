#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-10-12.
#  2019, SMART Health IT.

from __future__ import unicode_literals
import os
import io
import unittest
import json
from . import riskassessment
from .fhirdate import FHIRDate


class RiskAssessmentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("RiskAssessment", js["resourceType"])
        return riskassessment.RiskAssessment(js)
    
    def testRiskAssessment1(self):
        inst = self.instantiate_from("riskassessment-example-population.json")
        self.assertIsNotNone(inst, "Must have instantiated a RiskAssessment instance")
        self.implRiskAssessment1(inst)
        
        js = inst.as_json()
        self.assertEqual("RiskAssessment", js["resourceType"])
        inst2 = riskassessment.RiskAssessment(js)
        self.implRiskAssessment1(inst2)
    
    def implRiskAssessment1(self, inst):
        self.assertEqual(inst.id, "population")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testRiskAssessment2(self):
        inst = self.instantiate_from("riskassessment-example-cardiac.json")
        self.assertIsNotNone(inst, "Must have instantiated a RiskAssessment instance")
        self.implRiskAssessment2(inst)
        
        js = inst.as_json()
        self.assertEqual("RiskAssessment", js["resourceType"])
        inst2 = riskassessment.RiskAssessment(js)
        self.implRiskAssessment2(inst2)
    
    def implRiskAssessment2(self, inst):
        self.assertEqual(inst.id, "cardiac")
        self.assertEqual(inst.identifier.system, "http://example.org")
        self.assertEqual(inst.identifier.use, "official")
        self.assertEqual(inst.identifier.value, "risk-assessment-cardiac")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-07-19T16:04:00Z").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-07-19T16:04:00Z")
        self.assertEqual(inst.prediction[0].outcome.text, "Heart Attack")
        self.assertEqual(inst.prediction[0].probabilityDecimal, 0.02)
        self.assertEqual(inst.prediction[0].whenRange.high.code, "a")
        self.assertEqual(inst.prediction[0].whenRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[0].whenRange.high.unit, "years")
        self.assertEqual(inst.prediction[0].whenRange.high.value, 49)
        self.assertEqual(inst.prediction[0].whenRange.low.code, "a")
        self.assertEqual(inst.prediction[0].whenRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[0].whenRange.low.unit, "years")
        self.assertEqual(inst.prediction[0].whenRange.low.value, 39)
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "additional")
    
    def testRiskAssessment3(self):
        inst = self.instantiate_from("riskassessment-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RiskAssessment instance")
        self.implRiskAssessment3(inst)
        
        js = inst.as_json()
        self.assertEqual("RiskAssessment", js["resourceType"])
        inst2 = riskassessment.RiskAssessment(js)
        self.implRiskAssessment3(inst2)
    
    def implRiskAssessment3(self, inst):
        self.assertEqual(inst.comment, "High degree of certainty")
        self.assertEqual(inst.id, "genetic")
        self.assertEqual(inst.method.coding[0].code, "BRCAPRO")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2006-01-13T23:01:00Z").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2006-01-13T23:01:00Z")
        self.assertEqual(inst.prediction[0].outcome.text, "Breast Cancer")
        self.assertEqual(inst.prediction[0].probabilityDecimal, 0.000168)
        self.assertEqual(inst.prediction[0].whenRange.high.code, "a")
        self.assertEqual(inst.prediction[0].whenRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[0].whenRange.high.unit, "years")
        self.assertEqual(inst.prediction[0].whenRange.high.value, 53)
        self.assertEqual(inst.prediction[1].outcome.text, "Breast Cancer")
        self.assertEqual(inst.prediction[1].probabilityDecimal, 0.000368)
        self.assertEqual(inst.prediction[1].whenRange.high.code, "a")
        self.assertEqual(inst.prediction[1].whenRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[1].whenRange.high.unit, "years")
        self.assertEqual(inst.prediction[1].whenRange.high.value, 57)
        self.assertEqual(inst.prediction[1].whenRange.low.code, "a")
        self.assertEqual(inst.prediction[1].whenRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[1].whenRange.low.unit, "years")
        self.assertEqual(inst.prediction[1].whenRange.low.value, 54)
        self.assertEqual(inst.prediction[2].outcome.text, "Breast Cancer")
        self.assertEqual(inst.prediction[2].probabilityDecimal, 0.000594)
        self.assertEqual(inst.prediction[2].whenRange.high.code, "a")
        self.assertEqual(inst.prediction[2].whenRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[2].whenRange.high.unit, "years")
        self.assertEqual(inst.prediction[2].whenRange.high.value, 62)
        self.assertEqual(inst.prediction[2].whenRange.low.code, "a")
        self.assertEqual(inst.prediction[2].whenRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[2].whenRange.low.unit, "years")
        self.assertEqual(inst.prediction[2].whenRange.low.value, 58)
        self.assertEqual(inst.prediction[3].outcome.text, "Breast Cancer")
        self.assertEqual(inst.prediction[3].probabilityDecimal, 0.000838)
        self.assertEqual(inst.prediction[3].whenRange.high.code, "a")
        self.assertEqual(inst.prediction[3].whenRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[3].whenRange.high.unit, "years")
        self.assertEqual(inst.prediction[3].whenRange.high.value, 67)
        self.assertEqual(inst.prediction[3].whenRange.low.code, "a")
        self.assertEqual(inst.prediction[3].whenRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[3].whenRange.low.unit, "years")
        self.assertEqual(inst.prediction[3].whenRange.low.value, 63)
        self.assertEqual(inst.prediction[4].outcome.text, "Breast Cancer")
        self.assertEqual(inst.prediction[4].probabilityDecimal, 0.001089)
        self.assertEqual(inst.prediction[4].whenRange.high.code, "a")
        self.assertEqual(inst.prediction[4].whenRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[4].whenRange.high.unit, "years")
        self.assertEqual(inst.prediction[4].whenRange.high.value, 72)
        self.assertEqual(inst.prediction[4].whenRange.low.code, "a")
        self.assertEqual(inst.prediction[4].whenRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[4].whenRange.low.unit, "years")
        self.assertEqual(inst.prediction[4].whenRange.low.value, 68)
        self.assertEqual(inst.prediction[5].outcome.text, "Breast Cancer")
        self.assertEqual(inst.prediction[5].probabilityDecimal, 0.001327)
        self.assertEqual(inst.prediction[5].whenRange.high.code, "a")
        self.assertEqual(inst.prediction[5].whenRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[5].whenRange.high.unit, "years")
        self.assertEqual(inst.prediction[5].whenRange.high.value, 77)
        self.assertEqual(inst.prediction[5].whenRange.low.code, "a")
        self.assertEqual(inst.prediction[5].whenRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[5].whenRange.low.unit, "years")
        self.assertEqual(inst.prediction[5].whenRange.low.value, 73)
        self.assertEqual(inst.prediction[6].outcome.text, "Breast Cancer")
        self.assertEqual(inst.prediction[6].probabilityDecimal, 0.00153)
        self.assertEqual(inst.prediction[6].whenRange.high.code, "a")
        self.assertEqual(inst.prediction[6].whenRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[6].whenRange.high.unit, "years")
        self.assertEqual(inst.prediction[6].whenRange.high.value, 82)
        self.assertEqual(inst.prediction[6].whenRange.low.code, "a")
        self.assertEqual(inst.prediction[6].whenRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[6].whenRange.low.unit, "years")
        self.assertEqual(inst.prediction[6].whenRange.low.value, 78)
        self.assertEqual(inst.prediction[7].outcome.text, "Breast Cancer")
        self.assertEqual(inst.prediction[7].probabilityDecimal, 0.001663)
        self.assertEqual(inst.prediction[7].whenRange.high.code, "a")
        self.assertEqual(inst.prediction[7].whenRange.high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[7].whenRange.high.unit, "years")
        self.assertEqual(inst.prediction[7].whenRange.high.value, 88)
        self.assertEqual(inst.prediction[7].whenRange.low.code, "a")
        self.assertEqual(inst.prediction[7].whenRange.low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.prediction[7].whenRange.low.unit, "years")
        self.assertEqual(inst.prediction[7].whenRange.low.value, 83)
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testRiskAssessment4(self):
        inst = self.instantiate_from("riskassessment-example-prognosis.json")
        self.assertIsNotNone(inst, "Must have instantiated a RiskAssessment instance")
        self.implRiskAssessment4(inst)
        
        js = inst.as_json()
        self.assertEqual("RiskAssessment", js["resourceType"])
        inst2 = riskassessment.RiskAssessment(js)
        self.implRiskAssessment4(inst2)
    
    def implRiskAssessment4(self, inst):
        self.assertEqual(inst.id, "prognosis")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2010-11-22").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2010-11-22")
        self.assertEqual(inst.prediction[0].outcome.coding[0].code, "249943000:363698007=72098002,260868000=6934004")
        self.assertEqual(inst.prediction[0].outcome.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.prediction[0].outcome.text, "permanent weakness of the left arm")
        self.assertEqual(inst.prediction[0].qualitativeRisk.coding[0].code, "moderate")
        self.assertEqual(inst.prediction[0].qualitativeRisk.coding[0].display, "moderate likelihood")
        self.assertEqual(inst.prediction[0].qualitativeRisk.coding[0].system, "http://hl7.org/fhir/risk-probability")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "additional")

