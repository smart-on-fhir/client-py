#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/DocumentReference) on 2015-09-24.
#  2015, SMART Health IT.


from . import attachment
from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period


class DocumentReference(domainresource.DomainResource):
    """ A reference to a document.
    
    A reference to a document .
    """
    
    resource_name = "DocumentReference"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authenticator = None
        """ Who/what authenticated the document.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.author = None
        """ Who and/or what authored the document.
        List of `FHIRReference` items referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.class_fhir = None
        """ Categorization of document.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ Document referenced.
        List of `DocumentReferenceContent` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Clinical context of document.
        Type `DocumentReferenceContext` (represented as `dict` in JSON). """
        
        self.created = None
        """ Document creation time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.custodian = None
        """ Organization which maintains the document.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.description = None
        """ Human-readable description (title).
        Type `str`. """
        
        self.docStatus = None
        """ preliminary | final | appended | amended | entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Other identifiers for the document.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indexed = None
        """ When this document reference created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.masterIdentifier = None
        """ Master Version Specific Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relatesTo = None
        """ Relationships to other documents.
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ Document security-tags.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ current | superseded | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Who/what is the subject of the document.
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device` (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of document (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentReference, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentReference, self).elementProperties()
        js.extend([
            ("authenticator", "authenticator", fhirreference.FHIRReference, False),
            ("author", "author", fhirreference.FHIRReference, True),
            ("class_fhir", "class", codeableconcept.CodeableConcept, False),
            ("content", "content", DocumentReferenceContent, True),
            ("context", "context", DocumentReferenceContext, False),
            ("created", "created", fhirdate.FHIRDate, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False),
            ("description", "description", str, False),
            ("docStatus", "docStatus", codeableconcept.CodeableConcept, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("indexed", "indexed", fhirdate.FHIRDate, False),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False),
            ("relatesTo", "relatesTo", DocumentReferenceRelatesTo, True),
            ("securityLabel", "securityLabel", codeableconcept.CodeableConcept, True),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


class DocumentReferenceContent(fhirelement.FHIRElement):
    """ Document referenced.
    
    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """
    
    resource_name = "DocumentReferenceContent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.attachment = None
        """ Where to access the document.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.format = None
        """ Format/content rules for the document.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(DocumentReferenceContent, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentReferenceContent, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False),
            ("format", "format", coding.Coding, True),
        ])
        return js


class DocumentReferenceContext(fhirelement.FHIRElement):
    """ Clinical context of document.
    
    The clinical context in which the document was prepared.
    """
    
    resource_name = "DocumentReferenceContext"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.encounter = None
        """ Context of the document  content.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.event = None
        """ Main Clinical Acts Documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.facilityType = None
        """ Kind of facility where patient was seen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time of service that is being documented.
        Type `Period` (represented as `dict` in JSON). """
        
        self.practiceSetting = None
        """ Additional details about where the content was created (e.g.
        clinical specialty).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.related = None
        """ Related identifiers or resources.
        List of `DocumentReferenceContextRelated` items (represented as `dict` in JSON). """
        
        self.sourcePatientInfo = None
        """ Patient demographics from source.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(DocumentReferenceContext, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentReferenceContext, self).elementProperties()
        js.extend([
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("event", "event", codeableconcept.CodeableConcept, True),
            ("facilityType", "facilityType", codeableconcept.CodeableConcept, False),
            ("period", "period", period.Period, False),
            ("practiceSetting", "practiceSetting", codeableconcept.CodeableConcept, False),
            ("related", "related", DocumentReferenceContextRelated, True),
            ("sourcePatientInfo", "sourcePatientInfo", fhirreference.FHIRReference, False),
        ])
        return js


class DocumentReferenceContextRelated(fhirelement.FHIRElement):
    """ Related identifiers or resources.
    
    Related identifiers or resources associated with the DocumentReference.
    """
    
    resource_name = "DocumentReferenceContextRelated"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Identifier of related objects or events.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.ref = None
        """ Related Resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(DocumentReferenceContextRelated, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentReferenceContextRelated, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False),
            ("ref", "ref", fhirreference.FHIRReference, False),
        ])
        return js


class DocumentReferenceRelatesTo(fhirelement.FHIRElement):
    """ Relationships to other documents.
    
    Relationships that this document has with other document references that
    already exist.
    """
    
    resource_name = "DocumentReferenceRelatesTo"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ replaces | transforms | signs | appends.
        Type `str`. """
        
        self.target = None
        """ Target of the relationship.
        Type `FHIRReference` referencing `DocumentReference` (represented as `dict` in JSON). """
        
        super(DocumentReferenceRelatesTo, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentReferenceRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("target", "target", fhirreference.FHIRReference, False),
        ])
        return js

