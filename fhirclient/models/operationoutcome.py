#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (operationoutcome.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import coding
import fhirelement
import fhirresource
import narrative


class OperationOutcome(fhirresource.FHIRResource):
    """ Information about the success/failure of an action.
    
    Scope and Usage Operation Outcomes are sets of error, warning and
    information messages that provide detailed information about the outcome of
    some attempted system operation. They are provided as a direct system
    response, or component of one, where they provide information about the
    outcome of the operation.
    
    Specifically, OperationOutcomes are used in the following circumstances:
    
    * When an RESTful operation fails
    * As the response on a validation operation, to provide information about
    the outcomes
    * As part of a message response, usually when the message has not been
    processed correctly
    """
    
    resource_name = "OperationOutcome"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.issue = None
        """ A single issue associated with the action.
        List of `OperationOutcomeIssue` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(OperationOutcome, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OperationOutcome, self).update_with_json(jsondict)
        if 'issue' in jsondict:
            self.issue = OperationOutcomeIssue.with_json(jsondict['issue'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class OperationOutcomeIssue(fhirelement.FHIRElement):
    """ A single issue associated with the action.
    
    An error, warning or information message that results from a system action.
    """
    
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
            self.type = coding.Coding.with_json(jsondict['type'])

