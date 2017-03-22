#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/EligibilityRequest) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class EligibilityRequest(domainresource.DomainResource):
    """ Determine insurance validity and scope of coverage.
    
    The EligibilityRequest provides patient and insurance coverage information
    to an insurer for them to respond, in the form of an EligibilityResponse,
    with information regarding whether the stated coverage is valid and in-
    force and optionally to provide the insurance details of the policy.
    """
    
    resource_type = "EligibilityRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefitCategory = None
        """ Type of services covered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.benefitSubCategory = None
        """ Detailed services covered within the type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.businessArrangement = None
        """ Business agreement.
        Type `str`. """
        
        self.coverage = None
        """ Insurance or medical plan.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.enterer = None
        """ Author.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.facility = None
        """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurer = None
        """ Target.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Desired processing priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.servicedDate = None
        """ Estimated date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ Estimated date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(EligibilityRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityRequest, self).elementProperties()
        js.extend([
            ("benefitCategory", "benefitCategory", codeableconcept.CodeableConcept, False, None, False),
            ("benefitSubCategory", "benefitSubCategory", codeableconcept.CodeableConcept, False, None, False),
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("status", "status", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
