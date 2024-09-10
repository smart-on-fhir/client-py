# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DataRequirement).
# 2024, SMART Health IT.


from . import element

class DataRequirement(element.Element):
    """ Describes a required data item.
    
    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """
    
    resource_type = "DataRequirement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeFilter = None
        """ What codes are expected.
        List of `DataRequirementCodeFilter` items (represented as `dict` in JSON). """
        self._codeFilter = None
        """ Primitive extension for codeFilter. Type `FHIRPrimitiveExtension` """
        
        self.dateFilter = None
        """ What dates/date ranges are expected.
        List of `DataRequirementDateFilter` items (represented as `dict` in JSON). """
        self._dateFilter = None
        """ Primitive extension for dateFilter. Type `FHIRPrimitiveExtension` """
        
        self.limit = None
        """ Number of results.
        Type `int`. """
        self._limit = None
        """ Primitive extension for limit. Type `FHIRPrimitiveExtension` """
        
        self.mustSupport = None
        """ Indicates specific structure elements that are referenced by the
        knowledge module.
        List of `str` items. """
        self._mustSupport = None
        """ Primitive extension for mustSupport. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ The profile of the required data.
        List of `str` items. """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        self.sort = None
        """ Order of the results.
        List of `DataRequirementSort` items (represented as `dict` in JSON). """
        self._sort = None
        """ Primitive extension for sort. Type `FHIRPrimitiveExtension` """
        
        self.subjectCodeableConcept = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._subjectCodeableConcept = None
        """ Primitive extension for subjectCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.subjectReference = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subjectReference = None
        """ Primitive extension for subjectReference. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of the required data.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(DataRequirement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirement, self).elementProperties()
        js.extend([
            ("codeFilter", "codeFilter", DataRequirementCodeFilter, True, None, False),
            ("_codeFilter", "_codeFilter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dateFilter", "dateFilter", DataRequirementDateFilter, True, None, False),
            ("_dateFilter", "_dateFilter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("limit", "limit", int, False, None, False),
            ("_limit", "_limit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mustSupport", "mustSupport", str, True, None, False),
            ("_mustSupport", "_mustSupport", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sort", "sort", DataRequirementSort, True, None, False),
            ("_sort", "_sort", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("_subjectCodeableConcept", "_subjectCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("_subjectReference", "_subjectReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DataRequirementCodeFilter(element.Element):
    """ What codes are expected.
    
    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data. Each code
    filter defines an additional constraint on the data, i.e. code filters are
    AND'ed, not OR'ed.
    """
    
    resource_type = "DataRequirementCodeFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ What code is expected.
        List of `Coding` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.path = None
        """ A code-valued attribute to filter on.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        self.searchParam = None
        """ A coded (token) parameter to search on.
        Type `str`. """
        self._searchParam = None
        """ Primitive extension for searchParam. Type `FHIRPrimitiveExtension` """
        
        self.valueSet = None
        """ Valueset for the filter.
        Type `str`. """
        self._valueSet = None
        """ Primitive extension for valueSet. Type `FHIRPrimitiveExtension` """
        
        super(DataRequirementCodeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementCodeFilter, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("path", "path", str, False, None, False),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("_searchParam", "_searchParam", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
            ("_valueSet", "_valueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DataRequirementDateFilter(element.Element):
    """ What dates/date ranges are expected.
    
    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements. Each date filter specifies an
    additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
    """
    
    resource_type = "DataRequirementDateFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ A date-valued attribute to filter on.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        self.searchParam = None
        """ A date valued parameter to search on.
        Type `str`. """
        self._searchParam = None
        """ Primitive extension for searchParam. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ The value of the filter, as a Period, DateTime, or Duration value.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDuration = None
        """ The value of the filter, as a Period, DateTime, or Duration value.
        Type `Duration` (represented as `dict` in JSON). """
        self._valueDuration = None
        """ Primitive extension for valueDuration. Type `FHIRPrimitiveExtension` """
        
        self.valuePeriod = None
        """ The value of the filter, as a Period, DateTime, or Duration value.
        Type `Period` (represented as `dict` in JSON). """
        self._valuePeriod = None
        """ Primitive extension for valuePeriod. Type `FHIRPrimitiveExtension` """
        
        super(DataRequirementDateFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementDateFilter, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, False),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("_searchParam", "_searchParam", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", False),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("_valueDuration", "_valueDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("_valuePeriod", "_valuePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DataRequirementSort(element.Element):
    """ Order of the results.
    
    Specifies the order of the results to be returned.
    """
    
    resource_type = "DataRequirementSort"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.direction = None
        """ ascending | descending.
        Type `str`. """
        self._direction = None
        """ Primitive extension for direction. Type `FHIRPrimitiveExtension` """
        
        self.path = None
        """ The name of the attribute to perform the sort.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        super(DataRequirementSort, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementSort, self).elementProperties()
        js.extend([
            ("direction", "direction", str, False, None, True),
            ("_direction", "_direction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("path", "path", str, False, None, True),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import duration
from . import fhirdatetime
from . import fhirreference
from . import period