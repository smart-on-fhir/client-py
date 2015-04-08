#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Subscription) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import contactpoint
import domainresource
import fhirdate
import fhirelement


class Subscription(domainresource.DomainResource):
    """ A server push subscription criteria.
    
    The subscription resource is used to define a push based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system is able to take an appropriate action.
    """
    
    resource_name = "Subscription"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(Subscription, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Subscription, self).update_with_json(jsondict)
        if 'channel' in jsondict:
            self.channel = SubscriptionChannel.with_json_and_owner(jsondict['channel'], self)
        if 'contact' in jsondict:
            self.contact = contactpoint.ContactPoint.with_json_and_owner(jsondict['contact'], self)
        if 'criteria' in jsondict:
            self.criteria = jsondict['criteria']
        if 'end' in jsondict:
            self.end = fhirdate.FHIRDate.with_json_and_owner(jsondict['end'], self)
        if 'error' in jsondict:
            self.error = jsondict['error']
        if 'reason' in jsondict:
            self.reason = jsondict['reason']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'tag' in jsondict:
            self.tag = coding.Coding.with_json_and_owner(jsondict['tag'], self)


class SubscriptionChannel(fhirelement.FHIRElement):
    """ The channel on which to report matches to the criteria.
    
    Details where to send notifications when resources are received that meet
    the criteria.
    """
    
    resource_name = "SubscriptionChannel"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.endpoint = None
        """ Where the channel points to.
        Type `str`. """
        
        self.header = None
        """ Usage depends on the channel type.
        Type `str`. """
        
        self.payload = None
        """ Mimetype to send, or blank for no payload.
        Type `str`. """
        
        self.type = None
        """ rest-hook | websocket | email | sms | message.
        Type `str`. """
        
        super(SubscriptionChannel, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SubscriptionChannel, self).update_with_json(jsondict)
        if 'endpoint' in jsondict:
            self.endpoint = jsondict['endpoint']
        if 'header' in jsondict:
            self.header = jsondict['header']
        if 'payload' in jsondict:
            self.payload = jsondict['payload']
        if 'type' in jsondict:
            self.type = jsondict['type']

