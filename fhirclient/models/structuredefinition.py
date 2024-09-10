# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/StructureDefinition).
# 2024, SMART Health IT.


from . import domainresource

class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.
    
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """
    
    resource_type = "StructureDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abstract = None
        """ Whether the structure is abstract.
        Type `bool`. """
        self._abstract = None
        """ Primitive extension for abstract. Type `FHIRPrimitiveExtension` """
        
        self.baseDefinition = None
        """ Definition that this type is constrained/specialized from.
        Type `str`. """
        self._baseDefinition = None
        """ Primitive extension for baseDefinition. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.context = None
        """ If an extension, where it can be used in instances.
        List of `StructureDefinitionContext` items (represented as `dict` in JSON). """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.contextInvariant = None
        """ FHIRPath invariants - when the extension can be used.
        List of `str` items. """
        self._contextInvariant = None
        """ Primitive extension for contextInvariant. Type `FHIRPrimitiveExtension` """
        
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
        
        self.derivation = None
        """ specialization | constraint - How relates to base definition.
        Type `str`. """
        self._derivation = None
        """ Primitive extension for derivation. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the structure definition.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.differential = None
        """ Differential view of the structure.
        Type `StructureDefinitionDifferential` (represented as `dict` in JSON). """
        self._differential = None
        """ Primitive extension for differential. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.fhirVersion = None
        """ FHIR Version this StructureDefinition targets.
        Type `str`. """
        self._fhirVersion = None
        """ Primitive extension for fhirVersion. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the structure definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for structure definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.keyword = None
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        self._keyword = None
        """ Primitive extension for keyword. Type `FHIRPrimitiveExtension` """
        
        self.kind = None
        """ primitive-type | complex-type | resource | logical.
        Type `str`. """
        self._kind = None
        """ Primitive extension for kind. Type `FHIRPrimitiveExtension` """
        
        self.mapping = None
        """ External specification that the content is mapped to.
        List of `StructureDefinitionMapping` items (represented as `dict` in JSON). """
        self._mapping = None
        """ Primitive extension for mapping. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this structure definition (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this structure definition is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.snapshot = None
        """ Snapshot view of the structure.
        Type `StructureDefinitionSnapshot` (represented as `dict` in JSON). """
        self._snapshot = None
        """ Primitive extension for snapshot. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this structure definition (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type defined or constrained by this structure.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this structure definition, represented as
        a URI (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the structure definition.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(StructureDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinition, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, True),
            ("_abstract", "_abstract", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("baseDefinition", "baseDefinition", str, False, None, False),
            ("_baseDefinition", "_baseDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("context", "context", StructureDefinitionContext, True, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contextInvariant", "contextInvariant", str, True, None, False),
            ("_contextInvariant", "_contextInvariant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("derivation", "derivation", str, False, None, False),
            ("_derivation", "_derivation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("differential", "differential", StructureDefinitionDifferential, False, None, False),
            ("_differential", "_differential", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, False),
            ("_fhirVersion", "_fhirVersion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("keyword", "keyword", coding.Coding, True, None, False),
            ("_keyword", "_keyword", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mapping", "mapping", StructureDefinitionMapping, True, None, False),
            ("_mapping", "_mapping", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("snapshot", "snapshot", StructureDefinitionSnapshot, False, None, False),
            ("_snapshot", "_snapshot", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class StructureDefinitionContext(backboneelement.BackboneElement):
    """ If an extension, where it can be used in instances.
    
    Identifies the types of resource or data type elements to which the
    extension can be applied.
    """
    
    resource_type = "StructureDefinitionContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ Where the extension can be used in instances.
        Type `str`. """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ fhirpath | element | extension.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(StructureDefinitionContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionContext, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, True),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """ Differential view of the structure.
    
    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """
    
    resource_type = "StructureDefinitionDifferential"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        self._element = None
        """ Primitive extension for element. Type `FHIRPrimitiveExtension` """
        
        super(StructureDefinitionDifferential, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionDifferential, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
            ("_element", "_element", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureDefinitionMapping(backboneelement.BackboneElement):
    """ External specification that the content is mapped to.
    
    An external specification that the content is mapped to.
    """
    
    resource_type = "StructureDefinitionMapping"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Versions, Issues, Scope limitations etc..
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.identity = None
        """ Internal id when this mapping is used.
        Type `str`. """
        self._identity = None
        """ Primitive extension for identity. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """
        self._uri = None
        """ Primitive extension for uri. Type `FHIRPrimitiveExtension` """
        
        super(StructureDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionMapping, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identity", "identity", str, False, None, True),
            ("_identity", "_identity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("uri", "uri", str, False, None, False),
            ("_uri", "_uri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """ Snapshot view of the structure.
    
    A snapshot view is expressed in a standalone form that can be used and
    interpreted without considering the base StructureDefinition.
    """
    
    resource_type = "StructureDefinitionSnapshot"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        self._element = None
        """ Primitive extension for element. Type `FHIRPrimitiveExtension` """
        
        super(StructureDefinitionSnapshot, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionSnapshot, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
            ("_element", "_element", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import contactdetail
from . import elementdefinition
from . import fhirdatetime
from . import identifier
from . import usagecontext