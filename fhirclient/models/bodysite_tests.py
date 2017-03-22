#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import bodysite
from .fhirdate import FHIRDate


class BodySiteTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("BodySite", js["resourceType"])
        return bodysite.BodySite(js)
    
    def testBodySite1(self):
        inst = self.instantiate_from("bodysite-example-fetus.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodySite instance")
        self.implBodySite1(inst)
        
        js = inst.as_json()
        self.assertEqual("BodySite", js["resourceType"])
        inst2 = bodysite.BodySite(js)
        self.implBodySite1(inst2)
    
    def implBodySite1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "83418008")
        self.assertEqual(inst.code.coding[0].display, "Entire fetus (body structure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Fetus")
        self.assertEqual(inst.description, "EDD 1/1/2017 confirmation by LMP")
        self.assertEqual(inst.id, "fetus")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/bodysite/identifiers")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.text.status, "generated")
    
    def testBodySite2(self):
        inst = self.instantiate_from("bodysite-example-skin-patch.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodySite instance")
        self.implBodySite2(inst)
        
        js = inst.as_json()
        self.assertEqual("BodySite", js["resourceType"])
        inst2 = bodysite.BodySite(js)
        self.implBodySite2(inst2)
    
    def implBodySite2(self, inst):
        self.assertFalse(inst.active)
        self.assertEqual(inst.code.coding[0].code, "39937001")
        self.assertEqual(inst.code.coding[0].display, "Skin structure (body structure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Skin patch")
        self.assertEqual(inst.description, "inner surface (volar) of the left forearm")
        self.assertEqual(inst.id, "skin-patch")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/bodysite/identifiers")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.text.status, "generated")
    
    def testBodySite3(self):
        inst = self.instantiate_from("bodysite-example-tumor.json")
        self.assertIsNotNone(inst, "Must have instantiated a BodySite instance")
        self.implBodySite3(inst)
        
        js = inst.as_json()
        self.assertEqual("BodySite", js["resourceType"])
        inst2 = bodysite.BodySite(js)
        self.implBodySite3(inst2)
    
    def implBodySite3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "4147007")
        self.assertEqual(inst.code.coding[0].display, "Mass (morphologic abnormality)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Splenic mass")
        self.assertEqual(inst.description, "7 cm maximum diameter")
        self.assertEqual(inst.id, "tumor")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/bodysite/identifiers")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.image[0].contentType, "application/dicom")
        self.assertEqual(inst.image[0].url, "http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details")
        self.assertEqual(inst.qualifier[0].coding[0].code, "78961009")
        self.assertEqual(inst.qualifier[0].coding[0].display, "Splenic structure (body structure)")
        self.assertEqual(inst.qualifier[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.qualifier[0].text, "Splenic mass")
        self.assertEqual(inst.text.status, "generated")

