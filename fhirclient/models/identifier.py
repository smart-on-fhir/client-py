#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Identifier) on 2017-03-22.
#  2017, SMART Health IT.


from . import element

class Identifier(element.Element):
    """ An identifier intended for computation.
    
    A technical identifier - identifies some entity uniquely and unambiguously.
    """
    
    resource_type = "Identifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assigner = None
        """ Organization that issued id (may be just text).
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period when id is/was valid for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.system = None
        """ The namespace for the identifier value.
        Type `str`. """
        
        self.type = None
        """ Description of identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        """ usual | official | temp | secondary (If known).
        Type `str`. """
        
        self.value = None
        """ The value that is unique.
        Type `str`. """
        
        super(Identifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Identifier, self).elementProperties()
        js.extend([
            ("assigner", "assigner", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("system", "system", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("use", "use", str, False, None, False),
            ("value", "value", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
