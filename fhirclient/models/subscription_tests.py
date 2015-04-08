#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import subscription
from fhirdate import FHIRDate


class SubscriptionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = subscription.Subscription(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testSubscription1(self):
        inst = self.instantiate_from("subscription-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e3a2990> instance")
    
        self.assertEqual(inst.channel.endpoint, "https://biliwatch.com/customers/mount-auburn-miu/on-result")
        self.assertEqual(inst.channel.header, "Authorization: Bearer secret-token-abc-123")
        self.assertEqual(inst.channel.payload, "application/json")
        self.assertEqual(inst.channel.type, "rest-hook")
        self.assertEqual(inst.criteria, "/Observation?name=http://loinc.org|1975-2")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.reason, "Monitor new neonatal function")
        self.assertEqual(inst.status, "requested")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

