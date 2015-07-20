#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DocumentReference) on 2015-07-06.
#  2015, SMART Health IT.


from . import attachment
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period


class DocumentReference(domainresource.DomainResource):
    """ A reference to a document.
    """
    
    resource_name = "DocumentReference"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authenticator = None
        """ Who/What authenticated the document.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.author = None
        """ Who and/or what authored the document.
        List of `FHIRReference` items referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.confidentiality = None
        """ Document security-tags.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.content = None
        """ Where to access the document.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Clinical context of document.
        Type `DocumentReferenceContext` (represented as `dict` in JSON). """
        
        self.created = None
        """ Document creation time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.custodian = None
        """ Org which maintains the document.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.description = None
        """ Human-readable description (title).
        Type `str`. """
        
        self.docStatus = None
        """ preliminary | final | appended | amended | entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.format = None
        """ Format/content rules for the document.
        List of `str` items. """
        
        self.identifier = None
        """ Other identifiers for the document.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indexed = None
        """ When this document reference created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.klass = None
        """ Categorization of document.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.masterIdentifier = None
        """ Master Version Specific Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relatesTo = None
        """ Relationships to other documents.
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """
        
        self.status = None
        """ current | superceded | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Who|what is the subject of the document.
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device` (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of document.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentReference, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentReference, self).elementProperties()
        js.extend([
            ("authenticator", "authenticator", fhirreference.FHIRReference, False),
            ("author", "author", fhirreference.FHIRReference, True),
            ("confidentiality", "confidentiality", codeableconcept.CodeableConcept, True),
            ("content", "content", attachment.Attachment, True),
            ("context", "context", DocumentReferenceContext, False),
            ("created", "created", fhirdate.FHIRDate, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False),
            ("description", "description", str, False),
            ("docStatus", "docStatus", codeableconcept.CodeableConcept, False),
            ("format", "format", str, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("indexed", "indexed", fhirdate.FHIRDate, False),
            ("klass", "class", codeableconcept.CodeableConcept, False),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False),
            ("relatesTo", "relatesTo", DocumentReferenceRelatesTo, True),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
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
        """ Related things.
        List of `DocumentReferenceContextRelated` items (represented as `dict` in JSON). """
        
        self.sourcePatientInfo = None
        """ Source patient info.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(DocumentReferenceContext, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DocumentReferenceContext, self).elementProperties()
        js.extend([
            ("event", "event", codeableconcept.CodeableConcept, True),
            ("facilityType", "facilityType", codeableconcept.CodeableConcept, False),
            ("period", "period", period.Period, False),
            ("practiceSetting", "practiceSetting", codeableconcept.CodeableConcept, False),
            ("related", "related", DocumentReferenceContextRelated, True),
            ("sourcePatientInfo", "sourcePatientInfo", fhirreference.FHIRReference, False),
        ])
        return js


class DocumentReferenceContextRelated(fhirelement.FHIRElement):
    """ Related things.
    
    Related identifiers or resources associated with the DocumentReference.
    """
    
    resource_name = "DocumentReferenceContextRelated"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Related Identifier.
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

