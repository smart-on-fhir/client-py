#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import binary
from .fhirdate import FHIRDate


class BinaryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Binary", js["resourceType"])
        return binary.Binary(js)
    
    def testBinary1(self):
        inst = self.instantiate_from("binary-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Binary instance")
        self.implBinary1(inst)
        
        js = inst.as_json()
        self.assertEqual("Binary", js["resourceType"])
        inst2 = binary.Binary(js)
        self.implBinary1(inst2)
    
    def implBinary1(self, inst):
        self.assertEqual(inst.contentType, "application/pdf")
        self.assertEqual(inst.id, "example")

