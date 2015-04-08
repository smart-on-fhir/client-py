#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirreference
import identifier
import period
import timing


class DeviceUseStatement(domainresource.DomainResource):
    """ A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician..
    
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
        """ The details of the device used..
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ An external identifier for this statement such as an IRI..
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason or justification for the use of the device..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Details about the device statement that were not represented at all
        or sufficiently in one of the attributes provided in a class. These
        may include for example a comment, an instruction, or a note
        associated with the statement..
        List of `str` items. """
        
        self.recordedOn = None
        """ The time at which the statement was made/recorded..
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subject = None
        """ The patient who used the device..
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ How often the device was used..
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ How often the device was used..
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ How often the device was used..
        Type `Timing` (represented as `dict` in JSON). """
        
        self.whenUsed = None
        """ The time period over which the device was used..
        Type `Period` (represented as `dict` in JSON). """
        
        super(DeviceUseStatement, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DeviceUseStatement, self).update_with_json(jsondict)
        if 'bodySiteCodeableConcept' in jsondict:
            self.bodySiteCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['bodySiteCodeableConcept'], self)
        if 'bodySiteReference' in jsondict:
            self.bodySiteReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['bodySiteReference'], self)
        if 'device' in jsondict:
            self.device = fhirreference.FHIRReference.with_json_and_owner(jsondict['device'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'indication' in jsondict:
            self.indication = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['indication'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'recordedOn' in jsondict:
            self.recordedOn = fhirdate.FHIRDate.with_json_and_owner(jsondict['recordedOn'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'timingDateTime' in jsondict:
            self.timingDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['timingDateTime'], self)
        if 'timingPeriod' in jsondict:
            self.timingPeriod = period.Period.with_json_and_owner(jsondict['timingPeriod'], self)
        if 'timingTiming' in jsondict:
            self.timingTiming = timing.Timing.with_json_and_owner(jsondict['timingTiming'], self)
        if 'whenUsed' in jsondict:
            self.whenUsed = period.Period.with_json_and_owner(jsondict['whenUsed'], self)

