"""Facilitate working with FHIR dates and times."""
# 2014-2024, SMART Health IT.

import datetime
import re
from typing import Any, Union


class FHIRDate:
    """
    A convenience class for working with FHIR dates in Python.

    http://hl7.org/fhir/R4/datatypes.html#date

    Converting to a Python representation does require some compromises:
    - This class will convert partial dates ("reduced precision dates") like "2024" into full
      dates using the earliest possible time (in this example, "2024-01-01") because Python's
      date class does not support partial dates.

    If such compromise is not useful for you, avoid using the `date` or `isostring`
    properties and just use the `as_json()` method in order to work with the original,
    exact string.

    For backwards-compatibility reasons, this class is the parent class of FHIRDateTime,
    FHIRInstant, and FHIRTime. But they are all separate concepts and in a future major release,
    they should be split into entirely separate classes.

    Public properties:
    - `date`: datetime.date representing the JSON value
    - `isostring`: an ISO 8601 string version of the above Python object

    Public methods:
    - `as_json`: returns the original JSON used to construct the instance
    """

    def __init__(self, jsonval: Union[str, None] = None):
        self.date: Union[datetime.date, datetime.datetime, datetime.time, None] = None

        if jsonval is not None:
            if not isinstance(jsonval, str):
                raise TypeError("Expecting string when initializing {}, but got {}"
                    .format(type(self), type(jsonval)))
            if not self._REGEX.fullmatch(jsonval):
                raise ValueError("does not match expected format")
            self.date = self._from_string(jsonval)

        self.origval: Union[str, None] = jsonval

    def __setattr__(self, prop, value):
        if prop in {'date', self._FIELD}:
            self.origval = None
            # Keep these two fields in sync
            object.__setattr__(self, self._FIELD, value)
            object.__setattr__(self, "date", value)
        else:
            object.__setattr__(self, prop, value)

    @property
    def isostring(self) -> Union[str, None]:
        """
        Returns a standardized ISO 8601 version of the Python representation of the FHIR JSON.

        Note that this may not be a fully accurate version of the input JSON.
        In particular, it will convert partial dates like "2024" to full dates like "2024-01-01".
        It will also normalize the timezone, if present.
        """
        if self.date is None:
            return None
        return self.date.isoformat()

    @classmethod
    def with_json(cls, jsonobj: Union[str, list]):
        """ Initialize a date from an ISO date string.
        """
        if isinstance(jsonobj, str):
            return cls(jsonobj)

        if isinstance(jsonobj, list):
            return [cls(jsonval) for jsonval in jsonobj]

        raise TypeError("`cls.with_json()` only takes string or list of strings, but you provided {}"
            .format(type(jsonobj)))

    @classmethod
    def with_json_and_owner(cls, jsonobj: Union[str, list], owner):
        """ Added for compatibility reasons to FHIRElement; "owner" is
        discarded.
        """
        return cls.with_json(jsonobj)

    def as_json(self) -> Union[str, None]:
        """Returns the original JSON string used to create this instance."""
        if self.origval is not None:
            return self.origval
        return self.isostring

    ##################################
    # Private properties and methods #
    ##################################

    # Pulled from spec for date
    _REGEX = re.compile(r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)(-(0[1-9]|1[0-2])(-(0[1-9]|[1-2][0-9]|3[0-1]))?)?")
    _FIELD = "date"

    @staticmethod
    def _parse_partial(value: str, cls):
        """
        Handle partial dates like 1970 or 1980-12.

        FHIR allows them, but Python's datetime classes do not natively parse them.
        """
        # Note that `value` has already been regex-certified by this point,
        # so we don't have to handle really wild strings.
        if len(value) < 10:
            pieces = value.split("-")
            if len(pieces) == 1:
                return cls(int(pieces[0]), 1, 1)
            else:
                return cls(int(pieces[0]), int(pieces[1]), 1)
        return cls.fromisoformat(value)

    @staticmethod
    def _parse_date(value: str) -> datetime.date:
        return FHIRDate._parse_partial(value, datetime.date)

    @staticmethod
    def _parse_datetime(value: str) -> datetime.datetime:
        # Until we depend on Python 3.11+, manually handle Z
        value = value.replace("Z", "+00:00")
        value = FHIRDate._strip_leap_seconds(value)
        return FHIRDate._parse_partial(value, datetime.datetime)

    @staticmethod
    def _parse_time(value: str) -> datetime.time:
        value = FHIRDate._strip_leap_seconds(value)
        return datetime.time.fromisoformat(value)

    @staticmethod
    def _strip_leap_seconds(value: str) -> str:
        """
        Manually ignore leap seconds by clamping the seconds value to 59.

        Python native times don't support them (at the time of this writing, but also watch
        https://bugs.python.org/issue23574). For example, the stdlib's datetime.fromtimestamp()
        also clamps to 59 if the system gives it leap seconds.

        But FHIR allows leap seconds and says receiving code SHOULD accept them,
        so we should be graceful enough to at least not throw a ValueError,
        even though we can't natively represent the most-correct time.
        """
        # We can get away with such relaxed replacement because we are already regex-certified
        # and ":60" can't show up anywhere but seconds.
        return value.replace(":60", ":59")

    @staticmethod
    def _from_string(value: str) -> Any:
        return FHIRDate._parse_date(value)
