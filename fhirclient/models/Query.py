#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (query.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import Extension
import FHIRElement
import FHIRReference
import FHIRResource
import Narrative


class Query(FHIRResource.FHIRResource):
    """ A description of a query with a set of parameters.
    
    Scope and Usage The resource is used to perform queries using messaging-
    based exchanges, and to perform asynchronous searches using the RESTful
    interface.
    """
    
    resource_name = "Query"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Links query and its response(s).
        Type `str`. """
        
        self.parameter = None
        """ Set of query parameters with values.
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.response = None
        """ If this is a response to a query.
        Type `QueryResponse` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(Query, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Query, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'parameter' in jsondict:
            self.parameter = Extension.Extension.with_json(jsondict['parameter'])
        if 'response' in jsondict:
            self.response = QueryResponse.with_json(jsondict['response'])
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])


class QueryResponse(FHIRElement.FHIRElement):
    """ If this is a response to a query.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.first = None
        """ To get first page (if paged).
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Links response to source query.
        Type `str`. """
        
        self.last = None
        """ To get last page (if paged).
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.next = None
        """ To get next page (if paged).
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ ok | limited | refused | error.
        Type `str`. """
        
        self.parameter = None
        """ Parameters server used.
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.previous = None
        """ To get previous page (if paged).
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ Resources that are the results of the search.
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.total = None
        """ Total number of matching records.
        Type `int`. """
        
        super(QueryResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(QueryResponse, self).update_with_json(jsondict)
        if 'first' in jsondict:
            self.first = Extension.Extension.with_json(jsondict['first'])
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'last' in jsondict:
            self.last = Extension.Extension.with_json(jsondict['last'])
        if 'next' in jsondict:
            self.next = Extension.Extension.with_json(jsondict['next'])
        if 'outcome' in jsondict:
            self.outcome = jsondict['outcome']
        if 'parameter' in jsondict:
            self.parameter = Extension.Extension.with_json(jsondict['parameter'])
        if 'previous' in jsondict:
            self.previous = Extension.Extension.with_json(jsondict['previous'])
        if 'reference' in jsondict:
            self.reference = FHIRReference.FHIRReference.with_json_and_owner(jsondict['reference'], self, FHIRResource.FHIRResource)
        if 'total' in jsondict:
            self.total = jsondict['total']

