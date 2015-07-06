#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


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
        self.assertEqual(inst.codedDiagnosis[0].coding[0].code, "391040000")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].display, "At risk of osteoporotic fracture")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.diagnosticDateTime.date, FHIRDate("2008-06-17").date)
        self.assertEqual(inst.diagnosticDateTime.as_json(), "2008-06-17")
        self.assertEqual(inst.id, "102")
        self.assertEqual(inst.issued.date, FHIRDate("2008-06-18T09:23:00+10:00").date)
        self.assertEqual(inst.issued.as_json(), "2008-06-18T09:23:00+10:00")
        self.assertEqual(inst.name.coding[0].code, "38269-7")
        self.assertEqual(inst.name.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.name.text, "DXA BONE DENSITOMETRY")
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
        self.assertEqual(inst.conclusion, "Core lab")
        self.assertEqual(inst.diagnosticDateTime.date, FHIRDate("2013-04-02").date)
        self.assertEqual(inst.diagnosticDateTime.as_json(), "2013-04-02")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/reports")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "nr1239044")
        self.assertEqual(inst.issued.date, FHIRDate("2013-05-15T19:32:52+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-05-15T19:32:52+01:00")
        self.assertEqual(inst.name.coding[0].code, "58410-2")
        self.assertEqual(inst.name.coding[0].display, "Complete blood count (hemogram) panel - Blood by Automated count")
        self.assertEqual(inst.name.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.serviceCategory.coding[0].code, "252275004")
        self.assertEqual(inst.serviceCategory.coding[0].display, "Haematology test")
        self.assertEqual(inst.serviceCategory.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.serviceCategory.coding[1].code, "HM")
        self.assertEqual(inst.serviceCategory.coding[1].system, "http://hl7.org/fhir/v2/0074")
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
        self.assertEqual(inst.codedDiagnosis[0].coding[0].code, "188340000")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].display, "Malignant tumor of craniopharyngeal duct")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.conclusion, "CT brains: large tumor sphenoid/clivus.")
        self.assertEqual(inst.diagnosticDateTime.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.diagnosticDateTime.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.issued.date, FHIRDate("2012-12-01T12:00:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.name.coding[0].code, "429858000")
        self.assertEqual(inst.name.coding[0].display, "Computed tomography (CT) of head and neck")
        self.assertEqual(inst.name.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.name.text, "CT of head-neck")
        self.assertEqual(inst.serviceCategory.coding[0].code, "394914008")
        self.assertEqual(inst.serviceCategory.coding[0].display, "Radiology")
        self.assertEqual(inst.serviceCategory.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.serviceCategory.coding[1].code, "RAD")
        self.assertEqual(inst.serviceCategory.coding[1].system, "http://hl7.org/fhir/v2/0074")
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
        self.assertEqual(inst.codedDiagnosis[0].coding[0].code, "428763004")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].display, "Bacteremia due to staphylococcus")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.conclusion, "Blood culture tested positive on staphylococcus aureus")
        self.assertEqual(inst.diagnosticDateTime.date, FHIRDate("2013-03-11T03:45:00+01:00").date)
        self.assertEqual(inst.diagnosticDateTime.as_json(), "2013-03-11T03:45:00+01:00")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.issued.date, FHIRDate("2013-03-11T10:28:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-03-11T10:28:00+01:00")
        self.assertEqual(inst.name.coding[0].code, "104177005")
        self.assertEqual(inst.name.coding[0].display, "Blood culture for bacteria, including anaerobic screen")
        self.assertEqual(inst.name.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.serviceCategory.coding[0].code, "15220000")
        self.assertEqual(inst.serviceCategory.coding[0].display, "Laboratory test")
        self.assertEqual(inst.serviceCategory.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.serviceCategory.coding[1].code, "LAB")
        self.assertEqual(inst.serviceCategory.coding[1].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport5(self):
        inst = self.instantiate_from("diagnosticreport-example-lipids.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport5(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport5(inst2)
    
    def implDiagnosticReport5(self, inst):
        self.assertEqual(inst.diagnosticDateTime.date, FHIRDate("2011-03-04T08:30:00+11:00").date)
        self.assertEqual(inst.diagnosticDateTime.as_json(), "2011-03-04T08:30:00+11:00")
        self.assertEqual(inst.id, "lipids")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/lab/reports")
        self.assertEqual(inst.identifier[0].value, "5234342")
        self.assertEqual(inst.issued.date, FHIRDate("2013-01-27T11:45:33+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-01-27T11:45:33+11:00")
        self.assertEqual(inst.name.coding[0].code, "57698-3")
        self.assertEqual(inst.name.coding[0].display, "Lipid panel with direct LDL - Serum or Plasma")
        self.assertEqual(inst.name.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.name.text, "Lipid Panel")
        self.assertEqual(inst.serviceCategory.coding[0].code, "HM")
        self.assertEqual(inst.serviceCategory.coding[0].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport6(self):
        inst = self.instantiate_from("diagnosticreport-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport6(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport6(inst2)
    
    def implDiagnosticReport6(self, inst):
        self.assertEqual(inst.diagnosticDateTime.date, FHIRDate("2011-03-04T08:30:00+11:00").date)
        self.assertEqual(inst.diagnosticDateTime.as_json(), "2011-03-04T08:30:00+11:00")
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/lab/reports")
        self.assertEqual(inst.identifier[0].value, "5234342")
        self.assertEqual(inst.issued.date, FHIRDate("2011-03-04T11:45:33+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2011-03-04T11:45:33+11:00")
        self.assertEqual(inst.name.coding[0].code, "58410-2")
        self.assertEqual(inst.name.coding[0].display, "Complete blood count (hemogram) panel - Blood by Automated count")
        self.assertEqual(inst.name.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.name.coding[1].code, "CBC")
        self.assertEqual(inst.name.coding[1].display, "MASTER FULL BLOOD COUNT")
        self.assertEqual(inst.name.text, "Complete Blood Count")
        self.assertEqual(inst.presentedForm[0].contentType, "application/pdf")
        self.assertEqual(inst.presentedForm[0].language, "en-AU")
        self.assertEqual(inst.presentedForm[0].title, "HTML Report")
        self.assertEqual(inst.serviceCategory.coding[0].code, "HM")
        self.assertEqual(inst.serviceCategory.coding[0].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport7(self):
        inst = self.instantiate_from("diagnosticreport-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport7(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport7(inst2)
    
    def implDiagnosticReport7(self, inst):
        self.assertEqual(inst.diagnosticDateTime.date, FHIRDate("2011-03-04T08:30:00+11:00").date)
        self.assertEqual(inst.diagnosticDateTime.as_json(), "2011-03-04T08:30:00+11:00")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/diagnosticReport-locationPerformed")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/lab/reports")
        self.assertEqual(inst.identifier[0].value, "5234342")
        self.assertEqual(inst.issued.date, FHIRDate("2011-03-04T11:45:33+11:00").date)
        self.assertEqual(inst.issued.as_json(), "2011-03-04T11:45:33+11:00")
        self.assertEqual(inst.name.coding[0].code, "58410-2")
        self.assertEqual(inst.name.coding[0].display, "Complete blood count (hemogram) panel - Blood by Automated count")
        self.assertEqual(inst.name.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.name.coding[1].code, "CBC")
        self.assertEqual(inst.name.coding[1].display, "MASTER FULL BLOOD COUNT")
        self.assertEqual(inst.name.text, "Complete Blood Count")
        self.assertEqual(inst.presentedForm[0].contentType, "application/pdf")
        self.assertEqual(inst.presentedForm[0].language, "en-AU")
        self.assertEqual(inst.presentedForm[0].title, "HTML Report")
        self.assertEqual(inst.serviceCategory.coding[0].code, "HM")
        self.assertEqual(inst.serviceCategory.coding[0].system, "http://hl7.org/fhir/v2/0074")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport8(self):
        inst = self.instantiate_from("dr-uslab-example1.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport8(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport8(inst2)
    
    def implDiagnosticReport8(self, inst):
        self.assertEqual(inst.codedDiagnosis[0].coding[0].code, "407152001")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].display, "Increased blood lead level")
        self.assertEqual(inst.codedDiagnosis[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.conclusion, "Elevated Blood Lead levels")
        self.assertEqual(inst.diagnosticDateTime.date, FHIRDate("2014-12-05").date)
        self.assertEqual(inst.diagnosticDateTime.as_json(), "2014-12-05")
        self.assertEqual(inst.id, "uslab-example1")
        self.assertEqual(inst.identifier[0].system, "http://lis.acmelabs.org/identifiers/report")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "5234342")
        self.assertEqual(inst.issued.date, FHIRDate("2014-12-06T15:42:15-08:00").date)
        self.assertEqual(inst.issued.as_json(), "2014-12-06T15:42:15-08:00")
        self.assertEqual(inst.name.coding[0].code, "5671-3")
        self.assertEqual(inst.name.coding[0].display, "Lead [Mass/volume] in Blood")
        self.assertEqual(inst.name.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.name.coding[1].code, "BLDLD")
        self.assertEqual(inst.name.coding[1].display, "Blood Lead")
        self.assertEqual(inst.name.coding[1].system, "urn:oid:2.16.840.1.113883.3.72.5.24")
        self.assertEqual(inst.name.text, "Blood Lead Report")
        self.assertEqual(inst.presentedForm[0].contentType, "application/pdf")
        self.assertEqual(inst.presentedForm[0].language, "en")
        self.assertEqual(inst.presentedForm[0].title, "ACMELABS: Blood Lead Report")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")

