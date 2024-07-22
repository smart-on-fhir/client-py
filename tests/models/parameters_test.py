#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import parameters
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class ParametersTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Parameters", js["resourceType"])
        return parameters.Parameters(js)
    
    def testParameters1(self):
        inst = self.instantiate_from("parameters-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Parameters instance")
        self.implParameters1(inst)
        
        js = inst.as_json()
        self.assertEqual("Parameters", js["resourceType"])
        inst2 = parameters.Parameters(js)
        self.implParameters1(inst2)
    
    def implParameters1(self, inst):
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.parameter[0].name, "exact")
        self.assertTrue(inst.parameter[0].valueBoolean)
        self.assertEqual(inst.parameter[1].name, "property")
        self.assertEqual(inst.parameter[1].part[0].name, "code")
        self.assertEqual(inst.parameter[1].part[0].valueCode, "focus")
        self.assertEqual(inst.parameter[1].part[1].name, "value")
        self.assertEqual(inst.parameter[1].part[1].valueCode, "top")
        self.assertEqual(inst.parameter[2].name, "patient")
        self.assertEqual(inst.parameter[2].resource.id, "example")

