#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


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
        inst = self.instantiate_from("imagingstudy-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingStudy instance")
        self.implImagingStudy1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImagingStudy", js["resourceType"])
        inst2 = imagingstudy.ImagingStudy(js)
        self.implImagingStudy1(inst2)
    
    def implImagingStudy1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.numberOfInstances, 1)
        self.assertEqual(inst.numberOfSeries, 1)
        self.assertEqual(inst.series[0].bodySite.code, "67734004")
        self.assertEqual(inst.series[0].bodySite.display, "Upper Trunk Structure")
        self.assertEqual(inst.series[0].bodySite.system, "http://snomed.info/sct")
        self.assertEqual(inst.series[0].description, "CT Surview 180")
        self.assertEqual(inst.series[0].instance[0].content[0].url, "http://localhost/fhir/Binary/1.2.840.11361907579238403408700.3.0.14.19970327150033")
        self.assertEqual(inst.series[0].instance[0].number, 1)
        self.assertEqual(inst.series[0].instance[0].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.series[0].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092903")
        self.assertEqual(inst.series[0].modality.code, "CT")
        self.assertEqual(inst.series[0].modality.system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.series[0].number, 3)
        self.assertEqual(inst.series[0].numberOfInstances, 1)
        self.assertEqual(inst.series[0].uid, "urn:oid:2.16.124.113543.6003.2588828330.45298.17418.2723805630")
        self.assertEqual(inst.started.date, FHIRDate("2011-01-01T11:01:20+03:00").date)
        self.assertEqual(inst.started.as_json(), "2011-01-01T11:01:20+03:00")
        self.assertEqual(inst.text.div, "<div>Image 1 from Series 3: CT Images on Patient MINT (MINT1234) taken at 1-Jan 2011 01:20 AM</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.uid, "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430045")

