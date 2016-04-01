#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 on 2016-04-01.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import moduledefinition
from .fhirdate import FHIRDate


class ModuleDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ModuleDefinition", js["resourceType"])
        return moduledefinition.ModuleDefinition(js)
    
    def testModuleDefinition1(self):
        inst = self.instantiate_from("moduledefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ModuleDefinition instance")
        self.implModuleDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("ModuleDefinition", js["resourceType"])
        inst2 = moduledefinition.ModuleDefinition(js)
        self.implModuleDefinition1(inst2)
    
    def implModuleDefinition1(self, inst):
        self.assertEqual(inst.data[0].codeFilter[0].path, "code")
        self.assertEqual(inst.data[0].codeFilter[0].valueSetString, "Other Female Reproductive Conditions")
        self.assertEqual(inst.data[0].type, "Condition")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "ChalmydiaScreening_Common")
        self.assertEqual(inst.model[0].identifier, "QUICK")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueSet[0].identifier, "2.16.840.1.113883.3.560.100.2")
        self.assertEqual(inst.valueSet[0].name, "Female Administrative Sex")
        self.assertEqual(inst.version, "2.0.0")

