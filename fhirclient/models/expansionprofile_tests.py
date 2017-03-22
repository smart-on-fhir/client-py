#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import expansionprofile
from .fhirdate import FHIRDate


class ExpansionProfileTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ExpansionProfile", js["resourceType"])
        return expansionprofile.ExpansionProfile(js)
    
    def testExpansionProfile1(self):
        inst = self.instantiate_from("expansionprofile-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ExpansionProfile instance")
        self.implExpansionProfile1(inst)
        
        js = inst.as_json()
        self.assertEqual("ExpansionProfile", js["resourceType"])
        inst2 = expansionprofile.ExpansionProfile(js)
        self.implExpansionProfile1(inst2)
    
    def implExpansionProfile1(self, inst):
        self.assertEqual(inst.contact[0].name, "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2016-12-23").date)
        self.assertEqual(inst.date.as_json(), "2016-12-23")
        self.assertEqual(inst.description, "exanple ExpansionProfile for publication")
        self.assertTrue(inst.excludeNested)
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://example.org/profiles")
        self.assertEqual(inst.identifier.value, "example")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "001")
        self.assertEqual(inst.jurisdiction[0].coding[0].display, "World")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "http://unstats.un.org/unsd/methods/m49/m49.htm")
        self.assertEqual(inst.name, "Example Expansion Profile")
        self.assertEqual(inst.publisher, "HL7 International")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[ Provide Rendering ]</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/ExpansionProfile/example")
        self.assertEqual(inst.version, "0.1")

