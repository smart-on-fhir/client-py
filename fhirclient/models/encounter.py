# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Encounter).
# 2024, SMART Health IT.


from . import domainresource

class Encounter(domainresource.DomainResource):
    """ An interaction during which services are provided to the patient.
    
    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """
    
    resource_type = "Encounter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.account = None
        """ The set of accounts that may be used for billing for this Encounter.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._account = None
        """ Primitive extension for account. Type `FHIRPrimitiveExtension` """
        
        self.appointment = None
        """ The appointment that scheduled this encounter.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._appointment = None
        """ Primitive extension for appointment. Type `FHIRPrimitiveExtension` """
        
        self.basedOn = None
        """ The ServiceRequest that initiated this encounter.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.classHistory = None
        """ List of past encounter classes.
        List of `EncounterClassHistory` items (represented as `dict` in JSON). """
        self._classHistory = None
        """ Primitive extension for classHistory. Type `FHIRPrimitiveExtension` """
        
        self.class_fhir = None
        """ Classification of patient encounter.
        Type `Coding` (represented as `dict` in JSON). """
        self._class_fhir = None
        """ Primitive extension for class_fhir. Type `FHIRPrimitiveExtension` """
        
        self.diagnosis = None
        """ The list of diagnosis relevant to this encounter.
        List of `EncounterDiagnosis` items (represented as `dict` in JSON). """
        self._diagnosis = None
        """ Primitive extension for diagnosis. Type `FHIRPrimitiveExtension` """
        
        self.episodeOfCare = None
        """ Episode(s) of care that this encounter should be recorded against.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._episodeOfCare = None
        """ Primitive extension for episodeOfCare. Type `FHIRPrimitiveExtension` """
        
        self.hospitalization = None
        """ Details about the admission to a healthcare service.
        Type `EncounterHospitalization` (represented as `dict` in JSON). """
        self._hospitalization = None
        """ Primitive extension for hospitalization. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifier(s) by which this encounter is known.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.length = None
        """ Quantity of time the encounter lasted (less time absent).
        Type `Duration` (represented as `dict` in JSON). """
        self._length = None
        """ Primitive extension for length. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ List of locations where the patient has been.
        List of `EncounterLocation` items (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Another Encounter this encounter is part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.participant = None
        """ List of participants involved in the encounter.
        List of `EncounterParticipant` items (represented as `dict` in JSON). """
        self._participant = None
        """ Primitive extension for participant. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ The start and end time of the encounter.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ Indicates the urgency of the encounter.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Coded reason the encounter takes place.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Reason the encounter takes place (reference).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.serviceProvider = None
        """ The organization (facility) responsible for this encounter.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._serviceProvider = None
        """ Primitive extension for serviceProvider. Type `FHIRPrimitiveExtension` """
        
        self.serviceType = None
        """ Specific type of service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._serviceType = None
        """ Primitive extension for serviceType. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ planned | arrived | triaged | in-progress | onleave | finished |
        cancelled +.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusHistory = None
        """ List of past encounter statuses.
        List of `EncounterStatusHistory` items (represented as `dict` in JSON). """
        self._statusHistory = None
        """ Primitive extension for statusHistory. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ The patient or group present at the encounter.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Specific type of encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Encounter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Encounter, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, True, None, False),
            ("_account", "_account", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("appointment", "appointment", fhirreference.FHIRReference, True, None, False),
            ("_appointment", "_appointment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("classHistory", "classHistory", EncounterClassHistory, True, None, False),
            ("_classHistory", "_classHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("class_fhir", "class", coding.Coding, False, None, True),
            ("_class_fhir", "_class_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("diagnosis", "diagnosis", EncounterDiagnosis, True, None, False),
            ("_diagnosis", "_diagnosis", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("episodeOfCare", "episodeOfCare", fhirreference.FHIRReference, True, None, False),
            ("_episodeOfCare", "_episodeOfCare", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("hospitalization", "hospitalization", EncounterHospitalization, False, None, False),
            ("_hospitalization", "_hospitalization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("length", "length", duration.Duration, False, None, False),
            ("_length", "_length", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", EncounterLocation, True, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participant", "participant", EncounterParticipant, True, None, False),
            ("_participant", "_participant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serviceProvider", "serviceProvider", fhirreference.FHIRReference, False, None, False),
            ("_serviceProvider", "_serviceProvider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, False, None, False),
            ("_serviceType", "_serviceType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusHistory", "statusHistory", EncounterStatusHistory, True, None, False),
            ("_statusHistory", "_statusHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class EncounterClassHistory(backboneelement.BackboneElement):
    """ List of past encounter classes.
    
    The class history permits the tracking of the encounters transitions
    without needing to go  through the resource history.  This would be used
    for a case where an admission starts of as an emergency encounter, then
    transitions into an inpatient scenario. Doing this and not restarting a new
    encounter ensures that any lab/diagnostic results can more easily follow
    the patient and not require re-processing and not get lost or cancelled
    during a kind of discharge from emergency to inpatient.
    """
    
    resource_type = "EncounterClassHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.class_fhir = None
        """ inpatient | outpatient | ambulatory | emergency +.
        Type `Coding` (represented as `dict` in JSON). """
        self._class_fhir = None
        """ Primitive extension for class_fhir. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ The time that the episode was in the specified class.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        super(EncounterClassHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EncounterClassHistory, self).elementProperties()
        js.extend([
            ("class_fhir", "class", coding.Coding, False, None, True),
            ("_class_fhir", "_class_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, True),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EncounterDiagnosis(backboneelement.BackboneElement):
    """ The list of diagnosis relevant to this encounter.
    """
    
    resource_type = "EncounterDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.condition = None
        """ The diagnosis or procedure relevant to the encounter.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.rank = None
        """ Ranking of the diagnosis (for each role type).
        Type `int`. """
        self._rank = None
        """ Primitive extension for rank. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ Role that this diagnosis has within the encounter (e.g. admission,
        billing, discharge …).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        super(EncounterDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EncounterDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", fhirreference.FHIRReference, False, None, True),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rank", "rank", int, False, None, False),
            ("_rank", "_rank", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", codeableconcept.CodeableConcept, False, None, False),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EncounterHospitalization(backboneelement.BackboneElement):
    """ Details about the admission to a healthcare service.
    """
    
    resource_type = "EncounterHospitalization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.admitSource = None
        """ From where patient was admitted (physician referral, transfer).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._admitSource = None
        """ Primitive extension for admitSource. Type `FHIRPrimitiveExtension` """
        
        self.destination = None
        """ Location/organization to which the patient is discharged.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._destination = None
        """ Primitive extension for destination. Type `FHIRPrimitiveExtension` """
        
        self.dietPreference = None
        """ Diet preferences reported by the patient.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._dietPreference = None
        """ Primitive extension for dietPreference. Type `FHIRPrimitiveExtension` """
        
        self.dischargeDisposition = None
        """ Category or kind of location after discharge.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._dischargeDisposition = None
        """ Primitive extension for dischargeDisposition. Type `FHIRPrimitiveExtension` """
        
        self.origin = None
        """ The location/organization from which the patient came before
        admission.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._origin = None
        """ Primitive extension for origin. Type `FHIRPrimitiveExtension` """
        
        self.preAdmissionIdentifier = None
        """ Pre-admission identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        self._preAdmissionIdentifier = None
        """ Primitive extension for preAdmissionIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.reAdmission = None
        """ The type of hospital re-admission that has occurred (if any). If
        the value is absent, then this is not identified as a readmission.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._reAdmission = None
        """ Primitive extension for reAdmission. Type `FHIRPrimitiveExtension` """
        
        self.specialArrangement = None
        """ Wheelchair, translator, stretcher, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._specialArrangement = None
        """ Primitive extension for specialArrangement. Type `FHIRPrimitiveExtension` """
        
        self.specialCourtesy = None
        """ Special courtesies (VIP, board member).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._specialCourtesy = None
        """ Primitive extension for specialCourtesy. Type `FHIRPrimitiveExtension` """
        
        super(EncounterHospitalization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EncounterHospitalization, self).elementProperties()
        js.extend([
            ("admitSource", "admitSource", codeableconcept.CodeableConcept, False, None, False),
            ("_admitSource", "_admitSource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("_destination", "_destination", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dietPreference", "dietPreference", codeableconcept.CodeableConcept, True, None, False),
            ("_dietPreference", "_dietPreference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dischargeDisposition", "dischargeDisposition", codeableconcept.CodeableConcept, False, None, False),
            ("_dischargeDisposition", "_dischargeDisposition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("origin", "origin", fhirreference.FHIRReference, False, None, False),
            ("_origin", "_origin", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preAdmissionIdentifier", "preAdmissionIdentifier", identifier.Identifier, False, None, False),
            ("_preAdmissionIdentifier", "_preAdmissionIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reAdmission", "reAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("_reAdmission", "_reAdmission", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialArrangement", "specialArrangement", codeableconcept.CodeableConcept, True, None, False),
            ("_specialArrangement", "_specialArrangement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialCourtesy", "specialCourtesy", codeableconcept.CodeableConcept, True, None, False),
            ("_specialCourtesy", "_specialCourtesy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EncounterLocation(backboneelement.BackboneElement):
    """ List of locations where the patient has been.
    
    List of locations where  the patient has been during this encounter.
    """
    
    resource_type = "EncounterLocation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.location = None
        """ Location the encounter takes place.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Time period during which the patient was present at the location.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.physicalType = None
        """ The physical type of the location (usually the level in the
        location hierachy - bed room ward etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._physicalType = None
        """ Primitive extension for physicalType. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ planned | active | reserved | completed.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(EncounterLocation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EncounterLocation, self).elementProperties()
        js.extend([
            ("location", "location", fhirreference.FHIRReference, False, None, True),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False, None, False),
            ("_physicalType", "_physicalType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EncounterParticipant(backboneelement.BackboneElement):
    """ List of participants involved in the encounter.
    
    The list of people responsible for providing the service.
    """
    
    resource_type = "EncounterParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.individual = None
        """ Persons involved in the encounter other than the patient.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._individual = None
        """ Primitive extension for individual. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Period of time during the encounter that the participant
        participated.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Role of participant in encounter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(EncounterParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EncounterParticipant, self).elementProperties()
        js.extend([
            ("individual", "individual", fhirreference.FHIRReference, False, None, False),
            ("_individual", "_individual", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EncounterStatusHistory(backboneelement.BackboneElement):
    """ List of past encounter statuses.
    
    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """
    
    resource_type = "EncounterStatusHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ The time that the episode was in the specified status.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ planned | arrived | triaged | in-progress | onleave | finished |
        cancelled +.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(EncounterStatusHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EncounterStatusHistory, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, True),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import duration
from . import fhirreference
from . import identifier
from . import period