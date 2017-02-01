#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.10959 on 2017-02-01.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import messagedefinition
from .fhirdate import FHIRDate


class MessageDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MessageDefinition", js["resourceType"])
        return messagedefinition.MessageDefinition(js)
    
    def testMessageDefinition1(self):
        inst = self.instantiate_from("messagedefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MessageDefinition instance")
        self.implMessageDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("MessageDefinition", js["resourceType"])
        inst2 = messagedefinition.MessageDefinition(js)
        self.implMessageDefinition1(inst2)
    
    def implMessageDefinition1(self, inst):
        self.assertEqual(inst.category, "Notification")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org")
        self.assertEqual(inst.date.date, FHIRDate("2016-11-09").date)
        self.assertEqual(inst.date.as_json(), "2016-11-09")
        self.assertEqual(inst.event.code, "patient-link")
        self.assertEqual(inst.event.system, "http://hl7.org/fhir/message-events")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.focus[0].code, "Patient")
        self.assertEqual(inst.focus[0].max, "2")
        self.assertEqual(inst.focus[0].min, 2)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.name, "A24")
        self.assertEqual(inst.publisher, "Health Level Seven, Int'l")
        self.assertEqual(inst.purpose, "Notifies recipient systems that two patients have been 'linked' - meaning they represent the same individual")
        self.assertFalse(inst.responseRequired)
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Link patients notification")
        self.assertEqual(inst.url, "http://hl7.org/fhir/MessageDefinition/example")

