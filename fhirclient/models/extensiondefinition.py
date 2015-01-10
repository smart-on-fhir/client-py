#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (extensiondefinition.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import coding
import contactpoint
import elementdefinition
import fhirdate
import fhirelement
import fhirresource
import identifier


class ExtensionDefinition(fhirresource.FHIRResource):
    """ Extension Definition.
    
    Defines an extension that can be used in resources.
    """
    
    resource_name = "ExtensionDefinition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Where the extension can be used in instances.
        List of `str` items. """
        
        self.contextType = None
        """ resource | datatype | mapping | extension.
        Type `str`. """
        
        self.date = None
        """ Date for this version of the extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the extension.
        Type `str`. """
        
        self.display = None
        """ Use this name when displaying the value.
        Type `str`. """
        
        self.element = None
        """ Definition of the elements in the extension.
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Other identifiers for the extension.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.mapping = None
        """ External specification that the content is mapped to.
        List of `ExtensionDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Descriptional name for this profile.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Scope and Usage this extesion is for.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Literal URL used to reference this extension.
        Type `str`. """
        
        super(ExtensionDefinition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ExtensionDefinition, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'context' in jsondict:
            self.context = jsondict['context']
        if 'contextType' in jsondict:
            self.contextType = jsondict['contextType']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'element' in jsondict:
            self.element = elementdefinition.ElementDefinition.with_json_and_owner(jsondict['element'], self)
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'mapping' in jsondict:
            self.mapping = ExtensionDefinitionMapping.with_json_and_owner(jsondict['mapping'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'url' in jsondict:
            self.url = jsondict['url']


class ExtensionDefinitionMapping(fhirelement.FHIRElement):
    """ External specification that the content is mapped to.
    
    An external specification that the content is mapped to.
    """
    
    resource_name = "ExtensionDefinitionMapping"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comments = None
        """ Versions, Issues, Scope limitations etc.
        Type `str`. """
        
        self.identity = None
        """ Internal id when this mapping is used.
        Type `str`. """
        
        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """
        
        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """
        
        super(ExtensionDefinitionMapping, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ExtensionDefinitionMapping, self).update_with_json(jsondict)
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'identity' in jsondict:
            self.identity = jsondict['identity']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'uri' in jsondict:
            self.uri = jsondict['uri']

