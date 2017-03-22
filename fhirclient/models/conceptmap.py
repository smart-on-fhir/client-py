#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/ConceptMap) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class ConceptMap(domainresource.DomainResource):
    """ A map from one set of concepts to one or more other concepts.
    
    A statement of relationships from one set of concepts to one or more other
    concepts - either code systems or data elements, or classes in class
    models.
    """
    
    resource_type = "ConceptMap"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the concept map.
        Type `str`. """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.group = None
        """ Same source and target systems.
        List of `ConceptMapGroup` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for concept map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this concept map (computer friendly).
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Why this concept map is defined.
        Type `str`. """
        
        self.sourceReference = None
        """ Identifies the source of the concepts which are being mapped.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.sourceUri = None
        """ Identifies the source of the concepts which are being mapped.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.targetReference = None
        """ Provides context to the mappings.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.targetUri = None
        """ Provides context to the mappings.
        Type `str`. """
        
        self.title = None
        """ Name for this concept map (human friendly).
        Type `str`. """
        
        self.url = None
        """ Logical URI to reference this concept map (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the concept map.
        Type `str`. """
        
        super(ConceptMap, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", ConceptMapGroup, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", False),
            ("sourceUri", "sourceUri", str, False, "source", False),
            ("status", "status", str, False, None, True),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", False),
            ("targetUri", "targetUri", str, False, "target", False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ConceptMapGroup(backboneelement.BackboneElement):
    """ Same source and target systems.
    
    A group of mappings that all have the same source and target system.
    """
    
    resource_type = "ConceptMapGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        """ Mappings for a concept from the source set.
        List of `ConceptMapGroupElement` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Code System (if value set crosses code systems).
        Type `str`. """
        
        self.sourceVersion = None
        """ Specific version of the  code system.
        Type `str`. """
        
        self.target = None
        """ System of the target (if necessary).
        Type `str`. """
        
        self.targetVersion = None
        """ Specific version of the  code system.
        Type `str`. """
        
        self.unmapped = None
        """ When no match in the mappings.
        Type `ConceptMapGroupUnmapped` (represented as `dict` in JSON). """
        
        super(ConceptMapGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroup, self).elementProperties()
        js.extend([
            ("element", "element", ConceptMapGroupElement, True, None, True),
            ("source", "source", str, False, None, False),
            ("sourceVersion", "sourceVersion", str, False, None, False),
            ("target", "target", str, False, None, False),
            ("targetVersion", "targetVersion", str, False, None, False),
            ("unmapped", "unmapped", ConceptMapGroupUnmapped, False, None, False),
        ])
        return js


class ConceptMapGroupElement(backboneelement.BackboneElement):
    """ Mappings for a concept from the source set.
    
    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """
    
    resource_type = "ConceptMapGroupElement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Identifies element being mapped.
        Type `str`. """
        
        self.display = None
        """ Display for the code.
        Type `str`. """
        
        self.target = None
        """ Concept in target system for element.
        List of `ConceptMapGroupElementTarget` items (represented as `dict` in JSON). """
        
        super(ConceptMapGroupElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElement, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("target", "target", ConceptMapGroupElementTarget, True, None, False),
        ])
        return js


class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    """ Concept in target system for element.
    
    A concept from the target value set that this concept maps to.
    """
    
    resource_type = "ConceptMapGroupElementTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code that identifies the target element.
        Type `str`. """
        
        self.comment = None
        """ Description of status/issues in mapping.
        Type `str`. """
        
        self.dependsOn = None
        """ Other elements required for this mapping (from context).
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        self.display = None
        """ Display for the code.
        Type `str`. """
        
        self.equivalence = None
        """ relatedto | equivalent | equal | wider | subsumes | narrower |
        specializes | inexact | unmatched | disjoint.
        Type `str`. """
        
        self.product = None
        """ Other concepts that this mapping also produces.
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        super(ConceptMapGroupElementTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElementTarget, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("dependsOn", "dependsOn", ConceptMapGroupElementTargetDependsOn, True, None, False),
            ("display", "display", str, False, None, False),
            ("equivalence", "equivalence", str, False, None, False),
            ("product", "product", ConceptMapGroupElementTargetDependsOn, True, None, False),
        ])
        return js


class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    """ Other elements required for this mapping (from context).
    
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """
    
    resource_type = "ConceptMapGroupElementTargetDependsOn"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Value of the referenced element.
        Type `str`. """
        
        self.display = None
        """ Display for the code.
        Type `str`. """
        
        self.property = None
        """ Reference to property mapping depends on.
        Type `str`. """
        
        self.system = None
        """ Code System (if necessary).
        Type `str`. """
        
        super(ConceptMapGroupElementTargetDependsOn, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("display", "display", str, False, None, False),
            ("property", "property", str, False, None, True),
            ("system", "system", str, False, None, False),
        ])
        return js


class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """ When no match in the mappings.
    
    What to do when there is no match in the mappings in the group.
    """
    
    resource_type = "ConceptMapGroupUnmapped"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Fixed code when mode = fixed.
        Type `str`. """
        
        self.display = None
        """ Display for the code.
        Type `str`. """
        
        self.mode = None
        """ provided | fixed | other-map.
        Type `str`. """
        
        self.url = None
        """ Canonical URL for other concept map.
        Type `str`. """
        
        super(ConceptMapGroupUnmapped, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupUnmapped, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
