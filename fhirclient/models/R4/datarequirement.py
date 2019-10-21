#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DataRequirement) on 2019-05-07.
#  2019, SMART Health IT.


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
        
        self.dateFilter = None
        """ What dates/date ranges are expected.
        List of `DataRequirementDateFilter` items (represented as `dict` in JSON). """
        
        self.limit = None
        """ Number of results.
        Type `int`. """
        
        self.mustSupport = None
        """ Indicates specific structure elements that are referenced by the
        knowledge module.
        List of `str` items. """
        
        self.profile = None
        """ The profile of the required data.
        List of `str` items. """
        
        self.sort = None
        """ Order of the results.
        List of `DataRequirementSort` items (represented as `dict` in JSON). """
        
        self.subjectCodeableConcept = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of the required data.
        Type `str`. """
        
        super(DataRequirement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirement, self).elementProperties()
        js.extend([
            ("codeFilter", "codeFilter", DataRequirementCodeFilter, True, None, False),
            ("dateFilter", "dateFilter", DataRequirementDateFilter, True, None, False),
            ("limit", "limit", int, False, None, False),
            ("mustSupport", "mustSupport", str, True, None, False),
            ("profile", "profile", str, True, None, False),
            ("sort", "sort", DataRequirementSort, True, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("type", "type", str, False, None, True),
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
        
        self.path = None
        """ A code-valued attribute to filter on.
        Type `str`. """
        
        self.searchParam = None
        """ A coded (token) parameter to search on.
        Type `str`. """
        
        self.valueSet = None
        """ Valueset for the filter.
        Type `str`. """
        
        super(DataRequirementCodeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementCodeFilter, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, True, None, False),
            ("path", "path", str, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
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
        
        self.searchParam = None
        """ A date valued parameter to search on.
        Type `str`. """
        
        self.valueDateTime = None
        """ The value of the filter, as a Period, DateTime, or Duration value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDuration = None
        """ The value of the filter, as a Period, DateTime, or Duration value.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ The value of the filter, as a Period, DateTime, or Duration value.
        Type `Period` (represented as `dict` in JSON). """
        
        super(DataRequirementDateFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementDateFilter, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
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
        
        self.path = None
        """ The name of the attribute to perform the sort.
        Type `str`. """
        
        super(DataRequirementSort, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementSort, self).elementProperties()
        js.extend([
            ("direction", "direction", str, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
