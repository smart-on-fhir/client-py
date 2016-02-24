#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Annotation) on 2016-02-24.
#  2016, SMART Health IT.


from . import element

class Annotation(element.Element):
    """ Text node with attribution.
    
    A  text note which also  contains information about who made the statement
    and when.
    """
    
    resource_name = "Annotation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(Annotation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend([
            ("authorReference", "authorReference", fhirreference.FHIRReference, False),
            ("authorString", "authorString", str, False),
            ("text", "text", str, False),
            ("time", "time", fhirdate.FHIRDate, False),
        ])
        return js


from . import fhirdate
from . import fhirreference
