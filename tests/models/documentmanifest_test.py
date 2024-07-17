#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import documentmanifest
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class DocumentManifestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DocumentManifest", js["resourceType"])
        return documentmanifest.DocumentManifest(js)
    
    def testDocumentManifest1(self):
        inst = self.instantiate_from("documentmanifest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DocumentManifest instance")
        self.implDocumentManifest1(inst)
        
        js = inst.as_json()
        self.assertEqual("DocumentManifest", js["resourceType"])
        inst2 = documentmanifest.DocumentManifest(js)
        self.implDocumentManifest1(inst2)
    
    def implDocumentManifest1(self, inst):
        self.assertEqual(inst.contained[0].id, "a1")
        self.assertEqual(inst.created.datetime, FHIRDateTime("2004-12-25T23:50:50-05:00").datetime)
        self.assertEqual(inst.created.as_json(), "2004-12-25T23:50:50-05:00")
        self.assertEqual(inst.description, "Physical")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org/documents")
        self.assertEqual(inst.identifier[0].value, "23425234234-2347")
        self.assertEqual(inst.masterIdentifier.system, "http://example.org/documents")
        self.assertEqual(inst.masterIdentifier.value, "23425234234-2346")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.related[0].identifier.system, "http://example.org/documents")
        self.assertEqual(inst.related[0].identifier.value, "23425234234-9999")
        self.assertEqual(inst.source, "urn:oid:1.3.6.1.4.1.21367.2009.1.2.1")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Text</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.text, "History and Physical")

