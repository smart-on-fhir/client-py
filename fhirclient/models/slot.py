#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Slot) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Slot(domainresource.DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """
    
    resource_type = "Slot"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.appointmentType = None
        """ The style of appointment or patient that may be booked in the slot
        (not service type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Comments on the slot to describe any extended information. Such as
        custom constraints on the slot.
        Type `str`. """
        
        self.end = None
        """ Date/Time that the slot is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.overbooked = None
        """ This slot has already been overbooked, appointments are unlikely to
        be accepted for this time.
        Type `bool`. """
        
        self.schedule = None
        """ The schedule resource that this slot defines an interval of status
        information.
        Type `FHIRReference` referencing `Schedule` (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ A broad categorisation of the service that is to be performed
        during this appointment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.serviceType = None
        """ The type of appointments that can be booked into this slot (ideally
        this would be an identifiable service - which is at a location,
        rather than the location itself). If provided then this overrides
        the value provided on the availability resource.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ The specialty of a practitioner that would be required to perform
        the service requested in this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.start = None
        """ Date/Time that the slot is to begin.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ busy | free | busy-unavailable | busy-tentative | entered-in-error.
        Type `str`. """
        
        super(Slot, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Slot, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("overbooked", "overbooked", bool, False, None, False),
            ("schedule", "schedule", fhirreference.FHIRReference, False, None, True),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, False, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
