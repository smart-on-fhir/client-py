#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Base class for FHIR resources.
#  2014, SMART Platforms.

import fhirelement
import fhirdate
import fhirsearch


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
        
        self.id = None
        """ Logical id of this artefact. """
        
        self.meta = None
        """ Metadata about the resource. """
        
        self.implicitRules = None
        """ A set of rules under which this content was created. """
        
        self.language = None
        """ Human language of the content (BCP-47). """
        
        self.narrative = None
        """ A human-readable narrative. """
        
        super(FHIRResource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(FHIRResource, self).update_with_json(jsondict)
        if 'id' in jsondict:
            self.id = jsondict['id']
        if 'meta' in jsondict:
            self.meta = FHIRResourceMeta(jsondict['meta'])
        if 'implicitRules' in jsondict:
            self.implicitRules = jsondict['implicitRules']
        if 'language' in jsondict:
            self.language = jsondict['language']
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


class FHIRResourceMeta(fhirelement.FHIRElement):
    """ Metadata about a resource.
    """
    def __init__(self, jsondict=None):
        self.versionId = None
        """ Version specific identifier (a str). """
        
        self.lastUpdated = None
        """ When the resource version last changed (as FHIRDate). """
        
        self.profiles = None
        """ Profiles this resource claims to conform to (a list of URLs). """
        
        self.security = None
        """ Security Labels applied to this resource (a list of Coding). """
        
        self.tags = None
        """ Tags applied (a list of Coding instances). """
        
        super(FHIRResourceMeta, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(FHIRResourceMeta, self).update_with_json(jsondict)
        if "versionId" in jsondict:
            self.versionId = jsondict["versionId"]
        if "lastUpdated" in jsondict:
            self.lastUpdated = fhirdate.FHIRDate(jsondict["lastUpdated"])
        if "profiles" in jsondict:
            self.profiles = jsondict["profiles"]
        if "security" in jsondict:
            self.security = coding.Coding.with_json(jsondict["security"])
        if "tags" in jsondict:
            self.tags = coding.Coding.with_json(jsondict["tags"])


import coding
import narrative
