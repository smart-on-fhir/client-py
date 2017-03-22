#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/TriggerDefinition) on 2017-03-22.
#  2017, SMART Health IT.


from . import element

class TriggerDefinition(element.Element):
    """ Defines an expected trigger for a module.
    
    A description of a triggering event.
    """
    
    resource_type = "TriggerDefinition"
    
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
        """ Triggering event name.
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


import sys
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
