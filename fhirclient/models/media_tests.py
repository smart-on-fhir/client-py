#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import media
from .fhirdate import FHIRDate


class MediaTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Media", js["resourceType"])
        return media.Media(js)
    
    def testMedia1(self):
        inst = self.instantiate_from("media-example-dicom.json")
        self.assertIsNotNone(inst, "Must have instantiated a Media instance")
        self.implMedia1(inst)
        
        js = inst.as_json()
        self.assertEqual("Media", js["resourceType"])
        inst2 = media.Media(js)
        self.implMedia1(inst2)
    
    def implMedia1(self, inst):
        self.assertEqual(inst.content.contentType, "application/dicom")
        self.assertEqual(inst.extension[0].url, "http://nema.org/fhir/extensions#0002-0010")
        self.assertEqual(inst.extension[0].valueUri, "urn:oid:1.2.840.10008.1.2.1")
        self.assertEqual(inst.height, 480)
        self.assertEqual(inst.id, "1.2.840.11361907579238403408700.3.0.14.19970327150033")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].type.text, "InstanceUID")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.2.840.11361907579238403408700.3.0.14.19970327150033")
        self.assertEqual(inst.identifier[1].system, "http://acme-imaging.com/accession/2012")
        self.assertEqual(inst.identifier[1].type.text, "accessionNo")
        self.assertEqual(inst.identifier[1].value, "1234567")
        self.assertEqual(inst.identifier[2].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[2].type.text, "studyId")
        self.assertEqual(inst.identifier[2].value, "urn:oid:1.2.840.113619.2.21.848.34082.0.538976288.3")
        self.assertEqual(inst.identifier[3].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[3].type.text, "seriesId")
        self.assertEqual(inst.identifier[3].value, "urn:oid:1.2.840.113619.2.21.3408.700.0.757923840.3.0")
        self.assertEqual(inst.subtype.coding[0].code, "US")
        self.assertEqual(inst.subtype.coding[0].system, "http://dicom.nema.org/resources/ontology/DCM")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "photo")
        self.assertEqual(inst.view.coding[0].code, "399067008")
        self.assertEqual(inst.view.coding[0].display, "Lateral projection")
        self.assertEqual(inst.view.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.width, 640)
    
    def testMedia2(self):
        inst = self.instantiate_from("media-example-sound.json")
        self.assertIsNotNone(inst, "Must have instantiated a Media instance")
        self.implMedia2(inst)
        
        js = inst.as_json()
        self.assertEqual("Media", js["resourceType"])
        inst2 = media.Media(js)
        self.implMedia2(inst2)
    
    def implMedia2(self, inst):
        self.assertEqual(inst.content.contentType, "audio/mpeg")
        self.assertEqual(inst.content.data, "dG9vIGJpZyB0b28gaW5jbHVkZSB0aGUgd2hvbGU=")
        self.assertEqual(inst.content.id, "a1")
        self.assertEqual(inst.duration, 65)
        self.assertEqual(inst.id, "sound")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Sound recording of speech example for Patient Henry Levin (MRN 12345):<br/><img src=\"#11\" alt=\"diagram\"/></div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "video")
    
    def testMedia3(self):
        inst = self.instantiate_from("media-example-xray.json")
        self.assertIsNotNone(inst, "Must have instantiated a Media instance")
        self.implMedia3(inst)
        
        js = inst.as_json()
        self.assertEqual("Media", js["resourceType"])
        inst2 = media.Media(js)
        self.implMedia3(inst2)
    
    def implMedia3(self, inst):
        self.assertEqual(inst.bodySite.coding[0].code, "85151006")
        self.assertEqual(inst.bodySite.coding[0].display, "Structure of left hand (body structure)")
        self.assertEqual(inst.bodySite.coding[0].system, "http://snomed.info.sct")
        self.assertEqual(inst.content.contentType, "image/jpeg")
        self.assertEqual(inst.content.creation.date, FHIRDate("2016-03-15").date)
        self.assertEqual(inst.content.creation.as_json(), "2016-03-15")
        self.assertEqual(inst.content.id, "a1")
        self.assertEqual(inst.content.url, "http://someimagingcenter.org/fhir/Binary/A12345")
        self.assertEqual(inst.height, 432)
        self.assertEqual(inst.id, "xray")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-03-15").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-03-15")
        self.assertEqual(inst.subtype.coding[0].code, "39714003")
        self.assertEqual(inst.subtype.coding[0].display, "Skeletal X-ray of wrist and hand")
        self.assertEqual(inst.subtype.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Xray of left hand for Patient Henry Levin (MRN 12345) 2016-03-15</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "photo")
        self.assertEqual(inst.width, 640)
    
    def testMedia4(self):
        inst = self.instantiate_from("media-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Media instance")
        self.implMedia4(inst)
        
        js = inst.as_json()
        self.assertEqual("Media", js["resourceType"])
        inst2 = media.Media(js)
        self.implMedia4(inst2)
    
    def implMedia4(self, inst):
        self.assertEqual(inst.content.contentType, "image/gif")
        self.assertEqual(inst.content.creation.date, FHIRDate("2009-09-03").date)
        self.assertEqual(inst.content.creation.as_json(), "2009-09-03")
        self.assertEqual(inst.content.id, "a1")
        self.assertEqual(inst.frames, 1)
        self.assertEqual(inst.height, 145)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.subtype.coding[0].code, "diagram")
        self.assertEqual(inst.subtype.coding[0].system, "http://hl7.org/fhir/media-subtype")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Diagram for Patient Henry Levin (MRN 12345):<br/><img src=\"#11\" alt=\"diagram\"/></div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "photo")
        self.assertEqual(inst.width, 126)

