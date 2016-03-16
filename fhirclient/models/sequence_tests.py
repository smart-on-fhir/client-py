#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 on 2016-03-16.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import sequence
from .fhirdate import FHIRDate


class SequenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Sequence", js["resourceType"])
        return sequence.Sequence(js)
    
    def testSequence1(self):
        inst = self.instantiate_from("sequence-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence1(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence1(inst2)
    
    def implSequence1(self, inst):
        self.assertEqual(inst.coordinate[0].chromosome.coding[0].code, "7")
        self.assertEqual(inst.coordinate[0].end, 55227977)
        self.assertEqual(inst.coordinate[0].genomeBuild, "GRCh37")
        self.assertEqual(inst.coordinate[0].start, 55227976)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.observedAllele, "T")
        self.assertEqual(inst.referenceAllele, "A")
        self.assertEqual(inst.referenceSeq.coding[0].code, "ENSESTT00000085772.1")
        self.assertEqual(inst.referenceSeq.coding[0].system, "http://www.ensembl.org")
        self.assertEqual(inst.referenceSeq.text, "ENSESTT00000085772.1")
        self.assertEqual(inst.repository[0].name, "ga4gh")
        self.assertEqual(inst.repository[0].readGroupSetId, "B1B2")
        self.assertEqual(inst.repository[0].url, "https://www.googleapis.com/genomics/v1beta2")
        self.assertEqual(inst.repository[0].variantId, "A1A2")
        self.assertEqual(inst.species.coding[0].code, "337915000")
        self.assertEqual(inst.species.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.species.text, "Homo sapiens")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variationID[0].coding[0].code, "587778247")
        self.assertEqual(inst.variationID[0].coding[0].system, "http://www.ncbi.nlm.nih.gov/projects/SNP")
        self.assertEqual(inst.variationID[0].text, "rs587778247")
    
    def testSequence2(self):
        inst = self.instantiate_from("sequence-genetics-example2-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence2(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence2(inst2)
    
    def implSequence2(self, inst):
        self.assertEqual(inst.id, "seq2-1")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variationID[0].coding[0].code, "58238559")
        self.assertEqual(inst.variationID[0].coding[0].system, "http://www.ncbi.nlm.nih.gov/projects/SNP")
        self.assertEqual(inst.variationID[0].text, "rs58238559")
    
    def testSequence3(self):
        inst = self.instantiate_from("sequence-genetics-example2-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence3(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence3(inst2)
    
    def implSequence3(self, inst):
        self.assertEqual(inst.id, "seq2-2")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variationID[0].coding[0].code, "58238560")
        self.assertEqual(inst.variationID[0].coding[0].system, "http://www.ncbi.nlm.nih.gov/projects/SNP")
        self.assertEqual(inst.variationID[0].text, "rs58238560")
    
    def testSequence4(self):
        inst = self.instantiate_from("sequence-genetics-example2-3.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence4(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence4(inst2)
    
    def implSequence4(self, inst):
        self.assertEqual(inst.id, "seq2-3")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variationID[0].coding[0].code, "58238562")
        self.assertEqual(inst.variationID[0].coding[0].system, "http://www.ncbi.nlm.nih.gov/projects/SNP")
        self.assertEqual(inst.variationID[0].text, "rs58238562")
    
    def testSequence5(self):
        inst = self.instantiate_from("sequence-genetics-example2-4.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence5(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence5(inst2)
    
    def implSequence5(self, inst):
        self.assertEqual(inst.id, "seq2-4")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variationID[0].coding[0].code, "58238565")
        self.assertEqual(inst.variationID[0].coding[0].system, "http://www.ncbi.nlm.nih.gov/projects/SNP")
        self.assertEqual(inst.variationID[0].text, "rs58238565")
    
    def testSequence6(self):
        inst = self.instantiate_from("sequence-genetics-example3.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence6(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence6(inst2)
    
    def implSequence6(self, inst):
        self.assertEqual(inst.id, "seq3")
        self.assertEqual(inst.quantity.unit, "Transcripts per million(TPM)")
        self.assertEqual(inst.quantity.value, 23)
        self.assertEqual(inst.referenceSeq.coding[0].code, "NM_000927.4")
        self.assertEqual(inst.referenceSeq.coding[0].display, "Homo sapiens ATP-binding cassette, sub-family B (MDR/TAP), member 1 (ABCB1), mRNA")
        self.assertEqual(inst.referenceSeq.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore/")
        self.assertEqual(inst.species.coding[0].code, "337915000")
        self.assertEqual(inst.species.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.species.text, "Homo sapiens")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "RNA")
        self.assertEqual(inst.variationID[0].coding[0].code, "58238562")
        self.assertEqual(inst.variationID[0].coding[0].system, "http://www.ncbi.nlm.nih.gov/projects/SNP")
        self.assertEqual(inst.variationID[0].text, "rs58238562")
    
    def testSequence7(self):
        inst = self.instantiate_from("sequence-genetics-example4.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence7(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence7(inst2)
    
    def implSequence7(self, inst):
        self.assertEqual(inst.coordinate[0].chromosome.coding[0].code, "7")
        self.assertEqual(inst.coordinate[0].end, 87642522)
        self.assertEqual(inst.coordinate[0].genomeBuild, "GRCh38")
        self.assertEqual(inst.coordinate[0].start, 87627621)
        self.assertEqual(inst.copyNumberEvent.text, "deletion")
        self.assertEqual(inst.id, "seq4")
        self.assertEqual(inst.referenceSeq.coding[0].code, "NC_000007.14")
        self.assertEqual(inst.referenceSeq.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore/")
        self.assertEqual(inst.referenceSeq.text, "NC_000007.14")
        self.assertEqual(inst.species.coding[0].code, "337915000")
        self.assertEqual(inst.species.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.species.text, "Homo sapiens")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variationID[0].coding[0].code, "essv25820997")
        self.assertEqual(inst.variationID[0].coding[0].system, "http://www.ncbi.nlm.nih.gov/dbvar/")
        self.assertEqual(inst.variationID[0].text, "essv25820997")
    
    def testSequence8(self):
        inst = self.instantiate_from("sequence-genetics-example5.json")
        self.assertIsNotNone(inst, "Must have instantiated a Sequence instance")
        self.implSequence8(inst)
        
        js = inst.as_json()
        self.assertEqual("Sequence", js["resourceType"])
        inst2 = sequence.Sequence(js)
        self.implSequence8(inst2)
    
    def implSequence8(self, inst):
        self.assertEqual(inst.coordinate[0].end, 47)
        self.assertEqual(inst.coordinate[0].start, 46)
        self.assertEqual(inst.id, "seq5")
        self.assertEqual(inst.observedAllele, "L")
        self.assertEqual(inst.referenceAllele, "P")
        self.assertEqual(inst.referenceSeq.coding[0].code, "ENSP00000252486")
        self.assertEqual(inst.referenceSeq.coding[0].system, "http://www.ensembl.org/")
        self.assertEqual(inst.referenceSeq.text, "ENSP00000252486")
        self.assertEqual(inst.species.coding[0].code, "337915000")
        self.assertEqual(inst.species.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.species.text, "Homo sapiens")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "AA")

