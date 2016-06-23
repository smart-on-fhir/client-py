#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Money) on 2016-06-23.
#  2016, SMART Health IT.


from . import quantity

class Money(quantity.Quantity):
    """ An amount of money. With regard to precision, see [Decimal
    Precision](datatypes.html#precision).
    
    There SHALL be a code if there is a value and it SHALL be an expression of
    currency.  If system is present, it SHALL be ISO 4217 (system =
    "urn:iso:std:iso:4217" - currency).
    """
    
    resource_name = "Money"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        super(Money, self).__init__(jsondict=jsondict, strict=strict)


