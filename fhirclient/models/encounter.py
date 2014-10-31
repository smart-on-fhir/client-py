#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (encounter.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import duration
import fhirelement
import fhirreference
import fhirresource
import identifier
import location
import narrative
import organization
import patient
import period
import practitioner


class Encounter(fhirresource.FHIRResource):
    """ An interaction during which services are provided to the patient.
    
    Scope and Usage A patient encounter is further characterized by the setting
    in which it takes place. Amongst them are ambulatory, emergency, home
    health, inpatient and virtual encounters. An Encounter encompasses the
    lifecycle from pre-admission, the actual encounter (for ambulatory
    encounters), and admission, stay and discharge (for inpatient encounters).
    During the encounter the patient may move from practitioner to practitioner
    and location to location.
    
    Because of the broad scope of Encounter, not all elements will be relevant
    in all settings. For this reason, admission/discharge related information
    is kept in a separate Hospitalization component within Encounter. The class
    element is used to distinguish between these settings, which will guide
    further validation and application of business rules.
    
    There is also substantial variance from organization to organization (and
    between jurisdictions and countries) on which business events translate to
    the start of a new Encounter, or what level of aggregation is used for
    Encounter. For example, each single visit of a practitioner during a
    hospitalization may lead to a new instance of Encounter, but depending on
    local practice and the systems involved, it may well be that this is
    aggregated to a single instance for a whole hospitalization. Even more
    aggregation may occur where jurisdictions introduce groups of Encounters
    for financial or other reasons. Encounters can be aggregated or grouped
    under other Encounters using the partOf element. See below for examples.
    
    Encounter instances may exist before the actual encounter takes place to
    convey pre-admission information, including using Encounters elements to
    reflect the planned start date, planned accommodation or planned encounter
    locations. In this case the status element is set to 'planned'.
    """
    
    resource_name = "Encounter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.hospitalization = None
        """ Details about an admission to a clinic.
        Type `EncounterHospitalization` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier(s) by which this encounter is known.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason the encounter takes place (resource).
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.klass = None
        """ inpatient | outpatient | ambulatory | emergency +.
        Type `str`. """
        
        self.length = None
        """ Quantity of time the encounter lasted.
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
        
        self.period = None
        """ The start and end time of the encounter.
        Type `Period` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Indicates the urgency of the encounter.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Reason the encounter takes place (code).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.serviceProvider = None
        """ Department or team providing care.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | in progress | onleave | finished | cancelled.
        Type `str`. """
        
        self.subject = None
        """ The patient present at the encounter.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.type = None
        """ Specific type of encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Encounter, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Encounter, self).update_with_json(jsondict)
        if 'hospitalization' in jsondict:
            self.hospitalization = EncounterHospitalization.with_json(jsondict['hospitalization'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'indication' in jsondict:
            self.indication = fhirreference.FHIRReference.with_json_and_owner(jsondict['indication'], self, fhirresource.FHIRResource)
        if 'klass' in jsondict:
            self.klass = jsondict['klass']
        if 'length' in jsondict:
            self.length = duration.Duration.with_json(jsondict['length'])
        if 'location' in jsondict:
            self.location = EncounterLocation.with_json(jsondict['location'])
        if 'partOf' in jsondict:
            self.partOf = fhirreference.FHIRReference.with_json_and_owner(jsondict['partOf'], self, Encounter)
        if 'participant' in jsondict:
            self.participant = EncounterParticipant.with_json(jsondict['participant'])
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])
        if 'priority' in jsondict:
            self.priority = codeableconcept.CodeableConcept.with_json(jsondict['priority'])
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json(jsondict['reason'])
        if 'serviceProvider' in jsondict:
            self.serviceProvider = fhirreference.FHIRReference.with_json_and_owner(jsondict['serviceProvider'], self, organization.Organization)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])


class EncounterParticipant(fhirelement.FHIRElement):
    """ List of participants involved in the encounter.
    
    The main practitioner responsible for providing the service.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.individual = None
        """ Persons involved in the encounter other than the patient.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.type = None
        """ Role of participant in encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EncounterParticipant, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EncounterParticipant, self).update_with_json(jsondict)
        if 'individual' in jsondict:
            self.individual = fhirreference.FHIRReference.with_json_and_owner(jsondict['individual'], self, practitioner.Practitioner)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])


