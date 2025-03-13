import urllib
from typing import Optional

from typing import TYPE_CHECKING, Iterator

if TYPE_CHECKING:
    from fhirclient.server import FHIRServer
    from fhirclient.models.bundle import Bundle


# Use forward references to avoid circular imports
def _fetch_next_page(bundle: 'Bundle', server: 'FHIRServer') -> Optional['Bundle']:
    """
    Fetch the next page of results using the `next` link provided in the bundle.

    Args:
        bundle (Bundle): The FHIR Bundle containing the `next` link.
        server (FHIRServer): The FHIR server instance for handling requests and authentication.

    Returns:
        Optional[Bundle]: The next page of results as a FHIR Bundle, or None if no "next" link is found.
    """
    if next_link := _get_next_link(bundle):
        return _execute_pagination_request(next_link, server)
    return None


def _get_next_link(bundle: 'Bundle') -> Optional[str]:
    """
    Extract the `next` link from the Bundle's links.

    Args:
        bundle (Bundle): The FHIR Bundle containing pagination links.

    Returns:
        Optional[str]: The URL of the next page if available, None otherwise.
    """
    if not bundle.link:
        return None

    for link in bundle.link:
        if link.relation == "next":
            return _sanitize_next_link(link.url)
    return None


def _sanitize_next_link(next_link: str) -> str:
    """
    Sanitize the `next` link by validating its scheme and hostname against the origin server.

    This function ensures the `next` link URL uses a valid scheme (`http` or `https`) and that it contains a
    hostname. This provides a basic safeguard against malformed URLs without overly restricting flexibility.

    Args:
        next_link (str): The raw `next` link URL.

    Returns:
        str: The validated URL.

    Raises:
        ValueError: If the URL's scheme is not `http` or `https`, or if the hostname does not match the origin server.
    """

    parsed_url = urllib.parse.urlparse(next_link)

    # Validate scheme and netloc (domain)
    if parsed_url.scheme not in ["http", "https"]:
        raise ValueError("Invalid URL scheme in `next` link.")
    if not parsed_url.netloc:
        raise ValueError("Invalid URL domain in `next` link.")

    return next_link


def _execute_pagination_request(sanitized_url: str, server: 'FHIRServer') -> 'Bundle':
    """
    Execute the request to retrieve the next page using the sanitized URL via Bundle.read_from.

    Args:
        sanitized_url (str): The sanitized URL to fetch the next page.
        server (FHIRServer): The FHIR server instance to perform the request.

    Returns:
        Bundle: The next page of results as a FHIR Bundle.

    Raises:
        HTTPError: If the request fails due to network issues or server errors.
    """
    from fhirclient.models.bundle import Bundle
    return Bundle.read_from(sanitized_url, server)


def iter_pages(first_bundle: 'Bundle', server: 'FHIRServer') -> Iterator['Bundle']:
    """
    Iterator that yields each page of results as a FHIR Bundle.

    Args:
        first_bundle (Optional[Bundle]): The first Bundle to start pagination.
        server (FHIRServer): The FHIR server instance to perform the request.

    Yields:
        Bundle: Each page of results as a FHIR Bundle.
    """
    # Since _fetch_next_page can return None
    bundle: Optional[Bundle] = first_bundle
    while bundle:
        yield bundle
        bundle = _fetch_next_page(bundle, server)

