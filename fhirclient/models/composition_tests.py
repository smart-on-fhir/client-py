#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import composition
from .fhirdate import FHIRDate


class CompositionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Composition", js["resourceType"])
        return composition.Composition(js)
    
    def testComposition1(self):
        inst = self.instantiate_from("composition-example-mixed.json")
        self.assertIsNotNone(inst, "Must have instantiated a Composition instance")
        self.implComposition1(inst)
        
        js = inst.as_json()
        self.assertEqual("Composition", js["resourceType"])
        inst2 = composition.Composition(js)
        self.implComposition1(inst2)
    
    def implComposition1(self, inst):
        self.assertEqual(inst.attester[0].mode, "legal")
        self.assertEqual(inst.attester[0].time.date, FHIRDate("2012-01-04T09:10:14Z").date)
        self.assertEqual(inst.attester[0].time.as_json(), "2012-01-04T09:10:14Z")
        self.assertEqual(inst.category[0].coding[0].code, "LP173421-1")
        self.assertEqual(inst.category[0].coding[0].display, "Report")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.confidentiality, "N")
        self.assertEqual(inst.date.date, FHIRDate("2018-10-30T16:56:04+11:00").date)
        self.assertEqual(inst.date.as_json(), "2018-10-30T16:56:04+11:00")
        self.assertEqual(inst.id, "example-mixed")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.section[0].code.coding[0].code, "newborn")
        self.assertEqual(inst.section[0].code.coding[0].display, "New Born Details")
        self.assertEqual(inst.section[0].code.coding[0].system, "http://acme.org/codes/SectionType")
        self.assertEqual(inst.section[0].text.status, "generated")
        self.assertEqual(inst.section[0].title, "Child's Details")
        self.assertEqual(inst.section[1].code.coding[0].code, "mother")
        self.assertEqual(inst.section[1].code.coding[0].display, "Mother's Details")
        self.assertEqual(inst.section[1].code.coding[0].system, "http://acme.org/codes/SectionType")
        self.assertEqual(inst.section[1].text.status, "generated")
        self.assertEqual(inst.section[1].title, "Mpther's Details")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Discharge Summary (Neonatal Service)")
        self.assertEqual(inst.type.coding[0].code, "78418-1")
        self.assertEqual(inst.type.coding[0].display, "Neonatal perinatal medicine Discharge summary")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testComposition2(self):
        inst = self.instantiate_from("composition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Composition instance")
        self.implComposition2(inst)
        
        js = inst.as_json()
        self.assertEqual("Composition", js["resourceType"])
        inst2 = composition.Composition(js)
        self.implComposition2(inst2)
    
    def implComposition2(self, inst):
        self.assertEqual(inst.attester[0].mode, "legal")
        self.assertEqual(inst.attester[0].time.date, FHIRDate("2012-01-04T09:10:14Z").date)
        self.assertEqual(inst.attester[0].time.as_json(), "2012-01-04T09:10:14Z")
        self.assertEqual(inst.category[0].coding[0].code, "LP173421-1")
        self.assertEqual(inst.category[0].coding[0].display, "Report")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.confidentiality, "N")
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04T09:10:14Z").date)
        self.assertEqual(inst.date.as_json(), "2012-01-04T09:10:14Z")
        self.assertEqual(inst.event[0].code[0].coding[0].code, "HEALTHREC")
        self.assertEqual(inst.event[0].code[0].coding[0].display, "health record")
        self.assertEqual(inst.event[0].code[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.event[0].period.end.date, FHIRDate("2012-11-12").date)
        self.assertEqual(inst.event[0].period.end.as_json(), "2012-11-12")
        self.assertEqual(inst.event[0].period.start.date, FHIRDate("2010-07-18").date)
        self.assertEqual(inst.event[0].period.start.as_json(), "2010-07-18")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://healthintersections.com.au/test")
        self.assertEqual(inst.identifier.value, "1")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatesTo[0].code, "replaces")
        self.assertEqual(inst.relatesTo[1].code, "appends")
        self.assertEqual(inst.relatesTo[1].targetIdentifier.system, "http://example.org/fhir/NamingSystem/document-ids")
        self.assertEqual(inst.relatesTo[1].targetIdentifier.value, "ABC123")
        self.assertEqual(inst.section[0].code.coding[0].code, "11348-0")
        self.assertEqual(inst.section[0].code.coding[0].display, "History of past illness Narrative")
        self.assertEqual(inst.section[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.section[0].mode, "snapshot")
        self.assertEqual(inst.section[0].orderedBy.coding[0].code, "event-date")
        self.assertEqual(inst.section[0].orderedBy.coding[0].display, "Sorted by Event Date")
        self.assertEqual(inst.section[0].orderedBy.coding[0].system, "http://terminology.hl7.org/CodeSystem/list-order")
        self.assertEqual(inst.section[0].text.status, "generated")
        self.assertEqual(inst.section[0].title, "History of present illness")
        self.assertEqual(inst.section[1].code.coding[0].code, "10157-6")
        self.assertEqual(inst.section[1].code.coding[0].display, "History of family member diseases Narrative")
        self.assertEqual(inst.section[1].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.section[1].emptyReason.coding[0].code, "withheld")
        self.assertEqual(inst.section[1].emptyReason.coding[0].display, "Information Withheld")
        self.assertEqual(inst.section[1].emptyReason.coding[0].system, "http://terminology.hl7.org/CodeSystem/list-empty-reason")
        self.assertEqual(inst.section[1].mode, "snapshot")
        self.assertEqual(inst.section[1].text.status, "generated")
        self.assertEqual(inst.section[1].title, "History of family member diseases")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Consultation Note")
        self.assertEqual(inst.type.coding[0].code, "11488-4")
        self.assertEqual(inst.type.coding[0].display, "Consult note")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")

