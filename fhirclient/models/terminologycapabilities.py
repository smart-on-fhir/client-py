# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities).
# 2024, SMART Health IT.


from . import domainresource

class TerminologyCapabilities(domainresource.DomainResource):
    """ A statement of system capabilities.
    
    A TerminologyCapabilities resource documents a set of capabilities
    (behaviors) of a FHIR Terminology Server that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
    """
    
    resource_type = "TerminologyCapabilities"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.closure = None
        """ Information about the [ConceptMap/$closure](conceptmap-operation-
        closure.html) operation.
        Type `TerminologyCapabilitiesClosure` (represented as `dict` in JSON). """
        self._closure = None
        """ Primitive extension for closure. Type `FHIRPrimitiveExtension` """
        
        self.codeSearch = None
        """ explicit | all.
        Type `str`. """
        self._codeSearch = None
        """ Primitive extension for codeSearch. Type `FHIRPrimitiveExtension` """
        
        self.codeSystem = None
        """ A code system supported by the server.
        List of `TerminologyCapabilitiesCodeSystem` items (represented as `dict` in JSON). """
        self._codeSystem = None
        """ Primitive extension for codeSystem. Type `FHIRPrimitiveExtension` """
        
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
        """ Natural language description of the terminology capabilities.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.expansion = None
        """ Information about the [ValueSet/$expand](valueset-operation-
        expand.html) operation.
        Type `TerminologyCapabilitiesExpansion` (represented as `dict` in JSON). """
        self._expansion = None
        """ Primitive extension for expansion. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.implementation = None
        """ If this describes a specific instance.
        Type `TerminologyCapabilitiesImplementation` (represented as `dict` in JSON). """
        self._implementation = None
        """ Primitive extension for implementation. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for terminology capabilities (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.kind = None
        """ instance | capability | requirements.
        Type `str`. """
        self._kind = None
        """ Primitive extension for kind. Type `FHIRPrimitiveExtension` """
        
        self.lockedDate = None
        """ Whether lockedDate is supported.
        Type `bool`. """
        self._lockedDate = None
        """ Primitive extension for lockedDate. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this terminology capabilities (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this terminology capabilities is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.software = None
        """ Software that is covered by this terminology capability statement.
        Type `TerminologyCapabilitiesSoftware` (represented as `dict` in JSON). """
        self._software = None
        """ Primitive extension for software. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this terminology capabilities (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.translation = None
        """ Information about the [ConceptMap/$translate](conceptmap-operation-
        translate.html) operation.
        Type `TerminologyCapabilitiesTranslation` (represented as `dict` in JSON). """
        self._translation = None
        """ Primitive extension for translation. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this terminology capabilities, represented
        as a URI (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.validateCode = None
        """ Information about the [ValueSet/$validate-code](valueset-operation-
        validate-code.html) operation.
        Type `TerminologyCapabilitiesValidateCode` (represented as `dict` in JSON). """
        self._validateCode = None
        """ Primitive extension for validateCode. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the terminology capabilities.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilities, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilities, self).elementProperties()
        js.extend([
            ("closure", "closure", TerminologyCapabilitiesClosure, False, None, False),
            ("_closure", "_closure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("codeSearch", "codeSearch", str, False, None, False),
            ("_codeSearch", "_codeSearch", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("codeSystem", "codeSystem", TerminologyCapabilitiesCodeSystem, True, None, False),
            ("_codeSystem", "_codeSystem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, True),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expansion", "expansion", TerminologyCapabilitiesExpansion, False, None, False),
            ("_expansion", "_expansion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("implementation", "implementation", TerminologyCapabilitiesImplementation, False, None, False),
            ("_implementation", "_implementation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lockedDate", "lockedDate", bool, False, None, False),
            ("_lockedDate", "_lockedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("software", "software", TerminologyCapabilitiesSoftware, False, None, False),
            ("_software", "_software", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("translation", "translation", TerminologyCapabilitiesTranslation, False, None, False),
            ("_translation", "_translation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("validateCode", "validateCode", TerminologyCapabilitiesValidateCode, False, None, False),
            ("_validateCode", "_validateCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class TerminologyCapabilitiesClosure(backboneelement.BackboneElement):
    """ Information about the [ConceptMap/$closure](conceptmap-operation-
    closure.html) operation.
    
    Whether the $closure operation is supported.
    """
    
    resource_type = "TerminologyCapabilitiesClosure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.translation = None
        """ If cross-system closure is supported.
        Type `bool`. """
        self._translation = None
        """ Primitive extension for translation. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesClosure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesClosure, self).elementProperties()
        js.extend([
            ("translation", "translation", bool, False, None, False),
            ("_translation", "_translation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TerminologyCapabilitiesCodeSystem(backboneelement.BackboneElement):
    """ A code system supported by the server.
    
    Identifies a code system that is supported by the server. If there is a no
    code system URL, then this declares the general assumptions a client can
    make about support for any CodeSystem resource.
    """
    
    resource_type = "TerminologyCapabilitiesCodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.subsumption = None
        """ Whether subsumption is supported.
        Type `bool`. """
        self._subsumption = None
        """ Primitive extension for subsumption. Type `FHIRPrimitiveExtension` """
        
        self.uri = None
        """ URI for the Code System.
        Type `str`. """
        self._uri = None
        """ Primitive extension for uri. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Version of Code System supported.
        List of `TerminologyCapabilitiesCodeSystemVersion` items (represented as `dict` in JSON). """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesCodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystem, self).elementProperties()
        js.extend([
            ("subsumption", "subsumption", bool, False, None, False),
            ("_subsumption", "_subsumption", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("uri", "uri", str, False, None, False),
            ("_uri", "_uri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", TerminologyCapabilitiesCodeSystemVersion, True, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TerminologyCapabilitiesCodeSystemVersion(backboneelement.BackboneElement):
    """ Version of Code System supported.
    
    For the code system, a list of versions that are supported by the server.
    """
    
    resource_type = "TerminologyCapabilitiesCodeSystemVersion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Version identifier for this version.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.compositional = None
        """ If compositional grammar is supported.
        Type `bool`. """
        self._compositional = None
        """ Primitive extension for compositional. Type `FHIRPrimitiveExtension` """
        
        self.filter = None
        """ Filter Properties supported.
        List of `TerminologyCapabilitiesCodeSystemVersionFilter` items (represented as `dict` in JSON). """
        self._filter = None
        """ Primitive extension for filter. Type `FHIRPrimitiveExtension` """
        
        self.isDefault = None
        """ If this is the default version for this code system.
        Type `bool`. """
        self._isDefault = None
        """ Primitive extension for isDefault. Type `FHIRPrimitiveExtension` """
        
        self.language = None
        """ Language Displays supported.
        List of `str` items. """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        self.property = None
        """ Properties supported for $lookup.
        List of `str` items. """
        self._property = None
        """ Primitive extension for property. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesCodeSystemVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersion, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("_compositional", "_compositional", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("filter", "filter", TerminologyCapabilitiesCodeSystemVersionFilter, True, None, False),
            ("_filter", "_filter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("isDefault", "isDefault", bool, False, None, False),
            ("_isDefault", "_isDefault", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("language", "language", str, True, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("property", "property", str, True, None, False),
            ("_property", "_property", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TerminologyCapabilitiesCodeSystemVersionFilter(backboneelement.BackboneElement):
    """ Filter Properties supported.
    """
    
    resource_type = "TerminologyCapabilitiesCodeSystemVersionFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code of the property supported.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.op = None
        """ Operations supported for the property.
        List of `str` items. """
        self._op = None
        """ Primitive extension for op. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesCodeSystemVersionFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersionFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("op", "op", str, True, None, True),
            ("_op", "_op", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TerminologyCapabilitiesExpansion(backboneelement.BackboneElement):
    """ Information about the [ValueSet/$expand](valueset-operation-expand.html)
    operation.
    """
    
    resource_type = "TerminologyCapabilitiesExpansion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.hierarchical = None
        """ Whether the server can return nested value sets.
        Type `bool`. """
        self._hierarchical = None
        """ Primitive extension for hierarchical. Type `FHIRPrimitiveExtension` """
        
        self.incomplete = None
        """ Allow request for incomplete expansions?.
        Type `bool`. """
        self._incomplete = None
        """ Primitive extension for incomplete. Type `FHIRPrimitiveExtension` """
        
        self.paging = None
        """ Whether the server supports paging on expansion.
        Type `bool`. """
        self._paging = None
        """ Primitive extension for paging. Type `FHIRPrimitiveExtension` """
        
        self.parameter = None
        """ Supported expansion parameter.
        List of `TerminologyCapabilitiesExpansionParameter` items (represented as `dict` in JSON). """
        self._parameter = None
        """ Primitive extension for parameter. Type `FHIRPrimitiveExtension` """
        
        self.textFilter = None
        """ Documentation about text searching works.
        Type `str`. """
        self._textFilter = None
        """ Primitive extension for textFilter. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesExpansion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansion, self).elementProperties()
        js.extend([
            ("hierarchical", "hierarchical", bool, False, None, False),
            ("_hierarchical", "_hierarchical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("incomplete", "incomplete", bool, False, None, False),
            ("_incomplete", "_incomplete", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paging", "paging", bool, False, None, False),
            ("_paging", "_paging", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parameter", "parameter", TerminologyCapabilitiesExpansionParameter, True, None, False),
            ("_parameter", "_parameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("textFilter", "textFilter", str, False, None, False),
            ("_textFilter", "_textFilter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TerminologyCapabilitiesExpansionParameter(backboneelement.BackboneElement):
    """ Supported expansion parameter.
    """
    
    resource_type = "TerminologyCapabilitiesExpansionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ Description of support for parameter.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Expansion Parameter name.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesExpansionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansionParameter, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TerminologyCapabilitiesImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.
    
    Identifies a specific implementation instance that is described by the
    terminology capability statement - i.e. a particular installation, rather
    than the capabilities of a software program.
    """
    
    resource_type = "TerminologyCapabilitiesImplementation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Describes this specific instance.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Base URL for the implementation.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesImplementation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesImplementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TerminologyCapabilitiesSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this terminology capability statement.
    
    Software that is covered by this terminology capability statement.  It is
    used when the statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    
    resource_type = "TerminologyCapabilitiesSoftware"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ A name the software is known by.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Version covered by this statement.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesSoftware, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TerminologyCapabilitiesTranslation(backboneelement.BackboneElement):
    """ Information about the [ConceptMap/$translate](conceptmap-operation-
    translate.html) operation.
    """
    
    resource_type = "TerminologyCapabilitiesTranslation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.needsMap = None
        """ Whether the client must identify the map.
        Type `bool`. """
        self._needsMap = None
        """ Primitive extension for needsMap. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesTranslation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesTranslation, self).elementProperties()
        js.extend([
            ("needsMap", "needsMap", bool, False, None, True),
            ("_needsMap", "_needsMap", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TerminologyCapabilitiesValidateCode(backboneelement.BackboneElement):
    """ Information about the [ValueSet/$validate-code](valueset-operation-
    validate-code.html) operation.
    """
    
    resource_type = "TerminologyCapabilitiesValidateCode"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.translations = None
        """ Whether translations are validated.
        Type `bool`. """
        self._translations = None
        """ Primitive extension for translations. Type `FHIRPrimitiveExtension` """
        
        super(TerminologyCapabilitiesValidateCode, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesValidateCode, self).elementProperties()
        js.extend([
            ("translations", "translations", bool, False, None, True),
            ("_translations", "_translations", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import usagecontext