#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from order import Order
from fhirdate import FHIRDate


class OrderTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = Order(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testOrder1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/order-example-f201-physiotherapy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Order instance")
    
        self.assertEqual(inst.date.date, FHIRDate("2013-03-05T12:00:00+01:00").date)
        self.assertEqual(inst.date.isostring, "2013-03-05T12:00:00+01:00")
        self.assertEqual(inst.detail[0].display, "Consultation, not yet developed")
        self.assertEqual(inst.reasonCodeableConcept.text, "It concerns a one-off order for consultation in order to evaluate the stairs walking ability of Roel.")
        self.assertEqual(inst.source.reference, "Practitioner/f201")
        self.assertEqual(inst.subject.display, "Roel")
        self.assertEqual(inst.subject.reference, "Patient/f201")
        self.assertEqual(inst.target.display, "Juri van Gelder")
        self.assertEqual(inst.target.reference, "Practitioner/f203")
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>date</b>: 5-Mar 2013 12:0\n      </p>\n      <p>\n        <b>subject</b>: Roel\n      </p>\n      <p>\n        <b>source</b>: \n        <a href=\"practitioner-example-f201-ab.html\">UZI-nummer = 12345678901 (official); Dokter Bronsig(official); Male; birthDate: 24-Dec 1956; Implementation of planned interventions; Medical oncologist</a>\n      </p>\n      <p>\n        <b>target</b>: Juri van Gelder\n      </p>\n      <p>\n        <b>reason[x]</b>: \n        <span title=\"Codes: \">It concerns a one-off order for consultation in order to evaluate the stairs walking ability of Roel.</span>\n      </p>\n      <h3>Whens</h3>\n      <table class=\"grid\">\n        <tr>\n          <td>\n            <b>Code</b>\n          </td>\n          <td>\n            <b>Schedule</b>\n          </td>\n        </tr>\n        <tr>\n          <td>\n            <span title=\"Codes: {http://snomed.info/sct 394848005}\">Normal priority</span>\n          </td>\n          <td> </td>\n        </tr>\n      </table>\n      <p>\n        <b>detail</b>: Consultation, not yet developed\n      </p>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.when.code.coding[0].code, "394848005")
        self.assertEqual(inst.when.code.coding[0].display, "Normal priority")
        self.assertEqual(inst.when.code.coding[0].system, "http://snomed.info/sct")

