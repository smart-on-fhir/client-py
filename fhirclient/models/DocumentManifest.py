#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (documentmanifest.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import CodeableConcept
import DocumentReference
import FHIRDate
import FHIRReference
import FHIRResource
import Identifier
import Narrative
import Patient
import Practitioner


class DocumentManifest(FHIRResource.FHIRResource):
    """ A manifest that defines a set of documents.
    
    Scope and Usage A document manifest gathers a set of Document Reference
    resources into a single package that may be the subject of workflow such as
    access control, auditing, and targeted delivery.
    
    Typically, Document Manifest Resources are used in document indexing
    systems, such as IHE XDS (see the XDS specific profile).
    """
    
    resource_name = "DocumentManifest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who and/or what authored the document.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.confidentiality = None
        """ Sensitivity of set of documents.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ Contents of this set of documents.
        List of `FHIRReference` items referencing `DocumentReference` (represented as `dict` in JSON). """
        
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
        List of `FHIRReference` items referencing `Patient` (represented as `dict` in JSON). """
        
        self.source = None
        """ The source system/application/software.
        Type `str`. """
        
        self.status = None
        """ current | superceded | entered in error.
        Type `str`. """
        
        self.subject = None
        """ The subject of the set of documents.
        List of `FHIRReference` items referencing `Patient` (represented as `dict` in JSON). """
        
        self.supercedes = None
        """ If this document manifest replaces another.
        Type `FHIRReference` referencing `DocumentManifest` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of document set this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentManifest, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentManifest, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = FHIRReference.FHIRReference.with_json_and_owner(jsondict['author'], self, Practitioner.Practitioner)
        if 'confidentiality' in jsondict:
            self.confidentiality = CodeableConcept.CodeableConcept.with_json(jsondict['confidentiality'])
        if 'content' in jsondict:
            self.content = FHIRReference.FHIRReference.with_json_and_owner(jsondict['content'], self, DocumentReference.DocumentReference)
        if 'created' in jsondict:
            self.created = FHIRDate.FHIRDate.with_json(jsondict['created'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'masterIdentifier' in jsondict:
            self.masterIdentifier = Identifier.Identifier.with_json(jsondict['masterIdentifier'])
        if 'recipient' in jsondict:
            self.recipient = FHIRReference.FHIRReference.with_json_and_owner(jsondict['recipient'], self, Patient.Patient)
        if 'source' in jsondict:
            self.source = jsondict['source']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = FHIRReference.FHIRReference.with_json_and_owner(jsondict['subject'], self, Patient.Patient)
        if 'supercedes' in jsondict:
            self.supercedes = FHIRReference.FHIRReference.with_json_and_owner(jsondict['supercedes'], self, DocumentManifest)
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])

