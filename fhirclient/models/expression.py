# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Expression).
# 2024, SMART Health IT.


from . import element

class Expression(element.Element):
    """ An expression that can be used to generate a value.
    
    A expression that is evaluated in a specified context and returns a value.
    The context of use of the expression must specify the context in which the
    expression is evaluated, and how the result of the expression is used.
    """
    
    resource_type = "Expression"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Natural language description of the condition.
        Type `str`. """
        
        self.expression = None
        """ Expression in specified language.
        Type `str`. """
        
        self.language = None
        """ text/cql | text/fhirpath | application/x-fhir-query | etc..
        Type `str`. """
        
        self.name = None
        """ Short name assigned to expression for reuse.
        Type `str`. """
        
        self.reference = None
        """ Where the expression is found.
        Type `str`. """
        
        super(Expression, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Expression, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("reference", "reference", str, False, None, False),
        ])
        return js


