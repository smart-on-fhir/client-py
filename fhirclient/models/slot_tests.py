#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


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
        self.assertEqual(inst.freeBusyType, "busy")
        self.assertEqual(inst.id, "1")
        self.assertEqual(inst.identifier[0].system, "http://example.org/identifiers/slots")
        self.assertEqual(inst.identifier[0].value, "123132")
        self.assertTrue(inst.overbooked)
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:00:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:00:00Z")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "45")
        self.assertEqual(inst.type.coding[0].display, "Physiotherapy")
    
    def testSlot2(self):
        inst = self.instantiate_from("slot-example-tentative.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot2(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot2(inst2)
    
    def implSlot2(self, inst):
        self.assertEqual(inst.comment, "Dr Careful is out of the office")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T10:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T10:00:00Z")
        self.assertEqual(inst.freeBusyType, "busy-tentative")
        self.assertEqual(inst.id, "2")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:45:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:45:00Z")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "45")
        self.assertEqual(inst.type.coding[0].display, "Physiotherapy")
    
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
        self.assertEqual(inst.freeBusyType, "busy-unavailable")
        self.assertEqual(inst.id, "3")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "45")
        self.assertEqual(inst.type.coding[0].display, "Physiotherapy")
    
    def testSlot4(self):
        inst = self.instantiate_from("slot-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Slot instance")
        self.implSlot4(inst)
        
        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot4(inst2)
    
    def implSlot4(self, inst):
        self.assertEqual(inst.comment, "Assessments should be performed before requesting appointments in this slot.")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.freeBusyType, "free")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "45")
        self.assertEqual(inst.type.coding[0].display, "Physiotherapy")

