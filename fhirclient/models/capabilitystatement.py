#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/CapabilityStatement) on 2017-01-15.
#  2017, SMART Health IT.


from . import domainresource

class CapabilityStatement(domainresource.DomainResource):
    """ A statement of system Capabilities.
    
    A Capability Statement documents a set of capabilities (behaviors) of a
    FHIR Server that may be used as a statement of actual server functionality
    or a statement of required or desired server implementation.
    """
    
    resource_type = "CapabilityStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.acceptUnknown = None
        """ no | extensions | elements | both.
        Type `str`. """
        
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
        """ Natural language description of the capability statement.
        Type `str`. """
        
        self.document = None
        """ Document definition.
        List of `CapabilityStatementDocument` items (represented as `dict` in JSON). """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None
        """ FHIR Version the system uses.
        Type `str`. """
        
        self.format = None
        """ formats supported (xml | json | ttl | mime type).
        List of `str` items. """
        
        self.implementation = None
        """ If this describes a specific instance.
        Type `CapabilityStatementImplementation` (represented as `dict` in JSON). """
        
        self.implementationGuide = None
        """ Implementation Guide supported.
        List of `str` items. """
        
        self.instantiates = None
        """ Canonical URL of another capability statement this implements.
        List of `str` items. """
        
        self.jurisdiction = None
        """ Intended jurisdiction for capability statement (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kind = None
        """ instance | capability | requirements.
        Type `str`. """
        
        self.messaging = None
        """ If messaging is supported.
        List of `CapabilityStatementMessaging` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this capability statement (Computer friendly).
        Type `str`. """
        
        self.patchFormat = None
        """ Patch formats supported.
        List of `str` items. """
        
        self.profile = None
        """ Profiles for use cases supported.
        List of `FHIRReference` items referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Why this capability statement is defined.
        Type `str`. """
        
        self.rest = None
        """ If the endpoint is a RESTful one.
        List of `CapabilityStatementRest` items (represented as `dict` in JSON). """
        
        self.software = None
        """ Software that is covered by this capability statement.
        Type `CapabilityStatementSoftware` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.title = None
        """ Name for this capability statement (Human friendly).
        Type `str`. """
        
        self.url = None
        """ Logical uri to reference this capability statement (globally
        unique).
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the capability statement.
        Type `str`. """
        
        super(CapabilityStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement, self).elementProperties()
        js.extend([
            ("acceptUnknown", "acceptUnknown", str, False, None, True),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("document", "document", CapabilityStatementDocument, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, True),
            ("format", "format", str, True, None, True),
            ("implementation", "implementation", CapabilityStatementImplementation, False, None, False),
            ("implementationGuide", "implementationGuide", str, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("messaging", "messaging", CapabilityStatementMessaging, True, None, False),
            ("name", "name", str, False, None, False),
            ("patchFormat", "patchFormat", str, True, None, False),
            ("profile", "profile", fhirreference.FHIRReference, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("rest", "rest", CapabilityStatementRest, True, None, False),
            ("software", "software", CapabilityStatementSoftware, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
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
        
        self.mode = None
        """ producer | consumer.
        Type `str`. """
        
        self.profile = None
        """ Constraint on a resource used in the document.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        super(CapabilityStatementDocument, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementDocument, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("profile", "profile", fhirreference.FHIRReference, False, None, True),
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
        
        self.description = None
        """ Describes this specific instance.
        Type `str`. """
        
        self.url = None
        """ Base URL for the installation.
        Type `str`. """
        
        super(CapabilityStatementImplementation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementImplementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
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
        
        self.endpoint = None
        """ Where messages should be sent.
        List of `CapabilityStatementMessagingEndpoint` items (represented as `dict` in JSON). """
        
        self.event = None
        """ Declare support for this event.
        List of `CapabilityStatementMessagingEvent` items (represented as `dict` in JSON). """
        
        self.reliableCache = None
        """ Reliable Message Cache Length (min).
        Type `int`. """
        
        super(CapabilityStatementMessaging, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessaging, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("endpoint", "endpoint", CapabilityStatementMessagingEndpoint, True, None, False),
            ("event", "event", CapabilityStatementMessagingEvent, True, None, True),
            ("reliableCache", "reliableCache", int, False, None, False),
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
        """ Address of end-point.
        Type `str`. """
        
        self.protocol = None
        """ http | ftp | mllp +.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(CapabilityStatementMessagingEndpoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessagingEndpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, True),
            ("protocol", "protocol", coding.Coding, False, None, True),
        ])
        return js


class CapabilityStatementMessagingEvent(backboneelement.BackboneElement):
    """ Declare support for this event.
    
    A description of the solution's support for an event at this end-point.
    """
    
    resource_type = "CapabilityStatementMessagingEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Consequence | Currency | Notification.
        Type `str`. """
        
        self.code = None
        """ Event type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.documentation = None
        """ Endpoint-specific event documentation.
        Type `str`. """
        
        self.focus = None
        """ Resource that's focus of message.
        Type `str`. """
        
        self.mode = None
        """ sender | receiver.
        Type `str`. """
        
        self.request = None
        """ Profile that describes the request.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.response = None
        """ Profile that describes the response.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        super(CapabilityStatementMessagingEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessagingEvent, self).elementProperties()
        js.extend([
            ("category", "category", str, False, None, False),
            ("code", "code", coding.Coding, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("focus", "focus", str, False, None, True),
            ("mode", "mode", str, False, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, True),
            ("response", "response", fhirreference.FHIRReference, False, None, True),
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
        
        self.documentation = None
        """ General description of implementation.
        Type `str`. """
        
        self.interaction = None
        """ What operations are supported?.
        List of `CapabilityStatementRestInteraction` items (represented as `dict` in JSON). """
        
        self.mode = None
        """ client | server.
        Type `str`. """
        
        self.operation = None
        """ Definition of an operation or a custom query.
        List of `CapabilityStatementRestOperation` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resource served on the REST interface.
        List of `CapabilityStatementRestResource` items (represented as `dict` in JSON). """
        
        self.searchParam = None
        """ Search params for searching all resources.
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.security = None
        """ Information about security of implementation.
        Type `CapabilityStatementRestSecurity` (represented as `dict` in JSON). """
        
        super(CapabilityStatementRest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRest, self).elementProperties()
        js.extend([
            ("compartment", "compartment", str, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("interaction", "interaction", CapabilityStatementRestInteraction, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("operation", "operation", CapabilityStatementRestOperation, True, None, False),
            ("resource", "resource", CapabilityStatementRestResource, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("security", "security", CapabilityStatementRestSecurity, False, None, False),
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
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        
        super(CapabilityStatementRestInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class CapabilityStatementRestOperation(backboneelement.BackboneElement):
    """ Definition of an operation or a custom query.
    
    Definition of an operation or a named query and with its parameters and
    their meaning and type.
    """
    
    resource_type = "CapabilityStatementRestOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ The defined operation/query.
        Type `FHIRReference` referencing `OperationDefinition` (represented as `dict` in JSON). """
        
        self.name = None
        """ Name by which the operation/query is invoked.
        Type `str`. """
        
        super(CapabilityStatementRestOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestOperation, self).elementProperties()
        js.extend([
            ("definition", "definition", fhirreference.FHIRReference, False, None, True),
            ("name", "name", str, False, None, True),
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
        
        self.conditionalDelete = None
        """ not-supported | single | multiple - how conditional delete is
        supported.
        Type `str`. """
        
        self.conditionalRead = None
        """ not-supported | modified-since | not-match | full-support.
        Type `str`. """
        
        self.conditionalUpdate = None
        """ If allows/uses conditional update.
        Type `bool`. """
        
        self.documentation = None
        """ Additional information about the use of the resource type.
        Type `str`. """
        
        self.interaction = None
        """ What operations are supported?.
        List of `CapabilityStatementRestResourceInteraction` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ Base System profile for all uses of resource.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.readHistory = None
        """ Whether vRead can return past versions.
        Type `bool`. """
        
        self.referencePolicy = None
        """ literal | logical | resolves | enforced | local.
        List of `str` items. """
        
        self.searchInclude = None
        """ _include values supported by the server.
        List of `str` items. """
        
        self.searchParam = None
        """ Search params supported by implementation.
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.searchRevInclude = None
        """ _revinclude values supported by the server.
        List of `str` items. """
        
        self.type = None
        """ A resource type that is supported.
        Type `str`. """
        
        self.updateCreate = None
        """ If update can commit to a new identity.
        Type `bool`. """
        
        self.versioning = None
        """ no-version | versioned | versioned-update.
        Type `str`. """
        
        super(CapabilityStatementRestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResource, self).elementProperties()
        js.extend([
            ("conditionalCreate", "conditionalCreate", bool, False, None, False),
            ("conditionalDelete", "conditionalDelete", str, False, None, False),
            ("conditionalRead", "conditionalRead", str, False, None, False),
            ("conditionalUpdate", "conditionalUpdate", bool, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("interaction", "interaction", CapabilityStatementRestResourceInteraction, True, None, True),
            ("profile", "profile", fhirreference.FHIRReference, False, None, False),
            ("readHistory", "readHistory", bool, False, None, False),
            ("referencePolicy", "referencePolicy", str, True, None, False),
            ("searchInclude", "searchInclude", str, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("searchRevInclude", "searchRevInclude", str, True, None, False),
            ("type", "type", str, False, None, True),
            ("updateCreate", "updateCreate", bool, False, None, False),
            ("versioning", "versioning", str, False, None, False),
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
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        
        super(CapabilityStatementRestResourceInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
    """ Search params supported by implementation.
    
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
        
        self.documentation = None
        """ Server-specific usage.
        Type `str`. """
        
        self.name = None
        """ Name of search parameter.
        Type `str`. """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri.
        Type `str`. """
        
        super(CapabilityStatementRestResourceSearchParam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceSearchParam, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
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
        
        self.certificate = None
        """ Certificates associated with security profiles.
        List of `CapabilityStatementRestSecurityCertificate` items (represented as `dict` in JSON). """
        
        self.cors = None
        """ Adds CORS Headers (http://enable-cors.org/).
        Type `bool`. """
        
        self.description = None
        """ General description of how security works.
        Type `str`. """
        
        self.service = None
        """ OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(CapabilityStatementRestSecurity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestSecurity, self).elementProperties()
        js.extend([
            ("certificate", "certificate", CapabilityStatementRestSecurityCertificate, True, None, False),
            ("cors", "cors", bool, False, None, False),
            ("description", "description", str, False, None, False),
            ("service", "service", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class CapabilityStatementRestSecurityCertificate(backboneelement.BackboneElement):
    """ Certificates associated with security profiles.
    """
    
    resource_type = "CapabilityStatementRestSecurityCertificate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.blob = None
        """ Actual certificate.
        Type `str`. """
        
        self.type = None
        """ Mime type for certificate.
        Type `str`. """
        
        super(CapabilityStatementRestSecurityCertificate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestSecurityCertificate, self).elementProperties()
        js.extend([
            ("blob", "blob", str, False, None, False),
            ("type", "type", str, False, None, False),
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
        
        self.releaseDate = None
        """ Date this version released.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.version = None
        """ Version covered by this statement.
        Type `str`. """
        
        super(CapabilityStatementSoftware, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("releaseDate", "releaseDate", fhirdate.FHIRDate, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirreference
from . import usagecontext
