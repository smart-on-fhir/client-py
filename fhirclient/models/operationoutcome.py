#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (operationoutcome.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import coding
import fhirelement
import fhirresource


class OperationOutcome(fhirresource.FHIRResource):
    """ Information about the success/failure of an action.
    
    A collection of error, warning or information messages that result from a
    system action.
    """
    
    resource_name = "OperationOutcome"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.issue = None
        """ A single issue associated with the action.
        List of `OperationOutcomeIssue` items (represented as `dict` in JSON). """
        
        super(OperationOutcome, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OperationOutcome, self).update_with_json(jsondict)
        if 'issue' in jsondict:
            self.issue = OperationOutcomeIssue.with_json_and_owner(jsondict['issue'], self)


class OperationOutcomeIssue(fhirelement.FHIRElement):
    """ A single issue associated with the action.
    
    An error, warning or information message that results from a system action.
    """
    
    resource_name = "OperationOutcomeIssue"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.details = None
        """ Additional description of the issue.
        Type `str`. """
        
        self.location = None
        """ XPath of element(s) related to issue.
        List of `str` items. """
        
        self.severity = None
        """ fatal | error | warning | information.
        Type `str`. """
        
        self.type = None
        """ Error or warning code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(OperationOutcomeIssue, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OperationOutcomeIssue, self).update_with_json(jsondict)
        if 'details' in jsondict:
            self.details = jsondict['details']
        if 'location' in jsondict:
            self.location = jsondict['location']
        if 'severity' in jsondict:
            self.severity = jsondict['severity']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)

