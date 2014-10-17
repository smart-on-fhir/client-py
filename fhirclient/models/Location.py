#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (location.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import Address
import CodeableConcept
import Contact
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Narrative
import Organization


class Location(FHIRResource.FHIRResource):
    """ Details and position information for a physical place.
    
    Scope and Usage A Location includes both incidental locations (a place
    which is used for healthcare without prior designation or authorization)
    and dedicated, formally appointed locations. Locations may be private,
    public, mobile or fixed and scale from small freezers to full hospital
    buildings or parking garages.
    
    Examples of Locations are:
    
    * Building, ward, corridor or room
    * Freezer, incubator
    * Vehicle or lift
    * Home, shed, or a garage
    * Road, parking place, a park
    """
    
    resource_name = "Location"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Physical location.
        Type `Address` (represented as `dict` in JSON). """
        
        self.description = None
        """ Description of the Location, which helps in finding or referencing
        the place.
        Type `str`. """
        
        self.identifier = None
        """ Unique code or number identifying the location to its users.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ The organization that is responsible for the provisioning and
        upkeep of the location.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.mode = None
        """ instance | kind.
        Type `str`. """
        
        self.name = None
        """ Name of the location as used by humans.
        Type `str`. """
        
        self.partOf = None
        """ Another Location which this Location is physically part of.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.physicalType = None
        """ Physical form of the location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.position = None
        """ The absolute geographic location.
        Type `LocationPosition` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | suspended | inactive.
        Type `str`. """
        
        self.telecom = None
        """ Contact details of the location.
        List of `Contact` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.type = None
        """ Indicates the type of function performed at the location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Location, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Location, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = Address.Address.with_json(jsondict['address'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'managingOrganization' in jsondict:
            self.managingOrganization = FHIRReference.FHIRReference.with_json_and_owner(jsondict['managingOrganization'], self, Organization.Organization)
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'partOf' in jsondict:
            self.partOf = FHIRReference.FHIRReference.with_json_and_owner(jsondict['partOf'], self, Location)
        if 'physicalType' in jsondict:
            self.physicalType = CodeableConcept.CodeableConcept.with_json(jsondict['physicalType'])
        if 'position' in jsondict:
            self.position = LocationPosition.with_json(jsondict['position'])
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'telecom' in jsondict:
            self.telecom = Contact.Contact.with_json(jsondict['telecom'])
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])


class LocationPosition(FHIRElement.FHIRElement):
    """ The absolute geographic location.
    
    The absolute geographic location of the Location, expressed in a KML
    compatible manner (see notes below for KML).
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.altitude = None
        """ Altitude as expressed in KML.
        Type `float`. """
        
        self.latitude = None
        """ Latitude as expressed in KML.
        Type `float`. """
        
        self.longitude = None
        """ Longitude as expressed in KML.
        Type `float`. """
        
        super(LocationPosition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(LocationPosition, self).update_with_json(jsondict)
        if 'altitude' in jsondict:
            self.altitude = jsondict['altitude']
        if 'latitude' in jsondict:
            self.latitude = jsondict['latitude']
        if 'longitude' in jsondict:
            self.longitude = jsondict['longitude']

