#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (procedure.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirelement
import fhirreference
import fhirresource
import identifier
import period


class Procedure(fhirresource.FHIRResource):
    """ An action that is performed on a patient.
    
    An action that is performed on a patient. This can be a physical 'thing'
    like an operation, or less invasive like counseling or hypnotherapy.
    """
    
    resource_name = "Procedure"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySite = None
        """ Precise location details.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.date = None
        """ The date the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ The encounter when procedure performed.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.followUp = None
        """ Instructions for follow up.
        Type `str`. """
        
        self.identifier = None
        """ External Ids for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Additional information about procedure.
        Type `str`. """
        
        self.outcome = None
        """ What was result of procedure?.
        Type `str`. """
        
        self.patient = None
        """ Who procedure was performed on.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.relatedItem = None
        """ A procedure that is related to this one.
        List of `ProcedureRelatedItem` items (represented as `dict` in JSON). """
        
        self.report = None
        """ Any report that results from the procedure.
        List of `FHIRReference` items referencing `DiagnosticReport` (represented as `dict` in JSON). """
        
        self.type = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Procedure, self).update_with_json(jsondict)
        if 'bodySite' in jsondict:
            self.bodySite = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['bodySite'], self)
        if 'complication' in jsondict:
            self.complication = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['complication'], self)
        if 'date' in jsondict:
            self.date = period.Period.with_json_and_owner(jsondict['date'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'followUp' in jsondict:
            self.followUp = jsondict['followUp']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'indication' in jsondict:
            self.indication = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['indication'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'outcome' in jsondict:
            self.outcome = jsondict['outcome']
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'performer' in jsondict:
            self.performer = ProcedurePerformer.with_json_and_owner(jsondict['performer'], self)
        if 'relatedItem' in jsondict:
            self.relatedItem = ProcedureRelatedItem.with_json_and_owner(jsondict['relatedItem'], self)
        if 'report' in jsondict:
            self.report = fhirreference.FHIRReference.with_json_and_owner(jsondict['report'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


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
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `AllergyIntolerance, CarePlan, Condition, DiagnosticReport, FamilyHistory, ImagingStudy, Immunization, ImmunizationRecommendation, MedicationAdministration, MedicationDispense, MedicationPrescription, MedicationStatement, Observation, Procedure` (represented as `dict` in JSON). """
        
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

