import unittest

from fhirclient.client import FHIRClient


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
