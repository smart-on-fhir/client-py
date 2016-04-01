#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/TriggerDefinition) on 2016-04-01.
#  2016, SMART Health IT.


from . import element

class TriggerDefinition(element.Element):
    """ Defines an expected trigger for a module.
    
    A description of a triggering event.
    """
    
    resource_name = "TriggerDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.eventData = None
        """ Triggering data of the event.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.eventName = None
        """ Name of the event.
        Type `str`. """
        
        self.eventTimingDate = None
        """ Timing of the event.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.eventTimingDateTime = None
        """ Timing of the event.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.eventTimingReference = None
        """ Timing of the event.
        Type `FHIRReference` referencing `Schedule` (represented as `dict` in JSON). """
        
        self.eventTimingTiming = None
        """ Timing of the event.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.type = None
        """ named-event | periodic | data-added | data-modified | data-removed
        | data-accessed | data-access-ended.
        Type `str`. """
        
        super(TriggerDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TriggerDefinition, self).elementProperties()
        js.extend([
            ("eventData", "eventData", datarequirement.DataRequirement, False, None, False),
            ("eventName", "eventName", str, False, None, False),
            ("eventTimingDate", "eventTimingDate", fhirdate.FHIRDate, False, "eventTiming", False),
            ("eventTimingDateTime", "eventTimingDateTime", fhirdate.FHIRDate, False, "eventTiming", False),
            ("eventTimingReference", "eventTimingReference", fhirreference.FHIRReference, False, "eventTiming", False),
            ("eventTimingTiming", "eventTimingTiming", timing.Timing, False, "eventTiming", False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import datarequirement
from . import fhirdate
from . import fhirreference
from . import timing
