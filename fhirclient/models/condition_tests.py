#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import condition
from .fhirdate import FHIRDate


class ConditionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Condition", js["resourceType"])
        return condition.Condition(js)
    
    def testCondition1(self):
        inst = self.instantiate_from("cond-uslab-example1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition1(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition1(inst2)
    
    def implCondition1(self, inst):
        self.assertEqual(inst.category.coding[0].code, "diagnosis")
        self.assertEqual(inst.category.coding[0].display, "Diagnosis")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/condition-category")
        self.assertEqual(inst.clinicalStatus, "provisional")
        self.assertEqual(inst.code.coding[0].code, "39065001")
        self.assertEqual(inst.code.coding[0].display, "Increased lead level")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Increased lead level")
        self.assertEqual(inst.id, "uslab-example1")
        self.assertEqual(inst.notes, "Elevated lead levels on screening")
        self.assertEqual(inst.text.status, "generated")
    
    def testCondition2(self):
        inst = self.instantiate_from("cond-uslab-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition2(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition2(inst2)
    
    def implCondition2(self, inst):
        self.assertEqual(inst.category.coding[0].code, "diagnosis")
        self.assertEqual(inst.category.coding[0].display, "Diagnosis")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/condition-category")
        self.assertEqual(inst.clinicalStatus, "provisional")
        self.assertEqual(inst.code.coding[0].code, "R78.71")
        self.assertEqual(inst.code.coding[0].display, "Abnormal lead level in blood")
        self.assertEqual(inst.code.coding[0].system, "http://www.cms.gov/Medicare/Coding/ICD10/index.html")
        self.assertEqual(inst.id, "uslab-example2")
        self.assertEqual(inst.text.status, "generated")
    
    def testCondition3(self):
        inst = self.instantiate_from("condition-example-f001-heart.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition3(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition3(inst2)
    
    def implCondition3(self, inst):
        self.assertEqual(inst.category.coding[0].code, "439401001")
        self.assertEqual(inst.category.coding[0].display, "diagnosis")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.clinicalStatus, "confirmed")
        self.assertEqual(inst.code.coding[0].code, "368009")
        self.assertEqual(inst.code.coding[0].display, "Heart valve disorder")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2011-10-05").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2011-10-05")
        self.assertEqual(inst.evidence[0].code.coding[0].code, "426396005")
        self.assertEqual(inst.evidence[0].code.coding[0].display, "Cardiac chest pain")
        self.assertEqual(inst.evidence[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].code, "40768004")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].display, "Left thorax")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.location[0].siteCodeableConcept.text, "heart structure")
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2011-08-05").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2011-08-05")
        self.assertEqual(inst.severity.coding[0].code, "6736007")
        self.assertEqual(inst.severity.coding[0].display, "Moderate")
        self.assertEqual(inst.severity.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testCondition4(self):
        inst = self.instantiate_from("condition-example-f002-lung.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition4(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition4(inst2)
    
    def implCondition4(self, inst):
        self.assertEqual(inst.category.coding[0].code, "439401001")
        self.assertEqual(inst.category.coding[0].display, "diagnosis")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.clinicalStatus, "confirmed")
        self.assertEqual(inst.code.coding[0].code, "254637007")
        self.assertEqual(inst.code.coding[0].display, "NSCLC - Non-small cell lung cancer")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2012-06-03").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2012-06-03")
        self.assertEqual(inst.evidence[0].code.coding[0].code, "169069000")
        self.assertEqual(inst.evidence[0].code.coding[0].display, "CT of thorax")
        self.assertEqual(inst.evidence[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].code, "51185008")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].display, "Thorax")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.location[0].siteCodeableConcept.text, "lung")
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2011-05-05").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2011-05-05")
        self.assertEqual(inst.severity.coding[0].code, "24484000")
        self.assertEqual(inst.severity.coding[0].display, "Severe")
        self.assertEqual(inst.severity.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.stage.summary.coding[0].code, "258219007")
        self.assertEqual(inst.stage.summary.coding[0].display, "stage II")
        self.assertEqual(inst.stage.summary.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testCondition5(self):
        inst = self.instantiate_from("condition-example-f003-abscess.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition5(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition5(inst2)
    
    def implCondition5(self, inst):
        self.assertEqual(inst.category.coding[0].code, "439401001")
        self.assertEqual(inst.category.coding[0].display, "diagnosis")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.clinicalStatus, "confirmed")
        self.assertEqual(inst.code.coding[0].code, "18099001")
        self.assertEqual(inst.code.coding[0].display, "Retropharyngeal abscess")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2012-02-20").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2012-02-20")
        self.assertEqual(inst.evidence[0].code.coding[0].code, "169068008")
        self.assertEqual(inst.evidence[0].code.coding[0].display, "CT of neck")
        self.assertEqual(inst.evidence[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].code, "280193007")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].display, "Entire retropharyngeal area")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2012-02-27").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2012-02-27")
        self.assertEqual(inst.severity.coding[0].code, "371923003")
        self.assertEqual(inst.severity.coding[0].display, "Mild to moderate")
        self.assertEqual(inst.severity.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testCondition6(self):
        inst = self.instantiate_from("condition-example-f201-fever.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition6(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition6(inst2)
    
    def implCondition6(self, inst):
        self.assertEqual(inst.category.coding[0].code, "55607006")
        self.assertEqual(inst.category.coding[0].display, "Problem")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category.coding[1].code, "condition")
        self.assertEqual(inst.category.coding[1].system, "http://hl7.org/fhir/condition-category")
        self.assertEqual(inst.clinicalStatus, "confirmed")
        self.assertEqual(inst.code.coding[0].code, "386661006")
        self.assertEqual(inst.code.coding[0].display, "Fever")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2013-04-04").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2013-04-04")
        self.assertEqual(inst.evidence[0].code.coding[0].code, "258710007")
        self.assertEqual(inst.evidence[0].code.coding[0].display, "degrees C")
        self.assertEqual(inst.evidence[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].code, "38266002")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].display, "Entire body as a whole")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2013-04-02").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2013-04-02")
        self.assertEqual(inst.severity.coding[0].code, "255604002")
        self.assertEqual(inst.severity.coding[0].display, "Mild")
        self.assertEqual(inst.severity.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testCondition7(self):
        inst = self.instantiate_from("condition-example-f202-malignancy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition7(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition7(inst2)
    
    def implCondition7(self, inst):
        self.assertEqual(inst.category.coding[0].code, "diagnose")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/condition-category")
        self.assertEqual(inst.clinicalStatus, "confirmed")
        self.assertEqual(inst.code.coding[0].code, "363346000")
        self.assertEqual(inst.code.coding[0].display, "Malignant neoplastic disease")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2012-12-01").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2012-12-01")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].code, "361355005")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].display, "Entire head and neck")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.onsetAge.code, "258707000")
        self.assertEqual(inst.onsetAge.system, "http://snomed.info/sct")
        self.assertEqual(inst.onsetAge.units, "years")
        self.assertEqual(inst.onsetAge.value, 52)
        self.assertEqual(inst.severity.coding[0].code, "24484000")
        self.assertEqual(inst.severity.coding[0].display, "Severe")
        self.assertEqual(inst.severity.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testCondition8(self):
        inst = self.instantiate_from("condition-example-f203-sepsis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition8(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition8(inst2)
    
    def implCondition8(self, inst):
        self.assertEqual(inst.category.coding[0].code, "55607006")
        self.assertEqual(inst.category.coding[0].display, "Problem")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category.coding[1].code, "finding")
        self.assertEqual(inst.category.coding[1].system, "http://hl7.org/fhir/condition-category")
        self.assertEqual(inst.clinicalStatus, "confirmed")
        self.assertEqual(inst.code.coding[0].code, "10001005")
        self.assertEqual(inst.code.coding[0].display, "Bacterial sepsis")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2013-03-11")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].code, "281158006")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].display, "Pulmonary vascular structure")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2013-03-08").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2013-03-08")
        self.assertEqual(inst.severity.coding[0].code, "371924009")
        self.assertEqual(inst.severity.coding[0].display, "Moderate to severe")
        self.assertEqual(inst.severity.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testCondition9(self):
        inst = self.instantiate_from("condition-example-f204-renal.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition9(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition9(inst2)
    
    def implCondition9(self, inst):
        self.assertEqual(inst.abatementDate.date, FHIRDate("2013-03-20").date)
        self.assertEqual(inst.abatementDate.as_json(), "2013-03-20")
        self.assertEqual(inst.category.coding[0].code, "55607006")
        self.assertEqual(inst.category.coding[0].display, "Problem")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category.coding[1].code, "condition")
        self.assertEqual(inst.category.coding[1].system, "http://hl7.org/fhir/condition-category")
        self.assertEqual(inst.clinicalStatus, "working")
        self.assertEqual(inst.code.coding[0].code, "36225005")
        self.assertEqual(inst.code.coding[0].display, "Acute renal insufficiency specified as due to procedure")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2013-03-11")
        self.assertEqual(inst.id, "f204")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].code, "181414000")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].display, "Kidney")
        self.assertEqual(inst.location[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.onsetDateTime.date, FHIRDate("2013-03-11").date)
        self.assertEqual(inst.onsetDateTime.as_json(), "2013-03-11")
        self.assertEqual(inst.severity.coding[0].code, "24484000")
        self.assertEqual(inst.severity.coding[0].display, "Severe")
        self.assertEqual(inst.severity.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.stage.summary.coding[0].code, "14803004")
        self.assertEqual(inst.stage.summary.coding[0].display, "Temporary")
        self.assertEqual(inst.stage.summary.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.status, "generated")
    
    def testCondition10(self):
        inst = self.instantiate_from("condition-example-f205-infection.json")
        self.assertIsNotNone(inst, "Must have instantiated a Condition instance")
        self.implCondition10(inst)
        
        js = inst.as_json()
        self.assertEqual("Condition", js["resourceType"])
        inst2 = condition.Condition(js)
        self.implCondition10(inst2)
    
    def implCondition10(self, inst):
        self.assertEqual(inst.clinicalStatus, "working")
        self.assertEqual(inst.code.coding[0].code, "87628006")
        self.assertEqual(inst.code.coding[0].display, "Bacterial infectious disease")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.dateAsserted.date, FHIRDate("2013-04-04").date)
        self.assertEqual(inst.dateAsserted.as_json(), "2013-04-04")
        self.assertEqual(inst.id, "f205")
        self.assertEqual(inst.text.status, "generated")

