#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import operationdefinition
from .fhirdate import FHIRDate


class OperationDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OperationDefinition", js["resourceType"])
        return operationdefinition.OperationDefinition(js)
    
    def testOperationDefinition1(self):
        inst = self.instantiate_from("operationdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a OperationDefinition instance")
        self.implOperationDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition1(inst2)
    
    def implOperationDefinition1(self, inst):
        self.assertEqual(inst.code, "populate")
        self.assertEqual(inst.contact[0].name, "System Administrator")
        self.assertEqual(inst.contact[0].telecom[0].system, "email")
        self.assertEqual(inst.contact[0].telecom[0].value, "beep@coyote.acme.com")
        self.assertEqual(inst.date.date, FHIRDate("2015-08-04").date)
        self.assertEqual(inst.date.as_json(), "2015-08-04")
        self.assertEqual(inst.description, "Limited implementation of the Populate Questionnaire implemenation")
        self.assertEqual(inst.id, "example")
        self.assertTrue(inst.instance)
        self.assertEqual(inst.kind, "operation")
        self.assertEqual(inst.name, "Populate Questionnaire")
        self.assertEqual(inst.notes, "Only implemented for Labs and Medications so far")
        self.assertEqual(inst.parameter[0].max, "1")
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(inst.parameter[0].name, "subject")
        self.assertEqual(inst.parameter[0].type, "Reference")
        self.assertEqual(inst.parameter[0].use, "in")
        self.assertEqual(inst.parameter[1].documentation, "The partially (or fully)-populated set of answers for the specified Questionnaire")
        self.assertEqual(inst.parameter[1].max, "1")
        self.assertEqual(inst.parameter[1].min, 1)
        self.assertEqual(inst.parameter[1].name, "return")
        self.assertEqual(inst.parameter[1].type, "QuestionnaireResponse")
        self.assertEqual(inst.parameter[1].use, "out")
        self.assertEqual(inst.publisher, "Acme Healthcare Services")
        self.assertEqual(inst.status, "draft")
        self.assertFalse(inst.system)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0], "Questionnaire")
        self.assertEqual(inst.url, "http://h7.org/fhir/OperationDefinition/example")
        self.assertEqual(inst.version, "B")

