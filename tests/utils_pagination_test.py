import io
import json
import os
import unittest
from unittest.mock import patch, MagicMock

import requests
from fhirclient import server

from fhirclient.models import bundle
from fhirclient.models.bundle import Bundle
from fhirclient._utils import _get_next_link, _sanitize_next_link, _execute_pagination_request, _fetch_next_page, \
    iter_pages


class TestUtilsPagination(unittest.TestCase):

    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Bundle", js["resourceType"])
        return bundle.Bundle(js)

    def test_get_next_link(self):
        inst = self.instantiate_from("bundle-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Bundle instance")

        # The returned URL should be the sanitized version
        next_link = _get_next_link(inst)
        sanitized_expected_url = "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2"

        self.assertEqual(next_link, sanitized_expected_url)

    def test_get_next_link_no_next(self):
        bundle_without_next = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [{"relation": "self", "url": "http://example.com/fhir/Bundle/1"}],
        }
        bundle = Bundle(bundle_without_next)
        next_link = _get_next_link(bundle)
        self.assertIsNone(next_link)

    def test_sanitize_next_link_valid(self):
        next_link = "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2"
        sanitized_link = _sanitize_next_link(next_link)
        self.assertEqual(sanitized_link, next_link)

    def test_sanitize_next_link_invalid_scheme(self):
        next_link = "ftp://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2"
        with self.assertRaises(ValueError):
            _sanitize_next_link(next_link)

    def test_sanitize_next_link_missing_scheme(self):
        next_link = "example.com/base/MedicationRequest?patient=347&page=2"
        with self.assertRaises(ValueError):
            _sanitize_next_link(next_link)

    def test_sanitize_next_link_missing_netloc(self):
        next_link = "https:///MedicationRequest?page=2"
        with self.assertRaises(ValueError):
            _sanitize_next_link(next_link)

    @patch("requests.get")
    def test_execute_pagination_request_success(self, mock_get):
        inst = self.instantiate_from("bundle-example.json")

        mock_response = MagicMock()
        mock_response.json.return_value = inst.as_json()
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        next_link = "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2"
        sanitized_link = _sanitize_next_link(next_link)

        mock_server = MockServer("https://example.com/base")
        result = _execute_pagination_request(sanitized_link, mock_server)

        self.assertIsInstance(result, Bundle)
        self.assertIn("entry", result.as_json())
        mock_get.assert_called_once_with(sanitized_link)

    @patch("requests.get")
    def test_execute_pagination_request_http_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError("HTTP Error")

        next_link = "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2"
        sanitized_link = _sanitize_next_link(next_link)

        mock_server = MockServer("https://example.com/base")

        with self.assertRaises(requests.exceptions.HTTPError):
            _execute_pagination_request(sanitized_link, mock_server)

    @patch("requests.get")
    def test_execute_pagination_request_returns_last_bundle_if_no_next_link(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [{"relation": "self", "url": "http://example.com/fhir/Bundle/1"}],
            "entry": [{"resource": {"resourceType": "Patient", "id": "1"}}],
        }
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        sanitized_link = "https://example.com/base/MedicationRequest?patient\u003d347\u0026_include\u003dMedicationRequest.medication\u0026_count\u003d2"
        mock_server = MockServer("https://example.com/base")
        result = _execute_pagination_request(sanitized_link, mock_server)

        # Check that the result is the Bundle itself, not None
        self.assertIsInstance(result, Bundle)
        self.assertTrue(hasattr(result, 'entry'))
        mock_get.assert_called_once_with(sanitized_link)

    @patch("fhirclient._utils._execute_pagination_request")
    def test_fetch_next_page(self, mock_execute_request):
        inst = self.instantiate_from("bundle-example.json")
        mock_execute_request.return_value = inst
        mock_server = MockServer("https://example.com/base")

        result = _fetch_next_page(inst, mock_server)
        self.assertIsInstance(result, Bundle)
        self.assertTrue(hasattr(result, "entry"))
        mock_execute_request.assert_called_once_with(_get_next_link(inst), mock_server)

    def test_fetch_next_page_no_next_link(self):
        bundle_without_next = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [{"relation": "self", "url": "http://example.com/fhir/Bundle/1"}],
        }
        bundle = Bundle(bundle_without_next)
        mock_server = MockServer("https://example.com/base")
        result = _fetch_next_page(bundle, mock_server)
        self.assertIsNone(result)

    @patch("fhirclient._utils._execute_pagination_request")
    def test_iter_pages(self, mock_fetch_next_page):
        inst = self.instantiate_from("bundle-example.json")
        inst_page2 = self.instantiate_from("bundle-example-page2.json")

        # Set up the mock to return a new bundle, then None to stop iteration
        mock_fetch_next_page.side_effect = [inst_page2, None]
        mock_server = MockServer("https://example.com/base")
        pages = list(iter_pages(inst, mock_server))

        # Check that two bundles were returned (the first bundle and the one from mock)
        self.assertEqual(len(pages), 2)
        self.assertIsInstance(pages[0], Bundle)
        self.assertIsInstance(pages[1], Bundle)

        self.assertNotEqual(pages[0].as_json(), pages[1].as_json())  # Ensure the two pages are different
        self.assertEqual(pages[0].as_json(), inst.as_json())
        self.assertEqual(pages[1].as_json(), inst_page2.as_json())  # Ensure the second page is correct

        # Ensure that _fetch_next_page was called twice
        self.assertEqual(mock_fetch_next_page.call_count, 1)


class MockServer(server.FHIRServer):
    def __init__(self, base_url):
        super().__init__(None, base_uri=base_url)

    def request_json(self, path):
        if path.startswith("http"):
            full_url = path
        else:
            full_url = f"{self.base_uri.rstrip('/')}/{path.lstrip('/')}"
        response = requests.get(full_url)
        return response.json() if response else None
