#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8595 (http://hl7.org/fhir/StructureDefinition/Endpoint) on 2016-06-26.
#  2016, SMART Health IT.


from . import domainresource

class Endpoint(domainresource.DomainResource):
    """ The technical details of an endpoint that can be used for electronic
    services.
    
    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """
    
    resource_name = "Endpoint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Where the channel points to.
        Type `str`. """
        
        self.connectionType = None
        """ rest-hook | websocket | email | sms | message.
        Type `str`. """
        
        self.contact = None
        """ Contact details for source (e.g. troubleshooting).
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.header = None
        """ Usage depends on the channel type.
        List of `str` items. """
        
        self.identifier = None
        """ Identifies this endpoint across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization that exposes the endpoint.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.method = None
        """ The http verb to be used when calling this endpoint.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.name = None
        """ A name that this endpoint can be identified by.
        Type `str`. """
        
        self.payloadFormat = None
        """ Mimetype to send, or blank for no payload.
        Type `str`. """
        
        self.payloadType = None
        """ The type of content that may be used at this endpoint (e.g. XDS
        Discharge summaries).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Interval during responsibility is assumed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.publicKey = None
        """ PKI Public keys to support secure communications.
        Type `str`. """
        
        self.status = None
        """ active | suspended | error | off.
        Type `str`. """
        
        super(Endpoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Endpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, True),
            ("connectionType", "connectionType", str, False, None, True),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("header", "header", str, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("method", "method", coding.Coding, True, None, False),
            ("name", "name", str, False, None, False),
            ("payloadFormat", "payloadFormat", str, False, None, True),
            ("payloadType", "payloadType", codeableconcept.CodeableConcept, True, None, True),
            ("period", "period", period.Period, False, None, False),
            ("publicKey", "publicKey", str, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference
from . import identifier
from . import period
