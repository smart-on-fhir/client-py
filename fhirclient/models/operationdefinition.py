#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2015-07-06.
#  2015, SMART Health IT.


from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference


class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.
    
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """
    
    resource_name = "OperationDefinition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        """ Whether operation causes changes to content.
        Type `bool`. """
        
        self.instance = None
        """ Invoke on an instance?.
        Type `bool`. """
        
        self.kind = None
        """ operation | query.
        Type `str`. """
        
        self.name = None
        """ Informal name for this profile.
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
        """ Logical url to reference this operation definition.
        Type `str`. """
        
        self.version = None
        """ Logical id for this version of the operation definition.
        Type `str`. """
        
        super(OperationDefinition, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("base", "base", fhirreference.FHIRReference, False),
            ("code", "code", str, False),
            ("contact", "contact", OperationDefinitionContact, True),
            ("date", "date", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("experimental", "experimental", bool, False),
            ("idempotent", "idempotent", bool, False),
            ("instance", "instance", bool, False),
            ("kind", "kind", str, False),
            ("name", "name", str, False),
            ("notes", "notes", str, False),
            ("parameter", "parameter", OperationDefinitionParameter, True),
            ("publisher", "publisher", str, False),
            ("requirements", "requirements", str, False),
            ("status", "status", str, False),
            ("system", "system", bool, False),
            ("type", "type", str, True),
            ("url", "url", str, False),
            ("version", "version", str, False),
        ])
        return js


class OperationDefinitionContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "OperationDefinitionContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(OperationDefinitionContact, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(OperationDefinitionContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class OperationDefinitionParameter(fhirelement.FHIRElement):
    """ Parameters for the operation/query.
    
    The parameters for the operation/query.
    """
    
    resource_name = "OperationDefinitionParameter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
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
        """ Name of the parameter.
        Type `str`. """
        
        self.part = None
        """ Parts of a Tuple Parameter.
        List of `OperationDefinitionParameterPart` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ Profile on the type.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.type = None
        """ What type this parameter hs.
        Type `str`. """
        
        self.use = None
        """ in | out.
        Type `str`. """
        
        super(OperationDefinitionParameter, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False),
            ("max", "max", str, False),
            ("min", "min", int, False),
            ("name", "name", str, False),
            ("part", "part", OperationDefinitionParameterPart, True),
            ("profile", "profile", fhirreference.FHIRReference, False),
            ("type", "type", str, False),
            ("use", "use", str, False),
        ])
        return js


class OperationDefinitionParameterPart(fhirelement.FHIRElement):
    """ Parts of a Tuple Parameter.
    
    The parts of a Tuple Parameter.
    """
    
    resource_name = "OperationDefinitionParameterPart"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
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
        """ Name of the parameter.
        Type `str`. """
        
        self.profile = None
        """ Profile on the type.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.type = None
        """ What type this parameter hs.
        Type `str`. """
        
        super(OperationDefinitionParameterPart, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameterPart, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False),
            ("max", "max", str, False),
            ("min", "min", int, False),
            ("name", "name", str, False),
            ("profile", "profile", fhirreference.FHIRReference, False),
            ("type", "type", str, False),
        ])
        return js

