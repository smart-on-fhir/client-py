#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import basic
from .fhirdate import FHIRDate


class BasicTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Basic", js["resourceType"])
        return basic.Basic(js)
    
    def testBasic1(self):
        inst = self.instantiate_from("basic-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Basic instance")
        self.implBasic1(inst)
        
        js = inst.as_json()
        self.assertEqual("Basic", js["resourceType"])
        inst2 = basic.Basic(js)
        self.implBasic1(inst2)
    
    def implBasic1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "UMLCLASSMODEL")
        self.assertEqual(inst.code.coding[0].system, "http://example.org/do-not-use/fhir-codes#resourceTypes")
        self.assertEqual(inst.extension[0].extension[0].url, "name")
        self.assertEqual(inst.extension[0].extension[0].valueString, "Class1")
        self.assertEqual(inst.extension[0].extension[1].extension[0].url, "name")
        self.assertEqual(inst.extension[0].extension[1].extension[0].valueString, "attribute1")
        self.assertEqual(inst.extension[0].extension[1].extension[1].url, "minOccurs")
        self.assertEqual(inst.extension[0].extension[1].extension[1].valueInteger, 1)
        self.assertEqual(inst.extension[0].extension[1].extension[2].url, "maxOccurs")
        self.assertEqual(inst.extension[0].extension[1].extension[2].valueCode, "*")
        self.assertEqual(inst.extension[0].extension[1].url, "attribute")
        self.assertEqual(inst.extension[0].extension[2].extension[0].url, "name")
        self.assertEqual(inst.extension[0].extension[2].extension[0].valueString, "attribute2")
        self.assertEqual(inst.extension[0].extension[2].extension[1].url, "minOccurs")
        self.assertEqual(inst.extension[0].extension[2].extension[1].valueInteger, 0)
        self.assertEqual(inst.extension[0].extension[2].extension[2].url, "maxOccurs")
        self.assertEqual(inst.extension[0].extension[2].extension[2].valueInteger, 1)
        self.assertEqual(inst.extension[0].extension[2].url, "attribute")
        self.assertEqual(inst.extension[0].url, "http://example.org/do-not-use/fhir-extensions/UMLclass")
        self.assertEqual(inst.id, "classModel")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testBasic2(self):
        inst = self.instantiate_from("basic-example-narrative.json")
        self.assertIsNotNone(inst, "Must have instantiated a Basic instance")
        self.implBasic2(inst)
        
        js = inst.as_json()
        self.assertEqual("Basic", js["resourceType"])
        inst2 = basic.Basic(js)
        self.implBasic2(inst2)
    
    def implBasic2(self, inst):
        self.assertEqual(inst.code.text, "Example Narrative Tester")
        self.assertEqual(inst.id, "basic-example-narrative")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "additional")
    
    def testBasic3(self):
        inst = self.instantiate_from("basic-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Basic instance")
        self.implBasic3(inst)
        
        js = inst.as_json()
        self.assertEqual("Basic", js["resourceType"])
        inst2 = basic.Basic(js)
        self.implBasic3(inst2)
    
    def implBasic3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "referral")
        self.assertEqual(inst.code.coding[0].system, "http://terminology.hl7.org/CodeSystem/basic-resource-type")
        self.assertEqual(inst.created.date, FHIRDate("2013-05-14").date)
        self.assertEqual(inst.created.as_json(), "2013-05-14")
        self.assertEqual(inst.extension[0].url, "http://example.org/do-not-use/fhir-extensions/referral#requestingPractitioner")
        self.assertEqual(inst.extension[1].url, "http://example.org/do-not-use/fhir-extensions/referral#notes")
        self.assertEqual(inst.extension[1].valueString, "The patient had fever peaks over the last couple of days. He is worried about these peaks.")
        self.assertEqual(inst.extension[2].url, "http://example.org/do-not-use/fhir-extensions/referral#fulfillingEncounter")
        self.assertEqual(inst.id, "referral")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/basic/identifiers")
        self.assertEqual(inst.identifier[0].value, "19283746")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.modifierExtension[0].url, "http://example.org/do-not-use/fhir-extensions/referral#referredForService")
        self.assertEqual(inst.modifierExtension[0].valueCodeableConcept.coding[0].code, "11429006")
        self.assertEqual(inst.modifierExtension[0].valueCodeableConcept.coding[0].display, "Consultation")
        self.assertEqual(inst.modifierExtension[0].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.modifierExtension[1].url, "http://example.org/do-not-use/fhir-extensions/referral#targetDate")
        self.assertEqual(inst.modifierExtension[1].valuePeriod.end.date, FHIRDate("2013-04-15").date)
        self.assertEqual(inst.modifierExtension[1].valuePeriod.end.as_json(), "2013-04-15")
        self.assertEqual(inst.modifierExtension[1].valuePeriod.start.date, FHIRDate("2013-04-01").date)
        self.assertEqual(inst.modifierExtension[1].valuePeriod.start.as_json(), "2013-04-01")
        self.assertEqual(inst.modifierExtension[2].url, "http://example.org/do-not-use/fhir-extensions/referral#status")
        self.assertEqual(inst.modifierExtension[2].valueCode, "complete")
        self.assertEqual(inst.text.status, "generated")

