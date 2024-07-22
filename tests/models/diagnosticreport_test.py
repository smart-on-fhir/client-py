#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import diagnosticreport
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class DiagnosticReportTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DiagnosticReport", js["resourceType"])
        return diagnosticreport.DiagnosticReport(js)
    
    def testDiagnosticReport1(self):
        inst = self.instantiate_from("diagnosticreport-example-pgx.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport1(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport1(inst2)
    
    def implDiagnosticReport1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "PGxReport")
        self.assertEqual(inst.code.coding[0].display, "Pharmacogenetics Report")
        self.assertEqual(inst.code.coding[0].system, "https://system/PGxReport")
        self.assertEqual(inst.code.text, "Pharmacogenetics Report")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("2016-10-15T12:34:56+11:00").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-10-15T12:34:56+11:00")
        self.assertEqual(inst.id, "example-pgx")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2016-10-20T14:00:05+11:00").datetime)
        self.assertEqual(inst.issued.as_json(), "2016-10-20T14:00:05+11:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.presentedForm[0].contentType, "application/pdf")
        self.assertEqual(inst.presentedForm[0].creation.datetime, FHIRDateTime("2016-10-20T20:00:00+11:00").datetime)
        self.assertEqual(inst.presentedForm[0].creation.as_json(), "2016-10-20T20:00:00+11:00")
        self.assertEqual(inst.presentedForm[0].data, "cGRmSW5CYXNlNjRCaW5hcnk=")
        self.assertEqual(inst.presentedForm[0].hash, "571ef9c5655840f324e679072ed62b1b95eef8a0")
        self.assertEqual(inst.presentedForm[0].language, "en")
        self.assertEqual(inst.presentedForm[0].title, "Pharmacogenetics Report")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport2(self):
        inst = self.instantiate_from("diagnosticreport-example-papsmear.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport2(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport2(inst2)
    
    def implDiagnosticReport2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "47527-7")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("2013-02-11T10:33:33+11:00").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2013-02-11T10:33:33+11:00")
        self.assertEqual(inst.id, "pap")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2013-02-13T11:45:33+11:00").datetime)
        self.assertEqual(inst.issued.as_json(), "2013-02-13T11:45:33+11:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "additional")
    
    def testDiagnosticReport3(self):
        inst = self.instantiate_from("diagnosticreport-example-f201-brainct.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport3(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport3(inst2)
    
    def implDiagnosticReport3(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "394914008")
        self.assertEqual(inst.category[0].coding[0].display, "Radiology")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].coding[1].code, "RAD")
        self.assertEqual(inst.category[0].coding[1].system, "http://terminology.hl7.org/CodeSystem/v2-0074")
        self.assertEqual(inst.code.coding[0].code, "429858000")
        self.assertEqual(inst.code.coding[0].display, "Computed tomography (CT) of head and neck")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "CT of head-neck")
        self.assertEqual(inst.conclusion, "CT brains: large tumor sphenoid/clivus.")
        self.assertEqual(inst.conclusionCode[0].coding[0].code, "188340000")
        self.assertEqual(inst.conclusionCode[0].coding[0].display, "Malignant tumor of craniopharyngeal duct")
        self.assertEqual(inst.conclusionCode[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("2012-12-01T12:00:00+01:00").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2012-12-01T12:00:00+01:00").datetime)
        self.assertEqual(inst.issued.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport4(self):
        inst = self.instantiate_from("diagnosticreport-example-ultrasound.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport4(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport4(inst2)
    
    def implDiagnosticReport4(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "394914008")
        self.assertEqual(inst.category[0].coding[0].display, "Radiology")
        self.assertEqual(inst.category[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].coding[1].code, "RAD")
        self.assertEqual(inst.category[0].coding[1].system, "http://terminology.hl7.org/CodeSystem/v2-0074")
        self.assertEqual(inst.code.coding[0].code, "45036003")
        self.assertEqual(inst.code.coding[0].display, "Ultrasonography of abdomen")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Abdominal Ultrasound")
        self.assertEqual(inst.conclusion, "Unremarkable study")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("2012-12-01T12:00:00+01:00").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.id, "ultrasound")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2012-12-01T12:00:00+01:00").datetime)
        self.assertEqual(inst.issued.as_json(), "2012-12-01T12:00:00+01:00")
        self.assertEqual(inst.media[0].comment, "A comment about the image")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport5(self):
        inst = self.instantiate_from("diagnosticreport-example-gingival-mass.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport5(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport5(inst2)
    
    def implDiagnosticReport5(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "PAT")
        self.assertEqual(inst.category[0].coding[0].display, "Pathology (gross & histopath, not surgical)")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0074")
        self.assertEqual(inst.category[0].text, "Pathology")
        self.assertEqual(inst.code.coding[0].code, "4503")
        self.assertEqual(inst.code.coding[0].display, "Biopsy without Microscopic Description (1 Site/Lesion)-Standard")
        self.assertEqual(inst.code.coding[0].system, "https://www.acmeonline.com")
        self.assertEqual(inst.code.text, "Biopsy without Microscopic Description (1 Site/Lesion)-Standard")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("2017-03-02").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2017-03-02")
        self.assertEqual(inst.id, "gingival-mass")
        self.assertEqual(inst.identifier[0].system, "https://www.acmeonline.com")
        self.assertEqual(inst.identifier[0].value, "P73456090")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2017-03-15T08:13:08Z").datetime)
        self.assertEqual(inst.issued.as_json(), "2017-03-15T08:13:08Z")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.presentedForm[0].contentType, "application/pdf")
        self.assertEqual(inst.presentedForm[0].language, "en")
        self.assertEqual(inst.presentedForm[0].title, "LAB ID: P73456090 MAX JONES Biopsy without Microscopic Description (1 Site/Lesion)-Standard")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testDiagnosticReport6(self):
        inst = self.instantiate_from("diagnosticreport-example-dxa.json")
        self.assertIsNotNone(inst, "Must have instantiated a DiagnosticReport instance")
        self.implDiagnosticReport6(inst)
        
        js = inst.as_json()
        self.assertEqual("DiagnosticReport", js["resourceType"])
        inst2 = diagnosticreport.DiagnosticReport(js)
        self.implDiagnosticReport6(inst2)
    
    def implDiagnosticReport6(self, inst):
        self.assertEqual(inst.code.coding[0].code, "38269-7")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "DXA BONE DENSITOMETRY")
        self.assertEqual(inst.conclusionCode[0].coding[0].code, "391040000")
        self.assertEqual(inst.conclusionCode[0].coding[0].display, "At risk of osteoporotic fracture")
        self.assertEqual(inst.conclusionCode[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("2008-06-17").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2008-06-17")
        self.assertEqual(inst.id, "102")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2008-06-18T09:23:00+10:00").datetime)
        self.assertEqual(inst.issued.as_json(), "2008-06-18T09:23:00+10:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")

