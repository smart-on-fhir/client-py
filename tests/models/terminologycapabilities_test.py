#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import terminologycapabilities
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class TerminologyCapabilitiesTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("TerminologyCapabilities", js["resourceType"])
        return terminologycapabilities.TerminologyCapabilities(js)
    
    def testTerminologyCapabilities1(self):
        inst = self.instantiate_from("terminologycapabilities-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a TerminologyCapabilities instance")
        self.implTerminologyCapabilities1(inst)
        
        js = inst.as_json()
        self.assertEqual("TerminologyCapabilities", js["resourceType"])
        inst2 = terminologycapabilities.TerminologyCapabilities(js)
        self.implTerminologyCapabilities1(inst2)
    
    def implTerminologyCapabilities1(self, inst):
        self.assertEqual(inst.codeSearch, "explicit")
        self.assertEqual(inst.contact[0].name, "System Administrator")
        self.assertEqual(inst.contact[0].telecom[0].system, "email")
        self.assertEqual(inst.contact[0].telecom[0].value, "wile@acme.org")
        self.assertEqual(inst.date.datetime, FHIRDateTime("2012-01-04").datetime)
        self.assertEqual(inst.date.as_json(), "2012-01-04")
        self.assertEqual(inst.description, "This is the FHIR capability statement for the main EHR at ACME for the private interface - it does not describe the public interface")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.implementation.description, "Acme Terminology Server")
        self.assertEqual(inst.implementation.url, "http://example.org/tx")
        self.assertEqual(inst.kind, "instance")
        self.assertEqual(inst.name, "ACME-EHR")
        self.assertEqual(inst.publisher, "ACME Corporation")
        self.assertEqual(inst.software.name, "TxServer")
        self.assertEqual(inst.software.version, "0.1.2")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "ACME EHR capability statement")
        self.assertEqual(inst.url, "urn:uuid:68D043B5-9ECF-4559-A57A-396E0D452311")
        self.assertEqual(inst.version, "20130510")

