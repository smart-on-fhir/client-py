#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Money) on 2019-10-12.
#  2019, SMART Health IT.


from . import quantity

class Money(quantity.Quantity):
    """ An amount of money. With regard to precision, see [Decimal
    Precision](datatypes.html#precision).
    
    There SHALL be a code if there is a value and it SHALL be an expression of
    currency.  If system is present, it SHALL be ISO 4217 (system =
    "urn:iso:std:iso:4217" - currency).
    """
    
    resource_name = "Money"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Money, self).__init__(jsondict)


