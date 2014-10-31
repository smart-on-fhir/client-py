#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from allergyintolerance import AllergyIntolerance
from fhirdate import FHIRDate


class AllergyIntoleranceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = AllergyIntolerance(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testAllergyIntolerance1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/allergyintolerance-example-dust-f201.json")
        self.assertIsNotNone(inst, "Must have instantiated a AllergyIntolerance instance")
    
        self.assertEqual(inst.criticality, "medium")
        self.assertEqual(inst.identifier[0].label, "House dust allergy")
        self.assertEqual(inst.identifier[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.identifier[0].value, "232349006")
        self.assertEqual(inst.recordedDate.date, FHIRDate("2013-01-28").date)
        self.assertEqual(inst.recordedDate.isostring, "2013-01-28")
        self.assertEqual(inst.recorder.reference, "Practitioner/f201")
        self.assertEqual(inst.sensitivityType, "allergy")
        self.assertEqual(inst.status, "confirmed")
        self.assertEqual(inst.subject.display, "Roel")
        self.assertEqual(inst.subject.reference, "Patient/f201")
        self.assertEqual(inst.substance.display, "House dust allergen")
        self.assertEqual(inst.substance.reference, "Substance/f201")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>identifier</b>: House dust allergy = 232349006\n      </p>\n      <p>\n        <b>criticality</b>: medium\n      </p>\n      <p>\n        <b>sensitivityType</b>: allergy\n      </p>\n      <p>\n        <b>recordedDate</b>: 28-Jan 2013\n      </p>\n      <p>\n        <b>status</b>: confirmed\n      </p>\n      <p>\n        <b>subject</b>: Roel\n      </p>\n      <p>\n        <b>recorder</b>: \n        <a href=\"practitioner-example-f201-ab.html\">UZI-nummer = 12345678901 (official); Dokter Bronsig(official); Male; birthDate: 24-Dec 1956; Implementation of planned interventions; Medical oncologist</a>\n      </p>\n      <p>\n        <b>substance</b>: House dust allergen\n      </p>\n    </div>")
        self.assertEqual(inst.text.status, "generated")

