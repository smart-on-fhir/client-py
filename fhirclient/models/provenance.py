#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (provenance.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import period


class Provenance(fhirresource.FHIRResource):
    """ Who, What, When for a set of resources.
    
    Provenance information that describes the activity that led to the creation
    of a set of resources. This information can be used to help determine their
    reliability or trace where the information in them came from. The focus of
    the provenance resource is record keeping, audit and traceability, and not
    explicit statements of clinical significance.
    """
    
    resource_name = "Provenance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.agent = None
        """ Person, organization, records, etc. involved in creating resource.
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """
        
        self.entity = None
        """ An entity used in this activity.
        List of `ProvenanceEntity` items (represented as `dict` in JSON). """
        
        self.integritySignature = None
        """ Base64 signature (DigSig) - integrity check.
        Type `str`. """
        
        self.location = None
        """ Where the activity occurred, if relevant.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.period = None
        """ When the activity occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.policy = None
        """ Policy or plan the activity was defined by.
        List of `str` items. """
        
        self.reason = None
        """ Reason the activity is occurring.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.recorded = None
        """ When the activity was recorded / updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.target = None
        """ Target Reference(s) (usually version specific).
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        super(Provenance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Provenance, self).update_with_json(jsondict)
        if 'agent' in jsondict:
            self.agent = ProvenanceAgent.with_json_and_owner(jsondict['agent'], self)
        if 'entity' in jsondict:
            self.entity = ProvenanceEntity.with_json_and_owner(jsondict['entity'], self)
        if 'integritySignature' in jsondict:
            self.integritySignature = jsondict['integritySignature']
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'policy' in jsondict:
            self.policy = jsondict['policy']
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'recorded' in jsondict:
            self.recorded = fhirdate.FHIRDate.with_json_and_owner(jsondict['recorded'], self)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)


class ProvenanceAgent(fhirelement.FHIRElement):
    """ Person, organization, records, etc. involved in creating resource.
    
    An agent takes a role in an activity such that the agent can be assigned
    some degree of responsibility for the activity taking place. An agent can
    be a person, a piece of software, an inanimate object, an organization, or
    other entities that may be ascribed responsibility.
    """
    
    resource_name = "ProvenanceAgent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.display = None
        """ Human description of participant.
        Type `str`. """
        
        self.reference = None
        """ Identity of agent (urn or url).
        Type `str`. """
        
        self.role = None
        """ e.g. author | overseer | enterer | attester | source | cc: +.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None
        """ e.g. Resource | Person | Application | Record | Document +.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ProvenanceAgent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProvenanceAgent, self).update_with_json(jsondict)
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'reference' in jsondict:
            self.reference = jsondict['reference']
        if 'role' in jsondict:
            self.role = coding.Coding.with_json_and_owner(jsondict['role'], self)
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)


class ProvenanceEntity(fhirelement.FHIRElement):
    """ An entity used in this activity.
    """
    
    resource_name = "ProvenanceEntity"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.agent = None
        """ Person, organization, records, etc. involved in creating resource.
        Type `ProvenanceAgent` (represented as `dict` in JSON). """
        
        self.display = None
        """ Human description of participant.
        Type `str`. """
        
        self.reference = None
        """ Identity of participant (urn or url).
        Type `str`. """
        
        self.role = None
        """ derivation | revision | quotation | source.
        Type `str`. """
        
        self.type = None
        """ Resource Type, or something else.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ProvenanceEntity, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProvenanceEntity, self).update_with_json(jsondict)
        if 'agent' in jsondict:
            self.agent = ProvenanceAgent.with_json_and_owner(jsondict['agent'], self)
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'reference' in jsondict:
            self.reference = jsondict['reference']
        if 'role' in jsondict:
            self.role = jsondict['role']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)

