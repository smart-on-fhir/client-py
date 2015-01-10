#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (profile.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import coding
import contactpoint
import elementdefinition
import fhirdate
import fhirelement
import fhirresource
import identifier


class Profile(fhirresource.FHIRResource):
    """ Resource Profile.
    
    A Resource Profile - a statement of use of one or more FHIR Resources.  It
    may include constraints on Resources and Data Types, Terminology Binding
    Statements and Extension Definitions.
    """
    
    resource_name = "Profile"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.base = None
        """ Structure that this set of constraints applies to.
        Type `str`. """
        
        self.code = None
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for this version of the profile.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the profile.
        Type `str`. """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None
        """ FHIR Version this profile targets.
        Type `str`. """
        
        self.identifier = None
        """ Other identifiers for the profile.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.mapping = None
        """ External specification that the content is mapped to.
        List of `ProfileMapping` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name for this profile.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Scope and Usage this profile is for.
        Type `str`. """
        
        self.snapshot = None
        """ Snapshot view of the structure.
        Type `ProfileSnapshot` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ The Resource or Data Type being described.
        Type `str`. """
        
        self.url = None
        """ Literal URL used to reference this profile.
        Type `str`. """
        
        self.version = None
        """ Logical id for this version of the profile.
        Type `str`. """
        
        super(Profile, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Profile, self).update_with_json(jsondict)
        if 'base' in jsondict:
            self.base = jsondict['base']
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'fhirVersion' in jsondict:
            self.fhirVersion = jsondict['fhirVersion']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'mapping' in jsondict:
            self.mapping = ProfileMapping.with_json_and_owner(jsondict['mapping'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'snapshot' in jsondict:
            self.snapshot = ProfileSnapshot.with_json_and_owner(jsondict['snapshot'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'version' in jsondict:
            self.version = jsondict['version']


class ProfileMapping(fhirelement.FHIRElement):
    """ External specification that the content is mapped to.
    
    An external specification that the content is mapped to.
    """
    
    resource_name = "ProfileMapping"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comments = None
        """ Versions, Issues, Scope limitations etc.
        Type `str`. """
        
        self.identity = None
        """ Internal id when this mapping is used.
        Type `str`. """
        
        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """
        
        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """
        
        super(ProfileMapping, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileMapping, self).update_with_json(jsondict)
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'identity' in jsondict:
            self.identity = jsondict['identity']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'uri' in jsondict:
            self.uri = jsondict['uri']


class ProfileSnapshot(fhirelement.FHIRElement):
    """ Snapshot view of the structure.
    
    A snapshot view is expressed in a stand alone form that can be used and
    interpreted without considering the base profile.
    """
    
    resource_name = "ProfileSnapshot"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.element = None
        """ Definition of elements in the resource (if no profile).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(ProfileSnapshot, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProfileSnapshot, self).update_with_json(jsondict)
        if 'element' in jsondict:
            self.element = elementdefinition.ElementDefinition.with_json_and_owner(jsondict['element'], self)

