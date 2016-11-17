#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10061 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2016-10-24.
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
        
        self.beneficiary = None
        """ Plan Beneficiary.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.contract = None
        """ Contract details.
        List of `FHIRReference` items referencing `Contract` (represented as `dict` in JSON). """
        
        self.dependent = None
        """ Dependent number.
        Type `int`. """
        
        self.identifier = None
        """ The primary coverage ID.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.isAgreement = None
        """ Is a Payment Agreement.
        Type `bool`. """
        
        self.issuer = None
        """ Identifier for the plan or agreement issuer.
        Type `FHIRReference` referencing `Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.level = None
        """ Additional coverage classifications.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.network = None
        """ Insurer network.
        Type `str`. """
        
        self.period = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """
        
        self.planholder = None
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
        
        self.type = None
        """ Type of coverage.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("beneficiary", "beneficiary", fhirreference.FHIRReference, False, None, True),
            ("contract", "contract", fhirreference.FHIRReference, True, None, False),
            ("dependent", "dependent", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("isAgreement", "isAgreement", bool, False, None, False),
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, True),
            ("level", "level", coding.Coding, True, None, False),
            ("network", "network", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("planholder", "planholder", fhirreference.FHIRReference, False, None, True),
            ("relationship", "relationship", coding.Coding, False, None, True),
            ("sequence", "sequence", int, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


from . import coding
from . import fhirreference
from . import identifier
from . import period
