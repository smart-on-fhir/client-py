# -*- coding: utf-8 -*-

import io
import json
import os.path
import logging
import unittest
from . import server


logging.basicConfig(level=logging.CRITICAL)


class TestResourceReference(unittest.TestCase):

    def testContainedResourceDetectionR4(self):
        from .models.R4 import questionnaire, medication, resource, valueset

        with io.open('fhirclient/fixtures/test_contained_resource_R4.json', 'r', encoding='utf-8') as h:
            data = json.load(h)
        q = questionnaire.Questionnaire(data)
        self.assertIsNotNone(q, "Must instantiate Questionnaire")
        self.assertEqual('Questionnaire', q.resource_type if hasattr(q, "resource_type") else q.resource_name)

        group = q.item[0].item[3]
        self.assertEqual('Observation.subject', group.linkId)
        question = group.item[0]
        self.assertEqual('Observation.subject._type', question.linkId)
        self.assertIsNotNone(question.answerOption)
        with self.assertRaises(Exception):
            question.answerOption[0].valueReference.resolved()
        reference = question.answerOption[0].valueReference
        # 1st resolve, extracting from contained resources
        contained = reference.resolved(medication.Medication)
        self.assertIsNone(contained, "Must not resolve on resource type mismatch")
        contained = reference.resolved(valueset.ValueSet)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet")
        self.assertEqual('ValueSet', contained.resource_type)
        self.assertEqual('Type options for Observation.subject', contained.name)

        # 2nd resolve, should pull from cache
        contained = reference.resolved(medication.Medication)
        self.assertIsNone(contained, "Must not resolve on resource type mismatch")
        contained = reference.resolved(resource.Resource)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet even if requesting `Resource`")
        contained = reference.resolved(valueset.ValueSet)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet")
        self.assertEqual('ValueSet', contained.resource_type)

    def testContainedResourceDetectionSTU3(self):
        from .models.STU3 import questionnaire, medication, resource, valueset

        with io.open('fhirclient/fixtures/test_contained_resource_STU3.json', 'r', encoding='utf-8') as h:
            data = json.load(h)
        q = questionnaire.Questionnaire(data)
        self.assertIsNotNone(q, "Must instantiate Questionnaire")
        self.assertEqual('Questionnaire', q.resource_type)

        group = q.item[0].item[3]
        self.assertEqual('Observation.subject', group.linkId)
        question = group.item[0]
        self.assertEqual('Observation.subject._type', question.linkId)
        self.assertIsNotNone(question.options)
        with self.assertRaises(Exception):
            question.options.resolved()

        # 1st resolve, extracting from contained resources
        contained = question.options.resolved(medication.Medication)
        self.assertIsNone(contained, "Must not resolve on resource type mismatch")
        contained = question.options.resolved(valueset.ValueSet)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet")
        self.assertEqual('ValueSet', contained.resource_type)
        self.assertEqual('Type options for Observation.subject', contained.name)

        # 2nd resolve, should pull from cache
        contained = question.options.resolved(medication.Medication)
        self.assertIsNone(contained, "Must not resolve on resource type mismatch")
        contained = question.options.resolved(resource.Resource)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet even if requesting `Resource`")
        contained = question.options.resolved(valueset.ValueSet)
        self.assertIsNotNone(contained, "Must resolve contained ValueSet")
        self.assertEqual('ValueSet', contained.resource_type)

    def testContainedResourceDetectionDSTU2(self):
        from .models.DSTU2 import questionnaire, medication, resource, valueset

        with io.open('fhirclient/fixtures/test_contained_resource_DSTU2.json', 'r', encoding='utf-8') as h:
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

    def testRelativeReferenceR4(self):
        from .models.R4 import questionnaire, medication, resource, valueset

        with io.open('fhirclient/fixtures/test_relative_reference_R4.json', 'r', encoding='utf-8') as h:
            data = json.load(h)
        q = questionnaire.Questionnaire(data)
        self.assertIsNotNone(q, "Must instantiate Questionnaire")
        self.assertEqual('Questionnaire', q.resource_type)
        q._server = MockServer()

        group = q.item[0].item[0]
        self.assertEqual('Observation.subject', group.linkId)
        question = group.item[0]
        self.assertEqual('Observation.subject._type', question.linkId)
        if hasattr(question, 'answerOption'):
            self.assertIsNotNone(question.answerOption)
        else:
            self.assertIsNotNone(question.option)
        with self.assertRaises(Exception):
            question.answerOption[0].valueReference.resolved()
        reference = question.answerOption[0].valueReference

        # resolve relative resource
        relative = reference.resolved(valueset.ValueSet)
        self.assertIsNotNone(relative, "Must resolve relative ValueSet")
        self.assertEqual('ValueSet', relative.resource_type)
        self.assertEqual('Type options for Observation.subject', relative.name)

        # 2nd resolve, should pull from cache
        relative = reference.resolved(medication.Medication)
        self.assertIsNone(relative, "Must not resolve on resource type mismatch")
        relative = reference.resolved(resource.Resource)
        self.assertIsNotNone(relative, "Must resolve relative ValueSet even if requesting `Resource`")

    def testRelativeReferenceSTU3(self):
        from .models.STU3 import questionnaire, medication, resource, valueset

        with io.open('fhirclient/fixtures/test_relative_reference_STU3.json', 'r', encoding='utf-8') as h:
            data = json.load(h)
        q = questionnaire.Questionnaire(data)
        self.assertIsNotNone(q, "Must instantiate Questionnaire")
        self.assertEqual('Questionnaire', q.resource_type)
        q._server = MockServer()

        group = q.item[0].item[0]
        self.assertEqual('Observation.subject', group.linkId)
        question = group.item[0]
        self.assertEqual('Observation.subject._type', question.linkId)
        self.assertIsNotNone(question.options)
        with self.assertRaises(Exception):
            question.options.resolved()

        # resolve relative resource
        relative = question.options.resolved(valueset.ValueSet)
        self.assertIsNotNone(relative, "Must resolve relative ValueSet")
        self.assertEqual('ValueSet', relative.resource_type)
        self.assertEqual('Type options for Observation.subject', relative.name)

        # 2nd resolve, should pull from cache
        relative = question.options.resolved(medication.Medication)
        self.assertIsNone(relative, "Must not resolve on resource type mismatch")
        relative = question.options.resolved(resource.Resource)
        self.assertIsNotNone(relative, "Must resolve relative ValueSet even if requesting `Resource`")

    def _doBundleReferences(self, bundle_fixture, medication, resource, patient, bundle):
        with io.open(bundle_fixture, 'r', encoding='utf-8') as h:
            data = json.load(h)
        b = bundle.Bundle(data)
        self.assertIsNotNone(b, "Must instantiate Bundle")
        self.assertEqual('Bundle', b.resource_type)
        # b._server = MockServer()

        # get resources
        pat23 = b.entry[0].resource
        self.assertEqual('Patient', pat23.resource_type)
        self.assertEqual('Darth', pat23.name[0].given[0])
        patURN = b.entry[1].resource
        self.assertEqual('Patient', patURN.resource_type)
        self.assertEqual('Ben', patURN.name[0].given[0])
        obs123 = b.entry[2].resource
        self.assertEqual('Observation', obs123.resource_type)
        obs56 = b.entry[3].resource
        self.assertEqual('Observation', obs56.resource_type)
        obs34 = b.entry[4].resource
        self.assertEqual('Observation', obs34.resource_type)

        # test resolving w/o server (won't work)
        res = obs123.subject.resolved(patient.Patient)
        self.assertIsNone(res)

        # test resolving with server
        b._server = MockServer()
        res = obs123.subject.resolved(patient.Patient)
        self.assertEqual(res, pat23)
        res = obs123.subject.resolved(medication.Medication)
        self.assertIsNone(res, "Must not resolve on type mismatch")
        res = obs56.subject.resolved(patient.Patient)
        self.assertEqual(res, patURN)
        res = obs34.subject.resolved(patient.Patient)
        self.assertIsNone(res, "Must not resolve Patient on same server but different endpoint")

    def testBundleReferencesR4(self):
        from .models.R4 import medication, resource, patient, bundle
        self._doBundleReferences('fhirclient/fixtures/test_bundle_R4.json', medication, resource, patient, bundle)

    def testBundleReferencesSTU3(self):
        from .models.STU3 import medication, resource, patient, bundle
        self._doBundleReferences('fhirclient/fixtures/test_bundle_STU3.json', medication, resource, patient, bundle)


class MockServer(server.FHIRServer):
    """ Reads local files.
    """

    def __init__(self):
        super(MockServer, self).__init__(None, base_uri='https://fhir.smarthealthit.org')

    def request_json(self, path, nosign=False):
        assert path
        parts = os.path.split(path)
        filename = '_'.join(parts) + '.json'
        with io.open(os.path.join('fhirclient/fixtures', filename), 'r', encoding='utf-8') as handle:
            return json.load(handle)
        return None
