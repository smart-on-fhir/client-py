#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ContactPoint) on 2019-10-12.
#  2019, SMART Health IT.


from . import element

class ContactPoint(element.Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).
    
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    
    resource_name = "ContactPoint"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.period = None
        """ Time period when the contact point was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.rank = None
        """ Specify preferred order of use (1 = highest).
        Type `int`. """
        
        self.system = None
        """ phone | fax | email | pager | other.
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
            ("period", "period", period.Period, False, None, False),
            ("rank", "rank", int, False, None, False),
            ("system", "system", str, False, None, False),
            ("use", "use", str, False, None, False),
            ("value", "value", str, False, None, False),
        ])
        return js


from . import period
