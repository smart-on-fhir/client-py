#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import diagnosticorder
from .fhirdate import FHIRDate


class DiagnosticOrderTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DiagnosticOrder", js["resourceType"])
        return diagnosticorder.DiagnosticOrder(js)
    
    def testDiagnosticOrder1(self):
        inst = self.instantiate_from("diagnosticorder-example-di.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticOrder instance")
        self.implDiagnosticOrder1(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticOrder", js["resourceType"])
        inst2 = diagnosticorder.DiagnosticOrder(js)
        self.implDiagnosticOrder1(inst2)
    
    def implDiagnosticOrder1(self, inst):
        self.assertEqual(inst.event[0].dateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.event[0].dateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.event[0].status, "requested")
        self.assertEqual(inst.id, "di")
        self.assertEqual(inst.item[0].bodySite.coding[0].code, "51185008")
        self.assertEqual(inst.item[0].bodySite.coding[0].display, "Thoracic structure")
        self.assertEqual(inst.item[0].bodySite.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.item[0].code.coding[0].code, "24627-2")
        self.assertEqual(inst.item[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.item[0].code.text, "Chest CT")
        self.assertEqual(inst.reason[0].text, "Check for metastatic disease")
        self.assertEqual(inst.status, "requested")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticOrder2(self):
        inst = self.instantiate_from("diagnosticorder-example-ft4.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticOrder instance")
        self.implDiagnosticOrder2(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticOrder", js["resourceType"])
        inst2 = diagnosticorder.DiagnosticOrder(js)
        self.implDiagnosticOrder2(inst2)
    
    def implDiagnosticOrder2(self, inst):
        self.assertEqual(inst.contained[0].id, "rtt")
        self.assertEqual(inst.event[0].dateTime.date, FHIRDate("2015-08-27T09:33:27+07:00").date)
        self.assertEqual(inst.event[0].dateTime.as_json(), "2015-08-27T09:33:27+07:00")
        self.assertEqual(inst.event[0].status, "requested")
        self.assertEqual(inst.id, "ft4")
        self.assertEqual(inst.item[0].code.coding[0].code, "3024-7")
        self.assertEqual(inst.item[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.item[0].code.text, "Free T4")
        self.assertEqual(inst.status, "requested")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticOrder3(self):
        inst = self.instantiate_from("diagnosticorder-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticOrder instance")
        self.implDiagnosticOrder3(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticOrder", js["resourceType"])
        inst2 = diagnosticorder.DiagnosticOrder(js)
        self.implDiagnosticOrder3(inst2)
    
    def implDiagnosticOrder3(self, inst):
        self.assertEqual(inst.contained[0].id, "fasting")
        self.assertEqual(inst.event[0].dateTime.date, FHIRDate("2013-05-02T16:16:00-07:00").date)
        self.assertEqual(inst.event[0].dateTime.as_json(), "2013-05-02T16:16:00-07:00")
        self.assertEqual(inst.event[0].status, "requested")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "PLAC")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "2345234234234")
        self.assertEqual(inst.item[0].code.coding[0].code, "LIPID")
        self.assertEqual(inst.item[0].code.coding[0].system, "http://acme.org/tests")
        self.assertEqual(inst.item[0].code.text, "Lipid Panel")
        self.assertEqual(inst.note[0].text, "patient is afraid of needles")
        self.assertEqual(inst.reason[0].coding[0].code, "V173")
        self.assertEqual(inst.reason[0].coding[0].display, "Fam hx-ischem heart dis")
        self.assertEqual(inst.reason[0].coding[0].system, "http://hl7.org/fhir/sid/icd-9")
        self.assertEqual(inst.status, "received")
        self.assertEqual(inst.text.status, "generated")

