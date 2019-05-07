#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import slot
from .fhirdate import FHIRDate


class SlotTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Slot", js["resourceType"])
        return slot.Slot(js)
    
    def testSlot1(self):
        inst = self.instantiate_from("slot-example-busy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot1(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot1(inst2)
    
    def implSlot1(self, inst):
        self.assertEqual(inst.comment, "Assessments should be performed before requesting appointments in this slot.")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(inst.id, "1")
        self.assertEqual(inst.identifier[0].system, "http://example.org/identifiers/slots")
        self.assertEqual(inst.identifier[0].value, "123132")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertTrue(inst.overbooked)
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "General Practice")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:00:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:00:00Z")
        self.assertEqual(inst.status, "busy")
        self.assertEqual(inst.text.status, "generated")
    
    def testSlot2(self):
        inst = self.instantiate_from("slot-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot2(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot2(inst2)
    
    def implSlot2(self, inst):
        self.assertEqual(inst.appointmentType.coding[0].code, "WALKIN")
        self.assertEqual(inst.appointmentType.coding[0].display, "A previously unscheduled walk-in visit")
        self.assertEqual(inst.appointmentType.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0276")
        self.assertEqual(inst.comment, "Assessments should be performed before requesting appointments in this slot.")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "General Practice")
        self.assertEqual(inst.serviceType[0].coding[0].code, "57")
        self.assertEqual(inst.serviceType[0].coding[0].display, "Immunization")
        self.assertEqual(inst.specialty[0].coding[0].code, "408480009")
        self.assertEqual(inst.specialty[0].coding[0].display, "Clinical immunology")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(inst.status, "free")
        self.assertEqual(inst.text.status, "generated")
    
    def testSlot3(self):
        inst = self.instantiate_from("slot-example-unavailable.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot3(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot3(inst2)
    
    def implSlot3(self, inst):
        self.assertEqual(inst.comment, "Dr Careful is out of the office")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:45:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:45:00Z")
        self.assertEqual(inst.id, "3")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "General Practice")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.status, "busy-unavailable")
        self.assertEqual(inst.text.status, "generated")
    
    def testSlot4(self):
        inst = self.instantiate_from("slot-example-tentative.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot4(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot4(inst2)
    
    def implSlot4(self, inst):
        self.assertEqual(inst.comment, "Dr Careful is out of the office")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T10:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T10:00:00Z")
        self.assertEqual(inst.id, "2")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "General Practice")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:45:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:45:00Z")
        self.assertEqual(inst.status, "busy-tentative")
        self.assertEqual(inst.text.status, "generated")

