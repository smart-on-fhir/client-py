#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import careteam
from .fhirdate import FHIRDate


class CareTeamTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CareTeam", js["resourceType"])
        return careteam.CareTeam(js)
    
    def testCareTeam1(self):
        inst = self.instantiate_from("careteam-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CareTeam instance")
        self.implCareTeam1(inst)
        
        js = inst.as_json()
        self.assertEqual("CareTeam", js["resourceType"])
        inst2 = careteam.CareTeam(js)
        self.implCareTeam1(inst2)
    
    def implCareTeam1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "encounter")
        self.assertEqual(inst.category[0].coding[0].system, "http://hl7.org/fhir/care-team-category")
        self.assertEqual(inst.contained[0].id, "pr1")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.name, "Peter James Charlmers Care Plan for Inpatient Encounter")
        self.assertEqual(inst.participant[0].role.text, "responsiblePerson")
        self.assertEqual(inst.participant[1].period.end.date, FHIRDate("2013-01-01").date)
        self.assertEqual(inst.participant[1].period.end.as_json(), "2013-01-01")
        self.assertEqual(inst.participant[1].role.text, "adviser")
        self.assertEqual(inst.period.end.date, FHIRDate("2013-01-01").date)
        self.assertEqual(inst.period.end.as_json(), "2013-01-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Care Team</div>")
        self.assertEqual(inst.text.status, "generated")

