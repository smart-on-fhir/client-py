#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import implementationguide
from .fhirdate import FHIRDate


class ImplementationGuideTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImplementationGuide", js["resourceType"])
        return implementationguide.ImplementationGuide(js)
    
    def testImplementationGuide1(self):
        inst = self.instantiate_from("implementationguide-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImplementationGuide instance")
        self.implImplementationGuide1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImplementationGuide", js["resourceType"])
        inst2 = implementationguide.ImplementationGuide(js)
        self.implImplementationGuide1(inst2)
    
    def implImplementationGuide1(self, inst):
        self.assertEqual(inst.binary[0], "http://h7.org/fhir/fhir.css")
        self.assertEqual(inst.contact[0].name, "ONC")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://www.healthit.gov")
        self.assertEqual(inst.contact[1].name, "HL7")
        self.assertEqual(inst.contact[1].telecom[0].system, "url")
        self.assertEqual(inst.contact[1].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.copyright, "Published by ONC under the standard FHIR license (CC0)")
        self.assertEqual(inst.date.date, FHIRDate("2015-01-01").date)
        self.assertEqual(inst.date.as_json(), "2015-01-01")
        self.assertEqual(inst.dependency[0].type, "reference")
        self.assertEqual(inst.dependency[0].uri, "http://hl7.org/fhir/ImplementationGuide/uscore")
        self.assertFalse(inst.experimental)
        self.assertEqual(inst.fhirVersion, "1.0.0")
        self.assertEqual(inst.global_fhir[0].type, "Patient")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.name, "Data Access Framework (DAF)")
        self.assertEqual(inst.package[0].description, "Base package (not broken up into multiple packages)")
        self.assertEqual(inst.package[0].name, "test")
        self.assertEqual(inst.package[0].resource[0].acronym, "daf-tst")
        self.assertEqual(inst.package[0].resource[0].description, "A test example to show how a package works")
        self.assertTrue(inst.package[0].resource[0].example)
        self.assertEqual(inst.package[0].resource[0].name, "Test Example")
        self.assertEqual(inst.package[0].resource[0].sourceUri, "test.html")
        self.assertEqual(inst.page.kind, "page")
        self.assertEqual(inst.page.page[0].format, "text/html")
        self.assertEqual(inst.page.page[0].kind, "list")
        self.assertEqual(inst.page.page[0].package[0], "test")
        self.assertEqual(inst.page.page[0].source, "list.html")
        self.assertEqual(inst.page.page[0].title, "Value Set Page")
        self.assertEqual(inst.page.page[0].type[0], "ValueSet")
        self.assertEqual(inst.page.source, "patient-example.html")
        self.assertEqual(inst.page.title, "Example Patient Page")
        self.assertEqual(inst.publisher, "ONC / HL7 Joint project")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/us/daf")
        self.assertEqual(inst.version, "0")

