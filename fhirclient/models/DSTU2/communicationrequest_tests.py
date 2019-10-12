#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-10-12.
#  2019, SMART Health IT.

from __future__ import unicode_literals
import os
import io
import unittest
import json
from . import communicationrequest
from .fhirdate import FHIRDate


class CommunicationRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CommunicationRequest", js["resourceType"])
        return communicationrequest.CommunicationRequest(js)
    
    def testCommunicationRequest1(self):
        inst = self.instantiate_from("communicationrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CommunicationRequest instance")
        self.implCommunicationRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("CommunicationRequest", js["resourceType"])
        inst2 = communicationrequest.CommunicationRequest(js)
        self.implCommunicationRequest1(inst2)
    
    def implCommunicationRequest1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div>To be filled out at a later time</div>")
        self.assertEqual(inst.text.status, "generated")

