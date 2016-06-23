#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.
    
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """
    
    resource_name = "OperationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.base = None
        """ Marks this as a profile of the base.
        Type `FHIRReference` referencing `OperationDefinition` (represented as `dict` in JSON). """
        
        self.code = None
        """ Name used to invoke the operation.
        Type `str`. """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `OperationDefinitionContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for this version of the operation definition.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the operation.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.idempotent = None
        """ Whether content is unchanged by operation.
        Type `bool`. """
        
        self.instance = None
        """ Invoke on an instance?.
        Type `bool`. """
        
        self.kind = None
        """ operation | query.
        Type `str`. """
        
        self.name = None
        """ Informal name for this operation.
        Type `str`. """
        
        self.notes = None
        """ Additional information about use.
        Type `str`. """
        
        self.parameter = None
        """ Parameters for the operation/query.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Why is this needed?.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.system = None
        """ Invoke at the system level?.
        Type `bool`. """
        
        self.type = None
        """ Invoke at resource level for these type.
        List of `str` items. """
        
        self.url = None
        """ Logical URL to reference this operation definition.
        Type `str`. """
        
        self.version = None
        """ Logical id for this version of the operation definition.
        Type `str`. """
        
        super(OperationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("base", "base", fhirreference.FHIRReference, False, None, False),
            ("code", "code", str, False, None, True),
            ("contact", "contact", OperationDefinitionContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("idempotent", "idempotent", bool, False, None, False),
            ("instance", "instance", bool, False, None, True),
            ("kind", "kind", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("notes", "notes", str, False, None, False),
            ("parameter", "parameter", OperationDefinitionParameter, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("system", "system", bool, False, None, True),
            ("type", "type", str, True, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class OperationDefinitionContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "OperationDefinitionContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(OperationDefinitionContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """ Parameters for the operation/query.
    
    The parameters for the operation/query.
    """
    
    resource_name = "OperationDefinitionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `OperationDefinitionParameterBinding` (represented as `dict` in JSON). """
        
        self.documentation = None
        """ Description of meaning/use.
        Type `str`. """
        
        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        
        self.min = None
        """ Minimum Cardinality.
        Type `int`. """
        
        self.name = None
        """ Name in Parameters.parameter.name or in URL.
        Type `str`. """
        
        self.part = None
        """ Parts of a Tuple Parameter.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ Profile on the type.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.type = None
        """ What type this parameter has.
        Type `str`. """
        
        self.use = None
        """ in | out.
        Type `str`. """
        
        super(OperationDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("binding", "binding", OperationDefinitionParameterBinding, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("max", "max", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("name", "name", str, False, None, True),
            ("part", "part", OperationDefinitionParameter, True, None, False),
            ("profile", "profile", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, False),
            ("use", "use", str, False, None, True),
        ])
        return js


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """
    
    resource_name = "OperationDefinitionParameterBinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.strength = None
        """ required | extensible | preferred | example.
        Type `str`. """
        
        self.valueSetReference = None
        """ Source of value set.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.valueSetUri = None
        """ Source of value set.
        Type `str`. """
        
        super(OperationDefinitionParameterBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameterBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", str, False, None, True),
            ("valueSetReference", "valueSetReference", fhirreference.FHIRReference, False, "valueSet", True),
            ("valueSetUri", "valueSetUri", str, False, "valueSet", True),
        ])
        return js


from . import contactpoint
from . import fhirdate
from . import fhirreference
