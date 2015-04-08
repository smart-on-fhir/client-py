#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/StructureDefinition) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import coding
import contactpoint
import domainresource
import elementdefinition
import fhirdate
import fhirelement
import identifier


class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.
    
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions, and constraints on resources and data types.
    """
    
    resource_name = "StructureDefinition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.abstract = False
        """ Whether the structure is abstract.
        Type `bool`. """
        
        self.base = None
        """ Structure that this set of constraints applies to.
        Type `str`. """
        
        self.code = None
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `StructureDefinitionContact` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Where the extension can be used in instances.
        List of `str` items. """
        
        self.contextType = None
        """ resource | datatype | mapping | extension.
        Type `str`. """
        
        self.copyright = None
        """ Use and/or Publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date for this version of the StructureDefinition.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the StructureDefinition.
        Type `str`. """
        
        self.differential = None
        """ Differential view of the structure.
        Type `StructureDefinitionDifferential` (represented as `dict` in JSON). """
        
        self.display = None
        """ Use this name when displaying the value.
        Type `str`. """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None
        """ FHIR Version this StructureDefinition targets.
        Type `str`. """
        
        self.identifier = None
        """ Other identifiers for the StructureDefinition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.mapping = None
        """ External specification that the content is mapped to.
        List of `StructureDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name for this StructureDefinition.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Scope and Usage this structure definition is for.
        Type `str`. """
        
        self.snapshot = None
        """ Snapshot view of the structure.
        Type `StructureDefinitionSnapshot` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.type = None
        """ type | resource | constraint | extension.
        Type `str`. """
        
        self.url = None
        """ Literal URL used to reference this StructureDefinition.
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the StructureDefinition.
        Type `str`. """
        
        super(StructureDefinition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(StructureDefinition, self).update_with_json(jsondict)
        if 'abstract' in jsondict:
            self.abstract = jsondict['abstract']
        if 'base' in jsondict:
            self.base = jsondict['base']
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'contact' in jsondict:
            self.contact = StructureDefinitionContact.with_json_and_owner(jsondict['contact'], self)
        if 'context' in jsondict:
            self.context = jsondict['context']
        if 'contextType' in jsondict:
            self.contextType = jsondict['contextType']
        if 'copyright' in jsondict:
            self.copyright = jsondict['copyright']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'differential' in jsondict:
            self.differential = StructureDefinitionDifferential.with_json_and_owner(jsondict['differential'], self)
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'fhirVersion' in jsondict:
            self.fhirVersion = jsondict['fhirVersion']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'mapping' in jsondict:
            self.mapping = StructureDefinitionMapping.with_json_and_owner(jsondict['mapping'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'snapshot' in jsondict:
            self.snapshot = StructureDefinitionSnapshot.with_json_and_owner(jsondict['snapshot'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'useContext' in jsondict:
            self.useContext = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['useContext'], self)
        if 'version' in jsondict:
            self.version = jsondict['version']


class StructureDefinitionContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "StructureDefinitionContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionContact, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(StructureDefinitionContact, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


class StructureDefinitionDifferential(fhirelement.FHIRElement):
    """ Differential view of the structure.
    
    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """
    
    resource_name = "StructureDefinitionDifferential"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionDifferential, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(StructureDefinitionDifferential, self).update_with_json(jsondict)
        if 'element' in jsondict:
            self.element = elementdefinition.ElementDefinition.with_json_and_owner(jsondict['element'], self)


class StructureDefinitionMapping(fhirelement.FHIRElement):
    """ External specification that the content is mapped to.
    
    An external specification that the content is mapped to.
    """
    
    resource_name = "StructureDefinitionMapping"
    
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
        
        super(StructureDefinitionMapping, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(StructureDefinitionMapping, self).update_with_json(jsondict)
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'identity' in jsondict:
            self.identity = jsondict['identity']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'uri' in jsondict:
            self.uri = jsondict['uri']


class StructureDefinitionSnapshot(fhirelement.FHIRElement):
    """ Snapshot view of the structure.
    
    A snapshot view is expressed in a stand alone form that can be used and
    interpreted without considering the base StructureDefinition.
    """
    
    resource_name = "StructureDefinitionSnapshot"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionSnapshot, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(StructureDefinitionSnapshot, self).update_with_json(jsondict)
        if 'element' in jsondict:
            self.element = elementdefinition.ElementDefinition.with_json_and_owner(jsondict['element'], self)

