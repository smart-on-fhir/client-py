#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Conformance) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import coding
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference


class Conformance(domainresource.DomainResource):
    """ A conformance statement.
    
    A conformance statement is a set of capabilities of a FHIR Server that may
    be used as a statement of actual server functionality or a statement of
    required or desired server implementation.
    """
    
    resource_name = "Conformance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.acceptUnknown = None
        """ no | extensions | elements | both.
        Type `str`. """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ConformanceContact` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Human description of the conformance statement.
        Type `str`. """
        
        self.document = None
        """ Document definition.
        List of `ConformanceDocument` items (represented as `dict` in JSON). """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None
        """ FHIR Version the system uses.
        Type `str`. """
        
        self.format = None
        """ formats supported (xml | json | mime type).
        List of `str` items. """
        
        self.implementation = None
        """ If this describes a specific instance.
        Type `ConformanceImplementation` (represented as `dict` in JSON). """
        
        self.kind = None
        """ instance | capability | requirements.
        Type `str`. """
        
        self.messaging = None
        """ If messaging is supported.
        List of `ConformanceMessaging` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name for this conformance statement.
        Type `str`. """
        
        self.profile = None
        """ Profiles for use cases supported.
        List of `FHIRReference` items referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Why is this needed?.
        Type `str`. """
        
        self.rest = None
        """ If the endpoint is a RESTful one.
        List of `ConformanceRest` items (represented as `dict` in JSON). """
        
        self.software = None
        """ Software that is covered by this conformance statement.
        Type `ConformanceSoftware` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.url = None
        """ Logical uri to reference this statement.
        Type `str`. """
        
        self.version = None
        """ Logical id for this version of the statement.
        Type `str`. """
        
        super(Conformance, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Conformance, self).elementProperties()
        js.extend([
            ("acceptUnknown", "acceptUnknown", str, False),
            ("contact", "contact", ConformanceContact, True),
            ("copyright", "copyright", str, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("document", "document", ConformanceDocument, True),
            ("experimental", "experimental", bool, False),
            ("fhirVersion", "fhirVersion", str, False),
            ("format", "format", str, True),
            ("implementation", "implementation", ConformanceImplementation, False),
            ("kind", "kind", str, False),
            ("messaging", "messaging", ConformanceMessaging, True),
            ("name", "name", str, False),
            ("profile", "profile", fhirreference.FHIRReference, True),
            ("publisher", "publisher", str, False),
            ("requirements", "requirements", str, False),
            ("rest", "rest", ConformanceRest, True),
            ("software", "software", ConformanceSoftware, False),
            ("status", "status", str, False),
            ("url", "url", str, False),
            ("version", "version", str, False),
        ])
        return js


class ConformanceContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "ConformanceContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ConformanceContact, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class ConformanceDocument(fhirelement.FHIRElement):
    """ Document definition.
    
    A document definition.
    """
    
    resource_name = "ConformanceDocument"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(ConformanceDocument, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceDocument, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False),
            ("mode", "mode", str, False),
            ("profile", "profile", fhirreference.FHIRReference, False),
        ])
        return js


class ConformanceImplementation(fhirelement.FHIRElement):
    """ If this describes a specific instance.
    
    Identifies a specific implementation instance that is described by the
    conformance statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    
    resource_name = "ConformanceImplementation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Describes this specific instance.
        Type `str`. """
        
        self.url = None
        """ Base URL for the installation.
        Type `str`. """
        
        super(ConformanceImplementation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceImplementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False),
            ("url", "url", str, False),
        ])
        return js


class ConformanceMessaging(fhirelement.FHIRElement):
    """ If messaging is supported.
    
    A description of the messaging capabilities of the solution.
    """
    
    resource_name = "ConformanceMessaging"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.documentation = None
        """ Messaging interface behavior details.
        Type `str`. """
        
        self.endpoint = None
        """ A messaging service end-point.
        List of `ConformanceMessagingEndpoint` items (represented as `dict` in JSON). """
        
        self.event = None
        """ Declare support for this event.
        List of `ConformanceMessagingEvent` items (represented as `dict` in JSON). """
        
        self.reliableCache = None
        """ Reliable Message Cache Length (min).
        Type `int`. """
        
        super(ConformanceMessaging, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceMessaging, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False),
            ("endpoint", "endpoint", ConformanceMessagingEndpoint, True),
            ("event", "event", ConformanceMessagingEvent, True),
            ("reliableCache", "reliableCache", int, False),
        ])
        return js


class ConformanceMessagingEndpoint(fhirelement.FHIRElement):
    """ A messaging service end-point.
    
    An endpoint (network accessible address) to which messages and/or replies
    are to be sent.
    """
    
    resource_name = "ConformanceMessagingEndpoint"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Address of end-point.
        Type `str`. """
        
        self.protocol = None
        """ http | ftp | mllp +.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ConformanceMessagingEndpoint, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceMessagingEndpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, False),
            ("protocol", "protocol", coding.Coding, False),
        ])
        return js


class ConformanceMessagingEvent(fhirelement.FHIRElement):
    """ Declare support for this event.
    
    A description of the solution's support for an event at this end-point.
    """
    
    resource_name = "ConformanceMessagingEvent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(ConformanceMessagingEvent, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceMessagingEvent, self).elementProperties()
        js.extend([
            ("category", "category", str, False),
            ("code", "code", coding.Coding, False),
            ("documentation", "documentation", str, False),
            ("focus", "focus", str, False),
            ("mode", "mode", str, False),
            ("request", "request", fhirreference.FHIRReference, False),
            ("response", "response", fhirreference.FHIRReference, False),
        ])
        return js


class ConformanceRest(fhirelement.FHIRElement):
    """ If the endpoint is a RESTful one.
    
    A definition of the restful capabilities of the solution, if any.
    """
    
    resource_name = "ConformanceRest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.compartment = None
        """ Compartments served/used by system.
        List of `str` items. """
        
        self.documentation = None
        """ General description of implementation.
        Type `str`. """
        
        self.interaction = None
        """ What operations are supported?.
        List of `ConformanceRestInteraction` items (represented as `dict` in JSON). """
        
        self.mode = None
        """ client | server.
        Type `str`. """
        
        self.operation = None
        """ Definition of an operation or a custom query.
        List of `ConformanceRestOperation` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resource served on the REST interface.
        List of `ConformanceRestResource` items (represented as `dict` in JSON). """
        
        self.searchParam = None
        """ Search params for searching all resources.
        List of `ConformanceRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.security = None
        """ Information about security of implementation.
        Type `ConformanceRestSecurity` (represented as `dict` in JSON). """
        
        self.transactionMode = None
        """ not-supported | batch | transaction | both.
        Type `str`. """
        
        super(ConformanceRest, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceRest, self).elementProperties()
        js.extend([
            ("compartment", "compartment", str, True),
            ("documentation", "documentation", str, False),
            ("interaction", "interaction", ConformanceRestInteraction, True),
            ("mode", "mode", str, False),
            ("operation", "operation", ConformanceRestOperation, True),
            ("resource", "resource", ConformanceRestResource, True),
            ("searchParam", "searchParam", ConformanceRestResourceSearchParam, True),
            ("security", "security", ConformanceRestSecurity, False),
            ("transactionMode", "transactionMode", str, False),
        ])
        return js


