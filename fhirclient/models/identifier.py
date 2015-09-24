#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Identifier) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import fhirelement
from . import fhirreference
from . import period


class Identifier(fhirelement.FHIRElement):
    """ An identifier intended for computation.
    
    A technical identifier - identifies some entity uniquely and unambiguously.
    """
    
    resource_name = "Identifier"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.assigner = None
        """ Organization that issued id (may be just text).
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period when id is/was valid for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.system = None
        """ The namespace for the identifier.
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
        
        super(Identifier, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Identifier, self).elementProperties()
        js.extend([
            ("assigner", "assigner", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("system", "system", str, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
            ("use", "use", str, False),
            ("value", "value", str, False),
        ])
        return js

