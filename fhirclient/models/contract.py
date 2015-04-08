#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Contract) on 2015-04-08.
#  2015, SMART Health IT.


import attachment
import codeableconcept
import coding
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import money
import period
import quantity


class Contract(domainresource.DomainResource):
    """ Contract.
    
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """
    
    resource_name = "Contract"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        Type `FHIRReference` referencing `Composition, DocumentReference, QuestionnaireAnswers` (represented as `dict` in JSON). """
        
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
        
        super(Contract, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Contract, self).update_with_json(jsondict)
        if 'action' in jsondict:
            self.action = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['action'], self)
        if 'actionReason' in jsondict:
            self.actionReason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['actionReason'], self)
        if 'actor' in jsondict:
            self.actor = ContractActor.with_json_and_owner(jsondict['actor'], self)
        if 'applies' in jsondict:
            self.applies = period.Period.with_json_and_owner(jsondict['applies'], self)
        if 'authority' in jsondict:
            self.authority = fhirreference.FHIRReference.with_json_and_owner(jsondict['authority'], self)
        if 'bindingAttachment' in jsondict:
            self.bindingAttachment = attachment.Attachment.with_json_and_owner(jsondict['bindingAttachment'], self)
        if 'bindingReference' in jsondict:
            self.bindingReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['bindingReference'], self)
        if 'domain' in jsondict:
            self.domain = fhirreference.FHIRReference.with_json_and_owner(jsondict['domain'], self)
        if 'friendly' in jsondict:
            self.friendly = ContractFriendly.with_json_and_owner(jsondict['friendly'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'issued' in jsondict:
            self.issued = fhirdate.FHIRDate.with_json_and_owner(jsondict['issued'], self)
        if 'legal' in jsondict:
            self.legal = ContractLegal.with_json_and_owner(jsondict['legal'], self)
        if 'rule' in jsondict:
            self.rule = ContractRule.with_json_and_owner(jsondict['rule'], self)
        if 'signer' in jsondict:
            self.signer = ContractSigner.with_json_and_owner(jsondict['signer'], self)
        if 'subType' in jsondict:
            self.subType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['subType'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'term' in jsondict:
            self.term = ContractTerm.with_json_and_owner(jsondict['term'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'valuedItem' in jsondict:
            self.valuedItem = ContractValuedItem.with_json_and_owner(jsondict['valuedItem'], self)


class ContractActor(fhirelement.FHIRElement):
    """ Contract Actor.
    
    List of Contract actors.
    """
    
    resource_name = "ContractActor"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.entity = None
        """ Contract Actor Type.
        Type `FHIRReference` referencing `Contract, Device, Group, Location, Organization, Patient, Practitioner, RelatedPerson, Substance, Supply` (represented as `dict` in JSON). """
        
        self.role = None
        """ Contract  Actor Role.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ContractActor, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractActor, self).update_with_json(jsondict)
        if 'entity' in jsondict:
            self.entity = fhirreference.FHIRReference.with_json_and_owner(jsondict['entity'], self)
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['role'], self)


class ContractFriendly(fhirelement.FHIRElement):
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
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contentAttachment = None
        """ Easily comprehended representation of this Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Easily comprehended representation of this Contract.
        Type `FHIRReference` referencing `Composition, DocumentReference, QuestionnaireAnswers` (represented as `dict` in JSON). """
        
        super(ContractFriendly, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractFriendly, self).update_with_json(jsondict)
        if 'contentAttachment' in jsondict:
            self.contentAttachment = attachment.Attachment.with_json_and_owner(jsondict['contentAttachment'], self)
        if 'contentReference' in jsondict:
            self.contentReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['contentReference'], self)


class ContractLegal(fhirelement.FHIRElement):
    """ Contract Legal Language.
    
    List of Legal expressions or representations of this Contract.
    """
    
    resource_name = "ContractLegal"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contentAttachment = None
        """ Contract Legal Text.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Contract Legal Text.
        Type `FHIRReference` referencing `Composition, DocumentReference, QuestionnaireAnswers` (represented as `dict` in JSON). """
        
        super(ContractLegal, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractLegal, self).update_with_json(jsondict)
        if 'contentAttachment' in jsondict:
            self.contentAttachment = attachment.Attachment.with_json_and_owner(jsondict['contentAttachment'], self)
        if 'contentReference' in jsondict:
            self.contentReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['contentReference'], self)


