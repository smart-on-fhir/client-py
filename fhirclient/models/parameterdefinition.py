#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2017-01-15.
#  2017, SMART Health IT.


from . import element

class ParameterDefinition(element.Element):
    """ Definition of a parameter to a module.
    
    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """
    
    resource_type = "ParameterDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ A brief description of the parameter.
        Type `str`. """
        
        self.max = None
        """ Maximum cardinality (a number of *).
        Type `str`. """
        
        self.min = None
        """ Minimum cardinality.
        Type `int`. """
        
        self.name = None
        """ Parameter name.
        Type `str`. """
        
        self.profile = None
        """ The profile of the parameter, any.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type for the parameter.
        Type `str`. """
        
        self.use = None
        """ input | output.
        Type `str`. """
        
        super(ParameterDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ParameterDefinition, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("name", "name", str, False, None, False),
            ("profile", "profile", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js


from . import fhirreference
