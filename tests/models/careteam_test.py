#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import careteam
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class CareTeamTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CareTeam", js["resourceType"])
        return careteam.CareTeam(js)
    
    def testCareTeam1(self):
        inst = self.instantiate_from("careteam-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CareTeam instance")
        self.implCareTeam1(inst)
        
        js = inst.as_json()
        self.assertEqual("CareTeam", js["resourceType"])
        inst2 = careteam.CareTeam(js)
        self.implCareTeam1(inst2)
    
    def implCareTeam1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "LA27976-2")
        self.assertEqual(inst.category[0].coding[0].display, "Encounter-focused care team")
        self.assertEqual(inst.category[0].coding[0].system, "http://loinc.org")
        self.assertEqual(inst.contained[0].id, "pr1")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Peter James Charlmers Care Plan for Inpatient Encounter")
        self.assertEqual(inst.participant[0].role[0].text, "responsiblePerson")
        self.assertEqual(inst.participant[1].period.end.datetime, FHIRDateTime("2013-01-01").datetime)
        self.assertEqual(inst.participant[1].period.end.as_json(), "2013-01-01")
        self.assertEqual(inst.participant[1].role[0].text, "adviser")
        self.assertEqual(inst.period.end.datetime, FHIRDateTime("2013-01-01").datetime)
        self.assertEqual(inst.period.end.as_json(), "2013-01-01")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Care Team</div>")
        self.assertEqual(inst.text.status, "generated")

