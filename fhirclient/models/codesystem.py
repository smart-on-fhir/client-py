# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CodeSystem).
# 2024, SMART Health IT.


from . import domainresource

class CodeSystem(domainresource.DomainResource):
    """ Declares the existence of and describes a code system or code system
    supplement.
    
    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and
    optionally define a part or all of its content.
    """
    
    resource_type = "CodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.caseSensitive = None
        """ If code comparison is case sensitive.
        Type `bool`. """
        self._caseSensitive = None
        """ Primitive extension for caseSensitive. Type `FHIRPrimitiveExtension` """
        
        self.compositional = None
        """ If code system defines a compositional grammar.
        Type `bool`. """
        self._compositional = None
        """ Primitive extension for compositional. Type `FHIRPrimitiveExtension` """
        
        self.concept = None
        """ Concepts in the code system.
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """
        self._concept = None
        """ Primitive extension for concept. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.content = None
        """ not-present | example | fragment | complete | supplement.
        Type `str`. """
        self._content = None
        """ Primitive extension for content. Type `FHIRPrimitiveExtension` """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        self._copyright = None
        """ Primitive extension for copyright. Type `FHIRPrimitiveExtension` """
        
        self.count = None
        """ Total concepts in the code system.
        Type `int`. """
        self._count = None
        """ Primitive extension for count. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the code system.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.filter = None
        """ Filter that can be used in a value set.
        List of `CodeSystemFilter` items (represented as `dict` in JSON). """
        self._filter = None
        """ Primitive extension for filter. Type `FHIRPrimitiveExtension` """
        
        self.hierarchyMeaning = None
        """ grouped-by | is-a | part-of | classified-with.
        Type `str`. """
        self._hierarchyMeaning = None
        """ Primitive extension for hierarchyMeaning. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the code system (business identifier).
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for code system (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this code system (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.property = None
        """ Additional information supplied about each concept.
        List of `CodeSystemProperty` items (represented as `dict` in JSON). """
        self._property = None
        """ Primitive extension for property. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this code system is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.supplements = None
        """ Canonical URL of Code System this adds designations and properties
        to.
        Type `str`. """
        self._supplements = None
        """ Primitive extension for supplements. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this code system (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this code system, represented as a URI
        (globally unique) (Coding.system).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.valueSet = None
        """ Canonical reference to the value set with entire code system.
        Type `str`. """
        self._valueSet = None
        """ Primitive extension for valueSet. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the code system (Coding.version).
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        self.versionNeeded = None
        """ If definitions are not stable.
        Type `bool`. """
        self._versionNeeded = None
        """ Primitive extension for versionNeeded. Type `FHIRPrimitiveExtension` """
        
        super(CodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystem, self).elementProperties()
        js.extend([
            ("caseSensitive", "caseSensitive", bool, False, None, False),
            ("_caseSensitive", "_caseSensitive", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("_compositional", "_compositional", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("_concept", "_concept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("content", "content", str, False, None, True),
            ("_content", "_content", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("count", "count", int, False, None, False),
            ("_count", "_count", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("filter", "filter", CodeSystemFilter, True, None, False),
            ("_filter", "_filter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("hierarchyMeaning", "hierarchyMeaning", str, False, None, False),
            ("_hierarchyMeaning", "_hierarchyMeaning", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("property", "property", CodeSystemProperty, True, None, False),
            ("_property", "_property", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supplements", "supplements", str, False, None, False),
            ("_supplements", "_supplements", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
            ("_valueSet", "_valueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("versionNeeded", "versionNeeded", bool, False, None, False),
            ("_versionNeeded", "_versionNeeded", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class CodeSystemConcept(backboneelement.BackboneElement):
    """ Concepts in the code system.
    
    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meanings of the hierarchical relationships are.
    """
    
    resource_type = "CodeSystemConcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code that identifies concept.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.concept = None
        """ Child Concepts (is-a/contains/categorizes).
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """
        self._concept = None
        """ Primitive extension for concept. Type `FHIRPrimitiveExtension` """
        
        self.definition = None
        """ Formal definition.
        Type `str`. """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.designation = None
        """ Additional representations for the concept.
        List of `CodeSystemConceptDesignation` items (represented as `dict` in JSON). """
        self._designation = None
        """ Primitive extension for designation. Type `FHIRPrimitiveExtension` """
        
        self.display = None
        """ Text to display to the user.
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        self.property = None
        """ Property value for the concept.
        List of `CodeSystemConceptProperty` items (represented as `dict` in JSON). """
        self._property = None
        """ Primitive extension for property. Type `FHIRPrimitiveExtension` """
        
        super(CodeSystemConcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("_concept", "_concept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("designation", "designation", CodeSystemConceptDesignation, True, None, False),
            ("_designation", "_designation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("property", "property", CodeSystemConceptProperty, True, None, False),
            ("_property", "_property", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for the concept.
    
    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """
    
    resource_type = "CodeSystemConceptDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ Human language of the designation.
        Type `str`. """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ Details how this designation would be used.
        Type `Coding` (represented as `dict` in JSON). """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The text value for this designation.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(CodeSystemConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """ Property value for the concept.
    
    A property value for this concept.
    """
    
    resource_type = "CodeSystemConceptProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Reference to CodeSystem.property.code.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Value of the property for this concept.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCode = None
        """ Value of the property for this concept.
        Type `str`. """
        self._valueCode = None
        """ Primitive extension for valueCode. Type `FHIRPrimitiveExtension` """
        
        self.valueCoding = None
        """ Value of the property for this concept.
        Type `Coding` (represented as `dict` in JSON). """
        self._valueCoding = None
        """ Primitive extension for valueCoding. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ Value of the property for this concept.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ Value of the property for this concept.
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Value of the property for this concept.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Value of the property for this concept.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        super(CodeSystemConceptProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemConceptProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCode", "valueCode", str, False, "value", True),
            ("_valueCode", "_valueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("_valueCoding", "_valueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", True),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CodeSystemFilter(backboneelement.BackboneElement):
    """ Filter that can be used in a value set.
    
    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """
    
    resource_type = "CodeSystemFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code that identifies the filter.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ How or why the filter is used.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.operator = None
        """ = | is-a | descendent-of | is-not-a | regex | in | not-in |
        generalizes | exists.
        List of `str` items. """
        self._operator = None
        """ Primitive extension for operator. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ What to use for the value.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(CodeSystemFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operator", "operator", str, True, None, True),
            ("_operator", "_operator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CodeSystemProperty(backboneelement.BackboneElement):
    """ Additional information supplied about each concept.
    
    A property defines an additional slot through which additional information
    can be provided about a concept.
    """
    
    resource_type = "CodeSystemProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Identifies the property on the concepts, and when referred to in
        operations.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Why the property is defined, and/or what it conveys.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ code | Coding | string | integer | boolean | dateTime | decimal.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.uri = None
        """ Formal identifier for the property.
        Type `str`. """
        self._uri = None
        """ Primitive extension for uri. Type `FHIRPrimitiveExtension` """
        
        super(CodeSystemProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("uri", "uri", str, False, None, False),
            ("_uri", "_uri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdatetime
from . import identifier
from . import usagecontext