#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-06-19.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import contract
from fhirdate import FHIRDate


class ContractTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        return contract.Contract(js)
    
    def testContract1(self):
        inst = self.instantiate_from("contract-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract1(inst)
        inst2 = contract.Contract(inst.as_json())
        self.implContract1(inst2)
    
    def implContract1(self, inst):
        self.assertEqual(inst.id, "C-123")
        self.assertEqual(inst.text.div, "<div>A human-readable rendering of the contract</div>")
        self.assertEqual(inst.text.status, "generated")

