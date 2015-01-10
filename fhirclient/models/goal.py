#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (goal.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import fhirreference
import fhirresource
import identifier


class Goal(fhirresource.FHIRResource):
    """ Patient Health Goal.
    
    Describes the intended objective(s) of the care.
    """
    
    resource_name = "Goal"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.concern = None
        """ Health issues this goal addresses.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.description = None
        """ What's the desired outcome?.
        Type `str`. """
        
        self.identifier = None
        """ External Ids for this goal.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Comments about the goal.
        Type `str`. """
        
        self.patient = None
        """ The patient for whom this goal is intended for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | planned | in progress | achieved | sustaining |
        cancelled | accepted | rejected.
        Type `str`. """
        
        super(Goal, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Goal, self).update_with_json(jsondict)
        if 'concern' in jsondict:
            self.concern = fhirreference.FHIRReference.with_json_and_owner(jsondict['concern'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']

