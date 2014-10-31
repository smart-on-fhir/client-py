#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from relatedperson import RelatedPerson
from fhirdate import FHIRDate


class RelatedPersonTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = RelatedPerson(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testRelatedPerson1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/relatedperson-example-f001-sarah.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
    
        self.assertEqual(inst.gender.coding[0].code, "F")
        self.assertEqual(inst.gender.coding[0].display, "Female")
        self.assertEqual(inst.gender.coding[0].system, "http://hl7.org/fhir/v3/AdministrativeGender")
        self.assertEqual(inst.identifier[0].label, "BSN")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.name.family[0], "Abels")
        self.assertEqual(inst.name.given[0], "Sarah")
        self.assertEqual(inst.name.use, "usual")
        self.assertEqual(inst.patient.reference, "Patient/f001")
        self.assertEqual(inst.relationship.coding[0].code, "SIGOTHR")
        self.assertEqual(inst.relationship.coding[0].system, "http://hl7.org/fhir/v3/RoleCode")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "mobile")
        self.assertEqual(inst.telecom[0].value, "0690383372")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "home")
        self.assertEqual(inst.telecom[1].value, "s.abels@kpn.nl")
        self.assertEqual(inst.text.div, "<div>\n     Sarah Abels\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testRelatedPerson2(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/relatedperson-example-f002-ariadne.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
    
        self.assertEqual(inst.gender.coding[0].code, "F")
        self.assertEqual(inst.gender.coding[0].display, "Female")
        self.assertEqual(inst.gender.coding[0].system, "http://hl7.org/fhir/v3/AdministrativeGender")
        self.assertEqual(inst.name.text, "Ariadne Bor-Jansma")
        self.assertEqual(inst.name.use, "usual")
        self.assertEqual(inst.patient.reference, "Patient/f201")
        self.assertEqual(inst.relationship.coding[0].code, "SIGOTHR")
        self.assertEqual(inst.relationship.coding[0].system, "http://hl7.org/fhir/v3/RoleCode")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "home")
        self.assertEqual(inst.telecom[0].value, "+31201234567")
        self.assertEqual(inst.text.div, "<div>\n     Ariadne Bor-Jansma\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testRelatedPerson3(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/relatedperson-example-peter.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
    
        self.assertEqual(inst.address.city, "PleasantVille")
        self.assertEqual(inst.address.line[0], "534 Erewhon St")
        self.assertEqual(inst.address.state, "Vic")
        self.assertEqual(inst.address.use, "home")
        self.assertEqual(inst.address.zip, "3999")
        self.assertEqual(inst.gender.coding[0].code, "M")
        self.assertEqual(inst.gender.coding[0].display, "Male")
        self.assertEqual(inst.gender.coding[0].system, "http://hl7.org/fhir/v3/AdministrativeGender")
        self.assertEqual(inst.name.family[0], "Chalmers")
        self.assertEqual(inst.name.given[0], "Peter")
        self.assertEqual(inst.name.given[1], "James")
        self.assertEqual(inst.name.use, "official")
        self.assertEqual(inst.patient.reference, "Patient/animal")
        self.assertEqual(inst.photo[0].contentType, "image/jpeg")
        self.assertEqual(inst.photo[0].url, "binary/@f012")
        self.assertEqual(inst.relationship.coding[0].code, "owner")
        self.assertEqual(inst.relationship.coding[0].system, "http://hl7.org/fhir/patient-contact-relationship")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "(03) 5555 6473")
        self.assertEqual(inst.text.div, "<div>\n      <table>\n        <tbody>\n          <tr>\n            <td>Name</td>\n            <td>Peter Chalmers</td>\n          </tr>\n          <tr>\n            <td>Address</td>\n            <td>534 Erewhon, Pleasantville, Vic, 3999</td>\n          </tr>\n          <tr>\n            <td>Contacts</td>\n            <td>Work: (03) 5555 6473</td>\n          </tr>\n        </tbody>\n      </table>\n    </div>")
        self.assertEqual(inst.text.status, "generated")

