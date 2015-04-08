#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import coding
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier


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
    
    def update_with_json(self, jsondict):
        super(AuditEvent, self).update_with_json(jsondict)
        if 'event' in jsondict:
            self.event = AuditEventEvent.with_json_and_owner(jsondict['event'], self)
        if 'object' in jsondict:
            self.object = AuditEventObject.with_json_and_owner(jsondict['object'], self)
        if 'participant' in jsondict:
            self.participant = AuditEventParticipant.with_json_and_owner(jsondict['participant'], self)
        if 'source' in jsondict:
            self.source = AuditEventSource.with_json_and_owner(jsondict['source'], self)


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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type/identifier of event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AuditEventEvent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AuditEventEvent, self).update_with_json(jsondict)
        if 'action' in jsondict:
            self.action = jsondict['action']
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateTime'], self)
        if 'outcome' in jsondict:
            self.outcome = jsondict['outcome']
        if 'outcomeDesc' in jsondict:
            self.outcomeDesc = jsondict['outcomeDesc']
        if 'purposeOfEvent' in jsondict:
            self.purposeOfEvent = coding.Coding.with_json_and_owner(jsondict['purposeOfEvent'], self)
        if 'subtype' in jsondict:
            self.subtype = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['subtype'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


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
        Type `str`. """
        
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
        Type `str`. """
        
        self.sensitivity = None
        """ Policy-defined sensitivity for the object.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of object involved.
        Type `str`. """
        
        super(AuditEventObject, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AuditEventObject, self).update_with_json(jsondict)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'detail' in jsondict:
            self.detail = AuditEventObjectDetail.with_json_and_owner(jsondict['detail'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'lifecycle' in jsondict:
            self.lifecycle = jsondict['lifecycle']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'query' in jsondict:
            self.query = jsondict['query']
        if 'reference' in jsondict:
            self.reference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reference'], self)
        if 'role' in jsondict:
            self.role = jsondict['role']
        if 'sensitivity' in jsondict:
            self.sensitivity = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['sensitivity'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']


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
    
    def update_with_json(self, jsondict):
        super(AuditEventObjectDetail, self).update_with_json(jsondict)
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'value' in jsondict:
            self.value = jsondict['value']


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
        """ Participant purposeOfUse.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ Direct reference to resource.
        Type `FHIRReference` referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.requestor = False
        """ Whether user is initiator.
        Type `bool`. """
        
        self.role = None
        """ User roles (e.g. local RBAC codes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.userId = None
        """ Unique identifier for the user.
        Type `str`. """
        
        super(AuditEventParticipant, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AuditEventParticipant, self).update_with_json(jsondict)
        if 'altId' in jsondict:
            self.altId = jsondict['altId']
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'media' in jsondict:
            self.media = coding.Coding.with_json_and_owner(jsondict['media'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'network' in jsondict:
            self.network = AuditEventParticipantNetwork.with_json_and_owner(jsondict['network'], self)
        if 'policy' in jsondict:
            self.policy = jsondict['policy']
        if 'purposeOfUse' in jsondict:
            self.purposeOfUse = coding.Coding.with_json_and_owner(jsondict['purposeOfUse'], self)
        if 'reference' in jsondict:
            self.reference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reference'], self)
        if 'requestor' in jsondict:
            self.requestor = jsondict['requestor']
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['role'], self)
        if 'userId' in jsondict:
            self.userId = jsondict['userId']


class AuditEventParticipantNetwork(fhirelement.FHIRElement):
    """ Logical network location for application activity.
    
    Logical network location for application activity, if the activity has a
    network location.
    """
    
    resource_name = "AuditEventParticipantNetwork"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Identifier for the network access point of the user device.
        Type `str`. """
        
        self.type = None
        """ The type of network access point.
        Type `str`. """
        
        super(AuditEventParticipantNetwork, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AuditEventParticipantNetwork, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'type' in jsondict:
            self.type = jsondict['type']


class AuditEventSource(fhirelement.FHIRElement):
    """ Application systems and processes.
    """
    
    resource_name = "AuditEventSource"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ The id of source where event originated.
        Type `str`. """
        
        self.site = None
        """ Logical source location within the enterprise.
        Type `str`. """
        
        self.type = None
        """ The type of source where event originated.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(AuditEventSource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AuditEventSource, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'site' in jsondict:
            self.site = jsondict['site']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)

