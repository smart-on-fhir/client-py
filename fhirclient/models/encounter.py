#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Encounter) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import duration
import fhirelement
import fhirreference
import identifier
import period


class Encounter(domainresource.DomainResource):
    """ An interaction during which services are provided to the patient.
    
    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """
    
    resource_name = "Encounter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.episodeOfCare = None
        """ An episode of care that this encounter should be recorded against.
        Type `FHIRReference` referencing `EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.fulfills = None
        """ The appointment that scheduled this encounter.
        Type `FHIRReference` referencing `Appointment` (represented as `dict` in JSON). """
        
        self.hospitalization = None
        """ Details about an admission to a clinic.
        Type `EncounterHospitalization` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier(s) by which this encounter is known.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.incomingReferralRequest = None
        """ Incoming Referral Request.
        List of `FHIRReference` items referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason the encounter takes place (resource).
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.klass = None
        """ inpatient | outpatient | ambulatory | emergency +.
        Type `str`. """
        
        self.length = None
        """ Quantity of time the encounter lasted (less time absent).
        Type `Duration` (represented as `dict` in JSON). """
        
        self.location = None
        """ List of locations the patient has been at.
        List of `EncounterLocation` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Another Encounter this encounter is part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.participant = None
        """ List of participants involved in the encounter.
        List of `EncounterParticipant` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient present at the encounter.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ The start and end time of the encounter.
        Type `Period` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Indicates the urgency of the encounter.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Reason the encounter takes place (code).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceProvider = None
        """ The custodian organization of this Encounter record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | arrived | in-progress | onleave | finished | cancelled.
        Type `str`. """
        
        self.statusHistory = None
        """ List of Encounter statuses.
        List of `EncounterStatusHistory` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Specific type of encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Encounter, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Encounter, self).update_with_json(jsondict)
        if 'episodeOfCare' in jsondict:
            self.episodeOfCare = fhirreference.FHIRReference.with_json_and_owner(jsondict['episodeOfCare'], self)
        if 'fulfills' in jsondict:
            self.fulfills = fhirreference.FHIRReference.with_json_and_owner(jsondict['fulfills'], self)
        if 'hospitalization' in jsondict:
            self.hospitalization = EncounterHospitalization.with_json_and_owner(jsondict['hospitalization'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'incomingReferralRequest' in jsondict:
            self.incomingReferralRequest = fhirreference.FHIRReference.with_json_and_owner(jsondict['incomingReferralRequest'], self)
        if 'indication' in jsondict:
            self.indication = fhirreference.FHIRReference.with_json_and_owner(jsondict['indication'], self)
        if 'class' in jsondict:
            self.klass = jsondict['class']
        if 'length' in jsondict:
            self.length = duration.Duration.with_json_and_owner(jsondict['length'], self)
        if 'location' in jsondict:
            self.location = EncounterLocation.with_json_and_owner(jsondict['location'], self)
        if 'partOf' in jsondict:
            self.partOf = fhirreference.FHIRReference.with_json_and_owner(jsondict['partOf'], self)
        if 'participant' in jsondict:
            self.participant = EncounterParticipant.with_json_and_owner(jsondict['participant'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'priority' in jsondict:
            self.priority = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['priority'], self)
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'serviceProvider' in jsondict:
            self.serviceProvider = fhirreference.FHIRReference.with_json_and_owner(jsondict['serviceProvider'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'statusHistory' in jsondict:
            self.statusHistory = EncounterStatusHistory.with_json_and_owner(jsondict['statusHistory'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class EncounterHospitalization(fhirelement.FHIRElement):
    """ Details about an admission to a clinic.
    """
    
    resource_name = "EncounterHospitalization"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.admitSource = None
        """ From where patient was admitted (physician referral, transfer).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.destination = None
        """ Location to which the patient is discharged.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.dietPreference = None
        """ Diet preferences reported by the patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dischargeDiagnosis = None
        """ The final diagnosis given a patient before release from the
        hospital after all testing, surgery, and workup are complete.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.dischargeDisposition = None
        """ Category or kind of location after discharge.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.origin = None
        """ The location from which the patient came before admission.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.preAdmissionIdentifier = None
        """ Pre-admission identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.reAdmission = False
        """ Is this hospitalization a readmission?.
        Type `bool`. """
        
        self.specialArrangement = None
        """ Wheelchair, translator, stretcher, etc.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialCourtesy = None
        """ Special courtesies (VIP, board member).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EncounterHospitalization, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EncounterHospitalization, self).update_with_json(jsondict)
        if 'admitSource' in jsondict:
            self.admitSource = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['admitSource'], self)
        if 'destination' in jsondict:
            self.destination = fhirreference.FHIRReference.with_json_and_owner(jsondict['destination'], self)
        if 'dietPreference' in jsondict:
            self.dietPreference = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['dietPreference'], self)
        if 'dischargeDiagnosis' in jsondict:
            self.dischargeDiagnosis = fhirreference.FHIRReference.with_json_and_owner(jsondict['dischargeDiagnosis'], self)
        if 'dischargeDisposition' in jsondict:
            self.dischargeDisposition = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['dischargeDisposition'], self)
        if 'origin' in jsondict:
            self.origin = fhirreference.FHIRReference.with_json_and_owner(jsondict['origin'], self)
        if 'preAdmissionIdentifier' in jsondict:
            self.preAdmissionIdentifier = identifier.Identifier.with_json_and_owner(jsondict['preAdmissionIdentifier'], self)
        if 'reAdmission' in jsondict:
            self.reAdmission = jsondict['reAdmission']
        if 'specialArrangement' in jsondict:
            self.specialArrangement = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['specialArrangement'], self)
        if 'specialCourtesy' in jsondict:
            self.specialCourtesy = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['specialCourtesy'], self)


class EncounterLocation(fhirelement.FHIRElement):
    """ List of locations the patient has been at.
    
    List of locations at which the patient has been.
    """
    
    resource_name = "EncounterLocation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.location = None
        """ Location the encounter takes place.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period during which the patient was present at the location.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | present | reserved.
        Type `str`. """
        
        super(EncounterLocation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EncounterLocation, self).update_with_json(jsondict)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']


class EncounterParticipant(fhirelement.FHIRElement):
    """ List of participants involved in the encounter.
    
    The main practitioner responsible for providing the service.
    """
    
    resource_name = "EncounterParticipant"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.individual = None
        """ Persons involved in the encounter other than the patient.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period of time during the encounter participant was present.
        Type `Period` (represented as `dict` in JSON). """
        
        self.type = None
        """ Role of participant in encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EncounterParticipant, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EncounterParticipant, self).update_with_json(jsondict)
        if 'individual' in jsondict:
            self.individual = fhirreference.FHIRReference.with_json_and_owner(jsondict['individual'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class EncounterStatusHistory(fhirelement.FHIRElement):
    """ List of Encounter statuses.
    
    The current status is always found in the current version of the resource.
    This status history permits the encounter resource to contain the status
    history without the needing to read through the historical versions of the
    resource, or even have the server store them.
    """
    
    resource_name = "EncounterStatusHistory"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.period = None
        """ The time that the episode was in the specified status.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | arrived | in-progress | onleave | finished | cancelled.
        Type `str`. """
        
        super(EncounterStatusHistory, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EncounterStatusHistory, self).update_with_json(jsondict)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']