class ContractRule(fhirelement.FHIRElement):
    """ Computable Contract Language.
    
    List of Computable Policy Rule Language Representations of this Contract.
    """
    
    resource_name = "ContractRule"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contentAttachment = None
        """ Computable Contract Rules.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Computable Contract Rules.
        Type `FHIRReference` referencing `DocumentReference` (represented as `dict` in JSON). """
        
        super(ContractRule, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractRule, self).update_with_json(jsondict)
        if 'contentAttachment' in jsondict:
            self.contentAttachment = attachment.Attachment.with_json_and_owner(jsondict['contentAttachment'], self)
        if 'contentReference' in jsondict:
            self.contentReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['contentReference'], self)


class ContractSigner(fhirelement.FHIRElement):
    """ Contract Signer.
    
    Party signing this Contract.
    """
    
    resource_name = "ContractSigner"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(ContractSigner, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractSigner, self).update_with_json(jsondict)
        if 'party' in jsondict:
            self.party = fhirreference.FHIRReference.with_json_and_owner(jsondict['party'], self)
        if 'signature' in jsondict:
            self.signature = jsondict['signature']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)


class ContractTerm(fhirelement.FHIRElement):
    """ Contract Term List.
    
    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    
    resource_name = "ContractTerm"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        self.term = None
        """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Human readable Contract term text.
        Type `str`. """
        
        self.type = None
        """ Contract Term Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valuedItem = None
        """ Contract Term Valued Item.
        List of `ContractTermValuedItem` items (represented as `dict` in JSON). """
        
        super(ContractTerm, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractTerm, self).update_with_json(jsondict)
        if 'action' in jsondict:
            self.action = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['action'], self)
        if 'actionReason' in jsondict:
            self.actionReason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['actionReason'], self)
        if 'actor' in jsondict:
            self.actor = ContractTermActor.with_json_and_owner(jsondict['actor'], self)
        if 'applies' in jsondict:
            self.applies = period.Period.with_json_and_owner(jsondict['applies'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'issued' in jsondict:
            self.issued = fhirdate.FHIRDate.with_json_and_owner(jsondict['issued'], self)
        if 'subType' in jsondict:
            self.subType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['subType'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'term' in jsondict:
            self.term = ContractTerm.with_json_and_owner(jsondict['term'], self)
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'valuedItem' in jsondict:
            self.valuedItem = ContractTermValuedItem.with_json_and_owner(jsondict['valuedItem'], self)


class ContractTermActor(fhirelement.FHIRElement):
    """ Contract Term Actor List.
    
    List of actors participating in this Contract Provision.
    """
    
    resource_name = "ContractTermActor"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.entity = None
        """ Contract Term Actor.
        Type `FHIRReference` referencing `Contract, Device, Group, Location, Organization, Patient, Practitioner, RelatedPerson, Substance, Supply` (represented as `dict` in JSON). """
        
        self.role = None
        """ Contract Term Actor Role.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ContractTermActor, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractTermActor, self).update_with_json(jsondict)
        if 'entity' in jsondict:
            self.entity = fhirreference.FHIRReference.with_json_and_owner(jsondict['entity'], self)
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['role'], self)


class ContractTermValuedItem(fhirelement.FHIRElement):
    """ Contract Term Valued Item.
    
    Contract Provision Valued Item List.
    """
    
    resource_name = "ContractTermValuedItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(ContractTermValuedItem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractTermValuedItem, self).update_with_json(jsondict)
        if 'effectiveTime' in jsondict:
            self.effectiveTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['effectiveTime'], self)
        if 'entityCodeableConcept' in jsondict:
            self.entityCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['entityCodeableConcept'], self)
        if 'entityReference' in jsondict:
            self.entityReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['entityReference'], self)
        if 'factor' in jsondict:
            self.factor = jsondict['factor']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'net' in jsondict:
            self.net = money.Money.with_json_and_owner(jsondict['net'], self)
        if 'points' in jsondict:
            self.points = jsondict['points']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'unitPrice' in jsondict:
            self.unitPrice = money.Money.with_json_and_owner(jsondict['unitPrice'], self)


class ContractValuedItem(fhirelement.FHIRElement):
    """ Contract Valued Item.
    
    Contract Valued Item List.
    """
    
    resource_name = "ContractValuedItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(ContractValuedItem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractValuedItem, self).update_with_json(jsondict)
        if 'effectiveTime' in jsondict:
            self.effectiveTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['effectiveTime'], self)
        if 'entityCodeableConcept' in jsondict:
            self.entityCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['entityCodeableConcept'], self)
        if 'entityReference' in jsondict:
            self.entityReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['entityReference'], self)
        if 'factor' in jsondict:
            self.factor = jsondict['factor']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'net' in jsondict:
            self.net = money.Money.with_json_and_owner(jsondict['net'], self)
        if 'points' in jsondict:
            self.points = jsondict['points']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'unitPrice' in jsondict:
            self.unitPrice = money.Money.with_json_and_owner(jsondict['unitPrice'], self)

