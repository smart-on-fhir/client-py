#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        inst = self.instantiate_from("library-predecessor-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary1(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary1(inst2)
    
    def implLibrary1(self, inst):
        self.assertEqual(inst.content[0].contentType, "text/cql")
        self.assertEqual(inst.content[0].title, "FHIR Helpers")
        self.assertEqual(inst.content[0].url, "library-fhir-helpers-content.cql")
        self.assertEqual(inst.date.date, FHIRDate("2016-11-14").date)
        self.assertEqual(inst.date.as_json(), "2016-11-14")
        self.assertEqual(inst.description, "FHIR Helpers")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "library-fhir-helpers-predecessor")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "FHIRHelpers")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatedArtifact[0].resource, "Library/fhir-model-definition")
        self.assertEqual(inst.relatedArtifact[0].type, "depends-on")
        self.assertEqual(inst.relatedArtifact[1].resource, "Library/library-fhir-helpers")
        self.assertEqual(inst.relatedArtifact[1].type, "successor")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "FHIR Helpers")
        self.assertEqual(inst.topic[0].text, "FHIR Helpers")
        self.assertEqual(inst.type.coding[0].code, "logic-library")
        self.assertEqual(inst.version, "1.6")
    
    def testLibrary2(self):
        inst = self.instantiate_from("library-cms146-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary2(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary2(inst2)
    
    def implLibrary2(self, inst):
        self.assertEqual(inst.content[0].contentType, "text/cql")
        self.assertEqual(inst.content[0].url, "library-cms146-example-content.cql")
        self.assertEqual(inst.dataRequirement[0].type, "Patient")
        self.assertEqual(inst.dataRequirement[1].codeFilter[0].code[0].code, "diagnosis")
        self.assertEqual(inst.dataRequirement[1].codeFilter[0].path, "category")
        self.assertEqual(inst.dataRequirement[1].codeFilter[1].code[0].code, "confirmed")
        self.assertEqual(inst.dataRequirement[1].codeFilter[1].path, "clinicalStatus")
        self.assertEqual(inst.dataRequirement[1].codeFilter[2].path, "code")
        self.assertEqual(inst.dataRequirement[1].codeFilter[2].valueSet, "urn:oid:2.16.840.1.113883.3.464.1003.102.12.1011")
        self.assertEqual(inst.dataRequirement[1].type, "Condition")
        self.assertEqual(inst.dataRequirement[2].codeFilter[0].code[0].code, "diagnosis")
        self.assertEqual(inst.dataRequirement[2].codeFilter[0].path, "category")
        self.assertEqual(inst.dataRequirement[2].codeFilter[1].code[0].code, "confirmed")
        self.assertEqual(inst.dataRequirement[2].codeFilter[1].path, "clinicalStatus")
        self.assertEqual(inst.dataRequirement[2].codeFilter[2].path, "code")
        self.assertEqual(inst.dataRequirement[2].codeFilter[2].valueSet, "urn:oid:2.16.840.1.113883.3.464.1003.102.12.1012")
        self.assertEqual(inst.dataRequirement[2].type, "Condition")
        self.assertEqual(inst.dataRequirement[3].codeFilter[0].code[0].code, "finished")
        self.assertEqual(inst.dataRequirement[3].codeFilter[0].path, "status")
        self.assertEqual(inst.dataRequirement[3].codeFilter[1].code[0].code, "ambulatory")
        self.assertEqual(inst.dataRequirement[3].codeFilter[1].path, "class")
        self.assertEqual(inst.dataRequirement[3].codeFilter[2].path, "type")
        self.assertEqual(inst.dataRequirement[3].codeFilter[2].valueSet, "urn:oid:2.16.840.1.113883.3.464.1003.101.12.1061")
        self.assertEqual(inst.dataRequirement[3].type, "Encounter")
        self.assertEqual(inst.dataRequirement[4].codeFilter[0].path, "diagnosis")
        self.assertEqual(inst.dataRequirement[4].codeFilter[0].valueSet, "urn:oid:2.16.840.1.113883.3.464.1003.198.12.1012")
        self.assertEqual(inst.dataRequirement[4].type, "DiagnosticReport")
        self.assertEqual(inst.dataRequirement[5].codeFilter[0].path, "code")
        self.assertEqual(inst.dataRequirement[5].codeFilter[0].valueSet, "urn:oid:2.16.840.1.113883.3.464.1003.196.12.1001")
        self.assertEqual(inst.dataRequirement[5].type, "Medication")
        self.assertEqual(inst.dataRequirement[6].codeFilter[0].code[0].code, "active")
        self.assertEqual(inst.dataRequirement[6].codeFilter[0].path, "status")
        self.assertEqual(inst.dataRequirement[6].codeFilter[1].path, "medication.code")
        self.assertEqual(inst.dataRequirement[6].codeFilter[1].valueSet, "urn:oid:2.16.840.1.113883.3.464.1003.196.12.1001")
        self.assertEqual(inst.dataRequirement[6].type, "MedicationRequest")
        self.assertEqual(inst.dataRequirement[7].codeFilter[0].code[0].code, "completed")
        self.assertEqual(inst.dataRequirement[7].codeFilter[0].path, "status")
        self.assertEqual(inst.dataRequirement[7].codeFilter[1].path, "medication.code")
        self.assertEqual(inst.dataRequirement[7].codeFilter[1].valueSet, "urn:oid:2.16.840.1.113883.3.464.1003.196.12.1001")
        self.assertEqual(inst.dataRequirement[7].type, "MedicationStatement")
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(inst.description, "Logic for CMS 146: Appropriate Testing for Children with Pharyngitis")
        self.assertEqual(inst.id, "library-cms146-example")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "CMS146")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatedArtifact[0].resource, "Library/library-quick-model-definition")
        self.assertEqual(inst.relatedArtifact[0].type, "depends-on")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Appropriate Testing for Children with Pharyngitis")
        self.assertEqual(inst.type.coding[0].code, "logic-library")
        self.assertEqual(inst.version, "2.0.0")
    
    def testLibrary3(self):
        inst = self.instantiate_from("library-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary3(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary3(inst2)
    
    def implLibrary3(self, inst):
        self.assertEqual(inst.content[0].contentType, "text/cql")
        self.assertEqual(inst.content[0].url, "library-example-content.cql")
        self.assertEqual(inst.dataRequirement[0].codeFilter[0].path, "code")
        self.assertEqual(inst.dataRequirement[0].codeFilter[0].valueSet, "urn:oid:2.16.840.1.113883.3.464.1003.111.12.1006")
        self.assertEqual(inst.dataRequirement[0].type, "Condition")
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(inst.description, "Common Logic for adherence to Chlamydia Screening guidelines")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "ChalmydiaScreening_Common")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatedArtifact[0].resource, "Library/library-quick-model-definition")
        self.assertEqual(inst.relatedArtifact[0].type, "depends-on")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Chlamydia Screening Common Library")
        self.assertEqual(inst.topic[0].text, "Chlamydia Screening")
        self.assertEqual(inst.type.coding[0].code, "logic-library")
        self.assertEqual(inst.version, "2.0.0")
    
    def testLibrary4(self):
        inst = self.instantiate_from("library-composition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Library instance")
        self.implLibrary4(inst)
        
        js = inst.as_json()
        self.assertEqual("Library", js["resourceType"])
        inst2 = library.Library(js)
        self.implLibrary4(inst2)
    
    def implLibrary4(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2017-03-10").date)
        self.assertEqual(inst.date.as_json(), "2017-03-10")
        self.assertEqual(inst.description, "Artifacts required for implementation of Zika Virus Management")
        self.assertEqual(inst.id, "composition-example")
        self.assertEqual(inst.identifier[0].system, "http://example.org")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "Zika Artifacts")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatedArtifact[0].resource, "ActivityDefinition/administer-zika-virus-exposure-assessment")
        self.assertEqual(inst.relatedArtifact[0].type, "composed-of")
        self.assertEqual(inst.relatedArtifact[1].resource, "ActivityDefinition/order-serum-zika-dengue-virus-igm")
        self.assertEqual(inst.relatedArtifact[1].type, "composed-of")
        self.assertEqual(inst.relatedArtifact[2].resource, "ActivityDefinition/provide-mosquito-prevention-advice")
        self.assertEqual(inst.relatedArtifact[2].type, "composed-of")
        self.assertEqual(inst.relatedArtifact[3].resource, "Library/zika-virus-intervention-logic")
        self.assertEqual(inst.relatedArtifact[3].type, "composed-of")
        self.assertEqual(inst.relatedArtifact[4].resource, "PlanDefinition/zika-virus-intervention")
        self.assertEqual(inst.relatedArtifact[4].type, "composed-of")
        self.assertEqual(inst.relatedArtifact[5].resource, "Questionnaire/zika-virus-exposure-assessment")
        self.assertEqual(inst.relatedArtifact[5].type, "composed-of")
        self.assertEqual(inst.relatedArtifact[6].type, "derived-from")
        self.assertEqual(inst.relatedArtifact[6].url, "https://www.cdc.gov/mmwr/volumes/65/wr/mm6539e1.htm?s_cid=mm6539e1_w")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Zika Artifacts")
        self.assertEqual(inst.topic[0].text, "Zika Virus Management")
        self.assertEqual(inst.type.coding[0].code, "asset-collection")
        self.assertEqual(inst.version, "1.0.0")

