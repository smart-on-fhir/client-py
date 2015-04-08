#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ConceptMap) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import contactpoint
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier


class ConceptMap(domainresource.DomainResource):
    """ A map from one set of concepts to one or more other concepts.
    
    A statement of relationships from one set of concepts to one or more other
    concepts - either code systems or data elements, or classes in class
    models.
    """
    
    resource_name = "ConceptMap"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ConceptMapContact` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or Publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Human language description of the concept map.
        Type `str`. """
        
        self.element = None
        """ Mappings for a concept from the source set.
        List of `ConceptMapElement` items (represented as `dict` in JSON). """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name for this concept map.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Why is this needed?.
        Type `str`. """
        
        self.sourceReference = None
        """ Identifies the source of the concepts which are being mapped.
        Type `FHIRReference` referencing `ValueSet, StructureDefinition` (represented as `dict` in JSON). """
        
        self.sourceUri = None
        """ Identifies the source of the concepts which are being mapped.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.targetReference = None
        """ Provides context to the mappings.
        Type `FHIRReference` referencing `ValueSet, StructureDefinition` (represented as `dict` in JSON). """
        
        self.targetUri = None
        """ Provides context to the mappings.
        Type `str`. """
        
        self.url = None
        """ Globally unique logical id for concept map.
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the concept map.
        Type `str`. """
        
        super(ConceptMap, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMap, self).update_with_json(jsondict)
        if 'contact' in jsondict:
            self.contact = ConceptMapContact.with_json_and_owner(jsondict['contact'], self)
        if 'copyright' in jsondict:
            self.copyright = jsondict['copyright']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'element' in jsondict:
            self.element = ConceptMapElement.with_json_and_owner(jsondict['element'], self)
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'sourceReference' in jsondict:
            self.sourceReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['sourceReference'], self)
        if 'sourceUri' in jsondict:
            self.sourceUri = jsondict['sourceUri']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'targetReference' in jsondict:
            self.targetReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['targetReference'], self)
        if 'targetUri' in jsondict:
            self.targetUri = jsondict['targetUri']
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'useContext' in jsondict:
            self.useContext = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['useContext'], self)
        if 'version' in jsondict:
            self.version = jsondict['version']


class ConceptMapContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "ConceptMapContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ConceptMapContact, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMapContact, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


class ConceptMapElement(fhirelement.FHIRElement):
    """ Mappings for a concept from the source set.
    
    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """
    
    resource_name = "ConceptMapElement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Identifies element being mapped.
        Type `str`. """
        
        self.codeSystem = None
        """ Code System (if value set crosses code systems).
        Type `str`. """
        
        self.dependsOn = None
        """ Other elements required for this mapping (from context).
        List of `ConceptMapElementDependsOn` items (represented as `dict` in JSON). """
        
        self.map = None
        """ Target of this map.
        List of `ConceptMapElementMap` items (represented as `dict` in JSON). """
        
        super(ConceptMapElement, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMapElement, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'codeSystem' in jsondict:
            self.codeSystem = jsondict['codeSystem']
        if 'dependsOn' in jsondict:
            self.dependsOn = ConceptMapElementDependsOn.with_json_and_owner(jsondict['dependsOn'], self)
        if 'map' in jsondict:
            self.map = ConceptMapElementMap.with_json_and_owner(jsondict['map'], self)


class ConceptMapElementDependsOn(fhirelement.FHIRElement):
    """ Other elements required for this mapping (from context).
    
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """
    
    resource_name = "ConceptMapElementDependsOn"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Value of the referenced element.
        Type `str`. """
        
        self.codeSystem = None
        """ Code System (if necessary).
        Type `str`. """
        
        self.element = None
        """ Reference to element/field/valueset mapping depends on.
        Type `str`. """
        
        super(ConceptMapElementDependsOn, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMapElementDependsOn, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'codeSystem' in jsondict:
            self.codeSystem = jsondict['codeSystem']
        if 'element' in jsondict:
            self.element = jsondict['element']


class ConceptMapElementMap(fhirelement.FHIRElement):
    """ Target of this map.
    
    A concept from the target value set that this concept maps to.
    """
    
    resource_name = "ConceptMapElementMap"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code that identifies the target element.
        Type `str`. """
        
        self.codeSystem = None
        """ System of the target (if necessary).
        Type `str`. """
        
        self.comments = None
        """ Description of status/issues in mapping.
        Type `str`. """
        
        self.dependsOn = None
        """ Other elements required for this mapping (from context).
        List of `ConceptMapElementDependsOn` items (represented as `dict` in JSON). """
        
        self.equivalence = None
        """ equivalent | equal | wider | subsumes | narrower | specialises |
        inexact | unmatched | disjoint.
        Type `str`. """
        
        super(ConceptMapElementMap, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMapElementMap, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'codeSystem' in jsondict:
            self.codeSystem = jsondict['codeSystem']
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'dependsOn' in jsondict:
            self.dependsOn = ConceptMapElementDependsOn.with_json_and_owner(jsondict['dependsOn'], self)
        if 'equivalence' in jsondict:
            self.equivalence = jsondict['equivalence']

