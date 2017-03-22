#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import processresponse
from .fhirdate import FHIRDate


class ProcessResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ProcessResponse", js["resourceType"])
        return processresponse.ProcessResponse(js)
    
    def testProcessResponse1(self):
        inst = self.instantiate_from("processresponse-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessResponse instance")
        self.implProcessResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessResponse", js["resourceType"])
        inst2 = processresponse.ProcessResponse(js)
        self.implProcessResponse1(inst2)
    
    def implProcessResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-07-14").date)
        self.assertEqual(inst.created.as_json(), "2014-07-14")
        self.assertEqual(inst.disposition, "Referred to claim not found on system.")
        self.assertEqual(inst.error[0].coding[0].code, "a001")
        self.assertEqual(inst.error[0].coding[0].system, "http://hl7.org/fhir/adjudication-error")
        self.assertEqual(inst.form.coding[0].code, "PRRESP/2016/01")
        self.assertEqual(inst.form.coding[0].system, "http://ncforms.org/formid")
        self.assertEqual(inst.id, "SR2349")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/processresponse")
        self.assertEqual(inst.identifier[0].value, "ER987634")
        self.assertEqual(inst.outcome.coding[0].code, "error")
        self.assertEqual(inst.outcome.coding[0].system, "http://hl7.org/fhir/processoutcomecodes")
        self.assertEqual(inst.processNote[0].text, "Please check the submitted payor identification and local claim number.")
        self.assertEqual(inst.processNote[0].type.coding[0].code, "print")
        self.assertEqual(inst.processNote[0].type.coding[0].system, "http://hl7.org/fhir/note-type")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ProcessResponse</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessResponse2(self):
        inst = self.instantiate_from("processresponse-example-pended.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessResponse instance")
        self.implProcessResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessResponse", js["resourceType"])
        inst2 = processresponse.ProcessResponse(js)
        self.implProcessResponse2(inst2)
    
    def implProcessResponse2(self, inst):
        self.assertEqual(inst.contained[0].id, "comreq-1")
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Additional information required.")
        self.assertEqual(inst.id, "SR2499")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/processresponse")
        self.assertEqual(inst.identifier[0].value, "881222")
        self.assertEqual(inst.outcome.coding[0].code, "pended")
        self.assertEqual(inst.outcome.coding[0].system, "http://hl7.org/fhir/processoutcomecodes")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A ProcessResponse indicating pended status with a request for additional information.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcessResponse3(self):
        inst = self.instantiate_from("processresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcessResponse instance")
        self.implProcessResponse3(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcessResponse", js["resourceType"])
        inst2 = processresponse.ProcessResponse(js)
        self.implProcessResponse3(inst2)
    
    def implProcessResponse3(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Adjudication processing completed, ClaimResponse and EOB ready for retrieval.")
        self.assertEqual(inst.id, "SR2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/processresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertEqual(inst.outcome.coding[0].code, "complete")
        self.assertEqual(inst.outcome.coding[0].system, "http://hl7.org/fhir/processoutcomecodes")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the ProcessResponse</div>")
        self.assertEqual(inst.text.status, "generated")

