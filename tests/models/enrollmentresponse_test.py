#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import enrollmentresponse
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class EnrollmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EnrollmentResponse", js["resourceType"])
        return enrollmentresponse.EnrollmentResponse(js)
    
    def testEnrollmentResponse1(self):
        inst = self.instantiate_from("enrollmentresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EnrollmentResponse instance")
        self.implEnrollmentResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("EnrollmentResponse", js["resourceType"])
        inst2 = enrollmentresponse.EnrollmentResponse(js)
        self.implEnrollmentResponse1(inst2)
    
    def implEnrollmentResponse1(self, inst):
        self.assertEqual(inst.created.datetime, FHIRDateTime("2014-08-16").datetime)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Dependant added to policy.")
        self.assertEqual(inst.id, "ER2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/enrollmentresponse")
        self.assertEqual(inst.identifier[0].value, "781234")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EnrollmentResponse</div>")
        self.assertEqual(inst.text.status, "generated")

