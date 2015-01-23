#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (subscription.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import contactpoint
import fhirdate
import fhirelement
import fhirresource


class Subscription(fhirresource.FHIRResource):
    """ A server push subscription criteria.
    
    Todo.
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
        List of `SubscriptionTag` items (represented as `dict` in JSON). """
        
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
            self.tag = SubscriptionTag.with_json_and_owner(jsondict['tag'], self)


class SubscriptionChannel(fhirelement.FHIRElement):
    """ The channel on which to report matches to the criteria.
    
    Todo.
    """
    
    resource_name = "SubscriptionChannel"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.header = None
        """ Usage depends on the channel type.
        Type `str`. """
        
        self.payload = None
        """ Mimetype to send, or blank for no payload.
        Type `str`. """
        
        self.type = None
        """ rest-hook | websocket | email | sms | message.
        Type `str`. """
        
        self.url = None
        """ Where the channel points to.
        Type `str`. """
        
        super(SubscriptionChannel, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SubscriptionChannel, self).update_with_json(jsondict)
        if 'header' in jsondict:
            self.header = jsondict['header']
        if 'payload' in jsondict:
            self.payload = jsondict['payload']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'url' in jsondict:
            self.url = jsondict['url']


class SubscriptionTag(fhirelement.FHIRElement):
    """ A tag to add to matching resources.
    
    Todo.
    """
    
    resource_name = "SubscriptionTag"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Tag description label.
        Type `str`. """
        
        self.scheme = None
        """ The scheme for the tag (kind of tag).
        Type `str`. """
        
        self.term = None
        """ The term that identifies the tag.
        Type `str`. """
        
        super(SubscriptionTag, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SubscriptionTag, self).update_with_json(jsondict)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'scheme' in jsondict:
            self.scheme = jsondict['scheme']
        if 'term' in jsondict:
            self.term = jsondict['term']

