#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/OperationOutcome) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class OperationOutcome(domainresource.DomainResource):
    """ Information about the success/failure of an action.
    
    A collection of error, warning or information messages that result from a
    system action.
    """
    
    resource_type = "OperationOutcome"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.issue = None
        """ A single issue associated with the action.
        List of `OperationOutcomeIssue` items (represented as `dict` in JSON). """
        
        super(OperationOutcome, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationOutcome, self).elementProperties()
        js.extend([
            ("issue", "issue", OperationOutcomeIssue, True, None, True),
        ])
        return js


from . import backboneelement

class OperationOutcomeIssue(backboneelement.BackboneElement):
    """ A single issue associated with the action.
    
    An error, warning or information message that results from a system action.
    """
    
    resource_type = "OperationOutcomeIssue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Error or warning code.
        Type `str`. """
        
        self.details = None
        """ Additional details about the error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnostics = None
        """ Additional diagnostic information about the issue.
        Type `str`. """
        
        self.expression = None
        """ FHIRPath of element(s) related to issue.
        List of `str` items. """
        
        self.location = None
        """ Path of element(s) related to issue.
        List of `str` items. """
        
        self.severity = None
        """ fatal | error | warning | information.
        Type `str`. """
        
        super(OperationOutcomeIssue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationOutcomeIssue, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("details", "details", codeableconcept.CodeableConcept, False, None, False),
            ("diagnostics", "diagnostics", str, False, None, False),
            ("expression", "expression", str, True, None, False),
            ("location", "location", str, True, None, False),
            ("severity", "severity", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
