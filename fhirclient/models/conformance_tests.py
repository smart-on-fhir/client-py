#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import conformance
from .fhirdate import FHIRDate


class ConformanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Conformance", js["resourceType"])
        return conformance.Conformance(js)
    
    def testConformance1(self):
        inst = self.instantiate_from("conformance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Conformance instance")
        self.implConformance1(inst)
        
        js = inst.as_json()
        self.assertEqual("Conformance", js["resourceType"])
        inst2 = conformance.Conformance(js)
        self.implConformance1(inst2)
    
    def implConformance1(self, inst):
        self.assertTrue(inst.acceptUnknown)
        self.assertEqual(inst.contact[0].telecom[0].system, "email")
        self.assertEqual(inst.contact[0].telecom[0].value, "wile@acme.org")
        self.assertEqual(inst.date.date, FHIRDate("2012-01-04").date)
        self.assertEqual(inst.date.as_json(), "2012-01-04")
        self.assertEqual(inst.description, "This is the FHIR conformance statement for the main EHR at ACME for the private interface - it does not describe the public interface")
        self.assertEqual(inst.document[0].documentation, "Basic rules for all documents in the EHR system")
        self.assertEqual(inst.document[0].mode, "consumer")
        self.assertEqual(inst.fhirVersion, "0.07")
        self.assertEqual(inst.format[0], "xml")
        self.assertEqual(inst.format[1], "json")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.messaging[0].event[0].code.code, "admin-notify")
        self.assertEqual(inst.messaging[0].event[0].code.system, "http://hl7.org/fhir/message-type")
        self.assertEqual(inst.messaging[0].event[0].focus, "Patient")
        self.assertEqual(inst.messaging[0].event[0].mode, "receiver")
        self.assertEqual(inst.name, "ACME EHR Conformance statement")
        self.assertEqual(inst.publisher, "ACME Corporation")
        self.assertEqual(inst.rest[0].interaction[0].code, "transaction")
        self.assertEqual(inst.rest[0].interaction[1].code, "history-system")
        self.assertEqual(inst.rest[0].mode, "server")
        self.assertEqual(inst.rest[0].resource[0].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].code, "vread")
        self.assertEqual(inst.rest[0].resource[0].interaction[2].code, "update")
        self.assertEqual(inst.rest[0].resource[0].interaction[3].code, "history-instance")
        self.assertEqual(inst.rest[0].resource[0].interaction[4].code, "create")
        self.assertEqual(inst.rest[0].resource[0].interaction[5].code, "history-type")
        self.assertEqual(inst.rest[0].resource[0].type, "Patient")
        self.assertEqual(inst.software.name, "EHR")
        self.assertEqual(inst.software.version, "0.00.020.2134")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "68D043B5-9ECF-4559-A57A-396E0D452311")
        self.assertEqual(inst.version, "20130510")
    
    def testConformance2(self):
        inst = self.instantiate_from("conformance-phr-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Conformance instance")
        self.implConformance2(inst)
        
        js = inst.as_json()
        self.assertEqual("Conformance", js["resourceType"])
        inst2 = conformance.Conformance(js)
        self.implConformance2(inst2)
    
    def implConformance2(self, inst):
        self.assertFalse(inst.acceptUnknown)
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2013-06-18").date)
        self.assertEqual(inst.date.as_json(), "2013-06-18")
        self.assertEqual(inst.description, "Prototype Conformance Statement for September 2013 Connectathon")
        self.assertEqual(inst.fhirVersion, "0.09")
        self.assertEqual(inst.format[0], "json")
        self.assertEqual(inst.format[1], "xml")
        self.assertEqual(inst.id, "phr")
        self.assertEqual(inst.name, "PHR Template")
        self.assertEqual(inst.publisher, "FHIR Project")
        self.assertEqual(inst.rest[0].documentation, "Protoype server conformance statement for September 2013 Connectathon")
        self.assertEqual(inst.rest[0].mode, "server")
        self.assertEqual(inst.rest[0].resource[0].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[0].interaction[1].documentation, "When a client searches patients with no search criteria, they get a list of all patients they have access too. Servers may elect to offer additional search parameters, but this is not required")
        self.assertEqual(inst.rest[0].resource[0].type, "Patient")
        self.assertEqual(inst.rest[0].resource[1].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[1].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].documentation, "_id parameter always supported. For the connectathon, servers may elect which search parameters are supported")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[1].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[1].type, "DocumentReference")
        self.assertEqual(inst.rest[0].resource[2].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[2].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].documentation, "Standard _id parameter")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[2].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[2].type, "Condition")
        self.assertEqual(inst.rest[0].resource[3].interaction[0].code, "read")
        self.assertEqual(inst.rest[0].resource[3].interaction[1].code, "search-type")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].documentation, "Standard _id parameter")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].name, "_id")
        self.assertEqual(inst.rest[0].resource[3].searchParam[0].type, "token")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].documentation, "which diagnostic discipline/department created the report")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].name, "service")
        self.assertEqual(inst.rest[0].resource[3].searchParam[1].type, "token")
        self.assertEqual(inst.rest[0].resource[3].type, "DiagnosticReport")
        self.assertEqual(inst.rest[0].security.service[0].text, "OAuth")
        self.assertEqual(inst.text.status, "generated")

