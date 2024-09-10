# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Subscription).
# 2024, SMART Health IT.


from . import domainresource

class Subscription(domainresource.DomainResource):
    """ Server push subscription criteria.
    
    The subscription resource is used to define a push-based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system can take an appropriate action.
    """
    
    resource_type = "Subscription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.channel = None
        """ The channel on which to report matches to the criteria.
        Type `SubscriptionChannel` (represented as `dict` in JSON). """
        self._channel = None
        """ Primitive extension for channel. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for source (e.g. troubleshooting).
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.criteria = None
        """ Rule for server push.
        Type `str`. """
        self._criteria = None
        """ Primitive extension for criteria. Type `FHIRPrimitiveExtension` """
        
        self.end = None
        """ When to automatically delete the subscription.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._end = None
        """ Primitive extension for end. Type `FHIRPrimitiveExtension` """
        
        self.error = None
        """ Latest error note.
        Type `str`. """
        self._error = None
        """ Primitive extension for error. Type `FHIRPrimitiveExtension` """
        
        self.reason = None
        """ Description of why this subscription was created.
        Type `str`. """
        self._reason = None
        """ Primitive extension for reason. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ requested | active | error | off.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(Subscription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Subscription, self).elementProperties()
        js.extend([
            ("channel", "channel", SubscriptionChannel, False, None, True),
            ("_channel", "_channel", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("criteria", "criteria", str, False, None, True),
            ("_criteria", "_criteria", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("end", "end", fhirinstant.FHIRInstant, False, None, False),
            ("_end", "_end", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("error", "error", str, False, None, False),
            ("_error", "_error", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", str, False, None, True),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class SubscriptionChannel(backboneelement.BackboneElement):
    """ The channel on which to report matches to the criteria.
    
    Details where to send notifications when resources are received that meet
    the criteria.
    """
    
    resource_type = "SubscriptionChannel"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint = None
        """ Where the channel points to.
        Type `str`. """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.header = None
        """ Usage depends on the channel type.
        List of `str` items. """
        self._header = None
        """ Primitive extension for header. Type `FHIRPrimitiveExtension` """
        
        self.payload = None
        """ MIME type to send, or omit for no payload.
        Type `str`. """
        self._payload = None
        """ Primitive extension for payload. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ rest-hook | websocket | email | sms | message.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SubscriptionChannel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubscriptionChannel, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, False),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("header", "header", str, True, None, False),
            ("_header", "_header", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payload", "payload", str, False, None, False),
            ("_payload", "_payload", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import contactpoint
from . import fhirinstant