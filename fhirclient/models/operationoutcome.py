#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/OperationOutcome) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirelement


class OperationOutcome(domainresource.DomainResource):
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
        
        self.code = None
        """ Error or warning code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.details = None
        """ Additional diagnostic information about the issue.
        Type `str`. """
        
        self.location = None
        """ XPath of element(s) related to issue.
        List of `str` items. """
        
        self.severity = None
        """ fatal | error | warning | information.
        Type `str`. """
        
        super(OperationOutcomeIssue, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OperationOutcomeIssue, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'details' in jsondict:
            self.details = jsondict['details']
        if 'location' in jsondict:
            self.location = jsondict['location']
        if 'severity' in jsondict:
            self.severity = jsondict['severity']

