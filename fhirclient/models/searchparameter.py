# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SearchParameter).
# 2024, SMART Health IT.


from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ Search parameter for a resource.
    
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    
    resource_type = "SearchParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.base = None
        """ The resource type(s) this search parameter applies to.
        List of `str` items. """
        self._base = None
        """ Primitive extension for base. Type `FHIRPrimitiveExtension` """
        
        self.chain = None
        """ Chained names supported.
        List of `str` items. """
        self._chain = None
        """ Primitive extension for chain. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Code used in URL.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.comparator = None
        """ eq | ne | gt | lt | ge | le | sa | eb | ap.
        List of `str` items. """
        self._comparator = None
        """ Primitive extension for comparator. Type `FHIRPrimitiveExtension` """
        
        self.component = None
        """ For Composite resources to define the parts.
        List of `SearchParameterComponent` items (represented as `dict` in JSON). """
        self._component = None
        """ Primitive extension for component. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.derivedFrom = None
        """ Original definition for the search parameter.
        Type `str`. """
        self._derivedFrom = None
        """ Primitive extension for derivedFrom. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the search parameter.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.expression = None
        """ FHIRPath expression that extracts the values.
        Type `str`. """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for search parameter (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ missing | exact | contains | not | text | in | not-in | below |
        above | type | identifier | ofType.
        List of `str` items. """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        self.multipleAnd = None
        """ Allow multiple parameters (and).
        Type `bool`. """
        self._multipleAnd = None
        """ Primitive extension for multipleAnd. Type `FHIRPrimitiveExtension` """
        
        self.multipleOr = None
        """ Allow multiple values per parameter (or).
        Type `bool`. """
        self._multipleOr = None
        """ Primitive extension for multipleOr. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this search parameter (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this search parameter is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this search parameter, represented as a
        URI (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the search parameter.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        self.xpath = None
        """ XPath that extracts the values.
        Type `str`. """
        self._xpath = None
        """ Primitive extension for xpath. Type `FHIRPrimitiveExtension` """
        
        self.xpathUsage = None
        """ normal | phonetic | nearby | distance | other.
        Type `str`. """
        self._xpathUsage = None
        """ Primitive extension for xpathUsage. Type `FHIRPrimitiveExtension` """
        
        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("base", "base", str, True, None, True),
            ("_base", "_base", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("chain", "chain", str, True, None, False),
            ("_chain", "_chain", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comparator", "comparator", str, True, None, False),
            ("_comparator", "_comparator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("component", "component", SearchParameterComponent, True, None, False),
            ("_component", "_component", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("derivedFrom", "derivedFrom", str, False, None, False),
            ("_derivedFrom", "_derivedFrom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, True),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", str, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("multipleAnd", "multipleAnd", bool, False, None, False),
            ("_multipleAnd", "_multipleAnd", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("multipleOr", "multipleOr", bool, False, None, False),
            ("_multipleOr", "_multipleOr", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", str, True, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("_xpath", "_xpath", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("xpathUsage", "xpathUsage", str, False, None, False),
            ("_xpathUsage", "_xpathUsage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class SearchParameterComponent(backboneelement.BackboneElement):
    """ For Composite resources to define the parts.
    
    Used to define the parts of a composite search parameter.
    """
    
    resource_type = "SearchParameterComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ Defines how the part works.
        Type `str`. """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.expression = None
        """ Subexpression relative to main expression.
        Type `str`. """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expression", "expression", str, False, None, True),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import usagecontext