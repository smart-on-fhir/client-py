#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Annotation) on 2015-09-24.
#  2015, SMART Health IT.


from . import fhirdate
from . import fhirelement
from . import fhirreference


class Annotation(fhirelement.FHIRElement):
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

