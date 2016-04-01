#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 on 2016-04-01.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import imagingexcerpt
from .fhirdate import FHIRDate


class ImagingExcerptTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImagingExcerpt", js["resourceType"])
        return imagingexcerpt.ImagingExcerpt(js)
    
    def testImagingExcerpt1(self):
        inst = self.instantiate_from("imagingexcerpt-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingExcerpt instance")
        self.implImagingExcerpt1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImagingExcerpt", js["resourceType"])
        inst2 = imagingexcerpt.ImagingExcerpt(js)
        self.implImagingExcerpt1(inst2)
    
    def implImagingExcerpt1(self, inst):
        self.assertEqual(inst.authoringTime.date, FHIRDate("2014-11-20T11:01:20-08:00").date)
        self.assertEqual(inst.authoringTime.as_json(), "2014-11-20T11:01:20-08:00")
        self.assertEqual(inst.description, "1 SC image (screen snapshot) and 2 CT images to share a chest CT exam")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.study[0].dicom[0].type, "WADO-RS")
        self.assertEqual(inst.study[0].dicom[0].url, "http://localhost/wado/SCP/2.16.124.113543.6003.189642796.63084.16749.2599092904")
        self.assertEqual(inst.study[0].series[0].instance[0].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.7")
        self.assertEqual(inst.study[0].series[0].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092902")
        self.assertEqual(inst.study[0].series[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16750.2599092901")
        self.assertEqual(inst.study[0].series[1].instance[0].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.study[0].series[1].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092903")
        self.assertEqual(inst.study[0].series[1].instance[1].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.study[0].series[1].instance[1].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092904")
        self.assertEqual(inst.study[0].series[1].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16750.2599092902")
        self.assertEqual(inst.study[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16749.2599092904")
        self.assertEqual(inst.study[0].viewable[0].contentType, "image/jpeg")
        self.assertEqual(inst.study[0].viewable[0].height, 100)
        self.assertEqual(inst.study[0].viewable[0].title, "thumbnail image")
        self.assertEqual(inst.study[0].viewable[0].width, 100)
        self.assertEqual(inst.study[0].viewable[1].contentType, "video/mp4")
        self.assertEqual(inst.study[0].viewable[1].duration, 2)
        self.assertEqual(inst.study[0].viewable[1].frames, 10)
        self.assertEqual(inst.study[0].viewable[1].height, 500)
        self.assertEqual(inst.study[0].viewable[1].title, "Cine loop")
        self.assertEqual(inst.study[0].viewable[1].url, "http://localhost/wado/SCP/2.16.124.113543.6003.189642796.63084.16749.2599092904.mp4")
        self.assertEqual(inst.study[0].viewable[1].width, 500)
        self.assertEqual(inst.study[0].viewable[2].contentType, "*/*")
        self.assertEqual(inst.study[0].viewable[2].title, "web viewer")
        self.assertEqual(inst.study[0].viewable[2].url, "http://localhost/wado/SCP/2.16.124.113543.6003.189642796.63084.16749.2599092904.html")
        self.assertEqual(inst.text.div, "<div>A set of images accompanying to an exam document, including one SC image and two CT images, to publish the exam sharing</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title.coding[0].code, "113030")
        self.assertEqual(inst.title.coding[0].display, "Manifest")
        self.assertEqual(inst.title.coding[0].system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.title.text, "A set of objects that have been exported for sharing")
        self.assertEqual(inst.uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092901")

