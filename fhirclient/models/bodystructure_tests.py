#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import bodystructure
from .fhirdate import FHIRDate


class BodyStructureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("BodyStructure", js["resourceType"])
        return bodystructure.BodyStructure(js)
    
    def testBodyStructure1(self):
        inst = self.instantiate_from("bodystructure-example-fetus.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodyStructure instance")
        self.implBodyStructure1(inst)
        
        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure1(inst2)
    
    def implBodyStructure1(self, inst):
        self.assertEqual(inst.description, "EDD 1/1/2017 confirmation by LMP")
        self.assertEqual(inst.id, "fetus")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/bodystructure/identifiers")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.location.coding[0].code, "83418008")
        self.assertEqual(inst.location.coding[0].display, "Entire fetus (body structure)")
        self.assertEqual(inst.location.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.location.text, "Fetus")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status, "generated")
    
    def testBodyStructure2(self):
        inst = self.instantiate_from("bodystructure-example-tumor.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodyStructure instance")
        self.implBodyStructure2(inst)
        
        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure2(inst2)
    
    def implBodyStructure2(self, inst):
        self.assertEqual(inst.description, "7 cm maximum diameter")
        self.assertEqual(inst.id, "tumor")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/bodystructure/identifiers")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.image[0].contentType, "application/dicom")
        self.assertEqual(inst.image[0].url, "http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details")
        self.assertEqual(inst.location.coding[0].code, "78961009")
        self.assertEqual(inst.location.coding[0].display, "Splenic structure (body structure)")
        self.assertEqual(inst.location.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.location.text, "Spleen")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.morphology.coding[0].code, "4147007")
        self.assertEqual(inst.morphology.coding[0].display, "Mass (morphologic abnormality)")
        self.assertEqual(inst.morphology.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.morphology.text, "Splenic mass")
        self.assertEqual(inst.text.status, "generated")
    
    def testBodyStructure3(self):
        inst = self.instantiate_from("bodystructure-example-skin-patch.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodyStructure instance")
        self.implBodyStructure3(inst)
        
        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure3(inst2)
    
    def implBodyStructure3(self, inst):
        self.assertFalse(inst.active)
        self.assertEqual(inst.description, "inner surface (volar) of the left forearm")
        self.assertEqual(inst.id, "skin-patch")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/bodystructure/identifiers")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.location.coding[0].code, "14975008")
        self.assertEqual(inst.location.coding[0].display, "Forearm")
        self.assertEqual(inst.location.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.location.text, "Forearm")
        self.assertEqual(inst.locationQualifier[0].coding[0].code, "419161000")
        self.assertEqual(inst.locationQualifier[0].coding[0].display, "Unilateral left")
        self.assertEqual(inst.locationQualifier[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.locationQualifier[0].text, "Left")
        self.assertEqual(inst.locationQualifier[1].coding[0].code, "263929005")
        self.assertEqual(inst.locationQualifier[1].coding[0].display, "Volar")
        self.assertEqual(inst.locationQualifier[1].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.locationQualifier[1].text, "Volar")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.morphology.text, "Skin patch")
        self.assertEqual(inst.text.status, "generated")

