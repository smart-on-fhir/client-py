#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import slot
from fhirdate import FHIRDate


class SlotTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = slot.Slot(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testSlot1(self):
        inst = self.instantiate_from("slot-example-busy.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e398610> instance")
    
        self.assertEqual(inst.comment, "Assessments should be performed before requesting appointments in this slot.")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.end.isostring, "2013-12-25T09:15:00Z")
        self.assertEqual(inst.freeBusyType, "BUSY")
        self.assertEqual(inst.id, "1")
        self.assertEqual(inst.identifier[0].system, "http://example.org/identifiers/slots")
        self.assertEqual(inst.identifier[0].value, "123132")
        self.assertTrue(inst.overbooked)
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:00:00Z").date)
        self.assertEqual(inst.start.isostring, "2013-12-25T09:00:00Z")
        self.assertEqual(inst.text.div, "<div>\n			25 Dec 2013 9:00am - 9:15am: \n      <b>Busy</b> Physiotherapy\n		\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "45")
        self.assertEqual(inst.type.coding[0].display, "Physiotherapy")
    
    def testSlot2(self):
        inst = self.instantiate_from("slot-example-tentative.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e398610> instance")
    
        self.assertEqual(inst.comment, "Dr Careful is out of the office")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T10:00:00Z").date)
        self.assertEqual(inst.end.isostring, "2013-12-25T10:00:00Z")
        self.assertEqual(inst.freeBusyType, "BUSY-TENTATIVE")
        self.assertEqual(inst.id, "2")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:45:00Z").date)
        self.assertEqual(inst.start.isostring, "2013-12-25T09:45:00Z")
        self.assertEqual(inst.text.div, "<div>\n			25 Dec 2013 9:45am - 10:00am: \n      <b>Tentative</b> Physiotherapy\n		\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "45")
        self.assertEqual(inst.type.coding[0].display, "Physiotherapy")
    
    def testSlot3(self):
        inst = self.instantiate_from("slot-example-unavailable.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e398610> instance")
    
        self.assertEqual(inst.comment, "Dr Careful is out of the office")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:45:00Z").date)
        self.assertEqual(inst.end.isostring, "2013-12-25T09:45:00Z")
        self.assertEqual(inst.freeBusyType, "BUSY-UNAVAILABLE")
        self.assertEqual(inst.id, "3")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.start.isostring, "2013-12-25T09:30:00Z")
        self.assertEqual(inst.text.div, "<div>\n			25 Dec 2013 9:30am - 9:45am: \n      <b>Unavailable</b> Physiotherapy\n      <br/>\n			Dr Careful is out of the office\n		\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "45")
        self.assertEqual(inst.type.coding[0].display, "Physiotherapy")
    
    def testSlot4(self):
        inst = self.instantiate_from("slot-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e398610> instance")
    
        self.assertEqual(inst.comment, "Assessments should be performed before requesting appointments in this slot.")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-25T09:30:00Z").date)
        self.assertEqual(inst.end.isostring, "2013-12-25T09:30:00Z")
        self.assertEqual(inst.freeBusyType, "FREE")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-25T09:15:00Z").date)
        self.assertEqual(inst.start.isostring, "2013-12-25T09:15:00Z")
        self.assertEqual(inst.text.div, "<div>\n			25 Dec 2013 9:15am - 9:30am: \n      <b>Busy</b> Physiotherapy\n		\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "45")
        self.assertEqual(inst.type.coding[0].display, "Physiotherapy")

