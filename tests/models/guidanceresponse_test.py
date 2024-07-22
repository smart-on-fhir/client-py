#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import guidanceresponse
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class GuidanceResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("GuidanceResponse", js["resourceType"])
        return guidanceresponse.GuidanceResponse(js)
    
    def testGuidanceResponse1(self):
        inst = self.instantiate_from("guidanceresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a GuidanceResponse instance")
        self.implGuidanceResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("GuidanceResponse", js["resourceType"])
        inst2 = guidanceresponse.GuidanceResponse(js)
        self.implGuidanceResponse1(inst2)
    
    def implGuidanceResponse1(self, inst):
        self.assertEqual(inst.contained[0].id, "outputParameters1")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://example.org")
        self.assertEqual(inst.identifier[0].value, "guidanceResponse1")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.moduleUri, "http://someguidelineprovider.org/radiology-appropriateness-guidelines.html")
        self.assertEqual(inst.occurrenceDateTime.datetime, FHIRDateTime("2017-03-10T16:02:00Z").datetime)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2017-03-10T16:02:00Z")
        self.assertEqual(inst.reasonCode[0].text, "Guideline Appropriate Ordering Assessment")
        self.assertEqual(inst.requestIdentifier.system, "http://example.org")
        self.assertEqual(inst.requestIdentifier.value, "guidanceRequest1")
        self.assertEqual(inst.status, "success")
        self.assertEqual(inst.text.status, "generated")

