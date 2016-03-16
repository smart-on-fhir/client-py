#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2016-03-16.
#  2016, SMART Health IT.


from . import element

class ParameterDefinition(element.Element):
    """ Definition of a parameter to a module.
    
    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """
    
    resource_name = "ParameterDefinition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        """ None.
        Type `str`. """
        
        self.use = None
        """ None.
        Type `str`. """
        
        super(ParameterDefinition, self).__init__(jsondict)
    
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
