# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/OperationDefinition).
# 2024, SMART Health IT.


from . import domainresource

class OperationDefinition(domainresource.DomainResource):
    """ Definition of an operation or a named query.
    
    A formal computable definition of an operation (on the RESTful interface)
    or a named query (using the search interaction).
    """
    
    resource_type = "OperationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.affectsState = None
        """ Whether content is changed by the operation.
        Type `bool`. """
        self._affectsState = None
        """ Primitive extension for affectsState. Type `FHIRPrimitiveExtension` """
        
        self.base = None
        """ Marks this as a profile of the base.
        Type `str`. """
        self._base = None
        """ Primitive extension for base. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Name used to invoke the operation.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Additional information about use.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
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
        """ Natural language description of the operation definition.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.inputProfile = None
        """ Validation information for in parameters.
        Type `str`. """
        self._inputProfile = None
        """ Primitive extension for inputProfile. Type `FHIRPrimitiveExtension` """
        
        self.instance = None
        """ Invoke on an instance?.
        Type `bool`. """
        self._instance = None
        """ Primitive extension for instance. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for operation definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.kind = None
        """ operation | query.
        Type `str`. """
        self._kind = None
        """ Primitive extension for kind. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this operation definition (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.outputProfile = None
        """ Validation information for out parameters.
        Type `str`. """
        self._outputProfile = None
        """ Primitive extension for outputProfile. Type `FHIRPrimitiveExtension` """
        
        self.overload = None
        """ Define overloaded variants for when  generating code.
        List of `OperationDefinitionOverload` items (represented as `dict` in JSON). """
        self._overload = None
        """ Primitive extension for overload. Type `FHIRPrimitiveExtension` """
        
        self.parameter = None
        """ Parameters for the operation/query.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        self._parameter = None
        """ Primitive extension for parameter. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this operation definition is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ Types this operation applies to.
        List of `str` items. """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.system = None
        """ Invoke at the system level?.
        Type `bool`. """
        self._system = None
        """ Primitive extension for system. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this operation definition (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Invoke at the type level?.
        Type `bool`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this operation definition, represented as
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
        """ Business version of the operation definition.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(OperationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("affectsState", "affectsState", bool, False, None, False),
            ("_affectsState", "_affectsState", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("base", "base", str, False, None, False),
            ("_base", "_base", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("inputProfile", "inputProfile", str, False, None, False),
            ("_inputProfile", "_inputProfile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instance", "instance", bool, False, None, True),
            ("_instance", "_instance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outputProfile", "outputProfile", str, False, None, False),
            ("_outputProfile", "_outputProfile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("overload", "overload", OperationDefinitionOverload, True, None, False),
            ("_overload", "_overload", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parameter", "parameter", OperationDefinitionParameter, True, None, False),
            ("_parameter", "_parameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", str, True, None, False),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("system", "system", bool, False, None, True),
            ("_system", "_system", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", bool, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class OperationDefinitionOverload(backboneelement.BackboneElement):
    """ Define overloaded variants for when  generating code.
    
    Defines an appropriate combination of parameters to use when invoking this
    operation, to help code generators when generating overloaded parameter
    sets for this operation.
    """
    
    resource_type = "OperationDefinitionOverload"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Comments to go on overload.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.parameterName = None
        """ Name of parameter to include in overload.
        List of `str` items. """
        self._parameterName = None
        """ Primitive extension for parameterName. Type `FHIRPrimitiveExtension` """
        
        super(OperationDefinitionOverload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionOverload, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parameterName", "parameterName", str, True, None, False),
            ("_parameterName", "_parameterName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class OperationDefinitionParameter(backboneelement.BackboneElement):
    """ Parameters for the operation/query.
    
    The parameters for the operation/query.
    """
    
    resource_type = "OperationDefinitionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `OperationDefinitionParameterBinding` (represented as `dict` in JSON). """
        self._binding = None
        """ Primitive extension for binding. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Description of meaning/use.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        self._max = None
        """ Primitive extension for max. Type `FHIRPrimitiveExtension` """
        
        self.min = None
        """ Minimum Cardinality.
        Type `int`. """
        self._min = None
        """ Primitive extension for min. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name in Parameters.parameter.name or in URL.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.part = None
        """ Parts of a nested Parameter.
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        self._part = None
        """ Primitive extension for part. Type `FHIRPrimitiveExtension` """
        
        self.referencedFrom = None
        """ References to this parameter.
        List of `OperationDefinitionParameterReferencedFrom` items (represented as `dict` in JSON). """
        self._referencedFrom = None
        """ Primitive extension for referencedFrom. Type `FHIRPrimitiveExtension` """
        
        self.searchType = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """
        self._searchType = None
        """ Primitive extension for searchType. Type `FHIRPrimitiveExtension` """
        
        self.targetProfile = None
        """ If type is Reference | canonical, allowed targets.
        List of `str` items. """
        self._targetProfile = None
        """ Primitive extension for targetProfile. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ What type this parameter has.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ in | out.
        Type `str`. """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        super(OperationDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("binding", "binding", OperationDefinitionParameterBinding, False, None, False),
            ("_binding", "_binding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("max", "max", str, False, None, True),
            ("_max", "_max", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("min", "min", int, False, None, True),
            ("_min", "_min", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("part", "part", OperationDefinitionParameter, True, None, False),
            ("_part", "_part", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referencedFrom", "referencedFrom", OperationDefinitionParameterReferencedFrom, True, None, False),
            ("_referencedFrom", "_referencedFrom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("searchType", "searchType", str, False, None, False),
            ("_searchType", "_searchType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("_targetProfile", "_targetProfile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", str, False, None, True),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this parameter is coded (code, Coding,
    CodeableConcept).
    """
    
    resource_type = "OperationDefinitionParameterBinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.strength = None
        """ required | extensible | preferred | example.
        Type `str`. """
        self._strength = None
        """ Primitive extension for strength. Type `FHIRPrimitiveExtension` """
        
        self.valueSet = None
        """ Source of value set.
        Type `str`. """
        self._valueSet = None
        """ Primitive extension for valueSet. Type `FHIRPrimitiveExtension` """
        
        super(OperationDefinitionParameterBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameterBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", str, False, None, True),
            ("_strength", "_strength", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSet", "valueSet", str, False, None, True),
            ("_valueSet", "_valueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class OperationDefinitionParameterReferencedFrom(backboneelement.BackboneElement):
    """ References to this parameter.
    
    Identifies other resource parameters within the operation invocation that
    are expected to resolve to this resource.
    """
    
    resource_type = "OperationDefinitionParameterReferencedFrom"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.source = None
        """ Referencing parameter.
        Type `str`. """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.sourceId = None
        """ Element id of reference.
        Type `str`. """
        self._sourceId = None
        """ Primitive extension for sourceId. Type `FHIRPrimitiveExtension` """
        
        super(OperationDefinitionParameterReferencedFrom, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameterReferencedFrom, self).elementProperties()
        js.extend([
            ("source", "source", str, False, None, True),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("_sourceId", "_sourceId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import usagecontext