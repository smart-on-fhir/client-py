#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10061 (http://hl7.org/fhir/StructureDefinition/Consent) on 2016-10-24.
#  2016, SMART Health IT.


from . import domainresource

class Consent(domainresource.DomainResource):
    """ A healthcare consumer’s policy choices to permits or denies recipients or
    roles to perform actions for specific purposes and periods of time.
    
    A record of a healthcare consumer’s policy choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """
    
    resource_name = "Consent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Classification of the consent statement - for indexing/retrieval.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.consentor = None
        """ Who is agreeing to the policy and exceptions.
        List of `FHIRReference` items referencing `Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ When this Consent was created or indexed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.except_fhir = None
        """ Additional rule -  addition or removal of permissions.
        List of `ConsentExcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier for this record (external references).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Organization that manages the consent.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who the consent applies to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period that this consent applies.
        Type `Period` (represented as `dict` in JSON). """
        
        self.policy = None
        """ Policy that this consents to.
        Type `str`. """
        
        self.purpose = None
        """ Context of activities for which the agreement is made.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Whose access is controlled by the policy.
        List of `FHIRReference` items referencing `Device, Group, Organization, Patient, Practitioner, RelatedPerson, CareTeam` (represented as `dict` in JSON). """
        
        self.sourceAttachment = None
        """ Source from which this consent is taken.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.sourceIdentifier = None
        """ Source from which this consent is taken.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.sourceReference = None
        """ Source from which this consent is taken.
        Type `FHIRReference` referencing `Consent, DocumentReference, Contract, QuestionnaireResponse` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | proposed | active | rejected | inactive | entered-in-error.
        Type `str`. """
        
        super(Consent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Consent, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("consentor", "consentor", fhirreference.FHIRReference, True, None, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, False),
            ("except_fhir", "except", ConsentExcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("policy", "policy", str, False, None, True),
            ("purpose", "purpose", coding.Coding, True, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("sourceAttachment", "sourceAttachment", attachment.Attachment, False, "source", False),
            ("sourceIdentifier", "sourceIdentifier", identifier.Identifier, False, "source", False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class ConsentExcept(backboneelement.BackboneElement):
    """ Additional rule -  addition or removal of permissions.
    
    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """
    
    resource_name = "ConsentExcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Actions controlled by this exception.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ Who|what controlled by this exception (or group, by role).
        List of `ConsentExceptActor` items (represented as `dict` in JSON). """
        
        self.class_fhir = None
        """ e.g. Resource Type, Profile, or CDA etc.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.code = None
        """ e.g. LOINC or SNOMED CT code, etc in the content.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.data = None
        """ Data controlled by this exception.
        List of `ConsentExceptData` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Timeframe for data controlled by this exception.
        Type `Period` (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Context of activities covered by this exception.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ Security Labels that define affected resources.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ deny | permit.
        Type `str`. """
        
        super(ConsentExcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentExcept, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", ConsentExceptActor, True, None, False),
            ("class_fhir", "class", coding.Coding, True, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("data", "data", ConsentExceptData, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("purpose", "purpose", coding.Coding, True, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class ConsentExceptActor(backboneelement.BackboneElement):
    """ Who|what controlled by this exception (or group, by role).
    
    Who or what is controlled by this Exception. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """
    
    resource_name = "ConsentExceptActor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Resource for the actor (or group, by role).
        Type `FHIRReference` referencing `Device, Group, CareTeam, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.role = None
        """ How the actor is/was involved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConsentExceptActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentExceptActor, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ConsentExceptData(backboneelement.BackboneElement):
    """ Data controlled by this exception.
    
    The resources controlled by this exception, if specific resources are
    referenced.
    """
    
    resource_name = "ConsentExceptData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.meaning = None
        """ instance | related | dependents.
        Type `str`. """
        
        self.reference = None
        """ The actual data reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(ConsentExceptData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentExceptData, self).elementProperties()
        js.extend([
            ("meaning", "meaning", str, False, None, True),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
