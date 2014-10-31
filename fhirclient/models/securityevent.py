#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (securityevent.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import practitioner


class SecurityEvent(fhirresource.FHIRResource):
    """ Event record kept for security purposes.
    
    Scope and Usage The security event is based on the ATNA Audit record
    definitions, originally from RFC 3881, and now managed by DICOM (see DICOM
    Part 15 Annex A5). This resource is managed collaboratively between HL7,
    DICOM, and IHE for the MHD/mHealth initiatives.
    
    The primary purpose of this resource is the maintenance of audit log
    information. However, it can also be used for simple event-based
    notification or even general indexing of resources stored in a variety of
    repositories.
    """
    
    resource_name = "SecurityEvent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.event = None
        """ What was done.
        Type `SecurityEventEvent` (represented as `dict` in JSON). """
        
        self.object = None
        """ Specific instances of data or objects that have been accessed.
        List of `SecurityEventObject` items (represented as `dict` in JSON). """
        
        self.participant = None
        """ A person, a hardware device or software process.
        List of `SecurityEventParticipant` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Application systems and processes.
        Type `SecurityEventSource` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(SecurityEvent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SecurityEvent, self).update_with_json(jsondict)
        if 'event' in jsondict:
            self.event = SecurityEventEvent.with_json(jsondict['event'])
        if 'object' in jsondict:
            self.object = SecurityEventObject.with_json(jsondict['object'])
        if 'participant' in jsondict:
            self.participant = SecurityEventParticipant.with_json(jsondict['participant'])
        if 'source' in jsondict:
            self.source = SecurityEventSource.with_json(jsondict['source'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class SecurityEventEvent(fhirelement.FHIRElement):
    """ What was done.
    
    Identifies the name, action type, time, and disposition of the audited
    event.
    """
    
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
        
        self.subtype = None
        """ More specific type/id for the event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type/identifier of event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SecurityEventEvent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SecurityEventEvent, self).update_with_json(jsondict)
        if 'action' in jsondict:
            self.action = jsondict['action']
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json(jsondict['dateTime'])
        if 'outcome' in jsondict:
            self.outcome = jsondict['outcome']
        if 'outcomeDesc' in jsondict:
            self.outcomeDesc = jsondict['outcomeDesc']
        if 'subtype' in jsondict:
            self.subtype = codeableconcept.CodeableConcept.with_json(jsondict['subtype'])
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])


class SecurityEventParticipant(fhirelement.FHIRElement):
    """ A person, a hardware device or software process.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.altId = None
        """ Alternative User id e.g. authentication.
        Type `str`. """
        
        self.media = None
        """ Type of media.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None
        """ Human-meaningful name for the user.
        Type `str`. """
        
        self.network = None
        """ Logical network location for application activity.
        Type `SecurityEventParticipantNetwork` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Direct reference to resource.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.requestor = False
        """ Whether user is initiator.
        Type `bool`. """
        
        self.role = None
        """ User roles (e.g. local RBAC codes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.userId = None
        """ Unique identifier for the user.
        Type `str`. """
        
        super(SecurityEventParticipant, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SecurityEventParticipant, self).update_with_json(jsondict)
        if 'altId' in jsondict:
            self.altId = jsondict['altId']
        if 'media' in jsondict:
            self.media = coding.Coding.with_json(jsondict['media'])
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'network' in jsondict:
            self.network = SecurityEventParticipantNetwork.with_json(jsondict['network'])
        if 'reference' in jsondict:
            self.reference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reference'], self, practitioner.Practitioner)
        if 'requestor' in jsondict:
            self.requestor = jsondict['requestor']
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json(jsondict['role'])
        if 'userId' in jsondict:
            self.userId = jsondict['userId']


class SecurityEventParticipantNetwork(fhirelement.FHIRElement):
    """ Logical network location for application activity.
    
    Logical network location for application activity, if the activity has a
    network location.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Identifier for the network access point of the user device.
        Type `str`. """
        
        self.type = None
        """ The type of network access point.
        Type `str`. """
        
        super(SecurityEventParticipantNetwork, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SecurityEventParticipantNetwork, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'type' in jsondict:
            self.type = jsondict['type']


class SecurityEventSource(fhirelement.FHIRElement):
    """ Application systems and processes.
    """
    
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
        
        super(SecurityEventSource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SecurityEventSource, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'site' in jsondict:
            self.site = jsondict['site']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json(jsondict['type'])


class SecurityEventObject(fhirelement.FHIRElement):
    """ Specific instances of data or objects that have been accessed.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Descriptive text.
        Type `str`. """
        
        self.detail = None
        """ Additional Information about the Object.
        List of `SecurityEventObjectDetail` items (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.role = None
        """ Functional application role of Object.
        Type `str`. """
        
        self.sensitivity = None
        """ Policy-defined sensitivity for the object.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Object type being audited.
        Type `str`. """
        
        super(SecurityEventObject, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SecurityEventObject, self).update_with_json(jsondict)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'detail' in jsondict:
            self.detail = SecurityEventObjectDetail.with_json(jsondict['detail'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'lifecycle' in jsondict:
            self.lifecycle = jsondict['lifecycle']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'query' in jsondict:
            self.query = jsondict['query']
        if 'reference' in jsondict:
            self.reference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reference'], self, fhirresource.FHIRResource)
        if 'role' in jsondict:
            self.role = jsondict['role']
        if 'sensitivity' in jsondict:
            self.sensitivity = codeableconcept.CodeableConcept.with_json(jsondict['sensitivity'])
        if 'type' in jsondict:
            self.type = jsondict['type']


class SecurityEventObjectDetail(fhirelement.FHIRElement):
    """ Additional Information about the Object.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.type = None
        """ Name of the property.
        Type `str`. """
        
        self.value = None
        """ Property value.
        Type `str`. """
        
        super(SecurityEventObjectDetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SecurityEventObjectDetail, self).update_with_json(jsondict)
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'value' in jsondict:
            self.value = jsondict['value']

