import unittest
from urllib.parse import parse_qs, urlencode, urlparse

from aioresponses import aioresponses

from fhirclient.server import AsyncFHIRServer
from fhirclient.models.bundle import Bundle
from fhirclient.models.fhirsearch import FHIRSearch, FHIRSearchParam
from fhirclient.models.patient import Patient


def create_async_server() -> AsyncFHIRServer:
    return AsyncFHIRServer(
        None,
        state={
            "base_uri": "https://example.invalid/",
            "auth_type": "oauth2",
            "auth": {
                "aud": "https://example.invalid/",
                "registration_uri": "https://example.invalid/o2/registration",
                "authorize_uri": "https://example.invalid/o2/authorize",
                "redirect_uri": "https://example.invalid/o2/redirect",
                "token_uri": "https://example.invalid/o2/token",
                "auth_state": "931f4c31-73e2-4c04-bf6b-b7c9800312ea",
                "app_secret": "my-secret",
                "access_token": "my-access-token",
                "refresh_token": "my-refresh-token",
            },
        },
    )


class TestAsyncAPI(unittest.IsolatedAsyncioTestCase):
    async def test_request_json_async(self):
        fhir = create_async_server()
        try:
            with aioresponses() as mocked:
                mocked.get(
                    "https://example.invalid/Binary/bin1",
                    payload={"resourceType": "Binary", "id": "bin1"},
                )

                resp = await fhir.request_json_async("Binary/bin1")
                self.assertEqual(resp["id"], "bin1")
        finally:
            await fhir.aclose()

    async def test_handle_callback_async(self):
        fhir = create_async_server()
        try:
            uri = fhir.authorize_uri
            authorize_args = parse_qs(urlparse(uri).query)
            self.assertIn("code_challenge", authorize_args)

            with aioresponses() as mocked:
                mocked.post(
                    "https://example.invalid/o2/token",
                    payload={"access_token": "xyz"},
                )

                callback_url = "https://example.org/callback?" + urlencode(
                    dict(code="abc123", state=fhir.auth.auth_state)
                )
                await fhir.handle_callback_async(callback_url)
                self.assertEqual(fhir.auth.access_token, "xyz")
        finally:
            await fhir.aclose()

    async def test_read_resource_and_search_iter_async(self):
        fhir = create_async_server()
        try:
            with aioresponses() as mocked:
                mocked.get(
                    "https://example.invalid/Patient/p1",
                    payload={"resourceType": "Patient", "id": "p1"},
                )
                patient = await Patient.read_async("p1", fhir)
                self.assertEqual(patient.id, "p1")

                search = FHIRSearch(resource_type=Bundle)
                search.params = [
                    FHIRSearchParam(name="patient", value="347"),
                    FHIRSearchParam(name="_count", value="1"),
                ]
                mocked.get(
                    "https://example.invalid/Bundle?patient=347&_count=1",
                    payload={
                        "resourceType": "Bundle",
                        "type": "searchset",
                        "link": [
                            {
                                "relation": "next",
                                "url": "https://example.invalid/Bundle?patient=347&_count=1&page=2",
                            }
                        ],
                        "entry": [{"resource": {"resourceType": "Patient", "id": "p1"}}],
                    },
                )
                mocked.get(
                    "https://example.invalid/Bundle?patient=347&_count=1&page=2",
                    payload={
                        "resourceType": "Bundle",
                        "type": "searchset",
                        "entry": [{"resource": {"resourceType": "Patient", "id": "p2"}}],
                    },
                )

                pages = []
                async for bundle in search.perform_iter_async(fhir):
                    pages.append(bundle)

                self.assertEqual(len(pages), 2)
                self.assertEqual(pages[0].entry[0].resource.id, "p1")
                self.assertEqual(pages[1].entry[0].resource.id, "p2")
        finally:
            await fhir.aclose()
