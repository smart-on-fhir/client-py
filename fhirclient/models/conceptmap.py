#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (conceptmap.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import contactpoint
import fhirdate
import fhirelement
import fhirreference
import fhirresource


class ConceptMap(fhirresource.FHIRResource):
    """ A map from one set of concepts to one or more other concepts.
    
    A statement of relationships from one set of concepts to one or more other
    concepts - either code systems or data elements, or classes in class
    models.
    """
    
    resource_name = "ConceptMap"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.copyright = None
        """ About the concept map or its content.
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
        """ Logical id to reference this concept map.
        Type `str`. """
        
        self.name = None
        """ Informal name for this concept map.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.sourceReference = None
        """ Identifies the source of the concepts which are being mapped.
        Type `FHIRReference` referencing `ValueSet, Profile` (represented as `dict` in JSON). """
        
        self.sourceUri = None
        """ Identifies the source of the concepts which are being mapped.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.targetReference = None
        """ Provides context to the mappings.
        Type `FHIRReference` referencing `ValueSet, Profile` (represented as `dict` in JSON). """
        
        self.targetUri = None
        """ Provides context to the mappings.
        Type `str`. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the concept map.
        Type `str`. """
        
        super(ConceptMap, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMap, self).update_with_json(jsondict)
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
            self.identifier = jsondict['identifier']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
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
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'version' in jsondict:
            self.version = jsondict['version']


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

