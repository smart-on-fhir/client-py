#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Provenance) on 2017-03-22.
#  2017, SMART Health IT.


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
    
    resource_type = "Provenance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.activity = None
        """ Activity that occurred.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.agent = None
        """ Actor involved.
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
        List of `Coding` items (represented as `dict` in JSON). """
        
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
            ("activity", "activity", coding.Coding, False, None, False),
            ("agent", "agent", ProvenanceAgent, True, None, True),
            ("entity", "entity", ProvenanceEntity, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("reason", "reason", coding.Coding, True, None, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, True),
            ("signature", "signature", signature.Signature, True, None, False),
            ("target", "target", fhirreference.FHIRReference, True, None, True),
        ])
        return js


from . import backboneelement

class ProvenanceAgent(backboneelement.BackboneElement):
    """ Actor involved.
    
    An actor taking a role in an activity  for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    
    resource_type = "ProvenanceAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.onBehalfOfReference = None
        """ Who the agent is representing.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device, Organization` (represented as `dict` in JSON). """
        
        self.onBehalfOfUri = None
        """ Who the agent is representing.
        Type `str`. """
        
        self.relatedAgentType = None
        """ Type of relationship between agents.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.role = None
        """ What the agents role was.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.whoReference = None
        """ Who participated.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device, Organization` (represented as `dict` in JSON). """
        
        self.whoUri = None
        """ Who participated.
        Type `str`. """
        
        super(ProvenanceAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceAgent, self).elementProperties()
        js.extend([
            ("onBehalfOfReference", "onBehalfOfReference", fhirreference.FHIRReference, False, "onBehalfOf", False),
            ("onBehalfOfUri", "onBehalfOfUri", str, False, "onBehalfOf", False),
            ("relatedAgentType", "relatedAgentType", codeableconcept.CodeableConcept, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("whoReference", "whoReference", fhirreference.FHIRReference, False, "who", True),
            ("whoUri", "whoUri", str, False, "who", True),
        ])
        return js


class ProvenanceEntity(backboneelement.BackboneElement):
    """ An entity used in this activity.
    """
    
    resource_type = "ProvenanceEntity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.agent = None
        """ Entity is attributed to this agent.
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """
        
        self.role = None
        """ derivation | revision | quotation | source | removal.
        Type `str`. """
        
        self.whatIdentifier = None
        """ Identity of entity.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.whatReference = None
        """ Identity of entity.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.whatUri = None
        """ Identity of entity.
        Type `str`. """
        
        super(ProvenanceEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceEntity, self).elementProperties()
        js.extend([
            ("agent", "agent", ProvenanceAgent, True, None, False),
            ("role", "role", str, False, None, True),
            ("whatIdentifier", "whatIdentifier", identifier.Identifier, False, "what", True),
            ("whatReference", "whatReference", fhirreference.FHIRReference, False, "what", True),
            ("whatUri", "whatUri", str, False, "what", True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
