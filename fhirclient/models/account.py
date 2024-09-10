# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Account).
# 2024, SMART Health IT.


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
        
        self.coverage = None
        """ The party(s) that are responsible for covering the payment of this
        account, and what order should they be applied to the account.
        List of `AccountCoverage` items (represented as `dict` in JSON). """
        self._coverage = None
        """ Primitive extension for coverage. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Explanation of purpose/use.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.guarantor = None
        """ The parties ultimately responsible for balancing the Account.
        List of `AccountGuarantor` items (represented as `dict` in JSON). """
        self._guarantor = None
        """ Primitive extension for guarantor. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Account number.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Human-readable label.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.owner = None
        """ Entity managing the Account.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._owner = None
        """ Primitive extension for owner. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Reference to a parent Account.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.servicePeriod = None
        """ Transaction window.
        Type `Period` (represented as `dict` in JSON). """
        self._servicePeriod = None
        """ Primitive extension for servicePeriod. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | inactive | entered-in-error | on-hold | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ The entity that caused the expenses.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ E.g. patient, expense, depreciation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Account, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend([
            ("coverage", "coverage", AccountCoverage, True, None, False),
            ("_coverage", "_coverage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("guarantor", "guarantor", AccountGuarantor, True, None, False),
            ("_guarantor", "_guarantor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("_owner", "_owner", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("servicePeriod", "servicePeriod", period.Period, False, None, False),
            ("_servicePeriod", "_servicePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        """ The party(s), such as insurances, that may contribute to the
        payment of this account.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._coverage = None
        """ Primitive extension for coverage. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ The priority of the coverage in the context of this account.
        Type `int`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        super(AccountCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AccountCoverage, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("_coverage", "_coverage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", int, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class AccountGuarantor(backboneelement.BackboneElement):
    """ The parties ultimately responsible for balancing the Account.
    
    The parties responsible for balancing the account if other payment options
    fall short.
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
        self._onHold = None
        """ Primitive extension for onHold. Type `FHIRPrimitiveExtension` """
        
        self.party = None
        """ Responsible entity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._party = None
        """ Primitive extension for party. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Guarantee account during.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        super(AccountGuarantor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AccountGuarantor, self).elementProperties()
        js.extend([
            ("onHold", "onHold", bool, False, None, False),
            ("_onHold", "_onHold", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("_party", "_party", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period