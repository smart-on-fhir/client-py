#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import organization
from .fhirdate import FHIRDate


class OrganizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Organization", js["resourceType"])
        return organization.Organization(js)
    
    def testOrganization1(self):
        inst = self.instantiate_from("organization-example-f001-burgers.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization1(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization1(inst2)
    
    def implOrganization1(self, inst):
        self.assertEqual(inst.address[0].city, "Den Burg")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "9105 PZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.address[1].city, "Den Burg")
        self.assertEqual(inst.address[1].country, "NLD")
        self.assertEqual(inst.address[1].line[0], "PO Box 2311")
        self.assertEqual(inst.address[1].postalCode, "9100 AA")
        self.assertEqual(inst.address[1].use, "work")
        self.assertEqual(inst.contact[0].purpose.coding[0].code, "PRESS")
        self.assertEqual(inst.contact[0].purpose.coding[0].system, "http://hl7.org/fhir/contactentity-type")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].value, "022-655 2334")
        self.assertEqual(inst.contact[1].purpose.coding[0].code, "PATINF")
        self.assertEqual(inst.contact[1].purpose.coding[0].system, "http://hl7.org/fhir/contactentity-type")
        self.assertEqual(inst.contact[1].telecom[0].system, "phone")
        self.assertEqual(inst.contact[1].telecom[0].value, "022-655 2335")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "91654")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.1")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "17-0112278")
        self.assertEqual(inst.name, "Burgers University Medical Center")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "022-655 2300")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "V6")
        self.assertEqual(inst.type[0].coding[0].display, "University Medical Hospital")
        self.assertEqual(inst.type[0].coding[0].system, "urn:oid:2.16.840.1.113883.2.4.15.1060")
        self.assertEqual(inst.type[0].coding[1].code, "prov")
        self.assertEqual(inst.type[0].coding[1].display, "Healthcare Provider")
        self.assertEqual(inst.type[0].coding[1].system, "http://hl7.org/fhir/organization-type")
    
    def testOrganization2(self):
        inst = self.instantiate_from("organization-example-f002-burgers-card.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization2(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization2(inst2)
    
    def implOrganization2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].line[0], "South Wing, floor 2")
        self.assertEqual(inst.contact[0].address.line[0], "South Wing, floor 2")
        self.assertEqual(inst.contact[0].name.text, "mevr. D. de Haan")
        self.assertEqual(inst.contact[0].purpose.coding[0].code, "ADMIN")
        self.assertEqual(inst.contact[0].purpose.coding[0].system, "http://hl7.org/fhir/contactentity-type")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].value, "022-655 2321")
        self.assertEqual(inst.contact[0].telecom[1].system, "email")
        self.assertEqual(inst.contact[0].telecom[1].value, "cardio@burgersumc.nl")
        self.assertEqual(inst.contact[0].telecom[2].system, "fax")
        self.assertEqual(inst.contact[0].telecom[2].value, "022-655 2322")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.name, "Burgers UMC Cardiology unit")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].value, "022-655 2320")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "dept")
        self.assertEqual(inst.type[0].coding[0].display, "Hospital Department")
        self.assertEqual(inst.type[0].coding[0].system, "http://hl7.org/fhir/organization-type")
    
    def testOrganization3(self):
        inst = self.instantiate_from("organization-example-f003-burgers-ENT.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization3(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization3(inst2)
    
    def implOrganization3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].line[0], "West Wing, floor 5")
        self.assertEqual(inst.contact[0].address.line[0], "West Wing, floor 5")
        self.assertEqual(inst.contact[0].name.text, "mr. F. de Hond")
        self.assertEqual(inst.contact[0].purpose.coding[0].code, "ADMIN")
        self.assertEqual(inst.contact[0].purpose.coding[0].system, "http://hl7.org/fhir/contactentity-type")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].value, "022-655 7654")
        self.assertEqual(inst.contact[0].telecom[1].system, "email")
        self.assertEqual(inst.contact[0].telecom[1].value, "KNO@burgersumc.nl")
        self.assertEqual(inst.contact[0].telecom[2].system, "fax")
        self.assertEqual(inst.contact[0].telecom[2].value, "022-655 0998")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.name, "Burgers UMC Ear,Nose,Throat unit")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].value, "022-655 6780")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "dept")
        self.assertEqual(inst.type[0].coding[0].display, "Hospital Department")
        self.assertEqual(inst.type[0].coding[0].system, "http://hl7.org/fhir/organization-type")
    
    def testOrganization4(self):
        inst = self.instantiate_from("organization-example-f201-aumc.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization4(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization4(inst2)
    
    def implOrganization4(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Den Helder")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Walvisbaai 3")
        self.assertEqual(inst.address[0].postalCode, "2333ZA")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.contact[0].address.city, "Den helder")
        self.assertEqual(inst.contact[0].address.country, "NLD")
        self.assertEqual(inst.contact[0].address.line[0], "Walvisbaai 3")
        self.assertEqual(inst.contact[0].address.line[1], "Gebouw 2")
        self.assertEqual(inst.contact[0].address.postalCode, "2333ZA")
        self.assertEqual(inst.contact[0].name.family, "Brand")
        self.assertEqual(inst.contact[0].name.given[0], "Ronald")
        self.assertEqual(inst.contact[0].name.prefix[0], "Prof.Dr.")
        self.assertEqual(inst.contact[0].name.text, "Professor Brand")
        self.assertEqual(inst.contact[0].name.use, "official")
        self.assertEqual(inst.contact[0].telecom[0].system, "phone")
        self.assertEqual(inst.contact[0].telecom[0].use, "work")
        self.assertEqual(inst.contact[0].telecom[0].value, "+31715269702")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.identifier[0].system, "http://www.zorgkaartnederland.nl/")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "Artis University Medical Center")
        self.assertEqual(inst.name, "Artis University Medical Center (AUMC)")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31715269111")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "405608006")
        self.assertEqual(inst.type[0].coding[0].display, "Academic Medical Center")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type[0].coding[1].code, "V6")
        self.assertEqual(inst.type[0].coding[1].display, "University Medical Hospital")
        self.assertEqual(inst.type[0].coding[1].system, "urn:oid:2.16.840.1.113883.2.4.15.1060")
        self.assertEqual(inst.type[0].coding[2].code, "prov")
        self.assertEqual(inst.type[0].coding[2].display, "Healthcare Provider")
        self.assertEqual(inst.type[0].coding[2].system, "http://hl7.org/fhir/organization-type")
    
    def testOrganization5(self):
        inst = self.instantiate_from("organization-example-f203-bumc.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization5(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization5(inst2)
    
    def implOrganization5(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Blijdorp")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "apenrots 230")
        self.assertEqual(inst.address[0].postalCode, "3056BE")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.identifier[0].system, "http://www.zorgkaartnederland.nl/")
        self.assertEqual(inst.identifier[0].type.text, "Zorginstelling naam")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "Blijdorp MC")
        self.assertEqual(inst.name, "Blijdorp Medisch Centrum (BUMC)")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31107040704")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "405608006")
        self.assertEqual(inst.type[0].coding[0].display, "Academic Medical Center")
        self.assertEqual(inst.type[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type[0].coding[1].code, "prov")
        self.assertEqual(inst.type[0].coding[1].system, "http://hl7.org/fhir/organization-type")
    
    def testOrganization6(self):
        inst = self.instantiate_from("organization-example-gastro.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization6(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization6(inst2)
    
    def implOrganization6(self, inst):
        self.assertEqual(inst.id, "1")
        self.assertEqual(inst.identifier[0].system, "http://www.acme.org.au/units")
        self.assertEqual(inst.identifier[0].value, "Gastro")
        self.assertEqual(inst.name, "Gastroenterology")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "mobile")
        self.assertEqual(inst.telecom[0].value, "+1 555 234 3523")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "gastro@acme.org")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization7(self):
        inst = self.instantiate_from("organization-example-good-health-care.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization7(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization7(inst2)
    
    def implOrganization7(self, inst):
        self.assertEqual(inst.id, "2.16.840.1.113883.19.5")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "2.16.840.1.113883.19.5")
        self.assertEqual(inst.name, "Good Health Clinic")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization8(self):
        inst = self.instantiate_from("organization-example-insurer.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization8(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization8(inst2)
    
    def implOrganization8(self, inst):
        self.assertEqual(inst.alias[0], "ABC Insurance")
        self.assertEqual(inst.id, "2")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.840.1.113883.3.19.2.3")
        self.assertEqual(inst.identifier[0].value, "666666")
        self.assertEqual(inst.name, "XYZ Insurance")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization9(self):
        inst = self.instantiate_from("organization-example-lab.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization9(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization9(inst2)
    
    def implOrganization9(self, inst):
        self.assertEqual(inst.id, "1832473e-2fe0-452d-abe9-3cdb9879522f")
        self.assertEqual(inst.identifier[0].system, "http://www.acme.org.au/units")
        self.assertEqual(inst.identifier[0].value, "ClinLab")
        self.assertEqual(inst.name, "Clinical Lab")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+1 555 234 1234")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "contact@labs.acme.org")
        self.assertEqual(inst.text.status, "generated")
    
    def testOrganization10(self):
        inst = self.instantiate_from("organization-example-mmanu.json")
        self.assertIsNotNone(inst, "Must have instantiated a Organization instance")
        self.implOrganization10(inst)
        
        js = inst.as_json()
        self.assertEqual("Organization", js["resourceType"])
        inst2 = organization.Organization(js)
        self.implOrganization10(inst2)
    
    def implOrganization10(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].country, "Swizterland")
        self.assertEqual(inst.id, "mmanu")
        self.assertEqual(inst.name, "Acme Corporation")
        self.assertEqual(inst.text.status, "generated")

