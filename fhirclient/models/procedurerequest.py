#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (procedurerequest.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier
import period
import timing


class ProcedureRequest(fhirresource.FHIRResource):
    """ Procedure Request.
    
    A request for a procedure to be performed. May be a proposal or an order.
    """
    
    resource_name = "ProcedureRequest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.asNeededBoolean = False
        """ PRN.
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ PRN.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Target Body Site.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Indication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Notes.
        List of `str` items. """
        
        self.orderedOn = None
        """ When Requested.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.orderer = None
        """ Ordering Party.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson, Device` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Performer.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | stat | asap.
        Type `str`. """
        
        self.status = None
        """ proposed | planned | requested | received | accepted | in progress
        | completed | suspended | rejected | aborted.
        Type `str`. """
        
        self.subject = None
        """ Subject.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ Timing.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ Timing.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ Timing.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.type = None
        """ Procedure Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProcedureRequest, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProcedureRequest, self).update_with_json(jsondict)
        if 'asNeededBoolean' in jsondict:
            self.asNeededBoolean = jsondict['asNeededBoolean']
        if 'asNeededCodeableConcept' in jsondict:
            self.asNeededCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['asNeededCodeableConcept'], self)
        if 'bodySite' in jsondict:
            self.bodySite = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['bodySite'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'indication' in jsondict:
            self.indication = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['indication'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'orderedOn' in jsondict:
            self.orderedOn = fhirdate.FHIRDate.with_json_and_owner(jsondict['orderedOn'], self)
        if 'orderer' in jsondict:
            self.orderer = fhirreference.FHIRReference.with_json_and_owner(jsondict['orderer'], self)
        if 'performer' in jsondict:
            self.performer = fhirreference.FHIRReference.with_json_and_owner(jsondict['performer'], self)
        if 'priority' in jsondict:
            self.priority = jsondict['priority']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'timingDateTime' in jsondict:
            self.timingDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['timingDateTime'], self)
        if 'timingPeriod' in jsondict:
            self.timingPeriod = period.Period.with_json_and_owner(jsondict['timingPeriod'], self)
        if 'timingTiming' in jsondict:
            self.timingTiming = timing.Timing.with_json_and_owner(jsondict['timingTiming'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

