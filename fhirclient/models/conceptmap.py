#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/ConceptMap) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


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
        """ Use and/or publishing restrictions.
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
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name for this concept map.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Why needed.
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
    
    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("contact", "contact", ConceptMapContact, True),
            ("copyright", "copyright", str, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("element", "element", ConceptMapElement, True),
            ("experimental", "experimental", bool, False),
            ("identifier", "identifier", identifier.Identifier, False),
            ("name", "name", str, False),
            ("publisher", "publisher", str, False),
            ("requirements", "requirements", str, False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False),
            ("sourceUri", "sourceUri", str, False),
            ("status", "status", str, False),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False),
            ("targetUri", "targetUri", str, False),
            ("url", "url", str, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True),
            ("version", "version", str, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(ConceptMapContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


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
        
        self.target = None
        """ Concept in target system for element.
        List of `ConceptMapElementTarget` items (represented as `dict` in JSON). """
        
        super(ConceptMapElement, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConceptMapElement, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("codeSystem", "codeSystem", str, False),
            ("target", "target", ConceptMapElementTarget, True),
        ])
        return js


class ConceptMapElementTarget(fhirelement.FHIRElement):
    """ Concept in target system for element.
    
    A concept from the target value set that this concept maps to.
    """
    
    resource_name = "ConceptMapElementTarget"
    
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
        List of `ConceptMapElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        self.equivalence = None
        """ equivalent | equal | wider | subsumes | narrower | specializes |
        inexact | unmatched | disjoint.
        Type `str`. """
        
        self.product = None
        """ Other concepts that this mapping also produces.
        List of `ConceptMapElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        super(ConceptMapElementTarget, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConceptMapElementTarget, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("codeSystem", "codeSystem", str, False),
            ("comments", "comments", str, False),
            ("dependsOn", "dependsOn", ConceptMapElementTargetDependsOn, True),
            ("equivalence", "equivalence", str, False),
            ("product", "product", ConceptMapElementTargetDependsOn, True),
        ])
        return js


class ConceptMapElementTargetDependsOn(fhirelement.FHIRElement):
    """ Other elements required for this mapping (from context).
    
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """
    
    resource_name = "ConceptMapElementTargetDependsOn"
    
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
        """ Reference to element/field/ValueSet mapping depends on.
        Type `str`. """
        
        super(ConceptMapElementTargetDependsOn, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConceptMapElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("codeSystem", "codeSystem", str, False),
            ("element", "element", str, False),
        ])
        return js

