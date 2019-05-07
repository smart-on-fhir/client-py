#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import servicerequest
from .fhirdate import FHIRDate


class ServiceRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ServiceRequest", js["resourceType"])
        return servicerequest.ServiceRequest(js)
    
    def testServiceRequest1(self):
        inst = self.instantiate_from("servicerequest-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest1(inst2)
    
    def implServiceRequest1(self, inst):
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
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "20170201-0001")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurrenceTiming.repeat.duration, 15)
        self.assertEqual(inst.occurrenceTiming.repeat.durationMax, 25)
        self.assertEqual(inst.occurrenceTiming.repeat.durationUnit, "min")
        self.assertEqual(inst.occurrenceTiming.repeat.frequency, 1)
        self.assertEqual(inst.occurrenceTiming.repeat.frequencyMax, 4)
        self.assertEqual(inst.occurrenceTiming.repeat.period, 1)
        self.assertEqual(inst.occurrenceTiming.repeat.periodUnit, "d")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest2(self):
        inst = self.instantiate_from("servicerequest-example3.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest2(inst2)
    
    def implServiceRequest2(self, inst):
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
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority, "stat")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest3(self):
        inst = self.instantiate_from("servicerequest-example-lipid.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest3(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest3(inst2)
    
    def implServiceRequest3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "LIPID")
        self.assertEqual(inst.code.coding[0].system, "http://acme.org/tests")
        self.assertEqual(inst.code.text, "Lipid Panel")
        self.assertEqual(inst.contained[0].id, "fasting")
        self.assertEqual(inst.contained[1].id, "serum")
        self.assertEqual(inst.id, "lipid")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "PLAC")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].type.text, "Placer")
        self.assertEqual(inst.identifier[0].value, "2345234234234")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text, "patient is afraid of needles")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-02T16:16:00-07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-02T16:16:00-07:00")
        self.assertEqual(inst.reasonCode[0].coding[0].code, "V173")
        self.assertEqual(inst.reasonCode[0].coding[0].display, "Fam hx-ischem heart dis")
        self.assertEqual(inst.reasonCode[0].coding[0].system, "http://hl7.org/fhir/sid/icd-9")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest4(self):
        inst = self.instantiate_from("servicerequest-example-colonoscopy-bx.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest4(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest4(inst2)
    
    def implServiceRequest4(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(inst.code.coding[0].code, "76164006")
        self.assertEqual(inst.code.coding[0].display, "Biopsy of colon (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Biopsy of colon")
        self.assertEqual(inst.id, "colon-biopsy")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.requisition.system, "http://bumc.org/requisitions")
        self.assertEqual(inst.requisition.value, "req12345")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest5(self):
        inst = self.instantiate_from("servicerequest-example4.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest5(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest5(inst2)
    
    def implServiceRequest5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "229115003")
        self.assertEqual(inst.code.coding[0].display, "Bench Press (regime/therapy) ")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "benchpress")
        self.assertEqual(inst.intent, "plan")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurrenceTiming.repeat.count, 20)
        self.assertEqual(inst.occurrenceTiming.repeat.countMax, 30)
        self.assertEqual(inst.occurrenceTiming.repeat.frequency, 3)
        self.assertEqual(inst.occurrenceTiming.repeat.period, 1)
        self.assertEqual(inst.occurrenceTiming.repeat.periodUnit, "wk")
        self.assertEqual(inst.patientInstruction, "Start with 30kg 10-15 repetitions for three sets and increase in increments of 5kg when you feel ready")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest6(self):
        inst = self.instantiate_from("servicerequest-example-edu.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest6(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest6(inst2)
    
    def implServiceRequest6(self, inst):
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
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2014-08-16")
        self.assertEqual(inst.reasonCode[0].text, "early detection of breast mass")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest7(self):
        inst = self.instantiate_from("servicerequest-example-ventilation.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest7(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest7(inst2)
    
    def implServiceRequest7(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2018-02-20").date)
        self.assertEqual(inst.authoredOn.as_json(), "2018-02-20")
        self.assertEqual(inst.code.coding[0].code, "40617009")
        self.assertEqual(inst.code.coding[0].display, "Artificial respiration (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Mechanical Ventilation")
        self.assertEqual(inst.id, "vent")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.orderDetail[0].coding[0].code, "243144002")
        self.assertEqual(inst.orderDetail[0].coding[0].display, "Patient triggered inspiratory assistance (procedure)")
        self.assertEqual(inst.orderDetail[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.orderDetail[0].text, "IPPB")
        self.assertEqual(inst.orderDetail[1].text, " Initial Settings : Sens: -1 cm H20 Pressure 15 cm H2O moderate flow:  Monitor VS every 15 minutes x 4 at the start of mechanical ventilation, then routine for unit OR every 5 hr")
        self.assertEqual(inst.reasonCode[0].text, "chronic obstructive lung disease (COLD)")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest8(self):
        inst = self.instantiate_from("servicerequest-example-ambulation.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest8(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest8(inst2)
    
    def implServiceRequest8(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2017-03-05").date)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-05")
        self.assertEqual(inst.code.coding[0].code, "62013009")
        self.assertEqual(inst.code.coding[0].display, "Ambulating patient (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Ambulation")
        self.assertEqual(inst.id, "ambulation")
        self.assertEqual(inst.identifier[0].value, "45678")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest9(self):
        inst = self.instantiate_from("servicerequest-example-pt.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest9(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest9(inst2)
    
    def implServiceRequest9(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-09-20").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-09-20")
        self.assertEqual(inst.bodySite[0].coding[0].code, "36701003")
        self.assertEqual(inst.bodySite[0].coding[0].display, "Both knees (body structure)")
        self.assertEqual(inst.bodySite[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.bodySite[0].text, "Both knees")
        self.assertEqual(inst.category[0].coding[0].code, "386053000")
        self.assertEqual(inst.category[0].coding[0].display, "Evaluation procedure (procedure)")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].text, "Evaluation")
        self.assertEqual(inst.code.coding[0].code, "710830005")
        self.assertEqual(inst.code.coding[0].display, "Assessment of passive range of motion (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Assessment of passive range of motion")
        self.assertEqual(inst.id, "physical-therapy")
        self.assertEqual(inst.intent, "order")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-09-27").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-09-27")
        self.assertEqual(inst.reasonCode[0].text, "assessment of mobility limitations due to osteoarthritis")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testServiceRequest10(self):
        inst = self.instantiate_from("servicerequest-example-di.json")
        self.assertIsNotNone(inst, "Must have instantiated a ServiceRequest instance")
        self.implServiceRequest10(inst)
        
        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest10(inst2)
    
    def implServiceRequest10(self, inst):
        self.assertEqual(inst.code.coding[0].code, "24627-2")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Chest CT")
        self.assertEqual(inst.id, "di")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.reasonCode[0].text, "Check for metastatic disease")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

