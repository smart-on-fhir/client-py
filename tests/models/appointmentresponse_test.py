#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import appointmentresponse
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class AppointmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AppointmentResponse", js["resourceType"])
        return appointmentresponse.AppointmentResponse(js)
    
    def testAppointmentResponse1(self):
        inst = self.instantiate_from("appointmentresponse-example-req.json")
        self.assertIsNotNone(inst, "Must have instantiated a AppointmentResponse instance")
        self.implAppointmentResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("AppointmentResponse", js["resourceType"])
        inst2 = appointmentresponse.AppointmentResponse(js)
        self.implAppointmentResponse1(inst2)
    
    def implAppointmentResponse1(self, inst):
        self.assertEqual(inst.comment, "can't we try for this time, can't do mornings")
        self.assertEqual(inst.end.datetime, FHIRInstant("2013-12-25T13:30:00Z").datetime)
        self.assertEqual(inst.end.as_json(), "2013-12-25T13:30:00Z")
        self.assertEqual(inst.id, "exampleresp")
        self.assertEqual(inst.identifier[0].system, "http://example.org/sampleappointmentresponse-identifier")
        self.assertEqual(inst.identifier[0].value, "response123")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participantStatus, "tentative")
        self.assertEqual(inst.participantType[0].coding[0].code, "ATND")
        self.assertEqual(inst.participantType[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.start.datetime, FHIRInstant("2013-12-25T13:15:00Z").datetime)
        self.assertEqual(inst.start.as_json(), "2013-12-25T13:15:00Z")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testAppointmentResponse2(self):
        inst = self.instantiate_from("appointmentresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AppointmentResponse instance")
        self.implAppointmentResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("AppointmentResponse", js["resourceType"])
        inst2 = appointmentresponse.AppointmentResponse(js)
        self.implAppointmentResponse2(inst2)
    
    def implAppointmentResponse2(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participantStatus, "accepted")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status, "generated")

