#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11466 on 2017-02-27.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import requestgroup
from .fhirdate import FHIRDate


class RequestGroupTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("RequestGroup", js["resourceType"])
        return requestgroup.RequestGroup(js)
    
    def testRequestGroup1(self):
        inst = self.instantiate_from("requestgroup-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RequestGroup instance")
        self.implRequestGroup1(inst)
        
        js = inst.as_json()
        self.assertEqual("RequestGroup", js["resourceType"])
        inst2 = requestgroup.RequestGroup(js)
        self.implRequestGroup1(inst2)
    
    def implRequestGroup1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

