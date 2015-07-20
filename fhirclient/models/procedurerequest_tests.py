#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import procedurerequest
from .fhirdate import FHIRDate


class ProcedureRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ProcedureRequest", js["resourceType"])
        return procedurerequest.ProcedureRequest(js)
    
    def testProcedureRequest1(self):
        inst = self.instantiate_from("procedurerequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest1(inst2)
    
    def implProcedureRequest1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div>To be added</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "323418000")
        self.assertEqual(inst.type.coding[0].display, "Fix me up")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testProcedureRequest2(self):
        inst = self.instantiate_from("procedurerequest-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest2(inst2)
    
    def implProcedureRequest2(self, inst):
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].code, "66754008")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].display, "Appendix structure")
        self.assertEqual(inst.bodySite[0].siteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/procedurerequest-authorizedBy")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.indication[0].coding[0].code, "163220003")
        self.assertEqual(inst.indication[0].coding[0].display, "On examination - abdominal pain - right iliac")
        self.assertEqual(inst.indication[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.orderedOn.date, FHIRDate("2013-04-04").date)
        self.assertEqual(inst.orderedOn.as_json(), "2013-04-04")
        self.assertEqual(inst.priority, "urgent")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div>Request for Routine Appendectomy</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.timingDateTime.date, FHIRDate("2013-04-05").date)
        self.assertEqual(inst.timingDateTime.as_json(), "2013-04-05")
        self.assertEqual(inst.type.coding[0].code, "80146002")
        self.assertEqual(inst.type.coding[0].display, "Appendectomy (Procedure)")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.text, "Appendectomy")

