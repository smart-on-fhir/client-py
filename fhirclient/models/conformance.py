#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (conformance.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import coding
import contact
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import narrative
import profile


class Conformance(fhirresource.FHIRResource):
    """ A conformance statement.
    
    Scope and Usage Conformance statements are used in one of three ways:
    
    Describe an actual implementation In this scenario, the conformance
    statement describes the capabilities of a deployed and configured solution
    available at a particular access point or set of access points. The
    statement describes exactly how to interface with that deployed solution
    and thus provides for a degree of self-configuration of software solutions.
    
    This is the type of profile that FHIR restful solutions are expected to
    make available on invocation of the conformance operation. It is also the
    type of statement that forms a basis for the testing, certification or
    commissioning of specific software installations.
    
    A conformance statement is identified as being an implementation statement
    through the presence of the implementation element.
    
    Describe software solution capabilities In this scenario, the conformance
    statement describes generic capabilities of a software application or
    component solution. The solution might be available for purchase or other
    acquisition and might be deployed and configured at any number of
    independent sites. Because it is not dependent on any particular
    implementation, the profile cannot provide specific details such as
    endpoint addresses. It may also need to document various configurations in
    which the application can be set up or describe the degree of
    customizability associated with the solution.
    
    This type of statement may be used as a marketing tool by software and
    system developers to formally describe their capabilities. It can also be
    used as the basis for conformance testing of software solutions independent
    of a particular installation.
    
    A conformance statement is identified as being a software solution
    statement through the presence of the software element.
    
    Describe a desired solution In this scenario, the conformance statement
    describes the capabilities of a desired system. It might be used as part of
    an architectural design process to document needed system capabilities, or
    might be used as part of an RFP process to formally document the
    requirements of a requested solution and to document the criteria by which
    proposals will be evaluated.
    
    A conformance statement is identified as being a requirements statement
    through the presence of the proposal element.
    
    
    
    These three types of profiles can be used together. A requirements
    statement can be compared against the solution statements proffered by
    respondents to an RFP. A solution statement for a software package forms
    the starting point for the implementation statement associated with a
    particular installation of that software package.
    """
    
    resource_name = "Conformance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.acceptUnknown = False
        """ True if application accepts unknown elements.
        Type `bool`. """
        
        self.date = None
        """ Publication Date.
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
        List of `Contact` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the statement.
        Type `str`. """
        
        super(Conformance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Conformance, self).update_with_json(jsondict)
        if 'acceptUnknown' in jsondict:
            self.acceptUnknown = jsondict['acceptUnknown']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'document' in jsondict:
            self.document = ConformanceDocument.with_json(jsondict['document'])
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'fhirVersion' in jsondict:
            self.fhirVersion = jsondict['fhirVersion']
        if 'format' in jsondict:
            self.format = jsondict['format']
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'implementation' in jsondict:
            self.implementation = ConformanceImplementation.with_json(jsondict['implementation'])
        if 'messaging' in jsondict:
            self.messaging = ConformanceMessaging.with_json(jsondict['messaging'])
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'profile' in jsondict:
            self.profile = fhirreference.FHIRReference.with_json_and_owner(jsondict['profile'], self, profile.Profile)
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'rest' in jsondict:
            self.rest = ConformanceRest.with_json(jsondict['rest'])
        if 'software' in jsondict:
            self.software = ConformanceSoftware.with_json(jsondict['software'])
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'telecom' in jsondict:
            self.telecom = contact.Contact.with_json(jsondict['telecom'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'version' in jsondict:
            self.version = jsondict['version']


class ConformanceSoftware(fhirelement.FHIRElement):
    """ Software that is covered by this conformance statement.
    
    Software that is covered by this conformance statement.  It is used when
    the profile describes the capabilities of a particular software version,
    independent of an installation.
    """
    
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
            self.releaseDate = fhirdate.FHIRDate.with_json(jsondict['releaseDate'])
        if 'version' in jsondict:
            self.version = jsondict['version']


class ConformanceImplementation(fhirelement.FHIRElement):
    """ If this describes a specific instance.
    
    Identifies a specific implementation instance that is described by the
    conformance statement - i.e. a particular installation, rather than the
    capabilities of a software program.
    """
    
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


class ConformanceRest(fhirelement.FHIRElement):
    """ If the endpoint is a RESTful one.
    
    A definition of the restful capabilities of the solution, if any.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.documentMailbox = None
        """ How documents are accepted in /Mailbox.
        List of `str` items. """
        
        self.documentation = None
        """ General description of implementation.
        Type `str`. """
        
        self.mode = None
        """ client | server.
        Type `str`. """
        
        self.operation = None
        """ What operations are supported?.
        List of `ConformanceRestOperation` items (represented as `dict` in JSON). """
        
        self.query = None
        """ Definition of a named query.
        List of `ConformanceRestQuery` items (represented as `dict` in JSON). """
        
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
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'operation' in jsondict:
            self.operation = ConformanceRestOperation.with_json(jsondict['operation'])
        if 'query' in jsondict:
            self.query = ConformanceRestQuery.with_json(jsondict['query'])
        if 'resource' in jsondict:
            self.resource = ConformanceRestResource.with_json(jsondict['resource'])
        if 'security' in jsondict:
            self.security = ConformanceRestSecurity.with_json(jsondict['security'])


class ConformanceRestSecurity(fhirelement.FHIRElement):
    """ Information about security of implementation.
    """
    
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
            self.certificate = ConformanceRestSecurityCertificate.with_json(jsondict['certificate'])
        if 'cors' in jsondict:
            self.cors = jsondict['cors']
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'service' in jsondict:
            self.service = codeableconcept.CodeableConcept.with_json(jsondict['service'])


class ConformanceRestSecurityCertificate(fhirelement.FHIRElement):
    """ Certificates associated with security profiles.
    """
    
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


class ConformanceRestResource(fhirelement.FHIRElement):
    """ Resource served on the REST interface.
    
    A specification of the restful capabilities of the solution for a specific
    resource type.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.operation = None
        """ What operations are supported?.
        List of `ConformanceRestResourceOperation` items (represented as `dict` in JSON). """
        
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
        
        super(ConformanceRestResource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceRestResource, self).update_with_json(jsondict)
        if 'operation' in jsondict:
            self.operation = ConformanceRestResourceOperation.with_json(jsondict['operation'])
        if 'profile' in jsondict:
            self.profile = fhirreference.FHIRReference.with_json_and_owner(jsondict['profile'], self, profile.Profile)
        if 'readHistory' in jsondict:
            self.readHistory = jsondict['readHistory']
        if 'searchInclude' in jsondict:
            self.searchInclude = jsondict['searchInclude']
        if 'searchParam' in jsondict:
            self.searchParam = ConformanceRestResourceSearchParam.with_json(jsondict['searchParam'])
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'updateCreate' in jsondict:
            self.updateCreate = jsondict['updateCreate']


class ConformanceRestResourceOperation(fhirelement.FHIRElement):
    """ What operations are supported?.
    
    Identifies a restful operation supported by the solution.
    """
    
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
        
        super(ConformanceRestResourceOperation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceRestResourceOperation, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']


class ConformanceRestResourceSearchParam(fhirelement.FHIRElement):
    """ Additional search params defined.
    
    Additional search parameters for implementations to support and/or make use
    of.
    """
    
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


class ConformanceRestOperation(fhirelement.FHIRElement):
    """ What operations are supported?.
    
    A specification of restful operations supported by the system.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ transaction | search-system | history-system.
        Type `str`. """
        
        self.documentation = None
        """ Anything special about operation behavior.
        Type `str`. """
        
        super(ConformanceRestOperation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceRestOperation, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']


class ConformanceRestQuery(fhirelement.FHIRElement):
    """ Definition of a named query.
    
    Definition of a named query and its parameters and their meaning.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.definition = None
        """ Where query is defined.
        Type `str`. """
        
        self.documentation = None
        """ Additional usage guidance.
        Type `str`. """
        
        self.name = None
        """ Special named queries (_query=).
        Type `str`. """
        
        self.parameter = None
        """ Parameter for the named query.
        List of `ConformanceRestQueryParameter` items (represented as `dict` in JSON). """
        
        super(ConformanceRestQuery, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceRestQuery, self).update_with_json(jsondict)
        if 'definition' in jsondict:
            self.definition = jsondict['definition']
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'parameter' in jsondict:
            self.parameter = ConformanceRestQueryParameter.with_json(jsondict['parameter'])


class ConformanceRestQueryParameter(fhirelement.FHIRElement):
    """ Parameter for the named query.
    
    Identifies which of the parameters for the named query are supported.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(ConformanceRestQueryParameter, self).__init__(jsondict)


class ConformanceMessaging(fhirelement.FHIRElement):
    """ If messaging is supported.
    
    A description of the messaging capabilities of the solution.
    """
    
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
        """ Reliable Message Cache Length.
        Type `int`. """
        
        super(ConformanceMessaging, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConformanceMessaging, self).update_with_json(jsondict)
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'endpoint' in jsondict:
            self.endpoint = jsondict['endpoint']
        if 'event' in jsondict:
            self.event = ConformanceMessagingEvent.with_json(jsondict['event'])
        if 'reliableCache' in jsondict:
            self.reliableCache = jsondict['reliableCache']


class ConformanceMessagingEvent(fhirelement.FHIRElement):
    """ Declare support for this event.
    
    A description of the solution's support for an event at this end point.
    """
    
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
            self.code = coding.Coding.with_json(jsondict['code'])
        if 'documentation' in jsondict:
            self.documentation = jsondict['documentation']
        if 'focus' in jsondict:
            self.focus = jsondict['focus']
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'protocol' in jsondict:
            self.protocol = coding.Coding.with_json(jsondict['protocol'])
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self, profile.Profile)
        if 'response' in jsondict:
            self.response = fhirreference.FHIRReference.with_json_and_owner(jsondict['response'], self, profile.Profile)


class ConformanceDocument(fhirelement.FHIRElement):
    """ Document definition.
    
    A document definition.
    """
    
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
            self.profile = fhirreference.FHIRReference.with_json_and_owner(jsondict['profile'], self, profile.Profile)

