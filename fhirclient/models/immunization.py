# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Immunization).
# 2024, SMART Health IT.


from . import domainresource

class Immunization(domainresource.DomainResource):
    """ Immunization event information.
    
    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """
    
    resource_type = "Immunization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.doseQuantity = None
        """ Amount of vaccine administered.
        Type `Quantity` (represented as `dict` in JSON). """
        self._doseQuantity = None
        """ Primitive extension for doseQuantity. Type `FHIRPrimitiveExtension` """
        
        self.education = None
        """ Educational material presented to patient.
        List of `ImmunizationEducation` items (represented as `dict` in JSON). """
        self._education = None
        """ Primitive extension for education. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter immunization was part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.expirationDate = None
        """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._expirationDate = None
        """ Primitive extension for expirationDate. Type `FHIRPrimitiveExtension` """
        
        self.fundingSource = None
        """ Funding source for the vaccine.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._fundingSource = None
        """ Primitive extension for fundingSource. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.isSubpotent = None
        """ Dose potency.
        Type `bool`. """
        self._isSubpotent = None
        """ Primitive extension for isSubpotent. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Where immunization occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.lotNumber = None
        """ Vaccine lot number.
        Type `str`. """
        self._lotNumber = None
        """ Primitive extension for lotNumber. Type `FHIRPrimitiveExtension` """
        
        self.manufacturer = None
        """ Vaccine manufacturer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._manufacturer = None
        """ Primitive extension for manufacturer. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Additional immunization notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceDateTime = None
        """ Vaccine administration date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._occurrenceDateTime = None
        """ Primitive extension for occurrenceDateTime. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceString = None
        """ Vaccine administration date.
        Type `str`. """
        self._occurrenceString = None
        """ Primitive extension for occurrenceString. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Who was immunized.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Who performed event.
        List of `ImmunizationPerformer` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.primarySource = None
        """ Indicates context the data was recorded in.
        Type `bool`. """
        self._primarySource = None
        """ Primitive extension for primarySource. Type `FHIRPrimitiveExtension` """
        
        self.programEligibility = None
        """ Patient eligibility for a vaccination program.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._programEligibility = None
        """ Primitive extension for programEligibility. Type `FHIRPrimitiveExtension` """
        
        self.protocolApplied = None
        """ Protocol followed by the provider.
        List of `ImmunizationProtocolApplied` items (represented as `dict` in JSON). """
        self._protocolApplied = None
        """ Primitive extension for protocolApplied. Type `FHIRPrimitiveExtension` """
        
        self.reaction = None
        """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
        self._reaction = None
        """ Primitive extension for reaction. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why immunization occurred.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.recorded = None
        """ When the immunization was first captured in the subject's record.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._recorded = None
        """ Primitive extension for recorded. Type `FHIRPrimitiveExtension` """
        
        self.reportOrigin = None
        """ Indicates the source of a secondarily reported record.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._reportOrigin = None
        """ Primitive extension for reportOrigin. Type `FHIRPrimitiveExtension` """
        
        self.route = None
        """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._route = None
        """ Primitive extension for route. Type `FHIRPrimitiveExtension` """
        
        self.site = None
        """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._site = None
        """ Primitive extension for site. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ completed | entered-in-error | not-done.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ Reason not done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        self.subpotentReason = None
        """ Reason for being subpotent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._subpotentReason = None
        """ Primitive extension for subpotentReason. Type `FHIRPrimitiveExtension` """
        
        self.vaccineCode = None
        """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._vaccineCode = None
        """ Primitive extension for vaccineCode. Type `FHIRPrimitiveExtension` """
        
        super(Immunization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, None, False),
            ("_doseQuantity", "_doseQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("education", "education", ImmunizationEducation, True, None, False),
            ("_education", "_education", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("_expirationDate", "_expirationDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fundingSource", "fundingSource", codeableconcept.CodeableConcept, False, None, False),
            ("_fundingSource", "_fundingSource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("isSubpotent", "isSubpotent", bool, False, None, False),
            ("_isSubpotent", "_isSubpotent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("_lotNumber", "_lotNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("_manufacturer", "_manufacturer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", True),
            ("_occurrenceDateTime", "_occurrenceDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceString", "occurrenceString", str, False, "occurrence", True),
            ("_occurrenceString", "_occurrenceString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", ImmunizationPerformer, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("primarySource", "primarySource", bool, False, None, False),
            ("_primarySource", "_primarySource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("programEligibility", "programEligibility", codeableconcept.CodeableConcept, True, None, False),
            ("_programEligibility", "_programEligibility", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("protocolApplied", "protocolApplied", ImmunizationProtocolApplied, True, None, False),
            ("_protocolApplied", "_protocolApplied", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reaction", "reaction", ImmunizationReaction, True, None, False),
            ("_reaction", "_reaction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recorded", "recorded", fhirdatetime.FHIRDateTime, False, None, False),
            ("_recorded", "_recorded", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reportOrigin", "reportOrigin", codeableconcept.CodeableConcept, False, None, False),
            ("_reportOrigin", "_reportOrigin", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("_route", "_route", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("_site", "_site", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subpotentReason", "subpotentReason", codeableconcept.CodeableConcept, True, None, False),
            ("_subpotentReason", "_subpotentReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False, None, True),
            ("_vaccineCode", "_vaccineCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ImmunizationEducation(backboneelement.BackboneElement):
    """ Educational material presented to patient.
    
    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """
    
    resource_type = "ImmunizationEducation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentType = None
        """ Educational material document identifier.
        Type `str`. """
        self._documentType = None
        """ Primitive extension for documentType. Type `FHIRPrimitiveExtension` """
        
        self.presentationDate = None
        """ Educational material presentation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._presentationDate = None
        """ Primitive extension for presentationDate. Type `FHIRPrimitiveExtension` """
        
        self.publicationDate = None
        """ Educational material publication date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._publicationDate = None
        """ Primitive extension for publicationDate. Type `FHIRPrimitiveExtension` """
        
        self.reference = None
        """ Educational material reference pointer.
        Type `str`. """
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        super(ImmunizationEducation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationEducation, self).elementProperties()
        js.extend([
            ("documentType", "documentType", str, False, None, False),
            ("_documentType", "_documentType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("presentationDate", "presentationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_presentationDate", "_presentationDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publicationDate", "publicationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_publicationDate", "_publicationDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImmunizationPerformer(backboneelement.BackboneElement):
    """ Who performed event.
    
    Indicates who performed the immunization event.
    """
    
    resource_type = "ImmunizationPerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Individual or organization who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.function = None
        """ What type of performance was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._function = None
        """ Primitive extension for function. Type `FHIRPrimitiveExtension` """
        
        super(ImmunizationPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("_function", "_function", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    """ Protocol followed by the provider.
    
    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """
    
    resource_type = "ImmunizationProtocolApplied"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ Who is responsible for publishing the recommendations.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._authority = None
        """ Primitive extension for authority. Type `FHIRPrimitiveExtension` """
        
        self.doseNumberPositiveInt = None
        """ Dose number within series.
        Type `int`. """
        self._doseNumberPositiveInt = None
        """ Primitive extension for doseNumberPositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.doseNumberString = None
        """ Dose number within series.
        Type `str`. """
        self._doseNumberString = None
        """ Primitive extension for doseNumberString. Type `FHIRPrimitiveExtension` """
        
        self.series = None
        """ Name of vaccine series.
        Type `str`. """
        self._series = None
        """ Primitive extension for series. Type `FHIRPrimitiveExtension` """
        
        self.seriesDosesPositiveInt = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        self._seriesDosesPositiveInt = None
        """ Primitive extension for seriesDosesPositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.seriesDosesString = None
        """ Recommended number of doses for immunity.
        Type `str`. """
        self._seriesDosesString = None
        """ Primitive extension for seriesDosesString. Type `FHIRPrimitiveExtension` """
        
        self.targetDisease = None
        """ Vaccine preventatable disease being targetted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._targetDisease = None
        """ Primitive extension for targetDisease. Type `FHIRPrimitiveExtension` """
        
        super(ImmunizationProtocolApplied, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationProtocolApplied, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("_authority", "_authority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", True),
            ("_doseNumberPositiveInt", "_doseNumberPositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", True),
            ("_doseNumberString", "_doseNumberString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("series", "series", str, False, None, False),
            ("_series", "_series", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("_seriesDosesPositiveInt", "_seriesDosesPositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("_seriesDosesString", "_seriesDosesString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, True, None, False),
            ("_targetDisease", "_targetDisease", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.
    
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    
    resource_type = "ImmunizationReaction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When reaction started.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Additional information on reaction.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.reported = None
        """ Indicates self-reported reaction.
        Type `bool`. """
        self._reported = None
        """ Primitive extension for reported. Type `FHIRPrimitiveExtension` """
        
        super(ImmunizationReaction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, False, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reported", "reported", bool, False, None, False),
            ("_reported", "_reported", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity