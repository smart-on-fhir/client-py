#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Procedure) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period


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
    
    def update_with_json(self, jsondict):
        super(Procedure, self).update_with_json(jsondict)
        if 'bodySite' in jsondict:
            self.bodySite = ProcedureBodySite.with_json_and_owner(jsondict['bodySite'], self)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'complication' in jsondict:
            self.complication = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['complication'], self)
        if 'device' in jsondict:
            self.device = ProcedureDevice.with_json_and_owner(jsondict['device'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'followUp' in jsondict:
            self.followUp = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['followUp'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'indication' in jsondict:
            self.indication = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['indication'], self)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'outcome' in jsondict:
            self.outcome = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['outcome'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'performedDateTime' in jsondict:
            self.performedDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['performedDateTime'], self)
        if 'performedPeriod' in jsondict:
            self.performedPeriod = period.Period.with_json_and_owner(jsondict['performedPeriod'], self)
        if 'performer' in jsondict:
            self.performer = ProcedurePerformer.with_json_and_owner(jsondict['performer'], self)
        if 'relatedItem' in jsondict:
            self.relatedItem = ProcedureRelatedItem.with_json_and_owner(jsondict['relatedItem'], self)
        if 'report' in jsondict:
            self.report = fhirreference.FHIRReference.with_json_and_owner(jsondict['report'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'used' in jsondict:
            self.used = fhirreference.FHIRReference.with_json_and_owner(jsondict['used'], self)


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
    
    def update_with_json(self, jsondict):
        super(ProcedureBodySite, self).update_with_json(jsondict)
        if 'siteCodeableConcept' in jsondict:
            self.siteCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['siteCodeableConcept'], self)
        if 'siteReference' in jsondict:
            self.siteReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['siteReference'], self)


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
    
    def update_with_json(self, jsondict):
        super(ProcedureDevice, self).update_with_json(jsondict)
        if 'action' in jsondict:
            self.action = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['action'], self)
        if 'manipulated' in jsondict:
            self.manipulated = fhirreference.FHIRReference.with_json_and_owner(jsondict['manipulated'], self)


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
    
    def update_with_json(self, jsondict):
        super(ProcedurePerformer, self).update_with_json(jsondict)
        if 'person' in jsondict:
            self.person = fhirreference.FHIRReference.with_json_and_owner(jsondict['person'], self)
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['role'], self)


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
    
    def update_with_json(self, jsondict):
        super(ProcedureRelatedItem, self).update_with_json(jsondict)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']

