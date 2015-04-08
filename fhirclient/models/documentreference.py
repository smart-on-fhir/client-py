#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DocumentReference) on 2015-04-08.
#  2015, SMART Health IT.


import attachment
import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period


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
    
    def update_with_json(self, jsondict):
        super(DocumentReference, self).update_with_json(jsondict)
        if 'authenticator' in jsondict:
            self.authenticator = fhirreference.FHIRReference.with_json_and_owner(jsondict['authenticator'], self)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'confidentiality' in jsondict:
            self.confidentiality = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['confidentiality'], self)
        if 'content' in jsondict:
            self.content = attachment.Attachment.with_json_and_owner(jsondict['content'], self)
        if 'context' in jsondict:
            self.context = DocumentReferenceContext.with_json_and_owner(jsondict['context'], self)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'custodian' in jsondict:
            self.custodian = fhirreference.FHIRReference.with_json_and_owner(jsondict['custodian'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'docStatus' in jsondict:
            self.docStatus = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['docStatus'], self)
        if 'format' in jsondict:
            self.format = jsondict['format']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'indexed' in jsondict:
            self.indexed = fhirdate.FHIRDate.with_json_and_owner(jsondict['indexed'], self)
        if 'class' in jsondict:
            self.klass = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['class'], self)
        if 'masterIdentifier' in jsondict:
            self.masterIdentifier = identifier.Identifier.with_json_and_owner(jsondict['masterIdentifier'], self)
        if 'relatesTo' in jsondict:
            self.relatesTo = DocumentReferenceRelatesTo.with_json_and_owner(jsondict['relatesTo'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


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
    
    def update_with_json(self, jsondict):
        super(DocumentReferenceContext, self).update_with_json(jsondict)
        if 'event' in jsondict:
            self.event = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['event'], self)
        if 'facilityType' in jsondict:
            self.facilityType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['facilityType'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'practiceSetting' in jsondict:
            self.practiceSetting = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['practiceSetting'], self)
        if 'related' in jsondict:
            self.related = DocumentReferenceContextRelated.with_json_and_owner(jsondict['related'], self)
        if 'sourcePatientInfo' in jsondict:
            self.sourcePatientInfo = fhirreference.FHIRReference.with_json_and_owner(jsondict['sourcePatientInfo'], self)


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
    
    def update_with_json(self, jsondict):
        super(DocumentReferenceContextRelated, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'ref' in jsondict:
            self.ref = fhirreference.FHIRReference.with_json_and_owner(jsondict['ref'], self)


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
    
    def update_with_json(self, jsondict):
        super(DocumentReferenceRelatesTo, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)

