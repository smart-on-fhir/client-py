#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import imagingmanifest
from .fhirdate import FHIRDate


class ImagingManifestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImagingManifest", js["resourceType"])
        return imagingmanifest.ImagingManifest(js)
    
    def testImagingManifest1(self):
        inst = self.instantiate_from("imagingmanifest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingManifest instance")
        self.implImagingManifest1(inst)
        
        js = inst.as_json()
        self.assertEqual("ImagingManifest", js["resourceType"])
        inst2 = imagingmanifest.ImagingManifest(js)
        self.implImagingManifest1(inst2)
    
    def implImagingManifest1(self, inst):
        self.assertEqual(inst.authoringTime.date, FHIRDate("2014-11-20T11:01:20-08:00").date)
        self.assertEqual(inst.authoringTime.as_json(), "2014-11-20T11:01:20-08:00")
        self.assertEqual(inst.description, "1 SC image (screen snapshot) and 2 CT images to share a chest CT exam")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.value, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092901")
        self.assertEqual(inst.study[0].series[0].instance[0].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.7")
        self.assertEqual(inst.study[0].series[0].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092902")
        self.assertEqual(inst.study[0].series[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16750.2599092901")
        self.assertEqual(inst.study[0].series[1].instance[0].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.study[0].series[1].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092903")
        self.assertEqual(inst.study[0].series[1].instance[1].sopClass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.study[0].series[1].instance[1].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092904")
        self.assertEqual(inst.study[0].series[1].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16750.2599092902")
        self.assertEqual(inst.study[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16749.2599092904")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A set of images to share accompanying an report document, including one SC image and two CT image</div>")
        self.assertEqual(inst.text.status, "generated")

