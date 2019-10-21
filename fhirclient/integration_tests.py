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
