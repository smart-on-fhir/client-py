#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Provenance) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Provenance(domainresource.DomainResource):
    """ Who, What, When for a set of resources.
    
    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that
    resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement indicates
    clinical significance in terms of confidence in authenticity, reliability,
    and trustworthiness, integrity, and stage in lifecycle (e.g. Document
    Completion - has the artifact been legally authenticated), all of which may
    impact security, privacy, and trust policies.
    """
    
    resource_name = "Provenance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.activity = None
        """ Activity that occurred.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.agent = None
        """ Agents involved in creating resource.
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """
        
        self.entity = None
        """ An entity used in this activity.
        List of `ProvenanceEntity` items (represented as `dict` in JSON). """
        
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.recorded = None
        """ When the activity was recorded / updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.signature = None
        """ Signature on target.
        List of `Signature` items (represented as `dict` in JSON). """
        
        self.target = None
        """ Target Reference(s) (usually version specific).
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(Provenance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Provenance, self).elementProperties()
        js.extend([
            ("activity", "activity", codeableconcept.CodeableConcept, False, None, False),
            ("agent", "agent", ProvenanceAgent, True, None, False),
            ("entity", "entity", ProvenanceEntity, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, True),
            ("signature", "signature", signature.Signature, True, None, False),
            ("target", "target", fhirreference.FHIRReference, True, None, True),
        ])
        return js


from . import backboneelement

class ProvenanceAgent(backboneelement.BackboneElement):
    """ Agents involved in creating resource.
    
    An agent takes a role in an activity such that the agent can be assigned
    some degree of responsibility for the activity taking place. An agent can
    be a person, an organization, software, or other entities that may be
    ascribed responsibility.
    """
    
    resource_name = "ProvenanceAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Individual, device or organization playing role.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device, Organization` (represented as `dict` in JSON). """
        
        self.relatedAgent = None
        """ Track delegation between agents.
        List of `ProvenanceAgentRelatedAgent` items (represented as `dict` in JSON). """
        
        self.role = None
        """ What the agents involvement was.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.userId = None
        """ Authorization-system identifier for the agent.
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(ProvenanceAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceAgent, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("relatedAgent", "relatedAgent", ProvenanceAgentRelatedAgent, True, None, False),
            ("role", "role", coding.Coding, False, None, True),
            ("userId", "userId", identifier.Identifier, False, None, False),
        ])
        return js


class ProvenanceAgentRelatedAgent(backboneelement.BackboneElement):
    """ Track delegation between agents.
    
    A relationship between two the agents referenced in this resource. This is
    defined to allow for explicit description of the delegation between agents.
    For example, this human author used this device, or one person acted on
    another's behest.
    """
    
    resource_name = "ProvenanceAgentRelatedAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.target = None
        """ Reference to other agent in this resource by identifier.
        Type `str`. """
        
        self.type = None
        """ Type of relationship between agents.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProvenanceAgentRelatedAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceAgentRelatedAgent, self).elementProperties()
        js.extend([
            ("target", "target", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ProvenanceEntity(backboneelement.BackboneElement):
    """ An entity used in this activity.
    """
    
    resource_name = "ProvenanceEntity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.agent = None
        """ Entity is attributed to this agent.
        Type `ProvenanceAgent` (represented as `dict` in JSON). """
        
        self.display = None
        """ Human description of entity.
        Type `str`. """
        
        self.reference = None
        """ Identity of entity.
        Type `str`. """
        
        self.role = None
        """ derivation | revision | quotation | source.
        Type `str`. """
        
        self.type = None
        """ The type of resource in this entity.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ProvenanceEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceEntity, self).elementProperties()
        js.extend([
            ("agent", "agent", ProvenanceAgent, False, None, False),
            ("display", "display", str, False, None, False),
            ("reference", "reference", str, False, None, True),
            ("role", "role", str, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import signature
