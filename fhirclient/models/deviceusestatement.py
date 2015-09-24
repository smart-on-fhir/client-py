#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing


class DeviceUseStatement(domainresource.DomainResource):
    """ None.
    
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    
    resource_name = "DeviceUseStatement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySiteCodeableConcept = None
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySiteReference = None
        """ Target body site.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        self.device = None
        """ None.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ None.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ None.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ None.
        List of `str` items. """
        
        self.recordedOn = None
        """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subject = None
        """ None.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ None.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ None.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.whenUsed = None
        """ None.
        Type `Period` (represented as `dict` in JSON). """
        
        super(DeviceUseStatement, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("bodySiteCodeableConcept", "bodySiteCodeableConcept", codeableconcept.CodeableConcept, False),
            ("bodySiteReference", "bodySiteReference", fhirreference.FHIRReference, False),
            ("device", "device", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("indication", "indication", codeableconcept.CodeableConcept, True),
            ("notes", "notes", str, True),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False),
            ("timingPeriod", "timingPeriod", period.Period, False),
            ("timingTiming", "timingTiming", timing.Timing, False),
            ("whenUsed", "whenUsed", period.Period, False),
        ])
        return js

