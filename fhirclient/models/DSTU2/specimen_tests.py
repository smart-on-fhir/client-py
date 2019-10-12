#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-10-12.
#  2019, SMART Health IT.

from __future__ import unicode_literals
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
        inst = self.instantiate_from("specimen-example-isolate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen1(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen1(inst2)
    
    def implSpecimen1(self, inst):
        self.assertEqual(inst.accessionIdentifier.system, "http://lab.acme.org/specimens/2011")
        self.assertEqual(inst.accessionIdentifier.value, "X352356-ISO1")
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2015-08-16T07:03:00Z").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2015-08-16T07:03:00Z")
        self.assertEqual(inst.collection.method.coding[0].code, "BAP")
        self.assertEqual(inst.collection.method.coding[0].system, "http://hl7.org/fhir/v2/0488")
        self.assertEqual(inst.contained[0].id, "stool")
        self.assertEqual(inst.id, "isolate")
        self.assertEqual(inst.receivedTime.date, FHIRDate("2015-08-18T07:03:00Z").date)
        self.assertEqual(inst.receivedTime.as_json(), "2015-08-18T07:03:00Z")
        self.assertEqual(inst.status, "available")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "429951000124103")
        self.assertEqual(inst.type.coding[0].display, "Bacterial isolate specimen")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testSpecimen2(self):
        inst = self.instantiate_from("specimen-example-urine.json")
        self.assertIsNotNone(inst, "Must have instantiated a Specimen instance")
        self.implSpecimen2(inst)
        
        js = inst.as_json()
        self.assertEqual("Specimen", js["resourceType"])
        inst2 = specimen.Specimen(js)
        self.implSpecimen2(inst2)
    
    def implSpecimen2(self, inst):
        self.assertEqual(inst.accessionIdentifier.system, "http://lab.acme.org/specimens/2015")
        self.assertEqual(inst.accessionIdentifier.value, "X352356")
        self.assertEqual(inst.collection.collectedDateTime.date, FHIRDate("2015-08-18T07:03:00Z").date)
        self.assertEqual(inst.collection.collectedDateTime.as_json(), "2015-08-18T07:03:00Z")
        self.assertEqual(inst.container[0].capacity.unit, "mls")
        self.assertEqual(inst.container[0].capacity.value, 50)
        self.assertEqual(inst.container[0].specimenQuantity.unit, "mls")
        self.assertEqual(inst.container[0].specimenQuantity.value, 10)
        self.assertEqual(inst.container[0].type.text, "Non-sterile specimen container")
        self.assertEqual(inst.id, "vma-urine")
        self.assertEqual(inst.receivedTime.date, FHIRDate("2015-08-18T07:03:00Z").date)
        self.assertEqual(inst.receivedTime.as_json(), "2015-08-18T07:03:00Z")
        self.assertEqual(inst.status, "available")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.treatment[0].description, "Acidify to pH < 3.0 with 6 N HCl.")
        self.assertEqual(inst.treatment[0].procedure.coding[0].code, "ACID")
        self.assertEqual(inst.treatment[0].procedure.coding[0].system, "http://hl7.org/fhir/v2/0373")
        self.assertEqual(inst.type.coding[0].code, "RANDU")
        self.assertEqual(inst.type.coding[0].display, "Urine, Random")
        self.assertEqual(inst.type.coding[0].system, "http://hl7.org/fhir/v2/0487")
    
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
        self.assertEqual(inst.collection.comment[0], "Specimen is grossly lipemic")
        self.assertEqual(inst.collection.method.coding[0].code, "LNV")
        self.assertEqual(inst.collection.method.coding[0].system, "http://hl7.org/fhir/v2/0488")
        self.assertEqual(inst.collection.quantity.unit, "mL")
        self.assertEqual(inst.collection.quantity.value, 6)
        self.assertEqual(inst.contained[0].id, "hep")
        self.assertEqual(inst.container[0].capacity.unit, "mL")
        self.assertEqual(inst.container[0].capacity.value, 10)
        self.assertEqual(inst.container[0].description, "Green Gel tube")
        self.assertEqual(inst.container[0].identifier[0].value, "48736-15394-75465")
        self.assertEqual(inst.container[0].specimenQuantity.unit, "mL")
        self.assertEqual(inst.container[0].specimenQuantity.value, 6)
        self.assertEqual(inst.container[0].type.text, "Vacutainer")
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.identifier[0].system, "http://ehr.acme.org/identifiers/collections")
        self.assertEqual(inst.identifier[0].value, "23234352356")
        self.assertEqual(inst.receivedTime.date, FHIRDate("2011-03-04T07:03:00Z").date)
        self.assertEqual(inst.receivedTime.as_json(), "2011-03-04T07:03:00Z")
        self.assertEqual(inst.status, "available")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "122555007")
        self.assertEqual(inst.type.coding[0].display, "Venous blood specimen")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")

