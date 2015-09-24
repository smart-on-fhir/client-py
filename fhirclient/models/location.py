#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Location) on 2015-09-24.
#  2015, SMART Health IT.


from . import address
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirelement
from . import fhirreference
from . import identifier


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
        """ Description of the location.
        Type `str`. """
        
        self.identifier = None
        """ Unique code or number identifying the location to its users.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization responsible for provisioning and upkeep.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.mode = None
        """ instance | kind.
        Type `str`. """
        
        self.name = None
        """ Name of the location as used by humans.
        Type `str`. """
        
        self.partOf = None
        """ Another Location this one is physically part of.
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
        """ Type of function performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Location, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Location, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False),
            ("description", "description", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False),
            ("mode", "mode", str, False),
            ("name", "name", str, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False),
            ("position", "position", LocationPosition, False),
            ("status", "status", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


class LocationPosition(fhirelement.FHIRElement):
    """ The absolute geographic location.
    
    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
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
    
    def elementProperties(self):
        js = super(LocationPosition, self).elementProperties()
        js.extend([
            ("altitude", "altitude", float, False),
            ("latitude", "latitude", float, False),
            ("longitude", "longitude", float, False),
        ])
        return js

