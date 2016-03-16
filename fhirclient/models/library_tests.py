#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 on 2016-03-16.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import library
from .fhirdate import FHIRDate


class LibraryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Library", js["resourceType"])
        return library.Library(js)
    
    def testLibrary1(self):
        inst = self.instantiate_from("library-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary1(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary1(inst2)
    
    def implLibrary1(self, inst):
        self.assertEqual(inst.dataRequirement[0].codeFilter[0].path, "code")
        self.assertEqual(inst.dataRequirement[0].codeFilter[0].valueSetString, "Other Female Reproductive Conditions")
        self.assertEqual(inst.dataRequirement[0].type, "Condition")
        self.assertEqual(inst.document.contentType, "application/x-cql+text")
        self.assertEqual(inst.document.url, "http://cqlrepository.org/ChlamydiaScreening_Common.cql")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.model[0].identifier, "QUICK")
        self.assertEqual(inst.moduleMetadata.description, "Common Logic for adherence to Chlamydia Screening guidelines")
        self.assertEqual(inst.moduleMetadata.identifier[0].use, "official")
        self.assertEqual(inst.moduleMetadata.identifier[0].value, "ChalmydiaScreening_Common")
        self.assertEqual(inst.moduleMetadata.publicationDate.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.moduleMetadata.publicationDate.as_json(), "2015-07-22")
        self.assertEqual(inst.moduleMetadata.status, "draft")
        self.assertEqual(inst.moduleMetadata.title, "Chlamydia Screening Common Library")
        self.assertEqual(inst.moduleMetadata.topic[0].text, "Chlamydia Screening")
        self.assertEqual(inst.moduleMetadata.type, "library")
        self.assertEqual(inst.moduleMetadata.version, "2.0.0")
        self.assertEqual(inst.text.div, "<div>Chlamydia Screening Common Library</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueSet[0].identifier, "2.16.840.1.113883.3.560.100.2")
        self.assertEqual(inst.valueSet[0].name, "Female Administrative Sex")

