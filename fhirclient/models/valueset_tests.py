#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from valueset import ValueSet
from fhirdate import FHIRDate


class ValueSetTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = ValueSet(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testValueSet1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/valueset-list-example-codes.json")
        self.assertIsNotNone(inst, "Must have instantiated a ValueSet instance")
    
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
        self.assertEqual(inst.define.system, "http://hl7.org/fhir/list-example-use-codes")
        self.assertEqual(inst.description, "Example use codes for the List resource - typical kinds of use. TODO: Does LOINC define useful codes?")
        self.assertEqual(inst.identifier, "http://hl7.org/fhir/vs/list-example-codes")
        self.assertEqual(inst.name, "Example Use Codes for List")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.telecom[0].system, "url")
        self.assertEqual(inst.telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.text.div, "<div><h2>Example Use Codes for List</h2><p>Example use codes for the List resource - typical kinds of use. TODO: Does LOINC define useful codes?</p><p>This value set defines its own terms in the system http://hl7.org/fhir/list-example-use-codes</p><table><tr><td><b>Code</b></td><td><b>Display</b></td><td><b>Definition</b></td></tr><tr><td>alerts<a name=\"alerts\"> </a></td><td>Alerts</td><td>A list of alerts for the patient</td></tr><tr><td>adverserxns<a name=\"adverserxns\"> </a></td><td>Adverse Reactions</td><td>A list of part adverse reactions</td></tr><tr><td>allergies<a name=\"allergies\"> </a></td><td>Allergies</td><td>A list of Allergies for the patient</td></tr><tr><td>medications<a name=\"medications\"> </a></td><td>Medication List</td><td>A list of medication statements for the patient</td></tr><tr><td>problems<a name=\"problems\"> </a></td><td>Problem List</td><td>A list of problems that the patient is known of have (or have had in the past)</td></tr><tr><td>worklist<a name=\"worklist\"> </a></td><td>Worklist</td><td>A list of items that constitute a set of work to be performed (typically this code would be specialised for more specific uses, such as a ward round list)</td></tr><tr><td>waiting<a name=\"waiting\"> </a></td><td>Waiting List</td><td>A list of items waiting for an event (perhaps a surgical patient waiting list)</td></tr><tr><td>protocols<a name=\"protocols\"> </a></td><td>Protocols</td><td>A set of protocols to be followed</td></tr><tr><td>plans<a name=\"plans\"> </a></td><td>Care Plans</td><td>A set of care plans that apply in a particular context of care</td></tr></table></div>")
        self.assertEqual(inst.text.status, "generated")

