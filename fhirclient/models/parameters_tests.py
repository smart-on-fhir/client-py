#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import parameters
from fhirdate import FHIRDate


class ParametersTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = parameters.Parameters(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testParameters1(self):
        inst = self.instantiate_from("parameters-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e214a50> instance")
    
        self.assertEqual(inst.parameter[0].name, "start")
        self.assertEqual(inst.parameter[0].valueDate.date, FHIRDate("2010-01-01").date)
        self.assertEqual(inst.parameter[0].valueDate.isostring, "2010-01-01")
        self.assertEqual(inst.parameter[1].name, "end")

