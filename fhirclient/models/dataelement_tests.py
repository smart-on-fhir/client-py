#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import dataelement
from .fhirdate import FHIRDate


class DataElementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DataElement", js["resourceType"])
        return dataelement.DataElement(js)
    
    def testDataElement1(self):
        inst = self.instantiate_from("dataelement-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DataElement instance")
        self.implDataElement1(inst)
        
        js = inst.as_json()
        self.assertEqual("DataElement", js["resourceType"])
        inst2 = dataelement.DataElement(js)
        self.implDataElement1(inst2)
    
    def implDataElement1(self, inst):
        self.assertEqual(inst.contained[0].id, "2179414")
        self.assertEqual(inst.contained[1].id, "2179414-permitted")
        self.assertEqual(inst.contained[2].id, "2179414-cm")
        self.assertEqual(inst.date.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.date.as_json(), "2016-01-01")
        self.assertEqual(inst.element[0].binding.strength, "required")
        self.assertEqual(inst.element[0].code[0].code, "46098-0")
        self.assertEqual(inst.element[0].code[0].display, "Sex")
        self.assertEqual(inst.element[0].code[0].system, "http://loinc.org")
        self.assertEqual(inst.element[0].definition, "The code representing the gender of a person.")
        self.assertEqual(inst.element[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/minLength")
        self.assertEqual(inst.element[0].extension[0].valueInteger, 1)
        self.assertEqual(inst.element[0].extension[1].url, "http://hl7.org/fhir/StructureDefinition/elementdefinition-question")
        self.assertEqual(inst.element[0].extension[1].valueString, "Gender")
        self.assertEqual(inst.element[0].mapping[0].identity, "fhir")
        self.assertEqual(inst.element[0].mapping[0].language, "application/xquery")
        self.assertEqual(inst.element[0].mapping[0].map, "return f:/Patient/f:gender")
        self.assertEqual(inst.element[0].maxLength, 13)
        self.assertEqual(inst.element[0].path, "Gender")
        self.assertEqual(inst.element[0].type[0].code, "CodeableConcept")
        self.assertEqual(inst.id, "gender")
        self.assertEqual(inst.identifier[0].value, "2179650")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.mapping[0].identity, "fhir")
        self.assertEqual(inst.mapping[0].name, "Fast Healthcare Interoperable Resources (FHIR)")
        self.assertEqual(inst.mapping[0].uri, "http://hl7.org/fhir/api")
        self.assertEqual(inst.name, "Gender Code")
        self.assertEqual(inst.publisher, "DCP")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Administrative gender")
        self.assertEqual(inst.version, "1.0")
    
    def testDataElement2(self):
        inst = self.instantiate_from("dataelement-labtestmaster-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DataElement instance")
        self.implDataElement2(inst)
        
        js = inst.as_json()
        self.assertEqual("DataElement", js["resourceType"])
        inst2 = dataelement.DataElement(js)
        self.implDataElement2(inst2)
    
    def implDataElement2(self, inst):
        self.assertEqual(inst.element[0].alias[0], "Protime, PT")
        self.assertEqual(inst.element[0].comment, "Used to screen the integrity of the extrinsic and common pathways of coagulation and to monitor warfarin anticoagulation. ")
        self.assertEqual(inst.element[0].definition, "The PT test evaluates the extrinsic and common pathways of the coagulation cascade.")
        self.assertEqual(inst.element[0].example[0].label, "Simple")
        self.assertEqual(inst.element[0].example[0].valueDecimal, 10.0)
        self.assertEqual(inst.element[0].extension[0].url, "http://hl7.org/fhir/StructureDefinition/elementdefinition-allowedUnits")
        self.assertEqual(inst.element[0].extension[0].valueCodeableConcept.coding[0].code, "s")
        self.assertEqual(inst.element[0].extension[0].valueCodeableConcept.coding[0].display, "second")
        self.assertEqual(inst.element[0].extension[0].valueCodeableConcept.coding[0].system, "http://unitsofmeasure.org")
        self.assertTrue(inst.element[0].extension[0].valueCodeableConcept.coding[0].userSelected)
        self.assertEqual(inst.element[0].extension[0].valueCodeableConcept.coding[0].version, "1.9")
        self.assertEqual(inst.element[0].extension[0].valueCodeableConcept.text, "second")
        self.assertEqual(inst.element[0].mapping[0].identity, "loinc")
        self.assertEqual(inst.element[0].mapping[0].map, "5964-2")
        self.assertEqual(inst.element[0].path, "prothrombin")
        self.assertEqual(inst.element[0].requirements, "This test is orderable. A plasma specimen in a 3.2% sodium citrate blue top tube is required.")
        self.assertEqual(inst.element[0].type[0].code, "decimal")
        self.assertEqual(inst.id, "prothrombin")
        self.assertEqual(inst.identifier[0].period.start.date, FHIRDate("2011-05-19").date)
        self.assertEqual(inst.identifier[0].period.start.as_json(), "2011-05-19")
        self.assertEqual(inst.identifier[0].system, "http://www.CenturyHospital/Laboratory/DirectoryofServices")
        self.assertEqual(inst.identifier[0].type.text, "Prothrombin Time, PT")
        self.assertEqual(inst.identifier[0].value, "11")
        self.assertEqual(inst.mapping[0].comment, "Version 2.48 or later")
        self.assertEqual(inst.mapping[0].identity, "loinc")
        self.assertEqual(inst.mapping[0].name, "LOINC")
        self.assertEqual(inst.mapping[0].uri, "http://loinc.org/")
        self.assertEqual(inst.name, "Prothrombin Time")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

