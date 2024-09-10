# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Provenance).
# 2024, SMART Health IT.


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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._activity = None
        """ Primitive extension for activity. Type `FHIRPrimitiveExtension` """
        
        self.agent = None
        """ Actor involved.
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """
        self._agent = None
        """ Primitive extension for agent. Type `FHIRPrimitiveExtension` """
        
        self.entity = None
        """ An entity used in this activity.
        List of `ProvenanceEntity` items (represented as `dict` in JSON). """
        self._entity = None
        """ Primitive extension for entity. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Where the activity occurred, if relevant.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.occurredDateTime = None
        """ When the activity occurred.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._occurredDateTime = None
        """ Primitive extension for occurredDateTime. Type `FHIRPrimitiveExtension` """
        
        self.occurredPeriod = None
        """ When the activity occurred.
        Type `Period` (represented as `dict` in JSON). """
        self._occurredPeriod = None
        """ Primitive extension for occurredPeriod. Type `FHIRPrimitiveExtension` """
        
        self.policy = None
        """ Policy or plan the activity was defined by.
        List of `str` items. """
        self._policy = None
        """ Primitive extension for policy. Type `FHIRPrimitiveExtension` """
        
        self.reason = None
        """ Reason the activity is occurring.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reason = None
        """ Primitive extension for reason. Type `FHIRPrimitiveExtension` """
        
        self.recorded = None
        """ When the activity was recorded / updated.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._recorded = None
        """ Primitive extension for recorded. Type `FHIRPrimitiveExtension` """
        
        self.signature = None
        """ Signature on target.
        List of `Signature` items (represented as `dict` in JSON). """
        self._signature = None
        """ Primitive extension for signature. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Target Reference(s) (usually version specific).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        super(Provenance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Provenance, self).elementProperties()
        js.extend([
            ("activity", "activity", codeableconcept.CodeableConcept, False, None, False),
            ("_activity", "_activity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("agent", "agent", ProvenanceAgent, True, None, True),
            ("_agent", "_agent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("entity", "entity", ProvenanceEntity, True, None, False),
            ("_entity", "_entity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurredDateTime", "occurredDateTime", fhirdatetime.FHIRDateTime, False, "occurred", False),
            ("_occurredDateTime", "_occurredDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurredPeriod", "occurredPeriod", period.Period, False, "occurred", False),
            ("_occurredPeriod", "_occurredPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("_policy", "_policy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recorded", "recorded", fhirinstant.FHIRInstant, False, None, True),
            ("_recorded", "_recorded", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("signature", "signature", signature.Signature, True, None, False),
            ("_signature", "_signature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", fhirreference.FHIRReference, True, None, True),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        
        self.onBehalfOf = None
        """ Who the agent is representing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._onBehalfOf = None
        """ Primitive extension for onBehalfOf. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ What the agents role was.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ How the agent participated.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.who = None
        """ Who participated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._who = None
        """ Primitive extension for who. Type `FHIRPrimitiveExtension` """
        
        super(ProvenanceAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceAgent, self).elementProperties()
        js.extend([
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("_onBehalfOf", "_onBehalfOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, True),
            ("_who", "_who", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._agent = None
        """ Primitive extension for agent. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ derivation | revision | quotation | source | removal.
        Type `str`. """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        self.what = None
        """ Identity of entity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._what = None
        """ Primitive extension for what. Type `FHIRPrimitiveExtension` """
        
        super(ProvenanceEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceEntity, self).elementProperties()
        js.extend([
            ("agent", "agent", ProvenanceAgent, True, None, False),
            ("_agent", "_agent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", str, False, None, True),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("what", "what", fhirreference.FHIRReference, False, None, True),
            ("_what", "_what", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import period
from . import signature