#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import messageheader
from fhirdate import FHIRDate


class MessageHeaderTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = messageheader.MessageHeader(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testMessageHeader1(self):
        inst = self.instantiate_from("messageheader-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e33bcd0> instance")
    
        self.assertEqual(inst.destination[0].endpoint, "llp:10.11.12.14:5432")
        self.assertEqual(inst.destination[0].name, "Acme Message Gateway")
        self.assertEqual(inst.event.code, "admin-update")
        self.assertEqual(inst.event.system, "http://hl7.org/fhir/message-type")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier, "1cbdfb97-5859-48a4-8301-d54eab818d68")
        self.assertEqual(inst.response.code, "ok")
        self.assertEqual(inst.response.identifier, "5015fe84-8e76-4526-89d8-44b322e8d4fb")
        self.assertEqual(inst.source.contact.system, "phone")
        self.assertEqual(inst.source.contact.value, "+1 (555) 123 4567")
        self.assertEqual(inst.source.endpoint, "llp:10.11.12.13:5432")
        self.assertEqual(inst.source.name, "Acme Central Patient Registry")
        self.assertEqual(inst.source.software, "FooBar Patient Manager")
        self.assertEqual(inst.source.version, "3.1.45.AABB")
        self.assertEqual(inst.text.div, "<div>\n      \n      <p>Update Person resource for Peter James CHALMERS (Jim), MRN: 12345 (Acme Healthcare)</p>\n    \n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.timestamp.date, FHIRDate("2012-01-04T09:10:14Z").date)
        self.assertEqual(inst.timestamp.isostring, "2012-01-04T09:10:14Z")

