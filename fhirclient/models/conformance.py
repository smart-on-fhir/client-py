#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (conformance.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import coding
import contactpoint
import fhirdate
import fhirelement
import fhirreference
import fhirresource


class Conformance(fhirresource.FHIRResource):
    """ A conformance statement.
    
    A conformance statement is a set of requirements for a desired
    implementation or a description of how a target application fulfills those
    requirements in a particular implementation.
    """
    
    resource_name = "Conformance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.acceptUnknown = False
        """ True if application accepts unknown elements.
        Type `bool`. """
        
        self.date = None
        """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Human description of the conformance statement.
        Type `str`. """
        
        self.document = None
        """ Document definition.
        List of `ConformanceDocument` items (represented as `dict` in JSON). """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None
        """ FHIR Version.
        Type `str`. """
        
        self.format = None
        """ formats supported (xml | json | mime type).
        List of `str` items. """
        
        self.identifier = None
        """ Logical id to reference this statement.
        Type `str`. """
        
        self.implementation = None
        """ If this describes a specific instance.
        Type `ConformanceImplementation` (represented as `dict` in JSON). """
        
        self.messaging = None
        """ If messaging is supported.
        List of `ConformanceMessaging` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name for this conformance statement.
        Type `str`. """
        
        self.profile = None
        """ Profiles supported by the system.
        List of `FHIRReference` items referencing `Profile` (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Publishing Organization.
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
        
        self.telecom = None
        """ Contacts for Organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the statement.
        Type `str`. """
        
        super(Conformance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Conformance, self).update_with_json(jsondict)
        if 'acceptUnknown' in jsondict:
            self.acceptUnknown = jsondict['acceptUnknown']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'document' in jsondict:
            self.document = ConformanceDocument.with_json_and_owner(jsondict['document'], self)
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'fhirVersion' in jsondict:
            self.fhirVersion = jsondict['fhirVersion']
        if 'format' in jsondict:
            self.format = jsondict['format']
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'implementation' in jsondict:
            self.implementation = ConformanceImplementation.with_json_and_owner(jsondict['implementation'], self)
        if 'messaging' in jsondict:
            self.messaging = ConformanceMessaging.with_json_and_owner(jsondict['messaging'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'profile' in jsondict:
            self.profile = fhirreference.FHIRReference.with_json_and_owner(jsondict['profile'], self)
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'rest' in jsondict:
            self.rest = ConformanceRest.with_json_and_owner(jsondict['rest'], self)
        if 'software' in jsondict:
            self.software = ConformanceSoftware.with_json_and_owner(jsondict['software'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'version' in jsondict:
            self.version = jsondict['version']


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
        Type `FHIRReference` referencing `Profile` (represented as `dict` in JSON). """
        
        super(ConformanceDocument, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceDocument, self).update_with_json(jsondict)
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'profile' in jsondict:
            self.profile = fhirreference.FHIRReference.with_json_and_owner(jsondict['profile'], self)


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
    
    def update_with_json(self, jsondict):
        super(ConformanceImplementation, self).update_with_json(jsondict)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'url' in jsondict:
            self.url = jsondict['url']


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
        """ Actual endpoint being described.
        Type `str`. """
        
        self.event = None
        """ Declare support for this event.
        List of `ConformanceMessagingEvent` items (represented as `dict` in JSON). """
        
        self.reliableCache = None
        """ Reliable Message Cache Length (min).
        Type `int`. """
        
        super(ConformanceMessaging, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceMessaging, self).update_with_json(jsondict)
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'endpoint' in jsondict:
            self.endpoint = jsondict['endpoint']
        if 'event' in jsondict:
            self.event = ConformanceMessagingEvent.with_json_and_owner(jsondict['event'], self)
        if 'reliableCache' in jsondict:
            self.reliableCache = jsondict['reliableCache']


class ConformanceMessagingEvent(fhirelement.FHIRElement):
    """ Declare support for this event.
    
    A description of the solution's support for an event at this end point.
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
        
        self.protocol = None
        """ http | ftp | mllp +.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.request = None
        """ Profile that describes the request.
        Type `FHIRReference` referencing `Profile` (represented as `dict` in JSON). """
        
        self.response = None
        """ Profile that describes the response.
        Type `FHIRReference` referencing `Profile` (represented as `dict` in JSON). """
        
        super(ConformanceMessagingEvent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceMessagingEvent, self).update_with_json(jsondict)
        if 'category' in jsondict:
            self.category = jsondict['category']
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'focus' in jsondict:
            self.focus = jsondict['focus']
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'protocol' in jsondict:
            self.protocol = coding.Coding.with_json_and_owner(jsondict['protocol'], self)
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'response' in jsondict:
            self.response = fhirreference.FHIRReference.with_json_and_owner(jsondict['response'], self)


