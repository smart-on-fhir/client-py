#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Contract) on 2019-05-07.
#  2019, SMART Health IT.


from . import domainresource

class Contract(domainresource.DomainResource):
    """ Legal Agreement.
    
    Legally enforceable, formally recorded unilateral or bilateral directive
    i.e., a policy or agreement.
    """
    
    resource_type = "Contract"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias = None
        """ Acronym or short name.
        List of `str` items. """
        
        self.applies = None
        """ Effective time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.author = None
        """ Source of Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authority = None
        """ Authority under which this Contract has standing.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.contentDefinition = None
        """ Contract precursor content.
        Type `ContractContentDefinition` (represented as `dict` in JSON). """
        
        self.contentDerivative = None
        """ Content derived from the basal information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.domain = None
        """ A sphere of control governed by an authoritative jurisdiction,
        organization, or person.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.expirationType = None
        """ Contract cessation cause.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.friendly = None
        """ Contract Friendly Language.
        List of `ContractFriendly` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Source Contract Definition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.instantiatesUri = None
        """ External Contract Definition.
        Type `str`. """
        
        self.issued = None
        """ When this Contract was issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.legal = None
        """ Contract Legal Language.
        List of `ContractLegal` items (represented as `dict` in JSON). """
        
        self.legalState = None
        """ Negotiation status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.legallyBindingAttachment = None
        """ Binding Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.legallyBindingReference = None
        """ Binding Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.name = None
        """ Computer friendly designation.
        Type `str`. """
        
        self.relevantHistory = None
        """ Key event in Contract History.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.rule = None
        """ Computable Contract Language.
        List of `ContractRule` items (represented as `dict` in JSON). """
        
        self.scope = None
        """ Range of Legal Concerns.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.signer = None
        """ Contract Signatory.
        List of `ContractSigner` items (represented as `dict` in JSON). """
        
        self.site = None
        """ Specific Location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | suspended | cancelled | completed | entered-in-
        error | unknown.
        Type `str`. """
        
        self.subType = None
        """ Subtype within the context of type.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Contract Target Entity.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.subtitle = None
        """ Subordinate Friendly name.
        Type `str`. """
        
        self.supportingInfo = None
        """ Extra Information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.term = None
        """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Human Friendly name.
        Type `str`. """
        
        self.topicCodeableConcept = None
        """ Focus of contract interest.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.topicReference = None
        """ Focus of contract interest.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Legal instrument category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.url = None
        """ Basal definition.
        Type `str`. """
        
        self.version = None
        """ Business edition.
        Type `str`. """
        
        super(Contract, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contract, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authority", "authority", fhirreference.FHIRReference, True, None, False),
            ("contentDefinition", "contentDefinition", ContractContentDefinition, False, None, False),
            ("contentDerivative", "contentDerivative", codeableconcept.CodeableConcept, False, None, False),
            ("domain", "domain", fhirreference.FHIRReference, True, None, False),
            ("expirationType", "expirationType", codeableconcept.CodeableConcept, False, None, False),
            ("friendly", "friendly", ContractFriendly, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", fhirreference.FHIRReference, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("legal", "legal", ContractLegal, True, None, False),
            ("legalState", "legalState", codeableconcept.CodeableConcept, False, None, False),
            ("legallyBindingAttachment", "legallyBindingAttachment", attachment.Attachment, False, "legallyBinding", False),
            ("legallyBindingReference", "legallyBindingReference", fhirreference.FHIRReference, False, "legallyBinding", False),
            ("name", "name", str, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("rule", "rule", ContractRule, True, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("signer", "signer", ContractSigner, True, None, False),
            ("site", "site", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("term", "term", ContractTerm, True, None, False),
            ("title", "title", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ContractContentDefinition(backboneelement.BackboneElement):
    """ Contract precursor content.
    
    Precusory content developed with a focus and intent of supporting the
    formation a Contract instance, which may be associated with and
    transformable into a Contract.
    """
    
    resource_type = "ContractContentDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.copyright = None
        """ Publication Ownership.
        Type `str`. """
        
        self.publicationDate = None
        """ When published.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publicationStatus = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.publisher = None
        """ Publisher Entity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subType = None
        """ Detailed Content Type Definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Content structure and use.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractContentDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractContentDefinition, self).elementProperties()
        js.extend([
            ("copyright", "copyright", str, False, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("publicationStatus", "publicationStatus", str, False, None, True),
            ("publisher", "publisher", fhirreference.FHIRReference, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ContractFriendly(backboneelement.BackboneElement):
    """ Contract Friendly Language.
    
    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """
    
    resource_type = "ContractFriendly"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Easily comprehended representation of this Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Easily comprehended representation of this Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractFriendly, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractFriendly, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractLegal(backboneelement.BackboneElement):
    """ Contract Legal Language.
    
    List of Legal expressions or representations of this Contract.
    """
    
    resource_type = "ContractLegal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Contract Legal Text.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Contract Legal Text.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractLegal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractLegal, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractRule(backboneelement.BackboneElement):
    """ Computable Contract Language.
    
    List of Computable Policy Rule Language Representations of this Contract.
    """
    
    resource_type = "ContractRule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Computable Contract Rules.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Computable Contract Rules.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractRule, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractSigner(backboneelement.BackboneElement):
    """ Contract Signatory.
    
    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """
    
    resource_type = "ContractSigner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party = None
        """ Contract Signatory Party.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.signature = None
        """ Contract Documentation Signature.
        List of `Signature` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Signatory Role.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ContractSigner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractSigner, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("signature", "signature", signature.Signature, True, None, True),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class ContractTerm(backboneelement.BackboneElement):
    """ Contract Term List.
    
    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    
    resource_type = "ContractTerm"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Entity being ascribed responsibility.
        List of `ContractTermAction` items (represented as `dict` in JSON). """
        
        self.applies = None
        """ Contract Term Effective Time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.asset = None
        """ Contract Term Asset List.
        List of `ContractTermAsset` items (represented as `dict` in JSON). """
        
        self.group = None
        """ Nested Contract Term Group.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract Term Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Contract Term Issue Date Time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.offer = None
        """ Context of the Contract term.
        Type `ContractTermOffer` (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ Protection for the Term.
        List of `ContractTermSecurityLabel` items (represented as `dict` in JSON). """
        
        self.subType = None
        """ Contract Term Type specific classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Term Statement.
        Type `str`. """
        
        self.topicCodeableConcept = None
        """ Term Concern.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.topicReference = None
        """ Term Concern.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Term Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTerm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("action", "action", ContractTermAction, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("asset", "asset", ContractTermAsset, True, None, False),
            ("group", "group", ContractTerm, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("offer", "offer", ContractTermOffer, False, None, True),
            ("securityLabel", "securityLabel", ContractTermSecurityLabel, True, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermAction(backboneelement.BackboneElement):
    """ Entity being ascribed responsibility.
    
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    
    resource_type = "ContractTermAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.context = None
        """ Episode associated with action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contextLinkId = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.doNotPerform = None
        """ True if the term prohibits the  action.
        Type `bool`. """
        
        self.intent = None
        """ Purpose for the Contract Term Action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.note = None
        """ Comments about the action.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When action happens.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When action happens.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ When action happens.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Actor that wil execute (or not) the action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerLinkId = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.performerRole = None
        """ Competency of the performer.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ Kind of service performer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reason = None
        """ Why action is to be performed.
        List of `str` items. """
        
        self.reasonCode = None
        """ Why is action (not) needed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonLinkId = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.reasonReference = None
        """ Why is action (not) needed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester = None
        """ Who asked for action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requesterLinkId = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.securityLabelNumber = None
        """ Action restriction numbers.
        List of `int` items. """
        
        self.status = None
        """ State of the action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Entity of the action.
        List of `ContractTermActionSubject` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type or form of the action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAction, self).elementProperties()
        js.extend([
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("contextLinkId", "contextLinkId", str, True, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("intent", "intent", codeableconcept.CodeableConcept, False, None, True),
            ("linkId", "linkId", str, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerLinkId", "performerLinkId", str, True, None, False),
            ("performerRole", "performerRole", codeableconcept.CodeableConcept, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("reason", "reason", str, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonLinkId", "reasonLinkId", str, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, True, None, False),
            ("requesterLinkId", "requesterLinkId", str, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, True),
            ("subject", "subject", ContractTermActionSubject, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ContractTermActionSubject(backboneelement.BackboneElement):
    """ Entity of the action.
    """
    
    resource_type = "ContractTermActionSubject"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Entity of the action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.role = None
        """ Role type of the agent.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermActionSubject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermActionSubject, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermAsset(backboneelement.BackboneElement):
    """ Contract Term Asset List.
    """
    
    resource_type = "ContractTermAsset"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answer = None
        """ Response to assets.
        List of `ContractTermOfferAnswer` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ Quality desctiption of asset.
        Type `str`. """
        
        self.context = None
        """ Circumstance of the asset.
        List of `ContractTermAssetContext` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Pointer to asset text.
        List of `str` items. """
        
        self.period = None
        """ Time period of the asset.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.periodType = None
        """ Asset availability types.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.relationship = None
        """ Kinship of the asset.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.scope = None
        """ Range of asset.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.securityLabelNumber = None
        """ Asset restriction numbers.
        List of `int` items. """
        
        self.subtype = None
        """ Asset sub-category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Asset clause or question text.
        Type `str`. """
        
        self.type = None
        """ Asset category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.typeReference = None
        """ Associated entities.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.usePeriod = None
        """ Time period.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.valuedItem = None
        """ Contract Valued Item List.
        List of `ContractTermAssetValuedItem` items (represented as `dict` in JSON). """
        
        super(ContractTermAsset, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAsset, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", ContractTermAssetContext, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("period", "period", period.Period, True, None, False),
            ("periodType", "periodType", codeableconcept.CodeableConcept, True, None, False),
            ("relationship", "relationship", coding.Coding, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, True, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("typeReference", "typeReference", fhirreference.FHIRReference, True, None, False),
            ("usePeriod", "usePeriod", period.Period, True, None, False),
            ("valuedItem", "valuedItem", ContractTermAssetValuedItem, True, None, False),
        ])
        return js


class ContractTermAssetContext(backboneelement.BackboneElement):
    """ Circumstance of the asset.
    """
    
    resource_type = "ContractTermAssetContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Codeable asset context.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ Creator,custodian or owner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.text = None
        """ Context description.
        Type `str`. """
        
        super(ContractTermAssetContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetContext, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class ContractTermAssetValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item List.
    """
    
    resource_type = "ContractTermAssetValuedItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.effectiveTime = None
        """ Contract Valued Item Effective Tiem.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.entityCodeableConcept = None
        """ Contract Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.entityReference = None
        """ Contract Valued Item Type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Contract Valued Item Price Scaling Factor.
        Type `float`. """
        
        self.identifier = None
        """ Contract Valued Item Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.net = None
        """ Total Contract Valued Item Value.
        Type `Money` (represented as `dict` in JSON). """
        
        self.payment = None
        """ Terms of valuation.
        Type `str`. """
        
        self.paymentDate = None
        """ When payment is due.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.points = None
        """ Contract Valued Item Difficulty Scaling Factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Contract Valued Items.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Who will receive payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Who will make payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.securityLabelNumber = None
        """ Security Labels that define affected terms.
        List of `int` items. """
        
        self.unitPrice = None
        """ Contract Valued Item fee, charge, or cost.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ContractTermAssetValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdate.FHIRDate, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("payment", "payment", str, False, None, False),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ContractTermOffer(backboneelement.BackboneElement):
    """ Context of the Contract term.
    
    The matter of concern in the context of this provision of the agrement.
    """
    
    resource_type = "ContractTermOffer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answer = None
        """ Response to offer text.
        List of `ContractTermOfferAnswer` items (represented as `dict` in JSON). """
        
        self.decision = None
        """ Accepting party choice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.decisionMode = None
        """ How decision is conveyed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Offer business ID.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Pointer to text.
        List of `str` items. """
        
        self.party = None
        """ Offer Recipient.
        List of `ContractTermOfferParty` items (represented as `dict` in JSON). """
        
        self.securityLabelNumber = None
        """ Offer restriction numbers.
        List of `int` items. """
        
        self.text = None
        """ Human readable offer text.
        Type `str`. """
        
        self.topic = None
        """ Negotiable offer asset.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Offer Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermOffer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOffer, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("decision", "decision", codeableconcept.CodeableConcept, False, None, False),
            ("decisionMode", "decisionMode", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("party", "party", ContractTermOfferParty, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("text", "text", str, False, None, False),
            ("topic", "topic", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermOfferAnswer(backboneelement.BackboneElement):
    """ Response to offer text.
    """
    
    resource_type = "ContractTermOfferAnswer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueAttachment = None
        """ The actual answer response.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ The actual answer response.
        Type `bool`. """
        
        self.valueCoding = None
        """ The actual answer response.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ The actual answer response.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ The actual answer response.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ The actual answer response.
        Type `float`. """
        
        self.valueInteger = None
        """ The actual answer response.
        Type `int`. """
        
        self.valueQuantity = None
        """ The actual answer response.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ The actual answer response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ The actual answer response.
        Type `str`. """
        
        self.valueTime = None
        """ The actual answer response.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueUri = None
        """ The actual answer response.
        Type `str`. """
        
        super(ContractTermOfferAnswer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOfferAnswer, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
        ])
        return js


class ContractTermOfferParty(backboneelement.BackboneElement):
    """ Offer Recipient.
    """
    
    resource_type = "ContractTermOfferParty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Referenced entity.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.role = None
        """ Participant engagement type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermOfferParty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOfferParty, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ContractTermSecurityLabel(backboneelement.BackboneElement):
    """ Protection for the Term.
    
    Security labels that protect the handling of information about the term and
    its elements, which may be specifically identified..
    """
    
    resource_type = "ContractTermSecurityLabel"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Applicable Policy.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.classification = None
        """ Confidentiality Protection.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.control = None
        """ Handling Instructions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.number = None
        """ Link to Security Labels.
        List of `int` items. """
        
        super(ContractTermSecurityLabel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermSecurityLabel, self).elementProperties()
        js.extend([
            ("category", "category", coding.Coding, True, None, False),
            ("classification", "classification", coding.Coding, False, None, True),
            ("control", "control", coding.Coding, True, None, False),
            ("number", "number", int, True, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
