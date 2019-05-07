#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import endpoint
from .fhirdate import FHIRDate


class EndpointTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Endpoint", js["resourceType"])
        return endpoint.Endpoint(js)
    
    def testEndpoint1(self):
        inst = self.instantiate_from("endpoint-example-iid.json")
        self.assertIsNotNone(inst, "Must have instantiated a Endpoint instance")
        self.implEndpoint1(inst)
        
        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint1(inst2)
    
    def implEndpoint1(self, inst):
        self.assertEqual(inst.address, "https://pacs.hospital.org/IHEInvokeImageDisplay")
        self.assertEqual(inst.connectionType.code, "ihe-iid")
        self.assertEqual(inst.connectionType.system, "http://terminology.hl7.org/CodeSystem/endpoint-connection-type")
        self.assertEqual(inst.id, "example-iid")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "PACS Hospital Invoke Image Display endpoint")
        self.assertEqual(inst.payloadType[0].text, "DICOM IID")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testEndpoint2(self):
        inst = self.instantiate_from("endpoint-example-direct.json")
        self.assertIsNotNone(inst, "Must have instantiated a Endpoint instance")
        self.implEndpoint2(inst)
        
        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint2(inst2)
    
    def implEndpoint2(self, inst):
        self.assertEqual(inst.address, "mailto:MARTIN.SMIETANKA@directnppes.com")
        self.assertEqual(inst.connectionType.code, "direct-project")
        self.assertEqual(inst.id, "direct-endpoint")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "MARTIN SMIETANKA")
        self.assertEqual(inst.payloadType[0].coding[0].code, "urn:hl7-org:sdwg:ccda-structuredBody:1.1")
        self.assertEqual(inst.payloadType[0].coding[0].system, "urn:oid:1.3.6.1.4.1.19376.1.2.3")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testEndpoint3(self):
        inst = self.instantiate_from("endpoint-example-wadors.json")
        self.assertIsNotNone(inst, "Must have instantiated a Endpoint instance")
        self.implEndpoint3(inst)
        
        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint3(inst2)
    
    def implEndpoint3(self, inst):
        self.assertEqual(inst.address, "https://pacs.hospital.org/wado-rs")
        self.assertEqual(inst.connectionType.code, "dicom-wado-rs")
        self.assertEqual(inst.connectionType.system, "http://terminology.hl7.org/CodeSystem/endpoint-connection-type")
        self.assertEqual(inst.id, "example-wadors")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "PACS Hospital DICOM WADO-RS endpoint")
        self.assertEqual(inst.payloadMimeType[0], "application/dicom")
        self.assertEqual(inst.payloadType[0].text, "DICOM WADO-RS")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testEndpoint4(self):
        inst = self.instantiate_from("endpoint-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Endpoint instance")
        self.implEndpoint4(inst)
        
        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint4(inst2)
    
    def implEndpoint4(self, inst):
        self.assertEqual(inst.address, "http://fhir3.healthintersections.com.au/open/CarePlan")
        self.assertEqual(inst.connectionType.code, "hl7-fhir-rest")
        self.assertEqual(inst.connectionType.system, "http://terminology.hl7.org/CodeSystem/endpoint-connection-type")
        self.assertEqual(inst.contact[0].system, "email")
        self.assertEqual(inst.contact[0].use, "work")
        self.assertEqual(inst.contact[0].value, "endpointmanager@example.org")
        self.assertEqual(inst.header[0], "bearer-code BASGS534s4")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org/enpoint-identifier")
        self.assertEqual(inst.identifier[0].value, "epcp12")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Health Intersections CarePlan Hub")
        self.assertEqual(inst.payloadMimeType[0], "application/fhir+xml")
        self.assertEqual(inst.payloadType[0].coding[0].code, "CarePlan")
        self.assertEqual(inst.payloadType[0].coding[0].system, "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.period.start.date, FHIRDate("2014-09-01").date)
        self.assertEqual(inst.period.start.as_json(), "2014-09-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

