# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
import requests
from fhirclient.client import FHIRClient
from fhirclient.constants import FHIRVersion


SETTINGS = {
    FHIRVersion.R4: {
        "api_base": "https://launch.smarthealthit.org/v/r4/fhir",
        # This is '{"a":"1","b":"8d1f86a8-3284-43bd-b45e-5931948c97e4","e":"e92c468f-8f1b-4d5e-bf96-76dc945d2e8c","f":"1"}' base64
        "launch_token": "eyJhIjoiMSIsImIiOiI4ZDFmODZhOC0zMjg0LTQzYmQtYjQ1ZS01OTMxOTQ4Yzk3ZTQiLCJlIjoiZTkyYzQ2OGYtOGYxYi00ZDVlLWJmOTYtNzZkYzk0NWQyZThjIiwiZiI6IjEifQ",
        "name": "Mrs. Latanya Kohler",
    },
    FHIRVersion.STU3:  {
        "api_base": "https://launch.smarthealthit.org/v/r3/fhir",
        # This is '{"a":"1","b":"53918843-a2a2-499e-b397-2e25035cbeb3","e":"smart-Practitioner-71614502","f":"1"}' base64
        "launch_token": "eyJhIjoiMSIsImIiOiI1MzkxODg0My1hMmEyLTQ5OWUtYjM5Ny0yZTI1MDM1Y2JlYjMiLCJlIjoic21hcnQtUHJhY3RpdGlvbmVyLTcxNjE0NTAyIiwiZiI6IjEifQ",
        "encounter": "2b3ead66-c990-4132-a609-2934f00ec52c",
        "name": "Mr. Ronnie Gutmann",
        "meds": {
            "23fc6a0e-95a0-4dce-8c81-692d6d143e64",
            "cfc013c2-8487-48a0-aa13-0b45b73ba53b",
            "cfc013c2-8487-48a0-aa13-0b45b73ba53b",
        }
    },
    FHIRVersion.DSTU2:  {
        "api_base": "https://launch.smarthealthit.org/v/r2/fhir",
        # This is '{"a":"1","b":"57b85682-ce42-4187-a593-7864248a9484","e":"SMART-1234","f":"1"}' base64
        "launch_token": "eyJhIjoiMSIsImIiOiI1N2I4NTY4Mi1jZTQyLTQxODctYTU5My03ODY0MjQ4YTk0ODQiLCJlIjoiU01BUlQtMTIzNCIsImYiOiIxIn0",
        "encounter": "114b4ccb-cbf6-4abd-8f1b-8ded0dbb59a2",
        "name": "Mr. Ronnie Gutmann",
        "meds": {
            "RES368466",
            "RES368467",
        }
    },
}


class IntegrationTest(unittest.TestCase):

    def launch(self, version):
        settings = {
            "redirect_uri": "fhirclient://callback",
            "api_base": SETTINGS[version]["api_base"],
            "launch_token": SETTINGS[version]["launch_token"],
            "app_id": "app" + version,
            "app_secret": "secret",
            "version": version,
        }

        state = {}

        def save(s):
            state.clear()
            state.update(s)

        client = FHIRClient(settings=settings, save_func=save)

        authorize_url = client.authorize_url
        if "encounter" in SETTINGS[version]:
            authorize_url += "&encounter=" + SETTINGS[version]["encounter"]
        response = requests.get(authorize_url, allow_redirects=False)
        response.raise_for_status()

        # Restore from state for fun
        client = FHIRClient(state=state)
        client.handle_callback(response.headers["Location"])
        name = client.human_name(client.patient.name[0])
        self.assertEqual(SETTINGS[version]["name"], name)
        return client

    def test_launch_DSTU2(self):
        from .models.DSTU2.medicationorder import MedicationOrder
        client = self.launch(FHIRVersion.DSTU2)
        search = MedicationOrder.where(struct={"patient": "Patient/{}".format(client.patient.id)})
        meds = search.perform_resources(client.server)
        result = set()
        for med in meds:
            result.add(med.id)
        self.assertEqual(SETTINGS[FHIRVersion.DSTU2]["meds"], result)

    def test_launch_STU3(self):
        from .models.STU3.medicationrequest import MedicationRequest
        client = self.launch(FHIRVersion.STU3)
        search = MedicationRequest.where(struct={"patient": "Patient/{}".format(client.patient.id)})
        meds = search.perform_resources(client.server)
        result = set()
        for med in meds:
            result.add(med.id)
        self.assertEqual(SETTINGS[FHIRVersion.STU3]["meds"], result)

    @unittest.skip("r4 metadata currently broken")
    def test_launch_R4(self):
        from .models.R4.medicationrequest import MedicationRequest
        client = self.launch(FHIRVersion.R4)
        search = MedicationRequest.where(struct={"patient": "Patient/{}".format(client.patient.id)})
        meds = search.perform_resources(client.server)
        result = set()
        for med in meds:
            result.add(med.id)
        self.assertEqual(SETTINGS[FHIRVersion.R4]["meds"], result)
