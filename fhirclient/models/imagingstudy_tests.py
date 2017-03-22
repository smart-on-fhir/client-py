#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import imagingstudy
from .fhirdate import FHIRDate


class ImagingStudyTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImagingStudy", js["resourceType"])
        return imagingstudy.ImagingStudy(js)
    
    def testImagingStudy1(self):
        inst = self.instantiate_from("imagingstudy-example-xr.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingStudy instance")
        self.implImagingStudy1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImagingStudy", js["resourceType"])
        inst2 = imagingstudy.ImagingStudy(js)
        self.implImagingStudy1(inst2)
    
    def implImagingStudy1(self, inst):
        self.assertEqual(inst.accession.type.coding[0].code, "ACSN")
        self.assertEqual(inst.accession.type.coding[0].system, "http://hl7.org/fhir/v2/0203")
        self.assertEqual(inst.accession.use, "usual")
        self.assertEqual(inst.accession.value, "W12342398")
        self.assertEqual(inst.availability, "ONLINE")
        self.assertEqual(inst.description, "XR Wrist 3+ Views")
        self.assertEqual(inst.id, "example-xr")
        self.assertEqual(inst.identifier[0].use, "secondary")
        self.assertEqual(inst.identifier[0].value, "55551234")
        self.assertEqual(inst.modalityList[0].code, "DX")
        self.assertEqual(inst.modalityList[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.numberOfInstances, 2)
        self.assertEqual(inst.numberOfSeries, 1)
        self.assertEqual(inst.procedureCode[0].coding[0].code, "RPID2589")
        self.assertEqual(inst.procedureCode[0].coding[0].display, "XR Wrist 3+ Views")
        self.assertEqual(inst.procedureCode[0].coding[0].system, "http://www.radlex.org")
        self.assertEqual(inst.procedureCode[0].text, "XR Wrist 3+ Views")
        self.assertEqual(inst.reason.coding[0].code, "357009")
        self.assertEqual(inst.reason.coding[0].display, "Closed fracture of trapezoidal bone of wrist")
        self.assertEqual(inst.reason.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.series[0].availability, "ONLINE")
        self.assertEqual(inst.series[0].bodySite.code, "T-15460")
        self.assertEqual(inst.series[0].bodySite.display, "Wrist Joint")
        self.assertEqual(inst.series[0].bodySite.system, "http://snomed.info/sct")
        self.assertEqual(inst.series[0].description, "XR Wrist 3+ Views")
        self.assertEqual(inst.series[0].instance[0].number, 1)
        self.assertEqual(inst.series[0].instance[0].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.series[0].instance[0].title, "PA VIEW")
        self.assertEqual(inst.series[0].instance[0].uid, "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430045.1.1")
        self.assertEqual(inst.series[0].instance[1].number, 2)
        self.assertEqual(inst.series[0].instance[1].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.series[0].instance[1].title, "LL VIEW")
        self.assertEqual(inst.series[0].instance[1].uid, "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430045.1.2")
        self.assertEqual(inst.series[0].laterality.code, "419161000")
        self.assertEqual(inst.series[0].laterality.display, "Unilateral left")
        self.assertEqual(inst.series[0].laterality.system, "http://snomed.info/sct")
        self.assertEqual(inst.series[0].modality.code, "DX")
        self.assertEqual(inst.series[0].modality.system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.series[0].number, 3)
        self.assertEqual(inst.series[0].numberOfInstances, 2)
        self.assertEqual(inst.series[0].started.date, FHIRDate("2011-01-01T11:01:20+03:00").date)
        self.assertEqual(inst.series[0].started.as_json(), "2011-01-01T11:01:20+03:00")
        self.assertEqual(inst.series[0].uid, "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430045.1")
        self.assertEqual(inst.started.date, FHIRDate("2017-01-01T11:01:20+03:00").date)
        self.assertEqual(inst.started.as_json(), "2017-01-01T11:01:20+03:00")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">XR Wrist 3+ Views. John Smith (MRN: 09236). Accession: W12342398. Performed: 2017-01-01. 1 series, 2 images.</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.uid, "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430046")
    
    def testImagingStudy2(self):
        inst = self.instantiate_from("imagingstudy-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingStudy instance")
        self.implImagingStudy2(inst)
        
        js = inst.as_json()
        self.assertEqual("ImagingStudy", js["resourceType"])
        inst2 = imagingstudy.ImagingStudy(js)
        self.implImagingStudy2(inst2)
    
    def implImagingStudy2(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.numberOfInstances, 1)
        self.assertEqual(inst.numberOfSeries, 1)
        self.assertEqual(inst.series[0].bodySite.code, "67734004")
        self.assertEqual(inst.series[0].bodySite.display, "Upper Trunk Structure")
        self.assertEqual(inst.series[0].bodySite.system, "http://snomed.info/sct")
        self.assertEqual(inst.series[0].description, "CT Surview 180")
        self.assertEqual(inst.series[0].instance[0].number, 1)
        self.assertEqual(inst.series[0].instance[0].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.series[0].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092903")
        self.assertEqual(inst.series[0].modality.code, "CT")
        self.assertEqual(inst.series[0].modality.system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.series[0].number, 3)
        self.assertEqual(inst.series[0].numberOfInstances, 1)
        self.assertEqual(inst.series[0].uid, "urn:oid:2.16.124.113543.6003.2588828330.45298.17418.2723805630")
        self.assertEqual(inst.started.date, FHIRDate("2011-01-01T11:01:20+03:00").date)
        self.assertEqual(inst.started.as_json(), "2011-01-01T11:01:20+03:00")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">CT Chest.  John Smith (MRN: 09236). Accession: W12342398. Performed: 2011-01-01. 3 series, 12 images.</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.uid, "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430045")

