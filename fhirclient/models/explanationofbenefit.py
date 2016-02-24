#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2016-02-24.
#  2016, SMART Health IT.


from . import domainresource

class ExplanationOfBenefit(domainresource.DomainResource):
    """ Remittance resource.
    
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    
    resource_name = "ExplanationOfBenefit"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        self.organization = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error.
        Type `str`. """
        
        self.request = None
        """ Claim reference.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefit, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False),
            ("disposition", "disposition", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("organization", "organization", fhirreference.FHIRReference, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False),
            ("outcome", "outcome", str, False),
            ("request", "request", fhirreference.FHIRReference, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False),
            ("ruleset", "ruleset", coding.Coding, False),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
