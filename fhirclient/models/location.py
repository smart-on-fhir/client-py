# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Location).
# 2024, SMART Health IT.


from . import domainresource

class Location(domainresource.DomainResource):
    """ Details and position information for a physical place.
    
    Details and position information for a physical place where services are
    provided and resources and participants may be stored, found, contained, or
    accommodated.
    """
    
    resource_type = "Location"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Physical location.
        Type `Address` (represented as `dict` in JSON). """
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.alias = None
        """ A list of alternate names that the location is known as, or was
        known as, in the past.
        List of `str` items. """
        self._alias = None
        """ Primitive extension for alias. Type `FHIRPrimitiveExtension` """
        
        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `str`. """
        self._availabilityExceptions = None
        """ Primitive extension for availabilityExceptions. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Additional details about the location that could be displayed as
        further information to identify the location beyond its name.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.hoursOfOperation = None
        """ What days/times during a week is this location usually open.
        List of `LocationHoursOfOperation` items (represented as `dict` in JSON). """
        self._hoursOfOperation = None
        """ Primitive extension for hoursOfOperation. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Unique code or number identifying the location to its users.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.managingOrganization = None
        """ Organization responsible for provisioning and upkeep.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._managingOrganization = None
        """ Primitive extension for managingOrganization. Type `FHIRPrimitiveExtension` """
        
        self.mode = None
        """ instance | kind.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name of the location as used by humans.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.operationalStatus = None
        """ The operational status of the location (typically only for a
        bed/room).
        Type `Coding` (represented as `dict` in JSON). """
        self._operationalStatus = None
        """ Primitive extension for operationalStatus. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Another Location this one is physically a part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.physicalType = None
        """ Physical form of the location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._physicalType = None
        """ Primitive extension for physicalType. Type `FHIRPrimitiveExtension` """
        
        self.position = None
        """ The absolute geographic location.
        Type `LocationPosition` (represented as `dict` in JSON). """
        self._position = None
        """ Primitive extension for position. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | suspended | inactive.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ Contact details of the location.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of function performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Location, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Location, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("_alias", "_alias", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("_availabilityExceptions", "_availabilityExceptions", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("hoursOfOperation", "hoursOfOperation", LocationHoursOfOperation, True, None, False),
            ("_hoursOfOperation", "_hoursOfOperation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("_managingOrganization", "_managingOrganization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operationalStatus", "operationalStatus", coding.Coding, False, None, False),
            ("_operationalStatus", "_operationalStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False, None, False),
            ("_physicalType", "_physicalType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("position", "position", LocationPosition, False, None, False),
            ("_position", "_position", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class LocationHoursOfOperation(backboneelement.BackboneElement):
    """ What days/times during a week is this location usually open.
    """
    
    resource_type = "LocationHoursOfOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay = None
        """ The Location is open all day.
        Type `bool`. """
        self._allDay = None
        """ Primitive extension for allDay. Type `FHIRPrimitiveExtension` """
        
        self.closingTime = None
        """ Time that the Location closes.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._closingTime = None
        """ Primitive extension for closingTime. Type `FHIRPrimitiveExtension` """
        
        self.daysOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        self._daysOfWeek = None
        """ Primitive extension for daysOfWeek. Type `FHIRPrimitiveExtension` """
        
        self.openingTime = None
        """ Time that the Location opens.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._openingTime = None
        """ Primitive extension for openingTime. Type `FHIRPrimitiveExtension` """
        
        super(LocationHoursOfOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LocationHoursOfOperation, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("_allDay", "_allDay", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("closingTime", "closingTime", fhirtime.FHIRTime, False, None, False),
            ("_closingTime", "_closingTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("_daysOfWeek", "_daysOfWeek", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("openingTime", "openingTime", fhirtime.FHIRTime, False, None, False),
            ("_openingTime", "_openingTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class LocationPosition(backboneelement.BackboneElement):
    """ The absolute geographic location.
    
    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """
    
    resource_type = "LocationPosition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.altitude = None
        """ Altitude with WGS84 datum.
        Type `float`. """
        self._altitude = None
        """ Primitive extension for altitude. Type `FHIRPrimitiveExtension` """
        
        self.latitude = None
        """ Latitude with WGS84 datum.
        Type `float`. """
        self._latitude = None
        """ Primitive extension for latitude. Type `FHIRPrimitiveExtension` """
        
        self.longitude = None
        """ Longitude with WGS84 datum.
        Type `float`. """
        self._longitude = None
        """ Primitive extension for longitude. Type `FHIRPrimitiveExtension` """
        
        super(LocationPosition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LocationPosition, self).elementProperties()
        js.extend([
            ("altitude", "altitude", float, False, None, False),
            ("_altitude", "_altitude", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("latitude", "latitude", float, False, None, True),
            ("_latitude", "_latitude", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("longitude", "longitude", float, False, None, True),
            ("_longitude", "_longitude", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import address
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference
from . import fhirtime
from . import identifier