#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse) on 2016-08-31.
#  2016, SMART Health IT.


from . import domainresource

class EnrollmentResponse(domainresource.DomainResource):
    """ EnrollmentResponse resource.
    
    This resource provides enrollment and plan details from the processing of
    an Enrollment resource.
    """
    
    resource_name = "EnrollmentResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organizationIdentifier = None
        """ Insurer.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organizationReference = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error | partial.
        Type `str`. """
        
        self.requestIdentifier = None
        """ Claim reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestOrganizationIdentifier = None
        """ Responsible organization.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestOrganizationReference = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProviderIdentifier = None
        """ Responsible practitioner.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestProviderReference = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.requestReference = None
        """ Claim reference.
        Type `FHIRReference` referencing `EnrollmentRequest` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(EnrollmentResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organizationIdentifier", "organizationIdentifier", identifier.Identifier, False, "organization", False),
            ("organizationReference", "organizationReference", fhirreference.FHIRReference, False, "organization", False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, "request", False),
            ("requestOrganizationIdentifier", "requestOrganizationIdentifier", identifier.Identifier, False, "requestOrganization", False),
            ("requestOrganizationReference", "requestOrganizationReference", fhirreference.FHIRReference, False, "requestOrganization", False),
            ("requestProviderIdentifier", "requestProviderIdentifier", identifier.Identifier, False, "requestProvider", False),
            ("requestProviderReference", "requestProviderReference", fhirreference.FHIRReference, False, "requestProvider", False),
            ("requestReference", "requestReference", fhirreference.FHIRReference, False, "request", False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
