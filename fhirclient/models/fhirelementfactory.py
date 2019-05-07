#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    
    @classmethod
    def instantiate(cls, resource_type, jsondict):
        """ Instantiate a resource of the type correlating to "resource_type".
        
        :param str resource_type: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :returns: A resource of the respective type or `Element`
        """
        if "Account" == resource_type:
            from . import account
            return account.Account(jsondict)
        if "AccountCoverage" == resource_type:
            from . import account
            return account.AccountCoverage(jsondict)
        if "AccountGuarantor" == resource_type:
            from . import account
            return account.AccountGuarantor(jsondict)
        if "ActivityDefinition" == resource_type:
            from . import activitydefinition
            return activitydefinition.ActivityDefinition(jsondict)
        if "ActivityDefinitionDynamicValue" == resource_type:
            from . import activitydefinition
            return activitydefinition.ActivityDefinitionDynamicValue(jsondict)
        if "ActivityDefinitionParticipant" == resource_type:
            from . import activitydefinition
            return activitydefinition.ActivityDefinitionParticipant(jsondict)
        if "Address" == resource_type:
            from . import address
            return address.Address(jsondict)
        if "AdverseEvent" == resource_type:
            from . import adverseevent
            return adverseevent.AdverseEvent(jsondict)
        if "AdverseEventSuspectEntity" == resource_type:
            from . import adverseevent
            return adverseevent.AdverseEventSuspectEntity(jsondict)
        if "AdverseEventSuspectEntityCausality" == resource_type:
            from . import adverseevent
            return adverseevent.AdverseEventSuspectEntityCausality(jsondict)
        if "Age" == resource_type:
            from . import age
            return age.Age(jsondict)
        if "AllergyIntolerance" == resource_type:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntolerance(jsondict)
        if "AllergyIntoleranceReaction" == resource_type:
            from . import allergyintolerance
            return allergyintolerance.AllergyIntoleranceReaction(jsondict)
        if "Annotation" == resource_type:
            from . import annotation
            return annotation.Annotation(jsondict)
        if "Appointment" == resource_type:
            from . import appointment
            return appointment.Appointment(jsondict)
        if "AppointmentParticipant" == resource_type:
            from . import appointment
            return appointment.AppointmentParticipant(jsondict)
        if "AppointmentResponse" == resource_type:
            from . import appointmentresponse
            return appointmentresponse.AppointmentResponse(jsondict)
        if "Attachment" == resource_type:
            from . import attachment
            return attachment.Attachment(jsondict)
        if "AuditEvent" == resource_type:
            from . import auditevent
            return auditevent.AuditEvent(jsondict)
        if "AuditEventAgent" == resource_type:
            from . import auditevent
            return auditevent.AuditEventAgent(jsondict)
        if "AuditEventAgentNetwork" == resource_type:
            from . import auditevent
            return auditevent.AuditEventAgentNetwork(jsondict)
        if "AuditEventEntity" == resource_type:
            from . import auditevent
            return auditevent.AuditEventEntity(jsondict)
        if "AuditEventEntityDetail" == resource_type:
            from . import auditevent
            return auditevent.AuditEventEntityDetail(jsondict)
        if "AuditEventSource" == resource_type:
            from . import auditevent
            return auditevent.AuditEventSource(jsondict)
        if "BackboneElement" == resource_type:
            from . import backboneelement
            return backboneelement.BackboneElement(jsondict)
        if "Basic" == resource_type:
            from . import basic
            return basic.Basic(jsondict)
        if "Binary" == resource_type:
            from . import binary
            return binary.Binary(jsondict)
        if "BiologicallyDerivedProduct" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProduct(jsondict)
        if "BiologicallyDerivedProductCollection" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductCollection(jsondict)
        if "BiologicallyDerivedProductManipulation" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductManipulation(jsondict)
        if "BiologicallyDerivedProductProcessing" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductProcessing(jsondict)
        if "BiologicallyDerivedProductStorage" == resource_type:
            from . import biologicallyderivedproduct
            return biologicallyderivedproduct.BiologicallyDerivedProductStorage(jsondict)
        if "BodyStructure" == resource_type:
            from . import bodystructure
            return bodystructure.BodyStructure(jsondict)
        if "Bundle" == resource_type:
            from . import bundle
            return bundle.Bundle(jsondict)
        if "BundleEntry" == resource_type:
            from . import bundle
            return bundle.BundleEntry(jsondict)
        if "BundleEntryRequest" == resource_type:
            from . import bundle
            return bundle.BundleEntryRequest(jsondict)
        if "BundleEntryResponse" == resource_type:
            from . import bundle
            return bundle.BundleEntryResponse(jsondict)
        if "BundleEntrySearch" == resource_type:
            from . import bundle
            return bundle.BundleEntrySearch(jsondict)
        if "BundleLink" == resource_type:
            from . import bundle
            return bundle.BundleLink(jsondict)
        if "CapabilityStatement" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatement(jsondict)
        if "CapabilityStatementDocument" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementDocument(jsondict)
        if "CapabilityStatementImplementation" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementImplementation(jsondict)
        if "CapabilityStatementMessaging" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessaging(jsondict)
        if "CapabilityStatementMessagingEndpoint" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessagingEndpoint(jsondict)
        if "CapabilityStatementMessagingSupportedMessage" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessagingSupportedMessage(jsondict)
        if "CapabilityStatementRest" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRest(jsondict)
        if "CapabilityStatementRestInteraction" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestInteraction(jsondict)
        if "CapabilityStatementRestResource" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResource(jsondict)
        if "CapabilityStatementRestResourceInteraction" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceInteraction(jsondict)
        if "CapabilityStatementRestResourceOperation" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceOperation(jsondict)
        if "CapabilityStatementRestResourceSearchParam" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceSearchParam(jsondict)
        if "CapabilityStatementRestSecurity" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestSecurity(jsondict)
        if "CapabilityStatementSoftware" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementSoftware(jsondict)
        if "CarePlan" == resource_type:
            from . import careplan
            return careplan.CarePlan(jsondict)
        if "CarePlanActivity" == resource_type:
            from . import careplan
            return careplan.CarePlanActivity(jsondict)
        if "CarePlanActivityDetail" == resource_type:
            from . import careplan
            return careplan.CarePlanActivityDetail(jsondict)
        if "CareTeam" == resource_type:
            from . import careteam
            return careteam.CareTeam(jsondict)
        if "CareTeamParticipant" == resource_type:
            from . import careteam
            return careteam.CareTeamParticipant(jsondict)
        if "CatalogEntry" == resource_type:
            from . import catalogentry
            return catalogentry.CatalogEntry(jsondict)
        if "CatalogEntryRelatedEntry" == resource_type:
            from . import catalogentry
            return catalogentry.CatalogEntryRelatedEntry(jsondict)
        if "ChargeItem" == resource_type:
            from . import chargeitem
            return chargeitem.ChargeItem(jsondict)
        if "ChargeItemDefinition" == resource_type:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinition(jsondict)
        if "ChargeItemDefinitionApplicability" == resource_type:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinitionApplicability(jsondict)
        if "ChargeItemDefinitionPropertyGroup" == resource_type:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinitionPropertyGroup(jsondict)
        if "ChargeItemDefinitionPropertyGroupPriceComponent" == resource_type:
            from . import chargeitemdefinition
            return chargeitemdefinition.ChargeItemDefinitionPropertyGroupPriceComponent(jsondict)
        if "ChargeItemPerformer" == resource_type:
            from . import chargeitem
            return chargeitem.ChargeItemPerformer(jsondict)
        if "Claim" == resource_type:
            from . import claim
            return claim.Claim(jsondict)
        if "ClaimAccident" == resource_type:
            from . import claim
            return claim.ClaimAccident(jsondict)
        if "ClaimCareTeam" == resource_type:
            from . import claim
            return claim.ClaimCareTeam(jsondict)
        if "ClaimDiagnosis" == resource_type:
            from . import claim
            return claim.ClaimDiagnosis(jsondict)
        if "ClaimInsurance" == resource_type:
            from . import claim
            return claim.ClaimInsurance(jsondict)
        if "ClaimItem" == resource_type:
            from . import claim
            return claim.ClaimItem(jsondict)
        if "ClaimItemDetail" == resource_type:
            from . import claim
            return claim.ClaimItemDetail(jsondict)
        if "ClaimItemDetailSubDetail" == resource_type:
            from . import claim
            return claim.ClaimItemDetailSubDetail(jsondict)
        if "ClaimPayee" == resource_type:
            from . import claim
            return claim.ClaimPayee(jsondict)
        if "ClaimProcedure" == resource_type:
            from . import claim
            return claim.ClaimProcedure(jsondict)
        if "ClaimRelated" == resource_type:
            from . import claim
            return claim.ClaimRelated(jsondict)
        if "ClaimResponse" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponse(jsondict)
        if "ClaimResponseAddItem" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItem(jsondict)
        if "ClaimResponseAddItemDetail" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetail(jsondict)
        if "ClaimResponseAddItemDetailSubDetail" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseAddItemDetailSubDetail(jsondict)
        if "ClaimResponseError" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseError(jsondict)
        if "ClaimResponseInsurance" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseInsurance(jsondict)
        if "ClaimResponseItem" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseItem(jsondict)
        if "ClaimResponseItemAdjudication" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseItemAdjudication(jsondict)
        if "ClaimResponseItemDetail" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetail(jsondict)
        if "ClaimResponseItemDetailSubDetail" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseItemDetailSubDetail(jsondict)
        if "ClaimResponsePayment" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponsePayment(jsondict)
        if "ClaimResponseProcessNote" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseProcessNote(jsondict)
        if "ClaimResponseTotal" == resource_type:
            from . import claimresponse
            return claimresponse.ClaimResponseTotal(jsondict)
        if "ClaimSupportingInfo" == resource_type:
            from . import claim
            return claim.ClaimSupportingInfo(jsondict)
        if "ClinicalImpression" == resource_type:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpression(jsondict)
        if "ClinicalImpressionFinding" == resource_type:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionFinding(jsondict)
        if "ClinicalImpressionInvestigation" == resource_type:
            from . import clinicalimpression
            return clinicalimpression.ClinicalImpressionInvestigation(jsondict)
        if "CodeSystem" == resource_type:
            from . import codesystem
            return codesystem.CodeSystem(jsondict)
        if "CodeSystemConcept" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemConcept(jsondict)
        if "CodeSystemConceptDesignation" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemConceptDesignation(jsondict)
        if "CodeSystemConceptProperty" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemConceptProperty(jsondict)
        if "CodeSystemFilter" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemFilter(jsondict)
        if "CodeSystemProperty" == resource_type:
            from . import codesystem
            return codesystem.CodeSystemProperty(jsondict)
        if "CodeableConcept" == resource_type:
            from . import codeableconcept
            return codeableconcept.CodeableConcept(jsondict)
        if "Coding" == resource_type:
            from . import coding
            return coding.Coding(jsondict)
        if "Communication" == resource_type:
            from . import communication
            return communication.Communication(jsondict)
        if "CommunicationPayload" == resource_type:
            from . import communication
            return communication.CommunicationPayload(jsondict)
        if "CommunicationRequest" == resource_type:
            from . import communicationrequest
            return communicationrequest.CommunicationRequest(jsondict)
        if "CommunicationRequestPayload" == resource_type:
            from . import communicationrequest
            return communicationrequest.CommunicationRequestPayload(jsondict)
        if "CompartmentDefinition" == resource_type:
            from . import compartmentdefinition
            return compartmentdefinition.CompartmentDefinition(jsondict)
        if "CompartmentDefinitionResource" == resource_type:
            from . import compartmentdefinition
            return compartmentdefinition.CompartmentDefinitionResource(jsondict)
        if "Composition" == resource_type:
            from . import composition
            return composition.Composition(jsondict)
        if "CompositionAttester" == resource_type:
            from . import composition
            return composition.CompositionAttester(jsondict)
        if "CompositionEvent" == resource_type:
            from . import composition
            return composition.CompositionEvent(jsondict)
        if "CompositionRelatesTo" == resource_type:
            from . import composition
            return composition.CompositionRelatesTo(jsondict)
        if "CompositionSection" == resource_type:
            from . import composition
            return composition.CompositionSection(jsondict)
        if "ConceptMap" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMap(jsondict)
        if "ConceptMapGroup" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroup(jsondict)
        if "ConceptMapGroupElement" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroupElement(jsondict)
        if "ConceptMapGroupElementTarget" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroupElementTarget(jsondict)
        if "ConceptMapGroupElementTargetDependsOn" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroupElementTargetDependsOn(jsondict)
        if "ConceptMapGroupUnmapped" == resource_type:
            from . import conceptmap
            return conceptmap.ConceptMapGroupUnmapped(jsondict)
        if "Condition" == resource_type:
            from . import condition
            return condition.Condition(jsondict)
        if "ConditionEvidence" == resource_type:
            from . import condition
            return condition.ConditionEvidence(jsondict)
        if "ConditionStage" == resource_type:
            from . import condition
            return condition.ConditionStage(jsondict)
        if "Consent" == resource_type:
            from . import consent
            return consent.Consent(jsondict)
        if "ConsentPolicy" == resource_type:
            from . import consent
            return consent.ConsentPolicy(jsondict)
        if "ConsentProvision" == resource_type:
            from . import consent
            return consent.ConsentProvision(jsondict)
        if "ConsentProvisionActor" == resource_type:
            from . import consent
            return consent.ConsentProvisionActor(jsondict)
        if "ConsentProvisionData" == resource_type:
            from . import consent
            return consent.ConsentProvisionData(jsondict)
        if "ConsentVerification" == resource_type:
            from . import consent
            return consent.ConsentVerification(jsondict)
        if "ContactDetail" == resource_type:
            from . import contactdetail
            return contactdetail.ContactDetail(jsondict)
        if "ContactPoint" == resource_type:
            from . import contactpoint
            return contactpoint.ContactPoint(jsondict)
        if "Contract" == resource_type:
            from . import contract
            return contract.Contract(jsondict)
        if "ContractContentDefinition" == resource_type:
            from . import contract
            return contract.ContractContentDefinition(jsondict)
        if "ContractFriendly" == resource_type:
            from . import contract
            return contract.ContractFriendly(jsondict)
        if "ContractLegal" == resource_type:
            from . import contract
            return contract.ContractLegal(jsondict)
        if "ContractRule" == resource_type:
            from . import contract
            return contract.ContractRule(jsondict)
        if "ContractSigner" == resource_type:
            from . import contract
            return contract.ContractSigner(jsondict)
        if "ContractTerm" == resource_type:
            from . import contract
            return contract.ContractTerm(jsondict)
        if "ContractTermAction" == resource_type:
            from . import contract
            return contract.ContractTermAction(jsondict)
        if "ContractTermActionSubject" == resource_type:
            from . import contract
            return contract.ContractTermActionSubject(jsondict)
        if "ContractTermAsset" == resource_type:
            from . import contract
            return contract.ContractTermAsset(jsondict)
        if "ContractTermAssetContext" == resource_type:
            from . import contract
            return contract.ContractTermAssetContext(jsondict)
        if "ContractTermAssetValuedItem" == resource_type:
            from . import contract
            return contract.ContractTermAssetValuedItem(jsondict)
        if "ContractTermOffer" == resource_type:
            from . import contract
            return contract.ContractTermOffer(jsondict)
        if "ContractTermOfferAnswer" == resource_type:
            from . import contract
            return contract.ContractTermOfferAnswer(jsondict)
        if "ContractTermOfferParty" == resource_type:
            from . import contract
            return contract.ContractTermOfferParty(jsondict)
        if "ContractTermSecurityLabel" == resource_type:
            from . import contract
            return contract.ContractTermSecurityLabel(jsondict)
        if "Contributor" == resource_type:
            from . import contributor
            return contributor.Contributor(jsondict)
        if "Count" == resource_type:
            from . import count
            return count.Count(jsondict)
        if "Coverage" == resource_type:
            from . import coverage
            return coverage.Coverage(jsondict)
        if "CoverageClass" == resource_type:
            from . import coverage
            return coverage.CoverageClass(jsondict)
        if "CoverageCostToBeneficiary" == resource_type:
            from . import coverage
            return coverage.CoverageCostToBeneficiary(jsondict)
        if "CoverageCostToBeneficiaryException" == resource_type:
            from . import coverage
            return coverage.CoverageCostToBeneficiaryException(jsondict)
        if "CoverageEligibilityRequest" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequest(jsondict)
        if "CoverageEligibilityRequestInsurance" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestInsurance(jsondict)
        if "CoverageEligibilityRequestItem" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestItem(jsondict)
        if "CoverageEligibilityRequestItemDiagnosis" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestItemDiagnosis(jsondict)
        if "CoverageEligibilityRequestSupportingInfo" == resource_type:
            from . import coverageeligibilityrequest
            return coverageeligibilityrequest.CoverageEligibilityRequestSupportingInfo(jsondict)
        if "CoverageEligibilityResponse" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponse(jsondict)
        if "CoverageEligibilityResponseError" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseError(jsondict)
        if "CoverageEligibilityResponseInsurance" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseInsurance(jsondict)
        if "CoverageEligibilityResponseInsuranceItem" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItem(jsondict)
        if "CoverageEligibilityResponseInsuranceItemBenefit" == resource_type:
            from . import coverageeligibilityresponse
            return coverageeligibilityresponse.CoverageEligibilityResponseInsuranceItemBenefit(jsondict)
        if "DataRequirement" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirement(jsondict)
        if "DataRequirementCodeFilter" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirementCodeFilter(jsondict)
        if "DataRequirementDateFilter" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirementDateFilter(jsondict)
        if "DataRequirementSort" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirementSort(jsondict)
        if "DetectedIssue" == resource_type:
            from . import detectedissue
            return detectedissue.DetectedIssue(jsondict)
        if "DetectedIssueEvidence" == resource_type:
            from . import detectedissue
            return detectedissue.DetectedIssueEvidence(jsondict)
        if "DetectedIssueMitigation" == resource_type:
            from . import detectedissue
            return detectedissue.DetectedIssueMitigation(jsondict)
        if "Device" == resource_type:
            from . import device
            return device.Device(jsondict)
        if "DeviceDefinition" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinition(jsondict)
        if "DeviceDefinitionCapability" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionCapability(jsondict)
        if "DeviceDefinitionDeviceName" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionDeviceName(jsondict)
        if "DeviceDefinitionMaterial" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionMaterial(jsondict)
        if "DeviceDefinitionProperty" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionProperty(jsondict)
        if "DeviceDefinitionSpecialization" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionSpecialization(jsondict)
        if "DeviceDefinitionUdiDeviceIdentifier" == resource_type:
            from . import devicedefinition
            return devicedefinition.DeviceDefinitionUdiDeviceIdentifier(jsondict)
        if "DeviceDeviceName" == resource_type:
            from . import device
            return device.DeviceDeviceName(jsondict)
        if "DeviceMetric" == resource_type:
            from . import devicemetric
            return devicemetric.DeviceMetric(jsondict)
        if "DeviceMetricCalibration" == resource_type:
            from . import devicemetric
            return devicemetric.DeviceMetricCalibration(jsondict)
        if "DeviceProperty" == resource_type:
            from . import device
            return device.DeviceProperty(jsondict)
        if "DeviceRequest" == resource_type:
            from . import devicerequest
            return devicerequest.DeviceRequest(jsondict)
        if "DeviceRequestParameter" == resource_type:
            from . import devicerequest
            return devicerequest.DeviceRequestParameter(jsondict)
        if "DeviceSpecialization" == resource_type:
            from . import device
            return device.DeviceSpecialization(jsondict)
        if "DeviceUdiCarrier" == resource_type:
            from . import device
            return device.DeviceUdiCarrier(jsondict)
        if "DeviceUseStatement" == resource_type:
            from . import deviceusestatement
            return deviceusestatement.DeviceUseStatement(jsondict)
        if "DeviceVersion" == resource_type:
            from . import device
            return device.DeviceVersion(jsondict)
        if "DiagnosticReport" == resource_type:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReport(jsondict)
        if "DiagnosticReportMedia" == resource_type:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReportMedia(jsondict)
        if "Distance" == resource_type:
            from . import distance
            return distance.Distance(jsondict)
        if "DocumentManifest" == resource_type:
            from . import documentmanifest
            return documentmanifest.DocumentManifest(jsondict)
        if "DocumentManifestRelated" == resource_type:
            from . import documentmanifest
            return documentmanifest.DocumentManifestRelated(jsondict)
        if "DocumentReference" == resource_type:
            from . import documentreference
            return documentreference.DocumentReference(jsondict)
        if "DocumentReferenceContent" == resource_type:
            from . import documentreference
            return documentreference.DocumentReferenceContent(jsondict)
        if "DocumentReferenceContext" == resource_type:
            from . import documentreference
            return documentreference.DocumentReferenceContext(jsondict)
        if "DocumentReferenceRelatesTo" == resource_type:
            from . import documentreference
            return documentreference.DocumentReferenceRelatesTo(jsondict)
        if "DomainResource" == resource_type:
            from . import domainresource
            return domainresource.DomainResource(jsondict)
        if "Dosage" == resource_type:
            from . import dosage
            return dosage.Dosage(jsondict)
        if "DosageDoseAndRate" == resource_type:
            from . import dosage
            return dosage.DosageDoseAndRate(jsondict)
        if "Duration" == resource_type:
            from . import duration
            return duration.Duration(jsondict)
        if "EffectEvidenceSynthesis" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesis(jsondict)
        if "EffectEvidenceSynthesisCertainty" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisCertainty(jsondict)
        if "EffectEvidenceSynthesisCertaintyCertaintySubcomponent" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisCertaintyCertaintySubcomponent(jsondict)
        if "EffectEvidenceSynthesisEffectEstimate" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisEffectEstimate(jsondict)
        if "EffectEvidenceSynthesisEffectEstimatePrecisionEstimate" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisEffectEstimatePrecisionEstimate(jsondict)
        if "EffectEvidenceSynthesisResultsByExposure" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisResultsByExposure(jsondict)
        if "EffectEvidenceSynthesisSampleSize" == resource_type:
            from . import effectevidencesynthesis
            return effectevidencesynthesis.EffectEvidenceSynthesisSampleSize(jsondict)
        if "Element" == resource_type:
            from . import element
            return element.Element(jsondict)
        if "ElementDefinition" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinition(jsondict)
        if "ElementDefinitionBase" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBase(jsondict)
        if "ElementDefinitionBinding" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionBinding(jsondict)
        if "ElementDefinitionConstraint" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionConstraint(jsondict)
        if "ElementDefinitionExample" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionExample(jsondict)
        if "ElementDefinitionMapping" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionMapping(jsondict)
        if "ElementDefinitionSlicing" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionSlicing(jsondict)
        if "ElementDefinitionSlicingDiscriminator" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionSlicingDiscriminator(jsondict)
        if "ElementDefinitionType" == resource_type:
            from . import elementdefinition
            return elementdefinition.ElementDefinitionType(jsondict)
        if "Encounter" == resource_type:
            from . import encounter
            return encounter.Encounter(jsondict)
        if "EncounterClassHistory" == resource_type:
            from . import encounter
            return encounter.EncounterClassHistory(jsondict)
        if "EncounterDiagnosis" == resource_type:
            from . import encounter
            return encounter.EncounterDiagnosis(jsondict)
        if "EncounterHospitalization" == resource_type:
            from . import encounter
            return encounter.EncounterHospitalization(jsondict)
        if "EncounterLocation" == resource_type:
            from . import encounter
            return encounter.EncounterLocation(jsondict)
        if "EncounterParticipant" == resource_type:
            from . import encounter
            return encounter.EncounterParticipant(jsondict)
        if "EncounterStatusHistory" == resource_type:
            from . import encounter
            return encounter.EncounterStatusHistory(jsondict)
        if "Endpoint" == resource_type:
            from . import endpoint
            return endpoint.Endpoint(jsondict)
        if "EnrollmentRequest" == resource_type:
            from . import enrollmentrequest
            return enrollmentrequest.EnrollmentRequest(jsondict)
        if "EnrollmentResponse" == resource_type:
            from . import enrollmentresponse
            return enrollmentresponse.EnrollmentResponse(jsondict)
        if "EpisodeOfCare" == resource_type:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCare(jsondict)
        if "EpisodeOfCareDiagnosis" == resource_type:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareDiagnosis(jsondict)
        if "EpisodeOfCareStatusHistory" == resource_type:
            from . import episodeofcare
            return episodeofcare.EpisodeOfCareStatusHistory(jsondict)
        if "EventDefinition" == resource_type:
            from . import eventdefinition
            return eventdefinition.EventDefinition(jsondict)
        if "Evidence" == resource_type:
            from . import evidence
            return evidence.Evidence(jsondict)
        if "EvidenceVariable" == resource_type:
            from . import evidencevariable
            return evidencevariable.EvidenceVariable(jsondict)
        if "EvidenceVariableCharacteristic" == resource_type:
            from . import evidencevariable
            return evidencevariable.EvidenceVariableCharacteristic(jsondict)
        if "ExampleScenario" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenario(jsondict)
        if "ExampleScenarioActor" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioActor(jsondict)
        if "ExampleScenarioInstance" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioInstance(jsondict)
        if "ExampleScenarioInstanceContainedInstance" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioInstanceContainedInstance(jsondict)
        if "ExampleScenarioInstanceVersion" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioInstanceVersion(jsondict)
        if "ExampleScenarioProcess" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcess(jsondict)
        if "ExampleScenarioProcessStep" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcessStep(jsondict)
        if "ExampleScenarioProcessStepAlternative" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcessStepAlternative(jsondict)
        if "ExampleScenarioProcessStepOperation" == resource_type:
            from . import examplescenario
            return examplescenario.ExampleScenarioProcessStepOperation(jsondict)
        if "ExplanationOfBenefit" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefit(jsondict)
        if "ExplanationOfBenefitAccident" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAccident(jsondict)
        if "ExplanationOfBenefitAddItem" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItem(jsondict)
        if "ExplanationOfBenefitAddItemDetail" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItemDetail(jsondict)
        if "ExplanationOfBenefitAddItemDetailSubDetail" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitAddItemDetailSubDetail(jsondict)
        if "ExplanationOfBenefitBenefitBalance" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitBenefitBalance(jsondict)
        if "ExplanationOfBenefitBenefitBalanceFinancial" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitBenefitBalanceFinancial(jsondict)
        if "ExplanationOfBenefitCareTeam" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitCareTeam(jsondict)
        if "ExplanationOfBenefitDiagnosis" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitDiagnosis(jsondict)
        if "ExplanationOfBenefitInsurance" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitInsurance(jsondict)
        if "ExplanationOfBenefitItem" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItem(jsondict)
        if "ExplanationOfBenefitItemAdjudication" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemAdjudication(jsondict)
        if "ExplanationOfBenefitItemDetail" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetail(jsondict)
        if "ExplanationOfBenefitItemDetailSubDetail" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitItemDetailSubDetail(jsondict)
        if "ExplanationOfBenefitPayee" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitPayee(jsondict)
        if "ExplanationOfBenefitPayment" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitPayment(jsondict)
        if "ExplanationOfBenefitProcedure" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitProcedure(jsondict)
        if "ExplanationOfBenefitProcessNote" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitProcessNote(jsondict)
        if "ExplanationOfBenefitRelated" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitRelated(jsondict)
        if "ExplanationOfBenefitSupportingInfo" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitSupportingInfo(jsondict)
        if "ExplanationOfBenefitTotal" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitTotal(jsondict)
        if "Expression" == resource_type:
            from . import expression
            return expression.Expression(jsondict)
        if "Extension" == resource_type:
            from . import extension
            return extension.Extension(jsondict)
        if "FamilyMemberHistory" == resource_type:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistory(jsondict)
        if "FamilyMemberHistoryCondition" == resource_type:
            from . import familymemberhistory
            return familymemberhistory.FamilyMemberHistoryCondition(jsondict)
        if "Flag" == resource_type:
            from . import flag
            return flag.Flag(jsondict)
        if "Goal" == resource_type:
            from . import goal
            return goal.Goal(jsondict)
        if "GoalTarget" == resource_type:
            from . import goal
            return goal.GoalTarget(jsondict)
        if "GraphDefinition" == resource_type:
            from . import graphdefinition
            return graphdefinition.GraphDefinition(jsondict)
        if "GraphDefinitionLink" == resource_type:
            from . import graphdefinition
            return graphdefinition.GraphDefinitionLink(jsondict)
        if "GraphDefinitionLinkTarget" == resource_type:
            from . import graphdefinition
            return graphdefinition.GraphDefinitionLinkTarget(jsondict)
        if "GraphDefinitionLinkTargetCompartment" == resource_type:
            from . import graphdefinition
            return graphdefinition.GraphDefinitionLinkTargetCompartment(jsondict)
        if "Group" == resource_type:
            from . import group
            return group.Group(jsondict)
        if "GroupCharacteristic" == resource_type:
            from . import group
            return group.GroupCharacteristic(jsondict)
        if "GroupMember" == resource_type:
            from . import group
            return group.GroupMember(jsondict)
        if "GuidanceResponse" == resource_type:
            from . import guidanceresponse
            return guidanceresponse.GuidanceResponse(jsondict)
        if "HealthcareService" == resource_type:
            from . import healthcareservice
            return healthcareservice.HealthcareService(jsondict)
        if "HealthcareServiceAvailableTime" == resource_type:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceAvailableTime(jsondict)
        if "HealthcareServiceEligibility" == resource_type:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceEligibility(jsondict)
        if "HealthcareServiceNotAvailable" == resource_type:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceNotAvailable(jsondict)
        if "HumanName" == resource_type:
            from . import humanname
            return humanname.HumanName(jsondict)
        if "Identifier" == resource_type:
            from . import identifier
            return identifier.Identifier(jsondict)
        if "ImagingStudy" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudy(jsondict)
        if "ImagingStudySeries" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeries(jsondict)
        if "ImagingStudySeriesInstance" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeriesInstance(jsondict)
        if "ImagingStudySeriesPerformer" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeriesPerformer(jsondict)
        if "Immunization" == resource_type:
            from . import immunization
            return immunization.Immunization(jsondict)
        if "ImmunizationEducation" == resource_type:
            from . import immunization
            return immunization.ImmunizationEducation(jsondict)
        if "ImmunizationEvaluation" == resource_type:
            from . import immunizationevaluation
            return immunizationevaluation.ImmunizationEvaluation(jsondict)
        if "ImmunizationPerformer" == resource_type:
            from . import immunization
            return immunization.ImmunizationPerformer(jsondict)
        if "ImmunizationProtocolApplied" == resource_type:
            from . import immunization
            return immunization.ImmunizationProtocolApplied(jsondict)
        if "ImmunizationReaction" == resource_type:
            from . import immunization
            return immunization.ImmunizationReaction(jsondict)
        if "ImmunizationRecommendation" == resource_type:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendation(jsondict)
        if "ImmunizationRecommendationRecommendation" == resource_type:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendation(jsondict)
        if "ImmunizationRecommendationRecommendationDateCriterion" == resource_type:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion(jsondict)
        if "ImplementationGuide" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuide(jsondict)
        if "ImplementationGuideDefinition" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinition(jsondict)
        if "ImplementationGuideDefinitionGrouping" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionGrouping(jsondict)
        if "ImplementationGuideDefinitionPage" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionPage(jsondict)
        if "ImplementationGuideDefinitionParameter" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionParameter(jsondict)
        if "ImplementationGuideDefinitionResource" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionResource(jsondict)
        if "ImplementationGuideDefinitionTemplate" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDefinitionTemplate(jsondict)
        if "ImplementationGuideDependsOn" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDependsOn(jsondict)
        if "ImplementationGuideGlobal" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideGlobal(jsondict)
        if "ImplementationGuideManifest" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideManifest(jsondict)
        if "ImplementationGuideManifestPage" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideManifestPage(jsondict)
        if "ImplementationGuideManifestResource" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideManifestResource(jsondict)
        if "InsurancePlan" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlan(jsondict)
        if "InsurancePlanContact" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanContact(jsondict)
        if "InsurancePlanCoverage" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanCoverage(jsondict)
        if "InsurancePlanCoverageBenefit" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanCoverageBenefit(jsondict)
        if "InsurancePlanCoverageBenefitLimit" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanCoverageBenefitLimit(jsondict)
        if "InsurancePlanPlan" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlan(jsondict)
        if "InsurancePlanPlanGeneralCost" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanGeneralCost(jsondict)
        if "InsurancePlanPlanSpecificCost" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanSpecificCost(jsondict)
        if "InsurancePlanPlanSpecificCostBenefit" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanSpecificCostBenefit(jsondict)
        if "InsurancePlanPlanSpecificCostBenefitCost" == resource_type:
            from . import insuranceplan
            return insuranceplan.InsurancePlanPlanSpecificCostBenefitCost(jsondict)
        if "Invoice" == resource_type:
            from . import invoice
            return invoice.Invoice(jsondict)
        if "InvoiceLineItem" == resource_type:
            from . import invoice
            return invoice.InvoiceLineItem(jsondict)
        if "InvoiceLineItemPriceComponent" == resource_type:
            from . import invoice
            return invoice.InvoiceLineItemPriceComponent(jsondict)
        if "InvoiceParticipant" == resource_type:
            from . import invoice
            return invoice.InvoiceParticipant(jsondict)
        if "Library" == resource_type:
            from . import library
            return library.Library(jsondict)
        if "Linkage" == resource_type:
            from . import linkage
            return linkage.Linkage(jsondict)
        if "LinkageItem" == resource_type:
            from . import linkage
            return linkage.LinkageItem(jsondict)
        if "List" == resource_type:
            from . import list
            return list.List(jsondict)
        if "ListEntry" == resource_type:
            from . import list
            return list.ListEntry(jsondict)
        if "Location" == resource_type:
            from . import location
            return location.Location(jsondict)
        if "LocationHoursOfOperation" == resource_type:
            from . import location
            return location.LocationHoursOfOperation(jsondict)
        if "LocationPosition" == resource_type:
            from . import location
            return location.LocationPosition(jsondict)
        if "MarketingStatus" == resource_type:
            from . import marketingstatus
            return marketingstatus.MarketingStatus(jsondict)
        if "Measure" == resource_type:
            from . import measure
            return measure.Measure(jsondict)
        if "MeasureGroup" == resource_type:
            from . import measure
            return measure.MeasureGroup(jsondict)
        if "MeasureGroupPopulation" == resource_type:
            from . import measure
            return measure.MeasureGroupPopulation(jsondict)
        if "MeasureGroupStratifier" == resource_type:
            from . import measure
            return measure.MeasureGroupStratifier(jsondict)
        if "MeasureGroupStratifierComponent" == resource_type:
            from . import measure
            return measure.MeasureGroupStratifierComponent(jsondict)
        if "MeasureReport" == resource_type:
            from . import measurereport
            return measurereport.MeasureReport(jsondict)
        if "MeasureReportGroup" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroup(jsondict)
        if "MeasureReportGroupPopulation" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupPopulation(jsondict)
        if "MeasureReportGroupStratifier" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifier(jsondict)
        if "MeasureReportGroupStratifierStratum" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifierStratum(jsondict)
        if "MeasureReportGroupStratifierStratumComponent" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifierStratumComponent(jsondict)
        if "MeasureReportGroupStratifierStratumPopulation" == resource_type:
            from . import measurereport
            return measurereport.MeasureReportGroupStratifierStratumPopulation(jsondict)
        if "MeasureSupplementalData" == resource_type:
            from . import measure
            return measure.MeasureSupplementalData(jsondict)
        if "Media" == resource_type:
            from . import media
            return media.Media(jsondict)
        if "Medication" == resource_type:
            from . import medication
            return medication.Medication(jsondict)
        if "MedicationAdministration" == resource_type:
            from . import medicationadministration
            return medicationadministration.MedicationAdministration(jsondict)
        if "MedicationAdministrationDosage" == resource_type:
            from . import medicationadministration
            return medicationadministration.MedicationAdministrationDosage(jsondict)
        if "MedicationAdministrationPerformer" == resource_type:
            from . import medicationadministration
            return medicationadministration.MedicationAdministrationPerformer(jsondict)
        if "MedicationBatch" == resource_type:
            from . import medication
            return medication.MedicationBatch(jsondict)
        if "MedicationDispense" == resource_type:
            from . import medicationdispense
            return medicationdispense.MedicationDispense(jsondict)
        if "MedicationDispensePerformer" == resource_type:
            from . import medicationdispense
            return medicationdispense.MedicationDispensePerformer(jsondict)
        if "MedicationDispenseSubstitution" == resource_type:
            from . import medicationdispense
            return medicationdispense.MedicationDispenseSubstitution(jsondict)
        if "MedicationIngredient" == resource_type:
            from . import medication
            return medication.MedicationIngredient(jsondict)
        if "MedicationKnowledge" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledge(jsondict)
        if "MedicationKnowledgeAdministrationGuidelines" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeAdministrationGuidelines(jsondict)
        if "MedicationKnowledgeAdministrationGuidelinesDosage" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeAdministrationGuidelinesDosage(jsondict)
        if "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(jsondict)
        if "MedicationKnowledgeCost" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeCost(jsondict)
        if "MedicationKnowledgeDrugCharacteristic" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeDrugCharacteristic(jsondict)
        if "MedicationKnowledgeIngredient" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeIngredient(jsondict)
        if "MedicationKnowledgeKinetics" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeKinetics(jsondict)
        if "MedicationKnowledgeMedicineClassification" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeMedicineClassification(jsondict)
        if "MedicationKnowledgeMonitoringProgram" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeMonitoringProgram(jsondict)
        if "MedicationKnowledgeMonograph" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeMonograph(jsondict)
        if "MedicationKnowledgePackaging" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgePackaging(jsondict)
        if "MedicationKnowledgeRegulatory" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatory(jsondict)
        if "MedicationKnowledgeRegulatoryMaxDispense" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatoryMaxDispense(jsondict)
        if "MedicationKnowledgeRegulatorySchedule" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatorySchedule(jsondict)
        if "MedicationKnowledgeRegulatorySubstitution" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRegulatorySubstitution(jsondict)
        if "MedicationKnowledgeRelatedMedicationKnowledge" == resource_type:
            from . import medicationknowledge
            return medicationknowledge.MedicationKnowledgeRelatedMedicationKnowledge(jsondict)
        if "MedicationRequest" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequest(jsondict)
        if "MedicationRequestDispenseRequest" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequestDispenseRequest(jsondict)
        if "MedicationRequestDispenseRequestInitialFill" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequestDispenseRequestInitialFill(jsondict)
        if "MedicationRequestSubstitution" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequestSubstitution(jsondict)
        if "MedicationStatement" == resource_type:
            from . import medicationstatement
            return medicationstatement.MedicationStatement(jsondict)
        if "MedicinalProduct" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProduct(jsondict)
        if "MedicinalProductAuthorization" == resource_type:
            from . import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorization(jsondict)
        if "MedicinalProductAuthorizationJurisdictionalAuthorization" == resource_type:
            from . import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorizationJurisdictionalAuthorization(jsondict)
        if "MedicinalProductAuthorizationProcedure" == resource_type:
            from . import medicinalproductauthorization
            return medicinalproductauthorization.MedicinalProductAuthorizationProcedure(jsondict)
        if "MedicinalProductContraindication" == resource_type:
            from . import medicinalproductcontraindication
            return medicinalproductcontraindication.MedicinalProductContraindication(jsondict)
        if "MedicinalProductContraindicationOtherTherapy" == resource_type:
            from . import medicinalproductcontraindication
            return medicinalproductcontraindication.MedicinalProductContraindicationOtherTherapy(jsondict)
        if "MedicinalProductIndication" == resource_type:
            from . import medicinalproductindication
            return medicinalproductindication.MedicinalProductIndication(jsondict)
        if "MedicinalProductIndicationOtherTherapy" == resource_type:
            from . import medicinalproductindication
            return medicinalproductindication.MedicinalProductIndicationOtherTherapy(jsondict)
        if "MedicinalProductIngredient" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredient(jsondict)
        if "MedicinalProductIngredientSpecifiedSubstance" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstance(jsondict)
        if "MedicinalProductIngredientSpecifiedSubstanceStrength" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstanceStrength(jsondict)
        if "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(jsondict)
        if "MedicinalProductIngredientSubstance" == resource_type:
            from . import medicinalproductingredient
            return medicinalproductingredient.MedicinalProductIngredientSubstance(jsondict)
        if "MedicinalProductInteraction" == resource_type:
            from . import medicinalproductinteraction
            return medicinalproductinteraction.MedicinalProductInteraction(jsondict)
        if "MedicinalProductInteractionInteractant" == resource_type:
            from . import medicinalproductinteraction
            return medicinalproductinteraction.MedicinalProductInteractionInteractant(jsondict)
        if "MedicinalProductManufactured" == resource_type:
            from . import medicinalproductmanufactured
            return medicinalproductmanufactured.MedicinalProductManufactured(jsondict)
        if "MedicinalProductManufacturingBusinessOperation" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductManufacturingBusinessOperation(jsondict)
        if "MedicinalProductName" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductName(jsondict)
        if "MedicinalProductNameCountryLanguage" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductNameCountryLanguage(jsondict)
        if "MedicinalProductNameNamePart" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductNameNamePart(jsondict)
        if "MedicinalProductPackaged" == resource_type:
            from . import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackaged(jsondict)
        if "MedicinalProductPackagedBatchIdentifier" == resource_type:
            from . import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackagedBatchIdentifier(jsondict)
        if "MedicinalProductPackagedPackageItem" == resource_type:
            from . import medicinalproductpackaged
            return medicinalproductpackaged.MedicinalProductPackagedPackageItem(jsondict)
        if "MedicinalProductPharmaceutical" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceutical(jsondict)
        if "MedicinalProductPharmaceuticalCharacteristics" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalCharacteristics(jsondict)
        if "MedicinalProductPharmaceuticalRouteOfAdministration" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministration(jsondict)
        if "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(jsondict)
        if "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod" == resource_type:
            from . import medicinalproductpharmaceutical
            return medicinalproductpharmaceutical.MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(jsondict)
        if "MedicinalProductSpecialDesignation" == resource_type:
            from . import medicinalproduct
            return medicinalproduct.MedicinalProductSpecialDesignation(jsondict)
        if "MedicinalProductUndesirableEffect" == resource_type:
            from . import medicinalproductundesirableeffect
            return medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(jsondict)
        if "MessageDefinition" == resource_type:
            from . import messagedefinition
            return messagedefinition.MessageDefinition(jsondict)
        if "MessageDefinitionAllowedResponse" == resource_type:
            from . import messagedefinition
            return messagedefinition.MessageDefinitionAllowedResponse(jsondict)
        if "MessageDefinitionFocus" == resource_type:
            from . import messagedefinition
            return messagedefinition.MessageDefinitionFocus(jsondict)
        if "MessageHeader" == resource_type:
            from . import messageheader
            return messageheader.MessageHeader(jsondict)
        if "MessageHeaderDestination" == resource_type:
            from . import messageheader
            return messageheader.MessageHeaderDestination(jsondict)
        if "MessageHeaderResponse" == resource_type:
            from . import messageheader
            return messageheader.MessageHeaderResponse(jsondict)
        if "MessageHeaderSource" == resource_type:
            from . import messageheader
            return messageheader.MessageHeaderSource(jsondict)
        if "Meta" == resource_type:
            from . import meta
            return meta.Meta(jsondict)
        if "MetadataResource" == resource_type:
            from . import metadataresource
            return metadataresource.MetadataResource(jsondict)
        if "MolecularSequence" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequence(jsondict)
        if "MolecularSequenceQuality" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceQuality(jsondict)
        if "MolecularSequenceQualityRoc" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceQualityRoc(jsondict)
        if "MolecularSequenceReferenceSeq" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceReferenceSeq(jsondict)
        if "MolecularSequenceRepository" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceRepository(jsondict)
        if "MolecularSequenceStructureVariant" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceStructureVariant(jsondict)
        if "MolecularSequenceStructureVariantInner" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceStructureVariantInner(jsondict)
        if "MolecularSequenceStructureVariantOuter" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceStructureVariantOuter(jsondict)
        if "MolecularSequenceVariant" == resource_type:
            from . import molecularsequence
            return molecularsequence.MolecularSequenceVariant(jsondict)
        if "Money" == resource_type:
            from . import money
            return money.Money(jsondict)
        if "NamingSystem" == resource_type:
            from . import namingsystem
            return namingsystem.NamingSystem(jsondict)
        if "NamingSystemUniqueId" == resource_type:
            from . import namingsystem
            return namingsystem.NamingSystemUniqueId(jsondict)
        if "Narrative" == resource_type:
            from . import narrative
            return narrative.Narrative(jsondict)
        if "NutritionOrder" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrder(jsondict)
        if "NutritionOrderEnteralFormula" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormula(jsondict)
        if "NutritionOrderEnteralFormulaAdministration" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormulaAdministration(jsondict)
        if "NutritionOrderOralDiet" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDiet(jsondict)
        if "NutritionOrderOralDietNutrient" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietNutrient(jsondict)
        if "NutritionOrderOralDietTexture" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderOralDietTexture(jsondict)
        if "NutritionOrderSupplement" == resource_type:
            from . import nutritionorder
            return nutritionorder.NutritionOrderSupplement(jsondict)
        if "Observation" == resource_type:
            from . import observation
            return observation.Observation(jsondict)
        if "ObservationComponent" == resource_type:
            from . import observation
            return observation.ObservationComponent(jsondict)
        if "ObservationDefinition" == resource_type:
            from . import observationdefinition
            return observationdefinition.ObservationDefinition(jsondict)
        if "ObservationDefinitionQualifiedInterval" == resource_type:
            from . import observationdefinition
            return observationdefinition.ObservationDefinitionQualifiedInterval(jsondict)
        if "ObservationDefinitionQuantitativeDetails" == resource_type:
            from . import observationdefinition
            return observationdefinition.ObservationDefinitionQuantitativeDetails(jsondict)
        if "ObservationReferenceRange" == resource_type:
            from . import observation
            return observation.ObservationReferenceRange(jsondict)
        if "OperationDefinition" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinition(jsondict)
        if "OperationDefinitionOverload" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionOverload(jsondict)
        if "OperationDefinitionParameter" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameter(jsondict)
        if "OperationDefinitionParameterBinding" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameterBinding(jsondict)
        if "OperationDefinitionParameterReferencedFrom" == resource_type:
            from . import operationdefinition
            return operationdefinition.OperationDefinitionParameterReferencedFrom(jsondict)
        if "OperationOutcome" == resource_type:
            from . import operationoutcome
            return operationoutcome.OperationOutcome(jsondict)
        if "OperationOutcomeIssue" == resource_type:
            from . import operationoutcome
            return operationoutcome.OperationOutcomeIssue(jsondict)
        if "Organization" == resource_type:
            from . import organization
            return organization.Organization(jsondict)
        if "OrganizationAffiliation" == resource_type:
            from . import organizationaffiliation
            return organizationaffiliation.OrganizationAffiliation(jsondict)
        if "OrganizationContact" == resource_type:
            from . import organization
            return organization.OrganizationContact(jsondict)
        if "ParameterDefinition" == resource_type:
            from . import parameterdefinition
            return parameterdefinition.ParameterDefinition(jsondict)
        if "Parameters" == resource_type:
            from . import parameters
            return parameters.Parameters(jsondict)
        if "ParametersParameter" == resource_type:
            from . import parameters
            return parameters.ParametersParameter(jsondict)
        if "Patient" == resource_type:
            from . import patient
            return patient.Patient(jsondict)
        if "PatientCommunication" == resource_type:
            from . import patient
            return patient.PatientCommunication(jsondict)
        if "PatientContact" == resource_type:
            from . import patient
            return patient.PatientContact(jsondict)
        if "PatientLink" == resource_type:
            from . import patient
            return patient.PatientLink(jsondict)
        if "PaymentNotice" == resource_type:
            from . import paymentnotice
            return paymentnotice.PaymentNotice(jsondict)
        if "PaymentReconciliation" == resource_type:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliation(jsondict)
        if "PaymentReconciliationDetail" == resource_type:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationDetail(jsondict)
        if "PaymentReconciliationProcessNote" == resource_type:
            from . import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationProcessNote(jsondict)
        if "Period" == resource_type:
            from . import period
            return period.Period(jsondict)
        if "Person" == resource_type:
            from . import person
            return person.Person(jsondict)
        if "PersonLink" == resource_type:
            from . import person
            return person.PersonLink(jsondict)
        if "PlanDefinition" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinition(jsondict)
        if "PlanDefinitionAction" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionAction(jsondict)
        if "PlanDefinitionActionCondition" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionCondition(jsondict)
        if "PlanDefinitionActionDynamicValue" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionDynamicValue(jsondict)
        if "PlanDefinitionActionParticipant" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionParticipant(jsondict)
        if "PlanDefinitionActionRelatedAction" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionActionRelatedAction(jsondict)
        if "PlanDefinitionGoal" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionGoal(jsondict)
        if "PlanDefinitionGoalTarget" == resource_type:
            from . import plandefinition
            return plandefinition.PlanDefinitionGoalTarget(jsondict)
        if "Population" == resource_type:
            from . import population
            return population.Population(jsondict)
        if "Practitioner" == resource_type:
            from . import practitioner
            return practitioner.Practitioner(jsondict)
        if "PractitionerQualification" == resource_type:
            from . import practitioner
            return practitioner.PractitionerQualification(jsondict)
        if "PractitionerRole" == resource_type:
            from . import practitionerrole
            return practitionerrole.PractitionerRole(jsondict)
        if "PractitionerRoleAvailableTime" == resource_type:
            from . import practitionerrole
            return practitionerrole.PractitionerRoleAvailableTime(jsondict)
        if "PractitionerRoleNotAvailable" == resource_type:
            from . import practitionerrole
            return practitionerrole.PractitionerRoleNotAvailable(jsondict)
        if "Procedure" == resource_type:
            from . import procedure
            return procedure.Procedure(jsondict)
        if "ProcedureFocalDevice" == resource_type:
            from . import procedure
            return procedure.ProcedureFocalDevice(jsondict)
        if "ProcedurePerformer" == resource_type:
            from . import procedure
            return procedure.ProcedurePerformer(jsondict)
        if "ProdCharacteristic" == resource_type:
            from . import prodcharacteristic
            return prodcharacteristic.ProdCharacteristic(jsondict)
        if "ProductShelfLife" == resource_type:
            from . import productshelflife
            return productshelflife.ProductShelfLife(jsondict)
        if "Provenance" == resource_type:
            from . import provenance
            return provenance.Provenance(jsondict)
        if "ProvenanceAgent" == resource_type:
            from . import provenance
            return provenance.ProvenanceAgent(jsondict)
        if "ProvenanceEntity" == resource_type:
            from . import provenance
            return provenance.ProvenanceEntity(jsondict)
        if "Quantity" == resource_type:
            from . import quantity
            return quantity.Quantity(jsondict)
        if "Quantity" == resource_type:
            from . import quantity
            return quantity.Quantity(jsondict)
        if "Questionnaire" == resource_type:
            from . import questionnaire
            return questionnaire.Questionnaire(jsondict)
        if "QuestionnaireItem" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItem(jsondict)
        if "QuestionnaireItemAnswerOption" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItemAnswerOption(jsondict)
        if "QuestionnaireItemEnableWhen" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItemEnableWhen(jsondict)
        if "QuestionnaireItemInitial" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItemInitial(jsondict)
        if "QuestionnaireResponse" == resource_type:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponse(jsondict)
        if "QuestionnaireResponseItem" == resource_type:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseItem(jsondict)
        if "QuestionnaireResponseItemAnswer" == resource_type:
            from . import questionnaireresponse
            return questionnaireresponse.QuestionnaireResponseItemAnswer(jsondict)
        if "Range" == resource_type:
            from . import range
            return range.Range(jsondict)
        if "Ratio" == resource_type:
            from . import ratio
            return ratio.Ratio(jsondict)
        if "Reference" == resource_type:
            from . import reference
            return reference.Reference(jsondict)
        if "RelatedArtifact" == resource_type:
            from . import relatedartifact
            return relatedartifact.RelatedArtifact(jsondict)
        if "RelatedPerson" == resource_type:
            from . import relatedperson
            return relatedperson.RelatedPerson(jsondict)
        if "RelatedPersonCommunication" == resource_type:
            from . import relatedperson
            return relatedperson.RelatedPersonCommunication(jsondict)
        if "RequestGroup" == resource_type:
            from . import requestgroup
            return requestgroup.RequestGroup(jsondict)
        if "RequestGroupAction" == resource_type:
            from . import requestgroup
            return requestgroup.RequestGroupAction(jsondict)
        if "RequestGroupActionCondition" == resource_type:
            from . import requestgroup
            return requestgroup.RequestGroupActionCondition(jsondict)
        if "RequestGroupActionRelatedAction" == resource_type:
            from . import requestgroup
            return requestgroup.RequestGroupActionRelatedAction(jsondict)
        if "ResearchDefinition" == resource_type:
            from . import researchdefinition
            return researchdefinition.ResearchDefinition(jsondict)
        if "ResearchElementDefinition" == resource_type:
            from . import researchelementdefinition
            return researchelementdefinition.ResearchElementDefinition(jsondict)
        if "ResearchElementDefinitionCharacteristic" == resource_type:
            from . import researchelementdefinition
            return researchelementdefinition.ResearchElementDefinitionCharacteristic(jsondict)
        if "ResearchStudy" == resource_type:
            from . import researchstudy
            return researchstudy.ResearchStudy(jsondict)
        if "ResearchStudyArm" == resource_type:
            from . import researchstudy
            return researchstudy.ResearchStudyArm(jsondict)
        if "ResearchStudyObjective" == resource_type:
            from . import researchstudy
            return researchstudy.ResearchStudyObjective(jsondict)
        if "ResearchSubject" == resource_type:
            from . import researchsubject
            return researchsubject.ResearchSubject(jsondict)
        if "Resource" == resource_type:
            from . import resource
            return resource.Resource(jsondict)
        if "RiskAssessment" == resource_type:
            from . import riskassessment
            return riskassessment.RiskAssessment(jsondict)
        if "RiskAssessmentPrediction" == resource_type:
            from . import riskassessment
            return riskassessment.RiskAssessmentPrediction(jsondict)
        if "RiskEvidenceSynthesis" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesis(jsondict)
        if "RiskEvidenceSynthesisCertainty" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisCertainty(jsondict)
        if "RiskEvidenceSynthesisCertaintyCertaintySubcomponent" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisCertaintyCertaintySubcomponent(jsondict)
        if "RiskEvidenceSynthesisRiskEstimate" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisRiskEstimate(jsondict)
        if "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(jsondict)
        if "RiskEvidenceSynthesisSampleSize" == resource_type:
            from . import riskevidencesynthesis
            return riskevidencesynthesis.RiskEvidenceSynthesisSampleSize(jsondict)
        if "SampledData" == resource_type:
            from . import sampleddata
            return sampleddata.SampledData(jsondict)
        if "Schedule" == resource_type:
            from . import schedule
            return schedule.Schedule(jsondict)
        if "SearchParameter" == resource_type:
            from . import searchparameter
            return searchparameter.SearchParameter(jsondict)
        if "SearchParameterComponent" == resource_type:
            from . import searchparameter
            return searchparameter.SearchParameterComponent(jsondict)
        if "ServiceRequest" == resource_type:
            from . import servicerequest
            return servicerequest.ServiceRequest(jsondict)
        if "Signature" == resource_type:
            from . import signature
            return signature.Signature(jsondict)
        if "Slot" == resource_type:
            from . import slot
            return slot.Slot(jsondict)
        if "Specimen" == resource_type:
            from . import specimen
            return specimen.Specimen(jsondict)
        if "SpecimenCollection" == resource_type:
            from . import specimen
            return specimen.SpecimenCollection(jsondict)
        if "SpecimenContainer" == resource_type:
            from . import specimen
            return specimen.SpecimenContainer(jsondict)
        if "SpecimenDefinition" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinition(jsondict)
        if "SpecimenDefinitionTypeTested" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTested(jsondict)
        if "SpecimenDefinitionTypeTestedContainer" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTestedContainer(jsondict)
        if "SpecimenDefinitionTypeTestedContainerAdditive" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTestedContainerAdditive(jsondict)
        if "SpecimenDefinitionTypeTestedHandling" == resource_type:
            from . import specimendefinition
            return specimendefinition.SpecimenDefinitionTypeTestedHandling(jsondict)
        if "SpecimenProcessing" == resource_type:
            from . import specimen
            return specimen.SpecimenProcessing(jsondict)
        if "StructureDefinition" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinition(jsondict)
        if "StructureDefinitionContext" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionContext(jsondict)
        if "StructureDefinitionDifferential" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionDifferential(jsondict)
        if "StructureDefinitionMapping" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionMapping(jsondict)
        if "StructureDefinitionSnapshot" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinitionSnapshot(jsondict)
        if "StructureMap" == resource_type:
            from . import structuremap
            return structuremap.StructureMap(jsondict)
        if "StructureMapGroup" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroup(jsondict)
        if "StructureMapGroupInput" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupInput(jsondict)
        if "StructureMapGroupRule" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRule(jsondict)
        if "StructureMapGroupRuleDependent" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRuleDependent(jsondict)
        if "StructureMapGroupRuleSource" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRuleSource(jsondict)
        if "StructureMapGroupRuleTarget" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRuleTarget(jsondict)
        if "StructureMapGroupRuleTargetParameter" == resource_type:
            from . import structuremap
            return structuremap.StructureMapGroupRuleTargetParameter(jsondict)
        if "StructureMapStructure" == resource_type:
            from . import structuremap
            return structuremap.StructureMapStructure(jsondict)
        if "Subscription" == resource_type:
            from . import subscription
            return subscription.Subscription(jsondict)
        if "SubscriptionChannel" == resource_type:
            from . import subscription
            return subscription.SubscriptionChannel(jsondict)
        if "Substance" == resource_type:
            from . import substance
            return substance.Substance(jsondict)
        if "SubstanceAmount" == resource_type:
            from . import substanceamount
            return substanceamount.SubstanceAmount(jsondict)
        if "SubstanceAmountReferenceRange" == resource_type:
            from . import substanceamount
            return substanceamount.SubstanceAmountReferenceRange(jsondict)
        if "SubstanceIngredient" == resource_type:
            from . import substance
            return substance.SubstanceIngredient(jsondict)
        if "SubstanceInstance" == resource_type:
            from . import substance
            return substance.SubstanceInstance(jsondict)
        if "SubstanceNucleicAcid" == resource_type:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcid(jsondict)
        if "SubstanceNucleicAcidSubunit" == resource_type:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcidSubunit(jsondict)
        if "SubstanceNucleicAcidSubunitLinkage" == resource_type:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcidSubunitLinkage(jsondict)
        if "SubstanceNucleicAcidSubunitSugar" == resource_type:
            from . import substancenucleicacid
            return substancenucleicacid.SubstanceNucleicAcidSubunitSugar(jsondict)
        if "SubstancePolymer" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymer(jsondict)
        if "SubstancePolymerMonomerSet" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerMonomerSet(jsondict)
        if "SubstancePolymerMonomerSetStartingMaterial" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerMonomerSetStartingMaterial(jsondict)
        if "SubstancePolymerRepeat" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeat(jsondict)
        if "SubstancePolymerRepeatRepeatUnit" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeatRepeatUnit(jsondict)
        if "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(jsondict)
        if "SubstancePolymerRepeatRepeatUnitStructuralRepresentation" == resource_type:
            from . import substancepolymer
            return substancepolymer.SubstancePolymerRepeatRepeatUnitStructuralRepresentation(jsondict)
        if "SubstanceProtein" == resource_type:
            from . import substanceprotein
            return substanceprotein.SubstanceProtein(jsondict)
        if "SubstanceProteinSubunit" == resource_type:
            from . import substanceprotein
            return substanceprotein.SubstanceProteinSubunit(jsondict)
        if "SubstanceReferenceInformation" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformation(jsondict)
        if "SubstanceReferenceInformationClassification" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationClassification(jsondict)
        if "SubstanceReferenceInformationGene" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationGene(jsondict)
        if "SubstanceReferenceInformationGeneElement" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationGeneElement(jsondict)
        if "SubstanceReferenceInformationTarget" == resource_type:
            from . import substancereferenceinformation
            return substancereferenceinformation.SubstanceReferenceInformationTarget(jsondict)
        if "SubstanceSourceMaterial" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterial(jsondict)
        if "SubstanceSourceMaterialFractionDescription" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialFractionDescription(jsondict)
        if "SubstanceSourceMaterialOrganism" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganism(jsondict)
        if "SubstanceSourceMaterialOrganismAuthor" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganismAuthor(jsondict)
        if "SubstanceSourceMaterialOrganismHybrid" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganismHybrid(jsondict)
        if "SubstanceSourceMaterialOrganismOrganismGeneral" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialOrganismOrganismGeneral(jsondict)
        if "SubstanceSourceMaterialPartDescription" == resource_type:
            from . import substancesourcematerial
            return substancesourcematerial.SubstanceSourceMaterialPartDescription(jsondict)
        if "SubstanceSpecification" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecification(jsondict)
        if "SubstanceSpecificationMoiety" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationMoiety(jsondict)
        if "SubstanceSpecificationName" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationName(jsondict)
        if "SubstanceSpecificationNameOfficial" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationNameOfficial(jsondict)
        if "SubstanceSpecificationProperty" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationProperty(jsondict)
        if "SubstanceSpecificationRelationship" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationRelationship(jsondict)
        if "SubstanceSpecificationStructure" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationStructure(jsondict)
        if "SubstanceSpecificationStructureIsotope" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationStructureIsotope(jsondict)
        if "SubstanceSpecificationStructureIsotopeMolecularWeight" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationStructureIsotopeMolecularWeight(jsondict)
        if "SubstanceSpecificationStructureRepresentation" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationStructureRepresentation(jsondict)
        if "SubstanceSpecificationstr" == resource_type:
            from . import substancespecification
            return substancespecification.SubstanceSpecificationstr(jsondict)
        if "SupplyDelivery" == resource_type:
            from . import supplydelivery
            return supplydelivery.SupplyDelivery(jsondict)
        if "SupplyDeliverySuppliedItem" == resource_type:
            from . import supplydelivery
            return supplydelivery.SupplyDeliverySuppliedItem(jsondict)
        if "SupplyRequest" == resource_type:
            from . import supplyrequest
            return supplyrequest.SupplyRequest(jsondict)
        if "SupplyRequestParameter" == resource_type:
            from . import supplyrequest
            return supplyrequest.SupplyRequestParameter(jsondict)
        if "Task" == resource_type:
            from . import task
            return task.Task(jsondict)
        if "TaskInput" == resource_type:
            from . import task
            return task.TaskInput(jsondict)
        if "TaskOutput" == resource_type:
            from . import task
            return task.TaskOutput(jsondict)
        if "TaskRestriction" == resource_type:
            from . import task
            return task.TaskRestriction(jsondict)
        if "TerminologyCapabilities" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilities(jsondict)
        if "TerminologyCapabilitiesClosure" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesClosure(jsondict)
        if "TerminologyCapabilitiesCodeSystem" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesCodeSystem(jsondict)
        if "TerminologyCapabilitiesCodeSystemVersion" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesCodeSystemVersion(jsondict)
        if "TerminologyCapabilitiesCodeSystemVersionFilter" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesCodeSystemVersionFilter(jsondict)
        if "TerminologyCapabilitiesExpansion" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesExpansion(jsondict)
        if "TerminologyCapabilitiesExpansionParameter" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesExpansionParameter(jsondict)
        if "TerminologyCapabilitiesImplementation" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesImplementation(jsondict)
        if "TerminologyCapabilitiesSoftware" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesSoftware(jsondict)
        if "TerminologyCapabilitiesTranslation" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesTranslation(jsondict)
        if "TerminologyCapabilitiesValidateCode" == resource_type:
            from . import terminologycapabilities
            return terminologycapabilities.TerminologyCapabilitiesValidateCode(jsondict)
        if "TestReport" == resource_type:
            from . import testreport
            return testreport.TestReport(jsondict)
        if "TestReportParticipant" == resource_type:
            from . import testreport
            return testreport.TestReportParticipant(jsondict)
        if "TestReportSetup" == resource_type:
            from . import testreport
            return testreport.TestReportSetup(jsondict)
        if "TestReportSetupAction" == resource_type:
            from . import testreport
            return testreport.TestReportSetupAction(jsondict)
        if "TestReportSetupActionAssert" == resource_type:
            from . import testreport
            return testreport.TestReportSetupActionAssert(jsondict)
        if "TestReportSetupActionOperation" == resource_type:
            from . import testreport
            return testreport.TestReportSetupActionOperation(jsondict)
        if "TestReportTeardown" == resource_type:
            from . import testreport
            return testreport.TestReportTeardown(jsondict)
        if "TestReportTeardownAction" == resource_type:
            from . import testreport
            return testreport.TestReportTeardownAction(jsondict)
        if "TestReportTest" == resource_type:
            from . import testreport
            return testreport.TestReportTest(jsondict)
        if "TestReportTestAction" == resource_type:
            from . import testreport
            return testreport.TestReportTestAction(jsondict)
        if "TestScript" == resource_type:
            from . import testscript
            return testscript.TestScript(jsondict)
        if "TestScriptDestination" == resource_type:
            from . import testscript
            return testscript.TestScriptDestination(jsondict)
        if "TestScriptFixture" == resource_type:
            from . import testscript
            return testscript.TestScriptFixture(jsondict)
        if "TestScriptMetadata" == resource_type:
            from . import testscript
            return testscript.TestScriptMetadata(jsondict)
        if "TestScriptMetadataCapability" == resource_type:
            from . import testscript
            return testscript.TestScriptMetadataCapability(jsondict)
        if "TestScriptMetadataLink" == resource_type:
            from . import testscript
            return testscript.TestScriptMetadataLink(jsondict)
        if "TestScriptOrigin" == resource_type:
            from . import testscript
            return testscript.TestScriptOrigin(jsondict)
        if "TestScriptSetup" == resource_type:
            from . import testscript
            return testscript.TestScriptSetup(jsondict)
        if "TestScriptSetupAction" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupAction(jsondict)
        if "TestScriptSetupActionAssert" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionAssert(jsondict)
        if "TestScriptSetupActionOperation" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionOperation(jsondict)
        if "TestScriptSetupActionOperationRequestHeader" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionOperationRequestHeader(jsondict)
        if "TestScriptTeardown" == resource_type:
            from . import testscript
            return testscript.TestScriptTeardown(jsondict)
        if "TestScriptTeardownAction" == resource_type:
            from . import testscript
            return testscript.TestScriptTeardownAction(jsondict)
        if "TestScriptTest" == resource_type:
            from . import testscript
            return testscript.TestScriptTest(jsondict)
        if "TestScriptTestAction" == resource_type:
            from . import testscript
            return testscript.TestScriptTestAction(jsondict)
        if "TestScriptVariable" == resource_type:
            from . import testscript
            return testscript.TestScriptVariable(jsondict)
        if "Timing" == resource_type:
            from . import timing
            return timing.Timing(jsondict)
        if "TimingRepeat" == resource_type:
            from . import timing
            return timing.TimingRepeat(jsondict)
        if "TriggerDefinition" == resource_type:
            from . import triggerdefinition
            return triggerdefinition.TriggerDefinition(jsondict)
        if "UsageContext" == resource_type:
            from . import usagecontext
            return usagecontext.UsageContext(jsondict)
        if "ValueSet" == resource_type:
            from . import valueset
            return valueset.ValueSet(jsondict)
        if "ValueSetCompose" == resource_type:
            from . import valueset
            return valueset.ValueSetCompose(jsondict)
        if "ValueSetComposeInclude" == resource_type:
            from . import valueset
            return valueset.ValueSetComposeInclude(jsondict)
        if "ValueSetComposeIncludeConcept" == resource_type:
            from . import valueset
            return valueset.ValueSetComposeIncludeConcept(jsondict)
        if "ValueSetComposeIncludeConceptDesignation" == resource_type:
            from . import valueset
            return valueset.ValueSetComposeIncludeConceptDesignation(jsondict)
        if "ValueSetComposeIncludeFilter" == resource_type:
            from . import valueset
            return valueset.ValueSetComposeIncludeFilter(jsondict)
        if "ValueSetExpansion" == resource_type:
            from . import valueset
            return valueset.ValueSetExpansion(jsondict)
        if "ValueSetExpansionContains" == resource_type:
            from . import valueset
            return valueset.ValueSetExpansionContains(jsondict)
        if "ValueSetExpansionParameter" == resource_type:
            from . import valueset
            return valueset.ValueSetExpansionParameter(jsondict)
        if "VerificationResult" == resource_type:
            from . import verificationresult
            return verificationresult.VerificationResult(jsondict)
        if "VerificationResultAttestation" == resource_type:
            from . import verificationresult
            return verificationresult.VerificationResultAttestation(jsondict)
        if "VerificationResultPrimarySource" == resource_type:
            from . import verificationresult
            return verificationresult.VerificationResultPrimarySource(jsondict)
        if "VerificationResultValidator" == resource_type:
            from . import verificationresult
            return verificationresult.VerificationResultValidator(jsondict)
        if "VisionPrescription" == resource_type:
            from . import visionprescription
            return visionprescription.VisionPrescription(jsondict)
        if "VisionPrescriptionLensSpecification" == resource_type:
            from . import visionprescription
            return visionprescription.VisionPrescriptionLensSpecification(jsondict)
        if "VisionPrescriptionLensSpecificationPrism" == resource_type:
            from . import visionprescription
            return visionprescription.VisionPrescriptionLensSpecificationPrism(jsondict)
        from . import element
        return element.Element(jsondict)
