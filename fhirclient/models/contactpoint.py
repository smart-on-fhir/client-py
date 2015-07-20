#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ContactPoint) on 2015-07-06.
#  2015, SMART Health IT.


from . import fhirelement
from . import period


class ContactPoint(fhirelement.FHIRElement):
    """ Details of a Technology mediated contact point (phone, fax, email, etc).
    
    Details for All kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    
    resource_name = "ContactPoint"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.period = None
        """ Time period when the contact point was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.system = None
        """ phone | fax | email | url.
        Type `str`. """
        
        self.use = None
        """ home | work | temp | old | mobile - purpose of this contact point.
        Type `str`. """
        
        self.value = None
        """ The actual contact point details.
        Type `str`. """
        
        super(ContactPoint, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ContactPoint, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False),
            ("system", "system", str, False),
            ("use", "use", str, False),
            ("value", "value", str, False),
        ])
        return js

