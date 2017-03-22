#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
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
        inst = self.instantiate_from("procedurerequest-example-ambulation.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest1(inst2)
    
    def implProcedureRequest1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(inst.code.coding[0].code, "62013009")
        self.assertEqual(inst.code.coding[0].display, "Ambulating patient (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Ambulation")
        self.assertEqual(inst.id, "ambulation")
        self.assertEqual(inst.identifier[0].value, "45678")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest2(self):
        inst = self.instantiate_from("procedurerequest-example-appendectomy.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest2(inst2)
    
    def implProcedureRequest2(self, inst):
        self.assertEqual(inst.code.text, "Appendectomy")
        self.assertEqual(inst.id, "appendectomy-narrative")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "additional")
    
    def testProcedureRequest3(self):
        inst = self.instantiate_from("procedurerequest-example-colonoscopy-bx.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest3(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest3(inst2)
    
    def implProcedureRequest3(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(inst.code.coding[0].code, "76164006")
        self.assertEqual(inst.code.coding[0].display, "Biopsy of colon (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Biopsy of colon")
        self.assertEqual(inst.id, "colon-biopsy")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.requisition.system, "http://bumc.org/requisitions")
        self.assertEqual(inst.requisition.value, "req12345")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest4(self):
        inst = self.instantiate_from("procedurerequest-example-colonoscopy.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest4(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest4(inst2)
    
    def implProcedureRequest4(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(inst.code.coding[0].code, "73761001")
        self.assertEqual(inst.code.coding[0].display, "Colonoscopy (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Colonoscopy")
        self.assertEqual(inst.id, "colonoscopy")
        self.assertEqual(inst.identifier[0].value, "45678")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.requisition.system, "http://bumc.org/requisitions")
        self.assertEqual(inst.requisition.value, "req12345")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest5(self):
        inst = self.instantiate_from("procedurerequest-example-di.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest5(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest5(inst2)
    
    def implProcedureRequest5(self, inst):
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
    
    def testProcedureRequest6(self):
        inst = self.instantiate_from("procedurerequest-example-edu.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest6(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest6(inst2)
    
    def implProcedureRequest6(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-08-16").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-08-16")
        self.assertEqual(inst.category[0].coding[0].code, "311401005")
        self.assertEqual(inst.category[0].coding[0].display, "Patient education (procedure)")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].text, "Education")
        self.assertEqual(inst.code.coding[0].code, "48023004")
        self.assertEqual(inst.code.coding[0].display, "Breast self-examination technique education (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Health education - breast examination")
        self.assertEqual(inst.id, "education")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-08-16")
        self.assertEqual(inst.reasonCode[0].text, "early detection of breast mass")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest7(self):
        inst = self.instantiate_from("procedurerequest-example-ft4.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest7(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest7(inst2)
    
    def implProcedureRequest7(self, inst):
        self.assertEqual(inst.code.coding[0].code, "3024-7")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Free T4")
        self.assertEqual(inst.id, "ft4")
        self.assertEqual(inst.intent, "reflex-order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2015-08-27T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2015-08-27T09:33:27+07:00")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest8(self):
        inst = self.instantiate_from("procedurerequest-example-implant.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest8(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest8(inst2)
    
    def implProcedureRequest8(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2015-03-30").date)
        self.assertEqual(inst.authoredOn.as_json(), "2015-03-30")
        self.assertEqual(inst.code.coding[0].code, "25267002")
        self.assertEqual(inst.code.coding[0].display, "Insertion of intracardiac pacemaker (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Implant Pacemaker")
        self.assertEqual(inst.id, "example-implant")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.reasonCode[0].text, "Bradycardia")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedureRequest9(self):
        inst = self.instantiate_from("procedurerequest-example-lipid.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest9(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest9(inst2)
    
    def implProcedureRequest9(self, inst):
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
    
    def testProcedureRequest10(self):
        inst = self.instantiate_from("procedurerequest-example-ob.json")
        self.assertIsNotNone(inst, "Must have instantiated a ProcedureRequest instance")
        self.implProcedureRequest10(inst)
        
        js = inst.as_json()
        self.assertEqual("ProcedureRequest", js["resourceType"])
        inst2 = procedurerequest.ProcedureRequest(js)
        self.implProcedureRequest10(inst2)
    
    def implProcedureRequest10(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "386637004")
        self.assertEqual(inst.category[0].coding[0].display, "Obstetric procedure (procedure)")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].text, "OB")
        self.assertEqual(inst.code.coding[0].code, "22633006")
        self.assertEqual(inst.code.coding[0].display, "Vaginal delivery, medical personnel present (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Vaginal delivery")
        self.assertEqual(inst.id, "ob")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2012-06-02").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2012-06-02")
        self.assertEqual(inst.reasonCode[0].text, "term pregnancy, active labor")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")

