import unittest
from unittest.mock import MagicMock

from fhirclient.models.bundle import Bundle


class TestBundleIterator(unittest.TestCase):

    def test_bundle_iter_and_next(self):
        entry1 = MagicMock()
        entry2 = MagicMock()
        bundle = Bundle()
        bundle.entry = [entry1, entry2]

        iterator = iter(bundle)
        first_entry = next(iterator)
        second_entry = next(iterator)

        self.assertEqual(first_entry, entry1)
        self.assertEqual(second_entry, entry2)
        with self.assertRaises(StopIteration):
            next(iterator)
