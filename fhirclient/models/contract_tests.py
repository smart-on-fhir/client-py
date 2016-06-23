#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import contract
from .fhirdate import FHIRDate


class ContractTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Contract", js["resourceType"])
        return contract.Contract(js)
    
    def testContract1(self):
        inst = self.instantiate_from("contract-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract1(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract1(inst2)
    
    def implContract1(self, inst):
        self.assertEqual(inst.id, "C-123")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the contract</div>")
        self.assertEqual(inst.text.status, "generated")

