#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-04-08.
#  2015, SMART Health IT.

import fhirelement


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    
    @classmethod
    def instantiate(cls, resource_name, jsondict):
        if "Address" == resource_name:
            import address
            return address.Address(jsondict)
        if "Age" == resource_name:
            import age
            return age.Age(jsondict)
        if "AllergyIntolerance" == resource_name:
            import allergyintolerance
            return allergyintolerance.AllergyIntolerance(jsondict)
        if "AllergyIntoleranceEvent" == resource_name:
            import allergyintolerance
            return allergyintolerance.AllergyIntoleranceEvent(jsondict)
        if "Appointment" == resource_name:
            import appointment
            return appointment.Appointment(jsondict)
        if "AppointmentParticipant" == resource_name:
            import appointment
            return appointment.AppointmentParticipant(jsondict)
        if "AppointmentResponse" == resource_name:
            import appointmentresponse
            return appointmentresponse.AppointmentResponse(jsondict)
        if "Attachment" == resource_name:
            import attachment
            return attachment.Attachment(jsondict)
        if "AuditEvent" == resource_name:
            import auditevent
            return auditevent.AuditEvent(jsondict)
        if "AuditEventEvent" == resource_name:
            import auditevent
            return auditevent.AuditEventEvent(jsondict)
        if "AuditEventObject" == resource_name:
            import auditevent
            return auditevent.AuditEventObject(jsondict)
        if "AuditEventObjectDetail" == resource_name:
            import auditevent
            return auditevent.AuditEventObjectDetail(jsondict)
        if "AuditEventParticipant" == resource_name:
            import auditevent
            return auditevent.AuditEventParticipant(jsondict)
        if "AuditEventParticipantNetwork" == resource_name:
            import auditevent
            return auditevent.AuditEventParticipantNetwork(jsondict)
        if "AuditEventSource" == resource_name:
            import auditevent
            return auditevent.AuditEventSource(jsondict)
        if "BackboneElement" == resource_name:
            import backboneelement
            return backboneelement.BackboneElement(jsondict)
        if "Basic" == resource_name:
            import basic
            return basic.Basic(jsondict)
        if "Binary" == resource_name:
            import binary
            return binary.Binary(jsondict)
        if "BodySite" == resource_name:
            import bodysite
            return bodysite.BodySite(jsondict)
        if "Bundle" == resource_name:
            import bundle
            return bundle.Bundle(jsondict)
        if "BundleEntry" == resource_name:
            import bundle
            return bundle.BundleEntry(jsondict)
        if "BundleEntrySearch" == resource_name:
            import bundle
            return bundle.BundleEntrySearch(jsondict)
        if "BundleEntryTransaction" == resource_name:
            import bundle
            return bundle.BundleEntryTransaction(jsondict)
        if "BundleEntryTransactionResponse" == resource_name:
            import bundle
            return bundle.BundleEntryTransactionResponse(jsondict)
        if "BundleLink" == resource_name:
            import bundle
            return bundle.BundleLink(jsondict)
        if "CarePlan" == resource_name:
            import careplan
            return careplan.CarePlan(jsondict)
        if "CarePlanActivity" == resource_name:
            import careplan
            return careplan.CarePlanActivity(jsondict)
        if "CarePlanActivityDetail" == resource_name:
            import careplan
            return careplan.CarePlanActivityDetail(jsondict)
        if "CarePlanParticipant" == resource_name:
            import careplan
            return careplan.CarePlanParticipant(jsondict)
        if "Claim" == resource_name:
            import claim
            return claim.Claim(jsondict)
        if "ClaimCoverage" == resource_name:
            import claim
            return claim.ClaimCoverage(jsondict)
        if "ClaimDiagnosis" == resource_name:
            import claim
            return claim.ClaimDiagnosis(jsondict)
        if "ClaimItem" == resource_name:
            import claim
            return claim.ClaimItem(jsondict)
        if "ClaimItemDetail" == resource_name:
            import claim
            return claim.ClaimItemDetail(jsondict)
        if "ClaimItemDetailSubDetail" == resource_name:
            import claim
            return claim.ClaimItemDetailSubDetail(jsondict)
        if "ClaimItemProsthesis" == resource_name:
            import claim
            return claim.ClaimItemProsthesis(jsondict)
        if "ClaimMissingTeeth" == resource_name:
            import claim
            return claim.ClaimMissingTeeth(jsondict)
        if "ClaimPayee" == resource_name:
            import claim
            return claim.ClaimPayee(jsondict)
        if "ClaimResponse" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponse(jsondict)
        if "ClaimResponseAddItem" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseAddItem(jsondict)
        if "ClaimResponseAddItemAdjudication" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseAddItemAdjudication(jsondict)
        if "ClaimResponseAddItemDetail" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseAddItemDetail(jsondict)
        if "ClaimResponseAddItemDetailAdjudication" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseAddItemDetailAdjudication(jsondict)
        if "ClaimResponseCoverage" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseCoverage(jsondict)
        if "ClaimResponseError" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseError(jsondict)
        if "ClaimResponseItem" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseItem(jsondict)
        if "ClaimResponseItemAdjudication" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseItemAdjudication(jsondict)
        if "ClaimResponseItemDetail" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseItemDetail(jsondict)
        if "ClaimResponseItemDetailAdjudication" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseItemDetailAdjudication(jsondict)
        if "ClaimResponseItemDetailSubDetail" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseItemDetailSubDetail(jsondict)
        if "ClaimResponseItemDetailSubDetailAdjudication" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseItemDetailSubDetailAdjudication(jsondict)
        if "ClaimResponseNote" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseNote(jsondict)
        if "ClinicalImpression" == resource_name:
            import clinicalimpression
            return clinicalimpression.ClinicalImpression(jsondict)
        if "ClinicalImpressionFinding" == resource_name:
            import clinicalimpression
            return clinicalimpression.ClinicalImpressionFinding(jsondict)
        if "ClinicalImpressionInvestigations" == resource_name:
            import clinicalimpression
            return clinicalimpression.ClinicalImpressionInvestigations(jsondict)
        if "ClinicalImpressionRuledOut" == resource_name:
            import clinicalimpression
            return clinicalimpression.ClinicalImpressionRuledOut(jsondict)
        if "CodeableConcept" == resource_name:
            import codeableconcept
            return codeableconcept.CodeableConcept(jsondict)
        if "Coding" == resource_name:
            import coding
            return coding.Coding(jsondict)
        if "Communication" == resource_name:
            import communication
            return communication.Communication(jsondict)
        if "CommunicationPayload" == resource_name:
            import communication
            return communication.CommunicationPayload(jsondict)
        if "CommunicationRequest" == resource_name:
            import communicationrequest
            return communicationrequest.CommunicationRequest(jsondict)
        if "CommunicationRequestPayload" == resource_name:
            import communicationrequest
            return communicationrequest.CommunicationRequestPayload(jsondict)
        if "Composition" == resource_name:
            import composition
            return composition.Composition(jsondict)
        if "CompositionAttester" == resource_name:
            import composition
            return composition.CompositionAttester(jsondict)
        if "CompositionEvent" == resource_name:
            import composition
            return composition.CompositionEvent(jsondict)
        if "CompositionSection" == resource_name:
            import composition
            return composition.CompositionSection(jsondict)
        if "ConceptMap" == resource_name:
            import conceptmap
            return conceptmap.ConceptMap(jsondict)
        if "ConceptMapContact" == resource_name:
            import conceptmap
            return conceptmap.ConceptMapContact(jsondict)
        if "ConceptMapElement" == resource_name:
            import conceptmap
            return conceptmap.ConceptMapElement(jsondict)
        if "ConceptMapElementDependsOn" == resource_name:
            import conceptmap
            return conceptmap.ConceptMapElementDependsOn(jsondict)
        if "ConceptMapElementMap" == resource_name:
            import conceptmap
            return conceptmap.ConceptMapElementMap(jsondict)
        if "Condition" == resource_name:
            import condition
            return condition.Condition(jsondict)
        if "ConditionDueTo" == resource_name:
            import condition
            return condition.ConditionDueTo(jsondict)
        if "ConditionEvidence" == resource_name:
            import condition
            return condition.ConditionEvidence(jsondict)
        if "ConditionLocation" == resource_name:
            import condition
            return condition.ConditionLocation(jsondict)
        if "ConditionOccurredFollowing" == resource_name:
            import condition
            return condition.ConditionOccurredFollowing(jsondict)
        if "ConditionStage" == resource_name:
            import condition
            return condition.ConditionStage(jsondict)
        if "Conformance" == resource_name:
            import conformance
            return conformance.Conformance(jsondict)
        if "ConformanceContact" == resource_name:
            import conformance
            return conformance.ConformanceContact(jsondict)
        if "ConformanceDocument" == resource_name:
            import conformance
            return conformance.ConformanceDocument(jsondict)
        if "ConformanceImplementation" == resource_name:
            import conformance
            return conformance.ConformanceImplementation(jsondict)
        if "ConformanceMessaging" == resource_name:
            import conformance
            return conformance.ConformanceMessaging(jsondict)
        if "ConformanceMessagingEvent" == resource_name:
            import conformance
            return conformance.ConformanceMessagingEvent(jsondict)
        if "ConformanceRest" == resource_name:
            import conformance
            return conformance.ConformanceRest(jsondict)
        if "ConformanceRestInteraction" == resource_name:
            import conformance
            return conformance.ConformanceRestInteraction(jsondict)
        if "ConformanceRestOperation" == resource_name:
            import conformance
            return conformance.ConformanceRestOperation(jsondict)
        if "ConformanceRestResource" == resource_name:
            import conformance
            return conformance.ConformanceRestResource(jsondict)
        if "ConformanceRestResourceInteraction" == resource_name:
            import conformance
            return conformance.ConformanceRestResourceInteraction(jsondict)
        if "ConformanceRestResourceSearchParam" == resource_name:
            import conformance
            return conformance.ConformanceRestResourceSearchParam(jsondict)
        if "ConformanceRestSecurity" == resource_name:
            import conformance
            return conformance.ConformanceRestSecurity(jsondict)
        if "ConformanceRestSecurityCertificate" == resource_name:
            import conformance
            return conformance.ConformanceRestSecurityCertificate(jsondict)
        if "ConformanceSoftware" == resource_name:
            import conformance
            return conformance.ConformanceSoftware(jsondict)
        if "ContactPoint" == resource_name:
            import contactpoint
            return contactpoint.ContactPoint(jsondict)
        if "Contract" == resource_name:
            import contract
            return contract.Contract(jsondict)
        if "ContractActor" == resource_name:
            import contract
            return contract.ContractActor(jsondict)
        if "ContractFriendly" == resource_name:
            import contract
            return contract.ContractFriendly(jsondict)
        if "ContractLegal" == resource_name:
            import contract
            return contract.ContractLegal(jsondict)
        if "ContractRule" == resource_name:
            import contract
            return contract.ContractRule(jsondict)
        if "ContractSigner" == resource_name:
            import contract
            return contract.ContractSigner(jsondict)
        if "ContractTerm" == resource_name:
            import contract
            return contract.ContractTerm(jsondict)
        if "ContractTermActor" == resource_name:
            import contract
            return contract.ContractTermActor(jsondict)
        if "ContractTermValuedItem" == resource_name:
            import contract
            return contract.ContractTermValuedItem(jsondict)
        if "ContractValuedItem" == resource_name:
            import contract
            return contract.ContractValuedItem(jsondict)
        if "Contraindication" == resource_name:
            import contraindication
            return contraindication.Contraindication(jsondict)
        if "ContraindicationMitigation" == resource_name:
            import contraindication
            return contraindication.ContraindicationMitigation(jsondict)
        if "Count" == resource_name:
            import count
            return count.Count(jsondict)
        if "Coverage" == resource_name:
            import coverage
            return coverage.Coverage(jsondict)
        if "DataElement" == resource_name:
            import dataelement
            return dataelement.DataElement(jsondict)
        if "DataElementContact" == resource_name:
            import dataelement
            return dataelement.DataElementContact(jsondict)
        if "DataElementMapping" == resource_name:
            import dataelement
            return dataelement.DataElementMapping(jsondict)
        if "Device" == resource_name:
            import device
            return device.Device(jsondict)
        if "DeviceComponent" == resource_name:
            import devicecomponent
            return devicecomponent.DeviceComponent(jsondict)
        if "DeviceComponentProductionSpecification" == resource_name:
            import devicecomponent
            return devicecomponent.DeviceComponentProductionSpecification(jsondict)
        if "DeviceMetric" == resource_name:
            import devicemetric
            return devicemetric.DeviceMetric(jsondict)
        if "DeviceMetricCalibration" == resource_name:
            import devicemetric
            return devicemetric.DeviceMetricCalibration(jsondict)
        if "DeviceUseRequest" == resource_name:
            import deviceuserequest
            return deviceuserequest.DeviceUseRequest(jsondict)
        if "DeviceUseStatement" == resource_name:
            import deviceusestatement
            return deviceusestatement.DeviceUseStatement(jsondict)
        if "DiagnosticOrder" == resource_name:
            import diagnosticorder
            return diagnosticorder.DiagnosticOrder(jsondict)
        if "DiagnosticOrderEvent" == resource_name:
            import diagnosticorder
            return diagnosticorder.DiagnosticOrderEvent(jsondict)
        if "DiagnosticOrderItem" == resource_name:
            import diagnosticorder
            return diagnosticorder.DiagnosticOrderItem(jsondict)
        if "DiagnosticReport" == resource_name:
            import diagnosticreport
            return diagnosticreport.DiagnosticReport(jsondict)
        if "DiagnosticReportImage" == resource_name:
            import diagnosticreport
            return diagnosticreport.DiagnosticReportImage(jsondict)
        if "Distance" == resource_name:
            import distance
            return distance.Distance(jsondict)
        if "DocumentManifest" == resource_name:
            import documentmanifest
            return documentmanifest.DocumentManifest(jsondict)
        if "DocumentManifestContent" == resource_name:
            import documentmanifest
            return documentmanifest.DocumentManifestContent(jsondict)
        if "DocumentManifestRelated" == resource_name:
            import documentmanifest
            return documentmanifest.DocumentManifestRelated(jsondict)
        if "DocumentReference" == resource_name:
            import documentreference
            return documentreference.DocumentReference(jsondict)
        if "DocumentReferenceContext" == resource_name:
            import documentreference
            return documentreference.DocumentReferenceContext(jsondict)
        if "DocumentReferenceContextRelated" == resource_name:
            import documentreference
            return documentreference.DocumentReferenceContextRelated(jsondict)
        if "DocumentReferenceRelatesTo" == resource_name:
            import documentreference
            return documentreference.DocumentReferenceRelatesTo(jsondict)
        if "DomainResource" == resource_name:
            import domainresource
            return domainresource.DomainResource(jsondict)
        if "Duration" == resource_name:
            import duration
            return duration.Duration(jsondict)
        if "ElementDefinition" == resource_name:
            import elementdefinition
            return elementdefinition.ElementDefinition(jsondict)
        if "ElementDefinitionBinding" == resource_name:
            import elementdefinition
            return elementdefinition.ElementDefinitionBinding(jsondict)
        if "ElementDefinitionConstraint" == resource_name:
            import elementdefinition
            return elementdefinition.ElementDefinitionConstraint(jsondict)
        if "ElementDefinitionMapping" == resource_name:
            import elementdefinition
            return elementdefinition.ElementDefinitionMapping(jsondict)
        if "ElementDefinitionSlicing" == resource_name:
            import elementdefinition
            return elementdefinition.ElementDefinitionSlicing(jsondict)
        if "ElementDefinitionType" == resource_name:
            import elementdefinition
            return elementdefinition.ElementDefinitionType(jsondict)
        if "EligibilityRequest" == resource_name:
            import eligibilityrequest
            return eligibilityrequest.EligibilityRequest(jsondict)
        if "EligibilityResponse" == resource_name:
            import eligibilityresponse
            return eligibilityresponse.EligibilityResponse(jsondict)
        if "Encounter" == resource_name:
            import encounter
            return encounter.Encounter(jsondict)
        if "EncounterHospitalization" == resource_name:
            import encounter
            return encounter.EncounterHospitalization(jsondict)
        if "EncounterLocation" == resource_name:
            import encounter
            return encounter.EncounterLocation(jsondict)
        if "EncounterParticipant" == resource_name:
            import encounter
            return encounter.EncounterParticipant(jsondict)
        if "EncounterStatusHistory" == resource_name:
            import encounter
            return encounter.EncounterStatusHistory(jsondict)
        if "EnrollmentRequest" == resource_name:
            import enrollmentrequest
            return enrollmentrequest.EnrollmentRequest(jsondict)
        if "EnrollmentResponse" == resource_name:
            import enrollmentresponse
            return enrollmentresponse.EnrollmentResponse(jsondict)
        if "EpisodeOfCare" == resource_name:
            import episodeofcare
            return episodeofcare.EpisodeOfCare(jsondict)
        if "EpisodeOfCareCareTeam" == resource_name:
            import episodeofcare
            return episodeofcare.EpisodeOfCareCareTeam(jsondict)
        if "EpisodeOfCareStatusHistory" == resource_name:
            import episodeofcare
            return episodeofcare.EpisodeOfCareStatusHistory(jsondict)
        if "ExplanationOfBenefit" == resource_name:
            import explanationofbenefit
            return explanationofbenefit.ExplanationOfBenefit(jsondict)
        if "Extension" == resource_name:
            import extension
            return extension.Extension(jsondict)
        if "FamilyMemberHistory" == resource_name:
            import familymemberhistory
            return familymemberhistory.FamilyMemberHistory(jsondict)
        if "FamilyMemberHistoryCondition" == resource_name:
            import familymemberhistory
            return familymemberhistory.FamilyMemberHistoryCondition(jsondict)
        if "Flag" == resource_name:
            import flag
            return flag.Flag(jsondict)
        if "Goal" == resource_name:
            import goal
            return goal.Goal(jsondict)
        if "GoalOutcome" == resource_name:
            import goal
            return goal.GoalOutcome(jsondict)
        if "Group" == resource_name:
            import group
            return group.Group(jsondict)
        if "GroupCharacteristic" == resource_name:
            import group
            return group.GroupCharacteristic(jsondict)
        if "HealthcareService" == resource_name:
            import healthcareservice
            return healthcareservice.HealthcareService(jsondict)
        if "HealthcareServiceAvailableTime" == resource_name:
            import healthcareservice
            return healthcareservice.HealthcareServiceAvailableTime(jsondict)
        if "HealthcareServiceNotAvailable" == resource_name:
            import healthcareservice
            return healthcareservice.HealthcareServiceNotAvailable(jsondict)
        if "HealthcareServiceServiceType" == resource_name:
            import healthcareservice
            return healthcareservice.HealthcareServiceServiceType(jsondict)
        if "HumanName" == resource_name:
            import humanname
            return humanname.HumanName(jsondict)
        if "Identifier" == resource_name:
            import identifier
            return identifier.Identifier(jsondict)
        if "ImagingObjectSelection" == resource_name:
            import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelection(jsondict)
        if "ImagingObjectSelectionStudy" == resource_name:
            import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudy(jsondict)
        if "ImagingObjectSelectionStudySeries" == resource_name:
            import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudySeries(jsondict)
        if "ImagingObjectSelectionStudySeriesInstance" == resource_name:
            import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudySeriesInstance(jsondict)
        if "ImagingObjectSelectionStudySeriesInstanceFrames" == resource_name:
            import imagingobjectselection
            return imagingobjectselection.ImagingObjectSelectionStudySeriesInstanceFrames(jsondict)
        if "ImagingStudy" == resource_name:
            import imagingstudy
            return imagingstudy.ImagingStudy(jsondict)
        if "ImagingStudySeries" == resource_name:
            import imagingstudy
            return imagingstudy.ImagingStudySeries(jsondict)
        if "ImagingStudySeriesInstance" == resource_name:
            import imagingstudy
            return imagingstudy.ImagingStudySeriesInstance(jsondict)
        if "Immunization" == resource_name:
            import immunization
            return immunization.Immunization(jsondict)
        if "ImmunizationExplanation" == resource_name:
            import immunization
            return immunization.ImmunizationExplanation(jsondict)
        if "ImmunizationReaction" == resource_name:
            import immunization
            return immunization.ImmunizationReaction(jsondict)
        if "ImmunizationRecommendation" == resource_name:
            import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendation(jsondict)
        if "ImmunizationRecommendationRecommendation" == resource_name:
            import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendation(jsondict)
        if "ImmunizationRecommendationRecommendationDateCriterion" == resource_name:
            import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationDateCriterion(jsondict)
        if "ImmunizationRecommendationRecommendationProtocol" == resource_name:
            import immunizationrecommendation
            return immunizationrecommendation.ImmunizationRecommendationRecommendationProtocol(jsondict)
        if "ImmunizationVaccinationProtocol" == resource_name:
            import immunization
            return immunization.ImmunizationVaccinationProtocol(jsondict)
        if "List" == resource_name:
            import list
            return list.List(jsondict)
        if "ListEntry" == resource_name:
            import list
            return list.ListEntry(jsondict)
        if "Location" == resource_name:
            import location
            return location.Location(jsondict)
        if "LocationPosition" == resource_name:
            import location
            return location.LocationPosition(jsondict)
        if "Media" == resource_name:
            import media
            return media.Media(jsondict)
        if "Medication" == resource_name:
            import medication
            return medication.Medication(jsondict)
        if "MedicationAdministration" == resource_name:
            import medicationadministration
            return medicationadministration.MedicationAdministration(jsondict)
        if "MedicationAdministrationDosage" == resource_name:
            import medicationadministration
            return medicationadministration.MedicationAdministrationDosage(jsondict)
        if "MedicationDispense" == resource_name:
            import medicationdispense
            return medicationdispense.MedicationDispense(jsondict)
        if "MedicationDispenseDosageInstruction" == resource_name:
            import medicationdispense
            return medicationdispense.MedicationDispenseDosageInstruction(jsondict)
        if "MedicationDispenseSubstitution" == resource_name:
            import medicationdispense
            return medicationdispense.MedicationDispenseSubstitution(jsondict)
        if "MedicationPackage" == resource_name:
            import medication
            return medication.MedicationPackage(jsondict)
        if "MedicationPackageContent" == resource_name:
            import medication
            return medication.MedicationPackageContent(jsondict)
        if "MedicationPrescription" == resource_name:
            import medicationprescription
            return medicationprescription.MedicationPrescription(jsondict)
        if "MedicationPrescriptionDispense" == resource_name:
            import medicationprescription
            return medicationprescription.MedicationPrescriptionDispense(jsondict)
        if "MedicationPrescriptionDosageInstruction" == resource_name:
            import medicationprescription
            return medicationprescription.MedicationPrescriptionDosageInstruction(jsondict)
        if "MedicationPrescriptionSubstitution" == resource_name:
            import medicationprescription
            return medicationprescription.MedicationPrescriptionSubstitution(jsondict)
        if "MedicationProduct" == resource_name:
            import medication
            return medication.MedicationProduct(jsondict)
        if "MedicationProductBatch" == resource_name:
            import medication
            return medication.MedicationProductBatch(jsondict)
        if "MedicationProductIngredient" == resource_name:
            import medication
            return medication.MedicationProductIngredient(jsondict)
        if "MedicationStatement" == resource_name:
            import medicationstatement
            return medicationstatement.MedicationStatement(jsondict)
        if "MedicationStatementDosage" == resource_name:
            import medicationstatement
            return medicationstatement.MedicationStatementDosage(jsondict)
        if "MessageHeader" == resource_name:
            import messageheader
            return messageheader.MessageHeader(jsondict)
        if "MessageHeaderDestination" == resource_name:
            import messageheader
            return messageheader.MessageHeaderDestination(jsondict)
        if "MessageHeaderResponse" == resource_name:
            import messageheader
            return messageheader.MessageHeaderResponse(jsondict)
        if "MessageHeaderSource" == resource_name:
            import messageheader
            return messageheader.MessageHeaderSource(jsondict)
        if "Meta" == resource_name:
            import meta
            return meta.Meta(jsondict)
        if "Money" == resource_name:
            import money
            return money.Money(jsondict)
        if "NamingSystem" == resource_name:
            import namingsystem
            return namingsystem.NamingSystem(jsondict)
        if "NamingSystemContact" == resource_name:
            import namingsystem
            return namingsystem.NamingSystemContact(jsondict)
        if "NamingSystemUniqueId" == resource_name:
            import namingsystem
            return namingsystem.NamingSystemUniqueId(jsondict)
        if "Narrative" == resource_name:
            import narrative
            return narrative.Narrative(jsondict)
        if "NutritionOrder" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrder(jsondict)
        if "NutritionOrderEnteralFormula" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderEnteralFormula(jsondict)
        if "NutritionOrderOralDiet" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderOralDiet(jsondict)
        if "NutritionOrderOralDietNutrient" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderOralDietNutrient(jsondict)
        if "NutritionOrderOralDietTexture" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderOralDietTexture(jsondict)
        if "NutritionOrderSupplement" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderSupplement(jsondict)
        if "Observation" == resource_name:
            import observation
            return observation.Observation(jsondict)
        if "ObservationReferenceRange" == resource_name:
            import observation
            return observation.ObservationReferenceRange(jsondict)
        if "ObservationRelated" == resource_name:
            import observation
            return observation.ObservationRelated(jsondict)
        if "OperationDefinition" == resource_name:
            import operationdefinition
            return operationdefinition.OperationDefinition(jsondict)
        if "OperationDefinitionContact" == resource_name:
            import operationdefinition
            return operationdefinition.OperationDefinitionContact(jsondict)
        if "OperationDefinitionParameter" == resource_name:
            import operationdefinition
            return operationdefinition.OperationDefinitionParameter(jsondict)
        if "OperationDefinitionParameterPart" == resource_name:
            import operationdefinition
            return operationdefinition.OperationDefinitionParameterPart(jsondict)
        if "OperationOutcome" == resource_name:
            import operationoutcome
            return operationoutcome.OperationOutcome(jsondict)
        if "OperationOutcomeIssue" == resource_name:
            import operationoutcome
            return operationoutcome.OperationOutcomeIssue(jsondict)
        if "Order" == resource_name:
            import order
            return order.Order(jsondict)
        if "OrderResponse" == resource_name:
            import orderresponse
            return orderresponse.OrderResponse(jsondict)
        if "OrderWhen" == resource_name:
            import order
            return order.OrderWhen(jsondict)
        if "Organization" == resource_name:
            import organization
            return organization.Organization(jsondict)
        if "OrganizationContact" == resource_name:
            import organization
            return organization.OrganizationContact(jsondict)
        if "Parameters" == resource_name:
            import parameters
            return parameters.Parameters(jsondict)
        if "ParametersParameter" == resource_name:
            import parameters
            return parameters.ParametersParameter(jsondict)
        if "ParametersParameterPart" == resource_name:
            import parameters
            return parameters.ParametersParameterPart(jsondict)
        if "Patient" == resource_name:
            import patient
            return patient.Patient(jsondict)
        if "PatientAnimal" == resource_name:
            import patient
            return patient.PatientAnimal(jsondict)
        if "PatientCommunication" == resource_name:
            import patient
            return patient.PatientCommunication(jsondict)
        if "PatientContact" == resource_name:
            import patient
            return patient.PatientContact(jsondict)
        if "PatientLink" == resource_name:
            import patient
            return patient.PatientLink(jsondict)
        if "PaymentNotice" == resource_name:
            import paymentnotice
            return paymentnotice.PaymentNotice(jsondict)
        if "PaymentReconciliation" == resource_name:
            import paymentreconciliation
            return paymentreconciliation.PaymentReconciliation(jsondict)
        if "PaymentReconciliationDetail" == resource_name:
            import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationDetail(jsondict)
        if "PaymentReconciliationNote" == resource_name:
            import paymentreconciliation
            return paymentreconciliation.PaymentReconciliationNote(jsondict)
        if "Period" == resource_name:
            import period
            return period.Period(jsondict)
        if "Person" == resource_name:
            import person
            return person.Person(jsondict)
        if "PersonLink" == resource_name:
            import person
            return person.PersonLink(jsondict)
        if "Practitioner" == resource_name:
            import practitioner
            return practitioner.Practitioner(jsondict)
        if "PractitionerPractitionerRole" == resource_name:
            import practitioner
            return practitioner.PractitionerPractitionerRole(jsondict)
        if "PractitionerQualification" == resource_name:
            import practitioner
            return practitioner.PractitionerQualification(jsondict)
        if "Procedure" == resource_name:
            import procedure
            return procedure.Procedure(jsondict)
        if "ProcedureBodySite" == resource_name:
            import procedure
            return procedure.ProcedureBodySite(jsondict)
        if "ProcedureDevice" == resource_name:
            import procedure
            return procedure.ProcedureDevice(jsondict)
        if "ProcedurePerformer" == resource_name:
            import procedure
            return procedure.ProcedurePerformer(jsondict)
        if "ProcedureRelatedItem" == resource_name:
            import procedure
            return procedure.ProcedureRelatedItem(jsondict)
        if "ProcedureRequest" == resource_name:
            import procedurerequest
            return procedurerequest.ProcedureRequest(jsondict)
        if "ProcedureRequestBodySite" == resource_name:
            import procedurerequest
            return procedurerequest.ProcedureRequestBodySite(jsondict)
        if "ProcessRequest" == resource_name:
            import processrequest
            return processrequest.ProcessRequest(jsondict)
        if "ProcessRequestItem" == resource_name:
            import processrequest
            return processrequest.ProcessRequestItem(jsondict)
        if "ProcessResponse" == resource_name:
            import processresponse
            return processresponse.ProcessResponse(jsondict)
        if "ProcessResponseNotes" == resource_name:
            import processresponse
            return processresponse.ProcessResponseNotes(jsondict)
        if "Provenance" == resource_name:
            import provenance
            return provenance.Provenance(jsondict)
        if "ProvenanceAgent" == resource_name:
            import provenance
            return provenance.ProvenanceAgent(jsondict)
        if "ProvenanceEntity" == resource_name:
            import provenance
            return provenance.ProvenanceEntity(jsondict)
        if "Quantity" == resource_name:
            import quantity
            return quantity.Quantity(jsondict)
        if "Questionnaire" == resource_name:
            import questionnaire
            return questionnaire.Questionnaire(jsondict)
        if "QuestionnaireAnswers" == resource_name:
            import questionnaireanswers
            return questionnaireanswers.QuestionnaireAnswers(jsondict)
        if "QuestionnaireAnswersGroup" == resource_name:
            import questionnaireanswers
            return questionnaireanswers.QuestionnaireAnswersGroup(jsondict)
        if "QuestionnaireAnswersGroupQuestion" == resource_name:
            import questionnaireanswers
            return questionnaireanswers.QuestionnaireAnswersGroupQuestion(jsondict)
        if "QuestionnaireAnswersGroupQuestionAnswer" == resource_name:
            import questionnaireanswers
            return questionnaireanswers.QuestionnaireAnswersGroupQuestionAnswer(jsondict)
        if "QuestionnaireGroup" == resource_name:
            import questionnaire
            return questionnaire.QuestionnaireGroup(jsondict)
        if "QuestionnaireGroupQuestion" == resource_name:
            import questionnaire
            return questionnaire.QuestionnaireGroupQuestion(jsondict)
        if "Range" == resource_name:
            import range
            return range.Range(jsondict)
        if "Ratio" == resource_name:
            import ratio
            return ratio.Ratio(jsondict)
        if "Reference" == resource_name:
            import reference
            return reference.Reference(jsondict)
        if "ReferralRequest" == resource_name:
            import referralrequest
            return referralrequest.ReferralRequest(jsondict)
        if "RelatedPerson" == resource_name:
            import relatedperson
            return relatedperson.RelatedPerson(jsondict)
        if "Resource" == resource_name:
            import resource
            return resource.Resource(jsondict)
        if "RiskAssessment" == resource_name:
            import riskassessment
            return riskassessment.RiskAssessment(jsondict)
        if "RiskAssessmentPrediction" == resource_name:
            import riskassessment
            return riskassessment.RiskAssessmentPrediction(jsondict)
        if "SampledData" == resource_name:
            import sampleddata
            return sampleddata.SampledData(jsondict)
        if "Schedule" == resource_name:
            import schedule
            return schedule.Schedule(jsondict)
        if "SearchParameter" == resource_name:
            import searchparameter
            return searchparameter.SearchParameter(jsondict)
        if "SearchParameterContact" == resource_name:
            import searchparameter
            return searchparameter.SearchParameterContact(jsondict)
        if "Signature" == resource_name:
            import signature
            return signature.Signature(jsondict)
        if "Slot" == resource_name:
            import slot
            return slot.Slot(jsondict)
        if "Specimen" == resource_name:
            import specimen
            return specimen.Specimen(jsondict)
        if "SpecimenCollection" == resource_name:
            import specimen
            return specimen.SpecimenCollection(jsondict)
        if "SpecimenContainer" == resource_name:
            import specimen
            return specimen.SpecimenContainer(jsondict)
        if "SpecimenTreatment" == resource_name:
            import specimen
            return specimen.SpecimenTreatment(jsondict)
        if "StructureDefinition" == resource_name:
            import structuredefinition
            return structuredefinition.StructureDefinition(jsondict)
        if "StructureDefinitionContact" == resource_name:
            import structuredefinition
            return structuredefinition.StructureDefinitionContact(jsondict)
        if "StructureDefinitionDifferential" == resource_name:
            import structuredefinition
            return structuredefinition.StructureDefinitionDifferential(jsondict)
        if "StructureDefinitionMapping" == resource_name:
            import structuredefinition
            return structuredefinition.StructureDefinitionMapping(jsondict)
        if "StructureDefinitionSnapshot" == resource_name:
            import structuredefinition
            return structuredefinition.StructureDefinitionSnapshot(jsondict)
        if "Subscription" == resource_name:
            import subscription
            return subscription.Subscription(jsondict)
        if "SubscriptionChannel" == resource_name:
            import subscription
            return subscription.SubscriptionChannel(jsondict)
        if "Substance" == resource_name:
            import substance
            return substance.Substance(jsondict)
        if "SubstanceIngredient" == resource_name:
            import substance
            return substance.SubstanceIngredient(jsondict)
        if "SubstanceInstance" == resource_name:
            import substance
            return substance.SubstanceInstance(jsondict)
        if "Supply" == resource_name:
            import supply
            return supply.Supply(jsondict)
        if "SupplyDispense" == resource_name:
            import supply
            return supply.SupplyDispense(jsondict)
        if "Timing" == resource_name:
            import timing
            return timing.Timing(jsondict)
        if "TimingRepeat" == resource_name:
            import timing
            return timing.TimingRepeat(jsondict)
        if "ValueSet" == resource_name:
            import valueset
            return valueset.ValueSet(jsondict)
        if "ValueSetCompose" == resource_name:
            import valueset
            return valueset.ValueSetCompose(jsondict)
        if "ValueSetComposeInclude" == resource_name:
            import valueset
            return valueset.ValueSetComposeInclude(jsondict)
        if "ValueSetComposeIncludeConcept" == resource_name:
            import valueset
            return valueset.ValueSetComposeIncludeConcept(jsondict)
        if "ValueSetComposeIncludeFilter" == resource_name:
            import valueset
            return valueset.ValueSetComposeIncludeFilter(jsondict)
        if "ValueSetContact" == resource_name:
            import valueset
            return valueset.ValueSetContact(jsondict)
        if "ValueSetDefine" == resource_name:
            import valueset
            return valueset.ValueSetDefine(jsondict)
        if "ValueSetDefineConcept" == resource_name:
            import valueset
            return valueset.ValueSetDefineConcept(jsondict)
        if "ValueSetDefineConceptDesignation" == resource_name:
            import valueset
            return valueset.ValueSetDefineConceptDesignation(jsondict)
        if "ValueSetExpansion" == resource_name:
            import valueset
            return valueset.ValueSetExpansion(jsondict)
        if "ValueSetExpansionContains" == resource_name:
            import valueset
            return valueset.ValueSetExpansionContains(jsondict)
        if "ValueSetExpansionParameter" == resource_name:
            import valueset
            return valueset.ValueSetExpansionParameter(jsondict)
        if "VisionPrescription" == resource_name:
            import visionprescription
            return visionprescription.VisionPrescription(jsondict)
        if "VisionPrescriptionDispense" == resource_name:
            import visionprescription
            return visionprescription.VisionPrescriptionDispense(jsondict)
        return fhirelement.FHIRElement(json)
