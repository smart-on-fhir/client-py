#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        self.assertEqual(inst.contact[0].name, "ONC")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://www.healthit.gov")
        self.assertEqual(inst.contact[1].name, "HL7")
        self.assertEqual(inst.contact[1].telecom[0].system, "url")
        self.assertEqual(inst.contact[1].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.copyright, "Published by ONC under the standard FHIR license (CC0)")
        self.assertEqual(inst.date.date, FHIRDate("2015-01-01").date)
        self.assertEqual(inst.date.as_json(), "2015-01-01")
        self.assertEqual(inst.definition.grouping[0].description, "Base package (not broken up into multiple packages)")
        self.assertEqual(inst.definition.grouping[0].name, "test")
        self.assertEqual(inst.definition.page.generation, "html")
        self.assertEqual(inst.definition.page.nameUrl, "patient-example.html")
        self.assertEqual(inst.definition.page.page[0].generation, "html")
        self.assertEqual(inst.definition.page.page[0].nameUrl, "list.html")
        self.assertEqual(inst.definition.page.page[0].title, "Value Set Page")
        self.assertEqual(inst.definition.page.title, "Example Patient Page")
        self.assertEqual(inst.definition.parameter[0].code, "apply")
        self.assertEqual(inst.definition.parameter[0].value, "version")
        self.assertEqual(inst.definition.resource[0].description, "A test example to show how an implementation guide works")
        self.assertEqual(inst.definition.resource[0].exampleCanonical, "http://hl7.org/fhir/us/core/StructureDefinition/patient")
        self.assertEqual(inst.definition.resource[0].name, "Test Example")
        self.assertEqual(inst.dependsOn[0].uri, "http://hl7.org/fhir/ImplementationGuide/uscore")
        self.assertFalse(inst.experimental)
        self.assertEqual(inst.fhirVersion[0], "4.0.0")
        self.assertEqual(inst.global_fhir[0].profile, "http://hl7.org/fhir/us/core/StructureDefinition/patient")
        self.assertEqual(inst.global_fhir[0].type, "Patient")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.license, "CC0-1.0")
        self.assertEqual(inst.manifest.image[0], "fhir.png")
        self.assertEqual(inst.manifest.other[0], "fhir.css")
        self.assertEqual(inst.manifest.page[0].anchor[0], "patient-test")
        self.assertEqual(inst.manifest.page[0].anchor[1], "tx")
        self.assertEqual(inst.manifest.page[0].anchor[2], "uml")
        self.assertEqual(inst.manifest.page[0].name, "patient-test.html")
        self.assertEqual(inst.manifest.page[0].title, "Test Patient Example")
        self.assertEqual(inst.manifest.rendering, "http://hl7.org/fhir/us/daf")
        self.assertEqual(inst.manifest.resource[0].exampleCanonical, "http://hl7.org/fhir/us/core/StructureDefinition/patient")
        self.assertEqual(inst.manifest.resource[0].relativePath, "patient-test.html#patient-test")
        self.assertEqual(inst.name, "Data Access Framework (DAF)")
        self.assertEqual(inst.packageId, "hl7.fhir.us.daf")
        self.assertEqual(inst.publisher, "ONC / HL7 Joint project")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/us/daf")
        self.assertEqual(inst.version, "0")

