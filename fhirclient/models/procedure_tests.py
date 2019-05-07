#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import procedure
from .fhirdate import FHIRDate


class ProcedureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Procedure", js["resourceType"])
        return procedure.Procedure(js)
    
    def testProcedure1(self):
        inst = self.instantiate_from("procedure-example-f201-tpf.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure1(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure1(inst2)
    
    def implProcedure1(self, inst):
        self.assertEqual(inst.bodySite[0].coding[0].code, "272676008")
        self.assertEqual(inst.bodySite[0].coding[0].display, "Sphenoid bone")
        self.assertEqual(inst.bodySite[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[0].code, "367336001")
        self.assertEqual(inst.code.coding[0].display, "Chemotherapy")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.instantiatesCanonical[0], "PlanDefinition/KDN5")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text, "Eerste neo-adjuvante TPF-kuur bij groot proces in sphenoid met intracraniale uitbreiding.")
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-01-28T14:27:00+01:00").date)
        self.assertEqual(inst.performedPeriod.end.as_json(), "2013-01-28T14:27:00+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-01-28T13:31:00+01:00").date)
        self.assertEqual(inst.performedPeriod.start.as_json(), "2013-01-28T13:31:00+01:00")
        self.assertEqual(inst.performer[0].function.coding[0].code, "310512001")
        self.assertEqual(inst.performer[0].function.coding[0].display, "Medical oncologist")
        self.assertEqual(inst.performer[0].function.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reasonCode[0].text, "DiagnosticReport/f201")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedure2(self):
        inst = self.instantiate_from("procedure-example-ambulation.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure2(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure2(inst2)
    
    def implProcedure2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "62013009")
        self.assertEqual(inst.code.coding[0].display, "Ambulating patient (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Ambulation")
        self.assertEqual(inst.id, "ambulation")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.instantiatesUri[0], "http://example.org/protocol-for-hypertension-during-pregnancy")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "not-done")
        self.assertEqual(inst.statusReason.coding[0].code, "398254007")
        self.assertEqual(inst.statusReason.coding[0].display, "  Pre-eclampsia (disorder)")
        self.assertEqual(inst.statusReason.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.statusReason.text, "Pre-eclampsia")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Ambulation procedure was not done</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedure3(self):
        inst = self.instantiate_from("procedure-example-implant.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure3(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure3(inst2)
    
    def implProcedure3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "25267002")
        self.assertEqual(inst.code.coding[0].display, "Insertion of intracardiac pacemaker (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Implant Pacemaker")
        self.assertEqual(inst.focalDevice[0].action.coding[0].code, "implanted")
        self.assertEqual(inst.focalDevice[0].action.coding[0].system, "http://hl7.org/fhir/device-action")
        self.assertEqual(inst.followUp[0].text, "ROS 5 days  - 2013-04-10")
        self.assertEqual(inst.id, "example-implant")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text, "Routine Appendectomy. Appendix was inflamed and in retro-caecal position")
        self.assertEqual(inst.performedDateTime.date, FHIRDate("2015-04-05").date)
        self.assertEqual(inst.performedDateTime.as_json(), "2015-04-05")
        self.assertEqual(inst.reasonCode[0].text, "Bradycardia")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedure4(self):
        inst = self.instantiate_from("procedure-example-colon-biopsy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure4(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure4(inst2)
    
    def implProcedure4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "76164006")
        self.assertEqual(inst.code.coding[0].display, "Biopsy of colon (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Biopsy of colon")
        self.assertEqual(inst.id, "colon-biopsy")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Biopsy of colon, which was part of colonoscopy</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedure5(self):
        inst = self.instantiate_from("procedure-example-f004-tracheotomy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure5(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure5(inst2)
    
    def implProcedure5(self, inst):
        self.assertEqual(inst.bodySite[0].coding[0].code, "83030008")
        self.assertEqual(inst.bodySite[0].coding[0].display, "Retropharyngeal area")
        self.assertEqual(inst.bodySite[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[0].code, "48387007")
        self.assertEqual(inst.code.coding[0].display, "Tracheotomy")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.followUp[0].text, "described in care plan")
        self.assertEqual(inst.id, "f004")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome.text, "removal of the retropharyngeal abscess")
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-03-22T10:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.end.as_json(), "2013-03-22T10:30:10+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-03-22T09:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.start.as_json(), "2013-03-22T09:30:10+01:00")
        self.assertEqual(inst.performer[0].function.coding[0].code, "01.000")
        self.assertEqual(inst.performer[0].function.coding[0].display, "Arts")
        self.assertEqual(inst.performer[0].function.coding[0].system, "urn:oid:2.16.840.1.113883.2.4.15.111")
        self.assertEqual(inst.performer[0].function.text, "Care role")
        self.assertEqual(inst.reasonCode[0].text, "ensure breathing during surgery")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedure6(self):
        inst = self.instantiate_from("procedure-example-education.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure6(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure6(inst2)
    
    def implProcedure6(self, inst):
        self.assertEqual(inst.category.coding[0].code, "311401005")
        self.assertEqual(inst.category.coding[0].display, "Patient education (procedure)")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category.text, "Education")
        self.assertEqual(inst.code.coding[0].code, "48023004")
        self.assertEqual(inst.code.coding[0].display, "Breast self-examination technique education (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Health education - breast examination")
        self.assertEqual(inst.id, "education")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.performedDateTime.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.performedDateTime.as_json(), "2014-08-16")
        self.assertEqual(inst.reasonCode[0].text, "early detection of breast mass")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Health education - breast examination for early detection of breast mass</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedure7(self):
        inst = self.instantiate_from("procedure-example-colonoscopy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure7(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure7(inst2)
    
    def implProcedure7(self, inst):
        self.assertEqual(inst.code.coding[0].code, "73761001")
        self.assertEqual(inst.code.coding[0].display, "Colonoscopy (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Colonoscopy")
        self.assertEqual(inst.id, "colonoscopy")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Colonoscopy with complication</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedure8(self):
        inst = self.instantiate_from("procedure-example-physical-therapy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure8(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure8(inst2)
    
    def implProcedure8(self, inst):
        self.assertEqual(inst.bodySite[0].coding[0].code, "36701003")
        self.assertEqual(inst.bodySite[0].coding[0].display, "Both knees (body structure)")
        self.assertEqual(inst.bodySite[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.bodySite[0].text, "Both knees")
        self.assertEqual(inst.category.coding[0].code, "386053000")
        self.assertEqual(inst.category.coding[0].display, "Evaluation procedure (procedure)")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category.text, "Evaluation")
        self.assertEqual(inst.code.coding[0].code, "710830005")
        self.assertEqual(inst.code.coding[0].display, "Assessment of passive range of motion (procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Assessment of passive range of motion")
        self.assertEqual(inst.id, "physical-therapy")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.performedDateTime.date, FHIRDate("2016-09-27").date)
        self.assertEqual(inst.performedDateTime.as_json(), "2016-09-27")
        self.assertEqual(inst.reasonCode[0].text, "assessment of mobility limitations due to osteoarthritis")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Assessment of passive range of motion for both knees on Sept 27, 2016 due to osteoarthritis</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedure9(self):
        inst = self.instantiate_from("procedure-example-f003-abscess.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure9(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure9(inst2)
    
    def implProcedure9(self, inst):
        self.assertEqual(inst.bodySite[0].coding[0].code, "83030008")
        self.assertEqual(inst.bodySite[0].coding[0].display, "Retropharyngeal area")
        self.assertEqual(inst.bodySite[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[0].code, "172960003")
        self.assertEqual(inst.code.coding[0].display, "Incision of retropharyngeal abscess")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.followUp[0].text, "described in care plan")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome.text, "removal of the retropharyngeal abscess")
        self.assertEqual(inst.performedPeriod.end.date, FHIRDate("2013-03-24T10:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.end.as_json(), "2013-03-24T10:30:10+01:00")
        self.assertEqual(inst.performedPeriod.start.date, FHIRDate("2013-03-24T09:30:10+01:00").date)
        self.assertEqual(inst.performedPeriod.start.as_json(), "2013-03-24T09:30:10+01:00")
        self.assertEqual(inst.performer[0].function.coding[0].code, "01.000")
        self.assertEqual(inst.performer[0].function.coding[0].display, "Arts")
        self.assertEqual(inst.performer[0].function.coding[0].system, "urn:oid:2.16.840.1.113883.2.4.15.111")
        self.assertEqual(inst.performer[0].function.text, "Care role")
        self.assertEqual(inst.reasonCode[0].text, "abcess in retropharyngeal area")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testProcedure10(self):
        inst = self.instantiate_from("procedure-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Procedure instance")
        self.implProcedure10(inst)
        
        js = inst.as_json()
        self.assertEqual("Procedure", js["resourceType"])
        inst2 = procedure.Procedure(js)
        self.implProcedure10(inst2)
    
    def implProcedure10(self, inst):
        self.assertEqual(inst.code.coding[0].code, "80146002")
        self.assertEqual(inst.code.coding[0].display, "Appendectomy (Procedure)")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Appendectomy")
        self.assertEqual(inst.followUp[0].text, "ROS 5 days  - 2013-04-10")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text, "Routine Appendectomy. Appendix was inflamed and in retro-caecal position")
        self.assertEqual(inst.performedDateTime.date, FHIRDate("2013-04-05").date)
        self.assertEqual(inst.performedDateTime.as_json(), "2013-04-05")
        self.assertEqual(inst.reasonCode[0].text, "Generalized abdominal pain 24 hours. Localized in RIF with rebound and guarding")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Routine Appendectomy</div>")
        self.assertEqual(inst.text.status, "generated")

