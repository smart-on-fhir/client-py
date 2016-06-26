#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8595 on 2016-06-26.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import decisionsupportrule
from .fhirdate import FHIRDate


class DecisionSupportRuleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DecisionSupportRule", js["resourceType"])
        return decisionsupportrule.DecisionSupportRule(js)
    
    def testDecisionSupportRule1(self):
        inst = self.instantiate_from("decisionsupportrule-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DecisionSupportRule instance")
        self.implDecisionSupportRule1(inst)
        
        js = inst.as_json()
        self.assertEqual("DecisionSupportRule", js["resourceType"])
        inst2 = decisionsupportrule.DecisionSupportRule(js)
        self.implDecisionSupportRule1(inst2)
    
    def implDecisionSupportRule1(self, inst):
        self.assertEqual(inst.action[0].customization[0].expression, "ChlamydiaScreeningRequest")
        self.assertEqual(inst.action[0].customization[0].path, "~")
        self.assertEqual(inst.action[0].title, "Patient has not had chlamydia screening within the recommended timeframe...")
        self.assertEqual(inst.condition, "NoScreening")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.moduleMetadata.description, "Chlamydia Screening CDS Example Using Common")
        self.assertEqual(inst.moduleMetadata.identifier[0].use, "official")
        self.assertEqual(inst.moduleMetadata.identifier[0].value, "ChlamydiaScreening_CDS_UsingCommon")
        self.assertEqual(inst.moduleMetadata.publicationDate.date, FHIRDate("2015-07-22").date)
        self.assertEqual(inst.moduleMetadata.publicationDate.as_json(), "2015-07-22")
        self.assertEqual(inst.moduleMetadata.status, "draft")
        self.assertEqual(inst.moduleMetadata.title, "Chalmydia Screening CDS Example Using Common")
        self.assertEqual(inst.moduleMetadata.topic[0].text, "Chlamydia Screeening")
        self.assertEqual(inst.moduleMetadata.type, "module")
        self.assertEqual(inst.moduleMetadata.version, "2.0.0")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Chalmydia Screening CDS Example Using Common</div>")
        self.assertEqual(inst.text.status, "generated")

