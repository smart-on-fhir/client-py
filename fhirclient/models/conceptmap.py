#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (conceptmap.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import contact
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import narrative
import valueset


class ConceptMap(fhirresource.FHIRResource):
    """ A statement of relationships from one set of concepts to one or more other
    concept systems.
    
    Scope and Usage A concept map defines a mapping from a concept defined in
    one system to one or more concepts defined in other systems. Mappings are
    always framed within the concept of value sets - they are specific to a
    context of use.
    """
    
    resource_name = "ConceptMap"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.concept = None
        """ Mappings for a concept from the source valueset.
        List of `ConceptMapConcept` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ About the concept map or its content.
        Type `str`. """
        
        self.date = None
        """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Human language description of the concept map.
        Type `str`. """
        
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
        
        self.source = None
        """ Identifies the source value set which is being mapped.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.target = None
        """ Provides context to the mappings.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `Contact` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the concept map.
        Type `str`. """
        
        super(ConceptMap, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMap, self).update_with_json(jsondict)
        if 'concept' in jsondict:
            self.concept = ConceptMapConcept.with_json(jsondict['concept'])
        if 'copyright' in jsondict:
            self.copyright = jsondict['copyright']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'source' in jsondict:
            self.source = fhirreference.FHIRReference.with_json_and_owner(jsondict['source'], self, valueset.ValueSet)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self, valueset.ValueSet)
        if 'telecom' in jsondict:
            self.telecom = contact.Contact.with_json(jsondict['telecom'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'version' in jsondict:
            self.version = jsondict['version']


class ConceptMapConcept(fhirelement.FHIRElement):
    """ Mappings for a concept from the source valueset.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Identifies concept being mapped.
        Type `str`. """
        
        self.dependsOn = None
        """ Other concepts required for this mapping (from context).
        List of `ConceptMapConceptDependsOn` items (represented as `dict` in JSON). """
        
        self.map = None
        """ A concept from the target value set that this concept maps to.
        List of `ConceptMapConceptMap` items (represented as `dict` in JSON). """
        
        self.system = None
        """ System that defines the concept being mapped.
        Type `str`. """
        
        super(ConceptMapConcept, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMapConcept, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'dependsOn' in jsondict:
            self.dependsOn = ConceptMapConceptDependsOn.with_json(jsondict['dependsOn'])
        if 'map' in jsondict:
            self.map = ConceptMapConceptMap.with_json(jsondict['map'])
        if 'system' in jsondict:
            self.system = jsondict['system']


class ConceptMapConceptDependsOn(fhirelement.FHIRElement):
    """ Other concepts required for this mapping (from context).
    
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified concept can be resolved, and it has the
    specified value.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code for a concept in the referenced concept.
        Type `str`. """
        
        self.concept = None
        """ Reference to element/field/valueset provides the context.
        Type `str`. """
        
        self.system = None
        """ System for a concept in the referenced concept.
        Type `str`. """
        
        super(ConceptMapConceptDependsOn, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMapConceptDependsOn, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'concept' in jsondict:
            self.concept = jsondict['concept']
        if 'system' in jsondict:
            self.system = jsondict['system']


class ConceptMapConceptMap(fhirelement.FHIRElement):
    """ A concept from the target value set that this concept maps to.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code that identifies the target concept.
        Type `str`. """
        
        self.comments = None
        """ Description of status/issues in mapping.
        Type `str`. """
        
        self.equivalence = None
        """ equal | equivalent | wider | subsumes | narrower | specialises |
        inexact | unmatched | disjoint.
        Type `str`. """
        
        self.product = None
        """ Other concepts that this mapping also produces.
        List of `ConceptMapConceptMapProduct` items (represented as `dict` in JSON). """
        
        self.system = None
        """ System of the target.
        Type `str`. """
        
        super(ConceptMapConceptMap, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConceptMapConceptMap, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'equivalence' in jsondict:
            self.equivalence = jsondict['equivalence']
        if 'product' in jsondict:
            self.product = ConceptMapConceptMapProduct.with_json(jsondict['product'])
        if 'system' in jsondict:
            self.system = jsondict['system']


class ConceptMapConceptMapProduct(fhirelement.FHIRElement):
    """ Other concepts that this mapping also produces.
    
    A set of additional outcomes from this mapping to other value sets. To
    properly execute this mapping, the specified value set must be mapped to
    some data element or source that is in context. The mapping may still be
    useful without a place for the additional data elements, but the
    equivalence cannot be relied on.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(ConceptMapConceptMapProduct, self).__init__(jsondict)

