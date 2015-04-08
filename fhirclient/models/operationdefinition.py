#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2015-04-08.
#  2015, SMART Health IT.


import contactpoint
import domainresource
import fhirdate
import fhirelement
import fhirreference


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
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.idempotent = False
        """ Whether operation causes changes to content.
        Type `bool`. """
        
        self.instance = False
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
        
        self.system = False
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
    
    def update_with_json(self, jsondict):
        super(OperationDefinition, self).update_with_json(jsondict)
        if 'base' in jsondict:
            self.base = fhirreference.FHIRReference.with_json_and_owner(jsondict['base'], self)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'contact' in jsondict:
            self.contact = OperationDefinitionContact.with_json_and_owner(jsondict['contact'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'idempotent' in jsondict:
            self.idempotent = jsondict['idempotent']
        if 'instance' in jsondict:
            self.instance = jsondict['instance']
        if 'kind' in jsondict:
            self.kind = jsondict['kind']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'parameter' in jsondict:
            self.parameter = OperationDefinitionParameter.with_json_and_owner(jsondict['parameter'], self)
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'version' in jsondict:
            self.version = jsondict['version']


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
    
    def update_with_json(self, jsondict):
        super(OperationDefinitionContact, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


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
    
    def update_with_json(self, jsondict):
        super(OperationDefinitionParameter, self).update_with_json(jsondict)
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'max' in jsondict:
            self.max = jsondict['max']
        if 'min' in jsondict:
            self.min = jsondict['min']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'part' in jsondict:
            self.part = OperationDefinitionParameterPart.with_json_and_owner(jsondict['part'], self)
        if 'profile' in jsondict:
            self.profile = fhirreference.FHIRReference.with_json_and_owner(jsondict['profile'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'use' in jsondict:
            self.use = jsondict['use']


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
    
    def update_with_json(self, jsondict):
        super(OperationDefinitionParameterPart, self).update_with_json(jsondict)
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'max' in jsondict:
            self.max = jsondict['max']
        if 'min' in jsondict:
            self.min = jsondict['min']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'profile' in jsondict:
            self.profile = fhirreference.FHIRReference.with_json_and_owner(jsondict['profile'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']

