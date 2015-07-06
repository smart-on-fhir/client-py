#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import provenance
from .fhirdate import FHIRDate


class ProvenanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Provenance", js["resourceType"])
        return provenance.Provenance(js)
    
    def testProvenance1(self):
        inst = self.instantiate_from("provenance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance1(inst)
        
        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance1(inst2)
    
    def implProvenance1(self, inst):
        self.assertEqual(inst.agent[0].display, "Grahame Grieve")
        self.assertEqual(inst.agent[0].referenceUri, "mailto:grahame@healthintersections.com.au")
        self.assertEqual(inst.agent[0].role.code, "author")
        self.assertEqual(inst.agent[0].role.system, "http://hl7.org/fhir/provenance-participant-role")
        self.assertEqual(inst.agent[0].type.code, "person")
        self.assertEqual(inst.agent[0].type.system, "http://hl7.org/fhir/provenance-participant-type")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.period.start.date, FHIRDate("2011-06-23").date)
        self.assertEqual(inst.period.start.as_json(), "2011-06-23")
        self.assertEqual(inst.reason.text, "Editing the FHIR Specification")
        self.assertEqual(inst.recorded.date, FHIRDate("2012-11-08T23:16:03+11:00").date)
        self.assertEqual(inst.recorded.as_json(), "2012-11-08T23:16:03+11:00")
        self.assertEqual(inst.text.div, "<div>Authored on 8-Nov 2011 by Grahame Grieve. Content extracted from ISO-21090</div>")
        self.assertEqual(inst.text.status, "generated")

