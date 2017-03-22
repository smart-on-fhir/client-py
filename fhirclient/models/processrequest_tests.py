#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import processrequest
from .fhirdate import FHIRDate


class ProcessRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ProcessRequest", js["resourceType"])
        return processrequest.ProcessRequest(js)
    
    def testProcessRequest1(self):
        inst = self.instantiate_from("processrequest-example-poll-eob.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest1(inst2)
    
    def implProcessRequest1(self, inst):
        self.assertEqual(inst.action, "poll")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "1115")
        self.assertEqual(inst.identifier[0].system, "http://www.phr.com/patient/12345/processrequest")
        self.assertEqual(inst.identifier[0].value, "115")
        self.assertEqual(inst.include[0], "ExplanationOfBenefit")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessRequest2(self):
        inst = self.instantiate_from("processrequest-example-poll-exclusive.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest2(inst2)
    
    def implProcessRequest2(self, inst):
        self.assertEqual(inst.action, "poll")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.exclude[0], "Communication")
        self.assertEqual(inst.exclude[1], "PaymentReconciliation")
        self.assertEqual(inst.id, "1113")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/processrequest")
        self.assertEqual(inst.identifier[0].value, "113")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessRequest3(self):
        inst = self.instantiate_from("processrequest-example-poll-inclusive.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest3(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest3(inst2)
    
    def implProcessRequest3(self, inst):
        self.assertEqual(inst.action, "poll")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "1112")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/processrequest")
        self.assertEqual(inst.identifier[0].value, "112")
        self.assertEqual(inst.include[0], "PaymentReconciliation")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessRequest4(self):
        inst = self.instantiate_from("processrequest-example-poll-payrec.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest4(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest4(inst2)
    
    def implProcessRequest4(self, inst):
        self.assertEqual(inst.action, "poll")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "1114")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/processrequest")
        self.assertEqual(inst.identifier[0].value, "114")
        self.assertEqual(inst.include[0], "PaymentReconciliation")
        self.assertEqual(inst.period.end.date, FHIRDate("2014-08-20").date)
        self.assertEqual(inst.period.end.as_json(), "2014-08-20")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-08-10").date)
        self.assertEqual(inst.period.start.as_json(), "2014-08-10")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessRequest5(self):
        inst = self.instantiate_from("processrequest-example-poll-specific.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest5(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest5(inst2)
    
    def implProcessRequest5(self, inst):
        self.assertEqual(inst.action, "poll")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "1111")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/processrequest")
        self.assertEqual(inst.identifier[0].value, "111")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessRequest6(self):
        inst = self.instantiate_from("processrequest-example-reprocess.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest6(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest6(inst2)
    
    def implProcessRequest6(self, inst):
        self.assertEqual(inst.action, "reprocess")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "44654")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/processrequest")
        self.assertEqual(inst.identifier[0].value, "44543")
        self.assertEqual(inst.item[0].sequenceLinkId, 1)
        self.assertEqual(inst.reference, "ABC12345G")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ReProcess ProcessRequest resource.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessRequest7(self):
        inst = self.instantiate_from("processrequest-example-reverse.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest7(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest7(inst2)
    
    def implProcessRequest7(self, inst):
        self.assertEqual(inst.action, "cancel")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "87654")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/processrequest")
        self.assertEqual(inst.identifier[0].value, "76543")
        self.assertFalse(inst.nullify)
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Reversal ProcessRequest</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessRequest8(self):
        inst = self.instantiate_from("processrequest-example-status.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest8(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest8(inst2)
    
    def implProcessRequest8(self, inst):
        self.assertEqual(inst.action, "status")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "87655")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/processrequest")
        self.assertEqual(inst.identifier[0].value, "1776543")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Status ProcessRequest</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessRequest9(self):
        inst = self.instantiate_from("processrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessRequest instance")
        self.implProcessRequest9(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessRequest", js["resourceType"])
        inst2 = processrequest.ProcessRequest(js)
        self.implProcessRequest9(inst2)
    
    def implProcessRequest9(self, inst):
        self.assertEqual(inst.action, "poll")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id, "1110")
        self.assertEqual(inst.identifier[0].system, "http://happyvalley.com/processrequest")
        self.assertEqual(inst.identifier[0].value, "110")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the Poll ProcessRequest</div>")
        self.assertEqual(inst.text.status, "generated")

