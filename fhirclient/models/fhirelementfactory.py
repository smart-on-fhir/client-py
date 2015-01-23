#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 on 2015-01-23.
#  2015, SMART Platforms.

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
        if "Alert" == resource_name:
            import alert
            return alert.Alert(jsondict)
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
        if "BackboneElement" == resource_name:
            import backboneelement
            return backboneelement.BackboneElement(jsondict)
        if "Basic" == resource_name:
            import basic
            return basic.Basic(jsondict)
        if "Binary" == resource_name:
            import binary
            return binary.Binary(jsondict)
        if "Bundle" == resource_name:
            import bundle
            return bundle.Bundle(jsondict)
        if "BundleEntry" == resource_name:
            import bundle
            return bundle.BundleEntry(jsondict)
        if "BundleEntryDeleted" == resource_name:
            import bundle
            return bundle.BundleEntryDeleted(jsondict)
        if "BundleLink" == resource_name:
            import bundle
            return bundle.BundleLink(jsondict)
        if "CarePlan" == resource_name:
            import careplan
            return careplan.CarePlan(jsondict)
        if "CarePlan2" == resource_name:
            import careplan2
            return careplan2.CarePlan2(jsondict)
        if "CarePlan2Participant" == resource_name:
            import careplan2
            return careplan2.CarePlan2Participant(jsondict)
        if "CarePlanActivity" == resource_name:
            import careplan
            return careplan.CarePlanActivity(jsondict)
        if "CarePlanActivitySimple" == resource_name:
            import careplan
            return careplan.CarePlanActivitySimple(jsondict)
        if "CarePlanGoal" == resource_name:
            import careplan
            return careplan.CarePlanGoal(jsondict)
        if "CarePlanParticipant" == resource_name:
            import careplan
            return careplan.CarePlanParticipant(jsondict)
        if "ClaimResponse" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponse(jsondict)
        if "ClaimResponseAdditem" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseAdditem(jsondict)
        if "ClaimResponseAdditemAdjudication" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseAdditemAdjudication(jsondict)
        if "ClaimResponseAdditemDetail" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseAdditemDetail(jsondict)
        if "ClaimResponseAdditemDetailAdjudication" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseAdditemDetailAdjudication(jsondict)
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
        if "ClaimResponseItemDetailSubdetail" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseItemDetailSubdetail(jsondict)
        if "ClaimResponseItemDetailSubdetailAdjudication" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseItemDetailSubdetailAdjudication(jsondict)
        if "ClaimResponseNote" == resource_name:
            import claimresponse
            return claimresponse.ClaimResponseNote(jsondict)
        if "ClinicalAssessment" == resource_name:
            import clinicalassessment
            return clinicalassessment.ClinicalAssessment(jsondict)
        if "ClinicalAssessmentDiagnosis" == resource_name:
            import clinicalassessment
            return clinicalassessment.ClinicalAssessmentDiagnosis(jsondict)
        if "ClinicalAssessmentInvestigations" == resource_name:
            import clinicalassessment
            return clinicalassessment.ClinicalAssessmentInvestigations(jsondict)
        if "ClinicalAssessmentRuledOut" == resource_name:
            import clinicalassessment
            return clinicalassessment.ClinicalAssessmentRuledOut(jsondict)
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
        if "ContractSigner" == resource_name:
            import contract
            return contract.ContractSigner(jsondict)
        if "ContractTerm" == resource_name:
            import contract
            return contract.ContractTerm(jsondict)
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
        if "DataElementBinding" == resource_name:
            import dataelement
            return dataelement.DataElementBinding(jsondict)
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
        if "DeviceMetricCalibrationInfo" == resource_name:
            import devicemetric
            return devicemetric.DeviceMetricCalibrationInfo(jsondict)
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
        if "DocumentReference" == resource_name:
            import documentreference
            return documentreference.DocumentReference(jsondict)
        if "DocumentReferenceContext" == resource_name:
            import documentreference
            return documentreference.DocumentReferenceContext(jsondict)
        if "DocumentReferenceRelatesTo" == resource_name:
            import documentreference
            return documentreference.DocumentReferenceRelatesTo(jsondict)
        if "DocumentReferenceService" == resource_name:
            import documentreference
            return documentreference.DocumentReferenceService(jsondict)
        if "DocumentReferenceServiceParameter" == resource_name:
            import documentreference
            return documentreference.DocumentReferenceServiceParameter(jsondict)
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
        if "ExtensionDefinition" == resource_name:
            import extensiondefinition
            return extensiondefinition.ExtensionDefinition(jsondict)
        if "ExtensionDefinitionMapping" == resource_name:
            import extensiondefinition
            return extensiondefinition.ExtensionDefinitionMapping(jsondict)
        if "FamilyHistory" == resource_name:
            import familyhistory
            return familyhistory.FamilyHistory(jsondict)
        if "FamilyHistoryRelation" == resource_name:
            import familyhistory
            return familyhistory.FamilyHistoryRelation(jsondict)
        if "FamilyHistoryRelationCondition" == resource_name:
            import familyhistory
            return familyhistory.FamilyHistoryRelationCondition(jsondict)
        if "Genetics" == resource_name:
            import genetics
            return genetics.Genetics(jsondict)
        if "Goal" == resource_name:
            import goal
            return goal.Goal(jsondict)
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
        if "HealthcareServiceNotAvailableTime" == resource_name:
            import healthcareservice
            return healthcareservice.HealthcareServiceNotAvailableTime(jsondict)
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
        if "InstitutionalClaim" == resource_name:
            import institutionalclaim
            return institutionalclaim.InstitutionalClaim(jsondict)
        if "InstitutionalClaimCoverage" == resource_name:
            import institutionalclaim
            return institutionalclaim.InstitutionalClaimCoverage(jsondict)
        if "InstitutionalClaimDiagnosis" == resource_name:
            import institutionalclaim
            return institutionalclaim.InstitutionalClaimDiagnosis(jsondict)
        if "InstitutionalClaimItem" == resource_name:
            import institutionalclaim
            return institutionalclaim.InstitutionalClaimItem(jsondict)
        if "InstitutionalClaimItemDetail" == resource_name:
            import institutionalclaim
            return institutionalclaim.InstitutionalClaimItemDetail(jsondict)
        if "InstitutionalClaimItemDetailSubDetail" == resource_name:
            import institutionalclaim
            return institutionalclaim.InstitutionalClaimItemDetailSubDetail(jsondict)
        if "InstitutionalClaimPayee" == resource_name:
            import institutionalclaim
            return institutionalclaim.InstitutionalClaimPayee(jsondict)
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
        if "NutritionOrderItem" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderItem(jsondict)
        if "NutritionOrderItemEnteralFormula" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderItemEnteralFormula(jsondict)
        if "NutritionOrderItemOralDiet" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderItemOralDiet(jsondict)
        if "NutritionOrderItemOralDietNutrients" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderItemOralDietNutrients(jsondict)
        if "NutritionOrderItemOralDietTexture" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderItemOralDietTexture(jsondict)
        if "NutritionOrderItemSupplement" == resource_name:
            import nutritionorder
            return nutritionorder.NutritionOrderItemSupplement(jsondict)
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
        if "OralHealthClaim" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaim(jsondict)
        if "OralHealthClaimCoverage" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaimCoverage(jsondict)
        if "OralHealthClaimDiagnosis" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaimDiagnosis(jsondict)
        if "OralHealthClaimItem" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaimItem(jsondict)
        if "OralHealthClaimItemDetail" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaimItemDetail(jsondict)
        if "OralHealthClaimItemDetailSubDetail" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaimItemDetailSubDetail(jsondict)
        if "OralHealthClaimItemProsthesis" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaimItemProsthesis(jsondict)
        if "OralHealthClaimMissingteeth" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaimMissingteeth(jsondict)
        if "OralHealthClaimOrthoPlan" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaimOrthoPlan(jsondict)
        if "OralHealthClaimPayee" == resource_name:
            import oralhealthclaim
            return oralhealthclaim.OralHealthClaimPayee(jsondict)
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
        if "Other" == resource_name:
            import other
            return other.Other(jsondict)
        if "Patient" == resource_name:
            import patient
            return patient.Patient(jsondict)
        if "PatientAnimal" == resource_name:
            import patient
            return patient.PatientAnimal(jsondict)
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
        if "PendedRequest" == resource_name:
            import pendedrequest
            return pendedrequest.PendedRequest(jsondict)
        if "Period" == resource_name:
            import period
            return period.Period(jsondict)
        if "Person" == resource_name:
            import person
            return person.Person(jsondict)
        if "PersonLink" == resource_name:
            import person
            return person.PersonLink(jsondict)
        if "PharmacyClaim" == resource_name:
            import pharmacyclaim
            return pharmacyclaim.PharmacyClaim(jsondict)
        if "PharmacyClaimCoverage" == resource_name:
            import pharmacyclaim
            return pharmacyclaim.PharmacyClaimCoverage(jsondict)
        if "PharmacyClaimDiagnosis" == resource_name:
            import pharmacyclaim
            return pharmacyclaim.PharmacyClaimDiagnosis(jsondict)
        if "PharmacyClaimItem" == resource_name:
            import pharmacyclaim
            return pharmacyclaim.PharmacyClaimItem(jsondict)
        if "PharmacyClaimItemDetail" == resource_name:
            import pharmacyclaim
            return pharmacyclaim.PharmacyClaimItemDetail(jsondict)
        if "PharmacyClaimItemDetailSubDetail" == resource_name:
            import pharmacyclaim
            return pharmacyclaim.PharmacyClaimItemDetailSubDetail(jsondict)
        if "PharmacyClaimPayee" == resource_name:
            import pharmacyclaim
            return pharmacyclaim.PharmacyClaimPayee(jsondict)
        if "Practitioner" == resource_name:
            import practitioner
            return practitioner.Practitioner(jsondict)
        if "PractitionerQualification" == resource_name:
            import practitioner
            return practitioner.PractitionerQualification(jsondict)
        if "Procedure" == resource_name:
            import procedure
            return procedure.Procedure(jsondict)
        if "ProcedurePerformer" == resource_name:
            import procedure
            return procedure.ProcedurePerformer(jsondict)
        if "ProcedureRelatedItem" == resource_name:
            import procedure
            return procedure.ProcedureRelatedItem(jsondict)
        if "ProcedureRequest" == resource_name:
            import procedurerequest
            return procedurerequest.ProcedureRequest(jsondict)
        if "ProfessionalClaim" == resource_name:
            import professionalclaim
            return professionalclaim.ProfessionalClaim(jsondict)
        if "ProfessionalClaimCoverage" == resource_name:
            import professionalclaim
            return professionalclaim.ProfessionalClaimCoverage(jsondict)
        if "ProfessionalClaimDiagnosis" == resource_name:
            import professionalclaim
            return professionalclaim.ProfessionalClaimDiagnosis(jsondict)
        if "ProfessionalClaimItem" == resource_name:
            import professionalclaim
            return professionalclaim.ProfessionalClaimItem(jsondict)
        if "ProfessionalClaimItemDetail" == resource_name:
            import professionalclaim
            return professionalclaim.ProfessionalClaimItemDetail(jsondict)
        if "ProfessionalClaimItemDetailSubDetail" == resource_name:
            import professionalclaim
            return professionalclaim.ProfessionalClaimItemDetailSubDetail(jsondict)
        if "ProfessionalClaimPayee" == resource_name:
            import professionalclaim
            return professionalclaim.ProfessionalClaimPayee(jsondict)
        if "Profile" == resource_name:
            import profile
            return profile.Profile(jsondict)
        if "ProfileMapping" == resource_name:
            import profile
            return profile.ProfileMapping(jsondict)
        if "ProfileSnapshot" == resource_name:
            import profile
            return profile.ProfileSnapshot(jsondict)
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
        if "Readjudicate" == resource_name:
            import readjudicate
            return readjudicate.Readjudicate(jsondict)
        if "ReadjudicateItem" == resource_name:
            import readjudicate
            return readjudicate.ReadjudicateItem(jsondict)
        if "Reference" == resource_name:
            import reference
            return reference.Reference(jsondict)
        if "ReferralRequest" == resource_name:
            import referralrequest
            return referralrequest.ReferralRequest(jsondict)
        if "RelatedPerson" == resource_name:
            import relatedperson
            return relatedperson.RelatedPerson(jsondict)
        if "Reversal" == resource_name:
            import reversal
            return reversal.Reversal(jsondict)
        if "ReversalCoverage" == resource_name:
            import reversal
            return reversal.ReversalCoverage(jsondict)
        if "ReversalPayee" == resource_name:
            import reversal
            return reversal.ReversalPayee(jsondict)
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
        if "SecurityEvent" == resource_name:
            import securityevent
            return securityevent.SecurityEvent(jsondict)
        if "SecurityEventEvent" == resource_name:
            import securityevent
            return securityevent.SecurityEventEvent(jsondict)
        if "SecurityEventObject" == resource_name:
            import securityevent
            return securityevent.SecurityEventObject(jsondict)
        if "SecurityEventObjectDetail" == resource_name:
            import securityevent
            return securityevent.SecurityEventObjectDetail(jsondict)
        if "SecurityEventParticipant" == resource_name:
            import securityevent
            return securityevent.SecurityEventParticipant(jsondict)
        if "SecurityEventParticipantNetwork" == resource_name:
            import securityevent
            return securityevent.SecurityEventParticipantNetwork(jsondict)
        if "SecurityEventSource" == resource_name:
            import securityevent
            return securityevent.SecurityEventSource(jsondict)
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
        if "SpecimenSource" == resource_name:
            import specimen
            return specimen.SpecimenSource(jsondict)
        if "SpecimenTreatment" == resource_name:
            import specimen
            return specimen.SpecimenTreatment(jsondict)
        if "StatusRequest" == resource_name:
            import statusrequest
            return statusrequest.StatusRequest(jsondict)
        if "StatusResponse" == resource_name:
            import statusresponse
            return statusresponse.StatusResponse(jsondict)
        if "StatusResponseNotes" == resource_name:
            import statusresponse
            return statusresponse.StatusResponseNotes(jsondict)
        if "Subscription" == resource_name:
            import subscription
            return subscription.Subscription(jsondict)
        if "SubscriptionChannel" == resource_name:
            import subscription
            return subscription.SubscriptionChannel(jsondict)
        if "SubscriptionTag" == resource_name:
            import subscription
            return subscription.SubscriptionTag(jsondict)
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
        if "SupportingDocumentation" == resource_name:
            import supportingdocumentation
            return supportingdocumentation.SupportingDocumentation(jsondict)
        if "SupportingDocumentationDetail" == resource_name:
            import supportingdocumentation
            return supportingdocumentation.SupportingDocumentationDetail(jsondict)
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
        if "VisionClaim" == resource_name:
            import visionclaim
            return visionclaim.VisionClaim(jsondict)
        if "VisionClaimCoverage" == resource_name:
            import visionclaim
            return visionclaim.VisionClaimCoverage(jsondict)
        if "VisionClaimDiagnosis" == resource_name:
            import visionclaim
            return visionclaim.VisionClaimDiagnosis(jsondict)
        if "VisionClaimItem" == resource_name:
            import visionclaim
            return visionclaim.VisionClaimItem(jsondict)
        if "VisionClaimItemDetail" == resource_name:
            import visionclaim
            return visionclaim.VisionClaimItemDetail(jsondict)
        if "VisionClaimItemDetailSubDetail" == resource_name:
            import visionclaim
            return visionclaim.VisionClaimItemDetailSubDetail(jsondict)
        if "VisionClaimPayee" == resource_name:
            import visionclaim
            return visionclaim.VisionClaimPayee(jsondict)
        if "VisionPrescription" == resource_name:
            import visionprescription
            return visionprescription.VisionPrescription(jsondict)
        if "VisionPrescriptionDispense" == resource_name:
            import visionprescription
            return visionprescription.VisionPrescriptionDispense(jsondict)
        return fhirelement.FHIRElement(json)
