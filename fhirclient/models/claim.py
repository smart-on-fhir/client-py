#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Claim) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """
    
    resource_type = "Claim"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident = None
        """ Details about an accident.
        Type `ClaimAccident` (represented as `dict` in JSON). """
        
        self.billablePeriod = None
        """ Period for charge submission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ Members of the care team.
        List of `ClaimCareTeam` items (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosis = None
        """ List of Diagnosis.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
        
        self.employmentImpacted = None
        """ Period unable to work.
        Type `Period` (represented as `dict` in JSON). """
        
        self.enterer = None
        """ Author.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.facility = None
        """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.fundsReserve = None
        """ Funds requested to be reserved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.hospitalization = None
        """ Period in hospital.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Claim number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.information = None
        """ Exceptions, special considerations, the condition, situation, prior
        or concurrent issues.
        List of `ClaimInformation` items (represented as `dict` in JSON). """
        
        self.insurance = None
        """ Insurance or medical plan.
        List of `ClaimInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        """ Target.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.item = None
        """ Goods and Services.
        List of `ClaimItem` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalPrescription = None
        """ Original prescription if superceded by fulfiller.
        Type `FHIRReference` referencing `MedicationRequest` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Party to be paid any benefits payable.
        Type `ClaimPayee` (represented as `dict` in JSON). """
        
        self.prescription = None
        """ Prescription authorizing services or products.
        Type `FHIRReference` referencing `MedicationRequest, VisionPrescription` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Desired processing priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ Procedures performed.
        List of `ClaimProcedure` items (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible provider.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.referral = None
        """ Treatment Referral.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.related = None
        """ Related Claims which may be revelant to processing this claimn.
        List of `ClaimRelated` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.subType = None
        """ Finer grained claim type information.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.total = None
        """ Total claim cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type or discipline.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        """ complete | proposed | exploratory | other.
        Type `str`. """
        
        super(Claim, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("accident", "accident", ClaimAccident, False, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("careTeam", "careTeam", ClaimCareTeam, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("employmentImpacted", "employmentImpacted", period.Period, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("hospitalization", "hospitalization", period.Period, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("information", "information", ClaimInformation, True, None, False),
            ("insurance", "insurance", ClaimInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("procedure", "procedure", ClaimProcedure, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("related", "related", ClaimRelated, True, None, False),
            ("status", "status", str, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False),
            ("total", "total", money.Money, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("use", "use", str, False, None, False),
        ])
        return js


from . import backboneelement

class ClaimAccident(backboneelement.BackboneElement):
    """ Details about an accident.
    
    An accident which resulted in the need for healthcare services.
    """
    
    resource_type = "ClaimAccident"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the accident occurred
        see information codes
        see information codes.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.locationAddress = None
        """ Accident Place.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationReference = None
        """ Accident Place.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.type = None
        """ The nature of the accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimAccident, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimCareTeam(backboneelement.BackboneElement):
    """ Members of the care team.
    
    The members of the team who provided the overall service as well as their
    role and whether responsible and qualifications.
    """
    
    resource_type = "ClaimCareTeam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.provider = None
        """ Provider individual or organization.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.qualification = None
        """ Type, classification or Specialization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Billing provider.
        Type `bool`. """
        
        self.role = None
        """ Role on the team.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Number to covey order of careTeam.
        Type `int`. """
        
        super(ClaimCareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("qualification", "qualification", codeableconcept.CodeableConcept, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ List of Diagnosis.
    
    List of patient diagnosis for which care is sought.
    """
    
    resource_type = "ClaimDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosisCodeableConcept = None
        """ Patient's diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnosisReference = None
        """ Patient's diagnosis.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.packageCode = None
        """ Package billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Number to covey order of diagnosis.
        Type `int`. """
        
        self.type = None
        """ Timing or nature of the diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", True),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", True),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ClaimInformation(backboneelement.BackboneElement):
    """ Exceptions, special considerations, the condition, situation, prior or
    concurrent issues.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues. Often there are
    mutiple jurisdiction specific valuesets which are required.
    """
    
    resource_type = "ClaimInformation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ General class of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Type of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Reason associated with the information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Information instance identifier.
        Type `int`. """
        
        self.timingDate = None
        """ When it occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ When it occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Additional Data or supporting information.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Additional Data or supporting information.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Additional Data or supporting information.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Additional Data or supporting information.
        Type `str`. """
        
        super(ClaimInformation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimInformation, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
        ])
        return js


class ClaimInsurance(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_type = "ClaimInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement = None
        """ Business agreement.
        Type `str`. """
        
        self.claimResponse = None
        """ Adjudication results.
        Type `FHIRReference` referencing `ClaimResponse` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.focal = None
        """ Is the focal Coverage.
        Type `bool`. """
        
        self.preAuthRef = None
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        self.sequence = None
        """ Service instance identifier.
        Type `int`. """
        
        super(ClaimInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimItem(backboneelement.BackboneElement):
    """ Goods and Services.
    
    First tier of goods and services.
    """
    
    resource_type = "ClaimItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite = None
        """ Service Location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.careTeamLinkId = None
        """ Applicable careTeam members.
        List of `int` items. """
        
        self.category = None
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Additional items.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisLinkId = None
        """ Applicable diagnoses.
        List of `int` items. """
        
        self.encounter = None
        """ Encounters related to this billed item.
        List of `FHIRReference` items referencing `Encounter` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.informationLinkId = None
        """ Applicable exception and supporting information.
        List of `int` items. """
        
        self.locationAddress = None
        """ Place of service.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationCodeableConcept = None
        """ Place of service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationReference = None
        """ Place of service.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.procedureLinkId = None
        """ Applicable procedures.
        List of `int` items. """
        
        self.programCode = None
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.servicedDate = None
        """ Date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ Date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite = None
        """ Service Sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("careTeamLinkId", "careTeamLinkId", int, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
            ("diagnosisLinkId", "diagnosisLinkId", int, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("informationLinkId", "informationLinkId", int, True, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("procedureLinkId", "procedureLinkId", int, True, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", codeableconcept.CodeableConcept, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second tier of goods and services.
    """
    
    resource_type = "ClaimItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        """ Total additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.programCode = None
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subDetail = None
        """ Additional items.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", codeableconcept.CodeableConcept, False, None, False),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third tier of goods and services.
    """
    
    resource_type = "ClaimItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net = None
        """ Net additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.programCode = None
        """ Program specific reason for item inclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Billing Code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", codeableconcept.CodeableConcept, False, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimPayee(backboneelement.BackboneElement):
    """ Party to be paid any benefits payable.
    
    The party to be reimbursed for the services.
    """
    
    resource_type = "ClaimPayee"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party = None
        """ Party to receive the payable.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.resourceType = None
        """ organization | patient | practitioner | relatedperson.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of party: Subscriber, Provider, other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("resourceType", "resourceType", coding.Coding, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ClaimProcedure(backboneelement.BackboneElement):
    """ Procedures performed.
    
    Ordered list of patient procedures performed to support the adjudication.
    """
    
    resource_type = "ClaimProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.procedureCodeableConcept = None
        """ Patient's list of procedures performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedureReference = None
        """ Patient's list of procedures performed.
        Type `FHIRReference` referencing `Procedure` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Procedure sequence for reference.
        Type `int`. """
        
        super(ClaimProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, False, "procedure", True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimRelated(backboneelement.BackboneElement):
    """ Related Claims which may be revelant to processing this claimn.
    
    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """
    
    resource_type = "ClaimRelated"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.claim = None
        """ Reference to the related claim.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Related file or case reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ How the reference claim is related.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
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
