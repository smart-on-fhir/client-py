#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8595 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2016-06-26.
#  2016, SMART Health IT.


from . import domainresource

class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.
    
    Financial instrument which may be used to pay for or reimburse health care
    products and services.
    """
    
    resource_name = "Coverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.beneficiaryIdentifier = None
        """ Plan Beneficiary.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.beneficiaryReference = None
        """ Plan Beneficiary.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.bin = None
        """ BIN Number.
        Type `str`. """
        
        self.contract = None
        """ Contract details.
        List of `FHIRReference` items referencing `Contract` (represented as `dict` in JSON). """
        
        self.dependent = None
        """ Dependent number.
        Type `int`. """
        
        self.group = None
        """ An identifier for the group.
        Type `str`. """
        
        self.identifier = None
        """ The primary coverage ID.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.isAgreement = None
        """ Is a Payment Agreement.
        Type `bool`. """
        
        self.issuerIdentifier = None
        """ Identifier for the plan or agreement issuer.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issuerReference = None
        """ Identifier for the plan or agreement issuer.
        Type `FHIRReference` referencing `Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.network = None
        """ Insurer network.
        Type `str`. """
        
        self.period = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """
        
        self.plan = None
        """ An identifier for the plan.
        Type `str`. """
        
        self.planholderIdentifier = None
        """ Plan holder.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.planholderReference = None
        """ Plan holder.
        Type `FHIRReference` referencing `Patient, Organization` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ Beneficiary relationship to Planholder.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ The plan instance or sequence counter.
        Type `int`. """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.subPlan = None
        """ An identifier for the subsection of the plan.
        Type `str`. """
        
        self.type = None
        """ Type of coverage.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("beneficiaryIdentifier", "beneficiaryIdentifier", identifier.Identifier, False, "beneficiary", True),
            ("beneficiaryReference", "beneficiaryReference", fhirreference.FHIRReference, False, "beneficiary", True),
            ("bin", "bin", str, False, None, False),
            ("contract", "contract", fhirreference.FHIRReference, True, None, False),
            ("dependent", "dependent", int, False, None, False),
            ("group", "group", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("isAgreement", "isAgreement", bool, False, None, False),
            ("issuerIdentifier", "issuerIdentifier", identifier.Identifier, False, "issuer", True),
            ("issuerReference", "issuerReference", fhirreference.FHIRReference, False, "issuer", True),
            ("network", "network", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("plan", "plan", str, False, None, False),
            ("planholderIdentifier", "planholderIdentifier", identifier.Identifier, False, "planholder", True),
            ("planholderReference", "planholderReference", fhirreference.FHIRReference, False, "planholder", True),
            ("relationship", "relationship", coding.Coding, False, None, True),
            ("sequence", "sequence", int, False, None, False),
            ("status", "status", str, False, None, True),
            ("subPlan", "subPlan", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


from . import coding
from . import fhirreference
from . import identifier
from . import period
