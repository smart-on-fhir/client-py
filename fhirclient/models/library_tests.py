#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 on 2016-04-01.
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
        inst = self.instantiate_from("library-cms146-example.json")
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
        self.assertEqual(inst.dataRequirement[1].type, "Patient")
        self.assertEqual(inst.dataRequirement[2].codeFilter[0].path, "category")
        self.assertEqual(inst.dataRequirement[2].codeFilter[0].valueCode[0], "diagnosis")
        self.assertEqual(inst.dataRequirement[2].codeFilter[1].path, "clinicalStatus")
        self.assertEqual(inst.dataRequirement[2].codeFilter[1].valueCode[0], "confirmed")
        self.assertEqual(inst.dataRequirement[2].codeFilter[2].path, "code")
        self.assertEqual(inst.dataRequirement[2].codeFilter[2].valueSetString, "2.16.840.1.113883.3.464.1003.102.12.1011")
        self.assertEqual(inst.dataRequirement[2].type, "Condition")
        self.assertEqual(inst.dataRequirement[3].codeFilter[0].path, "category")
        self.assertEqual(inst.dataRequirement[3].codeFilter[0].valueCode[0], "diagnosis")
        self.assertEqual(inst.dataRequirement[3].codeFilter[1].path, "clinicalStatus")
        self.assertEqual(inst.dataRequirement[3].codeFilter[1].valueCode[0], "confirmed")
        self.assertEqual(inst.dataRequirement[3].codeFilter[2].path, "code")
        self.assertEqual(inst.dataRequirement[3].codeFilter[2].valueSetString, "2.16.840.1.113883.3.464.1003.102.12.1012")
        self.assertEqual(inst.dataRequirement[3].type, "Condition")
        self.assertEqual(inst.dataRequirement[4].codeFilter[0].path, "status")
        self.assertEqual(inst.dataRequirement[4].codeFilter[0].valueCode[0], "finished")
        self.assertEqual(inst.dataRequirement[4].codeFilter[1].path, "class")
        self.assertEqual(inst.dataRequirement[4].codeFilter[1].valueCode[0], "ambulatory")
        self.assertEqual(inst.dataRequirement[4].codeFilter[2].path, "type")
        self.assertEqual(inst.dataRequirement[4].codeFilter[2].valueSetString, "2.16.840.1.113883.3.464.1003.101.12.1061")
        self.assertEqual(inst.dataRequirement[4].type, "Encounter")
        self.assertEqual(inst.dataRequirement[5].codeFilter[0].path, "diagnosis")
        self.assertEqual(inst.dataRequirement[5].codeFilter[0].valueSetString, "2.16.840.1.113883.3.464.1003.198.12.1012")
        self.assertEqual(inst.dataRequirement[5].type, "DiagnosticReport")
        self.assertEqual(inst.dataRequirement[6].codeFilter[0].path, "code")
        self.assertEqual(inst.dataRequirement[6].codeFilter[0].valueSetString, "2.16.840.1.113883.3.464.1003.196.12.1001")
        self.assertEqual(inst.dataRequirement[6].type, "Medication")
        self.assertEqual(inst.dataRequirement[7].codeFilter[0].path, "status")
        self.assertEqual(inst.dataRequirement[7].codeFilter[0].valueCode[0], "active")
        self.assertEqual(inst.dataRequirement[7].codeFilter[1].path, "medication.code")
        self.assertEqual(inst.dataRequirement[7].codeFilter[1].valueSetString, "2.16.840.1.113883.3.464.1003.196.12.1001")
        self.assertEqual(inst.dataRequirement[7].type, "MedicationOrder")
        self.assertEqual(inst.dataRequirement[8].codeFilter[0].path, "status")
        self.assertEqual(inst.dataRequirement[8].codeFilter[0].valueCode[0], "completed")
        self.assertEqual(inst.dataRequirement[8].codeFilter[1].path, "medication.code")
        self.assertEqual(inst.dataRequirement[8].codeFilter[1].valueSetString, "2.16.840.1.113883.3.464.1003.196.12.1001")
        self.assertEqual(inst.dataRequirement[8].type, "MedicationStatement")
        self.assertEqual(inst.document.contentType, "application/cql+text")
        self.assertEqual(inst.document.url, "http://cqlrepository.org/CMS146.cql")
        self.assertEqual(inst.id, "library-cms146-example")
        self.assertEqual(inst.model[0].identifier, "QUICK")
        self.assertEqual(inst.moduleMetadata.description, "Logic for CMS 146: Appropriate Testing for Children with Pharyngitis")
        self.assertEqual(inst.moduleMetadata.identifier[0].use, "official")
        self.assertEqual(inst.moduleMetadata.identifier[0].value, "CMS146")
        self.assertEqual(inst.moduleMetadata.publicationDate.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.moduleMetadata.publicationDate.as_json(), "2015-07-22")
        self.assertEqual(inst.moduleMetadata.status, "draft")
        self.assertEqual(inst.moduleMetadata.title, "Appropriate Testing for Children with Pharyngitis")
        self.assertEqual(inst.moduleMetadata.type, "library")
        self.assertEqual(inst.moduleMetadata.version, "2.0.0")
        self.assertEqual(inst.text.div, "<div>CMS 146 Logic</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueSet[0].identifier, "2.16.840.1.113883.3.560.100.2")
        self.assertEqual(inst.valueSet[0].name, "Female Administrative Sex")
    
    def testLibrary2(self):
        inst = self.instantiate_from("library-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary2(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary2(inst2)
    
    def implLibrary2(self, inst):
        self.assertEqual(inst.dataRequirement[0].codeFilter[0].path, "code")
        self.assertEqual(inst.dataRequirement[0].codeFilter[0].valueSetString, "Other Female Reproductive Conditions")
        self.assertEqual(inst.dataRequirement[0].type, "Condition")
        self.assertEqual(inst.document.contentType, "application/cql+text")
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

