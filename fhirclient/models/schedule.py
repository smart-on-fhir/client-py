#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Schedule) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirreference
import identifier
import period


class Schedule(domainresource.DomainResource):
    """ A container for slot(s) of time that may be available for booking
    appointments.
    """
    
    resource_name = "Schedule"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actor = None
        """ The resource this Schedule resource is providing availability
        information for. These are expected to usually be one of
        HealthcareService, Location, Practitioner, Device, Patient or
        RelatedPerson.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Comments on the availability to describe any extended information.
        Such as custom constraints on the slot(s) that may be associated.
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
        
        self.type = None
        """ The schedule type can be used for the categorization of healthcare
        services or other appointment types.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Schedule, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Schedule, self).update_with_json(jsondict)
        if 'actor' in jsondict:
            self.actor = fhirreference.FHIRReference.with_json_and_owner(jsondict['actor'], self)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'planningHorizon' in jsondict:
            self.planningHorizon = period.Period.with_json_and_owner(jsondict['planningHorizon'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

