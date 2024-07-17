"""Facilitate working with FHIR time fields."""
# 2024, SMART Health IT.

import datetime
import re
from typing import Any, Union

from .fhirdate import FHIRDate


# This inherits from FHIRDate as a matter of backwards compatibility.
# (in case anyone was doing isinstance(obj, FHIRDate))
# Next time we bump the major version, we can stop that and also drop the
# backwards-compatible 'date' alias. R4-QUIRK

class FHIRInstant(FHIRDate):
    """
    A convenience class for working with FHIR instants in Python.

    http://hl7.org/fhir/R4/datatypes.html#instant

    Converting to a Python representation does require some compromises:
    - FHIR allows arbitrary sub-second precision, but Python only holds microseconds.
    - Leap seconds (:60) will be changed to the 59th second (:59) because Python's time classes
      do not support leap seconds.

    If such compromise is not useful for you, avoid using the `date`, `datetime`, or `isostring`
    properties and just use the `as_json()` method in order to work with the original,
    exact string.

    Public properties:
    - `datetime`: datetime.datetime representing the JSON value (aware only)
    - `date`: backwards-compatibility alias for `datetime`
    - `isostring`: an ISO 8601 string version of the above Python object

    Public methods:
    - `as_json`: returns the original JSON used to construct the instance
    """

    def __init__(self, jsonval: Union[str, None] = None):
        self.datetime: Union[datetime.datetime, None] = None
        super().__init__(jsonval)

    ##################################
    # Private properties and methods #
    ##################################

    # Pulled from spec for instant
    _REGEX = re.compile(r"([0-9]([0-9]([0-9][1-9]|[1-9]0)|[1-9]00)|[1-9]000)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])T([01][0-9]|2[0-3]):[0-5][0-9]:([0-5][0-9]|60)(\.[0-9]+)?(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))")
    _FIELD = "datetime"

    @staticmethod
    def _from_string(value: str) -> Any:
        return FHIRDate._parse_datetime(value)
