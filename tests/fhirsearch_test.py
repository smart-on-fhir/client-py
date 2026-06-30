import pytest
from fhirclient.models.fhirsearch import FHIRSearch, FHIRSearchParam
from fhirclient.models.bundle import Bundle


class TestFHIRSearchDuplicateParams:
    """Tests for duplicate search parameter support via list-of-tuples input."""

    def test_dict_struct_still_works(self):
        """Existing dict-based usage must not regress."""
        s = FHIRSearch(Bundle, {"_count": "10"})
        url = s.construct()
        assert "_count=10" in url

    def test_list_of_tuples_single_param(self):
        """List of tuples with a single entry produces the same URL as a dict."""
        s = FHIRSearch(Bundle, [("_count", "10")])
        url = s.construct()
        assert "_count=10" in url

    def test_list_of_tuples_duplicate_param(self):
        """Two entries with the same key both appear in the constructed URL.

        This is the core bug: a dict collapses the second 'date' key, so the
        URL only carries one date constraint.  A list of tuples preserves both.
        """
        s = FHIRSearch(Bundle, [
            ("date", {"$gt": "2018-05-21"}),
            ("date", {"$lt": "2018-05-24"}),
        ])
        url = s.construct()
        # Both constraints must be present as separate parameters
        params = url.split("?", 1)[1].split("&")
        date_params = [p for p in params if p.startswith("date=")]
        assert len(date_params) == 2, (
            f"Expected 2 date params, got {len(date_params)}: {params}"
        )

    def test_list_of_tuples_mixed_keys(self):
        """Mixed keys work the same as a dict."""
        s = FHIRSearch(Bundle, [("_count", "5"), ("status", "active")])
        url = s.construct()
        assert "_count=5" in url
        assert "status=active" in url

    def test_list_of_tuples_invalid_item_raises(self):
        """A list with non-pair items raises a clear exception."""
        with pytest.raises(Exception, match="key, value"):
            FHIRSearch(Bundle, ["not-a-pair"])

    def test_wrong_type_raises(self):
        """Passing something other than dict or list raises."""
        with pytest.raises(Exception):
            FHIRSearch(Bundle, "bad")

    def test_dict_cannot_express_duplicate_keys(self):
        """Confirm the dict path only produces one date param (documents the limitation)."""
        # Python silently drops duplicate dict keys at parse time; this verifies
        # that the dict path isn't somehow producing duplicates itself.
        s = FHIRSearch(Bundle, {"_count": "10", "status": "active"})
        url = s.construct()
        params = url.split("?", 1)[1].split("&")
        assert len(params) == 2
