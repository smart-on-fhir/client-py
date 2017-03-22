#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import testreport
from .fhirdate import FHIRDate


class TestReportTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("TestReport", js["resourceType"])
        return testreport.TestReport(js)
    
    def testTestReport1(self):
        inst = self.instantiate_from("testreport-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a TestReport instance")
        self.implTestReport1(inst)
        
        js = inst.as_json()
        self.assertEqual("TestReport", js["resourceType"])
        inst2 = testreport.TestReport(js)
        self.implTestReport1(inst2)
    
    def implTestReport1(self, inst):
        self.assertEqual(inst.id, "testreport-example")
        self.assertEqual(inst.identifier.system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier.value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.9878")
        self.assertEqual(inst.issued.date, FHIRDate("2016-10-07T08:25:34-05:00").date)
        self.assertEqual(inst.issued.as_json(), "2016-10-07T08:25:34-05:00")
        self.assertEqual(inst.name, "TestReport Example for TestScript Example")
        self.assertEqual(inst.participant[0].display, "Crucible")
        self.assertEqual(inst.participant[0].type, "test-engine")
        self.assertEqual(inst.participant[0].uri, "http://projectcrucible.org")
        self.assertEqual(inst.participant[1].display, "HealthIntersections STU3")
        self.assertEqual(inst.participant[1].type, "server")
        self.assertEqual(inst.participant[1].uri, "http://fhir3.healthintersections.com.au/open")
        self.assertEqual(inst.result, "pass")
        self.assertEqual(inst.score, 100.0)
        self.assertEqual(inst.setup.action[0].operation.detail, "http://projectcrucible.org/permalink/1")
        self.assertEqual(inst.setup.action[0].operation.message, "DELETE Patient")
        self.assertEqual(inst.setup.action[0].operation.result, "pass")
        self.assertEqual(inst.setup.action[1].assert_fhir.detail, "http://projectcrucible.org/permalink/1")
        self.assertEqual(inst.setup.action[1].assert_fhir.message, "HTTP 204")
        self.assertEqual(inst.setup.action[1].assert_fhir.result, "pass")
        self.assertEqual(inst.setup.action[2].operation.detail, "http://projectcrucible.org/permalink/1")
        self.assertEqual(inst.setup.action[2].operation.message, "POST Patient/fixture-patient-create")
        self.assertEqual(inst.setup.action[2].operation.result, "pass")
        self.assertEqual(inst.setup.action[3].assert_fhir.detail, "http://projectcrucible.org/permalink/1")
        self.assertEqual(inst.setup.action[3].assert_fhir.message, "HTTP 201")
        self.assertEqual(inst.setup.action[3].assert_fhir.result, "pass")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.teardown.action[0].operation.detail, "http://projectcrucible.org/permalink/3")
        self.assertEqual(inst.teardown.action[0].operation.message, "DELETE Patient/fixture-patient-create.")
        self.assertEqual(inst.teardown.action[0].operation.result, "pass")
        self.assertEqual(inst.test[0].action[0].operation.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[0].operation.message, "GET Patient/fixture-patient-create")
        self.assertEqual(inst.test[0].action[0].operation.result, "pass")
        self.assertEqual(inst.test[0].action[1].assert_fhir.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[1].assert_fhir.message, "HTTP 200")
        self.assertEqual(inst.test[0].action[1].assert_fhir.result, "pass")
        self.assertEqual(inst.test[0].action[2].assert_fhir.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[2].assert_fhir.message, "Last-Modified Present")
        self.assertEqual(inst.test[0].action[2].assert_fhir.result, "pass")
        self.assertEqual(inst.test[0].action[3].assert_fhir.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[3].assert_fhir.message, "Response is Patient")
        self.assertEqual(inst.test[0].action[3].assert_fhir.result, "pass")
        self.assertEqual(inst.test[0].action[4].assert_fhir.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[4].assert_fhir.message, "Response validates")
        self.assertEqual(inst.test[0].action[4].assert_fhir.result, "pass")
        self.assertEqual(inst.test[0].action[5].assert_fhir.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[5].assert_fhir.message, "Patient.name.family 'Chalmers'")
        self.assertEqual(inst.test[0].action[5].assert_fhir.result, "pass")
        self.assertEqual(inst.test[0].action[6].assert_fhir.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[6].assert_fhir.message, "Patient.name.given 'Peter'")
        self.assertEqual(inst.test[0].action[6].assert_fhir.result, "pass")
        self.assertEqual(inst.test[0].action[7].assert_fhir.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[7].assert_fhir.message, "Patient.name.family 'Chalmers'")
        self.assertEqual(inst.test[0].action[7].assert_fhir.result, "pass")
        self.assertEqual(inst.test[0].action[8].assert_fhir.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[8].assert_fhir.message, "Patient.name.family 'Chalmers'")
        self.assertEqual(inst.test[0].action[8].assert_fhir.result, "pass")
        self.assertEqual(inst.test[0].action[9].assert_fhir.detail, "http://projectcrucible.org/permalink/2")
        self.assertEqual(inst.test[0].action[9].assert_fhir.message, "Patient expected values.")
        self.assertEqual(inst.test[0].action[9].assert_fhir.result, "pass")
        self.assertEqual(inst.test[0].description, "Read a Patient and validate response.")
        self.assertEqual(inst.test[0].id, "01-ReadPatient")
        self.assertEqual(inst.test[0].name, "Read Patient")
        self.assertEqual(inst.tester, "HL7 Execution Engine")
        self.assertEqual(inst.text.status, "generated")

