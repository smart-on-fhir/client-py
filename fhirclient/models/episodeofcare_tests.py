#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import episodeofcare
from .fhirdate import FHIRDate


class EpisodeOfCareTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EpisodeOfCare", js["resourceType"])
        return episodeofcare.EpisodeOfCare(js)
    
    def testEpisodeOfCare1(self):
        inst = self.instantiate_from("episodeofcare-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EpisodeOfCare instance")
        self.implEpisodeOfCare1(inst)
        
        js = inst.as_json()
        self.assertEqual("EpisodeOfCare", js["resourceType"])
        inst2 = episodeofcare.EpisodeOfCare(js)
        self.implEpisodeOfCare1(inst2)
    
    def implEpisodeOfCare1(self, inst):
        self.assertEqual(inst.diagnosis[0].rank, 1)
        self.assertEqual(inst.diagnosis[0].role.coding[0].code, "CC")
        self.assertEqual(inst.diagnosis[0].role.coding[0].display, "Chief complaint")
        self.assertEqual(inst.diagnosis[0].role.coding[0].system, "http://hl7.org/fhir/diagnosis-role")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org/sampleepisodeofcare-identifier")
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-09-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-09-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.statusHistory[0].period.end.date, FHIRDate("2014-09-14").date)
        self.assertEqual(inst.statusHistory[0].period.end.as_json(), "2014-09-14")
        self.assertEqual(inst.statusHistory[0].period.start.date, FHIRDate("2014-09-01").date)
        self.assertEqual(inst.statusHistory[0].period.start.as_json(), "2014-09-01")
        self.assertEqual(inst.statusHistory[0].status, "planned")
        self.assertEqual(inst.statusHistory[1].period.end.date, FHIRDate("2014-09-21").date)
        self.assertEqual(inst.statusHistory[1].period.end.as_json(), "2014-09-21")
        self.assertEqual(inst.statusHistory[1].period.start.date, FHIRDate("2014-09-15").date)
        self.assertEqual(inst.statusHistory[1].period.start.as_json(), "2014-09-15")
        self.assertEqual(inst.statusHistory[1].status, "active")
        self.assertEqual(inst.statusHistory[2].period.end.date, FHIRDate("2014-09-24").date)
        self.assertEqual(inst.statusHistory[2].period.end.as_json(), "2014-09-24")
        self.assertEqual(inst.statusHistory[2].period.start.date, FHIRDate("2014-09-22").date)
        self.assertEqual(inst.statusHistory[2].period.start.as_json(), "2014-09-22")
        self.assertEqual(inst.statusHistory[2].status, "onhold")
        self.assertEqual(inst.statusHistory[3].period.start.date, FHIRDate("2014-09-25").date)
        self.assertEqual(inst.statusHistory[3].period.start.as_json(), "2014-09-25")
        self.assertEqual(inst.statusHistory[3].status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "hacc")
        self.assertEqual(inst.type[0].coding[0].display, "Home and Community Care")
        self.assertEqual(inst.type[0].coding[0].system, "http://hl7.org/fhir/episodeofcare-type")

