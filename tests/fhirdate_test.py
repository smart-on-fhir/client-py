import datetime
import unittest

from fhirclient.models.fhirabstractbase import FHIRValidationError
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime
from fhirclient.models.patient import Patient
from fhirclient.models.observation import Observation
from fhirclient.models.timing import Timing


class TestFHIRDate(unittest.TestCase):

    def test_empty(self):
        date = FHIRDate()
        self.assertIsNone(date.date)
        self.assertIsNone(date.isostring)
        self.assertIsNone(date.as_json())

    def test_class_hierarchy_backwards_compatibility(self):
        """Confirm that code that calls issubclass(cls, FHIRDate) will still work in >=4.2.0"""
        self.assertTrue(issubclass(FHIRDateTime, FHIRDate))
        self.assertTrue(issubclass(FHIRInstant, FHIRDate))
        self.assertTrue(issubclass(FHIRTime, FHIRDate))

    def test_object_validation(self):
        """Confirm that when constructing an invalid JSON class, we complain"""
        with self.assertRaisesRegex(FHIRValidationError, "Expecting string when initializing"):
            Timing({"event": [1923, "1924"]})
        with self.assertRaisesRegex(FHIRValidationError, "does not match expected format"):
            Patient({"birthDate": "1923-10-11T12:34:56Z"})

    def test_aliases(self):
        """Confirm that we keep the backwards-compatible date alias"""
        # DateTime
        date = FHIRDateTime("2024-01-02")
        self.assertIs(date.datetime, date.date)
        date.date = datetime.datetime(1982, 12, 12)
        self.assertEqual(date.datetime.isoformat(), "1982-12-12T00:00:00")
        self.assertIs(date.datetime, date.date)

        # Instant
        instant = FHIRInstant("2024-01-02T10:11:12Z")
        self.assertIs(instant.datetime, instant.date)
        instant.date = datetime.datetime(1982, 12, 12)
        self.assertEqual(instant.datetime.isoformat(), "1982-12-12T00:00:00")
        self.assertIs(instant.datetime, instant.date)

        # Time
        time = FHIRTime("10:10:10")
        self.assertIs(time.time, time.date)
        time.time = datetime.time(12, 12, 12)
        self.assertEqual(time.time.isoformat(), "12:12:12")
        self.assertIs(time.time, time.date)
        self.assertIsNone(time.origval)

    def test_with_json(self):
        """Confirm we can make objects correctly"""
        self.assertEqual(FHIRDate.with_json_and_owner("2024", None).isostring, "2024-01-01")
        self.assertEqual(FHIRTime.with_json("10:12:14").isostring, "10:12:14")
        self.assertEqual(
            [x.isostring for x in FHIRTime.with_json(["10:12:14", "01:01:01"])],
            ["10:12:14", "01:01:01"]
        )
        with self.assertRaisesRegex(TypeError, "only takes string or list"):
            FHIRDateTime.with_json(2024)

    def test_date(self):
        """
        Verify we parse valid date values.

        From http://hl7.org/fhir/datatypes.html#date:
        - The format is YYYY, YYYY-MM, or YYYY-MM-DD, e.g. 2018, 1973-06, or 1905-08-23.
        - There SHALL be no timezone offset
        """
        # Various happy path strings
        self.assertEqual(FHIRDate("0001").isostring, "0001-01-01")
        self.assertEqual(FHIRDate("2018").isostring, "2018-01-01")
        self.assertEqual(FHIRDate("1973-06").isostring, "1973-06-01")
        self.assertEqual(FHIRDate("1905-08-23").isostring, "1905-08-23")

        # Check that we also correctly provide the date property
        date = FHIRDate("1982").date  # datetime.date
        self.assertIsInstance(date, datetime.date)
        self.assertEqual(date.isoformat(), "1982-01-01")

        # Check that we give back the original input when converting back to as_json()
        self.assertEqual(FHIRDate("1982").as_json(), "1982")

        # Confirm we're used in actual objects
        p = Patient({"birthDate": "1923-10-11"})
        self.assertIsInstance(p.birthDate, FHIRDate)
        self.assertEqual(p.birthDate.isostring, "1923-10-11")

        # Now test a bunch of invalid strings
        self.assertRaises(ValueError, FHIRDate, "82")
        self.assertRaises(ValueError, FHIRDate, "82/07/23")
        self.assertRaises(ValueError, FHIRDate, "07-23-1982")
        self.assertRaises(ValueError, FHIRDate, "13:28:17")
        self.assertRaises(ValueError, FHIRDate, "2015-02-07T13:28:17-05:00")

    def test_datetime(self):
        """
        Verify we parse valid datetime values.

        From http://hl7.org/fhir/datatypes.html#datetime:
        - The format is YYYY, YYYY-MM, YYYY-MM-DD or YYYY-MM-DDThh:mm:ss+zz:zz
        - e.g. 2018, 1973-06, 1905-08-23, 2015-02-07T13:28:17-05:00 or 2017-01-01T00:00:00.000Z
        - If hours and minutes are specified, a timezone offset SHALL be populated
        - Seconds must be provided due to schema type constraints
          but may be zero-filled and may be ignored at receiver discretion.
        - Milliseconds are optionally allowed (the spec's regex actually allows arbitrary
          sub-second precision)
        """
        # Various happy path strings
        self.assertEqual(FHIRDateTime("2018").isostring, "2018-01-01T00:00:00")
        self.assertEqual(FHIRDateTime("1973-06").isostring, "1973-06-01T00:00:00")
        self.assertEqual(FHIRDateTime("1905-08-23").isostring, "1905-08-23T00:00:00")
        self.assertEqual(
            FHIRDateTime("2015-02-07T13:28:17-05:00").isostring, "2015-02-07T13:28:17-05:00"
        )
        self.assertEqual(
            FHIRDateTime("2017-01-01T00:00:00.123456Z").isostring,
            "2017-01-01T00:00:00.123456+00:00"
        )
        self.assertEqual(  # leap second
            FHIRDateTime("2015-02-07T13:28:60Z").isostring, "2015-02-07T13:28:59+00:00"
        )

        # Check that we also correctly provide the date property
        self.assertIsInstance(FHIRDateTime("2015").date, datetime.datetime)
        self.assertIsInstance(FHIRDateTime("2015-02-07").date, datetime.datetime)
        self.assertIsInstance(FHIRDateTime("2015-02-07T13:28:17Z").date, datetime.datetime)

        # Check that we give back the original input when converting back to as_json()
        self.assertEqual(FHIRDateTime("1982").as_json(), "1982")

        # Confirm we're used in actual objects
        p = Patient({"deceasedDateTime": "1923-10-11"})
        self.assertIsInstance(p.deceasedDateTime, FHIRDateTime)
        self.assertEqual(p.deceasedDateTime.isostring, "1923-10-11T00:00:00")

        # Now test a bunch of invalid strings
        self.assertRaises(ValueError, FHIRDateTime, "82")
        self.assertRaises(ValueError, FHIRDateTime, "82/07/23")
        self.assertRaises(ValueError, FHIRDateTime, "07-23-1982")
        self.assertRaises(ValueError, FHIRDateTime, "13:28:17")
        self.assertRaises(ValueError, FHIRDateTime, "2015-02-07T13:28")  # no seconds
        self.assertRaises(ValueError, FHIRDateTime, "2015-02-07T13:28:17")  # no timezone

    def test_instant(self):
        """
        Verify we parse valid instant values.

        From http://hl7.org/fhir/datatypes.html#instant:
        - The format is YYYY-MM-DDThh:mm:ss.sss+zz:zz
        - e.g. 2015-02-07T13:28:17.239+02:00 or 2017-01-01T00:00:00Z
        - The time SHALL be specified at least to the second and SHALL include a time zone.
        """
        # Various happy path strings
        self.assertEqual(
            FHIRInstant("2015-02-07T13:28:17-05:00").isostring, "2015-02-07T13:28:17-05:00"
        )
        self.assertEqual(
            FHIRInstant("2017-01-01T00:00:00.123456Z").isostring,
            "2017-01-01T00:00:00.123456+00:00"
        )
        self.assertEqual(  # leap second
            FHIRInstant("2017-01-01T00:00:60Z").isostring, "2017-01-01T00:00:59+00:00"
        )

        # Check that we also correctly provide the date property
        self.assertIsInstance(FHIRInstant("2015-02-07T13:28:17Z").date, datetime.datetime)

        # Check that we give back the original input when converting back to as_json()
        self.assertEqual(
            FHIRInstant("2017-01-01T00:00:00Z").as_json(),
            "2017-01-01T00:00:00Z"  # Z instead of +00.00
        )

        # Confirm we're used in actual objects
        obs = Observation({
            "issued": "2017-01-01T00:00:00.123Z",
            "status": "X",
            "code": {"text": "X"}},
        )
        self.assertIsInstance(obs.issued, FHIRInstant)
        self.assertEqual(obs.issued.isostring, "2017-01-01T00:00:00.123000+00:00")

        # Now test a bunch of invalid strings
        self.assertRaises(ValueError, FHIRInstant, "82")
        self.assertRaises(ValueError, FHIRInstant, "82/07/23")
        self.assertRaises(ValueError, FHIRInstant, "07-23-1982")
        self.assertRaises(ValueError, FHIRInstant, "13:28:17")
        self.assertRaises(ValueError, FHIRInstant, "2015")
        self.assertRaises(ValueError, FHIRInstant, "2015-02-07")
        self.assertRaises(ValueError, FHIRInstant, "2015-02-07T13:28")  # no seconds
        self.assertRaises(ValueError, FHIRInstant, "2015-02-07T13:28:17")  # no timezone

    def test_time(self):
        """
        Verify we parse valid time values.

        From http://hl7.org/fhir/datatypes.html#time:
        - The format is hh:mm:ss
        - A timezone offset SHALL NOT be present
        - Uses 24-hour time
        - Sub-seconds allowed (to arbitrary precision, per the regex...)
        """
        # Various happy path strings
        self.assertEqual(FHIRTime("13:28:17").isostring, "13:28:17")
        self.assertEqual(FHIRTime("13:28:17.123456").isostring, "13:28:17.123456")
        self.assertEqual(FHIRTime("00:00:60").isostring, "00:00:59")  # leap second

        # Check that we also correctly provide the date property (though it's a misnomer)
        self.assertIsInstance(FHIRTime("13:28:17").date, datetime.time)

        # Check that we give back the original input when converting back to as_json()
        self.assertEqual(FHIRTime("00:00:00").as_json(), "00:00:00")

        # Confirm we're used in actual objects
        obs = Observation({"valueTime": "14:49:32", "status": "X", "code": {"text": "X"}})
        self.assertIsInstance(obs.valueTime, FHIRTime)
        self.assertEqual(obs.valueTime.isostring, "14:49:32")

        # Now test a bunch of invalid strings
        self.assertRaises(ValueError, FHIRTime, "82")
        self.assertRaises(ValueError, FHIRTime, "82/07/23")
        self.assertRaises(ValueError, FHIRTime, "07-23-1982")
        self.assertRaises(ValueError, FHIRTime, "2015")
        self.assertRaises(ValueError, FHIRTime, "2015-02-07T13:28:17Z")
        self.assertRaises(ValueError, FHIRTime, "10:12")
