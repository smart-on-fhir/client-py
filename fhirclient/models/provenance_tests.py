#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import provenance
from .fhirdate import FHIRDate


class ProvenanceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Provenance", js["resourceType"])
        return provenance.Provenance(js)
    
    def testProvenance1(self):
        inst = self.instantiate_from("provenance-example-sig.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance1(inst)
        
        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance1(inst2)
    
    def implProvenance1(self, inst):
        self.assertEqual(inst.activity.coding[0].code, "AU")
        self.assertEqual(inst.activity.coding[0].display, "authenticated")
        self.assertEqual(inst.activity.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion")
        self.assertEqual(inst.agent[0].type.coding[0].code, "VERF")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/contractsignertypecodes")
        self.assertEqual(inst.id, "signature")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.reason[0].coding[0].code, "TREAT")
        self.assertEqual(inst.reason[0].coding[0].display, "treatment")
        self.assertEqual(inst.reason[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.recorded.date, FHIRDate("2015-08-27T08:39:24+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2015-08-27T08:39:24+10:00")
        self.assertEqual(inst.signature[0].data, "Li4u")
        self.assertEqual(inst.signature[0].sigFormat, "application/signature+xml")
        self.assertEqual(inst.signature[0].targetFormat, "application/fhir+xml")
        self.assertEqual(inst.signature[0].type[0].code, "1.2.840.10065.1.12.1.5")
        self.assertEqual(inst.signature[0].type[0].display, "Verification Signature")
        self.assertEqual(inst.signature[0].type[0].system, "urn:iso-astm:E1762-95:2013")
        self.assertEqual(inst.signature[0].when.date, FHIRDate("2015-08-27T08:39:24+10:00").date)
        self.assertEqual(inst.signature[0].when.as_json(), "2015-08-27T08:39:24+10:00")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">procedure record authored on 27-June 2015 by Harold Hippocrates, MD Content extracted from Referral received 26-June</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testProvenance2(self):
        inst = self.instantiate_from("provenance-example-cwl.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance2(inst)
        
        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance2(inst2)
    
    def implProvenance2(self, inst):
        self.assertEqual(inst.agent[0].type.coding[0].code, "AUT")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.entity[0].role, "source")
        self.assertEqual(inst.id, "example-cwl")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurredPeriod.start.date, FHIRDate("2016-11-30").date)
        self.assertEqual(inst.occurredPeriod.start.as_json(), "2016-11-30")
        self.assertEqual(inst.reason[0].text, "profiling Short Tandem Repeats (STRs) from high throughput sequencing data.")
        self.assertEqual(inst.recorded.date, FHIRDate("2016-12-01T08:12:14+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2016-12-01T08:12:14+10:00")
        self.assertEqual(inst.text.status, "generated")
    
    def testProvenance3(self):
        inst = self.instantiate_from("provenance-example-biocompute-object.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance3(inst)
        
        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance3(inst2)
    
    def implProvenance3(self, inst):
        self.assertEqual(inst.agent[0].type.coding[0].code, "AUT")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.entity[0].role, "source")
        self.assertEqual(inst.id, "example-biocompute-object")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurredPeriod.start.date, FHIRDate("2017-06-06").date)
        self.assertEqual(inst.occurredPeriod.start.as_json(), "2017-06-06")
        self.assertEqual(inst.reason[0].text, "antiviral resistance detection")
        self.assertEqual(inst.recorded.date, FHIRDate("2016-06-09T08:12:14+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2016-06-09T08:12:14+10:00")
        self.assertEqual(inst.text.status, "generated")
    
    def testProvenance4(self):
        inst = self.instantiate_from("provenance-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Provenance instance")
        self.implProvenance4(inst)
        
        js = inst.as_json()
        self.assertEqual("Provenance", js["resourceType"])
        inst2 = provenance.Provenance(js)
        self.implProvenance4(inst2)
    
    def implProvenance4(self, inst):
        self.assertEqual(inst.agent[0].type.coding[0].code, "AUT")
        self.assertEqual(inst.agent[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.agent[1].id, "a1")
        self.assertEqual(inst.agent[1].type.coding[0].code, "DEV")
        self.assertEqual(inst.agent[1].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.entity[0].role, "source")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurredPeriod.end.date, FHIRDate("2015-06-28").date)
        self.assertEqual(inst.occurredPeriod.end.as_json(), "2015-06-28")
        self.assertEqual(inst.occurredPeriod.start.date, FHIRDate("2015-06-27").date)
        self.assertEqual(inst.occurredPeriod.start.as_json(), "2015-06-27")
        self.assertEqual(inst.policy[0], "http://acme.com/fhir/Consent/25")
        self.assertEqual(inst.reason[0].coding[0].code, "3457005")
        self.assertEqual(inst.reason[0].coding[0].display, "Referral")
        self.assertEqual(inst.reason[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.recorded.date, FHIRDate("2015-06-27T08:39:24+10:00").date)
        self.assertEqual(inst.recorded.as_json(), "2015-06-27T08:39:24+10:00")
        self.assertEqual(inst.text.status, "generated")

