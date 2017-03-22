#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/ContactPoint) on 2017-03-22.
#  2017, SMART Health IT.


from . import element

class ContactPoint(element.Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).
    
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    
    resource_type = "ContactPoint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ Time period when the contact point was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.rank = None
        """ Specify preferred order of use (1 = highest).
        Type `int`. """
        
        self.system = None
        """ phone | fax | email | pager | url | sms | other.
        Type `str`. """
        
        self.use = None
        """ home | work | temp | old | mobile - purpose of this contact point.
        Type `str`. """
        
        self.value = None
        """ The actual contact point details.
        Type `str`. """
        
        super(ContactPoint, self).__init__(jsondict=jsondict, strict=strict)
    
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


import sys
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
