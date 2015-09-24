#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


class AuditEvent(domainresource.DomainResource):
    """ Event record kept for security purposes.
    
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """
    
    resource_name = "AuditEvent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.event = None
        """ What was done.
        Type `AuditEventEvent` (represented as `dict` in JSON). """
        
        self.object = None
        """ Specific instances of data or objects that have been accessed.
        List of `AuditEventObject` items (represented as `dict` in JSON). """
        
        self.participant = None
        """ A person, a hardware device or software process.
        List of `AuditEventParticipant` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Application systems and processes.
        Type `AuditEventSource` (represented as `dict` in JSON). """
        
        super(AuditEvent, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AuditEvent, self).elementProperties()
        js.extend([
            ("event", "event", AuditEventEvent, False),
            ("object", "object", AuditEventObject, True),
            ("participant", "participant", AuditEventParticipant, True),
            ("source", "source", AuditEventSource, False),
        ])
        return js


class AuditEventEvent(fhirelement.FHIRElement):
    """ What was done.
    
    Identifies the name, action type, time, and disposition of the audited
    event.
    """
    
    resource_name = "AuditEventEvent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ Type of action performed during the event.
        Type `str`. """
        
        self.dateTime = None
        """ Time when the event occurred on source.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.outcome = None
        """ Whether the event succeeded or failed.
        Type `str`. """
        
        self.outcomeDesc = None
        """ Description of the event outcome.
        Type `str`. """
        
        self.purposeOfEvent = None
        """ The purposeOfUse of the event.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.subtype = None
        """ More specific type/id for the event.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type/identifier of event.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(AuditEventEvent, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AuditEventEvent, self).elementProperties()
        js.extend([
            ("action", "action", str, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False),
            ("outcome", "outcome", str, False),
            ("outcomeDesc", "outcomeDesc", str, False),
            ("purposeOfEvent", "purposeOfEvent", coding.Coding, True),
            ("subtype", "subtype", coding.Coding, True),
            ("type", "type", coding.Coding, False),
        ])
        return js


class AuditEventObject(fhirelement.FHIRElement):
    """ Specific instances of data or objects that have been accessed.
    """
    
    resource_name = "AuditEventObject"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Descriptive text.
        Type `str`. """
        
        self.detail = None
        """ Additional Information about the Object.
        List of `AuditEventObjectDetail` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Specific instance of object (e.g. versioned).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.lifecycle = None
        """ Life-cycle stage for the object.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None
        """ Instance-specific descriptor for Object.
        Type `str`. """
        
        self.query = None
        """ Actual query for object.
        Type `str`. """
        
        self.reference = None
        """ Specific instance of resource (e.g. versioned).
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.role = None
        """ What role the Object played.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ Security labels applied to the object.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of object involved.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(AuditEventObject, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AuditEventObject, self).elementProperties()
        js.extend([
            ("description", "description", str, False),
            ("detail", "detail", AuditEventObjectDetail, True),
            ("identifier", "identifier", identifier.Identifier, False),
            ("lifecycle", "lifecycle", coding.Coding, False),
            ("name", "name", str, False),
            ("query", "query", str, False),
            ("reference", "reference", fhirreference.FHIRReference, False),
            ("role", "role", coding.Coding, False),
            ("securityLabel", "securityLabel", coding.Coding, True),
            ("type", "type", coding.Coding, False),
        ])
        return js


class AuditEventObjectDetail(fhirelement.FHIRElement):
    """ Additional Information about the Object.
    """
    
    resource_name = "AuditEventObjectDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.type = None
        """ Name of the property.
        Type `str`. """
        
        self.value = None
        """ Property value.
        Type `str`. """
        
        super(AuditEventObjectDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AuditEventObjectDetail, self).elementProperties()
        js.extend([
            ("type", "type", str, False),
            ("value", "value", str, False),
        ])
        return js


class AuditEventParticipant(fhirelement.FHIRElement):
    """ A person, a hardware device or software process.
    """
    
    resource_name = "AuditEventParticipant"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.altId = None
        """ Alternative User id e.g. authentication.
        Type `str`. """
        
        self.location = None
        """ Where.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.media = None
        """ Type of media.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None
        """ Human-meaningful name for the user.
        Type `str`. """
        
        self.network = None
        """ Logical network location for application activity.
        Type `AuditEventParticipantNetwork` (represented as `dict` in JSON). """
        
        self.policy = None
        """ Policy that authorized event.
        List of `str` items. """
        
        self.purposeOfUse = None
        """ Reason given for this user.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ Direct reference to resource.
        Type `FHIRReference` referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.requestor = None
        """ Whether user is initiator.
        Type `bool`. """
        
        self.role = None
        """ User roles (e.g. local RBAC codes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.userId = None
        """ Unique identifier for the user.
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(AuditEventParticipant, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AuditEventParticipant, self).elementProperties()
        js.extend([
            ("altId", "altId", str, False),
            ("location", "location", fhirreference.FHIRReference, False),
            ("media", "media", coding.Coding, False),
            ("name", "name", str, False),
            ("network", "network", AuditEventParticipantNetwork, False),
            ("policy", "policy", str, True),
            ("purposeOfUse", "purposeOfUse", coding.Coding, True),
            ("reference", "reference", fhirreference.FHIRReference, False),
            ("requestor", "requestor", bool, False),
            ("role", "role", codeableconcept.CodeableConcept, True),
            ("userId", "userId", identifier.Identifier, False),
        ])
        return js


class AuditEventParticipantNetwork(fhirelement.FHIRElement):
    """ Logical network location for application activity.
    
    Logical network location for application activity, if the activity has a
    network location.
    """
    
    resource_name = "AuditEventParticipantNetwork"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Identifier for the network access point of the user device.
        Type `str`. """
        
        self.type = None
        """ The type of network access point.
        Type `str`. """
        
        super(AuditEventParticipantNetwork, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AuditEventParticipantNetwork, self).elementProperties()
        js.extend([
            ("address", "address", str, False),
            ("type", "type", str, False),
        ])
        return js


class AuditEventSource(fhirelement.FHIRElement):
    """ Application systems and processes.
    """
    
    resource_name = "AuditEventSource"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ The identity of source detecting the event.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.site = None
        """ Logical source location within the enterprise.
        Type `str`. """
        
        self.type = None
        """ The type of source where event originated.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(AuditEventSource, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AuditEventSource, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False),
            ("site", "site", str, False),
            ("type", "type", coding.Coding, True),
        ])
        return js

