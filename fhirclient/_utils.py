import urllib
from typing import Optional, Iterable

import requests

from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from fhirclient.models.bundle import Bundle


# Use forward references to avoid circular imports
def _fetch_next_page(bundle: 'Bundle') -> Optional['Bundle']:
    """
    Fetch the next page of results using the `next` link provided in the bundle.

    Args:
        bundle (Bundle): The FHIR Bundle containing the `next` link.

    Returns:
        Optional[Bundle]: The next page of results as a FHIR Bundle, or None if no "next" link is found.
    """
    next_link = _get_next_link(bundle)
    if next_link:
        sanitized_next_link = _sanitize_next_link(next_link)
        return _execute_pagination_request(sanitized_next_link)
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
            return link.url
    return None


def _sanitize_next_link(next_link: str) -> str:
    """
    Sanitize the `next` link to ensure it is safe to use.

    Args:
        next_link (str): The raw `next` link URL.

    Returns:
        str: The sanitized URL.

    Raises:
        ValueError: If the URL scheme or domain is invalid.
    """
    parsed_url = urllib.parse.urlparse(next_link)

    # Validate scheme and netloc (domain)
    if parsed_url.scheme not in ["http", "https"]:
        raise ValueError("Invalid URL scheme in `next` link.")
    if not parsed_url.netloc:
        raise ValueError("Invalid URL domain in `next` link.")

    # Additional sanitization if necessary, e.g., removing dangerous query parameters
    query_params = urllib.parse.parse_qs(parsed_url.query)
    sanitized_query = {k: v for k, v in query_params.items()}

    # Rebuild the sanitized URL
    sanitized_url = urllib.parse.urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            urllib.parse.urlencode(sanitized_query, doseq=True),
            parsed_url.fragment,
        )
    )

    return sanitized_url


def _execute_pagination_request(sanitized_url: str) -> Optional['Bundle']:
    """
    Execute the request to retrieve the next page using the sanitized URL.

    Args:
        sanitized_url (str): The sanitized URL to fetch the next page.

    Returns:
        Optional[Bundle]: The next page of results as a FHIR Bundle, or None.

    Raises:
        HTTPError: If the request fails due to network issues or server errors.
    """
    from fhirclient.models.bundle import Bundle  # Import here to avoid circular import

    try:
        # Use requests.get directly to make the HTTP request
        response = requests.get(sanitized_url)
        response.raise_for_status()
        next_bundle_data = response.json()
        next_bundle = Bundle(next_bundle_data)

        return next_bundle

    except requests.exceptions.HTTPError as e:
        # Handle specific HTTP errors as needed, possibly including retry logic
        raise e


def iter_pages(first_bundle: 'Bundle') -> Iterable['Bundle']:
    """
    Iterator that yields each page of results as a FHIR Bundle.

    Args:
        first_bundle (Optional[Bundle]): The first Bundle to start pagination.

    Yields:
        Bundle: Each page of results as a FHIR Bundle.
    """
    # Since _fetch_next_page can return None
    bundle: Optional[Bundle] = first_bundle
    while bundle:
        yield bundle
        bundle = _fetch_next_page(bundle)

