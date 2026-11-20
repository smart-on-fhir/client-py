import unittest

from fhirclient.models.fhirsearch import FHIRSearch
from fhirclient.models.patient import Patient
from fhirclient.models.task import Task


class TestFHIRSearchInclude(unittest.TestCase):
    def test_include_renamed_search_parameter(self):
        search = FHIRSearch(Task).include("subject")
        self.assertEqual(search.construct(), "Task?_include=Task:subject")

    def test_revinclude_renamed_search_parameter(self):
        search = FHIRSearch(Patient).include("subject", Task, reverse=True)
        self.assertEqual(search.construct(), "Patient?_revinclude=Task:subject")
