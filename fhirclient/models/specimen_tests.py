#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import specimen
from .fhirdate import FHIRDate


class SpecimenTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Specimen", js["resourceType"])
        return specimen.Specimen(js)
    
    def testSpecimen1(self):
        inst = self.instantiate_from("spec-uslab-example1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen1(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen1(inst2)
    
    def implSpecimen1(self, inst):
        self.assertEqual(inst.accessionIdentifier.system, "http://lis.acmelabs.org/identifiers/accession")
        self.assertEqual(inst.accessionIdentifier.use, "official")
        self.assertEqual(inst.accessionIdentifier.value, "21041205000001")
        self.assertEqual(inst.collection.bodySiteCodeableConcept.coding[0].code, " 53120007")
        self.assertEqual(inst.collection.bodySiteCodeableConcept.coding[0].display, "Arm")
        self.assertEqual(inst.collection.bodySiteCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.collection.bodySiteCodeableConcept.coding[1].code, "ARM")
        self.assertEqual(inst.collection.bodySiteCodeableConcept.coding[1].display, "Arm")
        self.assertEqual(inst.collection.bodySiteCodeableConcept.coding[1].system, "http://ehr.goodhealthclinic.org")
        self.assertEqual(inst.collection.bodySiteCodeableConcept.text, "Drawn from Arm")
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2014-12-05").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2014-12-05")
        self.assertEqual(inst.id, "uslab-example1")
        self.assertEqual(inst.identifier[0].system, "http://ehr.goodhealthclinic.org/identifiers/specimen")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "SID123")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "122555007")
        self.assertEqual(inst.type.coding[0].display, "Venous blood specimen")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.coding[1].code, "BLD")
        self.assertEqual(inst.type.coding[1].display, "Blood")
        self.assertEqual(inst.type.coding[1].system, "http://ehr.goodhealthclinic.org")
        self.assertEqual(inst.type.text, "Blood sample")
    
    def testSpecimen2(self):
        inst = self.instantiate_from("spec-uslab-example2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen2(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen2(inst2)
    
    def implSpecimen2(self, inst):
        self.assertEqual(inst.accessionIdentifier.system, "http://lis.acmelabs.org/identifiers/accession")
        self.assertEqual(inst.accessionIdentifier.use, "official")
        self.assertEqual(inst.accessionIdentifier.value, "21041205000001")
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2014-12-05").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2014-12-05")
        self.assertEqual(inst.id, "uslab-example2")
        self.assertEqual(inst.identifier[0].system, "http://ehr.goodhealthclinic.org/identifiers/specimen")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "SID456")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "698276005")
        self.assertEqual(inst.type.coding[0].display, "First stream urine sample")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.coding[1].code, "UFV")
        self.assertEqual(inst.type.coding[1].display, "Urine, First Void")
        self.assertEqual(inst.type.coding[1].system, "http://ehr.goodhealthclinic.org")
        self.assertEqual(inst.type.text, "Urine, First Void")
    
    def testSpecimen3(self):
        inst = self.instantiate_from("specimen-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen3(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen3(inst2)
    
    def implSpecimen3(self, inst):
        self.assertEqual(inst.accessionIdentifier.system, "http://lab.acme.org/specimens/2011")
        self.assertEqual(inst.accessionIdentifier.value, "X352356")
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2011-05-30T06:15:00Z").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2011-05-30T06:15:00Z")
        self.assertEqual(inst.collection.method.coding[0].code, "LNV")
        self.assertEqual(inst.collection.method.coding[0].system, "http://hl7.org/fhir/v2/0488")
        self.assertEqual(inst.collection.quantity.units, "mL")
        self.assertEqual(inst.collection.quantity.value, 6)
        self.assertEqual(inst.container[0].capacity.units, "mL")
        self.assertEqual(inst.container[0].capacity.value, 10)
        self.assertEqual(inst.container[0].description, "Green Gel tube")
        self.assertEqual(inst.container[0].identifier[0].value, "48736-15394-75465")
        self.assertEqual(inst.container[0].specimenQuantity.units, "mL")
        self.assertEqual(inst.container[0].specimenQuantity.value, 6)
        self.assertEqual(inst.container[0].type.text, "Vacutainer")
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.identifier[0].system, "http://ehr.acme.org/identifiers/collections")
        self.assertEqual(inst.identifier[0].value, "23234352356")
        self.assertEqual(inst.receivedTime.date, FHIRDate("2011-03-04T07:03:00Z").date)
        self.assertEqual(inst.receivedTime.as_json(), "2011-03-04T07:03:00Z")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "122555007")
        self.assertEqual(inst.type.coding[0].display, "Venous blood specimen")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testSpecimen4(self):
        inst = self.instantiate_from("specimen-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen4(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen4(inst2)
    
    def implSpecimen4(self, inst):
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2011-03-06T06:15:00Z").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2011-03-06T06:15:00Z")
        self.assertEqual(inst.collection.extension[0].url, "http://hl7.org/fhir/StructureDefinition/specimen-collectionPriority")
        self.assertEqual(inst.collection.extension[0].valueCodeableConcept.coding[0].code, "5")
        self.assertEqual(inst.collection.extension[0].valueCodeableConcept.coding[0].display, "ROUTINE")
        self.assertEqual(inst.collection.extension[0].valueCodeableConcept.coding[0].system, "http://hl7.org/fhir/vs/specimen-collection-priority")
        self.assertEqual(inst.collection.extension[1].url, "http://hl7.org/fhir/StructureDefinition/specimen-specialHandling")
        self.assertEqual(inst.collection.extension[1].valueCodeableConcept.coding[0].code, "NOPERSISTP")
        self.assertEqual(inst.collection.extension[1].valueCodeableConcept.coding[0].display, "no collection beyond purpose of use")
        self.assertEqual(inst.collection.extension[1].valueCodeableConcept.coding[0].system, "http://hl7.org/fhir/v3/ActCode")
        self.assertEqual(inst.collection.quantity.extension[0].url, "http://hl7.org/fhir/StructureDefinition/specimen-isDryWeight")
        self.assertFalse(inst.collection.quantity.extension[0].valueBoolean)
        self.assertEqual(inst.collection.quantity.units, "mL")
        self.assertEqual(inst.collection.quantity.value, 6)
        self.assertEqual(inst.container[0].capacity.units, "mL")
        self.assertEqual(inst.container[0].capacity.value, 10)
        self.assertEqual(inst.container[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/specimen-sequenceNumber")
        self.assertEqual(inst.container[0].extension[0].valueInteger, 1)
        self.assertEqual(inst.container[0].type.coding[0].code, "434746001")
        self.assertEqual(inst.container[0].type.coding[0].display, "Specimen vial")
        self.assertEqual(inst.container[0].type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.receivedTime.date, FHIRDate("2011-03-04T07:03:00Z").date)
        self.assertEqual(inst.receivedTime.as_json(), "2011-03-04T07:03:00Z")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.treatment[0].description, "Treated with anticoagulants.")
        self.assertEqual(inst.treatment[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/specimen-treatmentTime")
        self.assertEqual(inst.treatment[0].extension[0].valuePeriod.end.date, FHIRDate("2011-03-04T07:03:00Z").date)
        self.assertEqual(inst.treatment[0].extension[0].valuePeriod.end.as_json(), "2011-03-04T07:03:00Z")
        self.assertEqual(inst.treatment[0].extension[0].valuePeriod.start.date, FHIRDate("2011-03-04T07:03:00Z").date)
        self.assertEqual(inst.treatment[0].extension[0].valuePeriod.start.as_json(), "2011-03-04T07:03:00Z")
        self.assertEqual(inst.type.coding[0].code, "122555007")
        self.assertEqual(inst.type.coding[0].display, "Venous blood specimen")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")

