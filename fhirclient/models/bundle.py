#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Bundle) on 2015-04-08.
#  2015, SMART Health IT.


import fhirdate
import fhirelement
import resource


class Bundle(resource.Resource):
    """ Contains a collection of resources.
    
    A container for a collection of resources.
    """
    
    resource_name = "Bundle"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.base = None
        """ Stated Base URL.
        Type `str`. """
        
        self.entry = None
        """ Entry in the bundle - will have a resource, or information.
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
    """ Entry in the bundle - will have a resource, or information.
    
    An entry in a bundle resource - will either contain a resource, or
    information about a resource (transactions and history only).
    """
    
    resource_name = "BundleEntry"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.base = None
        """ Base URL, if different to bundle base.
        Type `str`. """
        
        self.link = None
        """ Links related to this Bundle.
        List of `BundleLink` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resources in this bundle.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.search = None
        """ Search related information.
        Type `BundleEntrySearch` (represented as `dict` in JSON). """
        
        self.transaction = None
        """ Transaction Related Information.
        Type `BundleEntryTransaction` (represented as `dict` in JSON). """
        
        self.transactionResponse = None
        """ Transaction Related Information.
        Type `BundleEntryTransactionResponse` (represented as `dict` in JSON). """
        
        super(BundleEntry, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(BundleEntry, self).update_with_json(jsondict)
        if 'base' in jsondict:
            self.base = jsondict['base']
        if 'link' in jsondict:
            self.link = BundleLink.with_json_and_owner(jsondict['link'], self)
        if 'resource' in jsondict:
            self.resource = resource.Resource.with_json_and_owner(jsondict['resource'], self)
        if 'search' in jsondict:
            self.search = BundleEntrySearch.with_json_and_owner(jsondict['search'], self)
        if 'transaction' in jsondict:
            self.transaction = BundleEntryTransaction.with_json_and_owner(jsondict['transaction'], self)
        if 'transactionResponse' in jsondict:
            self.transactionResponse = BundleEntryTransactionResponse.with_json_and_owner(jsondict['transactionResponse'], self)


class BundleEntrySearch(fhirelement.FHIRElement):
    """ Search related information.
    
    Information about the search process that lead to the creation of this
    entry.
    """
    
    resource_name = "BundleEntrySearch"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.mode = None
        """ match | include - why this is in the result set.
        Type `str`. """
        
        self.score = None
        """ Search ranking (between 0 and 1).
        Type `float`. """
        
        super(BundleEntrySearch, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(BundleEntrySearch, self).update_with_json(jsondict)
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'score' in jsondict:
            self.score = jsondict['score']


class BundleEntryTransaction(fhirelement.FHIRElement):
    """ Transaction Related Information.
    
    Additional information about how this entry should be processed as part of
    a transaction.
    """
    
    resource_name = "BundleEntryTransaction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.ifMatch = None
        """ For managing update contention.
        Type `str`. """
        
        self.ifModifiedSince = None
        """ For managing update contention.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.ifNoneExist = None
        """ For conditional creates.
        Type `str`. """
        
        self.ifNoneMatch = None
        """ For managing cache currency.
        Type `str`. """
        
        self.method = None
        """ GET | POST | PUT | DELETE.
        Type `str`. """
        
        self.url = None
        """ The URL for the transaction.
        Type `str`. """
        
        super(BundleEntryTransaction, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(BundleEntryTransaction, self).update_with_json(jsondict)
        if 'ifMatch' in jsondict:
            self.ifMatch = jsondict['ifMatch']
        if 'ifModifiedSince' in jsondict:
            self.ifModifiedSince = fhirdate.FHIRDate.with_json_and_owner(jsondict['ifModifiedSince'], self)
        if 'ifNoneExist' in jsondict:
            self.ifNoneExist = jsondict['ifNoneExist']
        if 'ifNoneMatch' in jsondict:
            self.ifNoneMatch = jsondict['ifNoneMatch']
        if 'method' in jsondict:
            self.method = jsondict['method']
        if 'url' in jsondict:
            self.url = jsondict['url']


class BundleEntryTransactionResponse(fhirelement.FHIRElement):
    """ Transaction Related Information.
    
    Additional information about how this entry should be processed as part of
    a transaction.
    """
    
    resource_name = "BundleEntryTransactionResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.etag = None
        """ The etag for the resource (if relevant).
        Type `str`. """
        
        self.lastModified = None
        """ Server's date time modified.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.location = None
        """ The location, if the operation returns a location.
        Type `str`. """
        
        self.status = None
        """ Status return code for entry.
        Type `str`. """
        
        super(BundleEntryTransactionResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(BundleEntryTransactionResponse, self).update_with_json(jsondict)
        if 'etag' in jsondict:
            self.etag = jsondict['etag']
        if 'lastModified' in jsondict:
            self.lastModified = fhirdate.FHIRDate.with_json_and_owner(jsondict['lastModified'], self)
        if 'location' in jsondict:
            self.location = jsondict['location']
        if 'status' in jsondict:
            self.status = jsondict['status']


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

