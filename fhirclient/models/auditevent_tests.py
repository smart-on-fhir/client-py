#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import auditevent
from .fhirdate import FHIRDate


class AuditEventTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AuditEvent", js["resourceType"])
        return auditevent.AuditEvent(js)
    
    def testAuditEvent1(self):
        inst = self.instantiate_from("audit-event-example-login.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent1(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent1(inst2)
    
    def implAuditEvent1(self, inst):
        self.assertEqual(inst.event.action, "E")
        self.assertEqual(inst.event.dateTime.date, FHIRDate("2013-06-20T23:41:23Z").date)
        self.assertEqual(inst.event.dateTime.as_json(), "2013-06-20T23:41:23Z")
        self.assertEqual(inst.event.outcome, "0")
        self.assertEqual(inst.event.subtype[0].coding[0].code, "110122")
        self.assertEqual(inst.event.subtype[0].coding[0].display, "Login")
        self.assertEqual(inst.event.subtype[0].coding[0].system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.event.type.coding[0].code, "110114")
        self.assertEqual(inst.event.type.coding[0].display, "User Authentication")
        self.assertEqual(inst.event.type.coding[0].system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.id, "example-login")
        self.assertEqual(inst.participant[0].altId, "601847123")
        self.assertEqual(inst.participant[0].name, "Grahame Grieve")
        self.assertEqual(inst.participant[0].network.identifier, "127.0.0.1")
        self.assertEqual(inst.participant[0].network.type, "2")
        self.assertTrue(inst.participant[0].requestor)
        self.assertEqual(inst.participant[0].userId, "95")
        self.assertEqual(inst.source.identifier, "hl7connect.healthintersections.com.au")
        self.assertEqual(inst.source.site, "Cloud")
        self.assertEqual(inst.source.type[0].code, "3")
        self.assertEqual(inst.source.type[0].display, "Web Server")
        self.assertEqual(inst.source.type[0].system, "http://hl7.org/fhir/security-source-type")
        self.assertEqual(inst.text.status, "generated")
    
    def testAuditEvent2(self):
        inst = self.instantiate_from("audit-event-example-logout.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent2(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent2(inst2)
    
    def implAuditEvent2(self, inst):
        self.assertEqual(inst.event.action, "E")
        self.assertEqual(inst.event.dateTime.date, FHIRDate("2013-06-20T23:46:41Z").date)
        self.assertEqual(inst.event.dateTime.as_json(), "2013-06-20T23:46:41Z")
        self.assertEqual(inst.event.outcome, "0")
        self.assertEqual(inst.event.subtype[0].coding[0].code, "110123")
        self.assertEqual(inst.event.subtype[0].coding[0].display, "Logout")
        self.assertEqual(inst.event.subtype[0].coding[0].system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.event.type.coding[0].code, "110114")
        self.assertEqual(inst.event.type.coding[0].display, "User Authentication")
        self.assertEqual(inst.event.type.coding[0].system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.id, "example-logout")
        self.assertEqual(inst.participant[0].altId, "601847123")
        self.assertEqual(inst.participant[0].name, "Grahame Grieve")
        self.assertEqual(inst.participant[0].network.identifier, "127.0.0.1")
        self.assertEqual(inst.participant[0].network.type, "2")
        self.assertTrue(inst.participant[0].requestor)
        self.assertEqual(inst.participant[0].userId, "95")
        self.assertEqual(inst.source.identifier, "hl7connect.healthintersections.com.au")
        self.assertEqual(inst.source.site, "Cloud")
        self.assertEqual(inst.source.type[0].code, "3")
        self.assertEqual(inst.source.type[0].display, "Web Server")
        self.assertEqual(inst.source.type[0].system, "http://hl7.org/fhir/security-source-type")
        self.assertEqual(inst.text.status, "generated")
    
    def testAuditEvent3(self):
        inst = self.instantiate_from("audit-event-example-vread.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent3(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent3(inst2)
    
    def implAuditEvent3(self, inst):
        self.assertEqual(inst.event.action, "R")
        self.assertEqual(inst.event.dateTime.date, FHIRDate("2013-06-20T23:42:24Z").date)
        self.assertEqual(inst.event.dateTime.as_json(), "2013-06-20T23:42:24Z")
        self.assertEqual(inst.event.outcome, "0")
        self.assertEqual(inst.event.subtype[0].coding[0].code, "vread")
        self.assertEqual(inst.event.subtype[0].coding[0].display, "vread")
        self.assertEqual(inst.event.subtype[0].coding[0].system, "http://hl7.org/fhir/restful-interaction")
        self.assertEqual(inst.event.type.coding[0].code, "rest")
        self.assertEqual(inst.event.type.coding[0].display, "Restful Operation")
        self.assertEqual(inst.event.type.coding[0].system, "http://hl7.org/fhir/audit-event-type")
        self.assertEqual(inst.id, "example-rest")
        self.assertEqual(inst.object[0].lifecycle, "6")
        self.assertEqual(inst.object[0].type, "2")
        self.assertEqual(inst.participant[0].altId, "601847123")
        self.assertEqual(inst.participant[0].name, "Grahame Grieve")
        self.assertTrue(inst.participant[0].requestor)
        self.assertEqual(inst.participant[0].userId, "95")
        self.assertEqual(inst.source.identifier, "hl7connect.healthintersections.com.au")
        self.assertEqual(inst.source.site, "Cloud")
        self.assertEqual(inst.source.type[0].code, "3")
        self.assertEqual(inst.source.type[0].display, "Web Server")
        self.assertEqual(inst.source.type[0].system, "http://hl7.org/fhir/security-source-type")
        self.assertEqual(inst.text.status, "generated")
    
    def testAuditEvent4(self):
        inst = self.instantiate_from("auditevent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AuditEvent instance")
        self.implAuditEvent4(inst)
        
        js = inst.as_json()
        self.assertEqual("AuditEvent", js["resourceType"])
        inst2 = auditevent.AuditEvent(js)
        self.implAuditEvent4(inst2)
    
    def implAuditEvent4(self, inst):
        self.assertEqual(inst.event.action, "E")
        self.assertEqual(inst.event.dateTime.date, FHIRDate("2012-10-25T22:04:27+11:00").date)
        self.assertEqual(inst.event.dateTime.as_json(), "2012-10-25T22:04:27+11:00")
        self.assertEqual(inst.event.outcome, "0")
        self.assertEqual(inst.event.subtype[0].coding[0].code, "110120")
        self.assertEqual(inst.event.subtype[0].coding[0].display, "Application Start")
        self.assertEqual(inst.event.subtype[0].coding[0].system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.event.type.coding[0].code, "110100")
        self.assertEqual(inst.event.type.coding[0].display, "Application Activity")
        self.assertEqual(inst.event.type.coding[0].system, "http://nema.org/dicom/dicm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.object[0].identifier.type.coding[0].code, "SNO")
        self.assertEqual(inst.object[0].identifier.type.coding[0].system, "http://hl7.org/fhir/v2/0203")
        self.assertEqual(inst.object[0].identifier.type.text, "Dell Serial Number")
        self.assertEqual(inst.object[0].identifier.value, "ABCDEF")
        self.assertEqual(inst.object[0].lifecycle, "6")
        self.assertEqual(inst.object[0].name, "Grahame's Laptop")
        self.assertEqual(inst.object[0].role, "4")
        self.assertEqual(inst.object[0].type, "4")
        self.assertEqual(inst.participant[0].network.identifier, "127.0.0.1")
        self.assertEqual(inst.participant[0].network.type, "2")
        self.assertFalse(inst.participant[0].requestor)
        self.assertEqual(inst.participant[0].role[0].text, "Service User (Logon)")
        self.assertEqual(inst.participant[0].userId, "Grahame")
        self.assertEqual(inst.source.identifier, "Grahame's Laptop")
        self.assertEqual(inst.source.site, "Development")
        self.assertEqual(inst.source.type[0].code, "1")
        self.assertEqual(inst.source.type[0].system, "http://hl7.org/fhir/audit-event-sub-type")
        self.assertEqual(inst.text.div, "<div>Application Start for under service login &quot;Grahame&quot; (id: Grahame's Test HL7Connect)</div>")
        self.assertEqual(inst.text.status, "generated")