class ConformanceRestInteraction(fhirelement.FHIRElement):
    """ What operations are supported?.
    
    A specification of restful operations supported by the system.
    """
    
    resource_name = "ConformanceRestInteraction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ transaction | search-system | history-system.
        Type `str`. """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        
        super(ConformanceRestInteraction, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceRestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("documentation", "documentation", str, False),
        ])
        return js


class ConformanceRestOperation(fhirelement.FHIRElement):
    """ Definition of an operation or a custom query.
    
    Definition of an operation or a named query and with its parameters and
    their meaning and type.
    """
    
    resource_name = "ConformanceRestOperation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.definition = None
        """ The defined operation/query.
        Type `FHIRReference` referencing `OperationDefinition` (represented as `dict` in JSON). """
        
        self.name = None
        """ Name by which the operation/query is invoked.
        Type `str`. """
        
        super(ConformanceRestOperation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceRestOperation, self).elementProperties()
        js.extend([
            ("definition", "definition", fhirreference.FHIRReference, False),
            ("name", "name", str, False),
        ])
        return js


class ConformanceRestResource(fhirelement.FHIRElement):
    """ Resource served on the REST interface.
    
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    
    resource_name = "ConformanceRestResource"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.conditionalCreate = None
        """ If allows/uses conditional create.
        Type `bool`. """
        
        self.conditionalDelete = None
        """ not-supported | single | multiple - how conditional delete is
        supported.
        Type `str`. """
        
        self.conditionalUpdate = None
        """ If allows/uses conditional update.
        Type `bool`. """
        
        self.interaction = None
        """ What operations are supported?.
        List of `ConformanceRestResourceInteraction` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ Base System profile for all uses of resource.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.readHistory = None
        """ Whether vRead can return past versions.
        Type `bool`. """
        
        self.searchInclude = None
        """ _include values supported by the server.
        List of `str` items. """
        
        self.searchParam = None
        """ Search params supported by implementation.
        List of `ConformanceRestResourceSearchParam` items (represented as `dict` in JSON). """
        
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
        
        super(ConformanceRestResource, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceRestResource, self).elementProperties()
        js.extend([
            ("conditionalCreate", "conditionalCreate", bool, False),
            ("conditionalDelete", "conditionalDelete", str, False),
            ("conditionalUpdate", "conditionalUpdate", bool, False),
            ("interaction", "interaction", ConformanceRestResourceInteraction, True),
            ("profile", "profile", fhirreference.FHIRReference, False),
            ("readHistory", "readHistory", bool, False),
            ("searchInclude", "searchInclude", str, True),
            ("searchParam", "searchParam", ConformanceRestResourceSearchParam, True),
            ("searchRevInclude", "searchRevInclude", str, True),
            ("type", "type", str, False),
            ("updateCreate", "updateCreate", bool, False),
            ("versioning", "versioning", str, False),
        ])
        return js


class ConformanceRestResourceInteraction(fhirelement.FHIRElement):
    """ What operations are supported?.
    
    Identifies a restful operation supported by the solution.
    """
    
    resource_name = "ConformanceRestResourceInteraction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ read | vread | update | delete | history-instance | validate |
        history-type | create | search-type.
        Type `str`. """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        
        super(ConformanceRestResourceInteraction, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceRestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("documentation", "documentation", str, False),
        ])
        return js


