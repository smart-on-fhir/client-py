"""Regression tests for https://github.com/smart-on-fhir/client-py/issues/30.

Extensions on FHIR primitives (the `_name` underscore elements) must survive
a parse -> `as_json()` round-trip instead of being silently dropped.
"""

import unittest

from fhirclient.models import observation, patient


class PrimitiveExtensionTests(unittest.TestCase):
    def test_gender_extension_round_trip(self):
        """The exact example from issue #30."""
        data = {
            "resourceType": "Patient",
            "gender": "male",
            "_gender": {
                "extension": [{
                    "url": "http://test-extension",
                    "valueString": "with extra data",
                }],
            },
        }
        inst = patient.Patient(data)
        self.assertIsNotNone(inst._gender)
        self.assertEqual("http://test-extension", inst._gender.extension[0].url)
        self.assertEqual("with extra data", inst._gender.extension[0].valueString)

        js = inst.as_json()
        self.assertEqual(data["_gender"], js["_gender"])

        # a second round-trip must be stable
        inst2 = patient.Patient(js)
        self.assertEqual(js, inst2.as_json())

    def test_list_primitive_extension_round_trip(self):
        """`_given` is a same-length array shadowing the `given` primitives."""
        data = {
            "resourceType": "Patient",
            "name": [{
                "given": ["John", "J"],
                "_given": [
                    {"extension": [{"url": "http://x", "valueString": "y"}]},
                    None,
                ],
            }],
        }
        inst = patient.Patient(data)
        js = inst.as_json()
        self.assertEqual(data["name"][0]["_given"], js["name"][0]["_given"])

    def test_datetime_primitive_extension_round_trip(self):
        """Also works for choice/date primitives like `effectiveDateTime`."""
        data = {
            "resourceType": "Observation",
            "status": "final",
            "code": {"text": "x"},
            "effectiveDateTime": "2024-01-01T00:00:00Z",
            "_effectiveDateTime": {
                "extension": [{"url": "http://tz", "valueString": "UTC"}],
            },
        }
        inst = observation.Observation(data)
        js = inst.as_json()
        self.assertEqual(data["_effectiveDateTime"], js["_effectiveDateTime"])

    def test_no_phantom_underscore_keys(self):
        """Resources without underscore payloads serialize exactly as before."""
        inst = patient.Patient({"resourceType": "Patient", "gender": "male"})
        self.assertEqual({"resourceType", "gender"}, set(inst.as_json().keys()))
