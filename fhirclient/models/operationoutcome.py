# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/OperationOutcome).
# 2024, SMART Health IT.


from . import domainresource

class OperationOutcome(domainresource.DomainResource):
    """ Information about the success/failure of an action.
    
    A collection of error, warning, or information messages that result from a
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
        self._issue = None
        """ Primitive extension for issue. Type `FHIRPrimitiveExtension` """
        
        super(OperationOutcome, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationOutcome, self).elementProperties()
        js.extend([
            ("issue", "issue", OperationOutcomeIssue, True, None, True),
            ("_issue", "_issue", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class OperationOutcomeIssue(backboneelement.BackboneElement):
    """ A single issue associated with the action.
    
    An error, warning, or information message that results from a system
    action.
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
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.details = None
        """ Additional details about the error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._details = None
        """ Primitive extension for details. Type `FHIRPrimitiveExtension` """
        
        self.diagnostics = None
        """ Additional diagnostic information about the issue.
        Type `str`. """
        self._diagnostics = None
        """ Primitive extension for diagnostics. Type `FHIRPrimitiveExtension` """
        
        self.expression = None
        """ FHIRPath of element(s) related to issue.
        List of `str` items. """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Deprecated: Path of element(s) related to issue.
        List of `str` items. """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.severity = None
        """ fatal | error | warning | information.
        Type `str`. """
        self._severity = None
        """ Primitive extension for severity. Type `FHIRPrimitiveExtension` """
        
        super(OperationOutcomeIssue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationOutcomeIssue, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("details", "details", codeableconcept.CodeableConcept, False, None, False),
            ("_details", "_details", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("diagnostics", "diagnostics", str, False, None, False),
            ("_diagnostics", "_diagnostics", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expression", "expression", str, True, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", str, True, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("severity", "severity", str, False, None, True),
            ("_severity", "_severity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept