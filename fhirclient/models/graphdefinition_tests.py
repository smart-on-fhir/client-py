#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import graphdefinition
from .fhirdate import FHIRDate


class GraphDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("GraphDefinition", js["resourceType"])
        return graphdefinition.GraphDefinition(js)
    
    def testGraphDefinition1(self):
        inst = self.instantiate_from("graphdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a GraphDefinition instance")
        self.implGraphDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("GraphDefinition", js["resourceType"])
        inst2 = graphdefinition.GraphDefinition(js)
        self.implGraphDefinition1(inst2)
    
    def implGraphDefinition1(self, inst):
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2015-08-04").date)
        self.assertEqual(inst.date.as_json(), "2015-08-04")
        self.assertEqual(inst.description, "Specify to include list references when generating a document using the $document operation")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.link[0].description, "Link to List")
        self.assertEqual(inst.link[0].path, "Composition.section.entry")
        self.assertEqual(inst.link[0].target[0].compartment[0].code, "Patient")
        self.assertEqual(inst.link[0].target[0].compartment[0].rule, "identical")
        self.assertEqual(inst.link[0].target[0].link[0].description, "Include any list entries")
        self.assertEqual(inst.link[0].target[0].link[0].path, "List.entry.item")
        self.assertEqual(inst.link[0].target[0].link[0].target[0].compartment[0].code, "Patient")
        self.assertEqual(inst.link[0].target[0].link[0].target[0].compartment[0].rule, "identical")
        self.assertEqual(inst.link[0].target[0].link[0].target[0].type, "Resource")
        self.assertEqual(inst.link[0].target[0].type, "List")
        self.assertEqual(inst.name, "Document Generation Template")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.start, "Composition")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://h7.org/fhir/GraphDefinition/example")

