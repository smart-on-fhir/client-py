#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/DataRequirement) on 2017-03-22.
#  2017, SMART Health IT.


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
        
        self.mustSupport = None
        """ Indicates that specific structure elements are referenced by the
        knowledge module.
        List of `str` items. """
        
        self.profile = None
        """ The profile of the required data.
        List of `str` items. """
        
        self.type = None
        """ The type of the required data.
        Type `str`. """
        
        super(DataRequirement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirement, self).elementProperties()
        js.extend([
            ("codeFilter", "codeFilter", DataRequirementCodeFilter, True, None, False),
            ("dateFilter", "dateFilter", DataRequirementDateFilter, True, None, False),
            ("mustSupport", "mustSupport", str, True, None, False),
            ("profile", "profile", str, True, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class DataRequirementCodeFilter(element.Element):
    """ What codes are expected.
    
    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data.
    """
    
    resource_type = "DataRequirementCodeFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ The code-valued attribute of the filter.
        Type `str`. """
        
        self.valueCode = None
        """ What code is expected.
        List of `str` items. """
        
        self.valueCodeableConcept = None
        """ What CodeableConcept is expected.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ What Coding is expected.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.valueSetReference = None
        """ Valueset for the filter.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.valueSetString = None
        """ Valueset for the filter.
        Type `str`. """
        
        super(DataRequirementCodeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementCodeFilter, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("valueCode", "valueCode", str, True, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("valueCoding", "valueCoding", coding.Coding, True, None, False),
            ("valueSetReference", "valueSetReference", fhirreference.FHIRReference, False, "valueSet", False),
            ("valueSetString", "valueSetString", str, False, "valueSet", False),
        ])
        return js


class DataRequirementDateFilter(element.Element):
    """ What dates/date ranges are expected.
    
    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements.
    """
    
    resource_type = "DataRequirementDateFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ The date-valued attribute of the filter.
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
            ("path", "path", str, False, None, True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
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
