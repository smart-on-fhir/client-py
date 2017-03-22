#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import servicedefinition
from .fhirdate import FHIRDate


class ServiceDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ServiceDefinition", js["resourceType"])
        return servicedefinition.ServiceDefinition(js)
    
    def testServiceDefinition1(self):
        inst = self.instantiate_from("servicedefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceDefinition instance")
        self.implServiceDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceDefinition", js["resourceType"])
        inst2 = servicedefinition.ServiceDefinition(js)
        self.implServiceDefinition1(inst2)
    
    def implServiceDefinition1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.date.as_json(), "2015-07-22")
        self.assertEqual(inst.description, "Guideline appropriate ordering is used to assess appropriateness of an order given a patient, a proposed order, and a set of clinical indications.")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "guildeline-appropriate-ordering")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Guideline Appropriate Ordering Module")
        self.assertEqual(inst.topic[0].text, "Guideline Appropriate Ordering")
        self.assertEqual(inst.topic[1].text, "Appropriate Use Criteria")
        self.assertEqual(inst.version, "1.0.0")