class ConformanceRest(fhirelement.FHIRElement):
    """ If the endpoint is a RESTful one.
    
    A definition of the restful capabilities of the solution, if any.
    """
    
    resource_name = "ConformanceRest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.documentMailbox = None
        """ How documents are accepted in /Mailbox.
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
        
        self.security = None
        """ Information about security of implementation.
        Type `ConformanceRestSecurity` (represented as `dict` in JSON). """
        
        super(ConformanceRest, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceRest, self).update_with_json(jsondict)
        if 'documentMailbox' in jsondict:
            self.documentMailbox = jsondict['documentMailbox']
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'interaction' in jsondict:
            self.interaction = ConformanceRestInteraction.with_json_and_owner(jsondict['interaction'], self)
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'operation' in jsondict:
            self.operation = ConformanceRestOperation.with_json_and_owner(jsondict['operation'], self)
        if 'resource' in jsondict:
            self.resource = ConformanceRestResource.with_json_and_owner(jsondict['resource'], self)
        if 'security' in jsondict:
            self.security = ConformanceRestSecurity.with_json_and_owner(jsondict['security'], self)


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
    
    def update_with_json(self, jsondict):
        super(ConformanceRestInteraction, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']


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
        """ The the operation/query is defined.
        Type `FHIRReference` referencing `OperationDefinition` (represented as `dict` in JSON). """
        
        self.name = None
        """ Name by which the operation/query is invoked.
        Type `str`. """
        
        super(ConformanceRestOperation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceRestOperation, self).update_with_json(jsondict)
        if 'definition' in jsondict:
            self.definition = fhirreference.FHIRReference.with_json_and_owner(jsondict['definition'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']


class ConformanceRestResource(fhirelement.FHIRElement):
    """ Resource served on the REST interface.
    
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    
    resource_name = "ConformanceRestResource"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.interaction = None
        """ What operations are supported?.
        List of `ConformanceRestResourceInteraction` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ What structural features are supported.
        Type `FHIRReference` referencing `Profile` (represented as `dict` in JSON). """
        
        self.readHistory = False
        """ Whether vRead can return past versions.
        Type `bool`. """
        
        self.searchInclude = None
        """ _include values supported by the server.
        List of `str` items. """
        
        self.searchParam = None
        """ Additional search params defined.
        List of `ConformanceRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.type = None
        """ A resource type that is supported.
        Type `str`. """
        
        self.updateCreate = False
        """ If allows/uses update to a new location.
        Type `bool`. """
        
        self.versioning = None
        """ no-version | versioned | versioned-update.
        Type `str`. """
        
        super(ConformanceRestResource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceRestResource, self).update_with_json(jsondict)
        if 'interaction' in jsondict:
            self.interaction = ConformanceRestResourceInteraction.with_json_and_owner(jsondict['interaction'], self)
        if 'profile' in jsondict:
            self.profile = fhirreference.FHIRReference.with_json_and_owner(jsondict['profile'], self)
        if 'readHistory' in jsondict:
            self.readHistory = jsondict['readHistory']
        if 'searchInclude' in jsondict:
            self.searchInclude = jsondict['searchInclude']
        if 'searchParam' in jsondict:
            self.searchParam = ConformanceRestResourceSearchParam.with_json_and_owner(jsondict['searchParam'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'updateCreate' in jsondict:
            self.updateCreate = jsondict['updateCreate']
        if 'versioning' in jsondict:
            self.versioning = jsondict['versioning']


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
    
    def update_with_json(self, jsondict):
        super(ConformanceRestResourceInteraction, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']


class ConformanceRestResourceSearchParam(fhirelement.FHIRElement):
    """ Additional search params defined.
    
    Additional search parameters for implementations to support and/or make use
    of.
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
        
        self.name = None
        """ Name of search parameter.
        Type `str`. """
        
        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity.
        Type `str`. """
        
        super(ConformanceRestResourceSearchParam, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceRestResourceSearchParam, self).update_with_json(jsondict)
        if 'chain' in jsondict:
            self.chain = jsondict['chain']
        if 'definition' in jsondict:
            self.definition = jsondict['definition']
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'target' in jsondict:
            self.target = jsondict['target']
        if 'type' in jsondict:
            self.type = jsondict['type']


class ConformanceRestSecurity(fhirelement.FHIRElement):
    """ Information about security of implementation.
    """
    
    resource_name = "ConformanceRestSecurity"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.certificate = None
        """ Certificates associated with security profiles.
        List of `ConformanceRestSecurityCertificate` items (represented as `dict` in JSON). """
        
        self.cors = False
        """ Adds CORS Headers (http://enable-cors.org/).
        Type `bool`. """
        
        self.description = None
        """ General description of how security works.
        Type `str`. """
        
        self.service = None
        """ OAuth | OAuth2 | NTLM | Basic | Kerberos.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ConformanceRestSecurity, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceRestSecurity, self).update_with_json(jsondict)
        if 'certificate' in jsondict:
            self.certificate = ConformanceRestSecurityCertificate.with_json_and_owner(jsondict['certificate'], self)
        if 'cors' in jsondict:
            self.cors = jsondict['cors']
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'service' in jsondict:
            self.service = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['service'], self)


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
    
    def update_with_json(self, jsondict):
        super(ConformanceRestSecurityCertificate, self).update_with_json(jsondict)
        if 'blob' in jsondict:
            self.blob = jsondict['blob']
        if 'type' in jsondict:
            self.type = jsondict['type']


class ConformanceSoftware(fhirelement.FHIRElement):
    """ Software that is covered by this conformance statement.
    
    Software that is covered by this conformance statement.  It is used when
    the profile describes the capabilities of a particular software version,
    independent of an installation.
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
    
    def update_with_json(self, jsondict):
        super(ConformanceSoftware, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'releaseDate' in jsondict:
            self.releaseDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['releaseDate'], self)
        if 'version' in jsondict:
            self.version = jsondict['version']

