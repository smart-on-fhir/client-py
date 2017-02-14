#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11157 on 2017-02-14.
#  2017, SMART Health IT.


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
        inst = self.instantiate_from("procedurerequest-example-di.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest1(inst2)
    
    def implProcedureRequest1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "24627-2")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Chest CT")
        self.assertEqual(inst.id, "di")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.reasonCode[0].text, "Check for metastatic disease")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest2(self):
        inst = self.instantiate_from("procedurerequest-example-ft4.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest2(inst2)
    
    def implProcedureRequest2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "3024-7")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Free T4")
        self.assertEqual(inst.id, "ft4")
        self.assertEqual(inst.intent, "reflex-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2015-08-27T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2015-08-27T09:33:27+07:00")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest3(self):
        inst = self.instantiate_from("procedurerequest-example-lipid.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest3(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest3(inst2)
    
    def implProcedureRequest3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "LIPID")
        self.assertEqual(inst.code.coding[0].system, "http://acme.org/tests")
        self.assertEqual(inst.code.text, "Lipid Panel")
        self.assertEqual(inst.contained[0].id, "fasting")
        self.assertEqual(inst.contained[1].id, "serum")
        self.assertEqual(inst.id, "lipid")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "PLAC")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "2345234234234")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.note[0].text, "patient is afraid of needles")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-02T16:16:00-07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-02T16:16:00-07:00")
        self.assertEqual(inst.reasonCode[0].coding[0].code, "V173")
        self.assertEqual(inst.reasonCode[0].coding[0].display, "Fam hx-ischem heart dis")
        self.assertEqual(inst.reasonCode[0].coding[0].system, "http://hl7.org/fhir/sid/icd-9")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest4(self):
        inst = self.instantiate_from("procedurerequest-example-pgx.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest4(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest4(inst2)
    
    def implProcedureRequest4(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-10-10T15:00:00-07:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-10-10T15:00:00-07:00")
        self.assertEqual(inst.code.coding[0].code, "47403-1")
        self.assertEqual(inst.code.coding[0].display, "CYP2D6 gene targeted mutation analysis")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.id, "example-pgx")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest5(self):
        inst = self.instantiate_from("procedurerequest-example-subrequest.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest5(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest5(inst2)
    
    def implProcedureRequest5(self, inst):
        self.assertEqual(inst.bodySite[0].coding[0].display, "Right arm")
        self.assertEqual(inst.bodySite[0].text, "Right arm")
        self.assertEqual(inst.code.coding[0].code, "35542-0")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Peanut IgG")
        self.assertEqual(inst.id, "subrequest")
        self.assertEqual(inst.intent, "instance-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.performerType.coding[0].display, "Qualified nurse")
        self.assertEqual(inst.performerType.text, "Nurse")
        self.assertEqual(inst.priority, "routine")
        self.assertEqual(inst.reasonCode[0].text, "Check for Peanut Allergy")
        self.assertEqual(inst.requisition.value, "A13848392")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest6(self):
        inst = self.instantiate_from("procedurerequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest6(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest6(inst2)
    
    def implProcedureRequest6(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "103693007")
        self.assertEqual(inst.category[0].coding[0].display, "Diagnostic procedure (procedure)")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].text, "Diagnostics Procedure")
        self.assertEqual(inst.code.coding[0].code, "303653007")
        self.assertEqual(inst.code.coding[0].display, "Computed tomography of head")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">To be added</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest7(self):
        inst = self.instantiate_from("procedurerequest-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest7(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest7(inst2)
    
    def implProcedureRequest7(self, inst):
        self.assertEqual(inst.asNeededCodeableConcept.text, "as needed to clear mucus")
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-02-01T17:23:07Z").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-02-01T17:23:07Z")
        self.assertEqual(inst.code.coding[0].code, "34431008")
        self.assertEqual(inst.code.coding[0].display, "Physiotherapy of chest (regime/therapy) ")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.contained[0].id, "signature")
        self.assertEqual(inst.contained[1].id, "cystic-fibrosis")
        self.assertEqual(inst.id, "physiotherapy")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/placer-ids")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "PLAC")
        self.assertEqual(inst.identifier[0].type.coding[0].display, "Placer Identifier")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "20170201-0001")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.occurrenceTiming.repeat.frequency, 1)
        self.assertEqual(inst.occurrenceTiming.repeat.frequencyMax, 4)
        self.assertEqual(inst.occurrenceTiming.repeat.period, 1)
        self.assertEqual(inst.occurrenceTiming.repeat.periodUnit, "d")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest8(self):
        inst = self.instantiate_from("procedurerequest-example3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest8(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest8(inst2)
    
    def implProcedureRequest8(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-02-01T17:23:07Z").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-02-01T17:23:07Z")
        self.assertEqual(inst.code.coding[0].code, "359962006")
        self.assertEqual(inst.code.coding[0].display, "Turning patient in bed (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertTrue(inst.doNotPerform)
        self.assertEqual(inst.id, "do-not-turn")
        self.assertEqual(inst.identifier[0].system, "http://goodhealth.org/placer-ids")
        self.assertEqual(inst.identifier[0].value, "20170201-0002")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.priority, "stat")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest9(self):
        inst = self.instantiate_from("procedurerequest-genetics-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest9(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest9(inst2)
    
    def implProcedureRequest9(self, inst):
        self.assertEqual(inst.code.coding[0].code, "49874-1")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "ABCB4 gene mutation analysis")
        self.assertEqual(inst.id, "og-example1")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-05-12T16:16:00-07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-05-12T16:16:00-07:00")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

