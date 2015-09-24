#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Encounter) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity


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
        
        self.appointment = None
        """ The appointment that scheduled this encounter.
        Type `FHIRReference` referencing `Appointment` (represented as `dict` in JSON). """
        
        self.class_fhir = None
        """ inpatient | outpatient | ambulatory | emergency +.
        Type `str`. """
        
        self.episodeOfCare = None
        """ Episode(s) of care that this encounter should be recorded against.
        List of `FHIRReference` items referencing `EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.hospitalization = None
        """ Details about the admission to a healthcare service.
        Type `EncounterHospitalization` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier(s) by which this encounter is known.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.incomingReferral = None
        """ The ReferralRequest that initiated this encounter.
        List of `FHIRReference` items referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason the encounter takes place (resource).
        List of `FHIRReference` items referencing `Condition, Procedure` (represented as `dict` in JSON). """
        
        self.length = None
        """ Quantity of time the encounter lasted (less time absent).
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """
        
        self.location = None
        """ List of locations where the patient has been.
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
        """ List of past encounter statuses.
        List of `EncounterStatusHistory` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Specific type of encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Encounter, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Encounter, self).elementProperties()
        js.extend([
            ("appointment", "appointment", fhirreference.FHIRReference, False),
            ("class_fhir", "class", str, False),
            ("episodeOfCare", "episodeOfCare", fhirreference.FHIRReference, True),
            ("hospitalization", "hospitalization", EncounterHospitalization, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("incomingReferral", "incomingReferral", fhirreference.FHIRReference, True),
            ("indication", "indication", fhirreference.FHIRReference, True),
            ("length", "length", quantity.Quantity, False),
            ("location", "location", EncounterLocation, True),
            ("partOf", "partOf", fhirreference.FHIRReference, False),
            ("participant", "participant", EncounterParticipant, True),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True),
            ("serviceProvider", "serviceProvider", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
            ("statusHistory", "statusHistory", EncounterStatusHistory, True),
            ("type", "type", codeableconcept.CodeableConcept, True),
        ])
        return js


class EncounterHospitalization(fhirelement.FHIRElement):
    """ Details about the admission to a healthcare service.
    """
    
    resource_name = "EncounterHospitalization"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.admitSource = None
        """ From where patient was admitted (physician referral, transfer).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.admittingDiagnosis = None
        """ The admitting diagnosis as reported by admitting practitioner.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.destination = None
        """ Location to which the patient is discharged.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.dietPreference = None
        """ Diet preferences reported by the patient.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dischargeDiagnosis = None
        """ The final diagnosis given a patient before release from the
        hospital after all testing, surgery, and workup are complete.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.dischargeDisposition = None
        """ Category or kind of location after discharge.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.origin = None
        """ The location from which the patient came before admission.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.preAdmissionIdentifier = None
        """ Pre-admission identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.reAdmission = None
        """ The type of hospital re-admission that has occurred (if any). If
        the value is absent, then this is not identified as a readmission.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specialArrangement = None
        """ Wheelchair, translator, stretcher, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialCourtesy = None
        """ Special courtesies (VIP, board member).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EncounterHospitalization, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(EncounterHospitalization, self).elementProperties()
        js.extend([
            ("admitSource", "admitSource", codeableconcept.CodeableConcept, False),
            ("admittingDiagnosis", "admittingDiagnosis", fhirreference.FHIRReference, True),
            ("destination", "destination", fhirreference.FHIRReference, False),
            ("dietPreference", "dietPreference", codeableconcept.CodeableConcept, True),
            ("dischargeDiagnosis", "dischargeDiagnosis", fhirreference.FHIRReference, True),
            ("dischargeDisposition", "dischargeDisposition", codeableconcept.CodeableConcept, False),
            ("origin", "origin", fhirreference.FHIRReference, False),
            ("preAdmissionIdentifier", "preAdmissionIdentifier", identifier.Identifier, False),
            ("reAdmission", "reAdmission", codeableconcept.CodeableConcept, False),
            ("specialArrangement", "specialArrangement", codeableconcept.CodeableConcept, True),
            ("specialCourtesy", "specialCourtesy", codeableconcept.CodeableConcept, True),
        ])
        return js


class EncounterLocation(fhirelement.FHIRElement):
    """ List of locations where the patient has been.
    
    List of locations where  the patient has been during this encounter.
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
        """ planned | active | reserved | completed.
        Type `str`. """
        
        super(EncounterLocation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(EncounterLocation, self).elementProperties()
        js.extend([
            ("location", "location", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("status", "status", str, False),
        ])
        return js


class EncounterParticipant(fhirelement.FHIRElement):
    """ List of participants involved in the encounter.
    
    The list of people responsible for providing the service.
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
    
    def elementProperties(self):
        js = super(EncounterParticipant, self).elementProperties()
        js.extend([
            ("individual", "individual", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("type", "type", codeableconcept.CodeableConcept, True),
        ])
        return js


class EncounterStatusHistory(fhirelement.FHIRElement):
    """ List of past encounter statuses.
    
    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
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
    
    def elementProperties(self):
        js = super(EncounterStatusHistory, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False),
            ("status", "status", str, False),
        ])
        return js

