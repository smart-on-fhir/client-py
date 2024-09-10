# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Schedule).
# 2024, SMART Health IT.


from . import domainresource

class Schedule(domainresource.DomainResource):
    """ A container for slots of time that may be available for booking
    appointments.
    """
    
    resource_type = "Schedule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this schedule is in active use.
        Type `bool`. """
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.actor = None
        """ Resource(s) that availability information is being provided for.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Comments on availability.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.planningHorizon = None
        """ Period of time covered by schedule.
        Type `Period` (represented as `dict` in JSON). """
        self._planningHorizon = None
        """ Primitive extension for planningHorizon. Type `FHIRPrimitiveExtension` """
        
        self.serviceCategory = None
        """ High-level category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._serviceCategory = None
        """ Primitive extension for serviceCategory. Type `FHIRPrimitiveExtension` """
        
        self.serviceType = None
        """ Specific service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._serviceType = None
        """ Primitive extension for serviceType. Type `FHIRPrimitiveExtension` """
        
        self.specialty = None
        """ Type of specialty needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._specialty = None
        """ Primitive extension for specialty. Type `FHIRPrimitiveExtension` """
        
        super(Schedule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Schedule, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("actor", "actor", fhirreference.FHIRReference, True, None, True),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("planningHorizon", "planningHorizon", period.Period, False, None, False),
            ("_planningHorizon", "_planningHorizon", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False),
            ("_serviceCategory", "_serviceCategory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("_serviceType", "_serviceType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("_specialty", "_specialty", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period