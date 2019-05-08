#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import appointment
from .fhirdate import FHIRDate


class AppointmentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Appointment", js["resourceType"])
        return appointment.Appointment(js)
    
    def testAppointment1(self):
        inst = self.instantiate_from("appointment-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Appointment instance")
        self.implAppointment1(inst)
        
        js = inst.as_json()
        self.assertEqual("Appointment", js["resourceType"])
        inst2 = appointment.Appointment(js)
        self.implAppointment1(inst2)
    
    def implAppointment1(self, inst):
        self.assertEqual(inst.appointmentType.coding[0].code, "FOLLOWUP")
        self.assertEqual(inst.appointmentType.coding[0].display, "A follow up visit from a previous appointment")
        self.assertEqual(inst.appointmentType.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0276")
        self.assertEqual(inst.comment, "Further expand on the results of the MRI and determine the next actions that may be appropriate.")
        self.assertEqual(inst.created.date, FHIRDate("2013-10-10").date)
        self.assertEqual(inst.created.as_json(), "2013-10-10")
        self.assertEqual(inst.description, "Discussion on the results of your recent MRI")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-10T11:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-10T11:00:00Z")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participant[0].required, "required")
        self.assertEqual(inst.participant[0].status, "accepted")
        self.assertEqual(inst.participant[1].required, "required")
        self.assertEqual(inst.participant[1].status, "accepted")
        self.assertEqual(inst.participant[1].type[0].coding[0].code, "ATND")
        self.assertEqual(inst.participant[1].type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.participant[2].required, "required")
        self.assertEqual(inst.participant[2].status, "accepted")
        self.assertEqual(inst.priority, 5)
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "gp")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "General Practice")
        self.assertEqual(inst.serviceCategory[0].coding[0].system, "http://example.org/service-category")
        self.assertEqual(inst.serviceType[0].coding[0].code, "52")
        self.assertEqual(inst.serviceType[0].coding[0].display, "General Discussion")
        self.assertEqual(inst.specialty[0].coding[0].code, "394814009")
        self.assertEqual(inst.specialty[0].coding[0].display, "General practice")
        self.assertEqual(inst.specialty[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-10T09:00:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-10T09:00:00Z")
        self.assertEqual(inst.status, "booked")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testAppointment2(self):
        inst = self.instantiate_from("appointment-example-request.json")
        self.assertIsNotNone(inst, "Must have instantiated a Appointment instance")
        self.implAppointment2(inst)
        
        js = inst.as_json()
        self.assertEqual("Appointment", js["resourceType"])
        inst2 = appointment.Appointment(js)
        self.implAppointment2(inst2)
    
    def implAppointment2(self, inst):
        self.assertEqual(inst.appointmentType.coding[0].code, "WALKIN")
        self.assertEqual(inst.appointmentType.coding[0].display, "A previously unscheduled walk-in visit")
        self.assertEqual(inst.appointmentType.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0276")
        self.assertEqual(inst.comment, "Further expand on the results of the MRI and determine the next actions that may be appropriate.")
        self.assertEqual(inst.created.date, FHIRDate("2015-12-02").date)
        self.assertEqual(inst.created.as_json(), "2015-12-02")
        self.assertEqual(inst.description, "Discussion on the results of your recent MRI")
        self.assertEqual(inst.id, "examplereq")
        self.assertEqual(inst.identifier[0].system, "http://example.org/sampleappointment-identifier")
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.minutesDuration, 15)
        self.assertEqual(inst.participant[0].required, "required")
        self.assertEqual(inst.participant[0].status, "needs-action")
        self.assertEqual(inst.participant[1].required, "required")
        self.assertEqual(inst.participant[1].status, "needs-action")
        self.assertEqual(inst.participant[1].type[0].coding[0].code, "ATND")
        self.assertEqual(inst.participant[1].type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.participant[2].required, "required")
        self.assertEqual(inst.participant[2].status, "accepted")
        self.assertEqual(inst.priority, 5)
        self.assertEqual(inst.reasonCode[0].coding[0].code, "413095006")
        self.assertEqual(inst.reasonCode[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reasonCode[0].text, "Clinical Review")
        self.assertEqual(inst.requestedPeriod[0].end.date, FHIRDate("2016-06-09").date)
        self.assertEqual(inst.requestedPeriod[0].end.as_json(), "2016-06-09")
        self.assertEqual(inst.requestedPeriod[0].start.date, FHIRDate("2016-06-02").date)
        self.assertEqual(inst.requestedPeriod[0].start.as_json(), "2016-06-02")
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "gp")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "General Practice")
        self.assertEqual(inst.serviceCategory[0].coding[0].system, "http://example.org/service-category")
        self.assertEqual(inst.specialty[0].coding[0].code, "394814009")
        self.assertEqual(inst.specialty[0].coding[0].display, "General practice")
        self.assertEqual(inst.specialty[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "proposed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testAppointment3(self):
        inst = self.instantiate_from("appointment-example2doctors.json")
        self.assertIsNotNone(inst, "Must have instantiated a Appointment instance")
        self.implAppointment3(inst)
        
        js = inst.as_json()
        self.assertEqual("Appointment", js["resourceType"])
        inst2 = appointment.Appointment(js)
        self.implAppointment3(inst2)
    
    def implAppointment3(self, inst):
        self.assertEqual(inst.appointmentType.coding[0].code, "WALKIN")
        self.assertEqual(inst.appointmentType.coding[0].display, "A previously unscheduled walk-in visit")
        self.assertEqual(inst.appointmentType.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0276")
        self.assertEqual(inst.comment, "Clarify the results of the MRI to ensure context of test was correct")
        self.assertEqual(inst.description, "Discussion about Peter Chalmers MRI results")
        self.assertEqual(inst.end.date, FHIRDate("2013-12-09T11:00:00Z").date)
        self.assertEqual(inst.end.as_json(), "2013-12-09T11:00:00Z")
        self.assertEqual(inst.id, "2docs")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participant[0].required, "information-only")
        self.assertEqual(inst.participant[0].status, "accepted")
        self.assertEqual(inst.participant[1].required, "required")
        self.assertEqual(inst.participant[1].status, "accepted")
        self.assertEqual(inst.participant[2].required, "required")
        self.assertEqual(inst.participant[2].status, "accepted")
        self.assertEqual(inst.participant[3].required, "information-only")
        self.assertEqual(inst.participant[3].status, "accepted")
        self.assertEqual(inst.priority, 5)
        self.assertEqual(inst.serviceCategory[0].coding[0].code, "gp")
        self.assertEqual(inst.serviceCategory[0].coding[0].display, "General Practice")
        self.assertEqual(inst.serviceCategory[0].coding[0].system, "http://example.org/service-category")
        self.assertEqual(inst.serviceType[0].coding[0].code, "52")
        self.assertEqual(inst.serviceType[0].coding[0].display, "General Discussion")
        self.assertEqual(inst.specialty[0].coding[0].code, "394814009")
        self.assertEqual(inst.specialty[0].coding[0].display, "General practice")
        self.assertEqual(inst.specialty[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.start.date, FHIRDate("2013-12-09T09:00:00Z").date)
        self.assertEqual(inst.start.as_json(), "2013-12-09T09:00:00Z")
        self.assertEqual(inst.status, "booked")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status, "generated")

