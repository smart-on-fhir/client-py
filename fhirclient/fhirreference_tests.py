# -*- coding: utf-8 -*-

import json
import logging
import unittest
import models.questionnaire as questionnaire
import models.medication as medication
import models.resource as resource
import models.valueset as valueset


logging.basicConfig(level=logging.CRITICAL)


class TestContainedResource(unittest.TestCase):
    
    def testContainedResourceDetection(self):
        with open('test_contained_resource.json', 'r') as h:
            data = json.load(h)
        q = questionnaire.Questionnaire(data)
        self.assertIsNotNone(q, "Must instantiate Questionnaire")
        self.assertEqual('Questionnaire', q.resource_name)
        
        group = q.group.group[3]
        self.assertEqual('Observation.subject', group.linkId)
        question = group.question[0]
        self.assertEqual('Observation.subject._type', question.linkId)
        self.assertIsNotNone(question.options)
        with self.assertRaises(Exception):
            question.options.resolved()
        
        # 1st resolve, extracting from contained resources
        contained = question.options.resolved(medication.Medication)
        self.assertIsNone(contained, "Must not resolve on resource type mismatch")
        contained = question.options.resolved(valueset.ValueSet)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet")
        self.assertEqual('ValueSet', contained.resource_name)
        
        # 2nd resolve, should pull from cache
        contained = question.options.resolved(medication.Medication)
        self.assertIsNone(contained, "Must not resolve on resource type mismatch")
        contained = question.options.resolved(resource.Resource)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet even if requesting `Resource`")
        contained = question.options.resolved(valueset.ValueSet)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet")
        self.assertEqual('ValueSet', contained.resource_name)
