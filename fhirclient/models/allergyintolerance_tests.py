#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import allergyintolerance
from .fhirdate import FHIRDate


class AllergyIntoleranceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AllergyIntolerance", js["resourceType"])
        return allergyintolerance.AllergyIntolerance(js)
    
    def testAllergyIntolerance1(self):
        inst = self.instantiate_from("allergyintolerance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AllergyIntolerance instance")
        self.implAllergyIntolerance1(inst)
        
        js = inst.as_json()
        self.assertEqual("AllergyIntolerance", js["resourceType"])
        inst2 = allergyintolerance.AllergyIntolerance(js)
        self.implAllergyIntolerance1(inst2)
    
    def implAllergyIntolerance1(self, inst):
        self.assertEqual(inst.category, "food")
        self.assertEqual(inst.criticality, "high")
        self.assertEqual(inst.event[0].description, "Challenge Protocol. Severe Reaction to 1/8 cashew. Epinephrine administered")
        self.assertEqual(inst.event[0].manifestation[0].coding[0].code, "39579001")
        self.assertEqual(inst.event[0].manifestation[0].coding[0].display, "Anaphylactic reaction")
        self.assertEqual(inst.event[0].manifestation[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event[0].onset.date, FHIRDate("2012-06-12").date)
        self.assertEqual(inst.event[0].onset.as_json(), "2012-06-12")
        self.assertEqual(inst.event[0].severity, "severe")
        self.assertEqual(inst.event[0].substance.coding[0].code, "C3214954")
        self.assertEqual(inst.event[0].substance.coding[0].display, "cashew nut allergenic extract Injectable Product")
        self.assertEqual(inst.event[0].substance.coding[0].system, "http://www.nlm.nih.gov/research/umls/rxnorm")
        self.assertEqual(inst.event[1].certainty, "likely")
        self.assertEqual(inst.event[1].manifestation[0].coding[0].code, "64305001")
        self.assertEqual(inst.event[1].manifestation[0].coding[0].display, "Urticaria")
        self.assertEqual(inst.event[1].manifestation[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event[1].onset.date, FHIRDate("2004").date)
        self.assertEqual(inst.event[1].onset.as_json(), "2004")
        self.assertEqual(inst.event[1].severity, "moderate")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier[0].value, "49476534")
        self.assertEqual(inst.lastOccurence.date, FHIRDate("2012-06").date)
        self.assertEqual(inst.lastOccurence.as_json(), "2012-06")
        self.assertEqual(inst.recordedDate.date, FHIRDate("2014-10-09T14:58:00+11:00").date)
        self.assertEqual(inst.recordedDate.as_json(), "2014-10-09T14:58:00+11:00")
        self.assertEqual(inst.status, "confirmed")
        self.assertEqual(inst.substance.coding[0].code, "227493005")
        self.assertEqual(inst.substance.coding[0].display, "Cashew nuts")
        self.assertEqual(inst.substance.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "immune")
    
    def testAllergyIntolerance2(self):
        inst = self.instantiate_from("allergyintolerance-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AllergyIntolerance instance")
        self.implAllergyIntolerance2(inst)
        
        js = inst.as_json()
        self.assertEqual("AllergyIntolerance", js["resourceType"])
        inst2 = allergyintolerance.AllergyIntolerance(js)
        self.implAllergyIntolerance2(inst2)
    
    def implAllergyIntolerance2(self, inst):
        self.assertEqual(inst.category, "food")
        self.assertEqual(inst.criticality, "high")
        self.assertEqual(inst.event[0].certainty, "confirmed")
        self.assertEqual(inst.event[0].description, "Challenge Protocol. Severe Reaction to 1/8 cashew. Epinephrine administered")
        self.assertEqual(inst.event[0].manifestation[0].coding[0].code, "39579001")
        self.assertEqual(inst.event[0].manifestation[0].coding[0].display, "Anaphylactic reaction")
        self.assertEqual(inst.event[0].manifestation[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event[0].onset.date, FHIRDate("2012-06-12").date)
        self.assertEqual(inst.event[0].onset.as_json(), "2012-06-12")
        self.assertEqual(inst.event[0].severity, "severe")
        self.assertEqual(inst.event[0].substance.coding[0].code, "C3214954")
        self.assertEqual(inst.event[0].substance.coding[0].display, "cashew nut allergenic extract Injectable Product")
        self.assertEqual(inst.event[0].substance.coding[0].system, "http://www.nlm.nih.gov/research/umls/rxnorm")
        self.assertEqual(inst.event[1].certainty, "likely")
        self.assertEqual(inst.event[1].manifestation[0].coding[0].code, "64305001")
        self.assertEqual(inst.event[1].manifestation[0].coding[0].display, "Urticaria")
        self.assertEqual(inst.event[1].manifestation[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event[1].onset.date, FHIRDate("2004").date)
        self.assertEqual(inst.event[1].onset.as_json(), "2004")
        self.assertEqual(inst.event[1].severity, "moderate")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/allergyintolerance-reasonRefuted")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "MED")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "Medical Status Altered")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier[0].value, "49476534")
        self.assertEqual(inst.lastOccurence.date, FHIRDate("2012-06").date)
        self.assertEqual(inst.lastOccurence.as_json(), "2012-06")
        self.assertEqual(inst.recordedDate.date, FHIRDate("2014-10-09T14:58:00+11:00").date)
        self.assertEqual(inst.recordedDate.as_json(), "2014-10-09T14:58:00+11:00")
        self.assertEqual(inst.status, "confirmed")
        self.assertEqual(inst.substance.coding[0].code, "227493005")
        self.assertEqual(inst.substance.coding[0].display, "Cashew nuts")
        self.assertEqual(inst.substance.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "immune")

