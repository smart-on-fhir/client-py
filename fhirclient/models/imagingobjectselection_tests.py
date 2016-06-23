#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import imagingobjectselection
from .fhirdate import FHIRDate


class ImagingObjectSelectionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImagingObjectSelection", js["resourceType"])
        return imagingobjectselection.ImagingObjectSelection(js)
    
    def testImagingObjectSelection1(self):
        inst = self.instantiate_from("imagingobjectselection-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingObjectSelection instance")
        self.implImagingObjectSelection1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImagingObjectSelection", js["resourceType"])
        inst2 = imagingobjectselection.ImagingObjectSelection(js)
        self.implImagingObjectSelection1(inst2)
    
    def implImagingObjectSelection1(self, inst):
        self.assertEqual(inst.authoringTime.date, FHIRDate("2014-11-20T11:01:20-08:00").date)
        self.assertEqual(inst.authoringTime.as_json(), "2014-11-20T11:01:20-08:00")
        self.assertEqual(inst.description, "1 SC image (screen snapshot) and 2 CT images to share a chest CT exam")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.study[0].series[0].instance[0].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.7")
        self.assertEqual(inst.study[0].series[0].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092902")
        self.assertEqual(inst.study[0].series[0].instance[0].url, "http://localhost/wado/SCP/2.16.124.113543.6003.189642796.63084.16749.2599092904")
        self.assertEqual(inst.study[0].series[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16750.2599092901")
        self.assertEqual(inst.study[0].series[1].instance[0].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.study[0].series[1].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092903")
        self.assertEqual(inst.study[0].series[1].instance[0].url, "http://localhost/wado/SCP/2.16.124.113543.6003.189642796.63084.16748.2599092903")
        self.assertEqual(inst.study[0].series[1].instance[1].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.study[0].series[1].instance[1].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092904")
        self.assertEqual(inst.study[0].series[1].instance[1].url, "http://localhost/wado/SCP/2.16.124.113543.6003.189642796.63084.16750.2599092902")
        self.assertEqual(inst.study[0].series[1].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16750.2599092902")
        self.assertEqual(inst.study[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16749.2599092904")
        self.assertEqual(inst.text.div, "<div>A set of images accompanying to an exam document, including one SC image and two CT images, to publish the exam sharing</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title.coding[0].code, "113030")
        self.assertEqual(inst.title.coding[0].display, "Manifest")
        self.assertEqual(inst.title.coding[0].system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.title.text, "A set of objects that have been exported for sharing")
        self.assertEqual(inst.uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092901")

