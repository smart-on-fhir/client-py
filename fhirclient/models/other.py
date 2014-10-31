#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (other.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier
import narrative
import practitioner


class Other(fhirresource.FHIRResource):
    """ Resource for non-supported content.
    
    Scope and Usage Other is a special type of resource. Unlike all other
    resources, it doesn't correspond to a specific identifiable real-world
    concept. Instead, it's a placeholder for any resource-like concept that
    isn't already defined in the HL7 specification.
    
    The Other resource is intended for use in two circumstances:
    
    * When an implementer needs a resource concept that is likely to be defined
    by HL7 in the future but they have not yet done so (due to bandwidth
    issues, lack of sufficient requirements, lower prioritization, etc.)
    * When the resource concept falls "outside the 99%" - i.e. less than 1% of
    the systems that use FHIR are likely to ever make use of the resource. To
    keep the specification manageable, it cannot incorporate every esoteric
    requirement that might be needed in some implementation somewhere. This set
    of resources likely won't ever be officially defined in HL7.
    There's also a third circumstance: An implementer wishes to convey
    information that could/should be conveyed using a standard resource,
    however they want to represent the information in a custom format that
    isn't aligned with the official resource's elements. While this resource
    would be the preferred way of meeting that use-case because it will at
    least be wire-format compatible, such a use would not be conformant because
    making use of the Other resource would prevent the healthcare-related
    information from being safely processed, queried and analyzed by other
    conformant systems.
    
    Implementers don't really need to be concerned with one of the two
    categories their desired resource fits within. If they need a resource and
    it doesn't yet exist, they should use Other.
    """
    
    resource_name = "Other"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who created.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.code = None
        """ Kind of Resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.created = None
        """ When created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Identifies the.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(Other, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Other, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self, practitioner.Practitioner)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json(jsondict['created'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, fhirresource.FHIRResource)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])

