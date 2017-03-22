#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Schedule) on 2017-03-22.
#  2017, SMART Health IT.


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
        
        self.actor = None
        """ The resource this Schedule resource is providing availability
        information for. These are expected to usually be one of
        HealthcareService, Location, Practitioner, PractitionerRole,
        Device, Patient or RelatedPerson.
        List of `FHIRReference` items referencing `Patient, Practitioner, PractitionerRole, RelatedPerson, Device, HealthcareService, Location` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Comments on the availability to describe any extended information.
        Such as custom constraints on the slots that may be associated.
        Type `str`. """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.planningHorizon = None
        """ The period of time that the slots that are attached to this
        Schedule resource cover (even if none exist). These  cover the
        amount of time that an organization's planning horizon; the
        interval for which they are currently accepting appointments. This
        does not define a "template" for planning outside these dates.
        Type `Period` (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ A broad categorisation of the service that is to be performed
        during this appointment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.serviceType = None
        """ The specific service that is to be performed during this
        appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ The specialty of a practitioner that would be required to perform
        the service requested in this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Schedule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Schedule, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("actor", "actor", fhirreference.FHIRReference, True, None, True),
            ("comment", "comment", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("planningHorizon", "planningHorizon", period.Period, False, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, False, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
