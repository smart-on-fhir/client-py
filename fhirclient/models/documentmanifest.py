#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (documentmanifest.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier


class DocumentManifest(fhirresource.FHIRResource):
    """ A manifest that defines a set of documents.
    """
    
    resource_name = "DocumentManifest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who and/or what authored the document.
        List of `FHIRReference` items referencing `Practitioner, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.confidentiality = None
        """ Sensitivity of set of documents.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ Contents of this set of documents.
        List of `FHIRReference` items referencing `DocumentReference, Binary, Media` (represented as `dict` in JSON). """
        
        self.created = None
        """ When this document manifest created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Human-readable description (title).
        Type `str`. """
        
        self.identifier = None
        """ Other identifiers for the manifest.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.masterIdentifier = None
        """ Unique Identifier for the set of documents.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Intended to get notified about this set of documents.
        List of `FHIRReference` items referencing `Patient, Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.source = None
        """ The source system/application/software.
        Type `str`. """
        
        self.status = None
        """ current | superceded | entered in error.
        Type `str`. """
        
        self.subject = None
        """ The subject of the set of documents.
        List of `FHIRReference` items referencing `Patient, Practitioner, Group, Device` (represented as `dict` in JSON). """
        
        self.supercedes = None
        """ If this document manifest replaces another.
        Type `FHIRReference` referencing `DocumentManifest` (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of document set this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentManifest, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentManifest, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'confidentiality' in jsondict:
            self.confidentiality = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['confidentiality'], self)
        if 'content' in jsondict:
            self.content = fhirreference.FHIRReference.with_json_and_owner(jsondict['content'], self)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'masterIdentifier' in jsondict:
            self.masterIdentifier = identifier.Identifier.with_json_and_owner(jsondict['masterIdentifier'], self)
        if 'recipient' in jsondict:
            self.recipient = fhirreference.FHIRReference.with_json_and_owner(jsondict['recipient'], self)
        if 'source' in jsondict:
            self.source = jsondict['source']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'supercedes' in jsondict:
            self.supercedes = fhirreference.FHIRReference.with_json_and_owner(jsondict['supercedes'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

