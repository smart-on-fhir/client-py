#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Meta) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import fhirdate
import fhirelement


class Meta(fhirelement.FHIRElement):
    """ Metadata about a resource.
    
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not always be
    associated with version changes to the resource.
    """
    
    resource_name = "Meta"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.lastUpdated = None
        """ When the resource version last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profiles this resource claims to conform to.
        List of `str` items. """
        
        self.security = None
        """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.tag = None
        """ Tags applied.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.versionId = None
        """ Version specific identifier.
        Type `str`. """
        
        super(Meta, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Meta, self).update_with_json(jsondict)
        if 'lastUpdated' in jsondict:
            self.lastUpdated = fhirdate.FHIRDate.with_json_and_owner(jsondict['lastUpdated'], self)
        if 'profile' in jsondict:
            self.profile = jsondict['profile']
        if 'security' in jsondict:
            self.security = coding.Coding.with_json_and_owner(jsondict['security'], self)
        if 'tag' in jsondict:
            self.tag = coding.Coding.with_json_and_owner(jsondict['tag'], self)
        if 'versionId' in jsondict:
            self.versionId = jsondict['versionId']

