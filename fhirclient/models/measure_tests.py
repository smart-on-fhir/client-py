#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11157 on 2017-02-14.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import measure
from .fhirdate import FHIRDate


class MeasureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Measure", js["resourceType"])
        return measure.Measure(js)
    
    def testMeasure1(self):
        inst = self.instantiate_from("measure-cms146-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure1(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure1(inst2)
    
    def implMeasure1(self, inst):
        self.assertEqual(inst.description, "Percentage of children 2-18 years of age who were diagnosed with pharyngitis, ordered an antibiotic and received a group A streptococcus (strep) test for the episode.")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.group[0].identifier.value, "CMS146-group-1")
        self.assertEqual(inst.group[0].population[0].criteria, "CMS146.InInitialPopulation")
        self.assertEqual(inst.group[0].population[0].identifier.value, "initial-population-identifier")
        self.assertEqual(inst.group[0].population[0].type, "initial-population")
        self.assertEqual(inst.group[0].population[1].criteria, "CMS146.InNumerator")
        self.assertEqual(inst.group[0].population[1].identifier.value, "numerator-identifier")
        self.assertEqual(inst.group[0].population[1].type, "numerator")
        self.assertEqual(inst.group[0].population[2].criteria, "CMS146.InDenominator")
        self.assertEqual(inst.group[0].population[2].identifier.value, "denominator-identifier")
        self.assertEqual(inst.group[0].population[2].type, "denominator")
        self.assertEqual(inst.group[0].population[3].criteria, "CMS146.InDenominatorExclusions")
        self.assertEqual(inst.group[0].population[3].identifier.value, "denominator-exclusions-identifier")
        self.assertEqual(inst.group[0].population[3].type, "denominator-exclusion")
        self.assertEqual(inst.group[0].stratifier[0].criteria, "CMS146.AgesUpToNine")
        self.assertEqual(inst.group[0].stratifier[0].identifier.value, "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[1].criteria, "CMS146.AgesTenPlus")
        self.assertEqual(inst.group[0].stratifier[1].identifier.value, "stratifier-ages-10-plus")
        self.assertEqual(inst.group[0].stratifier[2].identifier.value, "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[2].path, "Patient.gender")
        self.assertEqual(inst.id, "measure-cms146-example")
        self.assertEqual(inst.identifier[0].system, "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/cms")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "146")
        self.assertEqual(inst.identifier[1].system, "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/nqf")
        self.assertEqual(inst.identifier[1].use, "official")
        self.assertEqual(inst.identifier[1].value, "0002")
        self.assertEqual(inst.scoring, "proportion")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.supplementalData[0].identifier.value, "supplemental-data-gender")
        self.assertEqual(inst.supplementalData[0].path, "Patient.gender")
        self.assertEqual(inst.supplementalData[1].identifier.value, "supplemental-data-deceased")
        self.assertEqual(inst.supplementalData[1].path, "deceasedBoolean")
        self.assertEqual(inst.text.status, "additional")
        self.assertEqual(inst.title, "Appropriate Testing for Children with Pharyngitis")
        self.assertEqual(inst.topic[0].coding[0].code, "57024-2")
        self.assertEqual(inst.topic[0].coding[0].system, "http://hl7.org/fhir/c80-doc-typecodes")
        self.assertEqual(inst.type[0], "process")
        self.assertEqual(inst.version, "1.0.0")

