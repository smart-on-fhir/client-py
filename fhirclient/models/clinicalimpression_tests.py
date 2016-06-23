#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import clinicalimpression
from .fhirdate import FHIRDate


class ClinicalImpressionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ClinicalImpression", js["resourceType"])
        return clinicalimpression.ClinicalImpression(js)
    
    def testClinicalImpression1(self):
        inst = self.instantiate_from("clinicalimpression-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ClinicalImpression instance")
        self.implClinicalImpression1(inst)
        
        js = inst.as_json()
        self.assertEqual("ClinicalImpression", js["resourceType"])
        inst2 = clinicalimpression.ClinicalImpression(js)
        self.implClinicalImpression1(inst2)
    
    def implClinicalImpression1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2014-12-06T22:33:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2014-12-06T22:33:00+11:00")
        self.assertEqual(inst.description, "This 26 yo male patient is brought into ER by ambulance after being involved in a motor vehicle accident")
        self.assertEqual(inst.finding[0].item.coding[0].code, "850.0")
        self.assertEqual(inst.finding[0].item.coding[0].system, "http://hl7.org/fhir/sid/icd-9")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.investigations[0].code.text, "Initial Examination")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.summary, "provisional diagnoses of laceration of head and traumatic brain injury (TBI)")
        self.assertEqual(inst.text.status, "generated")

