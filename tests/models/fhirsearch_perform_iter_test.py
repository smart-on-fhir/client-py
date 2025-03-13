import unittest
import requests
import responses

from fhirclient import server

from fhirclient.models.fhirsearch import FHIRSearch, FHIRSearchParam
from fhirclient.models.bundle import Bundle


class TestFHIRSearchIter(unittest.TestCase):
    def setUp(self):
        self.search = FHIRSearch(resource_type=Bundle)
        self.search.params = [
            FHIRSearchParam(name="patient", value="347"),
            FHIRSearchParam(name="_count", value="1")
        ]
        self.mock_server = MockServer("https://example.com")

    def create_bundle_entry(self, resource_id):
        """Helper to create a Bundle entry with a specific resource ID."""
        return {
            "fullUrl": f"https://example.com/base/MedicationRequest/{resource_id}",
            "resource": {
                "resourceType": "MedicationRequest",
                "id": resource_id,
                "subject": {"reference": "Patient/347"},
                "intent": "order",
                "status": "unknown",
                "medicationReference": {"reference": "Medication/example"}
            }
        }

    def add_mock_response(self, url, bundle_content):
        """Helper to set up a mock response for the given URL and bundle content."""
        responses.add(
            responses.GET,
            url,
            json=bundle_content,
            status=200
        )

    @responses.activate
    def test_perform_iter_single_bundle(self):
        # Mock the network response for the initial search request
        bundle_content = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": [self.create_bundle_entry("3123")]
        }

        # Mock the single page response
        self.add_mock_response("https://example.com/Bundle?patient=347&_count=1", bundle_content)

        # Call perform_iter with the server URL
        result = list(self.search.perform_iter(self.mock_server))

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].entry[0].resource.id, "3123")

    @responses.activate
    def test_perform_iter_pagination(self):
        bundle_page_1 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [
                {"relation": "next",
                 "url": "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2"}
            ],
            "entry": [self.create_bundle_entry("3123")]
        }

        # Second page bundle without a "next" link
        bundle_page_2 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": [self.create_bundle_entry("3124")]
        }

        # Mock both page responses
        self.add_mock_response("https://example.com/Bundle?patient=347&_count=1", bundle_page_1)
        self.add_mock_response(
            "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2",
            bundle_page_2)

        # Execute perform_iter to iterate over both pages
        result = list(self.search.perform_iter(self.mock_server))

        self.assertEqual(len(result), 2)  # Expect two pages of results
        self.assertEqual(result[0].entry[0].resource.id, "3123")
        self.assertEqual(result[1].entry[0].resource.id, "3124")

    @responses.activate
    def test_perform_iter_empty_bundle(self):
        # Mock an empty Bundle with no entries
        empty_bundle = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": []
        }
        self.add_mock_response("https://example.com/Bundle?patient=347&_count=1", empty_bundle)

        # Execute perform_iter with empty result
        result = list(self.search.perform_iter(self.mock_server))

        # Assertion: Should return an empty list
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0].entry), 0)

    @responses.activate
    def test_perform_iter_multiple_pages(self):
        # First page with a "next" link
        bundle_page_1 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [
                {"relation": "next", "url": "https://example.com/base/MedicationRequest?patient=347&page=2"}
            ],
            "entry": [self.create_bundle_entry("3123")]
        }

        # Second page with a "next" link
        bundle_page_2 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [
                {"relation": "next", "url": "https://example.com/base/MedicationRequest?patient=347&page=3"}
            ],
            "entry": [self.create_bundle_entry("3124")]
        }

        # Third page without a "next" link (end of pagination)
        bundle_page_3 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": [self.create_bundle_entry("3125")]
        }

        # Mock all page responses
        self.add_mock_response("https://example.com/Bundle?patient=347&_count=1", bundle_page_1)
        self.add_mock_response("https://example.com/base/MedicationRequest?patient=347&page=2", bundle_page_2)
        self.add_mock_response("https://example.com/base/MedicationRequest?patient=347&page=3", bundle_page_3)

        # Execute perform_iter to iterate over all pages
        result = list(self.search.perform_iter(self.mock_server))

        self.assertEqual(len(result), 3)  # Expect three pages of results
        self.assertEqual(result[0].entry[0].resource.id, "3123")
        self.assertEqual(result[1].entry[0].resource.id, "3124")
        self.assertEqual(result[2].entry[0].resource.id, "3125")

    @responses.activate
    def test_perform_resources_iter_single_page(self):
        # Single page bundle with one entry
        bundle_content = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": [self.create_bundle_entry("3123")]
        }

        # Mock the single page response
        self.add_mock_response("https://example.com/Bundle?patient=347&_count=1", bundle_content)

        # Call perform_resources_iter and collect resources
        result = list(self.search.perform_resources_iter(self.mock_server))

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, "3123")

    @responses.activate
    def test_perform_resources_iter_pagination(self):
        # First page bundle with a "next" link
        bundle_page_1 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [
                {"relation": "next",
                 "url": "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2"}
            ],
            "entry": [self.create_bundle_entry("3123")]
        }

        # Second page bundle without a "next" link
        bundle_page_2 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": [self.create_bundle_entry("3124")]
        }

        # Mock both page responses
        self.add_mock_response("https://example.com/Bundle?patient=347&_count=1", bundle_page_1)
        self.add_mock_response(
            "https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2",
            bundle_page_2)

        # Execute perform_resources_iter to retrieve resources across pages
        result = list(self.search.perform_resources_iter(self.mock_server))

        self.assertEqual(len(result), 2)  # Expect resources from both pages
        self.assertEqual(result[0].id, "3123")  # First page resource
        self.assertEqual(result[1].id, "3124")  # Second page resource

    @responses.activate
    def test_perform_resources_iter_multiple_pages(self):
        # Mock similar pagination for perform_resources_iter
        bundle_page_1 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [
                {"relation": "next", "url": "https://example.com/base/MedicationRequest?patient=347&page=2"}
            ],
            "entry": [self.create_bundle_entry("3123")]
        }

        bundle_page_2 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "link": [
                {"relation": "next", "url": "https://example.com/base/MedicationRequest?patient=347&page=3"}
            ],
            "entry": [self.create_bundle_entry("3124")]
        }

        bundle_page_3 = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": [self.create_bundle_entry("3125")]
        }

        # Mock responses for each page
        self.add_mock_response("https://example.com/Bundle?patient=347&_count=1", bundle_page_1)
        self.add_mock_response("https://example.com/base/MedicationRequest?patient=347&page=2", bundle_page_2)
        self.add_mock_response("https://example.com/base/MedicationRequest?patient=347&page=3", bundle_page_3)

        # Execute perform_resources_iter to retrieve resources across all pages
        result = list(self.search.perform_resources_iter(self.mock_server))

        self.assertEqual(len(result), 3)  # Expect resources from three pages
        self.assertEqual(result[0].id, "3123")
        self.assertEqual(result[1].id, "3124")
        self.assertEqual(result[2].id, "3125")

    @responses.activate
    def test_perform_resources_iter_null_bundle(self):
        """This happens when no results are found for a search."""
        # Mock the network response for the initial search request
        bundle_content = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": None,
        }

        # Mock the single page response
        self.add_mock_response("https://example.com/Bundle?patient=347&_count=1", bundle_content)

        # Call perform_resources_iter with the server URL
        result = list(self.search.perform_resources_iter(self.mock_server))
        self.assertEqual(result, [])

    @responses.activate
    def test_perform_resources_iter_null_resource(self):
        """This shouldn't happen for search results, but the spec allows .resource to be empty"""
        # Mock the network response for the initial search request
        bundle_content = {
            "resourceType": "Bundle",
            "type": "searchset",
            "entry": [{}],
        }

        # Mock the single page response
        self.add_mock_response("https://example.com/Bundle?patient=347&_count=1", bundle_content)

        # Call perform_resources_iter with the server URL
        result = list(self.search.perform_resources_iter(self.mock_server))
        self.assertEqual(result, [])


# Network-level Mocking
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
