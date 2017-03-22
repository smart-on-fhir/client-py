#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/ReferralRequest) on 2017-03-22.
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
        
        self.authoredOn = None
        """ Date of creation/activation.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Request fulfilled by this request.
        List of `FHIRReference` items referencing `ReferralRequest, CarePlan, ProcedureRequest` (represented as `dict` in JSON). """
        
        self.context = None
        """ Originating encounter.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.definition = None
        """ Instantiates protocol or definition.
        List of `FHIRReference` items referencing `ActivityDefinition, PlanDefinition` (represented as `dict` in JSON). """
        
        self.description = None
        """ A textual description of the referral.
        Type `str`. """
        
        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.intent = None
        """ proposal | plan | order.
        Type `str`. """
        
        self.note = None
        """ Comments made about referral request.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When the service(s) requested in the referral should occur.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When the service(s) requested in the referral should occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Urgency of referral / transfer of care request.
        Type `str`. """
        
        self.reasonCode = None
        """ Reason for referral / transfer of care request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why is service needed?.
        List of `FHIRReference` items referencing `Condition, Observation` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Receiver of referral / transfer of care request.
        List of `FHIRReference` items referencing `Practitioner, Organization, HealthcareService` (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        """ Key events in history of request.
        List of `FHIRReference` items referencing `Provenance` (represented as `dict` in JSON). """
        
        self.replaces = None
        """ Request(s) replaced by this request.
        List of `FHIRReference` items referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Who/what is requesting service.
        Type `ReferralRequestRequester` (represented as `dict` in JSON). """
        
        self.serviceRequested = None
        """ Actions requested as part of the referral.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ The clinical specialty (discipline) that the referral is requested
        for.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | suspended | cancelled | completed | entered-in-
        error | unknown.
        Type `str`. """
        
        self.subject = None
        """ Patient referred to care or transfer.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        self.supportingInfo = None
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
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", fhirreference.FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", ReferralRequestRequester, False, None, False),
            ("serviceRequested", "serviceRequested", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class ReferralRequestRequester(backboneelement.BackboneElement):
    """ Who/what is requesting service.
    
    The individual who initiated the request and has responsibility for its
    activation.
    """
    
    resource_type = "ReferralRequestRequester"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.agent = None
        """ Individual making the request.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson, Device` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ Organization agent is acting for.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(ReferralRequestRequester, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ReferralRequestRequester, self).elementProperties()
        js.extend([
            ("agent", "agent", fhirreference.FHIRReference, False, None, True),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
