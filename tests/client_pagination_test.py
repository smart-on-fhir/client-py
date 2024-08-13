import unittest
from unittest.mock import patch, MagicMock

import requests
from fhirclient.models.bundle import Bundle

from fhirclient.client import FHIRClient


class TestFHIRClientPagination(unittest.TestCase):
    def setUp(self) -> None:
        state = {
            "app_id": "AppID",
            "app_secret": "AppSecret",
            "scope": "user/*.read",
            "redirect": "http://test.invalid/redirect",
            "patient_id": "PatientID",
            "server": {
                "base_uri": "http://test.invalid/",
                "auth_type": "none",
                "auth": {
                    "app_id": "AppId",
                },
            },
            "launch_token": "LaunchToken",
            "launch_context": {
                "encounter": "EncounterID",
                "patient": "PatientID",
            },
            "jwt_token": "JwtToken",
        }

        # Confirm round trip
        self.client = FHIRClient(state=state)

        self.bundle = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [
                {"relation": "self", "url": "http://example.com/fhir/Bundle/1"},
                {"relation": "next", "url": "http://example.com/fhir/Bundle/2"},
            ],
            "entry": [
                {
                    "fullUrl": "http://example.com/fhir/Patient/1",
                    "resource": {
                        "resourceType": "Patient",
                        "id": "1",
                        "name": [{"family": "Doe", "given": ["John"]}],
                        "gender": "male",
                        "birthDate": "1980-01-01",
                    },
                },
                {
                    "fullUrl": "http://example.com/fhir/Patient/2",
                    "resource": {
                        "resourceType": "Patient",
                        "id": "2",
                        "name": [{"family": "Smith", "given": ["Jane"]}],
                        "gender": "female",
                        "birthDate": "1990-05-15",
                    },
                },
            ],
        }

    def test_get_next_link(self):
        next_link = self.client._get_next_link(Bundle(self.bundle))
        self.assertEqual(next_link, "http://example.com/fhir/Bundle/2")

    def test_get_next_link_no_next(self):
        bundle_without_next = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [{"relation": "self", "url": "http://example.com/fhir/Bundle/1"}],
        }
        bundle = Bundle(bundle_without_next)
        next_link = self.client._get_next_link(bundle)
        self.assertIsNone(next_link)

    def test_sanitize_next_link_valid(self):
        next_link = "http://example.com/fhir/Bundle/2?page=2&size=10"
        sanitized_link = self.client._sanitize_next_link(next_link)
        self.assertEqual(sanitized_link, next_link)

    def test_sanitize_next_link_invalid_scheme(self):
        next_link = "ftp://example.com/fhir/Bundle/2?page=2&size=10"
        with self.assertRaises(ValueError):
            self.client._sanitize_next_link(next_link)

    def test_sanitize_next_link_invalid_domain(self):
        next_link = "http:///fhir/Bundle/2?page=2&size=10"
        with self.assertRaises(ValueError):
            self.client._sanitize_next_link(next_link)

    @patch("requests.get")
    def test_execute_pagination_request_success(self, mock_get):
        mock_response = MagicMock()
        # Set up the mock to return a specific JSON payload when its json() method is called
        mock_response.json.return_value = self.bundle
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        next_link = "http://example.com/fhir/Bundle/2"
        sanitized_link = self.client._sanitize_next_link(next_link)
        result = self.client._execute_pagination_request(sanitized_link)
        self.assertIsInstance(result, Bundle)
        self.assertIn("entry", result.as_json())
        mock_get.assert_called_once_with(sanitized_link)

    @patch("requests.get")
    def test_execute_pagination_request_http_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError("HTTP Error")

        next_link = "http://example.com/fhir/Bundle/2"
        sanitized_link = self.client._sanitize_next_link(next_link)

        with self.assertRaises(requests.exceptions.HTTPError):
            self.client._execute_pagination_request(sanitized_link)

    @patch("requests.get")
    def test_execute_pagination_request_returns_last_bundle_if_no_next_link(self, mock_get):
        # Mock the response to simulate a Bundle with no next link
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [{"relation": "self", "url": "http://example.com/fhir/Bundle/1"}],
            "entry": [{"resource": {"resourceType": "Patient", "id": "1"}}],
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        sanitized_link = "http://example.com/fhir/Bundle/1"
        result = self.client._execute_pagination_request(sanitized_link)

        # Check that the result is the Bundle itself, not None
        self.assertIsInstance(result, Bundle)
        self.assertTrue(hasattr(result, 'entry'))
        mock_get.assert_called_once_with(sanitized_link)

    @patch("fhirclient.client.FHIRClient._execute_pagination_request")
    def test_fetch_next_page(self, mock_execute_request):
        mock_execute_request.return_value = Bundle(self.bundle)
        result = self.client._fetch_next_page(Bundle(self.bundle))
        self.assertIsInstance(result, Bundle)
        self.assertTrue(hasattr(result, "entry"))
        mock_execute_request.assert_called_once()

    def test_fetch_next_page_no_next_link(self):
        bundle_without_next = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [{"relation": "self", "url": "http://example.com/fhir/Bundle/1"}],
        }
        bundle = Bundle(bundle_without_next)
        result = self.client._fetch_next_page(bundle)
        self.assertIsNone(result)

    @patch("fhirclient.client.FHIRClient._fetch_next_page")
    def test_iter_pages(self, mock_fetch_next_page):
        # Set up the mock to return a new bundle, then None to stop iteration
        mock_fetch_next_page.side_effect = [Bundle(self.bundle), None]
        pages = list(self.client.iter_pages(Bundle(self.bundle)))

        # Check that two bundles were returned (the first bundle and the one from mock)
        self.assertEqual(len(pages), 2)
        self.assertIsInstance(pages[0], Bundle)
        self.assertIsInstance(pages[1], Bundle)

        # Compare JSON representations instead of object instances
        self.assertEqual(pages[0].as_json(), self.bundle)
        self.assertEqual(pages[1].as_json(), self.bundle)

        # Ensure that _fetch_next_page was called twice
        self.assertEqual(mock_fetch_next_page.call_count, 2)
