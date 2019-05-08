#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Consent) on 2019-05-07.
#  2019, SMART Health IT.


from . import domainresource

class Consent(domainresource.DomainResource):
    """ A healthcare consumer's  choices to permit or deny recipients or roles to
    perform actions for specific purposes and periods of time.
    
    A record of a healthcare consumer’s  choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """
    
    resource_type = "Consent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Classification of the consent statement - for indexing/retrieval.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ When this Consent was created or indexed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Identifier for this record (external references).
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Custodian of the consent.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who the consent applies to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who is agreeing to the policy and rules.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.policy = None
        """ Policies covered by this consent.
        List of `ConsentPolicy` items (represented as `dict` in JSON). """
        
        self.policyRule = None
        """ Regulation that this consents to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provision = None
        """ Constraints to the base Consent.policyRule.
        Type `ConsentProvision` (represented as `dict` in JSON). """
        
        self.scope = None
        """ Which of the four areas this resource covers (extensible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sourceAttachment = None
        """ Source from which this consent is taken.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.sourceReference = None
        """ Source from which this consent is taken.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | proposed | active | rejected | inactive | entered-in-error.
        Type `str`. """
        
        self.verification = None
        """ Consent Verified by patient or family.
        List of `ConsentVerification` items (represented as `dict` in JSON). """
        
        super(Consent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Consent, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, True),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("policy", "policy", ConsentPolicy, True, None, False),
            ("policyRule", "policyRule", codeableconcept.CodeableConcept, False, None, False),
            ("provision", "provision", ConsentProvision, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, True),
            ("sourceAttachment", "sourceAttachment", attachment.Attachment, False, "source", False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", False),
            ("status", "status", str, False, None, True),
            ("verification", "verification", ConsentVerification, True, None, False),
        ])
        return js


from . import backboneelement

class ConsentPolicy(backboneelement.BackboneElement):
    """ Policies covered by this consent.
    
    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """
    
    resource_type = "ConsentPolicy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ Enforcement source for policy.
        Type `str`. """
        
        self.uri = None
        """ Specific policy covered by this consent.
        Type `str`. """
        
        super(ConsentPolicy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentPolicy, self).elementProperties()
        js.extend([
            ("authority", "authority", str, False, None, False),
            ("uri", "uri", str, False, None, False),
        ])
        return js


class ConsentProvision(backboneelement.BackboneElement):
    """ Constraints to the base Consent.policyRule.
    
    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """
    
    resource_type = "ConsentProvision"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Actions controlled by this rule.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ Who|what controlled by this rule (or group, by role).
        List of `ConsentProvisionActor` items (represented as `dict` in JSON). """
        
        self.class_fhir = None
        """ e.g. Resource Type, Profile, CDA, etc..
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.code = None
        """ e.g. LOINC or SNOMED CT code, etc. in the content.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.data = None
        """ Data controlled by this rule.
        List of `ConsentProvisionData` items (represented as `dict` in JSON). """
        
        self.dataPeriod = None
        """ Timeframe for data controlled by this rule.
        Type `Period` (represented as `dict` in JSON). """
        
        self.period = None
        """ Timeframe for this rule.
        Type `Period` (represented as `dict` in JSON). """
        
        self.provision = None
        """ Nested Exception Rules.
        List of `ConsentProvision` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Context of activities covered by this rule.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ Security Labels that define affected resources.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ deny | permit.
        Type `str`. """
        
        super(ConsentProvision, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentProvision, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", ConsentProvisionActor, True, None, False),
            ("class_fhir", "class", coding.Coding, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("data", "data", ConsentProvisionData, True, None, False),
            ("dataPeriod", "dataPeriod", period.Period, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("provision", "provision", ConsentProvision, True, None, False),
            ("purpose", "purpose", coding.Coding, True, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class ConsentProvisionActor(backboneelement.BackboneElement):
    """ Who|what controlled by this rule (or group, by role).
    
    Who or what is controlled by this rule. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """
    
    resource_type = "ConsentProvisionActor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Resource for the actor (or group, by role).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role = None
        """ How the actor is involved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConsentProvisionActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentProvisionActor, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ConsentProvisionData(backboneelement.BackboneElement):
    """ Data controlled by this rule.
    
    The resources controlled by this rule if specific resources are referenced.
    """
    
    resource_type = "ConsentProvisionData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.meaning = None
        """ instance | related | dependents | authoredby.
        Type `str`. """
        
        self.reference = None
        """ The actual data reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ConsentProvisionData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentProvisionData, self).elementProperties()
        js.extend([
            ("meaning", "meaning", str, False, None, True),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ConsentVerification(backboneelement.BackboneElement):
    """ Consent Verified by patient or family.
    
    Whether a treatment instruction (e.g. artificial respiration yes or no) was
    verified with the patient, his/her family or another authorized person.
    """
    
    resource_type = "ConsentVerification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.verificationDate = None
        """ When consent verified.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.verified = None
        """ Has been verified.
        Type `bool`. """
        
        self.verifiedWith = None
        """ Person who verified.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ConsentVerification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentVerification, self).elementProperties()
        js.extend([
            ("verificationDate", "verificationDate", fhirdate.FHIRDate, False, None, False),
            ("verified", "verified", bool, False, None, True),
            ("verifiedWith", "verifiedWith", fhirreference.FHIRReference, False, None, False),
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
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
