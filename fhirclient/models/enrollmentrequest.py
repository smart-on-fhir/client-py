#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10061 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2016-10-24.
#  2016, SMART Health IT.


from . import domainresource

class EnrollmentRequest(domainresource.DomainResource):
    """ Enrollment request.
    
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    
    resource_name = "EnrollmentRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurerIdentifier = None
        """ Target.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.insurerReference = None
        """ Target.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.organizationIdentifier = None
        """ Responsible organization.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organizationReference = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.providerIdentifier = None
        """ Responsible practitioner.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.providerReference = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.subjectIdentifier = None
        """ The subject of the Products and Services.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(EnrollmentRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurerIdentifier", "insurerIdentifier", identifier.Identifier, False, "insurer", False),
            ("insurerReference", "insurerReference", fhirreference.FHIRReference, False, "insurer", False),
            ("organizationIdentifier", "organizationIdentifier", identifier.Identifier, False, "organization", False),
            ("organizationReference", "organizationReference", fhirreference.FHIRReference, False, "organization", False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("providerIdentifier", "providerIdentifier", identifier.Identifier, False, "provider", False),
            ("providerReference", "providerReference", fhirreference.FHIRReference, False, "provider", False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectIdentifier", "subjectIdentifier", identifier.Identifier, False, "subject", True),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", True),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
