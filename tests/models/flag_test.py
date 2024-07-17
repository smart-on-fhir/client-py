#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import flag
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class FlagTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Flag", js["resourceType"])
        return flag.Flag(js)
    
    def testFlag1(self):
        inst = self.instantiate_from("flag-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Flag instance")
        self.implFlag1(inst)
        
        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag1(inst2)
    
    def implFlag1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "safety")
        self.assertEqual(inst.category[0].coding[0].display, "Safety")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/flag-category")
        self.assertEqual(inst.category[0].text, "Safety")
        self.assertEqual(inst.code.coding[0].code, "bigdog")
        self.assertEqual(inst.code.coding[0].display, "Big dog")
        self.assertEqual(inst.code.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.code.text, "Patient has a big dog at his home. Always always wear a suit of armor or take other active counter-measures")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.datetime, FHIRDateTime("2016-12-01").datetime)
        self.assertEqual(inst.period.end.as_json(), "2016-12-01")
        self.assertEqual(inst.period.start.datetime, FHIRDateTime("2015-01-17").datetime)
        self.assertEqual(inst.period.start.as_json(), "2015-01-17")
        self.assertEqual(inst.status, "inactive")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Large Dog warning for Peter Patient</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testFlag2(self):
        inst = self.instantiate_from("flag-example-encounter.json")
        self.assertIsNotNone(inst, "Must have instantiated a Flag instance")
        self.implFlag2(inst)
        
        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag2(inst2)
    
    def implFlag2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "infection")
        self.assertEqual(inst.category[0].coding[0].display, "Infection Control Level")
        self.assertEqual(inst.category[0].coding[0].system, "http://example.org/local")
        self.assertEqual(inst.code.coding[0].code, "l3")
        self.assertEqual(inst.code.coding[0].display, "Follow Level 3 Protocol")
        self.assertEqual(inst.code.coding[0].system, "http://example.org/local/if1")
        self.assertEqual(inst.id, "example-encounter")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Follow Infection Control Level 3 Protocol</div>")
        self.assertEqual(inst.text.status, "generated")

