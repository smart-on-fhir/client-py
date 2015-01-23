#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (documentreference.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period


class DocumentReference(fhirresource.FHIRResource):
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
        List of `FHIRReference` items referencing `Practitioner, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.confidentiality = None
        """ Sensitivity of source document.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        """ preliminary | final | appended | amended | entered in error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.format = None
        """ Format/content rules for the document.
        List of `str` items. """
        
        self.hash = None
        """ Base64 representation of SHA1.
        Type `str`. """
        
        self.identifier = None
        """ Other identifiers for the document.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indexed = None
        """ When this document reference created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.klass = None
        """ Categorization of Document.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.location = None
        """ Where to access the document.
        Type `str`. """
        
        self.masterIdentifier = None
        """ Master Version Specific Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.mimeType = None
        """ Mime type, + maybe character encoding.
        Type `str`. """
        
        self.policyManager = None
        """ Manages access policies for the document.
        Type `str`. """
        
        self.primaryLanguage = None
        """ The marked primary language for the document.
        Type `str`. """
        
        self.relatesTo = None
        """ Relationships to other documents.
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """
        
        self.service = None
        """ If access is not fully described by location.
        Type `DocumentReferenceService` (represented as `dict` in JSON). """
        
        self.size = None
        """ Size of the document in bytes.
        Type `int`. """
        
        self.status = None
        """ current | superceded | entered in error.
        Type `str`. """
        
        self.subject = None
        """ Who|what is the subject of the document.
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device` (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of document this is (LOINC if possible).
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
        if 'hash' in jsondict:
            self.hash = jsondict['hash']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'indexed' in jsondict:
            self.indexed = fhirdate.FHIRDate.with_json_and_owner(jsondict['indexed'], self)
        if 'klass' in jsondict:
            self.klass = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['klass'], self)
        if 'location' in jsondict:
            self.location = jsondict['location']
        if 'masterIdentifier' in jsondict:
            self.masterIdentifier = identifier.Identifier.with_json_and_owner(jsondict['masterIdentifier'], self)
        if 'mimeType' in jsondict:
            self.mimeType = jsondict['mimeType']
        if 'policyManager' in jsondict:
            self.policyManager = jsondict['policyManager']
        if 'primaryLanguage' in jsondict:
            self.primaryLanguage = jsondict['primaryLanguage']
        if 'relatesTo' in jsondict:
            self.relatesTo = DocumentReferenceRelatesTo.with_json_and_owner(jsondict['relatesTo'], self)
        if 'service' in jsondict:
            self.service = DocumentReferenceService.with_json_and_owner(jsondict['service'], self)
        if 'size' in jsondict:
            self.size = jsondict['size']
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
        
        super(DocumentReferenceContext, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentReferenceContext, self).update_with_json(jsondict)
        if 'event' in jsondict:
            self.event = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['event'], self)
        if 'facilityType' in jsondict:
            self.facilityType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['facilityType'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)


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


class DocumentReferenceService(fhirelement.FHIRElement):
    """ If access is not fully described by location.
    
    A description of a service call that can be used to retrieve the document.
    """
    
    resource_name = "DocumentReferenceService"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Where service is located (usually a URL).
        Type `str`. """
        
        self.parameter = None
        """ Service call parameters.
        List of `DocumentReferenceServiceParameter` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of service (i.e. XDS.b).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentReferenceService, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentReferenceService, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = jsondict['address']
        if 'parameter' in jsondict:
            self.parameter = DocumentReferenceServiceParameter.with_json_and_owner(jsondict['parameter'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class DocumentReferenceServiceParameter(fhirelement.FHIRElement):
    """ Service call parameters.
    
    A list of named parameters that is used in the service call.
    """
    
    resource_name = "DocumentReferenceServiceParameter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Parameter name in service call.
        Type `str`. """
        
        self.value = None
        """ Parameter value for the name.
        Type `str`. """
        
        super(DocumentReferenceServiceParameter, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentReferenceServiceParameter, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'value' in jsondict:
            self.value = jsondict['value']

