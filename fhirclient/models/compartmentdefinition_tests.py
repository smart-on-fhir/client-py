#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import compartmentdefinition
from .fhirdate import FHIRDate


class CompartmentDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CompartmentDefinition", js["resourceType"])
        return compartmentdefinition.CompartmentDefinition(js)
    
    def testCompartmentDefinition1(self):
        inst = self.instantiate_from("compartmentdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CompartmentDefinition instance")
        self.implCompartmentDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("CompartmentDefinition", js["resourceType"])
        inst2 = compartmentdefinition.CompartmentDefinition(js)
        self.implCompartmentDefinition1(inst2)
    
    def implCompartmentDefinition1(self, inst):
        self.assertEqual(inst.code, "Device")
        self.assertEqual(inst.contact[0].name, "[string]")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2017-02-24").date)
        self.assertEqual(inst.date.as_json(), "2017-02-24")
        self.assertEqual(inst.description, "The set of resources associated with a particular Device (example with Communication and CommunicationRequest resourses only).")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.name, "EXAMPLE")
        self.assertEqual(inst.publisher, "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.purpose, "Provides an example of a FHIR compartment definition based on the Device resource type.")
        self.assertEqual(inst.resource[0].code, "Communication")
        self.assertEqual(inst.resource[0].documentation, "The device used as the message sender and recipient")
        self.assertEqual(inst.resource[0].param[0], "sender")
        self.assertEqual(inst.resource[0].param[1], "recipient")
        self.assertEqual(inst.resource[1].code, "CommunicationRequest")
        self.assertEqual(inst.resource[1].documentation, "The device used as the message sender and recipient")
        self.assertEqual(inst.resource[1].param[0], "sender")
        self.assertEqual(inst.resource[1].param[1], "recipient")
        self.assertTrue(inst.search)
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/CompartmentDefinition/example")
        self.assertEqual(inst.useContext[0].code.code, "focus")
        self.assertEqual(inst.useContext[0].code.system, "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code, "Device")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system, "http://hl7.org/fhir/resource-types")

