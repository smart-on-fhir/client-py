# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Procedure).
# 2024, SMART Health IT.


from . import domainresource

class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.
    
    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """
    
    resource_type = "Procedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asserter = None
        """ Person who asserts this procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._asserter = None
        """ Primitive extension for asserter. Type `FHIRPrimitiveExtension` """
        
        self.basedOn = None
        """ A request for this procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.bodySite = None
        """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._complication = None
        """ Primitive extension for complication. Type `FHIRPrimitiveExtension` """
        
        self.complicationDetail = None
        """ A condition that is a result of the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._complicationDetail = None
        """ Primitive extension for complicationDetail. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.focalDevice = None
        """ Manipulated, implanted, or removed device.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """
        self._focalDevice = None
        """ Primitive extension for focalDevice. Type `FHIRPrimitiveExtension` """
        
        self.followUp = None
        """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._followUp = None
        """ Primitive extension for followUp. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        self._instantiatesCanonical = None
        """ Primitive extension for instantiatesCanonical. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        self._instantiatesUri = None
        """ Primitive extension for instantiatesUri. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Where the procedure happened.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.performedAge = None
        """ When the procedure was performed.
        Type `Age` (represented as `dict` in JSON). """
        self._performedAge = None
        """ Primitive extension for performedAge. Type `FHIRPrimitiveExtension` """
        
        self.performedDateTime = None
        """ When the procedure was performed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._performedDateTime = None
        """ Primitive extension for performedDateTime. Type `FHIRPrimitiveExtension` """
        
        self.performedPeriod = None
        """ When the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
        self._performedPeriod = None
        """ Primitive extension for performedPeriod. Type `FHIRPrimitiveExtension` """
        
        self.performedRange = None
        """ When the procedure was performed.
        Type `Range` (represented as `dict` in JSON). """
        self._performedRange = None
        """ Primitive extension for performedRange. Type `FHIRPrimitiveExtension` """
        
        self.performedString = None
        """ When the procedure was performed.
        Type `str`. """
        self._performedString = None
        """ Primitive extension for performedString. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Coded reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ The justification that the procedure was performed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.recorder = None
        """ Who recorded the procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._recorder = None
        """ Primitive extension for recorder. Type `FHIRPrimitiveExtension` """
        
        self.report = None
        """ Any report resulting from the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._report = None
        """ Primitive extension for report. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who the procedure was performed on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.usedCode = None
        """ Coded items used during the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._usedCode = None
        """ Primitive extension for usedCode. Type `FHIRPrimitiveExtension` """
        
        self.usedReference = None
        """ Items used during procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._usedReference = None
        """ Primitive extension for usedReference. Type `FHIRPrimitiveExtension` """
        
        super(Procedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("_asserter", "_asserter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("complication", "complication", codeableconcept.CodeableConcept, True, None, False),
            ("_complication", "_complication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("complicationDetail", "complicationDetail", fhirreference.FHIRReference, True, None, False),
            ("_complicationDetail", "_complicationDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True, None, False),
            ("_focalDevice", "_focalDevice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("followUp", "followUp", codeableconcept.CodeableConcept, True, None, False),
            ("_followUp", "_followUp", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performedAge", "performedAge", age.Age, False, "performed", False),
            ("_performedAge", "_performedAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performedDateTime", "performedDateTime", fhirdatetime.FHIRDateTime, False, "performed", False),
            ("_performedDateTime", "_performedDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performedPeriod", "performedPeriod", period.Period, False, "performed", False),
            ("_performedPeriod", "_performedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performedRange", "performedRange", range.Range, False, "performed", False),
            ("_performedRange", "_performedRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performedString", "performedString", str, False, "performed", False),
            ("_performedString", "_performedString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", ProcedurePerformer, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("_recorder", "_recorder", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("report", "report", fhirreference.FHIRReference, True, None, False),
            ("_report", "_report", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usedCode", "usedCode", codeableconcept.CodeableConcept, True, None, False),
            ("_usedCode", "_usedCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usedReference", "usedReference", fhirreference.FHIRReference, True, None, False),
            ("_usedReference", "_usedReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Manipulated, implanted, or removed device.
    
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """
    
    resource_type = "ProcedureFocalDevice"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        self.manipulated = None
        """ Device that was changed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._manipulated = None
        """ Primitive extension for manipulated. Type `FHIRPrimitiveExtension` """
        
        super(ProcedureFocalDevice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, False),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manipulated", "manipulated", fhirreference.FHIRReference, False, None, True),
            ("_manipulated", "_manipulated", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.
    
    Limited to "real" people rather than equipment.
    """
    
    resource_type = "ProcedurePerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ The reference to the practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._function = None
        """ Primitive extension for function. Type `FHIRPrimitiveExtension` """
        
        self.onBehalfOf = None
        """ Organization the device or practitioner was acting for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._onBehalfOf = None
        """ Primitive extension for onBehalfOf. Type `FHIRPrimitiveExtension` """
        
        super(ProcedurePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("_function", "_function", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("_onBehalfOf", "_onBehalfOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import age
from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import range