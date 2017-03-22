#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Subscription) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Subscription(domainresource.DomainResource):
    """ A server push subscription criteria.
    
    The subscription resource is used to define a push based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system is able to take an appropriate action.
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
        
        self.contact = None
        """ Contact details for source (e.g. troubleshooting).
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.criteria = None
        """ Rule for server push criteria.
        Type `str`. """
        
        self.end = None
        """ When to automatically delete the subscription.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.error = None
        """ Latest error note.
        Type `str`. """
        
        self.reason = None
        """ Description of why this subscription was created.
        Type `str`. """
        
        self.status = None
        """ requested | active | error | off.
        Type `str`. """
        
        self.tag = None
        """ A tag to add to matching resources.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(Subscription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Subscription, self).elementProperties()
        js.extend([
            ("channel", "channel", SubscriptionChannel, False, None, True),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("criteria", "criteria", str, False, None, True),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("error", "error", str, False, None, False),
            ("reason", "reason", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("tag", "tag", coding.Coding, True, None, False),
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
        
        self.header = None
        """ Usage depends on the channel type.
        List of `str` items. """
        
        self.payload = None
        """ Mimetype to send, or omit for no payload.
        Type `str`. """
        
        self.type = None
        """ rest-hook | websocket | email | sms | message.
        Type `str`. """
        
        super(SubscriptionChannel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubscriptionChannel, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, False),
            ("header", "header", str, True, None, False),
            ("payload", "payload", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
