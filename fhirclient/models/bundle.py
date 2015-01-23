#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (bundle.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import fhirdate
import fhirelement
import fhirresource


class Bundle(fhirresource.FHIRResource):
    """ Contains a group of resources.
    
    A container for a group of resources.
    """
    
    resource_name = "Bundle"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.base = None
        """ Stated Base URL.
        Type `str`. """
        
        self.entry = None
        """ Entry in the bundle - will have deleted or resource.
        List of `BundleEntry` items (represented as `dict` in JSON). """
        
        self.link = None
        """ Links related to this Bundle.
        List of `BundleLink` items (represented as `dict` in JSON). """
        
        self.signature = None
        """ XML Digital Signature (base64 encoded).
        Type `str`. """
        
        self.total = None
        """ If search, the total number of matches.
        Type `int`. """
        
        self.type = None
        """ document | message | transaction | transaction-response | history |
        searchset | collection.
        Type `str`. """
        
        super(Bundle, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Bundle, self).update_with_json(jsondict)
        if 'base' in jsondict:
            self.base = jsondict['base']
        if 'entry' in jsondict:
            self.entry = BundleEntry.with_json_and_owner(jsondict['entry'], self)
        if 'link' in jsondict:
            self.link = BundleLink.with_json_and_owner(jsondict['link'], self)
        if 'signature' in jsondict:
            self.signature = jsondict['signature']
        if 'total' in jsondict:
            self.total = jsondict['total']
        if 'type' in jsondict:
            self.type = jsondict['type']


class BundleEntry(fhirelement.FHIRElement):
    """ Entry in the bundle - will have deleted or resource.
    
    An entry in a bundle resource - will either contain a resource, or a
    deleted entry (transaction and history bundles only).
    """
    
    resource_name = "BundleEntry"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.base = None
        """ Base URL, if different to bundle base.
        Type `str`. """
        
        self.deleted = None
        """ If this is a deleted resource (transaction/history).
        Type `BundleEntryDeleted` (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resources in this bundle.
        Type `FHIRResource` (represented as `dict` in JSON). """
        
        self.score = None
        """ Search ranking (between 0 and 1).
        Type `float`. """
        
        self.search = None
        """ Search URL (see transaction).
        Type `str`. """
        
        self.status = None
        """ create | update | match | include - for search & transaction.
        Type `str`. """
        
        super(BundleEntry, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(BundleEntry, self).update_with_json(jsondict)
        if 'base' in jsondict:
            self.base = jsondict['base']
        if 'deleted' in jsondict:
            self.deleted = BundleEntryDeleted.with_json_and_owner(jsondict['deleted'], self)
        if 'resource' in jsondict:
            self.resource = fhirresource.FHIRResource.with_json_and_owner(jsondict['resource'], self)
        if 'score' in jsondict:
            self.score = jsondict['score']
        if 'search' in jsondict:
            self.search = jsondict['search']
        if 'status' in jsondict:
            self.status = jsondict['status']


class BundleEntryDeleted(fhirelement.FHIRElement):
    """ If this is a deleted resource (transaction/history).
    
    If this is an entry that represents a deleted resource. Only used when the
    bundle is a transaction or a history type. See RESTful API documentation
    for further information.
    """
    
    resource_name = "BundleEntryDeleted"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.instant = None
        """ When the resource was deleted.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.resourceId = None
        """ Id of resource that was deleted.
        Type `str`. """
        
        self.type = None
        """ Type of resource that was deleted.
        Type `str`. """
        
        self.versionId = None
        """ Version id for related resource.
        Type `str`. """
        
        super(BundleEntryDeleted, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(BundleEntryDeleted, self).update_with_json(jsondict)
        if 'instant' in jsondict:
            self.instant = fhirdate.FHIRDate.with_json_and_owner(jsondict['instant'], self)
        if 'resourceId' in jsondict:
            self.resourceId = jsondict['resourceId']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'versionId' in jsondict:
            self.versionId = jsondict['versionId']


class BundleLink(fhirelement.FHIRElement):
    """ Links related to this Bundle.
    
    A series of links that provide context to this bundle.
    """
    
    resource_name = "BundleLink"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.relation = None
        """ http://www.iana.org/assignments/link-relations/link-relations.xhtml.
        Type `str`. """
        
        self.url = None
        """ Reference details for the link.
        Type `str`. """
        
        super(BundleLink, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(BundleLink, self).update_with_json(jsondict)
        if 'relation' in jsondict:
            self.relation = jsondict['relation']
        if 'url' in jsondict:
            self.url = jsondict['url']

