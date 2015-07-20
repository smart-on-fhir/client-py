#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


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
        self.assertEqual(inst.item[0].code.coding[0].code, "24627-2")
        self.assertEqual(inst.item[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.item[0].code.text, "Chest CT")
        self.assertEqual(inst.status, "requested")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticOrder2(self):
        inst = self.instantiate_from("diagnosticorder-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticOrder instance")
        self.implDiagnosticOrder2(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticOrder", js["resourceType"])
        inst2 = diagnosticorder.DiagnosticOrder(js)
        self.implDiagnosticOrder2(inst2)
    
    def implDiagnosticOrder2(self, inst):
        self.assertEqual(inst.event[0].dateTime.date, FHIRDate("2013-05-02T16:16:00-07:00").date)
        self.assertEqual(inst.event[0].dateTime.as_json(), "2013-05-02T16:16:00-07:00")
        self.assertEqual(inst.event[0].status, "requested")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "2345234234234")
        self.assertEqual(inst.item[0].code.coding[0].code, "LIPID")
        self.assertEqual(inst.item[0].code.coding[0].system, "http://acme.org/tests")
        self.assertEqual(inst.item[0].code.text, "Lipid Panel")
        self.assertEqual(inst.status, "received")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticOrder3(self):
        inst = self.instantiate_from("diagnosticorder-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticOrder instance")
        self.implDiagnosticOrder3(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticOrder", js["resourceType"])
        inst2 = diagnosticorder.DiagnosticOrder(js)
        self.implDiagnosticOrder3(inst2)
    
    def implDiagnosticOrder3(self, inst):
        self.assertEqual(inst.event[0].dateTime.date, FHIRDate("2013-05-02T16:16:00-07:00").date)
        self.assertEqual(inst.event[0].dateTime.as_json(), "2013-05-02T16:16:00-07:00")
        self.assertEqual(inst.event[0].status, "requested")
        self.assertEqual(inst.event[1].dateTime.date, FHIRDate("2013-05-06T11:20:00-07:00").date)
        self.assertEqual(inst.event[1].dateTime.as_json(), "2013-05-06T11:20:00-07:00")
        self.assertEqual(inst.event[1].status, "rejected")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/diagnosticorder-reason")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "PHY")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "Physician request")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/diagnosticorder-reasonRejected")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].code, "NON-AVAIL")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].display, "patient not-available")
        self.assertEqual(inst.extension[1].valueCodeableConcept.coding[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "2345234234234")
        self.assertEqual(inst.item[0].code.coding[0].code, "57698-3")
        self.assertEqual(inst.item[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.item[0].code.text, "Lipid panel with direct LDL - Serum or Plasma")
        self.assertEqual(inst.status, "rejected")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticOrder4(self):
        inst = self.instantiate_from("do-uslab-example1.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticOrder instance")
        self.implDiagnosticOrder4(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticOrder", js["resourceType"])
        inst2 = diagnosticorder.DiagnosticOrder(js)
        self.implDiagnosticOrder4(inst2)
    
    def implDiagnosticOrder4(self, inst):
        self.assertEqual(inst.clinicalNotes, "Screening for blood lead")
        self.assertEqual(inst.event[0].dateTime.date, FHIRDate("2014-12-04T15:42:15-08:00").date)
        self.assertEqual(inst.event[0].dateTime.as_json(), "2014-12-04T15:42:15-08:00")
        self.assertEqual(inst.event[0].description.coding[0].code, "new-request")
        self.assertEqual(inst.event[0].status, "requested")
        self.assertEqual(inst.id, "uslab-example1")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.840.1.113883.3.72.5.24")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "ORD000123A")
        self.assertEqual(inst.item[0].code.coding[0].code, "5671-3")
        self.assertEqual(inst.item[0].code.coding[0].display, "Lead [Mass/volume] in Blood")
        self.assertEqual(inst.item[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.item[0].code.coding[1].code, "BLDLD")
        self.assertEqual(inst.item[0].code.coding[1].display, "Blood Lead")
        self.assertEqual(inst.item[0].code.coding[1].system, "urn:oid:2.16.840.1.113883.3.72.5.24")
        self.assertEqual(inst.item[0].code.text, "Blood Lead")
        self.assertEqual(inst.item[0].status, "requested")
        self.assertEqual(inst.priority, "routine")
        self.assertEqual(inst.status, "requested")
        self.assertEqual(inst.text.status, "generated")

