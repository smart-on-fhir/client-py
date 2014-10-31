#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from questionnaire import Questionnaire
from fhirdate import FHIRDate


class QuestionnaireTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = Questionnaire(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testQuestionnaire1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/questionnaire-example-bluebook.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
    
        self.assertEqual(inst.author.reference, "http://www.hl7.org/fhir/Practitioner/1")
        self.assertEqual(inst.authored.date, FHIRDate("2013-02-19T14:15:00").date)
        self.assertEqual(inst.authored.isostring, "2013-02-19T14:15:00")
        self.assertEqual(inst.group.name.text, "NSW Government My Personal Health Record, january 2013")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.subject.reference, "http://www.hl7.org/fhir/Patient/1")
        self.assertEqual(inst.text.div, "<div>\n      <pre>\n        Cathy Jones, female. Birth weight 3.25 kg at 44.3 cm. \n        Injection of Vitamin K given on 1972-11-30 (first dose) and 1972-12-11 (second dose)\n        Note: Was able to speak Chinese at birth.\n      </pre>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testQuestionnaire2(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/questionnaire-example-f201-lifelines.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
    
        self.assertEqual(inst.author.reference, "Practitioner/f201")
        self.assertEqual(inst.authored.date, FHIRDate("2013-06-18T00:00:00+01:00").date)
        self.assertEqual(inst.authored.isostring, "2013-06-18T00:00:00+01:00")
        self.assertEqual(inst.identifier[0].label, "Roel's VL 1-1, 18-65_1.2.2")
        self.assertEqual(inst.identifier[0].use, "temp")
        self.assertEqual(inst.name.coding[0].code, "VL 1-1, 18-65_1.2.2")
        self.assertEqual(inst.name.coding[0].display, "Lifelines Questionnaire 1 part 1")
        self.assertEqual(inst.name.coding[0].system, "https://lifelines.nl")
        self.assertEqual(inst.source.reference, "Practitioner/f201")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.subject.display, "Roel")
        self.assertEqual(inst.subject.reference, "Patient/f201")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>status</b>: completed\n      </p>\n      <p>\n        <b>authored</b>: 18-Jun 2013 0:0\n      </p>\n      <p>\n        <b>subject</b>: Roel\n      </p>\n      <p>\n        <b>author</b>: \n        <a href=\"practitioner-example-f201-ab.html\">UZI-nummer = 12345678901 (official); Dokter Bronsig(official); Male; birthDate: 24-Dec 1956; Implementation of planned interventions; Medical oncologist</a>\n      </p>\n      <p>\n        <b>source</b>: \n        <a href=\"practitioner-example-f201-ab.html\">UZI-nummer = 12345678901 (official); Dokter Bronsig(official); Male; birthDate: 24-Dec 1956; Implementation of planned interventions; Medical oncologist</a>\n      </p>\n      <p>\n        <b>name</b>: \n        <span title=\"Codes: {https://lifelines.nl VL 1-1, 18-65_1.2.2}\">Lifelines Questionnaire 1 part 1</span>\n      </p>\n      <p>\n        <b>identifier</b>: Roel's VL 1-1, 18-65_1.2.2 = ?? (temp)\n      </p>\n      <blockquote>\n        <p>\n          <b>group</b>\n        </p>\n        <blockquote>\n          <p>\n            <b>group</b>\n          </p>\n        </blockquote>\n        <blockquote>\n          <p>\n            <b>group</b>\n          </p>\n        </blockquote>\n        <blockquote>\n          <p>\n            <b>group</b>\n          </p>\n        </blockquote>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")

