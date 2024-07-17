#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import insuranceplan
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class InsurancePlanTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("InsurancePlan", js["resourceType"])
        return insuranceplan.InsurancePlan(js)
    
    def testInsurancePlan1(self):
        inst = self.instantiate_from("insuranceplan-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a InsurancePlan instance")
        self.implInsurancePlan1(inst)
        
        js = inst.as_json()
        self.assertEqual("InsurancePlan", js["resourceType"])
        inst2 = insuranceplan.InsurancePlan(js)
        self.implInsurancePlan1(inst2)
    
    def implInsurancePlan1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "foo")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p><p><b>name</b>: foo</p></div>")
        self.assertEqual(inst.text.status, "generated")

