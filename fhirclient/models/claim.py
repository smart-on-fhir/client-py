#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/Claim) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """
    
    resource_name = "Claim"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.accidentDate = None
        """ Accident Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.accidentLocationAddress = None
        """ Accident Place.
        Type `Address` (represented as `dict` in JSON). """
        
        self.accidentLocationReference = None
        """ Accident Place.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.accidentType = None
        """ Accident Type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.additionalMaterials = None
        """ Additional materials, documents, etc..
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.billablePeriod = None
        """ Period for charge submission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance or medical plan.
        List of `ClaimCoverage` items (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosis = None
        """ Diagnosis.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
        
        self.employmentImpacted = None
        """ Period unable to work.
        Type `Period` (represented as `dict` in JSON). """
        
        self.entererIdentifier = None
        """ Author.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.entererReference = None
        """ Author.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.facilityIdentifier = None
        """ Servicing Facility.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.facilityReference = None
        """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.fundsReserve = None
        """ Funds requested to be reserved.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.hospitalization = None
        """ Period in hospital.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Claim number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interventionException = None
        """ Intervention and exception code (Pharma).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Goods and Services.
        List of `ClaimItem` items (represented as `dict` in JSON). """
        
        self.missingTeeth = None
        """ Only if type = oral.
        List of `ClaimMissingTeeth` items (represented as `dict` in JSON). """
        
        self.occurenceSpanCode = None
        """ Occurrence Span Codes.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.occurrenceCode = None
        """ Occurrence Codes.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.onsetDate = None
        """ Illness, injury or treatable condition date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.onsetPeriod = None
        """ Illness, injury or treatable condition date.
        Type `Period` (represented as `dict` in JSON). """
        
        self.organizationIdentifier = None
        """ Responsible organization.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organizationReference = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalPrescriptionIdentifier = None
        """ Original Prescription.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.originalPrescriptionReference = None
        """ Original Prescription.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patientIdentifier = None
        """ The subject of the Products and Services.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patientReference = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Payee.
        Type `ClaimPayee` (represented as `dict` in JSON). """
        
        self.prescriptionIdentifier = None
        """ Prescription.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.prescriptionReference = None
        """ Prescription.
        Type `FHIRReference` referencing `MedicationOrder, VisionPrescription` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Desired processing priority.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ Procedures performed.
        List of `ClaimProcedure` items (represented as `dict` in JSON). """
        
        self.providerIdentifier = None
        """ Responsible provider.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.providerReference = None
        """ Responsible provider.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.referralIdentifier = None
        """ Treatment Referral.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.referralReference = None
        """ Treatment Referral.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.related = None
        """ Related Claims.
        List of `ClaimRelated` items (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Current specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.specialCondition = None
        """ List of special Conditions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.subType = None
        """ Finer grained claim type information.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.targetIdentifier = None
        """ Insurer.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.targetReference = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.total = None
        """ Total claim cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.type = None
        """ institutional | oral | pharmacy | professional | vision.
        Type `str`. """
        
        self.use = None
        """ complete | proposed | exploratory | other.
        Type `str`. """
        
        self.valueCode = None
        """ Value Codes.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(Claim, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("accidentDate", "accidentDate", fhirdate.FHIRDate, False, None, False),
            ("accidentLocationAddress", "accidentLocationAddress", address.Address, False, "accidentLocation", False),
            ("accidentLocationReference", "accidentLocationReference", fhirreference.FHIRReference, False, "accidentLocation", False),
            ("accidentType", "accidentType", coding.Coding, False, None, False),
            ("additionalMaterials", "additionalMaterials", coding.Coding, True, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("coverage", "coverage", ClaimCoverage, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("employmentImpacted", "employmentImpacted", period.Period, False, None, False),
            ("entererIdentifier", "entererIdentifier", identifier.Identifier, False, "enterer", False),
            ("entererReference", "entererReference", fhirreference.FHIRReference, False, "enterer", False),
            ("facilityIdentifier", "facilityIdentifier", identifier.Identifier, False, "facility", False),
            ("facilityReference", "facilityReference", fhirreference.FHIRReference, False, "facility", False),
            ("fundsReserve", "fundsReserve", coding.Coding, False, None, False),
            ("hospitalization", "hospitalization", period.Period, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interventionException", "interventionException", coding.Coding, True, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("missingTeeth", "missingTeeth", ClaimMissingTeeth, True, None, False),
            ("occurenceSpanCode", "occurenceSpanCode", coding.Coding, True, None, False),
            ("occurrenceCode", "occurrenceCode", coding.Coding, True, None, False),
            ("onsetDate", "onsetDate", fhirdate.FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("organizationIdentifier", "organizationIdentifier", identifier.Identifier, False, "organization", False),
            ("organizationReference", "organizationReference", fhirreference.FHIRReference, False, "organization", False),
            ("originalPrescriptionIdentifier", "originalPrescriptionIdentifier", identifier.Identifier, False, "originalPrescription", False),
            ("originalPrescriptionReference", "originalPrescriptionReference", fhirreference.FHIRReference, False, "originalPrescription", False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("patientIdentifier", "patientIdentifier", identifier.Identifier, False, "patient", True),
            ("patientReference", "patientReference", fhirreference.FHIRReference, False, "patient", True),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("prescriptionIdentifier", "prescriptionIdentifier", identifier.Identifier, False, "prescription", False),
            ("prescriptionReference", "prescriptionReference", fhirreference.FHIRReference, False, "prescription", False),
            ("priority", "priority", coding.Coding, False, None, False),
            ("procedure", "procedure", ClaimProcedure, True, None, False),
            ("providerIdentifier", "providerIdentifier", identifier.Identifier, False, "provider", False),
            ("providerReference", "providerReference", fhirreference.FHIRReference, False, "provider", False),
            ("referralIdentifier", "referralIdentifier", identifier.Identifier, False, "referral", False),
            ("referralReference", "referralReference", fhirreference.FHIRReference, False, "referral", False),
            ("related", "related", ClaimRelated, True, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("specialCondition", "specialCondition", coding.Coding, True, None, False),
            ("subType", "subType", coding.Coding, True, None, False),
            ("targetIdentifier", "targetIdentifier", identifier.Identifier, False, "target", False),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", False),
            ("total", "total", quantity.Quantity, False, None, False),
            ("type", "type", str, False, None, True),
            ("use", "use", str, False, None, False),
            ("valueCode", "valueCode", coding.Coding, True, None, False),
        ])
        return js


from . import backboneelement

class ClaimCoverage(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_name = "ClaimCoverage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.businessArrangement = None
        """ Business agreement.
        Type `str`. """
        
        self.claimResponse = None
        """ Adjudication results.
        Type `FHIRReference` referencing `ClaimResponse` (represented as `dict` in JSON). """
        
        self.coverageIdentifier = None
        """ Insurance information.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.coverageReference = None
        """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.focal = None
        """ Is the focal Coverage.
        Type `bool`. """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        self.sequence = None
        """ Service instance identifier.
        Type `int`. """
        
        super(ClaimCoverage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimCoverage, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverageIdentifier", "coverageIdentifier", identifier.Identifier, False, "coverage", True),
            ("coverageReference", "coverageReference", fhirreference.FHIRReference, False, "coverage", True),
            ("focal", "focal", bool, False, None, True),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Diagnosis.
    
    Ordered list of patient diagnosis for which care is sought.
    """
    
    resource_name = "ClaimDiagnosis"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.diagnosis = None
        """ Patient's list of diagnosis.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Sequence of diagnosis.
        Type `int`. """
        
        super(ClaimDiagnosis, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosis", "diagnosis", coding.Coding, False, None, True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimItem(backboneelement.BackboneElement):
    """ Goods and Services.
    
    First tier of goods and services.
    """
    
    resource_name = "ClaimItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySite = None
        """ Service Location.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Additional items.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisLinkId = None
        """ Diagnosis Link.
        List of `int` items. """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.net = None
        """ Total item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.place = None
        """ Place of service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.prosthesis = None
        """ Prosthetic details.
        Type `ClaimItemProsthesis` (represented as `dict` in JSON). """
        
        self.providerIdentifier = None
        """ Responsible practitioner.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.providerQualification = None
        """ Type, classification or Specialization.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.providerReference = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Item Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.serviceModifier = None
        """ Service/Product modifiers.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.servicedDate = None
        """ Date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ Date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite = None
        """ Service Sub-location.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ClaimItem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
            ("diagnosisLinkId", "diagnosisLinkId", int, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", coding.Coding, True, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("place", "place", coding.Coding, False, None, False),
            ("points", "points", float, False, None, False),
            ("prosthesis", "prosthesis", ClaimItemProsthesis, False, None, False),
            ("providerIdentifier", "providerIdentifier", identifier.Identifier, False, "provider", False),
            ("providerQualification", "providerQualification", coding.Coding, False, None, False),
            ("providerReference", "providerReference", fhirreference.FHIRReference, False, "provider", False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("serviceModifier", "serviceModifier", coding.Coding, True, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second tier of goods and services.
    """
    
    resource_name = "ClaimItemDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Total additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subDetail = None
        """ Additional items.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("factor", "factor", float, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third tier of goods and services.
    """
    
    resource_name = "ClaimItemDetailSubDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Net additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetailSubDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("factor", "factor", float, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ClaimItemProsthesis(backboneelement.BackboneElement):
    """ Prosthetic details.
    
    The materials and placement date of prior fixed prosthesis.
    """
    
    resource_name = "ClaimItemProsthesis"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.initial = None
        """ Is this the initial service.
        Type `bool`. """
        
        self.priorDate = None
        """ Initial service Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.priorMaterial = None
        """ Prosthetic Material.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimItemProsthesis, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimItemProsthesis, self).elementProperties()
        js.extend([
            ("initial", "initial", bool, False, None, False),
            ("priorDate", "priorDate", fhirdate.FHIRDate, False, None, False),
            ("priorMaterial", "priorMaterial", coding.Coding, False, None, False),
        ])
        return js


class ClaimMissingTeeth(backboneelement.BackboneElement):
    """ Only if type = oral.
    
    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """
    
    resource_name = "ClaimMissingTeeth"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.extractionDate = None
        """ Date of Extraction.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reason = None
        """ Reason for missing.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.tooth = None
        """ Tooth Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimMissingTeeth, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimMissingTeeth, self).elementProperties()
        js.extend([
            ("extractionDate", "extractionDate", fhirdate.FHIRDate, False, None, False),
            ("reason", "reason", coding.Coding, False, None, False),
            ("tooth", "tooth", coding.Coding, False, None, True),
        ])
        return js


class ClaimPayee(backboneelement.BackboneElement):
    """ Payee.
    
    The party to be reimbursed for the services.
    """
    
    resource_name = "ClaimPayee"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.partyIdentifier = None
        """ Party to be paid any benefits payable.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.partyReference = None
        """ Party to be paid any benefits payable.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.type = None
        """ Payee type.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimPayee, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("partyIdentifier", "partyIdentifier", identifier.Identifier, False, "party", False),
            ("partyReference", "partyReference", fhirreference.FHIRReference, False, "party", False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class ClaimProcedure(backboneelement.BackboneElement):
    """ Procedures performed.
    
    Ordered list of patient procedures performed to support the adjudication.
    """
    
    resource_name = "ClaimProcedure"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ When the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.procedureCoding = None
        """ Patient's list of procedures performed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.procedureReference = None
        """ Patient's list of procedures performed.
        Type `FHIRReference` referencing `Procedure` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Procedure sequence for reference.
        Type `int`. """
        
        super(ClaimProcedure, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("procedureCoding", "procedureCoding", coding.Coding, False, "procedure", True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimRelated(backboneelement.BackboneElement):
    """ Related Claims.
    
    Other claims which are related to this claim such as prior claim versions
    or for related services.
    """
    
    resource_name = "ClaimRelated"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.claimIdentifier = None
        """ Related Claims.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.claimReference = None
        """ Related Claims.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Related file or case reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ How the reference claim is related.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimRelated, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claimIdentifier", "claimIdentifier", identifier.Identifier, False, "claim", False),
            ("claimReference", "claimReference", fhirreference.FHIRReference, False, "claim", False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("relationship", "relationship", coding.Coding, False, None, False),
        ])
        return js


from . import address
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
