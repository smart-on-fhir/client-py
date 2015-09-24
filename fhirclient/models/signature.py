#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Signature) on 2015-09-24.
#  2015, SMART Health IT.


from . import coding
from . import fhirdate
from . import fhirelement
from . import fhirreference


class Signature(fhirelement.FHIRElement):
    """ A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..
    
    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different Signature
    approaches have different utilities.
    """
    
    resource_name = "Signature"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.blob = None
        """ The actual signature content (XML DigSig. JWT, picture, etc.).
        Type `str`. """
        
        self.contentType = None
        """ The technical format of the signature.
        Type `str`. """
        
        self.type = None
        """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.when = None
        """ When the signature was created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.whoReference = None
        """ Who signed the signature.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device, Organization` (represented as `dict` in JSON). """
        
        self.whoUri = None
        """ Who signed the signature.
        Type `str`. """
        
        super(Signature, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("blob", "blob", str, False),
            ("contentType", "contentType", str, False),
            ("type", "type", coding.Coding, True),
            ("when", "when", fhirdate.FHIRDate, False),
            ("whoReference", "whoReference", fhirreference.FHIRReference, False),
            ("whoUri", "whoUri", str, False),
        ])
        return js

