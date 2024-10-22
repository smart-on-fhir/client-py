import io
import json
import os
import unittest
from unittest.mock import MagicMock, patch

import fhirclient

from fhirclient import server

from fhirclient.models import bundle
from fhirclient.models.fhirsearch import FHIRSearch
from fhirclient.models.bundle import Bundle, BundleEntry


class TestFHIRSearchIter(unittest.TestCase):
    def setUp(self):
        # self.mock_server = MockServer(tmpdir=os.path.join(os.path.dirname(__file__), '..', 'data', 'examples'))
        self.mock_server = MagicMock()
        self.search = FHIRSearch(resource_type=Bundle)
        self.mock_bundle = self.instantiate_from('bundle-example.json')
        self.mock_next_bundle = self.instantiate_from('bundle-example-page2.json')

    def instantiate_from(self, filename):
        # Construct the path to the example file
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        filepath = os.path.join(datadir, filename)

        # Read the JSON file and return a Bundle instance
        with io.open(filepath, 'r', encoding='utf-8') as handle:
            js = json.load(handle)

        self.assertEqual("Bundle", js["resourceType"], "The resourceType is not 'Bundle'.")
        return Bundle(js)

    @patch('fhirclient._utils._fetch_next_page')
    @patch('fhirclient._utils.iter_pages')
    @patch('fhirclient.models.fhirsearch.FHIRSearch.perform')
    def test_perform_iter_single_bundle(self, mock_perform, mock_iter_pages, mock_fetch_next_page):
        self.mock_bundle = self.instantiate_from('bundle-example-page2.json')
        mock_perform.return_value = self.mock_bundle
        mock_iter_pages.side_effect = iter([self.mock_bundle])
        mock_fetch_next_page.side_effect = [None]

        result = self.search.perform_iter(self.mock_server)
        bundles = list(result)

        self.assertEqual(len(bundles), 1, f"Expected 1 bundle but got {len(bundles)}")
        self.assertEqual(bundles[0], self.mock_bundle)

        mock_perform.assert_called_once_with(self.mock_server)


    @patch('fhirclient._utils._fetch_next_page')
    @patch('fhirclient._utils.iter_pages')
    @patch('fhirclient.models.fhirsearch.FHIRSearch.perform')
    def test_perform_iter(self, mock_perform, mock_iter_pages, mock_fetch_next_page):
        self.mock_bundle = self.instantiate_from('bundle-example.json')
        self.mock_next_bundle = self.instantiate_from('bundle-example-page2.json')

        # Set up mock_perform to return the first bundle
        mock_perform.return_value = self.mock_bundle
        mock_iter_pages.side_effect = iter([self.mock_bundle, self.mock_next_bundle])

        # Make _fetch_next_page return the next bundle and then stop
        mock_fetch_next_page.side_effect = [self.mock_next_bundle, None]

        result = self.search.perform_iter(self.mock_server)
        bundles = list(result)

        self.assertEqual(len(bundles), 2, f"Expected 2 bundles but got {len(bundles)}")
        self.assertEqual(bundles[0], self.mock_bundle)
        self.assertEqual(bundles[1], self.mock_next_bundle)

        mock_perform.assert_called_once_with(self.mock_server)
        mock_fetch_next_page.assert_called()

    def test_perform_iter_no_first_bundle(self):
        self.search.perform = MagicMock(return_value=None)
        result = list(self.search.perform_iter(self.mock_server))
        self.assertEqual(result, [])

    @patch('fhirclient._utils.iter_pages')
    @patch('requests.get')  # Mock requests.get to avoid actual HTTP calls
    def test_perform_resources_iter_single_page(self, mock_iter_pages, mock_get):
        
        # Test the case where there is only a single page in the bundle (no pagination).
        
        # Manually create valid FHIR resources
        medication_request_resource = {
            'resourceType': 'MedicationRequest',
            'id': '3123',
            'subject': {
                'reference': 'Patient/347'
            },
            'intent': 'order',
            'status': 'unknown',
            'medicationReference': {
                'reference': 'Medication/example'
            }
        }

        # Create a valid BundleEntry with the MedicationRequest resource
        mock_entry1 = BundleEntry({
            'fullUrl': 'https://example.com/base/MedicationRequest/3123',
            'resource': medication_request_resource
        })

        # Create a valid Bundle
        mock_bundle = Bundle({
            'resourceType': 'Bundle',
            'type': 'searchset',  # Required field
            'entry': [
                {'fullUrl': 'https://example.com/base/MedicationRequest/3123', 'resource': medication_request_resource}
            ]
        })

        # Mock the behavior of `perform` to return a bundle with entries
        self.search.perform = MagicMock(return_value=mock_bundle)

        # Mock `iter_pages` to return a single page (mock bundle)
        mock_iter_pages.return_value = iter([mock_bundle])

        # Ensure `requests.get` does not actually run
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'resourceType': 'Bundle'}

        resource_iter = self.search.perform_resources_iter(self.mock_server)
        resources = list(resource_iter)

        self.assertEqual(len(resources), len(mock_bundle.entry))
        self.assertTrue(all(isinstance(entry, BundleEntry) for entry in mock_bundle.entry))

    @patch('fhirclient._utils.iter_pages')
    def test_perform_resources_iter_multiple_pages(self, mock_iter_pages):
        # Create first bundle with one entry and a next link
        mock_bundle_page1 = Bundle({
            'resourceType': 'Bundle',
            'type': 'searchset',
            'entry': [
                {'fullUrl': 'https://example.com/base/MedicationRequest/3123',
                 'resource': {
                     'resourceType': 'MedicationRequest',
                     'id': '3123',
                     'subject': {
                         'reference': 'Patient/347'
                     },
                     'intent': 'order',
                     'status': 'unknown',
                     'medicationReference': {
                         'reference': 'Medication/example'
                     }
                 }}
            ],
            'link': [
                {
                    'relation': 'next',
                    'url': 'https://example.com/base/MedicationRequest?page=2'  # Simulating the next page link
                }
            ]
        })

        # Create second bundle with another entry
        mock_bundle_page2 = Bundle({
            'resourceType': 'Bundle',
            'type': 'searchset',
            'entry': [
                {'fullUrl': 'https://example.com/base/MedicationRequest/3124',
                 'resource': {
                     'resourceType': 'MedicationRequest',
                     'id': '3124',
                     'subject': {
                         'reference': 'Patient/348'
                     },
                     'intent': 'order',
                     'status': 'unknown',
                     'medicationReference': {
                         'reference': 'Medication/example2'
                     }
                 }}
            ]
        })

        # Directly mock requests.get to return a proper response
        mock_response = MagicMock()
        mock_response.raise_for_status = MagicMock()  # Simulate that there is no HTTP error
        mock_response.json.return_value = mock_bundle_page2.as_json()  # Return the second bundle's JSON

        # Now override the requests.get behavior
        with patch('requests.get', return_value=mock_response):
            # Mock perform to return the first page bundle
            self.search.perform = MagicMock(return_value=mock_bundle_page1)

            # Mock iter_pages to return both bundles
            mock_iter_pages.return_value = iter([mock_bundle_page1, mock_bundle_page2])

            # Execute the method to get resources
            resource_iter = self.search.perform_resources_iter(self.mock_server)
            resources = list(resource_iter)

            # Ensure that both resources from both pages are included
            self.assertEqual(len(resources), 2)  # Expect 2 resources, one per page

            # Ensure that the entries are from the correct pages
            self.assertEqual(resources[0].id, '3123')
            self.assertEqual(resources[1].id, '3124')

            # Ensure that all resources are correctly typed
            self.assertTrue(all(
                isinstance(resource, fhirclient.models.medicationrequest.MedicationRequest) for resource in resources))


class MockServer(server.FHIRServer):
    """ Reads local files.
    """

    def __init__(self, tmpdir: str):
        super().__init__(None, base_uri='https://fhir.smarthealthit.org')
        self.directory = tmpdir

    def request_json(self, path, nosign=False):
        assert path
        with io.open(os.path.join(self.directory, path), encoding='utf-8') as handle:
            return json.load(handle)
