#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


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
        if "BodySite" == resource_type:
            from . import bodysite
            return bodysite.BodySite(jsondict)
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
        if "CapabilityStatementMessagingEvent" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessagingEvent(jsondict)
        if "CapabilityStatementMessagingSupportedMessage" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementMessagingSupportedMessage(jsondict)
        if "CapabilityStatementRest" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRest(jsondict)
        if "CapabilityStatementRestInteraction" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestInteraction(jsondict)
        if "CapabilityStatementRestOperation" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestOperation(jsondict)
        if "CapabilityStatementRestResource" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResource(jsondict)
        if "CapabilityStatementRestResourceInteraction" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceInteraction(jsondict)
        if "CapabilityStatementRestResourceSearchParam" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestResourceSearchParam(jsondict)
        if "CapabilityStatementRestSecurity" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestSecurity(jsondict)
        if "CapabilityStatementRestSecurityCertificate" == resource_type:
            from . import capabilitystatement
            return capabilitystatement.CapabilityStatementRestSecurityCertificate(jsondict)
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
        if "ChargeItem" == resource_type:
            from . import chargeitem
            return chargeitem.ChargeItem(jsondict)
        if "ChargeItemParticipant" == resource_type:
            from . import chargeitem
            return chargeitem.ChargeItemParticipant(jsondict)
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
        if "ClaimInformation" == resource_type:
            from . import claim
            return claim.ClaimInformation(jsondict)
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
        if "CommunicationRequestRequester" == resource_type:
            from . import communicationrequest
            return communicationrequest.CommunicationRequestRequester(jsondict)
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
        if "ConsentActor" == resource_type:
            from . import consent
            return consent.ConsentActor(jsondict)
        if "ConsentData" == resource_type:
            from . import consent
            return consent.ConsentData(jsondict)
        if "ConsentExcept" == resource_type:
            from . import consent
            return consent.ConsentExcept(jsondict)
        if "ConsentExceptActor" == resource_type:
            from . import consent
            return consent.ConsentExceptActor(jsondict)
        if "ConsentExceptData" == resource_type:
            from . import consent
            return consent.ConsentExceptData(jsondict)
        if "ConsentPolicy" == resource_type:
            from . import consent
            return consent.ConsentPolicy(jsondict)
        if "ContactDetail" == resource_type:
            from . import contactdetail
            return contactdetail.ContactDetail(jsondict)
        if "ContactPoint" == resource_type:
            from . import contactpoint
            return contactpoint.ContactPoint(jsondict)
        if "Contract" == resource_type:
            from . import contract
            return contract.Contract(jsondict)
        if "ContractAgent" == resource_type:
            from . import contract
            return contract.ContractAgent(jsondict)
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
        if "ContractTermAgent" == resource_type:
            from . import contract
            return contract.ContractTermAgent(jsondict)
        if "ContractTermValuedItem" == resource_type:
            from . import contract
            return contract.ContractTermValuedItem(jsondict)
        if "ContractValuedItem" == resource_type:
            from . import contract
            return contract.ContractValuedItem(jsondict)
        if "Contributor" == resource_type:
            from . import contributor
            return contributor.Contributor(jsondict)
        if "Count" == resource_type:
            from . import count
            return count.Count(jsondict)
        if "Coverage" == resource_type:
            from . import coverage
            return coverage.Coverage(jsondict)
        if "CoverageGrouping" == resource_type:
            from . import coverage
            return coverage.CoverageGrouping(jsondict)
        if "DataElement" == resource_type:
            from . import dataelement
            return dataelement.DataElement(jsondict)
        if "DataElementMapping" == resource_type:
            from . import dataelement
            return dataelement.DataElementMapping(jsondict)
        if "DataRequirement" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirement(jsondict)
        if "DataRequirementCodeFilter" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirementCodeFilter(jsondict)
        if "DataRequirementDateFilter" == resource_type:
            from . import datarequirement
            return datarequirement.DataRequirementDateFilter(jsondict)
        if "DetectedIssue" == resource_type:
            from . import detectedissue
            return detectedissue.DetectedIssue(jsondict)
        if "DetectedIssueMitigation" == resource_type:
            from . import detectedissue
            return detectedissue.DetectedIssueMitigation(jsondict)
        if "Device" == resource_type:
            from . import device
            return device.Device(jsondict)
        if "DeviceComponent" == resource_type:
            from . import devicecomponent
            return devicecomponent.DeviceComponent(jsondict)
        if "DeviceComponentProductionSpecification" == resource_type:
            from . import devicecomponent
            return devicecomponent.DeviceComponentProductionSpecification(jsondict)
        if "DeviceMetric" == resource_type:
            from . import devicemetric
            return devicemetric.DeviceMetric(jsondict)
        if "DeviceMetricCalibration" == resource_type:
            from . import devicemetric
            return devicemetric.DeviceMetricCalibration(jsondict)
        if "DeviceRequest" == resource_type:
            from . import devicerequest
            return devicerequest.DeviceRequest(jsondict)
        if "DeviceRequestRequester" == resource_type:
            from . import devicerequest
            return devicerequest.DeviceRequestRequester(jsondict)
        if "DeviceUdi" == resource_type:
            from . import device
            return device.DeviceUdi(jsondict)
        if "DeviceUseStatement" == resource_type:
            from . import deviceusestatement
            return deviceusestatement.DeviceUseStatement(jsondict)
        if "DiagnosticReport" == resource_type:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReport(jsondict)
        if "DiagnosticReportImage" == resource_type:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReportImage(jsondict)
        if "DiagnosticReportPerformer" == resource_type:
            from . import diagnosticreport
            return diagnosticreport.DiagnosticReportPerformer(jsondict)
        if "Distance" == resource_type:
            from . import distance
            return distance.Distance(jsondict)
        if "DocumentManifest" == resource_type:
            from . import documentmanifest
            return documentmanifest.DocumentManifest(jsondict)
        if "DocumentManifestContent" == resource_type:
            from . import documentmanifest
            return documentmanifest.DocumentManifestContent(jsondict)
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
        if "DocumentReferenceContextRelated" == resource_type:
            from . import documentreference
            return documentreference.DocumentReferenceContextRelated(jsondict)
        if "DocumentReferenceRelatesTo" == resource_type:
            from . import documentreference
            return documentreference.DocumentReferenceRelatesTo(jsondict)
        if "DomainResource" == resource_type:
            from . import domainresource
            return domainresource.DomainResource(jsondict)
        if "Dosage" == resource_type:
            from . import dosage
            return dosage.Dosage(jsondict)
        if "Duration" == resource_type:
            from . import duration
            return duration.Duration(jsondict)
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
        if "EligibilityRequest" == resource_type:
            from . import eligibilityrequest
            return eligibilityrequest.EligibilityRequest(jsondict)
        if "EligibilityResponse" == resource_type:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponse(jsondict)
        if "EligibilityResponseError" == resource_type:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponseError(jsondict)
        if "EligibilityResponseInsurance" == resource_type:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponseInsurance(jsondict)
        if "EligibilityResponseInsuranceBenefitBalance" == resource_type:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponseInsuranceBenefitBalance(jsondict)
        if "EligibilityResponseInsuranceBenefitBalanceFinancial" == resource_type:
            from . import eligibilityresponse
            return eligibilityresponse.EligibilityResponseInsuranceBenefitBalanceFinancial(jsondict)
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
        if "ExpansionProfile" == resource_type:
            from . import expansionprofile
            return expansionprofile.ExpansionProfile(jsondict)
        if "ExpansionProfileDesignation" == resource_type:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignation(jsondict)
        if "ExpansionProfileDesignationExclude" == resource_type:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignationExclude(jsondict)
        if "ExpansionProfileDesignationExcludeDesignation" == resource_type:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignationExcludeDesignation(jsondict)
        if "ExpansionProfileDesignationInclude" == resource_type:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignationInclude(jsondict)
        if "ExpansionProfileDesignationIncludeDesignation" == resource_type:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileDesignationIncludeDesignation(jsondict)
        if "ExpansionProfileExcludedSystem" == resource_type:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileExcludedSystem(jsondict)
        if "ExpansionProfileFixedVersion" == resource_type:
            from . import expansionprofile
            return expansionprofile.ExpansionProfileFixedVersion(jsondict)
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
        if "ExplanationOfBenefitInformation" == resource_type:
            from . import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefitInformation(jsondict)
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
        if "HealthcareServiceNotAvailable" == resource_type:
            from . import healthcareservice
            return healthcareservice.HealthcareServiceNotAvailable(jsondict)
        if "HumanName" == resource_type:
            from . import humanname
            return humanname.HumanName(jsondict)
        if "Identifier" == resource_type:
            from . import identifier
            return identifier.Identifier(jsondict)
        if "ImagingManifest" == resource_type:
            from . import imagingmanifest
            return imagingmanifest.ImagingManifest(jsondict)
        if "ImagingManifestStudy" == resource_type:
            from . import imagingmanifest
            return imagingmanifest.ImagingManifestStudy(jsondict)
        if "ImagingManifestStudySeries" == resource_type:
            from . import imagingmanifest
            return imagingmanifest.ImagingManifestStudySeries(jsondict)
        if "ImagingManifestStudySeriesInstance" == resource_type:
            from . import imagingmanifest
            return imagingmanifest.ImagingManifestStudySeriesInstance(jsondict)
        if "ImagingStudy" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudy(jsondict)
        if "ImagingStudySeries" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeries(jsondict)
        if "ImagingStudySeriesInstance" == resource_type:
            from . import imagingstudy
            return imagingstudy.ImagingStudySeriesInstance(jsondict)
        if "Immunization" == resource_type:
            from . import immunization
            return immunization.Immunization(jsondict)
        if "ImmunizationExplanation" == resource_type:
            from . import immunization
            return immunization.ImmunizationExplanation(jsondict)
        if "ImmunizationPractitioner" == resource_type:
            from . import immunization
            return immunization.ImmunizationPractitioner(jsondict)
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
        if "ImmunizationRecommendationRecommendationProtocol" == resource_type:
            from . import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationProtocol(jsondict)
        if "ImmunizationVaccinationProtocol" == resource_type:
            from . import immunization
            return immunization.ImmunizationVaccinationProtocol(jsondict)
        if "ImplementationGuide" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuide(jsondict)
        if "ImplementationGuideDependency" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideDependency(jsondict)
        if "ImplementationGuideGlobal" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuideGlobal(jsondict)
        if "ImplementationGuidePackage" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuidePackage(jsondict)
        if "ImplementationGuidePackageResource" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuidePackageResource(jsondict)
        if "ImplementationGuidePage" == resource_type:
            from . import implementationguide
            return implementationguide.ImplementationGuidePage(jsondict)
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
        if "LocationPosition" == resource_type:
            from . import location
            return location.LocationPosition(jsondict)
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
        if "MedicationPackage" == resource_type:
            from . import medication
            return medication.MedicationPackage(jsondict)
        if "MedicationPackageBatch" == resource_type:
            from . import medication
            return medication.MedicationPackageBatch(jsondict)
        if "MedicationPackageContent" == resource_type:
            from . import medication
            return medication.MedicationPackageContent(jsondict)
        if "MedicationRequest" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequest(jsondict)
        if "MedicationRequestDispenseRequest" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequestDispenseRequest(jsondict)
        if "MedicationRequestRequester" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequestRequester(jsondict)
        if "MedicationRequestSubstitution" == resource_type:
            from . import medicationrequest
            return medicationrequest.MedicationRequestSubstitution(jsondict)
        if "MedicationStatement" == resource_type:
            from . import medicationstatement
            return medicationstatement.MedicationStatement(jsondict)
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
        if "ObservationReferenceRange" == resource_type:
            from . import observation
            return observation.ObservationReferenceRange(jsondict)
        if "ObservationRelated" == resource_type:
            from . import observation
            return observation.ObservationRelated(jsondict)
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
        if "OperationOutcome" == resource_type:
            from . import operationoutcome
            return operationoutcome.OperationOutcome(jsondict)
        if "OperationOutcomeIssue" == resource_type:
            from . import operationoutcome
            return operationoutcome.OperationOutcomeIssue(jsondict)
        if "Organization" == resource_type:
            from . import organization
            return organization.Organization(jsondict)
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
        if "PatientAnimal" == resource_type:
            from . import patient
            return patient.PatientAnimal(jsondict)
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
        if "ProcedureRequest" == resource_type:
            from . import procedurerequest
            return procedurerequest.ProcedureRequest(jsondict)
        if "ProcedureRequestRequester" == resource_type:
            from . import procedurerequest
            return procedurerequest.ProcedureRequestRequester(jsondict)
        if "ProcessRequest" == resource_type:
            from . import processrequest
            return processrequest.ProcessRequest(jsondict)
        if "ProcessRequestItem" == resource_type:
            from . import processrequest
            return processrequest.ProcessRequestItem(jsondict)
        if "ProcessResponse" == resource_type:
            from . import processresponse
            return processresponse.ProcessResponse(jsondict)
        if "ProcessResponseProcessNote" == resource_type:
            from . import processresponse
            return processresponse.ProcessResponseProcessNote(jsondict)
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
        if "Questionnaire" == resource_type:
            from . import questionnaire
            return questionnaire.Questionnaire(jsondict)
        if "QuestionnaireItem" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItem(jsondict)
        if "QuestionnaireItemEnableWhen" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItemEnableWhen(jsondict)
        if "QuestionnaireItemOption" == resource_type:
            from . import questionnaire
            return questionnaire.QuestionnaireItemOption(jsondict)
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
        if "ReferralRequest" == resource_type:
            from . import referralrequest
            return referralrequest.ReferralRequest(jsondict)
        if "ReferralRequestRequester" == resource_type:
            from . import referralrequest
            return referralrequest.ReferralRequestRequester(jsondict)
        if "RelatedArtifact" == resource_type:
            from . import relatedartifact
            return relatedartifact.RelatedArtifact(jsondict)
        if "RelatedPerson" == resource_type:
            from . import relatedperson
            return relatedperson.RelatedPerson(jsondict)
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
        if "ResearchStudy" == resource_type:
            from . import researchstudy
            return researchstudy.ResearchStudy(jsondict)
        if "ResearchStudyArm" == resource_type:
            from . import researchstudy
            return researchstudy.ResearchStudyArm(jsondict)
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
        if "Sequence" == resource_type:
            from . import sequence
            return sequence.Sequence(jsondict)
        if "SequenceQuality" == resource_type:
            from . import sequence
            return sequence.SequenceQuality(jsondict)
        if "SequenceReferenceSeq" == resource_type:
            from . import sequence
            return sequence.SequenceReferenceSeq(jsondict)
        if "SequenceRepository" == resource_type:
            from . import sequence
            return sequence.SequenceRepository(jsondict)
        if "SequenceVariant" == resource_type:
            from . import sequence
            return sequence.SequenceVariant(jsondict)
        if "ServiceDefinition" == resource_type:
            from . import servicedefinition
            return servicedefinition.ServiceDefinition(jsondict)
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
        if "SpecimenProcessing" == resource_type:
            from . import specimen
            return specimen.SpecimenProcessing(jsondict)
        if "StructureDefinition" == resource_type:
            from . import structuredefinition
            return structuredefinition.StructureDefinition(jsondict)
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
        if "SubstanceIngredient" == resource_type:
            from . import substance
            return substance.SubstanceIngredient(jsondict)
        if "SubstanceInstance" == resource_type:
            from . import substance
            return substance.SubstanceInstance(jsondict)
        if "SupplyDelivery" == resource_type:
            from . import supplydelivery
            return supplydelivery.SupplyDelivery(jsondict)
        if "SupplyDeliverySuppliedItem" == resource_type:
            from . import supplydelivery
            return supplydelivery.SupplyDeliverySuppliedItem(jsondict)
        if "SupplyRequest" == resource_type:
            from . import supplyrequest
            return supplyrequest.SupplyRequest(jsondict)
        if "SupplyRequestOrderedItem" == resource_type:
            from . import supplyrequest
            return supplyrequest.SupplyRequestOrderedItem(jsondict)
        if "SupplyRequestRequester" == resource_type:
            from . import supplyrequest
            return supplyrequest.SupplyRequestRequester(jsondict)
        if "Task" == resource_type:
            from . import task
            return task.Task(jsondict)
        if "TaskInput" == resource_type:
            from . import task
            return task.TaskInput(jsondict)
        if "TaskOutput" == resource_type:
            from . import task
            return task.TaskOutput(jsondict)
        if "TaskRequester" == resource_type:
            from . import task
            return task.TaskRequester(jsondict)
        if "TaskRestriction" == resource_type:
            from . import task
            return task.TaskRestriction(jsondict)
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
        if "TestScriptRule" == resource_type:
            from . import testscript
            return testscript.TestScriptRule(jsondict)
        if "TestScriptRuleParam" == resource_type:
            from . import testscript
            return testscript.TestScriptRuleParam(jsondict)
        if "TestScriptRuleset" == resource_type:
            from . import testscript
            return testscript.TestScriptRuleset(jsondict)
        if "TestScriptRulesetRule" == resource_type:
            from . import testscript
            return testscript.TestScriptRulesetRule(jsondict)
        if "TestScriptRulesetRuleParam" == resource_type:
            from . import testscript
            return testscript.TestScriptRulesetRuleParam(jsondict)
        if "TestScriptSetup" == resource_type:
            from . import testscript
            return testscript.TestScriptSetup(jsondict)
        if "TestScriptSetupAction" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupAction(jsondict)
        if "TestScriptSetupActionAssert" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionAssert(jsondict)
        if "TestScriptSetupActionAssertRule" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionAssertRule(jsondict)
        if "TestScriptSetupActionAssertRuleParam" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionAssertRuleParam(jsondict)
        if "TestScriptSetupActionAssertRuleset" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionAssertRuleset(jsondict)
        if "TestScriptSetupActionAssertRulesetRule" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionAssertRulesetRule(jsondict)
        if "TestScriptSetupActionAssertRulesetRuleParam" == resource_type:
            from . import testscript
            return testscript.TestScriptSetupActionAssertRulesetRuleParam(jsondict)
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
        if "VisionPrescription" == resource_type:
            from . import visionprescription
            return visionprescription.VisionPrescription(jsondict)
        if "VisionPrescriptionDispense" == resource_type:
            from . import visionprescription
            return visionprescription.VisionPrescriptionDispense(jsondict)
        from . import element
        return element.Element(jsondict)
