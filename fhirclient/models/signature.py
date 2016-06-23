#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Signature) on 2016-06-23.
#  2016, SMART Health IT.


from . import element

class Signature(element.Element):
    """ A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..
    
    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different Signature
    approaches have different utilities.
    """
    
    resource_name = "Signature"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(Signature, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("blob", "blob", str, False, None, True),
            ("contentType", "contentType", str, False, None, True),
            ("type", "type", coding.Coding, True, None, True),
            ("when", "when", fhirdate.FHIRDate, False, None, True),
            ("whoReference", "whoReference", fhirreference.FHIRReference, False, "who", True),
            ("whoUri", "whoUri", str, False, "who", True),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
