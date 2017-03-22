#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Annotation) on 2017-03-22.
#  2017, SMART Health IT.


from . import element

class Annotation(element.Element):
    """ Text node with attribution.
    
    A  text note which also  contains information about who made the statement
    and when.
    """
    
    resource_type = "Annotation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorReference = None
        """ Individual responsible for the annotation.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.authorString = None
        """ Individual responsible for the annotation.
        Type `str`. """
        
        self.text = None
        """ The annotation  - text content.
        Type `str`. """
        
        self.time = None
        """ When the annotation was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Annotation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend([
            ("authorReference", "authorReference", fhirreference.FHIRReference, False, "author", False),
            ("authorString", "authorString", str, False, "author", False),
            ("text", "text", str, False, None, True),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
