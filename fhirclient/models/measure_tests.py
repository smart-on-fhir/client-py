#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11466 on 2017-02-27.
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
        self.assertEqual(inst.description, "Percentage of children 3-18 years of age who were diagnosed with pharyngitis, ordered an antibiotic and received a group A streptococcus (strep) test for the episode.")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.group[0].identifier.value, "CMS146-group-1")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code, "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria, "CMS146.InInitialPopulation")
        self.assertEqual(inst.group[0].population[0].identifier.value, "initial-population-identifier")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code, "numerator")
        self.assertEqual(inst.group[0].population[1].criteria, "CMS146.InNumerator")
        self.assertEqual(inst.group[0].population[1].identifier.value, "numerator-identifier")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code, "denominator")
        self.assertEqual(inst.group[0].population[2].criteria, "CMS146.InDenominator")
        self.assertEqual(inst.group[0].population[2].identifier.value, "denominator-identifier")
        self.assertEqual(inst.group[0].population[3].code.coding[0].code, "denominator-exclusion")
        self.assertEqual(inst.group[0].population[3].criteria, "CMS146.InDenominatorExclusions")
        self.assertEqual(inst.group[0].population[3].identifier.value, "denominator-exclusions-identifier")
        self.assertEqual(inst.group[0].stratifier[0].criteria, "CMS146.AgesUpToNine")
        self.assertEqual(inst.group[0].stratifier[0].identifier.value, "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[1].criteria, "CMS146.AgesTenPlus")
        self.assertEqual(inst.group[0].stratifier[1].identifier.value, "stratifier-ages-10-plus")
        self.assertEqual(inst.group[0].stratifier[2].identifier.value, "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[2].path, "Patient.gender")
        self.assertEqual(inst.guidance, "This is an episode of care measure that examines all eligible episodes for the patient during the measurement period. If the patient has more than one episode, include all episodes in the measure")
        self.assertEqual(inst.id, "measure-cms146-example")
        self.assertEqual(inst.identifier[0].system, "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/cms")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "146")
        self.assertEqual(inst.identifier[1].system, "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/nqf")
        self.assertEqual(inst.identifier[1].use, "official")
        self.assertEqual(inst.identifier[1].value, "0002")
        self.assertEqual(inst.improvementNotation, "Higher score indicates better quality")
        self.assertEqual(inst.purpose, "Measure of children with a group A streptococcus test in the 7-day period from 3 days prior through 3 days after the diagnosis of pharyngitis")
        self.assertEqual(inst.relatedArtifact[0].citation, "Linder, J.A., D.W. Bates, G.M. Lee, J.A. Finkelstein. 2005. \"Antibiotic treatment of children with sore throat.\" JAMA 294(18):2315-2322. ")
        self.assertEqual(inst.relatedArtifact[0].type, "documentation")
        self.assertEqual(inst.relatedArtifact[1].citation, "Infectious Diseases Society of America. 2012. \"Clinical Practice Guideline for the Diagnosis and Management of Group A Streptococcal Pharyngitis: 2012 Update.\" ")
        self.assertEqual(inst.relatedArtifact[1].type, "documentation")
        self.assertEqual(inst.relatedArtifact[2].type, "documentation")
        self.assertEqual(inst.scoring.coding[0].code, "proportion")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.supplementalData[0].identifier.value, "supplemental-data-gender")
        self.assertEqual(inst.supplementalData[0].path, "Patient.gender")
        self.assertEqual(inst.supplementalData[1].identifier.value, "supplemental-data-deceased")
        self.assertEqual(inst.supplementalData[1].path, "deceasedBoolean")
        self.assertEqual(inst.text.status, "additional")
        self.assertEqual(inst.title, "Appropriate Testing for Children with Pharyngitis")
        self.assertEqual(inst.topic[0].coding[0].code, "57024-2")
        self.assertEqual(inst.topic[0].coding[0].system, "http://hl7.org/fhir/c80-doc-typecodes")
        self.assertEqual(inst.type[0].coding[0].code, "process")
        self.assertEqual(inst.version, "1.0.0")

