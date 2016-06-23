#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import account
from .fhirdate import FHIRDate


class AccountTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Account", js["resourceType"])
        return account.Account(js)
    
    def testAccount1(self):
        inst = self.instantiate_from("account-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Account instance")
        self.implAccount1(inst)
        
        js = inst.as_json()
        self.assertEqual("Account", js["resourceType"])
        inst2 = account.Account(js)
        self.implAccount1(inst2)
    
    def implAccount1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

