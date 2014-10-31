#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from securityevent import SecurityEvent
from fhirdate import FHIRDate


class SecurityEventTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = SecurityEvent(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testSecurityEvent1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/security-event-example-login.json")
        self.assertIsNotNone(inst, "Must have instantiated a SecurityEvent instance")
    
        self.assertEqual(inst.event.action, "E")
        self.assertEqual(inst.event.dateTime.date, FHIRDate("2013-06-20T23:41:23Z").date)
        self.assertEqual(inst.event.dateTime.isostring, "2013-06-20T23:41:23Z")
        self.assertEqual(inst.event.outcome, "0")
        self.assertEqual(inst.event.subtype[0].coding[0].code, "110122")
        self.assertEqual(inst.event.subtype[0].coding[0].display, "Login")
        self.assertEqual(inst.event.subtype[0].coding[0].system, "http://nema.org/dicom/dcid")
        self.assertEqual(inst.event.type.coding[0].code, "110114")
        self.assertEqual(inst.event.type.coding[0].display, "User Authentication")
        self.assertEqual(inst.event.type.coding[0].system, "http://nema.org/dicom/dcid")
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
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <h3>Events</h3>\n      <table class=\"grid\">\n        <tr>\n          <td>\n            <b>Type</b>\n          </td>\n          <td>\n            <b>Subtype</b>\n          </td>\n          <td>\n            <b>Action</b>\n          </td>\n          <td>\n            <b>DateTime</b>\n          </td>\n          <td>\n            <b>Outcome</b>\n          </td>\n          <td>\n            <b>OutcomeDesc</b>\n          </td>\n        </tr>\n        <tr>\n          <td>\n            <span title=\"Codes: {http://nema.org/dicom/dcid 110114}\">User Authentication</span>\n          </td>\n          <td>\n            <span title=\"Codes: {http://nema.org/dicom/dcid 110122}\">Login</span>\n          </td>\n          <td>E</td>\n          <td>20-Jun 2013 23:41</td>\n          <td>_0</td>\n          <td> </td>\n        </tr>\n      </table>\n      <blockquote>\n        <p>\n          <b>participant</b>\n        </p>\n        <p>\n          <b>userId</b>: 95\n        </p>\n        <p>\n          <b>altId</b>: 601847123\n        </p>\n        <p>\n          <b>name</b>: Grahame Grieve\n        </p>\n        <p>\n          <b>requestor</b>: true\n        </p>\n        <h3>Networks</h3>\n        <table class=\"grid\">\n          <tr>\n            <td>\n              <b>Identifier</b>\n            </td>\n            <td>\n              <b>Type</b>\n            </td>\n          </tr>\n          <tr>\n            <td>127.0.0.1</td>\n            <td>_2</td>\n          </tr>\n        </table>\n      </blockquote>\n      <h3>Sources</h3>\n      <table class=\"grid\">\n        <tr>\n          <td>\n            <b>Site</b>\n          </td>\n          <td>\n            <b>Identifier</b>\n          </td>\n          <td>\n            <b>Type</b>\n          </td>\n        </tr>\n        <tr>\n          <td>Cloud</td>\n          <td>hl7connect.healthintersections.com.au</td>\n          <td>\n            <span title=\"{http://hl7.org/fhir/security-source-type 3}\">Web Server</span>\n          </td>\n        </tr>\n      </table>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testSecurityEvent2(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/security-event-example-logout.json")
        self.assertIsNotNone(inst, "Must have instantiated a SecurityEvent instance")
    
        self.assertEqual(inst.event.action, "E")
        self.assertEqual(inst.event.dateTime.date, FHIRDate("2013-06-20T23:46:41Z").date)
        self.assertEqual(inst.event.dateTime.isostring, "2013-06-20T23:46:41Z")
        self.assertEqual(inst.event.outcome, "0")
        self.assertEqual(inst.event.subtype[0].coding[0].code, "110123")
        self.assertEqual(inst.event.subtype[0].coding[0].display, "Logout")
        self.assertEqual(inst.event.subtype[0].coding[0].system, "http://nema.org/dicom/dcid")
        self.assertEqual(inst.event.type.coding[0].code, "110114")
        self.assertEqual(inst.event.type.coding[0].display, "User Authentication")
        self.assertEqual(inst.event.type.coding[0].system, "http://nema.org/dicom/dcid")
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
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <h3>Events</h3>\n      <table class=\"grid\">\n        <tr>\n          <td>\n            <b>Type</b>\n          </td>\n          <td>\n            <b>Subtype</b>\n          </td>\n          <td>\n            <b>Action</b>\n          </td>\n          <td>\n            <b>DateTime</b>\n          </td>\n          <td>\n            <b>Outcome</b>\n          </td>\n          <td>\n            <b>OutcomeDesc</b>\n          </td>\n        </tr>\n        <tr>\n          <td>\n            <span title=\"Codes: {http://nema.org/dicom/dcid 110114}\">User Authentication</span>\n          </td>\n          <td>\n            <span title=\"Codes: {http://nema.org/dicom/dcid 110123}\">Logout</span>\n          </td>\n          <td>E</td>\n          <td>20-Jun 2013 23:46</td>\n          <td>_0</td>\n          <td> </td>\n        </tr>\n      </table>\n      <blockquote>\n        <p>\n          <b>participant</b>\n        </p>\n        <p>\n          <b>userId</b>: 95\n        </p>\n        <p>\n          <b>altId</b>: 601847123\n        </p>\n        <p>\n          <b>name</b>: Grahame Grieve\n        </p>\n        <p>\n          <b>requestor</b>: true\n        </p>\n        <h3>Networks</h3>\n        <table class=\"grid\">\n          <tr>\n            <td>\n              <b>Identifier</b>\n            </td>\n            <td>\n              <b>Type</b>\n            </td>\n          </tr>\n          <tr>\n            <td>127.0.0.1</td>\n            <td>_2</td>\n          </tr>\n        </table>\n      </blockquote>\n      <h3>Sources</h3>\n      <table class=\"grid\">\n        <tr>\n          <td>\n            <b>Site</b>\n          </td>\n          <td>\n            <b>Identifier</b>\n          </td>\n          <td>\n            <b>Type</b>\n          </td>\n        </tr>\n        <tr>\n          <td>Cloud</td>\n          <td>hl7connect.healthintersections.com.au</td>\n          <td>\n            <span title=\"{http://hl7.org/fhir/security-source-type 3}\">Web Server</span>\n          </td>\n        </tr>\n      </table>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testSecurityEvent3(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/security-event-example-vread.json")
        self.assertIsNotNone(inst, "Must have instantiated a SecurityEvent instance")
    
        self.assertEqual(inst.event.action, "R")
        self.assertEqual(inst.event.dateTime.date, FHIRDate("2013-06-20T23:42:24Z").date)
        self.assertEqual(inst.event.dateTime.isostring, "2013-06-20T23:42:24Z")
        self.assertEqual(inst.event.outcome, "0")
        self.assertEqual(inst.event.subtype[0].coding[0].code, "vread")
        self.assertEqual(inst.event.subtype[0].coding[0].display, "vread")
        self.assertEqual(inst.event.subtype[0].coding[0].system, "http://hl7.org/fhir/restful-operation")
        self.assertEqual(inst.event.type.coding[0].code, "rest")
        self.assertEqual(inst.event.type.coding[0].display, "Restful Operation")
        self.assertEqual(inst.event.type.coding[0].system, "http://hl7.org/fhir/security-event-type")
        self.assertEqual(inst.object[0].lifecycle, "6")
        self.assertEqual(inst.object[0].reference.reference, "Patient/example/history/1")
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
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <h3>Events</h3>\n      <table class=\"grid\">\n        <tr>\n          <td>\n            <b>Type</b>\n          </td>\n          <td>\n            <b>Subtype</b>\n          </td>\n          <td>\n            <b>Action</b>\n          </td>\n          <td>\n            <b>DateTime</b>\n          </td>\n          <td>\n            <b>Outcome</b>\n          </td>\n          <td>\n            <b>OutcomeDesc</b>\n          </td>\n        </tr>\n        <tr>\n          <td>\n            <span title=\"Codes: {http://hl7.org/fhir/security-event-type rest}\">Restful Operation</span>\n          </td>\n          <td>\n            <span title=\"Codes: {http://hl7.org/fhir/restful-operation vread}\">vread</span>\n          </td>\n          <td>R</td>\n          <td>20-Jun 2013 23:42</td>\n          <td>_0</td>\n          <td> </td>\n        </tr>\n      </table>\n      <blockquote>\n        <p>\n          <b>participant</b>\n        </p>\n        <p>\n          <b>userId</b>: 95\n        </p>\n        <p>\n          <b>altId</b>: 601847123\n        </p>\n        <p>\n          <b>name</b>: Grahame Grieve\n        </p>\n        <p>\n          <b>requestor</b>: true\n        </p>\n      </blockquote>\n      <h3>Sources</h3>\n      <table class=\"grid\">\n        <tr>\n          <td>\n            <b>Site</b>\n          </td>\n          <td>\n            <b>Identifier</b>\n          </td>\n          <td>\n            <b>Type</b>\n          </td>\n        </tr>\n        <tr>\n          <td>Cloud</td>\n          <td>hl7connect.healthintersections.com.au</td>\n          <td>\n            <span title=\"{http://hl7.org/fhir/security-source-type 3}\">Web Server</span>\n          </td>\n        </tr>\n      </table>\n      <blockquote>\n        <p>\n          <b>object</b>\n        </p>\n        <p>\n          <b>reference</b>: \n          <a href=\"Patient/example/history/1\">Patient/example/history/1</a>\n        </p>\n        <p>\n          <b>type</b>: _2\n        </p>\n        <p>\n          <b>lifecycle</b>: _6\n        </p>\n      </blockquote>\n    </div>")
        self.assertEqual(inst.text.status, "generated")

