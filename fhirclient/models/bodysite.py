#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/BodySite) on 2015-04-08.
#  2015, SMART Health IT.


import attachment
import codeableconcept
import domainresource
import fhirreference
import identifier


class BodySite(domainresource.DomainResource):
    """ Specific and identified anatomical location.
    
    Record details about the anatomical location of a specimen or body part.
    This resource may be used when a coded concept does not provide the
    necessary detail needed for the use case.
    """
    
    resource_name = "BodySite"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Named anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ The Description of anatomical location.
        Type `str`. """
        
        self.identifier = None
        """ Bodysite identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.image = None
        """ Attached images.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.mod = None
        """ Modification to location code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(BodySite, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(BodySite, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'image' in jsondict:
            self.image = attachment.Attachment.with_json_and_owner(jsondict['image'], self)
        if 'modifier' in jsondict:
            self.mod = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['modifier'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)

