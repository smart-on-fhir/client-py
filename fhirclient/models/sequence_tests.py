#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10210 on 2016-11-17.
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
        self.assertEqual(inst.coordinateSystem, 0)
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].code, "NC_000007.14")
        self.assertEqual(inst.referenceSeq.referenceSeqId.coding[0].system, "http://www.ncbi.nlm.nih.gov/nuccore")
        self.assertEqual(inst.referenceSeq.strand, 1)
        self.assertEqual(inst.referenceSeq.windowEnd, 55227980)
        self.assertEqual(inst.referenceSeq.windowStart, 55227970)
        self.assertEqual(inst.repository[0].name, "ga4gh")
        self.assertEqual(inst.repository[0].url, "https://www.googleapis.com/genomics/v1beta2")
        self.assertEqual(inst.repository[0].variantId, "A1A2")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "DNA")
        self.assertEqual(inst.variant[0].end, 55227977)
        self.assertEqual(inst.variant[0].observedAllele, "T")
        self.assertEqual(inst.variant[0].referenceAllele, "A")
        self.assertEqual(inst.variant[0].start, 55227976)

