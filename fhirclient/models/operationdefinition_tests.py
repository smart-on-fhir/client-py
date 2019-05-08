#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        self.assertEqual(inst.base, "OperationDefinition/Questionnaire-populate")
        self.assertEqual(inst.code, "populate")
        self.assertEqual(inst.comment, "Only implemented for Labs and Medications so far")
        self.assertEqual(inst.contact[0].name, "System Administrator")
        self.assertEqual(inst.contact[0].telecom[0].system, "email")
        self.assertEqual(inst.contact[0].telecom[0].value, "beep@coyote.acme.com")
        self.assertEqual(inst.date.date, FHIRDate("2015-08-04").date)
        self.assertEqual(inst.date.as_json(), "2015-08-04")
        self.assertEqual(inst.description, "Limited implementation of the Populate Questionnaire implementation")
        self.assertEqual(inst.id, "example")
        self.assertTrue(inst.instance)
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "GB")
        self.assertEqual(inst.jurisdiction[0].coding[0].display, "United Kingdom of Great Britain and Northern Ireland (the)")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind, "operation")
        self.assertEqual(inst.name, "Populate Questionnaire")
        self.assertEqual(inst.overload[0].parameterName[0], "subject")
        self.assertEqual(inst.overload[0].parameterName[1], "local")
        self.assertEqual(inst.overload[1].comment, "local defaults to false when not passed as a parameter")
        self.assertEqual(inst.overload[1].parameterName[0], "subject")
        self.assertEqual(inst.parameter[0].max, "1")
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(inst.parameter[0].name, "subject")
        self.assertEqual(inst.parameter[0].type, "Reference")
        self.assertEqual(inst.parameter[0].use, "in")
        self.assertEqual(inst.parameter[1].documentation, "If the *local* parameter is set to true, server information about the specified subject will be used to populate the instance.")
        self.assertEqual(inst.parameter[1].max, "1")
        self.assertEqual(inst.parameter[1].min, 0)
        self.assertEqual(inst.parameter[1].name, "local")
        self.assertEqual(inst.parameter[1].type, "Reference")
        self.assertEqual(inst.parameter[1].use, "in")
        self.assertEqual(inst.parameter[2].documentation, "The partially (or fully)-populated set of answers for the specified Questionnaire")
        self.assertEqual(inst.parameter[2].max, "1")
        self.assertEqual(inst.parameter[2].min, 1)
        self.assertEqual(inst.parameter[2].name, "return")
        self.assertEqual(inst.parameter[2].type, "QuestionnaireResponse")
        self.assertEqual(inst.parameter[2].use, "out")
        self.assertEqual(inst.publisher, "Acme Healthcare Services")
        self.assertEqual(inst.resource[0], "Questionnaire")
        self.assertEqual(inst.status, "draft")
        self.assertFalse(inst.system)
        self.assertEqual(inst.text.status, "generated")
        self.assertFalse(inst.type)
        self.assertEqual(inst.url, "http://h7.org/fhir/OperationDefinition/example")
        self.assertEqual(inst.useContext[0].code.code, "venue")
        self.assertEqual(inst.useContext[0].code.display, "Clinical Venue")
        self.assertEqual(inst.useContext[0].code.system, "http://build.fhir.org/codesystem-usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "IMP")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display, "inpatient encounter")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.version, "B")

