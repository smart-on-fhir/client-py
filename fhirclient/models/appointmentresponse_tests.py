#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import appointmentresponse
from .fhirdate import FHIRDate


class AppointmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AppointmentResponse", js["resourceType"])
        return appointmentresponse.AppointmentResponse(js)
    
    def testAppointmentResponse1(self):
        inst = self.instantiate_from("appointmentresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AppointmentResponse instance")
        self.implAppointmentResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("AppointmentResponse", js["resourceType"])
        inst2 = appointmentresponse.AppointmentResponse(js)
        self.implAppointmentResponse1(inst2)
    
    def implAppointmentResponse1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.participantStatus, "accepted")
        self.assertEqual(inst.text.div, "<div>Accept Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status, "generated")

