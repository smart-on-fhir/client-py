#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Contract) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Contract(domainresource.DomainResource):
    """ Legal Agreement.
    
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """
    
    resource_type = "Contract"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Action stipulated by this Contract.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actionReason = None
        """ Rationale for the stiplulated action.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.agent = None
        """ Entity being ascribed responsibility.
        List of `ContractAgent` items (represented as `dict` in JSON). """
        
        self.applies = None
        """ Effective time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.authority = None
        """ Authority under which this Contract has standing.
        List of `FHIRReference` items referencing `Organization` (represented as `dict` in JSON). """
        
        self.bindingAttachment = None
        """ Binding Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.bindingReference = None
        """ Binding Contract.
        Type `FHIRReference` referencing `Composition, DocumentReference, QuestionnaireResponse` (represented as `dict` in JSON). """
        
        self.contentDerivative = None
        """ Content derived from the basal information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.decisionType = None
        """ Decision by Grantor.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.domain = None
        """ Domain in which this Contract applies.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.friendly = None
        """ Contract Friendly Language.
        List of `ContractFriendly` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued = None
        """ When this Contract was issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.legal = None
        """ Contract Legal Language.
        List of `ContractLegal` items (represented as `dict` in JSON). """
        
        self.rule = None
        """ Computable Contract Language.
        List of `ContractRule` items (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ Security Labels that define affected resources.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.signer = None
        """ Contract Signatory.
        List of `ContractSigner` items (represented as `dict` in JSON). """
        
        self.status = None
        """ amended | appended | cancelled | disputed | entered-in-error |
        executable | executed | negotiable | offered | policy | rejected |
        renewed | revoked | resolved | terminated.
        Type `str`. """
        
        self.subType = None
        """ Subtype within the context of type.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Contract Target Entity.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.term = None
        """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.topic = None
        """ Context of the Contract.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type or form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valuedItem = None
        """ Contract Valued Item List.
        List of `ContractValuedItem` items (represented as `dict` in JSON). """
        
        super(Contract, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contract, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actionReason", "actionReason", codeableconcept.CodeableConcept, True, None, False),
            ("agent", "agent", ContractAgent, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("authority", "authority", fhirreference.FHIRReference, True, None, False),
            ("bindingAttachment", "bindingAttachment", attachment.Attachment, False, "binding", False),
            ("bindingReference", "bindingReference", fhirreference.FHIRReference, False, "binding", False),
            ("contentDerivative", "contentDerivative", codeableconcept.CodeableConcept, False, None, False),
            ("decisionType", "decisionType", codeableconcept.CodeableConcept, False, None, False),
            ("domain", "domain", fhirreference.FHIRReference, True, None, False),
            ("friendly", "friendly", ContractFriendly, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("legal", "legal", ContractLegal, True, None, False),
            ("rule", "rule", ContractRule, True, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("signer", "signer", ContractSigner, True, None, False),
            ("status", "status", str, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("term", "term", ContractTerm, True, None, False),
            ("topic", "topic", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valuedItem", "valuedItem", ContractValuedItem, True, None, False),
        ])
        return js


from . import backboneelement

class ContractAgent(backboneelement.BackboneElement):
    """ Entity being ascribed responsibility.
    
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    
    resource_type = "ContractAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Contract Agent Type.
        Type `FHIRReference` referencing `Contract, Device, Group, Location, Organization, Patient, Practitioner, RelatedPerson, Substance` (represented as `dict` in JSON). """
        
        self.role = None
        """ Role type of the agent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ContractAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractAgent, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
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
        Type `FHIRReference` referencing `Composition, DocumentReference, QuestionnaireResponse` (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `Composition, DocumentReference, QuestionnaireResponse` (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `DocumentReference` (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
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
        """ Contract Term Activity.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actionReason = None
        """ Purpose for the Contract Term Action.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.agent = None
        """ Contract Term Agent List.
        List of `ContractTermAgent` items (represented as `dict` in JSON). """
        
        self.applies = None
        """ Contract Term Effective Time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.group = None
        """ Nested Contract Term Group.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract Term Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Contract Term Issue Date Time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.securityLabel = None
        """ Security Labels that define affected terms.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.subType = None
        """ Contract Term Type specific classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Human readable Contract term text.
        Type `str`. """
        
        self.topic = None
        """ Context of the Contract term.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Term Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valuedItem = None
        """ Contract Term Valued Item List.
        List of `ContractTermValuedItem` items (represented as `dict` in JSON). """
        
        super(ContractTerm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actionReason", "actionReason", codeableconcept.CodeableConcept, True, None, False),
            ("agent", "agent", ContractTermAgent, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("group", "group", ContractTerm, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("topic", "topic", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valuedItem", "valuedItem", ContractTermValuedItem, True, None, False),
        ])
        return js


class ContractTermAgent(backboneelement.BackboneElement):
    """ Contract Term Agent List.
    
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    
    resource_type = "ContractTermAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Contract Term Agent Subject.
        Type `FHIRReference` referencing `Contract, Device, Group, Location, Organization, Patient, Practitioner, RelatedPerson, Substance` (represented as `dict` in JSON). """
        
        self.role = None
        """ Type of the Contract Term Agent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ContractTermAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAgent, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ContractTermValuedItem(backboneelement.BackboneElement):
    """ Contract Term Valued Item List.
    
    Contract Provision Valued Item List.
    """
    
    resource_type = "ContractTermValuedItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.effectiveTime = None
        """ Contract Term Valued Item Effective Tiem.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.entityCodeableConcept = None
        """ Contract Term Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.entityReference = None
        """ Contract Term Valued Item Type.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Contract Term Valued Item Price Scaling Factor.
        Type `float`. """
        
        self.identifier = None
        """ Contract Term Valued Item Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.net = None
        """ Total Contract Term Valued Item Value.
        Type `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Contract Term Valued Item Difficulty Scaling Factor.
        Type `float`. """
        
        self.quantity = None
        """ Contract Term Valued Item Count.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Contract Term Valued Item fee, charge, or cost.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ContractTermValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdate.FHIRDate, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ContractValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item List.
    """
    
    resource_type = "ContractValuedItem"
    
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
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Contract Valued Item Price Scaling Factor.
        Type `float`. """
        
        self.identifier = None
        """ Contract Valued Item Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.net = None
        """ Total Contract Valued Item Value.
        Type `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Contract Valued Item Difficulty Scaling Factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Contract Valued Items.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Contract Valued Item fee, charge, or cost.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ContractValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdate.FHIRDate, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
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
