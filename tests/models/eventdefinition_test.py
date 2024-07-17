#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import eventdefinition
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class EventDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EventDefinition", js["resourceType"])
        return eventdefinition.EventDefinition(js)
    
    def testEventDefinition1(self):
        inst = self.instantiate_from("eventdefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EventDefinition instance")
        self.implEventDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("EventDefinition", js["resourceType"])
        inst2 = eventdefinition.EventDefinition(js)
        self.implEventDefinition1(inst2)
    
    def implEventDefinition1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.purpose, "Monitor all admissions to Emergency")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.trigger[0].condition.description, "Encounter Location = emergency (active/completed encounters, current or previous)")
        self.assertEqual(inst.trigger[0].condition.expression, "(this | %previous).location.where(location = 'Location/emergency' and status in {'active', 'completed'}).exists()")
        self.assertEqual(inst.trigger[0].condition.language, "text/fhirpath")
        self.assertEqual(inst.trigger[0].data[0].type, "Encounter")
        self.assertEqual(inst.trigger[0].name, "monitor-emergency-admissions")
        self.assertEqual(inst.trigger[0].type, "named-event")

