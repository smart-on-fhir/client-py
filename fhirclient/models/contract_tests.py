#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11157 on 2017-02-14.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import contract
from .fhirdate import FHIRDate


class ContractTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Contract", js["resourceType"])
        return contract.Contract(js)
    
    def testContract1(self):
        inst = self.instantiate_from("contract-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract1(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract1(inst2)
    
    def implContract1(self, inst):
        self.assertEqual(inst.id, "C-123")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the contract</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testContract2(self):
        inst = self.instantiate_from("pcd-example-notAuthor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract2(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract2(inst2)
    
    def implContract2(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notAuthor")
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].text, "Withhold all data authored by Good Health provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-authored-by")
        self.assertEqual(inst.term[0].type.coding[0].display, "Withhold all data authored by specified actor entity.")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://hl7.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract3(self):
        inst = self.instantiate_from("pcd-example-notLabs.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract3(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract3(inst2)
    
    def implContract3(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notLabs")
        self.assertEqual(inst.issued.date, FHIRDate("2014-08-17").date)
        self.assertEqual(inst.issued.as_json(), "2014-08-17")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].subType.coding[0].code, "ProcedureRequest")
        self.assertEqual(inst.term[0].subType.coding[0].system, "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.term[0].text, "Withhold orders from any provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-object-type")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://hl7.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.term[1].subType.coding[0].code, "DiagnosticReport")
        self.assertEqual(inst.term[1].subType.coding[0].system, "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.term[1].text, "Withhold order results from any provider.")
        self.assertEqual(inst.term[1].type.coding[0].code, "withhold-object-type")
        self.assertEqual(inst.term[1].type.coding[0].system, "http://hl7.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract4(self):
        inst = self.instantiate_from("pcd-example-notOrg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract4(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract4(inst2)
    
    def implContract4(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notOrg")
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].text, "Withhold this order and any results or related objects from any provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-from")
        self.assertEqual(inst.term[0].type.coding[0].display, "Withhold all data from specified actor entity.")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://hl7.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract5(self):
        inst = self.instantiate_from("pcd-example-notThem.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract5(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract5(inst2)
    
    def implContract5(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notThem")
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].text, "Withhold this order and any results or related objects from specified nurse provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-from")
        self.assertEqual(inst.term[0].type.coding[0].display, "Withhold all data from specified actor entity.")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://hl7.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract6(self):
        inst = self.instantiate_from("pcd-example-notThis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract6(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract6(inst2)
    
    def implContract6(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notThis")
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].text, "Withhold this order and any results or related objects from any provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-identified-object-and-related")
        self.assertEqual(inst.term[0].type.coding[0].display, "Withhold the identified object and any other resources that are related to this object.")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://hl7.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")

