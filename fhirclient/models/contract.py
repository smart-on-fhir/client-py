#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (contract.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import attachment
import codeableconcept
import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import money
import period
import quantity


class Contract(fhirresource.FHIRResource):
    """ A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters..
    
    A formal agreement between parties regarding the conduct of business,
    exchange of information or other matters.
    """
    
    resource_name = "Contract"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.applies = None
        """ Effective time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.author = None
        """ Contract author or responsible party.
        List of `FHIRReference` items referencing `Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON). """
        
        self.authority = None
        """ Authority.
        List of `FHIRReference` items referencing `Organization` (represented as `dict` in JSON). """
        
        self.binding = None
        """ Binding Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.bindingDateTime = None
        """ Binding Contract effective time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.domain = None
        """ Domain.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.executor = None
        """ Trustee.
        List of `FHIRReference` items referencing `Practitioner, RelatedPerson, Organization, Patient` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.friendly = None
        """ Human readable contract text.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.friendlyDateTime = None
        """ Human readable contract text effective time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.grantee = None
        """ Second Party or delegatee.
        List of `FHIRReference` items referencing `Practitioner, RelatedPerson, Organization, Patient` (represented as `dict` in JSON). """
        
        self.grantor = None
        """ First Party or delegator.
        List of `FHIRReference` items referencing `Practitioner, RelatedPerson, Organization, Patient` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Contract identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issued = None
        """ When this was issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.legal = None
        """ Legal contract text.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.legalDateTime = None
        """ Legal contract text date time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.notary = None
        """ Notary Public.
        List of `FHIRReference` items referencing `Practitioner, RelatedPerson, Organization, Patient` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rule = None
        """ Computable contract text.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.ruleDateTime = None
        """ Computable contract text effect time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.signer = None
        """ Signer.
        List of `ContractSigner` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Subject.
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.subtype = None
        """ Subtype of contract.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.term = None
        """ The terms of the Contract.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of contract.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        self.witness = None
        """ Witness to the contract.
        List of `FHIRReference` items referencing `Practitioner, RelatedPerson, Patient` (represented as `dict` in JSON). """
        
        super(Contract, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Contract, self).update_with_json(jsondict)
        if 'applies' in jsondict:
            self.applies = period.Period.with_json_and_owner(jsondict['applies'], self)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'authority' in jsondict:
            self.authority = fhirreference.FHIRReference.with_json_and_owner(jsondict['authority'], self)
        if 'binding' in jsondict:
            self.binding = attachment.Attachment.with_json_and_owner(jsondict['binding'], self)
        if 'bindingDateTime' in jsondict:
            self.bindingDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['bindingDateTime'], self)
        if 'domain' in jsondict:
            self.domain = fhirreference.FHIRReference.with_json_and_owner(jsondict['domain'], self)
        if 'executor' in jsondict:
            self.executor = fhirreference.FHIRReference.with_json_and_owner(jsondict['executor'], self)
        if 'factor' in jsondict:
            self.factor = jsondict['factor']
        if 'friendly' in jsondict:
            self.friendly = attachment.Attachment.with_json_and_owner(jsondict['friendly'], self)
        if 'friendlyDateTime' in jsondict:
            self.friendlyDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['friendlyDateTime'], self)
        if 'grantee' in jsondict:
            self.grantee = fhirreference.FHIRReference.with_json_and_owner(jsondict['grantee'], self)
        if 'grantor' in jsondict:
            self.grantor = fhirreference.FHIRReference.with_json_and_owner(jsondict['grantor'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'issued' in jsondict:
            self.issued = fhirdate.FHIRDate.with_json_and_owner(jsondict['issued'], self)
        if 'legal' in jsondict:
            self.legal = attachment.Attachment.with_json_and_owner(jsondict['legal'], self)
        if 'legalDateTime' in jsondict:
            self.legalDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['legalDateTime'], self)
        if 'net' in jsondict:
            self.net = money.Money.with_json_and_owner(jsondict['net'], self)
        if 'notary' in jsondict:
            self.notary = fhirreference.FHIRReference.with_json_and_owner(jsondict['notary'], self)
        if 'points' in jsondict:
            self.points = jsondict['points']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'rule' in jsondict:
            self.rule = attachment.Attachment.with_json_and_owner(jsondict['rule'], self)
        if 'ruleDateTime' in jsondict:
            self.ruleDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['ruleDateTime'], self)
        if 'signer' in jsondict:
            self.signer = ContractSigner.with_json_and_owner(jsondict['signer'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'subtype' in jsondict:
            self.subtype = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['subtype'], self)
        if 'term' in jsondict:
            self.term = ContractTerm.with_json_and_owner(jsondict['term'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'unitPrice' in jsondict:
            self.unitPrice = money.Money.with_json_and_owner(jsondict['unitPrice'], self)
        if 'witness' in jsondict:
            self.witness = fhirreference.FHIRReference.with_json_and_owner(jsondict['witness'], self)


class ContractSigner(fhirelement.FHIRElement):
    """ Signer.
    
    List or contract signatures.
    """
    
    resource_name = "ContractSigner"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.signature = None
        """ Documentation Signature.
        Type `str`. """
        
        self.type = None
        """ Signer Type.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(ContractSigner, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractSigner, self).update_with_json(jsondict)
        if 'signature' in jsondict:
            self.signature = jsondict['signature']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)


class ContractTerm(fhirelement.FHIRElement):
    """ The terms of the Contract.
    
    The itemized terms of the contract. The legal clause or conditions of the
    Contract that requires or prevents either one or both parties to perform a
    particular requirement by some specified time.
    """
    
    resource_name = "ContractTerm"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.applies = None
        """ When effective.
        Type `Period` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.identifier = None
        """ Term identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued = None
        """ When issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Subject for the Term.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.subtype = None
        """ Term subtype.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Human readable Term text.
        Type `str`. """
        
        self.type = None
        """ Term type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ContractTerm, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContractTerm, self).update_with_json(jsondict)
        if 'applies' in jsondict:
            self.applies = period.Period.with_json_and_owner(jsondict['applies'], self)
        if 'factor' in jsondict:
            self.factor = jsondict['factor']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'issued' in jsondict:
            self.issued = fhirdate.FHIRDate.with_json_and_owner(jsondict['issued'], self)
        if 'net' in jsondict:
            self.net = money.Money.with_json_and_owner(jsondict['net'], self)
        if 'points' in jsondict:
            self.points = jsondict['points']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'subtype' in jsondict:
            self.subtype = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['subtype'], self)
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'unitPrice' in jsondict:
            self.unitPrice = money.Money.with_json_and_owner(jsondict['unitPrice'], self)

