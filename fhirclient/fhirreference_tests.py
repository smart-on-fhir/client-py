# -*- coding: utf-8 -*-

import io
import json
import os.path
import logging
import unittest
import models.questionnaire as questionnaire
import models.medication as medication
import models.resource as resource
import models.valueset as valueset
import server


logging.basicConfig(level=logging.CRITICAL)


class TestResourceReference(unittest.TestCase):
    
    def testContainedResourceDetection(self):
        with io.open('test_contained_resource.json', 'r', encoding='utf-8') as h:
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
        self.assertEqual('Type options for Observation.subject', contained.name)
        
        # 2nd resolve, should pull from cache
        contained = question.options.resolved(medication.Medication)
        self.assertIsNone(contained, "Must not resolve on resource type mismatch")
        contained = question.options.resolved(resource.Resource)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet even if requesting `Resource`")
        contained = question.options.resolved(valueset.ValueSet)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet")
        self.assertEqual('ValueSet', contained.resource_name)
    
    def testRelativeReference(self):
        with io.open('test_relative_reference.json', 'r', encoding='utf-8') as h:
            data = json.load(h)
        q = questionnaire.Questionnaire(data)
        self.assertIsNotNone(q, "Must instantiate Questionnaire")
        self.assertEqual('Questionnaire', q.resource_name)
        q._server = MockServer()
        
        group = q.group.group[0]
        self.assertEqual('Observation.subject', group.linkId)
        question = group.question[0]
        self.assertEqual('Observation.subject._type', question.linkId)
        self.assertIsNotNone(question.options)
        with self.assertRaises(Exception):
            question.options.resolved()
        
        # resolve relative resource
        relative = question.options.resolved(valueset.ValueSet)
        self.assertIsNotNone(relative, "Must resolve relative ValueSet")
        self.assertEqual('ValueSet', relative.resource_name)
        self.assertEqual('Type options for Observation.subject', relative.name)
        
        # 2nd resolve, should pull from cache
        relative = question.options.resolved(medication.Medication)
        self.assertIsNone(relative, "Must not resolve on resource type mismatch")
        relative = question.options.resolved(resource.Resource)
        self.assertIsNotNone(relative, "Must resolve relative ValueSet even if requesting `Resource`")


class MockServer(server.FHIRServer):
    """ Reads local files.
    """
    
    def __init__(self):
        super().__init__(None, base_uri='https://fhir.smarthealthit.org')
    
    def request_json(self, path, nosign=False):
        assert path
        parts = os.path.split(path)
        filename = '_'.join(parts) + '.json'
        with io.open(filename, 'r', encoding='utf-8') as handle:
            return json.load(handle)
        return None

