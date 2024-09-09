import unittest
from unittest import mock

from fhirclient.client import FHIRClient
from fhirclient.server import FHIRNotFoundException, FHIRUnauthorizedException

# Smallest valid-but-fake client state
MIN_STATE = {
    "server": {"base_uri": "http://example.com/fhir"},
}


class TestClient(unittest.TestCase):

    def test_load_from_state(self):
        state = {
            'app_id': 'AppID',
            'app_secret': 'AppSecret',
            'scope': 'user/*.read',
            'redirect': 'http://test.invalid/redirect',
            'patient_id': 'PatientID',
            'server': {
                'base_uri': 'http://test.invalid/',
                'auth_type': 'none',
                'auth': {
                    'app_id': 'AppId',
                },
            },
            'launch_token': 'LaunchToken',
            'launch_context': {
                'encounter': 'EncounterID',
                'patient': 'PatientID',
            },
            'jwt_token': 'JwtToken',
        }

        # Confirm round trip
        client = FHIRClient(state=state)
        self.assertEqual(state, client.state)

        # Sanity check a couple of the properties actually got set
        self.assertEqual('AppID', client.app_id)
        self.assertEqual('LaunchToken', client.launch_token)

        # Confirm we can do a partial from_state() - well, kind of partial since server is required
        client.from_state({'app_id': 'NewID', 'server': state['server']})
        self.assertEqual('NewID', client.app_id)
        self.assertEqual('LaunchToken', client.launch_token)

    @mock.patch("fhirclient.models.patient.Patient.read")
    def test_patient_property_happy_path(self, mock_read):
        save_func = mock.MagicMock()

        # Verify that we gracefully handle no patient_id being given
        client = FHIRClient(state=MIN_STATE, save_func=save_func)
        self.assertIsNone(client.patient)
        self.assertEqual(mock_read.call_count, 0)
        self.assertEqual(save_func.call_count, 0)

        # Verify we expose the provided patient ID as a Patient object
        client = FHIRClient(state={"patient_id": "P123", **MIN_STATE}, save_func=save_func)
        self.assertIsNotNone(client.patient)
        self.assertEqual(mock_read.call_count, 1)
        self.assertEqual(mock_read.call_args, mock.call("P123", client.server))
        self.assertEqual(save_func.call_count, 1)

    @mock.patch("fhirclient.models.patient.Patient.read")
    @mock.patch("fhirclient.client.FHIRClient.reauthorize")
    def test_patient_property_unauthorized(self, mock_reauthorize, mock_read):
        """We should attempt to reauthorize and re-request the patient"""

        client = FHIRClient(state={"patient_id": "P123", **MIN_STATE})

        # First try with a failed re-authorize
        mock_read.side_effect = FHIRUnauthorizedException("response")
        mock_reauthorize.return_value = False
        self.assertIsNone(client.patient)
        self.assertEqual(mock_read.call_count, 1)
        self.assertEqual(mock_reauthorize.call_count, 1)

        # Then with a successful re-authorize
        mock_read.reset_mock()
        mock_read.side_effect = [FHIRUnauthorizedException("response"), mock.MagicMock()]
        mock_reauthorize.reset_mock()
        mock_reauthorize.return_value = True
        self.assertIsNotNone(client.patient)
        self.assertEqual(mock_read.call_count, 2)
        self.assertEqual(mock_reauthorize.call_count, 1)

    @mock.patch("fhirclient.models.patient.Patient.read")
    def test_patient_property_not_found(self, mock_read):
        """We should attempt to reauthorize and re-request the patient"""
        mock_read.side_effect = FHIRNotFoundException("response")

        client = FHIRClient(state={"patient_id": "P123", **MIN_STATE})
        self.assertEqual(client.patient_id, "P123")  # sanity check before we start

        self.assertIsNone(client.patient)
        self.assertIsNone(client.patient_id)  # we clear out the patient id
