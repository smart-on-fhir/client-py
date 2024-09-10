# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AuditEvent).
# 2024, SMART Health IT.


from . import domainresource

class AuditEvent(domainresource.DomainResource):
    """ Event record kept for security purposes.
    
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """
    
    resource_type = "AuditEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Type of action performed during the event.
        Type `str`. """
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        self.agent = None
        """ Actor involved in the event.
        List of `AuditEventAgent` items (represented as `dict` in JSON). """
        self._agent = None
        """ Primitive extension for agent. Type `FHIRPrimitiveExtension` """
        
        self.entity = None
        """ Data or objects used.
        List of `AuditEventEntity` items (represented as `dict` in JSON). """
        self._entity = None
        """ Primitive extension for entity. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ Whether the event succeeded or failed.
        Type `str`. """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.outcomeDesc = None
        """ Description of the event outcome.
        Type `str`. """
        self._outcomeDesc = None
        """ Primitive extension for outcomeDesc. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ When the activity occurred.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.purposeOfEvent = None
        """ The purposeOfUse of the event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._purposeOfEvent = None
        """ Primitive extension for purposeOfEvent. Type `FHIRPrimitiveExtension` """
        
        self.recorded = None
        """ Time when the event was recorded.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._recorded = None
        """ Primitive extension for recorded. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Audit Event Reporter.
        Type `AuditEventSource` (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.subtype = None
        """ More specific type/id for the event.
        List of `Coding` items (represented as `dict` in JSON). """
        self._subtype = None
        """ Primitive extension for subtype. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type/identifier of event.
        Type `Coding` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(AuditEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEvent, self).elementProperties()
        js.extend([
            ("action", "action", str, False, None, False),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("agent", "agent", AuditEventAgent, True, None, True),
            ("_agent", "_agent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("entity", "entity", AuditEventEntity, True, None, False),
            ("_entity", "_entity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcomeDesc", "outcomeDesc", str, False, None, False),
            ("_outcomeDesc", "_outcomeDesc", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purposeOfEvent", "purposeOfEvent", codeableconcept.CodeableConcept, True, None, False),
            ("_purposeOfEvent", "_purposeOfEvent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recorded", "recorded", fhirinstant.FHIRInstant, False, None, True),
            ("_recorded", "_recorded", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", AuditEventSource, False, None, True),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subtype", "subtype", coding.Coding, True, None, False),
            ("_subtype", "_subtype", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class AuditEventAgent(backboneelement.BackboneElement):
    """ Actor involved in the event.
    
    An actor taking an active role in the event or activity that is logged.
    """
    
    resource_type = "AuditEventAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.altId = None
        """ Alternative User identity.
        Type `str`. """
        self._altId = None
        """ Primitive extension for altId. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Where.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.media = None
        """ Type of media.
        Type `Coding` (represented as `dict` in JSON). """
        self._media = None
        """ Primitive extension for media. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Human friendly name for the agent.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.network = None
        """ Logical network location for application activity.
        Type `AuditEventAgentNetwork` (represented as `dict` in JSON). """
        self._network = None
        """ Primitive extension for network. Type `FHIRPrimitiveExtension` """
        
        self.policy = None
        """ Policy that authorized event.
        List of `str` items. """
        self._policy = None
        """ Primitive extension for policy. Type `FHIRPrimitiveExtension` """
        
        self.purposeOfUse = None
        """ Reason given for this user.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._purposeOfUse = None
        """ Primitive extension for purposeOfUse. Type `FHIRPrimitiveExtension` """
        
        self.requestor = None
        """ Whether user is initiator.
        Type `bool`. """
        self._requestor = None
        """ Primitive extension for requestor. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ Agent role in the event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ How agent participated.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.who = None
        """ Identifier of who.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._who = None
        """ Primitive extension for who. Type `FHIRPrimitiveExtension` """
        
        super(AuditEventAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventAgent, self).elementProperties()
        js.extend([
            ("altId", "altId", str, False, None, False),
            ("_altId", "_altId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("media", "media", coding.Coding, False, None, False),
            ("_media", "_media", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("network", "network", AuditEventAgentNetwork, False, None, False),
            ("_network", "_network", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("_policy", "_policy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purposeOfUse", "purposeOfUse", codeableconcept.CodeableConcept, True, None, False),
            ("_purposeOfUse", "_purposeOfUse", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestor", "requestor", bool, False, None, True),
            ("_requestor", "_requestor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
            ("_who", "_who", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class AuditEventAgentNetwork(backboneelement.BackboneElement):
    """ Logical network location for application activity.
    
    Logical network location for application activity, if the activity has a
    network location.
    """
    
    resource_type = "AuditEventAgentNetwork"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Identifier for the network access point of the user device.
        Type `str`. """
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of network access point.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(AuditEventAgentNetwork, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventAgentNetwork, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, False),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class AuditEventEntity(backboneelement.BackboneElement):
    """ Data or objects used.
    
    Specific instances of data or objects that have been accessed.
    """
    
    resource_type = "AuditEventEntity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Descriptive text.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Additional Information about the entity.
        List of `AuditEventEntityDetail` items (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.lifecycle = None
        """ Life-cycle stage for the entity.
        Type `Coding` (represented as `dict` in JSON). """
        self._lifecycle = None
        """ Primitive extension for lifecycle. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Descriptor for entity.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.query = None
        """ Query parameters.
        Type `str`. """
        self._query = None
        """ Primitive extension for query. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ What role the entity played.
        Type `Coding` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        self.securityLabel = None
        """ Security labels on the entity.
        List of `Coding` items (represented as `dict` in JSON). """
        self._securityLabel = None
        """ Primitive extension for securityLabel. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of entity involved.
        Type `Coding` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.what = None
        """ Specific instance of resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._what = None
        """ Primitive extension for what. Type `FHIRPrimitiveExtension` """
        
        super(AuditEventEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventEntity, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", AuditEventEntityDetail, True, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lifecycle", "lifecycle", coding.Coding, False, None, False),
            ("_lifecycle", "_lifecycle", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("query", "query", str, False, None, False),
            ("_query", "_query", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", coding.Coding, False, None, False),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("_securityLabel", "_securityLabel", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("what", "what", fhirreference.FHIRReference, False, None, False),
            ("_what", "_what", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class AuditEventEntityDetail(backboneelement.BackboneElement):
    """ Additional Information about the entity.
    
    Tagged value pairs for conveying additional information about the entity.
    """
    
    resource_type = "AuditEventEntityDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Name of the property.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.valueBase64Binary = None
        """ Property value.
        Type `str`. """
        self._valueBase64Binary = None
        """ Primitive extension for valueBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Property value.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        super(AuditEventEntityDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventEntityDetail, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("_valueBase64Binary", "_valueBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class AuditEventSource(backboneelement.BackboneElement):
    """ Audit Event Reporter.
    
    The system that is reporting the event.
    """
    
    resource_type = "AuditEventSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.observer = None
        """ The identity of source detecting the event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._observer = None
        """ Primitive extension for observer. Type `FHIRPrimitiveExtension` """
        
        self.site = None
        """ Logical source location within the enterprise.
        Type `str`. """
        self._site = None
        """ Primitive extension for site. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of source where event originated.
        List of `Coding` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(AuditEventSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventSource, self).elementProperties()
        js.extend([
            ("observer", "observer", fhirreference.FHIRReference, False, None, True),
            ("_observer", "_observer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("site", "site", str, False, None, False),
            ("_site", "_site", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", coding.Coding, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import fhirinstant
from . import fhirreference
from . import period