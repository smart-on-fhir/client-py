#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import list
from .fhirdate import FHIRDate


class ListTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("List", js["resourceType"])
        return list.List(js)
    
    def testList1(self):
        inst = self.instantiate_from("list-example-allergies.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList1(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList1(inst2)
    
    def implList1(self, inst):
        self.assertEqual(inst.code.coding[0].code, "52472-8")
        self.assertEqual(inst.code.coding[0].display, "Allergies and Adverse Drug Reactions")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Current Allergy List")
        self.assertEqual(inst.date.date, FHIRDate("2015-07-14T23:10:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2015-07-14T23:10:23+11:00")
        self.assertEqual(inst.id, "current-allergies")
        self.assertEqual(inst.mode, "working")
        self.assertEqual(inst.orderedBy.coding[0].code, "entry-date")
        self.assertEqual(inst.orderedBy.coding[0].system, "http://hl7.org/fhir/list-order")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Current Allergy List")
    
    def testList2(self):
        inst = self.instantiate_from("list-example-double-cousin-relationship-pedigree.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList2(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList2(inst2)
    
    def implList2(self, inst):
        self.assertEqual(inst.code.coding[0].code, "80738-8")
        self.assertEqual(inst.code.coding[0].display, "TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal")
        self.assertEqual(inst.contained[0].id, "1")
        self.assertEqual(inst.contained[1].id, "2")
        self.assertEqual(inst.contained[2].id, "3")
        self.assertEqual(inst.contained[3].id, "4")
        self.assertEqual(inst.contained[4].id, "5")
        self.assertEqual(inst.contained[5].id, "6")
        self.assertEqual(inst.id, "example-double-cousin-relationship")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList3(self):
        inst = self.instantiate_from("list-example-empty.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList3(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList3(inst2)
    
    def implList3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "182836005")
        self.assertEqual(inst.code.coding[0].display, "Review of medication")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Medication Review")
        self.assertEqual(inst.date.date, FHIRDate("2012-11-26T07:30:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-11-26T07:30:23+11:00")
        self.assertEqual(inst.emptyReason.coding[0].code, "nilknown")
        self.assertEqual(inst.emptyReason.coding[0].display, "Nil Known")
        self.assertEqual(inst.emptyReason.coding[0].system, "http://hl7.org/fhir/list-empty-reason")
        self.assertEqual(inst.emptyReason.text, "The patient is not on any medications")
        self.assertEqual(inst.id, "example-empty")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList4(self):
        inst = self.instantiate_from("list-example-familyhistory-f201-roel.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList4(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList4(inst2)
    
    def implList4(self, inst):
        self.assertEqual(inst.code.coding[0].code, "8670-2")
        self.assertEqual(inst.code.coding[0].display, "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.contained[0].id, "fmh-1")
        self.assertEqual(inst.contained[1].id, "fmh-2")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.note[0].text, "Both parents, both brothers and both children (twin) are still alive.")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList5(self):
        inst = self.instantiate_from("list-example-familyhistory-genetics-profile-annie.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList5(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList5(inst2)
    
    def implList5(self, inst):
        self.assertEqual(inst.code.coding[0].code, "8670-2")
        self.assertEqual(inst.code.coding[0].display, "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.contained[0].id, "image")
        self.assertEqual(inst.contained[1].id, "1")
        self.assertEqual(inst.contained[2].id, "2")
        self.assertEqual(inst.contained[3].id, "3")
        self.assertEqual(inst.contained[4].id, "4")
        self.assertEqual(inst.contained[5].id, "5")
        self.assertEqual(inst.contained[6].id, "6")
        self.assertEqual(inst.contained[7].id, "7")
        self.assertEqual(inst.contained[8].id, "8")
        self.assertEqual(inst.contained[9].id, "9")
        self.assertEqual(inst.id, "prognosis")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList6(self):
        inst = self.instantiate_from("list-example-familyhistory-genetics-profile.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList6(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList6(inst2)
    
    def implList6(self, inst):
        self.assertEqual(inst.code.coding[0].code, "8670-2")
        self.assertEqual(inst.code.coding[0].display, "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.contained[0].id, "1")
        self.assertEqual(inst.contained[1].id, "2")
        self.assertEqual(inst.contained[2].id, "3")
        self.assertEqual(inst.contained[3].id, "4")
        self.assertEqual(inst.contained[4].id, "5")
        self.assertEqual(inst.contained[5].id, "6")
        self.assertEqual(inst.contained[6].id, "7")
        self.assertEqual(inst.contained[7].id, "8")
        self.assertEqual(inst.id, "genetic")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList7(self):
        inst = self.instantiate_from("list-example-medlist.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList7(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList7(inst2)
    
    def implList7(self, inst):
        self.assertEqual(inst.code.coding[0].code, "182836005")
        self.assertEqual(inst.code.coding[0].display, "Review of medication")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Medication Review")
        self.assertEqual(inst.date.date, FHIRDate("2013-11-20T23:10:23+11:00").date)
        self.assertEqual(inst.date.as_json(), "2013-11-20T23:10:23+11:00")
        self.assertEqual(inst.entry[0].flag.coding[0].code, "01")
        self.assertEqual(inst.entry[0].flag.coding[0].display, "Prescribed")
        self.assertEqual(inst.entry[0].flag.coding[0].system, "http://nehta.gov.au/codes/medications/changetype")
        self.assertTrue(inst.entry[1].deleted)
        self.assertEqual(inst.entry[1].flag.coding[0].code, "02")
        self.assertEqual(inst.entry[1].flag.coding[0].display, "Cancelled")
        self.assertEqual(inst.entry[1].flag.coding[0].system, "http://nehta.gov.au/codes/medications/changetype")
        self.assertEqual(inst.id, "med-list")
        self.assertEqual(inst.mode, "changes")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList8(self):
        inst = self.instantiate_from("list-example-simple-empty.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList8(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList8(inst2)
    
    def implList8(self, inst):
        self.assertEqual(inst.code.coding[0].code, "346638")
        self.assertEqual(inst.code.coding[0].display, "Patient Admission List")
        self.assertEqual(inst.code.coding[0].system, "http://acme.com/list-codes")
        self.assertEqual(inst.date.date, FHIRDate("2016-07-14T11:54:05+10:00").date)
        self.assertEqual(inst.date.as_json(), "2016-07-14T11:54:05+10:00")
        self.assertEqual(inst.id, "example-simple-empty")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")
    
    def testList9(self):
        inst = self.instantiate_from("list-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
        self.implList9(inst)
        
        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList9(inst2)
    
    def implList9(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-11-25T22:17:00+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-11-25T22:17:00+11:00")
        self.assertTrue(inst.entry[0].deleted)
        self.assertEqual(inst.entry[0].flag.text, "Deleted due to error")
        self.assertEqual(inst.entry[1].date.date, FHIRDate("2012-11-21").date)
        self.assertEqual(inst.entry[1].date.as_json(), "2012-11-21")
        self.assertEqual(inst.entry[1].flag.text, "Added")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:uuid:a9fcea7c-fcdf-4d17-a5e0-f26dda030b59")
        self.assertEqual(inst.identifier[0].value, "23974652")
        self.assertEqual(inst.mode, "changes")
        self.assertEqual(inst.status, "current")
        self.assertEqual(inst.text.status, "generated")

