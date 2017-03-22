#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/BodySite) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class BodySite(domainresource.DomainResource):
    """ Specific and identified anatomical location.
    
    Record details about the anatomical location of a specimen or body part.
    This resource may be used when a coded concept does not provide the
    necessary detail needed for the use case.
    """
    
    resource_type = "BodySite"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this body site record is in active use.
        Type `bool`. """
        
        self.code = None
        """ Named anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Anatomical location description.
        Type `str`. """
        
        self.identifier = None
        """ Bodysite identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.image = None
        """ Attached images.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who this is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.qualifier = None
        """ Modification to location code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(BodySite, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BodySite, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("qualifier", "qualifier", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
