#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import messagedefinition
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class MessageDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
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
        self.assertEqual(inst.category, "notification")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org")
        self.assertEqual(inst.date.datetime, FHIRDateTime("2016-11-09").datetime)
        self.assertEqual(inst.date.as_json(), "2016-11-09")
        self.assertEqual(inst.eventCoding.code, "admin-notify")
        self.assertEqual(inst.eventCoding.system, "http://example.org/fhir/message-events")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.name, "EXAMPLE")
        self.assertEqual(inst.publisher, "Health Level Seven, Int'l")
        self.assertEqual(inst.purpose, "Defines a base example for other MessageDefinition instances.")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Message definition base example</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Message definition base example")
        self.assertEqual(inst.url, "http://hl7.org/fhir/MessageDefinition/example")