class ConformanceRestResourceSearchParam(fhirelement.FHIRElement):
    """ Search params supported by implementation.
    
    Search parameters for implementations to support and/or make use of -
    either references to ones defined in the specification, or additional ones
    defined for/by the implementation.
    """
    
    resource_name = "ConformanceRestResourceSearchParam"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.chain = None
        """ Chained names supported.
        List of `str` items. """
        
        self.definition = None
        """ Source of definition for parameter.
        Type `str`. """
        
        self.documentation = None
        """ Server-specific usage.
        Type `str`. """
        
        self.modifier = None
        """ missing | exact | contains | not | text | in | not-in | below |
        above | type.
        List of `str` items. """
        
        self.name = None
        """ Name of search parameter.
        Type `str`. """
        
        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri.
        Type `str`. """
        
        super(ConformanceRestResourceSearchParam, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceRestResourceSearchParam, self).elementProperties()
        js.extend([
            ("chain", "chain", str, True),
            ("definition", "definition", str, False),
            ("documentation", "documentation", str, False),
            ("modifier", "modifier", str, True),
            ("name", "name", str, False),
            ("target", "target", str, True),
            ("type", "type", str, False),
        ])
        return js


class ConformanceRestSecurity(fhirelement.FHIRElement):
    """ Information about security of implementation.
    
    Information about security implementation from an interface perspective -
    what a client needs to know.
    """
    
    resource_name = "ConformanceRestSecurity"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.certificate = None
        """ Certificates associated with security profiles.
        List of `ConformanceRestSecurityCertificate` items (represented as `dict` in JSON). """
        
        self.cors = None
        """ Adds CORS Headers (http://enable-cors.org/).
        Type `bool`. """
        
        self.description = None
        """ General description of how security works.
        Type `str`. """
        
        self.service = None
        """ OAuth | SMART-on-FHIR | NTLM | Basic | Kerberos | Certificates.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ConformanceRestSecurity, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceRestSecurity, self).elementProperties()
        js.extend([
            ("certificate", "certificate", ConformanceRestSecurityCertificate, True),
            ("cors", "cors", bool, False),
            ("description", "description", str, False),
            ("service", "service", codeableconcept.CodeableConcept, True),
        ])
        return js


class ConformanceRestSecurityCertificate(fhirelement.FHIRElement):
    """ Certificates associated with security profiles.
    """
    
    resource_name = "ConformanceRestSecurityCertificate"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.blob = None
        """ Actual certificate.
        Type `str`. """
        
        self.type = None
        """ Mime type for certificate.
        Type `str`. """
        
        super(ConformanceRestSecurityCertificate, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceRestSecurityCertificate, self).elementProperties()
        js.extend([
            ("blob", "blob", str, False),
            ("type", "type", str, False),
        ])
        return js


class ConformanceSoftware(fhirelement.FHIRElement):
    """ Software that is covered by this conformance statement.
    
    Software that is covered by this conformance statement.  It is used when
    the conformance statement describes the capabilities of a particular
    software version, independent of an installation.
    """
    
    resource_name = "ConformanceSoftware"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(ConformanceSoftware, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConformanceSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("releaseDate", "releaseDate", fhirdate.FHIRDate, False),
            ("version", "version", str, False),
        ])
        return js

