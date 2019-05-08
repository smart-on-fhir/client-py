#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import immunizationevaluation
from .fhirdate import FHIRDate


class ImmunizationEvaluationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImmunizationEvaluation", js["resourceType"])
        return immunizationevaluation.ImmunizationEvaluation(js)
    
    def testImmunizationEvaluation1(self):
        inst = self.instantiate_from("immunizationevaluation-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImmunizationEvaluation instance")
        self.implImmunizationEvaluation1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImmunizationEvaluation", js["resourceType"])
        inst2 = immunizationevaluation.ImmunizationEvaluation(js)
        self.implImmunizationEvaluation1(inst2)
    
    def implImmunizationEvaluation1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(inst.doseNumberPositiveInt, 1)
        self.assertEqual(inst.doseStatus.coding[0].code, "valid")
        self.assertEqual(inst.doseStatus.coding[0].display, "Valid")
        self.assertEqual(inst.doseStatus.coding[0].system, "http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.series, "Vaccination Series 1")
        self.assertEqual(inst.seriesDosesPositiveInt, 3)
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.targetDisease.coding[0].code, "1857005")
        self.assertEqual(inst.targetDisease.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testImmunizationEvaluation2(self):
        inst = self.instantiate_from("immunizationevaluation-example-notvalid.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImmunizationEvaluation instance")
        self.implImmunizationEvaluation2(inst)
        
        js = inst.as_json()
        self.assertEqual("ImmunizationEvaluation", js["resourceType"])
        inst2 = immunizationevaluation.ImmunizationEvaluation(js)
        self.implImmunizationEvaluation2(inst2)
    
    def implImmunizationEvaluation2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(inst.doseNumberPositiveInt, 2)
        self.assertEqual(inst.doseStatus.coding[0].code, "notvalid")
        self.assertEqual(inst.doseStatus.coding[0].display, "Not Valid")
        self.assertEqual(inst.doseStatus.coding[0].system, "http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status")
        self.assertEqual(inst.doseStatusReason[0].coding[0].code, "outsidesched")
        self.assertEqual(inst.doseStatusReason[0].coding[0].display, "Administered outside recommended schedule")
        self.assertEqual(inst.doseStatusReason[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status-reason")
        self.assertEqual(inst.id, "notValid")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.series, "Vaccination Series 1")
        self.assertEqual(inst.seriesDosesPositiveInt, 3)
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.targetDisease.coding[0].code, "1857005")
        self.assertEqual(inst.targetDisease.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")

