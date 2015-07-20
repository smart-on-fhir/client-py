#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Procedure) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period


class Procedure(domainresource.DomainResource):
    """ An action that was or is currently being performed on a patient.
    
    An action that is or was performed on a patient. This can be a physical
    'thing' like an operation, or less invasive like counseling or
    hypnotherapy.
    """
    
    resource_name = "Procedure"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySite = None
        """ Precise location details.
        List of `ProcedureBodySite` items (represented as `dict` in JSON). """
        
        self.category = None
        """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.device = None
        """ Device changed in procedure.
        List of `ProcedureDevice` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ The encounter when procedure performed.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.followUp = None
        """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the procedure happened.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.notes = None
        """ Additional information about procedure.
        Type `str`. """
        
        self.outcome = None
        """ What was result of procedure?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who procedure was performed on.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.performedDateTime = None
        """ Date/Period the procedure was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.performedPeriod = None
        """ Date/Period the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.relatedItem = None
        """ A procedure that is related to this one.
        List of `ProcedureRelatedItem` items (represented as `dict` in JSON). """
        
        self.report = None
        """ Any report that results from the procedure.
        List of `FHIRReference` items referencing `DiagnosticReport` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | aborted | completed | entered-in-error.
        Type `str`. """
        
        self.type = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.used = None
        """ Items used during procedure.
        List of `FHIRReference` items referencing `Device, Medication, Substance` (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", ProcedureBodySite, True),
            ("category", "category", codeableconcept.CodeableConcept, False),
            ("complication", "complication", codeableconcept.CodeableConcept, True),
            ("device", "device", ProcedureDevice, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("followUp", "followUp", codeableconcept.CodeableConcept, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("indication", "indication", codeableconcept.CodeableConcept, True),
            ("location", "location", fhirreference.FHIRReference, False),
            ("notes", "notes", str, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("performedDateTime", "performedDateTime", fhirdate.FHIRDate, False),
            ("performedPeriod", "performedPeriod", period.Period, False),
            ("performer", "performer", ProcedurePerformer, True),
            ("relatedItem", "relatedItem", ProcedureRelatedItem, True),
            ("report", "report", fhirreference.FHIRReference, True),
            ("status", "status", str, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
            ("used", "used", fhirreference.FHIRReference, True),
        ])
        return js


class ProcedureBodySite(fhirelement.FHIRElement):
    """ Precise location details.
    
    Detailed and structured anatomical location information. Multiple locations
    are allowed - e.g. multiple punch biopsies of a lesion.
    """
    
    resource_name = "ProcedureBodySite"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.siteCodeableConcept = None
        """ Precise location details.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Precise location details.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        super(ProcedureBodySite, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProcedureBodySite, self).elementProperties()
        js.extend([
            ("siteCodeableConcept", "siteCodeableConcept", codeableconcept.CodeableConcept, False),
            ("siteReference", "siteReference", fhirreference.FHIRReference, False),
        ])
        return js


class ProcedureDevice(fhirelement.FHIRElement):
    """ Device changed in procedure.
    
    A device change during the procedure.
    """
    
    resource_name = "ProcedureDevice"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manipulated = None
        """ Device that was changed.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        super(ProcedureDevice, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProcedureDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False),
            ("manipulated", "manipulated", fhirreference.FHIRReference, False),
        ])
        return js


class ProcedurePerformer(fhirelement.FHIRElement):
    """ The people who performed the procedure.
    
    Limited to 'real' people rather than equipment.
    """
    
    resource_name = "ProcedurePerformer"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.person = None
        """ The reference to the practitioner.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.role = None
        """ The role the person was in.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProcedurePerformer, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("person", "person", fhirreference.FHIRReference, False),
            ("role", "role", codeableconcept.CodeableConcept, False),
        ])
        return js


class ProcedureRelatedItem(fhirelement.FHIRElement):
    """ A procedure that is related to this one.
    
    Procedures may be related to other items such as procedures or medications.
    For example treating wound dehiscence following a previous procedure.
    """
    
    resource_name = "ProcedureRelatedItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.target = None
        """ The related item - e.g. a procedure.
        Type `FHIRReference` referencing `AllergyIntolerance, CarePlan, Condition, DiagnosticReport, FamilyMemberHistory, ImagingStudy, Immunization, ImmunizationRecommendation, MedicationAdministration, MedicationDispense, MedicationPrescription, MedicationStatement, Observation, Procedure` (represented as `dict` in JSON). """
        
        self.type = None
        """ caused-by | because-of.
        Type `str`. """
        
        super(ProcedureRelatedItem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProcedureRelatedItem, self).elementProperties()
        js.extend([
            ("target", "target", fhirreference.FHIRReference, False),
            ("type", "type", str, False),
        ])
        return js

