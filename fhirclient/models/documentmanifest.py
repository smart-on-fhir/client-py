#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DocumentManifest) on 2015-04-08.
#  2015, SMART Health IT.


import attachment
import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier


class DocumentManifest(domainresource.DomainResource):
    """ A manifest that defines a set of documents.
    """
    
    resource_name = "DocumentManifest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who and/or what authored the document.
        List of `FHIRReference` items referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.content = None
        """ Contents of the manifest.
        List of `DocumentManifestContent` items (represented as `dict` in JSON). """
        
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
        
        self.related = None
        """ Related things.
        List of `DocumentManifestRelated` items (represented as `dict` in JSON). """
        
        self.source = None
        """ The source system/application/software.
        Type `str`. """
        
        self.status = None
        """ current | superceded | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ The subject of the set of documents.
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device` (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of document set this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentManifest, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentManifest, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'content' in jsondict:
            self.content = DocumentManifestContent.with_json_and_owner(jsondict['content'], self)
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
        if 'related' in jsondict:
            self.related = DocumentManifestRelated.with_json_and_owner(jsondict['related'], self)
        if 'source' in jsondict:
            self.source = jsondict['source']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class DocumentManifestContent(fhirelement.FHIRElement):
    """ Contents of the manifest.
    
    The manifest list.
    """
    
    resource_name = "DocumentManifestContent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.pAttachment = None
        """ Contents of this set of documents.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.pReference = None
        """ Contents of this set of documents.
        Type `FHIRReference` referencing `DocumentReference, Media` (represented as `dict` in JSON). """
        
        super(DocumentManifestContent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentManifestContent, self).update_with_json(jsondict)
        if 'pAttachment' in jsondict:
            self.pAttachment = attachment.Attachment.with_json_and_owner(jsondict['pAttachment'], self)
        if 'pReference' in jsondict:
            self.pReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['pReference'], self)


class DocumentManifestRelated(fhirelement.FHIRElement):
    """ Related things.
    
    Related identifiers or resources associated with the DocumentManifest.
    """
    
    resource_name = "DocumentManifestRelated"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Related Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.ref = None
        """ Related Resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(DocumentManifestRelated, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentManifestRelated, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'ref' in jsondict:
            self.ref = fhirreference.FHIRReference.with_json_and_owner(jsondict['ref'], self)

