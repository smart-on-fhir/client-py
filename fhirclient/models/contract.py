#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Contract) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Contract(domainresource.DomainResource):
    """ Contract.
    
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """
    
    resource_name = "Contract"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Contract Action.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actionReason = None
        """ Contract Action Reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ Contract Actor.
        List of `ContractActor` items (represented as `dict` in JSON). """
        
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
        
        self.domain = None
        """ Domain in which this Contract applies.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.friendly = None
        """ Contract Friendly Language.
        List of `ContractFriendly` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract identifier.
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
        
        self.signer = None
        """ Contract Signer.
        List of `ContractSigner` items (represented as `dict` in JSON). """
        
        self.subType = None
        """ Contract Subtype.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Subject of this Contract.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.term = None
        """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Contract Tyoe.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valuedItem = None
        """ Contract Valued Item.
        List of `ContractValuedItem` items (represented as `dict` in JSON). """
        
        super(Contract, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contract, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actionReason", "actionReason", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", ContractActor, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("authority", "authority", fhirreference.FHIRReference, True, None, False),
            ("bindingAttachment", "bindingAttachment", attachment.Attachment, False, "binding", False),
            ("bindingReference", "bindingReference", fhirreference.FHIRReference, False, "binding", False),
            ("domain", "domain", fhirreference.FHIRReference, True, None, False),
            ("friendly", "friendly", ContractFriendly, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("legal", "legal", ContractLegal, True, None, False),
            ("rule", "rule", ContractRule, True, None, False),
            ("signer", "signer", ContractSigner, True, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("term", "term", ContractTerm, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valuedItem", "valuedItem", ContractValuedItem, True, None, False),
        ])
        return js


from . import backboneelement

class ContractActor(backboneelement.BackboneElement):
    """ Contract Actor.
    
    List of Contract actors.
    """
    
    resource_name = "ContractActor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.entity = None
        """ Contract Actor Type.
        Type `FHIRReference` referencing `Contract, Device, Group, Location, Organization, Patient, Practitioner, RelatedPerson, Substance` (represented as `dict` in JSON). """
        
        self.role = None
        """ Contract  Actor Role.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ContractActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractActor, self).elementProperties()
        js.extend([
            ("entity", "entity", fhirreference.FHIRReference, False, None, True),
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
    
    resource_name = "ContractFriendly"
    
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
    
    resource_name = "ContractLegal"
    
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
    
    resource_name = "ContractRule"
    
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
    """ Contract Signer.
    
    Party signing this Contract.
    """
    
    resource_name = "ContractSigner"
    
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
        Type `str`. """
        
        self.type = None
        """ Contract Signer Type.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ContractSigner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractSigner, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("signature", "signature", str, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class ContractTerm(backboneelement.BackboneElement):
    """ Contract Term List.
    
    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    
    resource_name = "ContractTerm"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Contract Term Action.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actionReason = None
        """ Contract Term Action Reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ Contract Term Actor List.
        List of `ContractTermActor` items (represented as `dict` in JSON). """
        
        self.applies = None
        """ Contract Term Effective Time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.group = None
        """ Nested Contract Term Group.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract Term identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Contract Term Issue Date Time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subType = None
        """ Contract Term Subtype.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Subject of this Contract Term.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.text = None
        """ Human readable Contract term text.
        Type `str`. """
        
        self.type = None
        """ Contract Term Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valuedItem = None
        """ Contract Term Valued Item.
        List of `ContractTermValuedItem` items (represented as `dict` in JSON). """
        
        super(ContractTerm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actionReason", "actionReason", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", ContractTermActor, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("group", "group", ContractTerm, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valuedItem", "valuedItem", ContractTermValuedItem, True, None, False),
        ])
        return js


class ContractTermActor(backboneelement.BackboneElement):
    """ Contract Term Actor List.
    
    List of actors participating in this Contract Provision.
    """
    
    resource_name = "ContractTermActor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.entity = None
        """ Contract Term Actor.
        Type `FHIRReference` referencing `Contract, Device, Group, Location, Organization, Patient, Practitioner, RelatedPerson, Substance` (represented as `dict` in JSON). """
        
        self.role = None
        """ Contract Term Actor Role.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ContractTermActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermActor, self).elementProperties()
        js.extend([
            ("entity", "entity", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ContractTermValuedItem(backboneelement.BackboneElement):
    """ Contract Term Valued Item.
    
    Contract Provision Valued Item List.
    """
    
    resource_name = "ContractTermValuedItem"
    
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
        """ Contract Term Valued Item Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.net = None
        """ Total Contract Term Valued Item Value.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Contract Term Valued Item Difficulty Scaling Factor.
        Type `float`. """
        
        self.quantity = None
        """ Contract Term Valued Item Count.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Contract Term Valued Item fee, charge, or cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ContractTermValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdate.FHIRDate, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ContractValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item.
    
    Contract Valued Item List.
    """
    
    resource_name = "ContractValuedItem"
    
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
        """ Contract Valued Item Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.net = None
        """ Total Contract Valued Item Value.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Contract Valued Item Difficulty Scaling Factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Contract Valued Items.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Contract Valued Item fee, charge, or cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ContractValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdate.FHIRDate, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
