#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/ReferralRequest) on 2017-03-15.
#  2017, SMART Health IT.


from . import domainresource

class ReferralRequest(domainresource.DomainResource):
    """ A request for referral or transfer of care.
    
    Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider
    organization.
    """
    
    resource_type = "ReferralRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authored = None
        """ Date of creation/activation.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Request fulfilled by this request.
        List of `FHIRReference` items referencing `ReferralRequest, CarePlan, DiagnosticRequest, ProcedureRequest` (represented as `dict` in JSON). """
        
        self.category = None
        """ proposal | plan | request.
        Type `str`. """
        
        self.context = None
        """ Originating encounter.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.description = None
        """ A textual description of the referral.
        Type `str`. """
        
        self.fulfillmentTime = None
        """ Requested service(s) fulfillment time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.parent = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient referred to care or transfer.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Urgency of referral / transfer of care request.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Reason for referral / transfer of care request.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Receiver of referral / transfer of care request.
        List of `FHIRReference` items referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Requester of referral / transfer of care.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient` (represented as `dict` in JSON). """
        
        self.serviceRequested = None
        """ Actions requested as part of the referral.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ The clinical specialty (discipline) that the referral is requested
        for.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | cancelled | completed | entered-in-error.
        Type `str`. """
        
        self.supportingInformation = None
        """ Additonal information to support referral or transfer of care
        request.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.type = None
        """ Referral/Transition of care request type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ReferralRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ReferralRequest, self).elementProperties()
        js.extend([
            ("authored", "authored", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", str, False, None, True),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("fulfillmentTime", "fulfillmentTime", period.Period, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("parent", "parent", identifier.Identifier, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("serviceRequested", "serviceRequested", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
