#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8595 (http://hl7.org/fhir/StructureDefinition/Consent) on 2016-06-26.
#  2016, SMART Health IT.


from . import domainresource

class Consent(domainresource.DomainResource):
    """ Information about a healthcare consumer’s consent statements.
    
    Information about a healthcare consumer’s consent - a series of statements
    regard their agreement (or lack thereof) to various health-related
    procedures, in accordance with governing jurisdictional and organization
    privacy policies that grant or withhold consent:.
    """
    
    resource_name = "Consent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Actions controlled by this consent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ Who|what controlled by this concept (or group, by role).
        List of `ConsentActor` items (represented as `dict` in JSON). """
        
        self.author = None
        """ Who made the consent statement.
        Type `FHIRReference` referencing `Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.category = None
        """ Classification of the consent statement - for indexing/retrieval.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.data = None
        """ Data controlled by this Consent.
        List of `ConsentData` items (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ When this Consent was created or indexed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.except_fhir = None
        """ Consent Exception.
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
        """ Security Labels for the operation/context.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ Security Labels that define affected resources.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.sourceAttachment = None
        """ Source from which this consent is taken.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.sourceIdentifier = None
        """ Source from which this consent is taken.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.sourceReference = None
        """ Source from which this consent is taken.
        Type `FHIRReference` referencing `Consent, DocumentReference, Contract, Questionnaire` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | proposed | active | rejected | inactive | entered-in-error.
        Type `str`. """
        
        super(Consent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Consent, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", ConsentActor, True, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("data", "data", ConsentData, True, None, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, False),
            ("except_fhir", "except", ConsentExcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("policy", "policy", str, False, None, True),
            ("purpose", "purpose", coding.Coding, True, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("sourceAttachment", "sourceAttachment", attachment.Attachment, False, "source", False),
            ("sourceIdentifier", "sourceIdentifier", identifier.Identifier, False, "source", False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class ConsentActor(backboneelement.BackboneElement):
    """ Who|what controlled by this concept (or group, by role).
    
    Who or what is controlled by this Consent.
    """
    
    resource_name = "ConsentActor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Resource for the actor (or group, by role).
        Type `FHIRReference` referencing `Device, Group, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.role = None
        """ How the individual is/was involved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConsentActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentActor, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ConsentData(backboneelement.BackboneElement):
    """ Data controlled by this Consent.
    
    The resources controlled by this consent.
    """
    
    resource_name = "ConsentData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.meaning = None
        """ instance | related | dependents | profile | valueset.
        Type `str`. """
        
        self.reference = None
        """ The actual data reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(ConsentData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentData, self).elementProperties()
        js.extend([
            ("meaning", "meaning", str, False, None, True),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ConsentExcept(backboneelement.BackboneElement):
    """ Consent Exception.
    
    An exception to the base policy of this Consent.
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
        List of `ConsentActor` items (represented as `dict` in JSON). """
        
        self.data = None
        """ Data controlled by this exception.
        List of `ConsentData` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Consent Exception Effective Time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Security Labels for the operation/context.
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
            ("actor", "actor", ConsentActor, True, None, False),
            ("data", "data", ConsentData, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("purpose", "purpose", coding.Coding, True, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
