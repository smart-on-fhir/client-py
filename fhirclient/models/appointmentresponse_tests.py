#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import appointmentresponse
from fhirdate import FHIRDate


class AppointmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = appointmentresponse.AppointmentResponse(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testAppointmentResponse1(self):
        inst = self.instantiate_from("appointmentresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e254ed0> instance")
    
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.participantStatus, "accepted")
        self.assertEqual(inst.text.div, "<div>Accept Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status, "generated")

