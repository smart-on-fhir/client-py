#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Signature) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import fhirdate
import fhirelement
import fhirreference


class Signature(fhirelement.FHIRElement):
    """ An XML digital Signature.
    
    An XML digital signature along with supporting context.
    """
    
    resource_name = "Signature"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.blob = None
        """ The actual XML Dig-Sig.
        Type `str`. """
        
        self.type = None
        """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.when = None
        """ When the signature was created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.whoReference = None
        """ Who signed the signature.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient` (represented as `dict` in JSON). """
        
        self.whoUri = None
        """ Who signed the signature.
        Type `str`. """
        
        super(Signature, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Signature, self).update_with_json(jsondict)
        if 'blob' in jsondict:
            self.blob = jsondict['blob']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)
        if 'when' in jsondict:
            self.when = fhirdate.FHIRDate.with_json_and_owner(jsondict['when'], self)
        if 'whoReference' in jsondict:
            self.whoReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['whoReference'], self)
        if 'whoUri' in jsondict:
            self.whoUri = jsondict['whoUri']

