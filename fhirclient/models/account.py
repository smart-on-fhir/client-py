#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Account) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Account(domainresource.DomainResource):
    """ Tracks balance, charges, for patient or cost center.
    
    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """
    
    resource_type = "Account"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Time window that transactions may be posted to this account.
        Type `Period` (represented as `dict` in JSON). """
        
        self.balance = None
        """ How much is in account?.
        Type `Money` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ The party(s) that are responsible for covering the payment of this
        account, and what order should they be applied to the account.
        List of `AccountCoverage` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Explanation of purpose/use.
        Type `str`. """
        
        self.guarantor = None
        """ Responsible for the account.
        List of `AccountGuarantor` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Account number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Human-readable label.
        Type `str`. """
        
        self.owner = None
        """ Who is responsible?.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Transaction window.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ What is account tied to?.
        Type `FHIRReference` referencing `Patient, Device, Practitioner, Location, HealthcareService, Organization` (represented as `dict` in JSON). """
        
        self.type = None
        """ E.g. patient, expense, depreciation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Account, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend([
            ("active", "active", period.Period, False, None, False),
            ("balance", "balance", money.Money, False, None, False),
            ("coverage", "coverage", AccountCoverage, True, None, False),
            ("description", "description", str, False, None, False),
            ("guarantor", "guarantor", AccountGuarantor, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class AccountCoverage(backboneelement.BackboneElement):
    """ The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """
    
    resource_type = "AccountCoverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        """ The party(s) that are responsible for covering the payment of this
        account.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.priority = None
        """ The priority of the coverage in the context of this account.
        Type `int`. """
        
        super(AccountCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AccountCoverage, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("priority", "priority", int, False, None, False),
        ])
        return js


class AccountGuarantor(backboneelement.BackboneElement):
    """ Responsible for the account.
    
    Parties financially responsible for the account.
    """
    
    resource_type = "AccountGuarantor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.onHold = None
        """ Credit or other hold applied.
        Type `bool`. """
        
        self.party = None
        """ Responsible entity.
        Type `FHIRReference` referencing `Patient, RelatedPerson, Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Guarrantee account during.
        Type `Period` (represented as `dict` in JSON). """
        
        super(AccountGuarantor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AccountGuarantor, self).elementProperties()
        js.extend([
            ("onHold", "onHold", bool, False, None, False),
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
