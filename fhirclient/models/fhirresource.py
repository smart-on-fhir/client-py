#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Base class for FHIR resources.
#  2014, SMART Health IT.

import fhirelement
import fhirdate
import fhirsearch
import fhirelementfactory


class FHIRResource(fhirelement.FHIRElement):
    """ Extends the FHIRElement base class with server talking capabilities.
    """
    resource_name = 'Resource'
    
    def __init__(self, jsondict=None):
        self._local_id = None
        """ If the instance was read from a server, this is the id that was
        used, likely the same as `id`. """
        
        self._server = None
        """ The server the instance was read from. """
        
        super(FHIRResource, self).__init__(jsondict)
    
    @classmethod
    def with_json(cls, jsonobj):
        """ Overridden to use a factory if called on the base resource and
        "resourceType" is defined in the JSON.
        """
        if 'Resource' == cls.resource_name:     # cannot use isinstance(cls, FHIRResource) because of module mismatch
            if isinstance(jsonobj, dict) and 'resourceType' in jsonobj:
                return fhirelementfactory.FHIRElementFactory.instantiate(jsonobj['resourceType'], jsonobj)
        return super(FHIRResource, cls).with_json(jsonobj)
    
    
    # MARK: Server Connection
    
    def server(self):
        """ Walks the owner hierarchy until it finds an owner with a server.
        """
        if self._server is not None:
            return self._server
        owningRes = self.owningResource()
        return owningRes.server() if owningRes is not None else None
    
    def owningResource(self):
        """ Walks the owner hierarchy and returns the next parent that is a
        FHIRResource instance.
        """
        owner = self._owner
        while owner is not None:
            if isinstance(owner, self.__class__):
                break
            owner = owner._owner
        return owner
    
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
        instance._local_id = rem_id
        
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
        """ Search can be started via a dictionary containing a search
        construct.
        
        Calling this method with a search struct will return a `FHIRSearch`
        object representing the search struct, with "$type" and "id" added.
        
        :param dict struct: An optional search structure
        :returns: A FHIRSearch instance
        """
        if struct is None:
            struct = {'$type': self.__class__.resource_name}
        if self._local_id is not None or self.id is not None:
            struct['id'] = self._local_id or self.id
        return self.__class__.where(struct)
    
    @classmethod
    def where(cls, struct):
        """ Search can be started via a dictionary containing a search
        construct.
        
        Calling this method with a search struct will return a `FHIRSearch`
        object representing the search struct
        
        :param dict struct: A search structure
        :returns: A FHIRSearch instance
        """
        return fhirsearch.FHIRSearch(cls, struct)

