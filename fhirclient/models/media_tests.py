#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from media import Media
from fhirdate import FHIRDate


class MediaTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = Media(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testMedia1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/media-example-dicom.json")
        self.assertIsNotNone(inst, "Must have instantiated a Media instance")
    
        self.assertEqual(inst.content.contentType, "application/dicom")
        self.assertEqual(inst.content.url, "http://imaging.acme.com/wado/server?requestType=WADO&contentType=application%2Fdicom&studyUid=1.2.840.113619.2.21.848.34082.0.538976288.3&seriesUid=1.2.840.113619.2.21.3408.700.0.757923840.3.0&objectUid=1.2.840.11361907579238403408700.3.0.14.19970327150033")
        self.assertEqual(inst.deviceName, "G.E. Medical Systems")
        self.assertEqual(inst.height, 480)
        self.assertEqual(inst.identifier[0].label, "InstanceUID")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.2.840.11361907579238403408700.3.0.14.19970327150033")
        self.assertEqual(inst.identifier[1].label, "accessionNo")
        self.assertEqual(inst.identifier[1].system, "http://acme-imaging.com/accession/2012")
        self.assertEqual(inst.identifier[1].value, "1234567")
        self.assertEqual(inst.identifier[2].label, "studyId")
        self.assertEqual(inst.identifier[2].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[2].value, "urn:oid:1.2.840.113619.2.21.848.34082.0.538976288.3")
        self.assertEqual(inst.identifier[3].label, "seriesId")
        self.assertEqual(inst.identifier[3].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[3].value, "urn:oid:1.2.840.113619.2.21.3408.700.0.757923840.3.0")
        self.assertEqual(inst.subject.reference, "Patient/example")
        self.assertEqual(inst.subtype.coding[0].code, "US")
        self.assertEqual(inst.subtype.coding[0].system, "http://nema.org/dicom/dcid")
        self.assertEqual(inst.text.div, "<div>\n      Ultrasound Image on patient &quot;James Chalmers&quot;:<br/>\n      <img alt=\"WADO reference to image\" src=\"http://imaging.acme.com/wado/server?requestType=WADO&amp;contentType=application%2Fdicom&amp;studyUid=1.2.840.113619.2.21.848.34082.0.538976288.3&amp;seriesUid=1.2.840.113619.2.21.3408.700.0.757923840.3.0&amp;objectUid=1.2.840.11361907579238403408700.3.0.14.19970327150033\"/>\n        \n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "photo")
        self.assertEqual(inst.width, 640)

