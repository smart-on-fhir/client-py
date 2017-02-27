#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11466 on 2017-02-27.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import activitydefinition
from .fhirdate import FHIRDate


class ActivityDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ActivityDefinition", js["resourceType"])
        return activitydefinition.ActivityDefinition(js)
    
    def testActivityDefinition1(self):
        inst = self.instantiate_from("activitydefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition1(inst2)
    
    def implActivityDefinition1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "306206005")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Referral to service (procedure)")
        self.assertEqual(inst.description, "refer to primary care mental-health integrated care program for evaluation and treatment of mental health conditions now")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind, "ReferralRequest")
        self.assertEqual(inst.participant[0].type, "practitioner")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.topic[0].text, "Mental Health Referral")
        self.assertEqual(inst.useContext[0].code.code, "age")
        self.assertEqual(inst.useContext[0].code.system, "http://hl7.org/fhir/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "D000328")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display, "Adult")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "https://meshb.nlm.nih.gov")
        self.assertEqual(inst.useContext[1].code.code, "focus")
        self.assertEqual(inst.useContext[1].code.system, "http://hl7.org/fhir/usage-context-type")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].code, "87512008")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].display, "Mild major depression")
        self.assertEqual(inst.useContext[1].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[2].code.code, "focus")
        self.assertEqual(inst.useContext[2].code.system, "http://hl7.org/fhir/usage-context-type")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].code, "40379007")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].display, "Major depression, recurrent, mild")
        self.assertEqual(inst.useContext[2].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[3].code.code, "focus")
        self.assertEqual(inst.useContext[3].code.system, "http://hl7.org/fhir/usage-context-type")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].code, "225444004")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].display, "At risk for suicide (finding)")
        self.assertEqual(inst.useContext[3].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[4].code.code, "focus")
        self.assertEqual(inst.useContext[4].code.system, "http://hl7.org/fhir/usage-context-type")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].code, "306206005")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].display, "Referral to service (procedure)")
        self.assertEqual(inst.useContext[4].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[5].code.code, "user")
        self.assertEqual(inst.useContext[5].code.system, "http://hl7.org/fhir/usage-context-type")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].code, "309343006")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].display, "Physician")
        self.assertEqual(inst.useContext[5].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.useContext[6].code.code, "venue")
        self.assertEqual(inst.useContext[6].code.system, "http://hl7.org/fhir/usage-context-type")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].code, "440655000")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].display, "Outpatient environment")
        self.assertEqual(inst.useContext[6].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
    
    def testActivityDefinition2(self):
        inst = self.instantiate_from("activitydefinition-medicationorder-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ActivityDefinition instance")
        self.implActivityDefinition2(inst)
        
        js = inst.as_json()
        self.assertEqual("ActivityDefinition", js["resourceType"])
        inst2 = activitydefinition.ActivityDefinition(js)
        self.implActivityDefinition2(inst2)
    
    def implActivityDefinition2(self, inst):
        self.assertEqual(inst.contained[0].id, "citalopramMedication")
        self.assertEqual(inst.contained[1].id, "citalopramSubstance")
        self.assertEqual(inst.dosage[0].doseQuantity.unit, "{tbl}")
        self.assertEqual(inst.dosage[0].doseQuantity.value, 1)
        self.assertEqual(inst.dosage[0].route.coding[0].code, "26643006")
        self.assertEqual(inst.dosage[0].route.coding[0].display, "Oral route (qualifier value)")
        self.assertEqual(inst.dosage[0].route.text, "Oral route (qualifier value)")
        self.assertEqual(inst.dosage[0].text, "1 tablet oral 1 time daily")
        self.assertEqual(inst.dosage[0].timing.repeat.frequency, 1)
        self.assertEqual(inst.dosage[0].timing.repeat.period, 1)
        self.assertEqual(inst.dosage[0].timing.repeat.periodUnit, "d")
        self.assertEqual(inst.dynamicValue[0].expression, "3")
        self.assertEqual(inst.dynamicValue[0].path, "dispenseRequest.numberOfRepeatsAllowed")
        self.assertEqual(inst.dynamicValue[1].expression, "30 '{tbl}'")
        self.assertEqual(inst.dynamicValue[1].path, "dispenseRequest.quantity")
        self.assertEqual(inst.id, "citalopramPrescription")
        self.assertEqual(inst.kind, "MedicationRequest")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")

