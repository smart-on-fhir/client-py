# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Contract).
# 2024, SMART Health IT.


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
        self._alias = None
        """ Primitive extension for alias. Type `FHIRPrimitiveExtension` """
        
        self.applies = None
        """ Effective time.
        Type `Period` (represented as `dict` in JSON). """
        self._applies = None
        """ Primitive extension for applies. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Source of Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.authority = None
        """ Authority under which this Contract has standing.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._authority = None
        """ Primitive extension for authority. Type `FHIRPrimitiveExtension` """
        
        self.contentDefinition = None
        """ Contract precursor content.
        Type `ContractContentDefinition` (represented as `dict` in JSON). """
        self._contentDefinition = None
        """ Primitive extension for contentDefinition. Type `FHIRPrimitiveExtension` """
        
        self.contentDerivative = None
        """ Content derived from the basal information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._contentDerivative = None
        """ Primitive extension for contentDerivative. Type `FHIRPrimitiveExtension` """
        
        self.domain = None
        """ A sphere of control governed by an authoritative jurisdiction,
        organization, or person.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._domain = None
        """ Primitive extension for domain. Type `FHIRPrimitiveExtension` """
        
        self.expirationType = None
        """ Contract cessation cause.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._expirationType = None
        """ Primitive extension for expirationType. Type `FHIRPrimitiveExtension` """
        
        self.friendly = None
        """ Contract Friendly Language.
        List of `ContractFriendly` items (represented as `dict` in JSON). """
        self._friendly = None
        """ Primitive extension for friendly. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Contract number.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesCanonical = None
        """ Source Contract Definition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._instantiatesCanonical = None
        """ Primitive extension for instantiatesCanonical. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesUri = None
        """ External Contract Definition.
        Type `str`. """
        self._instantiatesUri = None
        """ Primitive extension for instantiatesUri. Type `FHIRPrimitiveExtension` """
        
        self.issued = None
        """ When this Contract was issued.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._issued = None
        """ Primitive extension for issued. Type `FHIRPrimitiveExtension` """
        
        self.legal = None
        """ Contract Legal Language.
        List of `ContractLegal` items (represented as `dict` in JSON). """
        self._legal = None
        """ Primitive extension for legal. Type `FHIRPrimitiveExtension` """
        
        self.legalState = None
        """ Negotiation status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._legalState = None
        """ Primitive extension for legalState. Type `FHIRPrimitiveExtension` """
        
        self.legallyBindingAttachment = None
        """ Binding Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        self._legallyBindingAttachment = None
        """ Primitive extension for legallyBindingAttachment. Type `FHIRPrimitiveExtension` """
        
        self.legallyBindingReference = None
        """ Binding Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._legallyBindingReference = None
        """ Primitive extension for legallyBindingReference. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Computer friendly designation.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.relevantHistory = None
        """ Key event in Contract History.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._relevantHistory = None
        """ Primitive extension for relevantHistory. Type `FHIRPrimitiveExtension` """
        
        self.rule = None
        """ Computable Contract Language.
        List of `ContractRule` items (represented as `dict` in JSON). """
        self._rule = None
        """ Primitive extension for rule. Type `FHIRPrimitiveExtension` """
        
        self.scope = None
        """ Range of Legal Concerns.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._scope = None
        """ Primitive extension for scope. Type `FHIRPrimitiveExtension` """
        
        self.signer = None
        """ Contract Signatory.
        List of `ContractSigner` items (represented as `dict` in JSON). """
        self._signer = None
        """ Primitive extension for signer. Type `FHIRPrimitiveExtension` """
        
        self.site = None
        """ Specific Location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._site = None
        """ Primitive extension for site. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ amended | appended | cancelled | disputed | entered-in-error |
        executable | executed | negotiable | offered | policy | rejected |
        renewed | revoked | resolved | terminated.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subType = None
        """ Subtype within the context of type.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._subType = None
        """ Primitive extension for subType. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Contract Target Entity.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.subtitle = None
        """ Subordinate Friendly name.
        Type `str`. """
        self._subtitle = None
        """ Primitive extension for subtitle. Type `FHIRPrimitiveExtension` """
        
        self.supportingInfo = None
        """ Extra Information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingInfo = None
        """ Primitive extension for supportingInfo. Type `FHIRPrimitiveExtension` """
        
        self.term = None
        """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        self._term = None
        """ Primitive extension for term. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Human Friendly name.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.topicCodeableConcept = None
        """ Focus of contract interest.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._topicCodeableConcept = None
        """ Primitive extension for topicCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.topicReference = None
        """ Focus of contract interest.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._topicReference = None
        """ Primitive extension for topicReference. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Legal instrument category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Basal definition.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business edition.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(Contract, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contract, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("_alias", "_alias", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("_applies", "_applies", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("authority", "authority", fhirreference.FHIRReference, True, None, False),
            ("_authority", "_authority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentDefinition", "contentDefinition", ContractContentDefinition, False, None, False),
            ("_contentDefinition", "_contentDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentDerivative", "contentDerivative", codeableconcept.CodeableConcept, False, None, False),
            ("_contentDerivative", "_contentDerivative", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("domain", "domain", fhirreference.FHIRReference, True, None, False),
            ("_domain", "_domain", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expirationType", "expirationType", codeableconcept.CodeableConcept, False, None, False),
            ("_expirationType", "_expirationType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("friendly", "friendly", ContractFriendly, True, None, False),
            ("_friendly", "_friendly", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", fhirreference.FHIRReference, False, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("_instantiatesUri", "_instantiatesUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issued", "issued", fhirdatetime.FHIRDateTime, False, None, False),
            ("_issued", "_issued", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("legal", "legal", ContractLegal, True, None, False),
            ("_legal", "_legal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("legalState", "legalState", codeableconcept.CodeableConcept, False, None, False),
            ("_legalState", "_legalState", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("legallyBindingAttachment", "legallyBindingAttachment", attachment.Attachment, False, "legallyBinding", False),
            ("_legallyBindingAttachment", "_legallyBindingAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("legallyBindingReference", "legallyBindingReference", fhirreference.FHIRReference, False, "legallyBinding", False),
            ("_legallyBindingReference", "_legallyBindingReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("_relevantHistory", "_relevantHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rule", "rule", ContractRule, True, None, False),
            ("_rule", "_rule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("_scope", "_scope", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("signer", "signer", ContractSigner, True, None, False),
            ("_signer", "_signer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("site", "site", fhirreference.FHIRReference, True, None, False),
            ("_site", "_site", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False),
            ("_subType", "_subType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("_subtitle", "_subtitle", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("_supportingInfo", "_supportingInfo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("term", "term", ContractTerm, True, None, False),
            ("_term", "_term", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("_topicCodeableConcept", "_topicCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("_topicReference", "_topicReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._copyright = None
        """ Primitive extension for copyright. Type `FHIRPrimitiveExtension` """
        
        self.publicationDate = None
        """ When published.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._publicationDate = None
        """ Primitive extension for publicationDate. Type `FHIRPrimitiveExtension` """
        
        self.publicationStatus = None
        """ amended | appended | cancelled | disputed | entered-in-error |
        executable | executed | negotiable | offered | policy | rejected |
        renewed | revoked | resolved | terminated.
        Type `str`. """
        self._publicationStatus = None
        """ Primitive extension for publicationStatus. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Publisher Entity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.subType = None
        """ Detailed Content Type Definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._subType = None
        """ Primitive extension for subType. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Content structure and use.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ContractContentDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractContentDefinition, self).elementProperties()
        js.extend([
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publicationDate", "publicationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_publicationDate", "_publicationDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publicationStatus", "publicationStatus", str, False, None, True),
            ("_publicationStatus", "_publicationStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", fhirreference.FHIRReference, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("_subType", "_subType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._contentAttachment = None
        """ Primitive extension for contentAttachment. Type `FHIRPrimitiveExtension` """
        
        self.contentReference = None
        """ Easily comprehended representation of this Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._contentReference = None
        """ Primitive extension for contentReference. Type `FHIRPrimitiveExtension` """
        
        super(ContractFriendly, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractFriendly, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("_contentAttachment", "_contentAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("_contentReference", "_contentReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._contentAttachment = None
        """ Primitive extension for contentAttachment. Type `FHIRPrimitiveExtension` """
        
        self.contentReference = None
        """ Contract Legal Text.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._contentReference = None
        """ Primitive extension for contentReference. Type `FHIRPrimitiveExtension` """
        
        super(ContractLegal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractLegal, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("_contentAttachment", "_contentAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("_contentReference", "_contentReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._contentAttachment = None
        """ Primitive extension for contentAttachment. Type `FHIRPrimitiveExtension` """
        
        self.contentReference = None
        """ Computable Contract Rules.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._contentReference = None
        """ Primitive extension for contentReference. Type `FHIRPrimitiveExtension` """
        
        super(ContractRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractRule, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("_contentAttachment", "_contentAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("_contentReference", "_contentReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._party = None
        """ Primitive extension for party. Type `FHIRPrimitiveExtension` """
        
        self.signature = None
        """ Contract Documentation Signature.
        List of `Signature` items (represented as `dict` in JSON). """
        self._signature = None
        """ Primitive extension for signature. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Contract Signatory Role.
        Type `Coding` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ContractSigner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractSigner, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("_party", "_party", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("signature", "signature", signature.Signature, True, None, True),
            ("_signature", "_signature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        self.applies = None
        """ Contract Term Effective Time.
        Type `Period` (represented as `dict` in JSON). """
        self._applies = None
        """ Primitive extension for applies. Type `FHIRPrimitiveExtension` """
        
        self.asset = None
        """ Contract Term Asset List.
        List of `ContractTermAsset` items (represented as `dict` in JSON). """
        self._asset = None
        """ Primitive extension for asset. Type `FHIRPrimitiveExtension` """
        
        self.group = None
        """ Nested Contract Term Group.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        self._group = None
        """ Primitive extension for group. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Contract Term Number.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.issued = None
        """ Contract Term Issue Date Time.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._issued = None
        """ Primitive extension for issued. Type `FHIRPrimitiveExtension` """
        
        self.offer = None
        """ Context of the Contract term.
        Type `ContractTermOffer` (represented as `dict` in JSON). """
        self._offer = None
        """ Primitive extension for offer. Type `FHIRPrimitiveExtension` """
        
        self.securityLabel = None
        """ Protection for the Term.
        List of `ContractTermSecurityLabel` items (represented as `dict` in JSON). """
        self._securityLabel = None
        """ Primitive extension for securityLabel. Type `FHIRPrimitiveExtension` """
        
        self.subType = None
        """ Contract Term Type specific classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._subType = None
        """ Primitive extension for subType. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Term Statement.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.topicCodeableConcept = None
        """ Term Concern.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._topicCodeableConcept = None
        """ Primitive extension for topicCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.topicReference = None
        """ Term Concern.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._topicReference = None
        """ Primitive extension for topicReference. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Contract Term Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ContractTerm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("action", "action", ContractTermAction, True, None, False),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("_applies", "_applies", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("asset", "asset", ContractTermAsset, True, None, False),
            ("_asset", "_asset", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("group", "group", ContractTerm, True, None, False),
            ("_group", "_group", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issued", "issued", fhirdatetime.FHIRDateTime, False, None, False),
            ("_issued", "_issued", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("offer", "offer", ContractTermOffer, False, None, True),
            ("_offer", "_offer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("securityLabel", "securityLabel", ContractTermSecurityLabel, True, None, False),
            ("_securityLabel", "_securityLabel", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("_subType", "_subType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("_topicCodeableConcept", "_topicCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("_topicReference", "_topicReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.contextLinkId = None
        """ Pointer to specific item.
        List of `str` items. """
        self._contextLinkId = None
        """ Primitive extension for contextLinkId. Type `FHIRPrimitiveExtension` """
        
        self.doNotPerform = None
        """ True if the term prohibits the  action.
        Type `bool`. """
        self._doNotPerform = None
        """ Primitive extension for doNotPerform. Type `FHIRPrimitiveExtension` """
        
        self.intent = None
        """ Purpose for the Contract Term Action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._intent = None
        """ Primitive extension for intent. Type `FHIRPrimitiveExtension` """
        
        self.linkId = None
        """ Pointer to specific item.
        List of `str` items. """
        self._linkId = None
        """ Primitive extension for linkId. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments about the action.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceDateTime = None
        """ When action happens.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._occurrenceDateTime = None
        """ Primitive extension for occurrenceDateTime. Type `FHIRPrimitiveExtension` """
        
        self.occurrencePeriod = None
        """ When action happens.
        Type `Period` (represented as `dict` in JSON). """
        self._occurrencePeriod = None
        """ Primitive extension for occurrencePeriod. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceTiming = None
        """ When action happens.
        Type `Timing` (represented as `dict` in JSON). """
        self._occurrenceTiming = None
        """ Primitive extension for occurrenceTiming. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Actor that wil execute (or not) the action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.performerLinkId = None
        """ Pointer to specific item.
        List of `str` items. """
        self._performerLinkId = None
        """ Primitive extension for performerLinkId. Type `FHIRPrimitiveExtension` """
        
        self.performerRole = None
        """ Competency of the performer.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._performerRole = None
        """ Primitive extension for performerRole. Type `FHIRPrimitiveExtension` """
        
        self.performerType = None
        """ Kind of service performer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._performerType = None
        """ Primitive extension for performerType. Type `FHIRPrimitiveExtension` """
        
        self.reason = None
        """ Why action is to be performed.
        List of `str` items. """
        self._reason = None
        """ Primitive extension for reason. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why is action (not) needed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonLinkId = None
        """ Pointer to specific item.
        List of `str` items. """
        self._reasonLinkId = None
        """ Primitive extension for reasonLinkId. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why is action (not) needed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.requester = None
        """ Who asked for action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._requester = None
        """ Primitive extension for requester. Type `FHIRPrimitiveExtension` """
        
        self.requesterLinkId = None
        """ Pointer to specific item.
        List of `str` items. """
        self._requesterLinkId = None
        """ Primitive extension for requesterLinkId. Type `FHIRPrimitiveExtension` """
        
        self.securityLabelNumber = None
        """ Action restriction numbers.
        List of `int` items. """
        self._securityLabelNumber = None
        """ Primitive extension for securityLabelNumber. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ State of the action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Entity of the action.
        List of `ContractTermActionSubject` items (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type or form of the action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ContractTermAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAction, self).elementProperties()
        js.extend([
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contextLinkId", "contextLinkId", str, True, None, False),
            ("_contextLinkId", "_contextLinkId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("_doNotPerform", "_doNotPerform", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("intent", "intent", codeableconcept.CodeableConcept, False, None, True),
            ("_intent", "_intent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("_linkId", "_linkId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", False),
            ("_occurrenceDateTime", "_occurrenceDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("_occurrencePeriod", "_occurrencePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("_occurrenceTiming", "_occurrenceTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performerLinkId", "performerLinkId", str, True, None, False),
            ("_performerLinkId", "_performerLinkId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performerRole", "performerRole", codeableconcept.CodeableConcept, False, None, False),
            ("_performerRole", "_performerRole", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("_performerType", "_performerType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", str, True, None, False),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonLinkId", "reasonLinkId", str, True, None, False),
            ("_reasonLinkId", "_reasonLinkId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, True, None, False),
            ("_requester", "_requester", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requesterLinkId", "requesterLinkId", str, True, None, False),
            ("_requesterLinkId", "_requesterLinkId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("_securityLabelNumber", "_securityLabelNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", ContractTermActionSubject, True, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ Role type of the agent.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        super(ContractTermActionSubject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermActionSubject, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._answer = None
        """ Primitive extension for answer. Type `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ Quality desctiption of asset.
        Type `str`. """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.context = None
        """ Circumstance of the asset.
        List of `ContractTermAssetContext` items (represented as `dict` in JSON). """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.linkId = None
        """ Pointer to asset text.
        List of `str` items. """
        self._linkId = None
        """ Primitive extension for linkId. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Time period of the asset.
        List of `Period` items (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.periodType = None
        """ Asset availability types.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._periodType = None
        """ Primitive extension for periodType. Type `FHIRPrimitiveExtension` """
        
        self.relationship = None
        """ Kinship of the asset.
        Type `Coding` (represented as `dict` in JSON). """
        self._relationship = None
        """ Primitive extension for relationship. Type `FHIRPrimitiveExtension` """
        
        self.scope = None
        """ Range of asset.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._scope = None
        """ Primitive extension for scope. Type `FHIRPrimitiveExtension` """
        
        self.securityLabelNumber = None
        """ Asset restriction numbers.
        List of `int` items. """
        self._securityLabelNumber = None
        """ Primitive extension for securityLabelNumber. Type `FHIRPrimitiveExtension` """
        
        self.subtype = None
        """ Asset sub-category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._subtype = None
        """ Primitive extension for subtype. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Asset clause or question text.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Asset category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.typeReference = None
        """ Associated entities.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._typeReference = None
        """ Primitive extension for typeReference. Type `FHIRPrimitiveExtension` """
        
        self.usePeriod = None
        """ Time period.
        List of `Period` items (represented as `dict` in JSON). """
        self._usePeriod = None
        """ Primitive extension for usePeriod. Type `FHIRPrimitiveExtension` """
        
        self.valuedItem = None
        """ Contract Valued Item List.
        List of `ContractTermAssetValuedItem` items (represented as `dict` in JSON). """
        self._valuedItem = None
        """ Primitive extension for valuedItem. Type `FHIRPrimitiveExtension` """
        
        super(ContractTermAsset, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAsset, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("_answer", "_answer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("context", "context", ContractTermAssetContext, True, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("_linkId", "_linkId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, True, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("periodType", "periodType", codeableconcept.CodeableConcept, True, None, False),
            ("_periodType", "_periodType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", coding.Coding, False, None, False),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("_scope", "_scope", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("_securityLabelNumber", "_securityLabelNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, True, None, False),
            ("_subtype", "_subtype", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("typeReference", "typeReference", fhirreference.FHIRReference, True, None, False),
            ("_typeReference", "_typeReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usePeriod", "usePeriod", period.Period, True, None, False),
            ("_usePeriod", "_usePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuedItem", "valuedItem", ContractTermAssetValuedItem, True, None, False),
            ("_valuedItem", "_valuedItem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.reference = None
        """ Creator,custodian or owner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Context description.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        super(ContractTermAssetContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetContext, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._effectiveTime = None
        """ Primitive extension for effectiveTime. Type `FHIRPrimitiveExtension` """
        
        self.entityCodeableConcept = None
        """ Contract Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._entityCodeableConcept = None
        """ Primitive extension for entityCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.entityReference = None
        """ Contract Valued Item Type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._entityReference = None
        """ Primitive extension for entityReference. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Contract Valued Item Price Scaling Factor.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Contract Valued Item Number.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.linkId = None
        """ Pointer to specific item.
        List of `str` items. """
        self._linkId = None
        """ Primitive extension for linkId. Type `FHIRPrimitiveExtension` """
        
        self.net = None
        """ Total Contract Valued Item Value.
        Type `Money` (represented as `dict` in JSON). """
        self._net = None
        """ Primitive extension for net. Type `FHIRPrimitiveExtension` """
        
        self.payment = None
        """ Terms of valuation.
        Type `str`. """
        self._payment = None
        """ Primitive extension for payment. Type `FHIRPrimitiveExtension` """
        
        self.paymentDate = None
        """ When payment is due.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._paymentDate = None
        """ Primitive extension for paymentDate. Type `FHIRPrimitiveExtension` """
        
        self.points = None
        """ Contract Valued Item Difficulty Scaling Factor.
        Type `float`. """
        self._points = None
        """ Primitive extension for points. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Count of Contract Valued Items.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.recipient = None
        """ Who will receive payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._recipient = None
        """ Primitive extension for recipient. Type `FHIRPrimitiveExtension` """
        
        self.responsible = None
        """ Who will make payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._responsible = None
        """ Primitive extension for responsible. Type `FHIRPrimitiveExtension` """
        
        self.securityLabelNumber = None
        """ Security Labels that define affected terms.
        List of `int` items. """
        self._securityLabelNumber = None
        """ Primitive extension for securityLabelNumber. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Contract Valued Item fee, charge, or cost.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(ContractTermAssetValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdatetime.FHIRDateTime, False, None, False),
            ("_effectiveTime", "_effectiveTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("_entityCodeableConcept", "_entityCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("_entityReference", "_entityReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("_linkId", "_linkId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("_net", "_net", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payment", "payment", str, False, None, False),
            ("_payment", "_payment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paymentDate", "paymentDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_paymentDate", "_paymentDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("points", "points", float, False, None, False),
            ("_points", "_points", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False),
            ("_recipient", "_recipient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("_responsible", "_responsible", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("_securityLabelNumber", "_securityLabelNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._answer = None
        """ Primitive extension for answer. Type `FHIRPrimitiveExtension` """
        
        self.decision = None
        """ Accepting party choice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._decision = None
        """ Primitive extension for decision. Type `FHIRPrimitiveExtension` """
        
        self.decisionMode = None
        """ How decision is conveyed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._decisionMode = None
        """ Primitive extension for decisionMode. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Offer business ID.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.linkId = None
        """ Pointer to text.
        List of `str` items. """
        self._linkId = None
        """ Primitive extension for linkId. Type `FHIRPrimitiveExtension` """
        
        self.party = None
        """ Offer Recipient.
        List of `ContractTermOfferParty` items (represented as `dict` in JSON). """
        self._party = None
        """ Primitive extension for party. Type `FHIRPrimitiveExtension` """
        
        self.securityLabelNumber = None
        """ Offer restriction numbers.
        List of `int` items. """
        self._securityLabelNumber = None
        """ Primitive extension for securityLabelNumber. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Human readable offer text.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.topic = None
        """ Negotiable offer asset.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._topic = None
        """ Primitive extension for topic. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Contract Offer Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ContractTermOffer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOffer, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("_answer", "_answer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("decision", "decision", codeableconcept.CodeableConcept, False, None, False),
            ("_decision", "_decision", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("decisionMode", "decisionMode", codeableconcept.CodeableConcept, True, None, False),
            ("_decisionMode", "_decisionMode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("_linkId", "_linkId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("party", "party", ContractTermOfferParty, True, None, False),
            ("_party", "_party", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("_securityLabelNumber", "_securityLabelNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("topic", "topic", fhirreference.FHIRReference, False, None, False),
            ("_topic", "_topic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._valueAttachment = None
        """ Primitive extension for valueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ The actual answer response.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCoding = None
        """ The actual answer response.
        Type `Coding` (represented as `dict` in JSON). """
        self._valueCoding = None
        """ Primitive extension for valueCoding. Type `FHIRPrimitiveExtension` """
        
        self.valueDate = None
        """ The actual answer response.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._valueDate = None
        """ Primitive extension for valueDate. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ The actual answer response.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ The actual answer response.
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ The actual answer response.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ The actual answer response.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ The actual answer response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ The actual answer response.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ The actual answer response.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        self.valueUri = None
        """ The actual answer response.
        Type `str`. """
        self._valueUri = None
        """ Primitive extension for valueUri. Type `FHIRPrimitiveExtension` """
        
        super(ContractTermOfferAnswer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOfferAnswer, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("_valueAttachment", "_valueAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("_valueCoding", "_valueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("_valueDate", "_valueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", True),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("_valueReference", "_valueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
            ("_valueTime", "_valueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUri", "valueUri", str, False, "value", True),
            ("_valueUri", "_valueUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ Participant engagement type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        super(ContractTermOfferParty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOfferParty, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.classification = None
        """ Confidentiality Protection.
        Type `Coding` (represented as `dict` in JSON). """
        self._classification = None
        """ Primitive extension for classification. Type `FHIRPrimitiveExtension` """
        
        self.control = None
        """ Handling Instructions.
        List of `Coding` items (represented as `dict` in JSON). """
        self._control = None
        """ Primitive extension for control. Type `FHIRPrimitiveExtension` """
        
        self.number = None
        """ Link to Security Labels.
        List of `int` items. """
        self._number = None
        """ Primitive extension for number. Type `FHIRPrimitiveExtension` """
        
        super(ContractTermSecurityLabel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermSecurityLabel, self).elementProperties()
        js.extend([
            ("category", "category", coding.Coding, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("classification", "classification", coding.Coding, False, None, True),
            ("_classification", "_classification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("control", "control", coding.Coding, True, None, False),
            ("_control", "_control", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("number", "number", int, True, None, False),
            ("_number", "_number", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import fhirtime
from . import identifier
from . import money
from . import period
from . import quantity
from . import signature
from . import timing