#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import valueset
from .fhirdate import FHIRDate


class ValueSetTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ValueSet", js["resourceType"])
        return valueset.ValueSet(js)
    
    def testValueSet1(self):
        inst = self.instantiate_from("valueset-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet1(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet1(inst2)
    
    def implValueSet1(self, inst):
        self.assertEqual(inst.compose.include[0].concept[0].code, "14647-2")
        self.assertEqual(inst.compose.include[0].concept[1].code, "2093-3")
        self.assertEqual(inst.compose.include[0].concept[2].code, "35200-5")
        self.assertEqual(inst.compose.include[0].concept[3].code, "9342-7")
        self.assertEqual(inst.compose.include[0].system, "http://loinc.org")
        self.assertEqual(inst.compose.include[0].version, "2.36")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.copyright, "This content from LOINC® is copyright © 1995 Regenstrief Institute, Inc. and the LOINC Committee, and available at no cost under the license at http://loinc.org/terms-of-use")
        self.assertEqual(inst.date.date, FHIRDate("2012-06-13").date)
        self.assertEqual(inst.date.as_json(), "2012-06-13")
        self.assertEqual(inst.description, "This is an example value set that includes        all the LOINC codes for serum cholesterol from v2.36")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.name, "LOINC Codes for Cholesterol")
        self.assertEqual(inst.publisher, "FHIR project team (example)")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "urn:uuid:256a5231-a2bb-49bd-9fea-f349d428b70d")
        self.assertEqual(inst.version, "20120613")
    
    def testValueSet2(self):
        inst = self.instantiate_from("valueset-list-example-codes.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
        self.implValueSet2(inst)
        
        js = inst.as_json()
        self.assertEqual("ValueSet", js["resourceType"])
        inst2 = valueset.ValueSet(js)
        self.implValueSet2(inst2)
    
    def implValueSet2(self, inst):
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertTrue(inst.define.caseSensitive)
        self.assertEqual(inst.define.concept[0].code, "alerts")
        self.assertEqual(inst.define.concept[0].definition, "A list of alerts for the patient")
        self.assertEqual(inst.define.concept[0].display, "Alerts")
        self.assertEqual(inst.define.concept[1].code, "adverserxns")
        self.assertEqual(inst.define.concept[1].definition, "A list of part adverse reactions")
        self.assertEqual(inst.define.concept[1].display, "Adverse Reactions")
        self.assertEqual(inst.define.concept[2].code, "allergies")
        self.assertEqual(inst.define.concept[2].definition, "A list of Allergies for the patient")
        self.assertEqual(inst.define.concept[2].display, "Allergies")
        self.assertEqual(inst.define.concept[3].code, "medications")
        self.assertEqual(inst.define.concept[3].definition, "A list of medication statements for the patient")
        self.assertEqual(inst.define.concept[3].display, "Medication List")
        self.assertEqual(inst.define.concept[4].code, "problems")
        self.assertEqual(inst.define.concept[4].definition, "A list of problems that the patient is known of have (or have had in the past)")
        self.assertEqual(inst.define.concept[4].display, "Problem List")
        self.assertEqual(inst.define.concept[5].code, "worklist")
        self.assertEqual(inst.define.concept[5].definition, "A list of items that constitute a set of work to be performed (typically this code would be specialised for more specific uses, such as a ward round list)")
        self.assertEqual(inst.define.concept[5].display, "Worklist")
        self.assertEqual(inst.define.concept[6].code, "waiting")
        self.assertEqual(inst.define.concept[6].definition, "A list of items waiting for an event (perhaps a surgical patient waiting list)")
        self.assertEqual(inst.define.concept[6].display, "Waiting List")
        self.assertEqual(inst.define.concept[7].code, "protocols")
        self.assertEqual(inst.define.concept[7].definition, "A set of protocols to be followed")
        self.assertEqual(inst.define.concept[7].display, "Protocols")
        self.assertEqual(inst.define.concept[8].code, "plans")
        self.assertEqual(inst.define.concept[8].definition, "A set of care plans that apply in a particular context of care")
        self.assertEqual(inst.define.concept[8].display, "Care Plans")
        self.assertEqual(inst.define.extension[0].url, "http://hl7.org/fhir/StructureDefinition/valueset-oid")
        self.assertEqual(inst.define.extension[0].valueUri, "urn:oid:null")
        self.assertEqual(inst.define.system, "http://hl7.org/fhir/list-example-use-codes")
        self.assertEqual(inst.description, "Example use codes for the List resource - typical kinds of use. TODO: Does LOINC define useful codes?")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/valueset-oid")
        self.assertEqual(inst.extension[0].valueUri, "urn:oid:2.16.840.1.113883.4.642.2.320")
        self.assertEqual(inst.id, "valueset-list-example-codes")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2015-04-03T14:24:32.000+11:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2015-04-03T14:24:32.000+11:00")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/valueset-shareable-definition")
        self.assertEqual(inst.name, "Example Use Codes for List")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/vs/list-example-codes")
        self.assertEqual(inst.version, "0.5.0")

