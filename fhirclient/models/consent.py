# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Consent).
# 2024, SMART Health IT.


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
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.dateTime = None
        """ When this Consent was created or indexed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._dateTime = None
        """ Primitive extension for dateTime. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifier for this record (external references).
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.organization = None
        """ Custodian of the consent.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._organization = None
        """ Primitive extension for organization. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Who the consent applies to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Who is agreeing to the policy and rules.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.policy = None
        """ Policies covered by this consent.
        List of `ConsentPolicy` items (represented as `dict` in JSON). """
        self._policy = None
        """ Primitive extension for policy. Type `FHIRPrimitiveExtension` """
        
        self.policyRule = None
        """ Regulation that this consents to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._policyRule = None
        """ Primitive extension for policyRule. Type `FHIRPrimitiveExtension` """
        
        self.provision = None
        """ Constraints to the base Consent.policyRule.
        Type `ConsentProvision` (represented as `dict` in JSON). """
        self._provision = None
        """ Primitive extension for provision. Type `FHIRPrimitiveExtension` """
        
        self.scope = None
        """ Which of the four areas this resource covers (extensible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._scope = None
        """ Primitive extension for scope. Type `FHIRPrimitiveExtension` """
        
        self.sourceAttachment = None
        """ Source from which this consent is taken.
        Type `Attachment` (represented as `dict` in JSON). """
        self._sourceAttachment = None
        """ Primitive extension for sourceAttachment. Type `FHIRPrimitiveExtension` """
        
        self.sourceReference = None
        """ Source from which this consent is taken.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._sourceReference = None
        """ Primitive extension for sourceReference. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | proposed | active | rejected | inactive | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.verification = None
        """ Consent Verified by patient or family.
        List of `ConsentVerification` items (represented as `dict` in JSON). """
        self._verification = None
        """ Primitive extension for verification. Type `FHIRPrimitiveExtension` """
        
        super(Consent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Consent, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, True),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dateTime", "dateTime", fhirdatetime.FHIRDateTime, False, None, False),
            ("_dateTime", "_dateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, True, None, False),
            ("_organization", "_organization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("policy", "policy", ConsentPolicy, True, None, False),
            ("_policy", "_policy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("policyRule", "policyRule", codeableconcept.CodeableConcept, False, None, False),
            ("_policyRule", "_policyRule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("provision", "provision", ConsentProvision, False, None, False),
            ("_provision", "_provision", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, True),
            ("_scope", "_scope", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceAttachment", "sourceAttachment", attachment.Attachment, False, "source", False),
            ("_sourceAttachment", "_sourceAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", False),
            ("_sourceReference", "_sourceReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("verification", "verification", ConsentVerification, True, None, False),
            ("_verification", "_verification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._authority = None
        """ Primitive extension for authority. Type `FHIRPrimitiveExtension` """
        
        self.uri = None
        """ Specific policy covered by this consent.
        Type `str`. """
        self._uri = None
        """ Primitive extension for uri. Type `FHIRPrimitiveExtension` """
        
        super(ConsentPolicy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentPolicy, self).elementProperties()
        js.extend([
            ("authority", "authority", str, False, None, False),
            ("_authority", "_authority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("uri", "uri", str, False, None, False),
            ("_uri", "_uri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        self.actor = None
        """ Who|what controlled by this rule (or group, by role).
        List of `ConsentProvisionActor` items (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.class_fhir = None
        """ e.g. Resource Type, Profile, CDA, etc..
        List of `Coding` items (represented as `dict` in JSON). """
        self._class_fhir = None
        """ Primitive extension for class_fhir. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ e.g. LOINC or SNOMED CT code, etc. in the content.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.data = None
        """ Data controlled by this rule.
        List of `ConsentProvisionData` items (represented as `dict` in JSON). """
        self._data = None
        """ Primitive extension for data. Type `FHIRPrimitiveExtension` """
        
        self.dataPeriod = None
        """ Timeframe for data controlled by this rule.
        Type `Period` (represented as `dict` in JSON). """
        self._dataPeriod = None
        """ Primitive extension for dataPeriod. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Timeframe for this rule.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.provision = None
        """ Nested Exception Rules.
        List of `ConsentProvision` items (represented as `dict` in JSON). """
        self._provision = None
        """ Primitive extension for provision. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Context of activities covered by this rule.
        List of `Coding` items (represented as `dict` in JSON). """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.securityLabel = None
        """ Security Labels that define affected resources.
        List of `Coding` items (represented as `dict` in JSON). """
        self._securityLabel = None
        """ Primitive extension for securityLabel. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ deny | permit.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ConsentProvision, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentProvision, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("actor", "actor", ConsentProvisionActor, True, None, False),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("class_fhir", "class", coding.Coding, True, None, False),
            ("_class_fhir", "_class_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("data", "data", ConsentProvisionData, True, None, False),
            ("_data", "_data", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dataPeriod", "dataPeriod", period.Period, False, None, False),
            ("_dataPeriod", "_dataPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("provision", "provision", ConsentProvision, True, None, False),
            ("_provision", "_provision", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", coding.Coding, True, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("_securityLabel", "_securityLabel", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ How the actor is involved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        super(ConsentProvisionActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentProvisionActor, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._meaning = None
        """ Primitive extension for meaning. Type `FHIRPrimitiveExtension` """
        
        self.reference = None
        """ The actual data reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        super(ConsentProvisionData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentProvisionData, self).elementProperties()
        js.extend([
            ("meaning", "meaning", str, False, None, True),
            ("_meaning", "_meaning", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._verificationDate = None
        """ Primitive extension for verificationDate. Type `FHIRPrimitiveExtension` """
        
        self.verified = None
        """ Has been verified.
        Type `bool`. """
        self._verified = None
        """ Primitive extension for verified. Type `FHIRPrimitiveExtension` """
        
        self.verifiedWith = None
        """ Person who verified.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._verifiedWith = None
        """ Primitive extension for verifiedWith. Type `FHIRPrimitiveExtension` """
        
        super(ConsentVerification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentVerification, self).elementProperties()
        js.extend([
            ("verificationDate", "verificationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_verificationDate", "_verificationDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("verified", "verified", bool, False, None, True),
            ("_verified", "_verified", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("verifiedWith", "verifiedWith", fhirreference.FHIRReference, False, None, False),
            ("_verifiedWith", "_verifiedWith", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period