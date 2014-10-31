#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (provenance.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import location
import narrative
import period


class Provenance(fhirresource.FHIRResource):
    """ Who, What, When for a set of resources.
    
    Scope and Usage The provenance resource tracks information about activity
    that created a version of a resource, including the entities, and agents
    involved in producing a resource. This information can be used to form
    assessments about its quality, reliability or trustworthiness, or to
    provide pointers for where to go to further investigate the origins of the
    resource and the information in it.
    
    Provenance resources are a record-keeping assertion that gathers
    information about the context in which the information in a resource was
    obtained. Provenance resources are prepared by the application that
    initiates the create/update etc. of the resource. A Security Event resource
    contains overlapping information, but is created as events occur, to track
    and audit the events. Security Event resources are often (though not
    exclusively) created by the application responding to the
    read/query/create/update etc. event.
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
        """ Target resource(s) (usually version specific).
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(Provenance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Provenance, self).update_with_json(jsondict)
        if 'agent' in jsondict:
            self.agent = ProvenanceAgent.with_json(jsondict['agent'])
        if 'entity' in jsondict:
            self.entity = ProvenanceEntity.with_json(jsondict['entity'])
        if 'integritySignature' in jsondict:
            self.integritySignature = jsondict['integritySignature']
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self, location.Location)
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])
        if 'policy' in jsondict:
            self.policy = jsondict['policy']
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json(jsondict['reason'])
        if 'recorded' in jsondict:
            self.recorded = fhirdate.FHIRDate.with_json(jsondict['recorded'])
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self, fhirresource.FHIRResource)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class ProvenanceAgent(fhirelement.FHIRElement):
    """ Person, organization, records, etc. involved in creating resource.
    
    An agent takes a role in an activity such that the agent can be assigned
    some degree of responsibility for the activity taking place. An agent can
    be a person, a piece of software, an inanimate object, an organization, or
    other entities that may be ascribed responsibility.
    """
    
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
            self.role = coding.Coding.with_json(jsondict['role'])
        if 'type' in jsondict:
            self.type = coding.Coding.with_json(jsondict['type'])


class ProvenanceEntity(fhirelement.FHIRElement):
    """ An entity used in this activity.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.agent = None
        """ Entity is attributed to this agent.
        Type `ProvenanceEntityAgent` (represented as `dict` in JSON). """
        
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
            self.agent = ProvenanceEntityAgent.with_json(jsondict['agent'])
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'reference' in jsondict:
            self.reference = jsondict['reference']
        if 'role' in jsondict:
            self.role = jsondict['role']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json(jsondict['type'])


class ProvenanceEntityAgent(fhirelement.FHIRElement):
    """ Entity is attributed to this agent.
    
    The entity is attributed to an agent to express the agent's responsibility
    for that entity, possibly along with other agents. This description can be
    understood as shorthand for saying that the agent was responsible for the
    activity which generated the entity.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(ProvenanceEntityAgent, self).__init__(jsondict)

