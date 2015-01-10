#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (operationdefinition.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import coding
import contactpoint
import fhirdate
import fhirelement
import fhirreference
import fhirresource


class OperationDefinition(fhirresource.FHIRResource):
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
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for this version of the operation definition.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the operation.
        Type `str`. """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Logical id to reference this operation definition.
        Type `str`. """
        
        self.instance = False
        """ Invoke on an instance?.
        Type `bool`. """
        
        self.kind = None
        """ operation | query.
        Type `str`. """
        
        self.name = None
        """ Name used to invoke the operation.
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
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.system = False
        """ Invoke at the system level?.
        Type `bool`. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Informal name for this profile.
        Type `str`. """
        
        self.type = None
        """ Invoke at resource level for these type.
        List of `str` items. """
        
        self.version = None
        """ Logical id for this version of the operation definition.
        Type `str`. """
        
        super(OperationDefinition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OperationDefinition, self).update_with_json(jsondict)
        if 'base' in jsondict:
            self.base = fhirreference.FHIRReference.with_json_and_owner(jsondict['base'], self)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
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
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'title' in jsondict:
            self.title = jsondict['title']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'version' in jsondict:
            self.version = jsondict['version']


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
        Type `FHIRReference` referencing `Profile` (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `Profile` (represented as `dict` in JSON). """
        
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

