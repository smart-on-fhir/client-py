#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import diagnosticreport
from .fhirdate import FHIRDate


class DiagnosticReportTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DiagnosticReport", js["resourceType"])
        return diagnosticreport.DiagnosticReport(js)
    
    def testDiagnosticReport1(self):
        inst = self.instantiate_from("diagnosticreport-example-dxa.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport1(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport1(inst2)
    
    def implDiagnosticReport1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "38269-7")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "DXA BONE DENSITOMETRY")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].code, "391040000")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].display, "At risk of osteoporotic fracture")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2008-06-17").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2008-06-17")
        self.assertEqual(inst.id, "102")
        self.assertEqual(inst.issued.date, FHIRDate("2008-06-18T09:23:00+10:00").date)
        self.assertEqual(inst.issued.as_json(), "2008-06-18T09:23:00+10:00")
        self.assertEqual(inst.performer[0].role.coding[0].code, "66862007")
        self.assertEqual(inst.performer[0].role.coding[0].display, "Radiologist")
        self.assertEqual(inst.performer[0].role.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.performer[0].role.text, "Radiologist")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport2(self):
        inst = self.instantiate_from("diagnosticreport-example-f001-bloodexam.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport2(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport2(inst2)
    
    def implDiagnosticReport2(self, inst):
        self.assertEqual(inst.category.coding[0].code, "252275004")
        self.assertEqual(inst.category.coding[0].display, "Haematology test")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category.coding[1].code, "HM")
        self.assertEqual(inst.category.coding[1].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.code.coding[0].code, "58410-2")
        self.assertEqual(inst.code.coding[0].display, "Complete blood count (hemogram) panel - Blood by Automated count")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.conclusion, "Core lab")
        self.assertEqual(inst.contained[0].id, "req")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/reports")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "nr1239044")
        self.assertEqual(inst.issued.date, FHIRDate("2013-05-15T19:32:52+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-05-15T19:32:52+01:00")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport3(self):
        inst = self.instantiate_from("diagnosticreport-example-f201-brainct.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport3(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport3(inst2)
    
    def implDiagnosticReport3(self, inst):
        self.assertEqual(inst.category.coding[0].code, "394914008")
        self.assertEqual(inst.category.coding[0].display, "Radiology")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category.coding[1].code, "RAD")
        self.assertEqual(inst.category.coding[1].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.code.coding[0].code, "429858000")
        self.assertEqual(inst.code.coding[0].display, "Computed tomography (CT) of head and neck")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "CT of head-neck")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].code, "188340000")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].display, "Malignant tumor of craniopharyngeal duct")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.conclusion, "CT brains: large tumor sphenoid/clivus.")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.issued.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport4(self):
        inst = self.instantiate_from("diagnosticreport-example-f202-bloodculture.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport4(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport4(inst2)
    
    def implDiagnosticReport4(self, inst):
        self.assertEqual(inst.category.coding[0].code, "15220000")
        self.assertEqual(inst.category.coding[0].display, "Laboratory test")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category.coding[1].code, "LAB")
        self.assertEqual(inst.category.coding[1].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.code.coding[0].code, "104177005")
        self.assertEqual(inst.code.coding[0].display, "Blood culture for bacteria, including anaerobic screen")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].code, "428763004")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].display, "Bacteremia due to staphylococcus")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.conclusion, "Blood culture tested positive on staphylococcus aureus")
        self.assertEqual(inst.contained[0].id, "req")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.issued.date, FHIRDate("2013-03-11T10:28:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-03-11T10:28:00+01:00")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport5(self):
        inst = self.instantiate_from("diagnosticreport-example-ghp.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport5(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport5(inst2)
    
    def implDiagnosticReport5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "GHP")
        self.assertEqual(inst.code.coding[0].display, "General Health Profile")
        self.assertEqual(inst.code.coding[0].system, "http://acme.com/labs/reports")
        self.assertEqual(inst.contained[0].id, "rtt")
        self.assertEqual(inst.contained[1].id, "ltt")
        self.assertEqual(inst.contained[2].id, "urine")
        self.assertEqual(inst.contained[3].id, "p2")
        self.assertEqual(inst.contained[4].id, "r1")
        self.assertEqual(inst.contained[5].id, "r2")
        self.assertEqual(inst.contained[6].id, "r3")
        self.assertEqual(inst.contained[7].id, "r4")
        self.assertEqual(inst.contained[8].id, "r5")
        self.assertEqual(inst.contained[9].id, "r6")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2015-08-16T06:40:17Z").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2015-08-16T06:40:17Z")
        self.assertEqual(inst.id, "ghp")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/lab/reports")
        self.assertEqual(inst.identifier[0].value, "ghp-example")
        self.assertEqual(inst.issued.date, FHIRDate("2015-08-17T06:40:17Z").date)
        self.assertEqual(inst.issued.as_json(), "2015-08-17T06:40:17Z")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2015-08-16T10:35:23Z").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2015-08-16T10:35:23Z")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport6(self):
        inst = self.instantiate_from("diagnosticreport-example-gingival-mass.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport6(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport6(inst2)
    
    def implDiagnosticReport6(self, inst):
        self.assertEqual(inst.category.coding[0].code, "PAT")
        self.assertEqual(inst.category.coding[0].display, "Pathology (gross & histopath, not surgical)")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.category.text, "Pathology")
        self.assertEqual(inst.code.coding[0].code, "4503")
        self.assertEqual(inst.code.coding[0].display, "Biopsy without Microscopic Description (1 Site/Lesion)-Standard")
        self.assertEqual(inst.code.coding[0].system, "https://www.acmeonline.com")
        self.assertEqual(inst.code.text, "Biopsy without Microscopic Description (1 Site/Lesion)-Standard")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2017-03-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2017-03-02")
        self.assertEqual(inst.id, "gingival-mass")
        self.assertEqual(inst.identifier[0].system, "https://www.acmeonline.com")
        self.assertEqual(inst.identifier[0].value, "P73456090")
        self.assertEqual(inst.issued.date, FHIRDate("2017-03-15T08:13:08Z").date)
        self.assertEqual(inst.issued.as_json(), "2017-03-15T08:13:08Z")
        self.assertEqual(inst.presentedForm[0].contentType, "application/pdf")
        self.assertEqual(inst.presentedForm[0].language, "en")
        self.assertEqual(inst.presentedForm[0].title, "LAB ID: P73456090 MAX JONES Biopsy without Microscopic Description (1 Site/Lesion)-Standard")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport7(self):
        inst = self.instantiate_from("diagnosticreport-example-lipids.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport7(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport7(inst2)
    
    def implDiagnosticReport7(self, inst):
        self.assertEqual(inst.category.coding[0].code, "HM")
        self.assertEqual(inst.category.coding[0].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.code.coding[0].code, "24331-1")
        self.assertEqual(inst.code.coding[0].display, "Lipid 1996 panel - Serum or Plasma")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Lipid Panel")
        self.assertEqual(inst.contained[0].id, "cholesterol")
        self.assertEqual(inst.contained[1].id, "triglyceride")
        self.assertEqual(inst.contained[2].id, "hdlcholesterol")
        self.assertEqual(inst.contained[3].id, "ldlcholesterol")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2011-03-04T08:30:00+11:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2011-03-04T08:30:00+11:00")
        self.assertEqual(inst.id, "lipids")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/lab/reports")
        self.assertEqual(inst.identifier[0].value, "5234342")
        self.assertEqual(inst.issued.date, FHIRDate("2013-01-27T11:45:33+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-01-27T11:45:33+11:00")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport8(self):
        inst = self.instantiate_from("diagnosticreport-example-papsmear.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport8(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport8(inst2)
    
    def implDiagnosticReport8(self, inst):
        self.assertEqual(inst.code.coding[0].code, "47527-7")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2013-02-11T10:33:33+11:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2013-02-11T10:33:33+11:00")
        self.assertEqual(inst.id, "pap")
        self.assertEqual(inst.issued.date, FHIRDate("2013-02-13T11:45:33+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-02-13T11:45:33+11:00")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "additional")
    
    def testDiagnosticReport9(self):
        inst = self.instantiate_from("diagnosticreport-example-pgx.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport9(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport9(inst2)
    
    def implDiagnosticReport9(self, inst):
        self.assertEqual(inst.code.coding[0].code, "PGxReport")
        self.assertEqual(inst.code.coding[0].display, "Pharmacogenetics Report")
        self.assertEqual(inst.code.coding[0].system, "https://system/PGxReport")
        self.assertEqual(inst.code.text, "Pharmacogenetics Report")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2016-10-15T12:34:56+11:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-10-15T12:34:56+11:00")
        self.assertEqual(inst.id, "example-pgx")
        self.assertEqual(inst.issued.date, FHIRDate("2016-10-20T14:00:05+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2016-10-20T14:00:05+11:00")
        self.assertEqual(inst.presentedForm[0].contentType, "PDF")
        self.assertEqual(inst.presentedForm[0].creation.date, FHIRDate("2016-10-20T20:00:00+11:00").date)
        self.assertEqual(inst.presentedForm[0].creation.as_json(), "2016-10-20T20:00:00+11:00")
        self.assertEqual(inst.presentedForm[0].data, "cGRmSW5CYXNlNjRCaW5hcnk=")
        self.assertEqual(inst.presentedForm[0].hash, "571ef9c5655840f324e679072ed62b1b95eef8a0")
        self.assertEqual(inst.presentedForm[0].language, "en")
        self.assertEqual(inst.presentedForm[0].title, "Pharmacogenetics Report")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport10(self):
        inst = self.instantiate_from("diagnosticreport-example-ultrasound.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport10(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport10(inst2)
    
    def implDiagnosticReport10(self, inst):
        self.assertEqual(inst.category.coding[0].code, "394914008")
        self.assertEqual(inst.category.coding[0].display, "Radiology")
        self.assertEqual(inst.category.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category.coding[1].code, "RAD")
        self.assertEqual(inst.category.coding[1].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.code.coding[0].code, "45036003")
        self.assertEqual(inst.code.coding[0].display, "Ultrasonography of abdomen")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Abdominal Ultrasound")
        self.assertEqual(inst.conclusion, "Unremarkable study")
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.id, "ultrasound")
        self.assertEqual(inst.image[0].comment, "A comment about the image")
        self.assertEqual(inst.issued.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")

