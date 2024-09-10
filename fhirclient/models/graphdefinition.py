# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/GraphDefinition).
# 2024, SMART Health IT.


from . import domainresource

class GraphDefinition(domainresource.DomainResource):
    """ Definition of a graph of resources.
    
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """
    
    resource_type = "GraphDefinition"
    
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
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the graph definition.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for graph definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.link = None
        """ Links this graph makes rules about.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        self._link = None
        """ Primitive extension for link. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this graph definition (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ Profile on base resource.
        Type `str`. """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this graph definition is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.start = None
        """ Type of resource at which the graph starts.
        Type `str`. """
        self._start = None
        """ Primitive extension for start. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this graph definition, represented as a
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
        """ Business version of the graph definition.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(GraphDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinition, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("_link", "_link", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("start", "start", str, False, None, True),
            ("_start", "_start", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class GraphDefinitionLink(backboneelement.BackboneElement):
    """ Links this graph makes rules about.
    """
    
    resource_type = "GraphDefinitionLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Why this link is specified.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.max = None
        """ Maximum occurrences for this link.
        Type `str`. """
        self._max = None
        """ Primitive extension for max. Type `FHIRPrimitiveExtension` """
        
        self.min = None
        """ Minimum occurrences for this link.
        Type `int`. """
        self._min = None
        """ Primitive extension for min. Type `FHIRPrimitiveExtension` """
        
        self.path = None
        """ Path in the resource that contains the link.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        self.sliceName = None
        """ Which slice (if profiled).
        Type `str`. """
        self._sliceName = None
        """ Primitive extension for sliceName. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Potential target for the link.
        List of `GraphDefinitionLinkTarget` items (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        super(GraphDefinitionLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLink, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("max", "max", str, False, None, False),
            ("_max", "_max", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("min", "min", int, False, None, False),
            ("_min", "_min", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("path", "path", str, False, None, False),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("_sliceName", "_sliceName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", GraphDefinitionLinkTarget, True, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class GraphDefinitionLinkTarget(backboneelement.BackboneElement):
    """ Potential target for the link.
    """
    
    resource_type = "GraphDefinitionLinkTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compartment = None
        """ Compartment Consistency Rules.
        List of `GraphDefinitionLinkTargetCompartment` items (represented as `dict` in JSON). """
        self._compartment = None
        """ Primitive extension for compartment. Type `FHIRPrimitiveExtension` """
        
        self.link = None
        """ Additional links from target resource.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        self._link = None
        """ Primitive extension for link. Type `FHIRPrimitiveExtension` """
        
        self.params = None
        """ Criteria for reverse lookup.
        Type `str`. """
        self._params = None
        """ Primitive extension for params. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ Profile for the target resource.
        Type `str`. """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of resource this link refers to.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(GraphDefinitionLinkTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLinkTarget, self).elementProperties()
        js.extend([
            ("compartment", "compartment", GraphDefinitionLinkTargetCompartment, True, None, False),
            ("_compartment", "_compartment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("_link", "_link", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("params", "params", str, False, None, False),
            ("_params", "_params", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class GraphDefinitionLinkTargetCompartment(backboneelement.BackboneElement):
    """ Compartment Consistency Rules.
    """
    
    resource_type = "GraphDefinitionLinkTargetCompartment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Patient | Encounter | RelatedPerson | Practitioner | Device.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Documentation for FHIRPath expression.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.expression = None
        """ Custom rule, as a FHIRPath expression.
        Type `str`. """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.rule = None
        """ identical | matching | different | custom.
        Type `str`. """
        self._rule = None
        """ Primitive extension for rule. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ condition | requirement.
        Type `str`. """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        super(GraphDefinitionLinkTargetCompartment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLinkTargetCompartment, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rule", "rule", str, False, None, True),
            ("_rule", "_rule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", str, False, None, True),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import usagecontext