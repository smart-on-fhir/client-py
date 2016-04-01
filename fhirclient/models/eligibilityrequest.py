#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/EligibilityRequest) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class EligibilityRequest(domainresource.DomainResource):
    """ Eligibility request.
    
    This resource provides the insurance eligibility details from the insurer
    regarding a specified coverage and optionally some class of service.
    """
    
    resource_name = "EligibilityRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefitCategory = None
        """ Benefit Category.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.benefitSubCategory = None
        """ Benefit SubCategory.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.businessArrangement = None
        """ Business agreement.
        Type `str`. """
        
        self.coverageIdentifier = None
        """ Insurance or medical plan.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.coverageReference = None
        """ Insurance or medical plan.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.entererIdentifier = None
        """ Author.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.entererReference = None
        """ Author.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.facilityIdentifier = None
        """ Servicing Facility.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.facilityReference = None
        """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organizationIdentifier = None
        """ Responsible organization.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organizationReference = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patientIdentifier = None
        """ The subject of the Products and Services.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patientReference = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Desired processing priority.
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
        
        self.servicedDate = None
        """ Estimated date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ Estimated date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.targetIdentifier = None
        """ Insurer.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.targetReference = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(EligibilityRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityRequest, self).elementProperties()
        js.extend([
            ("benefitCategory", "benefitCategory", coding.Coding, False, None, False),
            ("benefitSubCategory", "benefitSubCategory", coding.Coding, False, None, False),
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("coverageIdentifier", "coverageIdentifier", identifier.Identifier, False, "coverage", False),
            ("coverageReference", "coverageReference", fhirreference.FHIRReference, False, "coverage", False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("entererIdentifier", "entererIdentifier", identifier.Identifier, False, "enterer", False),
            ("entererReference", "entererReference", fhirreference.FHIRReference, False, "enterer", False),
            ("facilityIdentifier", "facilityIdentifier", identifier.Identifier, False, "facility", False),
            ("facilityReference", "facilityReference", fhirreference.FHIRReference, False, "facility", False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organizationIdentifier", "organizationIdentifier", identifier.Identifier, False, "organization", False),
            ("organizationReference", "organizationReference", fhirreference.FHIRReference, False, "organization", False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("patientIdentifier", "patientIdentifier", identifier.Identifier, False, "patient", False),
            ("patientReference", "patientReference", fhirreference.FHIRReference, False, "patient", False),
            ("priority", "priority", coding.Coding, False, None, False),
            ("providerIdentifier", "providerIdentifier", identifier.Identifier, False, "provider", False),
            ("providerReference", "providerReference", fhirreference.FHIRReference, False, "provider", False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("targetIdentifier", "targetIdentifier", identifier.Identifier, False, "target", False),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", False),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
