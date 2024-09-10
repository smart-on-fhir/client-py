# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CapabilityStatement).
# 2024, SMART Health IT.


from . import domainresource

class CapabilityStatement(domainresource.DomainResource):
    """ A statement of system capabilities.
    
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server for a particular version of FHIR that may be used as a
    statement of actual server functionality or a statement of required or
    desired server implementation.
    """
    
    resource_type = "CapabilityStatement"
    
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
        """ Natural language description of the capability statement.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.document = None
        """ Document definition.
        List of `CapabilityStatementDocument` items (represented as `dict` in JSON). """
        self._document = None
        """ Primitive extension for document. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.fhirVersion = None
        """ FHIR Version the system supports.
        Type `str`. """
        self._fhirVersion = None
        """ Primitive extension for fhirVersion. Type `FHIRPrimitiveExtension` """
        
        self.format = None
        """ formats supported (xml | json | ttl | mime type).
        List of `str` items. """
        self._format = None
        """ Primitive extension for format. Type `FHIRPrimitiveExtension` """
        
        self.implementation = None
        """ If this describes a specific instance.
        Type `CapabilityStatementImplementation` (represented as `dict` in JSON). """
        self._implementation = None
        """ Primitive extension for implementation. Type `FHIRPrimitiveExtension` """
        
        self.implementationGuide = None
        """ Implementation guides supported.
        List of `str` items. """
        self._implementationGuide = None
        """ Primitive extension for implementationGuide. Type `FHIRPrimitiveExtension` """
        
        self.imports = None
        """ Canonical URL of another capability statement this adds to.
        List of `str` items. """
        self._imports = None
        """ Primitive extension for imports. Type `FHIRPrimitiveExtension` """
        
        self.instantiates = None
        """ Canonical URL of another capability statement this implements.
        List of `str` items. """
        self._instantiates = None
        """ Primitive extension for instantiates. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for capability statement (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.kind = None
        """ instance | capability | requirements.
        Type `str`. """
        self._kind = None
        """ Primitive extension for kind. Type `FHIRPrimitiveExtension` """
        
        self.messaging = None
        """ If messaging is supported.
        List of `CapabilityStatementMessaging` items (represented as `dict` in JSON). """
        self._messaging = None
        """ Primitive extension for messaging. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this capability statement (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.patchFormat = None
        """ Patch formats supported.
        List of `str` items. """
        self._patchFormat = None
        """ Primitive extension for patchFormat. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this capability statement is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.rest = None
        """ If the endpoint is a RESTful one.
        List of `CapabilityStatementRest` items (represented as `dict` in JSON). """
        self._rest = None
        """ Primitive extension for rest. Type `FHIRPrimitiveExtension` """
        
        self.software = None
        """ Software that is covered by this capability statement.
        Type `CapabilityStatementSoftware` (represented as `dict` in JSON). """
        self._software = None
        """ Primitive extension for software. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this capability statement (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this capability statement, represented as
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
        """ Business version of the capability statement.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, True),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("document", "document", CapabilityStatementDocument, True, None, False),
            ("_document", "_document", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, True),
            ("_fhirVersion", "_fhirVersion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("format", "format", str, True, None, True),
            ("_format", "_format", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("implementation", "implementation", CapabilityStatementImplementation, False, None, False),
            ("_implementation", "_implementation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("implementationGuide", "implementationGuide", str, True, None, False),
            ("_implementationGuide", "_implementationGuide", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("imports", "imports", str, True, None, False),
            ("_imports", "_imports", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("_instantiates", "_instantiates", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("messaging", "messaging", CapabilityStatementMessaging, True, None, False),
            ("_messaging", "_messaging", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patchFormat", "patchFormat", str, True, None, False),
            ("_patchFormat", "_patchFormat", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rest", "rest", CapabilityStatementRest, True, None, False),
            ("_rest", "_rest", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("software", "software", CapabilityStatementSoftware, False, None, False),
            ("_software", "_software", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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

class CapabilityStatementDocument(backboneelement.BackboneElement):
    """ Document definition.
    
    A document definition.
    """
    
    resource_type = "CapabilityStatementDocument"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ Description of document support.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.mode = None
        """ producer | consumer.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ Constraint on the resources used in the document.
        Type `str`. """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementDocument, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementDocument, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", str, False, None, True),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.
    
    Identifies a specific implementation instance that is described by the
    capability statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    
    resource_type = "CapabilityStatementImplementation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.custodian = None
        """ Organization that manages the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._custodian = None
        """ Primitive extension for custodian. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Describes this specific instance.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Base URL for the installation.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementImplementation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementImplementation, self).elementProperties()
        js.extend([
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("_custodian", "_custodian", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, True),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementMessaging(backboneelement.BackboneElement):
    """ If messaging is supported.
    
    A description of the messaging capabilities of the solution.
    """
    
    resource_type = "CapabilityStatementMessaging"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ Messaging interface behavior details.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.endpoint = None
        """ Where messages should be sent.
        List of `CapabilityStatementMessagingEndpoint` items (represented as `dict` in JSON). """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.reliableCache = None
        """ Reliable Message Cache Length (min).
        Type `int`. """
        self._reliableCache = None
        """ Primitive extension for reliableCache. Type `FHIRPrimitiveExtension` """
        
        self.supportedMessage = None
        """ Messages supported by this system.
        List of `CapabilityStatementMessagingSupportedMessage` items (represented as `dict` in JSON). """
        self._supportedMessage = None
        """ Primitive extension for supportedMessage. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementMessaging, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessaging, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endpoint", "endpoint", CapabilityStatementMessagingEndpoint, True, None, False),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reliableCache", "reliableCache", int, False, None, False),
            ("_reliableCache", "_reliableCache", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportedMessage", "supportedMessage", CapabilityStatementMessagingSupportedMessage, True, None, False),
            ("_supportedMessage", "_supportedMessage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementMessagingEndpoint(backboneelement.BackboneElement):
    """ Where messages should be sent.
    
    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """
    
    resource_type = "CapabilityStatementMessagingEndpoint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Network address or identifier of the end-point.
        Type `str`. """
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.protocol = None
        """ http | ftp | mllp +.
        Type `Coding` (represented as `dict` in JSON). """
        self._protocol = None
        """ Primitive extension for protocol. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementMessagingEndpoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessagingEndpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, True),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("protocol", "protocol", coding.Coding, False, None, True),
            ("_protocol", "_protocol", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementMessagingSupportedMessage(backboneelement.BackboneElement):
    """ Messages supported by this system.
    
    References to message definitions for messages this system can send or
    receive.
    """
    
    resource_type = "CapabilityStatementMessagingSupportedMessage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ Message supported by this system.
        Type `str`. """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.mode = None
        """ sender | receiver.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementMessagingSupportedMessage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessagingSupportedMessage, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementRest(backboneelement.BackboneElement):
    """ If the endpoint is a RESTful one.
    
    A definition of the restful capabilities of the solution, if any.
    """
    
    resource_type = "CapabilityStatementRest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compartment = None
        """ Compartments served/used by system.
        List of `str` items. """
        self._compartment = None
        """ Primitive extension for compartment. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ General description of implementation.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.interaction = None
        """ What operations are supported?.
        List of `CapabilityStatementRestInteraction` items (represented as `dict` in JSON). """
        self._interaction = None
        """ Primitive extension for interaction. Type `FHIRPrimitiveExtension` """
        
        self.mode = None
        """ client | server.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.operation = None
        """ Definition of a system level operation.
        List of `CapabilityStatementRestResourceOperation` items (represented as `dict` in JSON). """
        self._operation = None
        """ Primitive extension for operation. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ Resource served on the REST interface.
        List of `CapabilityStatementRestResource` items (represented as `dict` in JSON). """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.searchParam = None
        """ Search parameters for searching all resources.
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        self._searchParam = None
        """ Primitive extension for searchParam. Type `FHIRPrimitiveExtension` """
        
        self.security = None
        """ Information about security of implementation.
        Type `CapabilityStatementRestSecurity` (represented as `dict` in JSON). """
        self._security = None
        """ Primitive extension for security. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementRest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRest, self).elementProperties()
        js.extend([
            ("compartment", "compartment", str, True, None, False),
            ("_compartment", "_compartment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("interaction", "interaction", CapabilityStatementRestInteraction, True, None, False),
            ("_interaction", "_interaction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
            ("_operation", "_operation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", CapabilityStatementRestResource, True, None, False),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("_searchParam", "_searchParam", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("security", "security", CapabilityStatementRestSecurity, False, None, False),
            ("_security", "_security", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementRestInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    A specification of restful operations supported by the system.
    """
    
    resource_type = "CapabilityStatementRestInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ transaction | batch | search-system | history-system.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementRestInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementRestResource(backboneelement.BackboneElement):
    """ Resource served on the REST interface.
    
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    
    resource_type = "CapabilityStatementRestResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conditionalCreate = None
        """ If allows/uses conditional create.
        Type `bool`. """
        self._conditionalCreate = None
        """ Primitive extension for conditionalCreate. Type `FHIRPrimitiveExtension` """
        
        self.conditionalDelete = None
        """ not-supported | single | multiple - how conditional delete is
        supported.
        Type `str`. """
        self._conditionalDelete = None
        """ Primitive extension for conditionalDelete. Type `FHIRPrimitiveExtension` """
        
        self.conditionalRead = None
        """ not-supported | modified-since | not-match | full-support.
        Type `str`. """
        self._conditionalRead = None
        """ Primitive extension for conditionalRead. Type `FHIRPrimitiveExtension` """
        
        self.conditionalUpdate = None
        """ If allows/uses conditional update.
        Type `bool`. """
        self._conditionalUpdate = None
        """ Primitive extension for conditionalUpdate. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Additional information about the use of the resource type.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.interaction = None
        """ What operations are supported?.
        List of `CapabilityStatementRestResourceInteraction` items (represented as `dict` in JSON). """
        self._interaction = None
        """ Primitive extension for interaction. Type `FHIRPrimitiveExtension` """
        
        self.operation = None
        """ Definition of a resource operation.
        List of `CapabilityStatementRestResourceOperation` items (represented as `dict` in JSON). """
        self._operation = None
        """ Primitive extension for operation. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ Base System profile for all uses of resource.
        Type `str`. """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        self.readHistory = None
        """ Whether vRead can return past versions.
        Type `bool`. """
        self._readHistory = None
        """ Primitive extension for readHistory. Type `FHIRPrimitiveExtension` """
        
        self.referencePolicy = None
        """ literal | logical | resolves | enforced | local.
        List of `str` items. """
        self._referencePolicy = None
        """ Primitive extension for referencePolicy. Type `FHIRPrimitiveExtension` """
        
        self.searchInclude = None
        """ _include values supported by the server.
        List of `str` items. """
        self._searchInclude = None
        """ Primitive extension for searchInclude. Type `FHIRPrimitiveExtension` """
        
        self.searchParam = None
        """ Search parameters supported by implementation.
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        self._searchParam = None
        """ Primitive extension for searchParam. Type `FHIRPrimitiveExtension` """
        
        self.searchRevInclude = None
        """ _revinclude values supported by the server.
        List of `str` items. """
        self._searchRevInclude = None
        """ Primitive extension for searchRevInclude. Type `FHIRPrimitiveExtension` """
        
        self.supportedProfile = None
        """ Profiles for use cases supported.
        List of `str` items. """
        self._supportedProfile = None
        """ Primitive extension for supportedProfile. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ A resource type that is supported.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.updateCreate = None
        """ If update can commit to a new identity.
        Type `bool`. """
        self._updateCreate = None
        """ Primitive extension for updateCreate. Type `FHIRPrimitiveExtension` """
        
        self.versioning = None
        """ no-version | versioned | versioned-update.
        Type `str`. """
        self._versioning = None
        """ Primitive extension for versioning. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementRestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResource, self).elementProperties()
        js.extend([
            ("conditionalCreate", "conditionalCreate", bool, False, None, False),
            ("_conditionalCreate", "_conditionalCreate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("conditionalDelete", "conditionalDelete", str, False, None, False),
            ("_conditionalDelete", "_conditionalDelete", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("conditionalRead", "conditionalRead", str, False, None, False),
            ("_conditionalRead", "_conditionalRead", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("conditionalUpdate", "conditionalUpdate", bool, False, None, False),
            ("_conditionalUpdate", "_conditionalUpdate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("interaction", "interaction", CapabilityStatementRestResourceInteraction, True, None, False),
            ("_interaction", "_interaction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
            ("_operation", "_operation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("readHistory", "readHistory", bool, False, None, False),
            ("_readHistory", "_readHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referencePolicy", "referencePolicy", str, True, None, False),
            ("_referencePolicy", "_referencePolicy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("searchInclude", "searchInclude", str, True, None, False),
            ("_searchInclude", "_searchInclude", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("_searchParam", "_searchParam", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("searchRevInclude", "searchRevInclude", str, True, None, False),
            ("_searchRevInclude", "_searchRevInclude", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportedProfile", "supportedProfile", str, True, None, False),
            ("_supportedProfile", "_supportedProfile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("updateCreate", "updateCreate", bool, False, None, False),
            ("_updateCreate", "_updateCreate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("versioning", "versioning", str, False, None, False),
            ("_versioning", "_versioning", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    """ What operations are supported?.
    
    Identifies a restful operation supported by the solution.
    """
    
    resource_type = "CapabilityStatementRestResourceInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ read | vread | update | patch | delete | history-instance |
        history-type | create | search-type.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementRestResourceInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementRestResourceOperation(backboneelement.BackboneElement):
    """ Definition of a resource operation.
    
    Definition of an operation or a named query together with its parameters
    and their meaning and type. Consult the definition of the operation for
    details about how to invoke the operation, and the parameters.
    """
    
    resource_type = "CapabilityStatementRestResourceOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ The defined operation/query.
        Type `str`. """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Specific details about operation behavior.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name by which the operation/query is invoked.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementRestResourceOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceOperation, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    """ Search parameters supported by implementation.
    
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    
    resource_type = "CapabilityStatementRestResourceSearchParam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ Source of definition for parameter.
        Type `str`. """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Server-specific usage.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name of search parameter.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementRestResourceSearchParam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceSearchParam, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
    """ Information about security of implementation.
    
    Information about security implementation from an interface perspective -
    what a client needs to know.
    """
    
    resource_type = "CapabilityStatementRestSecurity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cors = None
        """ Adds CORS Headers (http://enable-cors.org/).
        Type `bool`. """
        self._cors = None
        """ Primitive extension for cors. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ General description of how security works.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.service = None
        """ OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._service = None
        """ Primitive extension for service. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementRestSecurity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestSecurity, self).elementProperties()
        js.extend([
            ("cors", "cors", bool, False, None, False),
            ("_cors", "_cors", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("service", "service", codeableconcept.CodeableConcept, True, None, False),
            ("_service", "_service", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CapabilityStatementSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this capability statement.
    
    Software that is covered by this capability statement.  It is used when the
    capability statement describes the capabilities of a particular software
    version, independent of an installation.
    """
    
    resource_type = "CapabilityStatementSoftware"
    
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
        
        self.releaseDate = None
        """ Date this version was released.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._releaseDate = None
        """ Primitive extension for releaseDate. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Version covered by this statement.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(CapabilityStatementSoftware, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("releaseDate", "releaseDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_releaseDate", "_releaseDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdatetime
from . import fhirreference
from . import usagecontext