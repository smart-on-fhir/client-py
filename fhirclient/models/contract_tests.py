#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
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
        inst = self.instantiate_from("contract-example-42cfr-part2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract1(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract1(inst2)
    
    def implContract1(self, inst):
        self.assertEqual(inst.agent[0].role[0].coding[0].code, "IR")
        self.assertEqual(inst.agent[0].role[0].coding[0].display, "Recipient")
        self.assertEqual(inst.agent[0].role[0].coding[0].system, "http://org.mdhhs.fhir.consent-actor-type")
        self.assertEqual(inst.agent[0].role[0].text, "Recipient of restricted health information")
        self.assertEqual(inst.agent[1].role[0].coding[0].code, "IS")
        self.assertEqual(inst.agent[1].role[0].coding[0].display, "Sender")
        self.assertEqual(inst.agent[1].role[0].coding[0].system, "http://org.mdhhs.fhir.consent-actor-type")
        self.assertEqual(inst.agent[1].role[0].text, "Sender of restricted health information")
        self.assertEqual(inst.id, "C-2121")
        self.assertEqual(inst.issued.date, FHIRDate("2031-11-01T21:18:27-04:00").date)
        self.assertEqual(inst.issued.as_json(), "2031-11-01T21:18:27-04:00")
        self.assertEqual(inst.legal[0].contentAttachment.contentType, "application/pdf")
        self.assertEqual(inst.legal[0].contentAttachment.language, "en-US")
        self.assertEqual(inst.legal[0].contentAttachment.title, "MDHHS-5515 Consent To Share Your Health Information")
        self.assertEqual(inst.legal[0].contentAttachment.url, "http://org.mihin.ecms/ConsentDirective-2121")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRDate("2016-07-19T18:18:42.108-04:00").date)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2016-07-19T18:18:42.108-04:00")
        self.assertEqual(inst.meta.versionId, "1")
        self.assertEqual(inst.securityLabel[0].code, "R")
        self.assertEqual(inst.securityLabel[0].display, "Restricted")
        self.assertEqual(inst.securityLabel[0].system, "http://hl7.org/fhir/v3/Confidentiality")
        self.assertEqual(inst.securityLabel[1].code, "ETH")
        self.assertEqual(inst.securityLabel[1].display, "substance abuse information sensitivity")
        self.assertEqual(inst.securityLabel[1].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.securityLabel[2].code, "42CFRPart2")
        self.assertEqual(inst.securityLabel[2].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.securityLabel[3].code, "TREAT")
        self.assertEqual(inst.securityLabel[3].display, "treatment")
        self.assertEqual(inst.securityLabel[3].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.securityLabel[4].code, "HPAYMT")
        self.assertEqual(inst.securityLabel[4].display, "healthcare payment")
        self.assertEqual(inst.securityLabel[4].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.securityLabel[5].code, "HOPERAT")
        self.assertEqual(inst.securityLabel[5].display, "healthcare operations")
        self.assertEqual(inst.securityLabel[5].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.securityLabel[6].code, "PERSISTLABEL")
        self.assertEqual(inst.securityLabel[6].display, "persist security label")
        self.assertEqual(inst.securityLabel[6].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.securityLabel[7].code, "PRIVMARK")
        self.assertEqual(inst.securityLabel[7].display, "privacy mark")
        self.assertEqual(inst.securityLabel[7].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.securityLabel[8].code, "NORDSCLCD")
        self.assertEqual(inst.securityLabel[8].display, "no redisclosure without consent directive")
        self.assertEqual(inst.securityLabel[8].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.signer[0].signature[0].type[0].code, "1.2.840.10065.1.12.1.1")
        self.assertEqual(inst.signer[0].signature[0].type[0].system, "urn:iso-astm:E1762-95:2013")
        self.assertEqual(inst.signer[0].signature[0].when.date, FHIRDate("2017-02-08T10:57:34+01:00").date)
        self.assertEqual(inst.signer[0].signature[0].when.as_json(), "2017-02-08T10:57:34+01:00")
        self.assertEqual(inst.signer[0].type.code, "SELF")
        self.assertEqual(inst.signer[0].type.system, "http://org.mdhhs.fhir.consent-signer-type")
        self.assertEqual(inst.subType[0].coding[0].code, "MDHHS-5515")
        self.assertEqual(inst.subType[0].coding[0].display, "Michigan MDHHS-5515 Consent to Share Behavioral Health Information for Care Coordination Purposes")
        self.assertEqual(inst.subType[0].coding[0].system, "http://hl7.org/fhir/consentcategorycodes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "OPTIN")
        self.assertEqual(inst.type.coding[0].system, "http://org.mdhhs.fhir.consentdirective-type")
        self.assertEqual(inst.type.text, "Opt-in consent directive")
    
    def testContract2(self):
        inst = self.instantiate_from("contract-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract2(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract2(inst2)
    
    def implContract2(self, inst):
        self.assertEqual(inst.id, "C-123")
        self.assertEqual(inst.identifier.system, "http://happyvalley.com/contract")
        self.assertEqual(inst.identifier.value, "12347")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the contract</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testContract3(self):
        inst = self.instantiate_from("pcd-example-notAuthor.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract3(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract3(inst2)
    
    def implContract3(self, inst):
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
        self.assertEqual(inst.term[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract4(self):
        inst = self.instantiate_from("pcd-example-notLabs.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract4(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract4(inst2)
    
    def implContract4(self, inst):
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
        self.assertEqual(inst.term[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.term[1].subType.coding[0].code, "DiagnosticReport")
        self.assertEqual(inst.term[1].subType.coding[0].system, "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.term[1].text, "Withhold order results from any provider.")
        self.assertEqual(inst.term[1].type.coding[0].code, "withhold-object-type")
        self.assertEqual(inst.term[1].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract5(self):
        inst = self.instantiate_from("pcd-example-notOrg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract5(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract5(inst2)
    
    def implContract5(self, inst):
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
        self.assertEqual(inst.term[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract6(self):
        inst = self.instantiate_from("pcd-example-notThem.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract6(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract6(inst2)
    
    def implContract6(self, inst):
        self.assertEqual(inst.friendly[0].contentAttachment.title, "The terms of the consent in friendly consumer speak.")
        self.assertEqual(inst.id, "pcd-example-notThem")
        self.assertEqual(inst.issued.date, FHIRDate("2015-11-18").date)
        self.assertEqual(inst.issued.as_json(), "2015-11-18")
        self.assertEqual(inst.legal[0].contentAttachment.title, "The terms of the consent in lawyer speak.")
        self.assertEqual(inst.signer[0].signature[0].type[0].code, "1.2.840.10065.1.12.1.1")
        self.assertEqual(inst.signer[0].signature[0].type[0].system, "urn:iso-astm:E1762-95:2013")
        self.assertEqual(inst.signer[0].signature[0].when.date, FHIRDate("2013-06-08T10:57:34-07:00").date)
        self.assertEqual(inst.signer[0].signature[0].when.as_json(), "2013-06-08T10:57:34-07:00")
        self.assertEqual(inst.signer[0].type.code, "COVPTY")
        self.assertEqual(inst.signer[0].type.system, "http://www.hl7.org/fhir/contractsignertypecodes")
        self.assertEqual(inst.subType[0].coding[0].code, "Opt-In")
        self.assertEqual(inst.subType[0].coding[0].display, "Default Authorization with exceptions.")
        self.assertEqual(inst.subType[0].coding[0].system, "http://www.infoway-inforoute.ca.org/Consent-subtype-codes")
        self.assertEqual(inst.term[0].text, "Withhold this order and any results or related objects from specified nurse provider.")
        self.assertEqual(inst.term[0].type.coding[0].code, "withhold-from")
        self.assertEqual(inst.term[0].type.coding[0].display, "Withhold all data from specified actor entity.")
        self.assertEqual(inst.term[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")
    
    def testContract7(self):
        inst = self.instantiate_from("pcd-example-notThis.json")
        self.assertIsNotNone(inst, "Must have instantiated a Contract instance")
        self.implContract7(inst)
        
        js = inst.as_json()
        self.assertEqual("Contract", js["resourceType"])
        inst2 = contract.Contract(js)
        self.implContract7(inst2)
    
    def implContract7(self, inst):
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
        self.assertEqual(inst.term[0].type.coding[0].system, "http://example.org/fhir/consent-term-type-codes")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "57016-8")
        self.assertEqual(inst.type.coding[0].system, "http://loinc.org")

