#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import organization
import patient
import period
import practitioner


class DocumentReference(fhirresource.FHIRResource):
    """ XDSDocumentEntry.
    """
    
    resource_name = "DocumentReference"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authenticator = None
        """ ??.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.author = None
        """ XDSDocumentEntry.author.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.confidentiality = None
        """ XDSDocumentEntry.confidentialityCode.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context = None
        """ event codes, service Start & Stop time, and facility type.
        Type `DocumentReferenceContext` (represented as `dict` in JSON). """
        
        self.created = None
        """ XDSDocumentEntry.creationTime.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.custodian = None
        """ n/a.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.description = None
        """ XDSDocumentEntry.title.
        Type `str`. """
        
        self.docStatus = None
        """ preliminary | final | appended | amended | entered in error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.format = None
        """ XDSDocumentEntry.formatCode.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.hash = None
        """ XDSDocumentEntry.hash.
        Type `str`. """
        
        self.identifier = None
        """ XDSDocumentEntry.referenceIdList.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indexed = None
        """ XDS submission time or XDSDocumentEntry.creationTime  if unknown.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.klass = None
        """ XDSDocumentEntry.classCode.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.location = None
        """ repository location (by implication & configuration).
        Type `str`. """
        
        self.masterIdentifier = None
        """ XDSDocumentEntry.uniqueId.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.mimeType = None
        """ XDSDocumentEntry.mimeType.
        Type `str`. """
        
        self.policyManager = None
        """ XDSDocumentEntry.homeCommunityId.
        Type `str`. """
        
        self.primaryLanguage = None
        """ XDSDocumentEntry.languageCode.
        Type `str`. """
        
        self.relatesTo = None
        """ Relationships that this document has with other document references
        that already exist.
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """
        
        self.service = None
        """ can be determined from repository location + parameters.
        Type `DocumentReferenceService` (represented as `dict` in JSON). """
        
        self.size = None
        """ XDSDocumentEntry.size.
        Type `int`. """
        
        self.status = None
        """ implied by XDS workflow.
        Type `str`. """
        
        self.subject = None
        """ XDSDocumentEntry.patientId + sourcePatientId/sourcePatientInfo.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.type = None
        """ XDSDocumentEntry.typeCode.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentReference, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentReference, self).update_with_json(jsondict)
        if 'authenticator' in jsondict:
            self.authenticator = fhirreference.FHIRReference.with_json_and_owner(jsondict['authenticator'], self, practitioner.Practitioner)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self, practitioner.Practitioner)
        if 'confidentiality' in jsondict:
            self.confidentiality = codeableconcept.CodeableConcept.with_json(jsondict['confidentiality'])
        if 'context' in jsondict:
            self.context = DocumentReferenceContext.with_json(jsondict['context'])
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json(jsondict['created'])
        if 'custodian' in jsondict:
            self.custodian = fhirreference.FHIRReference.with_json_and_owner(jsondict['custodian'], self, organization.Organization)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'docStatus' in jsondict:
            self.docStatus = codeableconcept.CodeableConcept.with_json(jsondict['docStatus'])
        if 'format' in jsondict:
            self.format = codeableconcept.CodeableConcept.with_json(jsondict['format'])
        if 'hash' in jsondict:
            self.hash = jsondict['hash']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'indexed' in jsondict:
            self.indexed = fhirdate.FHIRDate.with_json(jsondict['indexed'])
        if 'klass' in jsondict:
            self.klass = codeableconcept.CodeableConcept.with_json(jsondict['klass'])
        if 'location' in jsondict:
            self.location = jsondict['location']
        if 'masterIdentifier' in jsondict:
            self.masterIdentifier = identifier.Identifier.with_json(jsondict['masterIdentifier'])
        if 'mimeType' in jsondict:
            self.mimeType = jsondict['mimeType']
        if 'policyManager' in jsondict:
            self.policyManager = jsondict['policyManager']
        if 'primaryLanguage' in jsondict:
            self.primaryLanguage = jsondict['primaryLanguage']
        if 'relatesTo' in jsondict:
            self.relatesTo = DocumentReferenceRelatesTo.with_json(jsondict['relatesTo'])
        if 'service' in jsondict:
            self.service = DocumentReferenceService.with_json(jsondict['service'])
        if 'size' in jsondict:
            self.size = jsondict['size']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])


class DocumentReferenceRelatesTo(fhirelement.FHIRElement):
    """ Relationships that this document has with other document references that
    already exist.
    
    Relationships to other documents.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ The type of relationship that this document has with anther
        document.
        Type `str`. """
        
        self.target = None
        """ The target document of this relationship.
        Type `FHIRReference` referencing `DocumentReference` (represented as `dict` in JSON). """
        
        super(DocumentReferenceRelatesTo, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentReferenceRelatesTo, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self, DocumentReference)


class DocumentReferenceService(fhirelement.FHIRElement):
    """ can be determined from repository location + parameters.
    
    If access is not fully described by location.
    """
    
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
            self.parameter = DocumentReferenceServiceParameter.with_json(jsondict['parameter'])
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])


class DocumentReferenceServiceParameter(fhirelement.FHIRElement):
    """ Service call parameters.
    
    A list of named parameters that is used in the service call.
    """
    
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


class DocumentReferenceContext(fhirelement.FHIRElement):
    """ event codes, service Start & Stop time, and facility type.
    
    Clinical context of document - eventCodeList, serviceStart & Stop time, and
    facility type.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.event = None
        """ XDSDocumentEntry.eventCodeList.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.facilityType = None
        """ XDSDocumentEntry.healthCareFacilityTypeCode.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.period = None
        """ XDSDocumentEntry.serviceStartTime &
        XDSDocumentEntry.serviceStopTime.
        Type `Period` (represented as `dict` in JSON). """
        
        super(DocumentReferenceContext, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DocumentReferenceContext, self).update_with_json(jsondict)
        if 'event' in jsondict:
            self.event = codeableconcept.CodeableConcept.with_json(jsondict['event'])
        if 'facilityType' in jsondict:
            self.facilityType = codeableconcept.CodeableConcept.with_json(jsondict['facilityType'])
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])

