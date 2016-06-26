#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8595 (http://hl7.org/fhir/StructureDefinition/UsageContext) on 2016-06-26.
#  2016, SMART Health IT.


from . import element

class UsageContext(element.Element):
    """ Describes the context of use for a module.
    
    Specifies various attributes of the patient population for whom and/or
    environment of care in which a knowledge module is applicable.
    """
    
    resource_name = "UsageContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.focus = None
        """ patient-gender | patient-age-group | clinical-focus | target-user |
        workflow-setting | workflow-task | clinical-venue | jurisdiction.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Value of the usage attribute.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(UsageContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(UsageContext, self).elementProperties()
        js.extend([
            ("focus", "focus", coding.Coding, False, None, True),
            ("value", "value", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import codeableconcept
from . import coding
