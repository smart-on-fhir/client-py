#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.10959 on 2017-02-01.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import practitionerrole
from .fhirdate import FHIRDate


class PractitionerRoleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PractitionerRole", js["resourceType"])
        return practitionerrole.PractitionerRole(js)
    
    def testPractitionerRole1(self):
        inst = self.instantiate_from("practitionerrole-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a PractitionerRole instance")
        self.implPractitionerRole1(inst)
        
        js = inst.as_json()
        self.assertEqual("PractitionerRole", js["resourceType"])
        inst2 = practitionerrole.PractitionerRole(js)
        self.implPractitionerRole1(inst2)
    
    def implPractitionerRole1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.code[0].coding[0].code, "RP")
        self.assertEqual(inst.code[0].coding[0].system, "http://hl7.org/fhir/v2/0286")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://www.acme.org/practitioners")
        self.assertEqual(inst.identifier[0].value, "23")
        self.assertEqual(inst.period.end.date, FHIRDate("2012-03-31").date)
        self.assertEqual(inst.period.end.as_json(), "2012-03-31")
        self.assertEqual(inst.period.start.date, FHIRDate("2012-01-01").date)
        self.assertEqual(inst.period.start.as_json(), "2012-01-01")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "home")
        self.assertEqual(inst.telecom[0].value, "(03) 5555 6473")
        self.assertEqual(inst.text.status, "generated")

