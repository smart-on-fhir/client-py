#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Base class for FHIR resources.
#  2014, SMART Platforms.

import fhirelement
import fhirsearch
import fhirsearchelement


class FHIRResource(fhirelement.FHIRElement):
    """ Extends the FHIRElement base class with server talking capabilities.
    """
    resource_name = 'Resource'
    
    def __init__(self, jsondict=None):
        self._remote_id = None
        self._server = None
        
        self.language = None
        """ Human language of the content (BCP-47). """
        
        super(FHIRResource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(FHIRResource, self).update_with_json(jsondict)
        if 'language' in jsondict:
            self.language = jsondict['language']
    
    
    # MARK: Server Connection
    
    @classmethod
    def read(cls, rem_id, server):
        """ Read the resource with the given id from the given server. The
        passed-in server instance must support a `request_json()` method call,
        taking a relative path as first (and only mandatory) argument.
        
        :param str rem_id: The id of the resource on the remote server
        :param FHIRServer server: An instance of a FHIR server or compatible class
        :returns: An instance of the receiving class
        """
        if not rem_id:
            raise Exception("Cannot read resource without remote id")
        
        path = '{}/{}'.format(cls.resource_name, rem_id)
        instance = cls.read_from(path, server)
        instance._remote_id = rem_id
        
        return instance
    
    @classmethod
    def read_from(cls, path, server):
        """ Requests data from the given REST path on the server and creates
        an instance of the receiving class.
        
        :param str path: The REST path to read from
        :param FHIRServer server: An instance of a FHIR server or compatible class
        :returns: An instance of the receiving class
        """
        if not path:
            raise Exception("Cannot read resource without REST path")
        if server is None:
            raise Exception("Cannot read resource without server instance")
        
        ret = server.request_json(path)
        instance = cls(jsondict=ret)
        instance._server = server
        
        return instance
    
    
    # MARK: Search
    
    def search(self, struct=None):
        """ Search can be started in two ways:
        
          - via a dictionary containing a search construct
          - by chaining FHIRSearchElement instances
        
        Calling this method with a search struct will return a `FHIRSearch`
        object representing the search struct. Not supplying a search struct
        will return a `FHIRSearchElement` instance which will accept subsequent
        search elements and create a chain.
        
        :param dict struct: An optional search structure
        :returns: A FHIRSearch or FHIRSearchElement instance
        """
        if struct is None and self._remote_id is not None:
            p = fhirsearchelement.FHIRSearchElement('_id')        # TODO: currently the subject of the first search element is ignored, make this work
            p.reference = self._remote_id
            p.resource_type = self.__class__
            return p
        return self.__class__.where(struct)
    
    @classmethod
    def where(cls, struct=None):
        """ Search can be started in two ways:
        
          - via a dictionary containing a search construct
          - by chaining FHIRSearchElement instances
        
        Calling this method with a search struct will return a `FHIRSearch`
        object representing the search struct. Not supplying a search struct
        will return a `FHIRSearchElement` instance which will accept subsequent
        search elements and create a chain.
        
        :param dict struct: An optional search structure
        :returns: A FHIRSearch or FHIRSearchElement instance
        """
        if struct is not None:
            return fhirsearch.FHIRSearch(cls, struct)
        
        p = fhirsearchelement.FHIRSearchElement(None)
        p.resource_type = cls
        return p
    
