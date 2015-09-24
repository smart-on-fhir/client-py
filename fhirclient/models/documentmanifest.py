#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/DocumentManifest) on 2015-09-24.
#  2015, SMART Health IT.


from . import attachment
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


class DocumentManifest(domainresource.DomainResource):
    """ A manifest that defines a set of documents.
    """
    
    resource_name = "DocumentManifest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who and/or what authored the manifest.
        List of `FHIRReference` items referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.content = None
        """ The items included.
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
        List of `FHIRReference` items referencing `Patient, Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON). """
        
        self.related = None
        """ Related things.
        List of `DocumentManifestRelated` items (represented as `dict` in JSON). """
        
        self.source = None
        """ The source system/application/software.
        Type `str`. """
        
        self.status = None
        """ current | superseded | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ The subject of the set of documents.
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device` (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of document set.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentManifest, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentManifest, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, True),
            ("content", "content", DocumentManifestContent, True),
            ("created", "created", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True),
            ("related", "related", DocumentManifestRelated, True),
            ("source", "source", str, False),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


class DocumentManifestContent(fhirelement.FHIRElement):
    """ The items included.
    
    The list of Documents included in the manifest.
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
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(DocumentManifestContent, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentManifestContent, self).elementProperties()
        js.extend([
            ("pAttachment", "pAttachment", attachment.Attachment, False),
            ("pReference", "pReference", fhirreference.FHIRReference, False),
        ])
        return js


class DocumentManifestRelated(fhirelement.FHIRElement):
    """ Related things.
    
    Related identifiers or resources associated with the DocumentManifest.
    """
    
    resource_name = "DocumentManifestRelated"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Identifiers of things that are related.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.ref = None
        """ Related Resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(DocumentManifestRelated, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentManifestRelated, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False),
            ("ref", "ref", fhirreference.FHIRReference, False),
        ])
        return js

