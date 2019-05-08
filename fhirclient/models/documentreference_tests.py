#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import documentreference
from .fhirdate import FHIRDate


class DocumentReferenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DocumentReference", js["resourceType"])
        return documentreference.DocumentReference(js)
    
    def testDocumentReference1(self):
        inst = self.instantiate_from("documentreference-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentReference instance")
        self.implDocumentReference1(inst)
        
        js = inst.as_json()
        self.assertEqual("DocumentReference", js["resourceType"])
        inst2 = documentreference.DocumentReference(js)
        self.implDocumentReference1(inst2)
    
    def implDocumentReference1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "History and Physical")
        self.assertEqual(inst.category[0].coding[0].display, "History and Physical")
        self.assertEqual(inst.category[0].coding[0].system, "http://ihe.net/xds/connectathon/classCodes")
        self.assertEqual(inst.contained[0].id, "a2")
        self.assertEqual(inst.content[0].attachment.contentType, "application/hl7-v3+xml")
        self.assertEqual(inst.content[0].attachment.creation.date, FHIRDate("2005-12-24T09:35:00+11:00").date)
        self.assertEqual(inst.content[0].attachment.creation.as_json(), "2005-12-24T09:35:00+11:00")
        self.assertEqual(inst.content[0].attachment.hash, "2jmj7l5rSw0yVb/vlWAYkK/YBwk=")
        self.assertEqual(inst.content[0].attachment.language, "en-US")
        self.assertEqual(inst.content[0].attachment.size, 3654)
        self.assertEqual(inst.content[0].attachment.title, "Physical")
        self.assertEqual(inst.content[0].attachment.url, "http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510")
        self.assertEqual(inst.content[0].format.code, "urn:ihe:pcc:handp:2008")
        self.assertEqual(inst.content[0].format.display, "History and Physical Specification")
        self.assertEqual(inst.content[0].format.system, "urn:oid:1.3.6.1.4.1.19376.1.2.3")
        self.assertEqual(inst.context.event[0].coding[0].code, "T-D8200")
        self.assertEqual(inst.context.event[0].coding[0].display, "Arm")
        self.assertEqual(inst.context.event[0].coding[0].system, "http://ihe.net/xds/connectathon/eventCodes")
        self.assertEqual(inst.context.facilityType.coding[0].code, "Outpatient")
        self.assertEqual(inst.context.facilityType.coding[0].display, "Outpatient")
        self.assertEqual(inst.context.facilityType.coding[0].system, "http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes")
        self.assertEqual(inst.context.period.end.date, FHIRDate("2004-12-23T08:01:00+11:00").date)
        self.assertEqual(inst.context.period.end.as_json(), "2004-12-23T08:01:00+11:00")
        self.assertEqual(inst.context.period.start.date, FHIRDate("2004-12-23T08:00:00+11:00").date)
        self.assertEqual(inst.context.period.start.as_json(), "2004-12-23T08:00:00+11:00")
        self.assertEqual(inst.context.practiceSetting.coding[0].code, "General Medicine")
        self.assertEqual(inst.context.practiceSetting.coding[0].display, "General Medicine")
        self.assertEqual(inst.context.practiceSetting.coding[0].system, "http://www.ihe.net/xds/connectathon/practiceSettingCodes")
        self.assertEqual(inst.date.date, FHIRDate("2005-12-24T09:43:41+11:00").date)
        self.assertEqual(inst.date.as_json(), "2005-12-24T09:43:41+11:00")
        self.assertEqual(inst.description, "Physical")
        self.assertEqual(inst.docStatus, "preliminary")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234")
        self.assertEqual(inst.masterIdentifier.system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.masterIdentifier.value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatesTo[0].code, "appends")
        self.assertEqual(inst.securityLabel[0].coding[0].code, "V")
        self.assertEqual(inst.securityLabel[0].coding[0].display, "very restricted")
        self.assertEqual(inst.securityLabel[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-Confidentiality")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "34108-1")
        self.assertEqual(inst.type.coding[0].display, "Outpatient Note")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")

