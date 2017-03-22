#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import immunization
from .fhirdate import FHIRDate


class ImmunizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Immunization", js["resourceType"])
        return immunization.Immunization(js)
    
    def testImmunization1(self):
        inst = self.instantiate_from("immunization-example-historical.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization1(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization1(inst2)
    
    def implImmunization1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-01-15").date)
        self.assertEqual(inst.date.as_json(), "2012-01-15")
        self.assertEqual(inst.id, "historical")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234")
        self.assertFalse(inst.notGiven)
        self.assertEqual(inst.note[0].text, "Notes on adminstration of a historical vaccine")
        self.assertFalse(inst.primarySource)
        self.assertEqual(inst.reportOrigin.coding[0].code, "record")
        self.assertEqual(inst.reportOrigin.coding[0].system, "http://hl7.org/fhir/immunization-origin")
        self.assertEqual(inst.reportOrigin.text, "Written Record")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.vaccineCode.coding[0].code, "GNFLU")
        self.assertEqual(inst.vaccineCode.coding[0].system, "urn:oid:1.2.36.1.2001.1005.17")
        self.assertEqual(inst.vaccineCode.text, "Influenza")
    
    def testImmunization2(self):
        inst = self.instantiate_from("immunization-example-refused.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization2(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization2(inst2)
    
    def implImmunization2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(inst.explanation.reasonNotGiven[0].coding[0].code, "MEDPREC")
        self.assertEqual(inst.explanation.reasonNotGiven[0].coding[0].display, "medical precaution")
        self.assertEqual(inst.explanation.reasonNotGiven[0].coding[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.id, "notGiven")
        self.assertTrue(inst.notGiven)
        self.assertTrue(inst.primarySource)
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.vaccineCode.coding[0].code, "01")
        self.assertEqual(inst.vaccineCode.coding[0].display, "DTP")
        self.assertEqual(inst.vaccineCode.coding[0].system, "http://hl7.org/fhir/sid/cvx")
    
    def testImmunization3(self):
        inst = self.instantiate_from("immunization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Immunization instance")
        self.implImmunization3(inst)
        
        js = inst.as_json()
        self.assertEqual("Immunization", js["resourceType"])
        inst2 = immunization.Immunization(js)
        self.implImmunization3(inst2)
    
    def implImmunization3(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.date.as_json(), "2013-01-10")
        self.assertEqual(inst.doseQuantity.code, "mg")
        self.assertEqual(inst.doseQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.doseQuantity.value, 5)
        self.assertEqual(inst.expirationDate.date, FHIRDate("2015-02-15").date)
        self.assertEqual(inst.expirationDate.as_json(), "2015-02-15")
        self.assertEqual(inst.explanation.reason[0].coding[0].code, "429060002")
        self.assertEqual(inst.explanation.reason[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234")
        self.assertEqual(inst.lotNumber, "AAJN11K")
        self.assertFalse(inst.notGiven)
        self.assertEqual(inst.note[0].text, "Notes on adminstration of vaccine")
        self.assertEqual(inst.practitioner[0].role.coding[0].code, "OP")
        self.assertEqual(inst.practitioner[0].role.coding[0].system, "http://hl7.org/fhir/v2/0443")
        self.assertEqual(inst.practitioner[1].role.coding[0].code, "AP")
        self.assertEqual(inst.practitioner[1].role.coding[0].system, "http://hl7.org/fhir/v2/0443")
        self.assertTrue(inst.primarySource)
        self.assertEqual(inst.reaction[0].date.date, FHIRDate("2013-01-10").date)
        self.assertEqual(inst.reaction[0].date.as_json(), "2013-01-10")
        self.assertTrue(inst.reaction[0].reported)
        self.assertEqual(inst.route.coding[0].code, "IM")
        self.assertEqual(inst.route.coding[0].display, "Injection, intramuscular")
        self.assertEqual(inst.route.coding[0].system, "http://hl7.org/fhir/v3/RouteOfAdministration")
        self.assertEqual(inst.site.coding[0].code, "LA")
        self.assertEqual(inst.site.coding[0].display, "left arm")
        self.assertEqual(inst.site.coding[0].system, "http://hl7.org/fhir/v3/ActSite")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.vaccinationProtocol[0].description, "Vaccination Protocol Sequence 1")
        self.assertEqual(inst.vaccinationProtocol[0].doseSequence, 1)
        self.assertEqual(inst.vaccinationProtocol[0].doseStatus.coding[0].code, "count")
        self.assertEqual(inst.vaccinationProtocol[0].doseStatus.coding[0].display, "Counts")
        self.assertEqual(inst.vaccinationProtocol[0].doseStatus.coding[0].system, "http://hl7.org/fhir/vaccination-protocol-dose-status")
        self.assertEqual(inst.vaccinationProtocol[0].doseStatusReason.coding[0].code, "coldchbrk")
        self.assertEqual(inst.vaccinationProtocol[0].doseStatusReason.coding[0].display, "Cold chain break")
        self.assertEqual(inst.vaccinationProtocol[0].doseStatusReason.coding[0].system, "http://hl7.org/fhir/vaccination-protocol-dose-status-reason")
        self.assertEqual(inst.vaccinationProtocol[0].series, "Vaccination Series 1")
        self.assertEqual(inst.vaccinationProtocol[0].seriesDoses, 2)
        self.assertEqual(inst.vaccinationProtocol[0].targetDisease[0].coding[0].code, "1857005")
        self.assertEqual(inst.vaccinationProtocol[0].targetDisease[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.vaccineCode.coding[0].code, "FLUVAX")
        self.assertEqual(inst.vaccineCode.coding[0].system, "urn:oid:1.2.36.1.2001.1005.17")
        self.assertEqual(inst.vaccineCode.text, "Fluvax (Influenza)")

