#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Procedure) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.
    
    An action that is or was performed on a patient. This can be a physical
    intervention like an operation, or less invasive like counseling or
    hypnotherapy.
    """
    
    resource_type = "Procedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ A request for this procedure.
        List of `FHIRReference` items referencing `CarePlan, ProcedureRequest, ReferralRequest` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.complicationDetail = None
        """ A condition that is a result of the procedure.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or episode associated with the procedure.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.definition = None
        """ Instantiates protocol or definition.
        List of `FHIRReference` items referencing `PlanDefinition, ActivityDefinition, HealthcareService` (represented as `dict` in JSON). """
        
        self.focalDevice = None
        """ Device changed in procedure.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """
        
        self.followUp = None
        """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the procedure happened.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.notDone = None
        """ True if procedure was not performed as scheduled.
        Type `bool`. """
        
        self.notDoneReason = None
        """ Reason procedure was not performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items referencing `Procedure, Observation, MedicationAdministration` (represented as `dict` in JSON). """
        
        self.performedDateTime = None
        """ Date/Period the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.performedPeriod = None
        """ Date/Period the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Coded reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Condition that is the reason the procedure performed.
        List of `FHIRReference` items referencing `Condition, Observation` (represented as `dict` in JSON). """
        
        self.report = None
        """ Any report resulting from the procedure.
        List of `FHIRReference` items referencing `DiagnosticReport` (represented as `dict` in JSON). """
        
        self.status = None
        """ preparation | in-progress | suspended | aborted | completed |
        entered-in-error | unknown.
        Type `str`. """
        
        self.subject = None
        """ Who the procedure was performed on.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        self.usedCode = None
        """ Coded items used during the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.usedReference = None
        """ Items used during procedure.
        List of `FHIRReference` items referencing `Device, Medication, Substance` (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("complication", "complication", codeableconcept.CodeableConcept, True, None, False),
            ("complicationDetail", "complicationDetail", fhirreference.FHIRReference, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", fhirreference.FHIRReference, True, None, False),
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True, None, False),
            ("followUp", "followUp", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("notDone", "notDone", bool, False, None, False),
            ("notDoneReason", "notDoneReason", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performedDateTime", "performedDateTime", fhirdate.FHIRDate, False, "performed", False),
            ("performedPeriod", "performedPeriod", period.Period, False, "performed", False),
            ("performer", "performer", ProcedurePerformer, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("report", "report", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("usedCode", "usedCode", codeableconcept.CodeableConcept, True, None, False),
            ("usedReference", "usedReference", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Device changed in procedure.
    
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
        
        self.manipulated = None
        """ Device that was changed.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        super(ProcedureFocalDevice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, False),
            ("manipulated", "manipulated", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.
    
    Limited to 'real' people rather than equipment.
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
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson, Device` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ Organization the device or practitioner was acting for.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.role = None
        """ The role the actor was in.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProcedurePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