class EncounterHospitalization(fhirelement.FHIRElement):
    """ Details about an admission to a clinic.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.accomodation = None
        """ Where the patient stays during this encounter.
        List of `EncounterHospitalizationAccomodation` items (represented as `dict` in JSON). """
        
        self.admitSource = None
        """ From where patient was admitted (physician referral, transfer).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.destination = None
        """ Location to which the patient is discharged.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.diet = None
        """ Dietary restrictions for the patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dischargeDiagnosis = None
        """ The final diagnosis given a patient before release from the
        hospital after all testing, surgery, and workup are complete.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.dischargeDisposition = None
        """ Category or kind of location after discharge.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.origin = None
        """ The location from which the patient came before admission.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period during which the patient was admitted.
        Type `Period` (represented as `dict` in JSON). """
        
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
        if 'accomodation' in jsondict:
            self.accomodation = EncounterHospitalizationAccomodation.with_json(jsondict['accomodation'])
        if 'admitSource' in jsondict:
            self.admitSource = codeableconcept.CodeableConcept.with_json(jsondict['admitSource'])
        if 'destination' in jsondict:
            self.destination = fhirreference.FHIRReference.with_json_and_owner(jsondict['destination'], self, location.Location)
        if 'diet' in jsondict:
            self.diet = codeableconcept.CodeableConcept.with_json(jsondict['diet'])
        if 'dischargeDiagnosis' in jsondict:
            self.dischargeDiagnosis = fhirreference.FHIRReference.with_json_and_owner(jsondict['dischargeDiagnosis'], self, fhirresource.FHIRResource)
        if 'dischargeDisposition' in jsondict:
            self.dischargeDisposition = codeableconcept.CodeableConcept.with_json(jsondict['dischargeDisposition'])
        if 'origin' in jsondict:
            self.origin = fhirreference.FHIRReference.with_json_and_owner(jsondict['origin'], self, location.Location)
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])
        if 'preAdmissionIdentifier' in jsondict:
            self.preAdmissionIdentifier = identifier.Identifier.with_json(jsondict['preAdmissionIdentifier'])
        if 'reAdmission' in jsondict:
            self.reAdmission = jsondict['reAdmission']
        if 'specialArrangement' in jsondict:
            self.specialArrangement = codeableconcept.CodeableConcept.with_json(jsondict['specialArrangement'])
        if 'specialCourtesy' in jsondict:
            self.specialCourtesy = codeableconcept.CodeableConcept.with_json(jsondict['specialCourtesy'])


class EncounterHospitalizationAccomodation(fhirelement.FHIRElement):
    """ Where the patient stays during this encounter.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bed = None
        """ The bed that is assigned to the patient.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period during which the patient was assigned the bed.
        Type `Period` (represented as `dict` in JSON). """
        
        super(EncounterHospitalizationAccomodation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EncounterHospitalizationAccomodation, self).update_with_json(jsondict)
        if 'bed' in jsondict:
            self.bed = fhirreference.FHIRReference.with_json_and_owner(jsondict['bed'], self, location.Location)
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])


class EncounterLocation(fhirelement.FHIRElement):
    """ List of locations the patient has been at.
    
    List of locations at which the patient has been.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.location = None
        """ Location the encounter takes place.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period during which the patient was present at the location.
        Type `Period` (represented as `dict` in JSON). """
        
        super(EncounterLocation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EncounterLocation, self).update_with_json(jsondict)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self, location.Location)
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])

