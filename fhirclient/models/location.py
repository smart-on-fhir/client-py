#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Location) on 2015-04-08.
#  2015, SMART Health IT.


import address
import codeableconcept
import contactpoint
import domainresource
import fhirelement
import fhirreference
import identifier


class Location(domainresource.DomainResource):
    """ Details and position information for a physical place.
    
    Details and position information for a physical place where services are
    provided  and resources and participants may be stored, found, contained or
    accommodated.
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
        List of `Identifier` items (represented as `dict` in JSON). """
        
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
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Indicates the type of function performed at the location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Location, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Location, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = address.Address.with_json_and_owner(jsondict['address'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'managingOrganization' in jsondict:
            self.managingOrganization = fhirreference.FHIRReference.with_json_and_owner(jsondict['managingOrganization'], self)
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'partOf' in jsondict:
            self.partOf = fhirreference.FHIRReference.with_json_and_owner(jsondict['partOf'], self)
        if 'physicalType' in jsondict:
            self.physicalType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['physicalType'], self)
        if 'position' in jsondict:
            self.position = LocationPosition.with_json_and_owner(jsondict['position'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class LocationPosition(fhirelement.FHIRElement):
    """ The absolute geographic location.
    
    The absolute geographic location of the Location, expressed in with the
    WGS84 datum (This is the same co-ordinate system used in KML).
    """
    
    resource_name = "LocationPosition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.altitude = None
        """ Altitude with WGS84 datum.
        Type `float`. """
        
        self.latitude = None
        """ Latitude with WGS84 datum.
        Type `float`. """
        
        self.longitude = None
        """ Longitude with WGS84 datum.
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

