# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ConceptMap).
# 2024, SMART Health IT.


from . import domainresource

class ConceptMap(domainresource.DomainResource):
    """ A map from one set of concepts to one or more other concepts.
    
    A statement of relationships from one set of concepts to one or more other
    concepts - either concepts in code systems, or data element/data element
    concepts, or classes in class models.
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
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        self._copyright = None
        """ Primitive extension for copyright. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the concept map.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.group = None
        """ Same source and target systems.
        List of `ConceptMapGroup` items (represented as `dict` in JSON). """
        self._group = None
        """ Primitive extension for group. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for concept map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this concept map (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this concept map is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.sourceCanonical = None
        """ The source value set that contains the concepts that are being
        mapped.
        Type `str`. """
        self._sourceCanonical = None
        """ Primitive extension for sourceCanonical. Type `FHIRPrimitiveExtension` """
        
        self.sourceUri = None
        """ The source value set that contains the concepts that are being
        mapped.
        Type `str`. """
        self._sourceUri = None
        """ Primitive extension for sourceUri. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.targetCanonical = None
        """ The target value set which provides context for the mappings.
        Type `str`. """
        self._targetCanonical = None
        """ Primitive extension for targetCanonical. Type `FHIRPrimitiveExtension` """
        
        self.targetUri = None
        """ The target value set which provides context for the mappings.
        Type `str`. """
        self._targetUri = None
        """ Primitive extension for targetUri. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this concept map (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this concept map, represented as a URI
        (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the concept map.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ConceptMap, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("group", "group", ConceptMapGroup, True, None, False),
            ("_group", "_group", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceCanonical", "sourceCanonical", str, False, "source", False),
            ("_sourceCanonical", "_sourceCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceUri", "sourceUri", str, False, "source", False),
            ("_sourceUri", "_sourceUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetCanonical", "targetCanonical", str, False, "target", False),
            ("_targetCanonical", "_targetCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetUri", "targetUri", str, False, "target", False),
            ("_targetUri", "_targetUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._element = None
        """ Primitive extension for element. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Source system where concepts to be mapped are defined.
        Type `str`. """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.sourceVersion = None
        """ Specific version of the  code system.
        Type `str`. """
        self._sourceVersion = None
        """ Primitive extension for sourceVersion. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Target system that the concepts are to be mapped to.
        Type `str`. """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        self.targetVersion = None
        """ Specific version of the  code system.
        Type `str`. """
        self._targetVersion = None
        """ Primitive extension for targetVersion. Type `FHIRPrimitiveExtension` """
        
        self.unmapped = None
        """ What to do when there is no mapping for the source concept.
        Type `ConceptMapGroupUnmapped` (represented as `dict` in JSON). """
        self._unmapped = None
        """ Primitive extension for unmapped. Type `FHIRPrimitiveExtension` """
        
        super(ConceptMapGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroup, self).elementProperties()
        js.extend([
            ("element", "element", ConceptMapGroupElement, True, None, True),
            ("_element", "_element", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", str, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceVersion", "sourceVersion", str, False, None, False),
            ("_sourceVersion", "_sourceVersion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", str, False, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetVersion", "targetVersion", str, False, None, False),
            ("_targetVersion", "_targetVersion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unmapped", "unmapped", ConceptMapGroupUnmapped, False, None, False),
            ("_unmapped", "_unmapped", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.display = None
        """ Display for the code.
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Concept in target system for element.
        List of `ConceptMapGroupElementTarget` items (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        super(ConceptMapGroupElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElement, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", ConceptMapGroupElementTarget, True, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Description of status/issues in mapping.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.dependsOn = None
        """ Other elements required for this mapping (from context).
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        self._dependsOn = None
        """ Primitive extension for dependsOn. Type `FHIRPrimitiveExtension` """
        
        self.display = None
        """ Display for the code.
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        self.equivalence = None
        """ relatedto | equivalent | equal | wider | subsumes | narrower |
        specializes | inexact | unmatched | disjoint.
        Type `str`. """
        self._equivalence = None
        """ Primitive extension for equivalence. Type `FHIRPrimitiveExtension` """
        
        self.product = None
        """ Other concepts that this mapping also produces.
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        self._product = None
        """ Primitive extension for product. Type `FHIRPrimitiveExtension` """
        
        super(ConceptMapGroupElementTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElementTarget, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dependsOn", "dependsOn", ConceptMapGroupElementTargetDependsOn, True, None, False),
            ("_dependsOn", "_dependsOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("equivalence", "equivalence", str, False, None, True),
            ("_equivalence", "_equivalence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("product", "product", ConceptMapGroupElementTargetDependsOn, True, None, False),
            ("_product", "_product", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        
        self.display = None
        """ Display for the code (if value is a code).
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        self.property = None
        """ Reference to property mapping depends on.
        Type `str`. """
        self._property = None
        """ Primitive extension for property. Type `FHIRPrimitiveExtension` """
        
        self.system = None
        """ Code System (if necessary).
        Type `str`. """
        self._system = None
        """ Primitive extension for system. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ Value of the referenced element.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(ConceptMapGroupElementTargetDependsOn, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("property", "property", str, False, None, True),
            ("_property", "_property", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """ What to do when there is no mapping for the source concept.
    
    What to do when there is no mapping for the source concept. "Unmapped" does
    not include codes that are unmatched, and the unmapped element is ignored
    in a code is specified to have equivalence = unmatched.
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
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.display = None
        """ Display for the code.
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        self.mode = None
        """ provided | fixed | other-map.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ canonical reference to an additional ConceptMap to use for mapping
        if the source concept is unmapped.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(ConceptMapGroupUnmapped, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupUnmapped, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import identifier
from . import usagecontext