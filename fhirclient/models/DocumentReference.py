#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-17.
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
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Narrative
import Organization
import Patient
import Period
import Practitioner


class DocumentReference(FHIRResource.FHIRResource):
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
            self.authenticator = FHIRReference.FHIRReference.with_json_and_owner(jsondict['authenticator'], self, Practitioner.Practitioner)
        if 'author' in jsondict:
            self.author = FHIRReference.FHIRReference.with_json_and_owner(jsondict['author'], self, Practitioner.Practitioner)
        if 'confidentiality' in jsondict:
            self.confidentiality = CodeableConcept.CodeableConcept.with_json(jsondict['confidentiality'])
        if 'context' in jsondict:
            self.context = DocumentReferenceContext.with_json(jsondict['context'])
        if 'created' in jsondict:
            self.created = FHIRDate.FHIRDate.with_json(jsondict['created'])
        if 'custodian' in jsondict:
            self.custodian = FHIRReference.FHIRReference.with_json_and_owner(jsondict['custodian'], self, Organization.Organization)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'docStatus' in jsondict:
            self.docStatus = CodeableConcept.CodeableConcept.with_json(jsondict['docStatus'])
        if 'format' in jsondict:
            self.format = CodeableConcept.CodeableConcept.with_json(jsondict['format'])
        if 'hash' in jsondict:
            self.hash = jsondict['hash']
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'indexed' in jsondict:
            self.indexed = FHIRDate.FHIRDate.with_json(jsondict['indexed'])
        if 'klass' in jsondict:
            self.klass = CodeableConcept.CodeableConcept.with_json(jsondict['klass'])
        if 'location' in jsondict:
            self.location = jsondict['location']
        if 'masterIdentifier' in jsondict:
            self.masterIdentifier = Identifier.Identifier.with_json(jsondict['masterIdentifier'])
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
            self.subject = FHIRReference.FHIRReference.with_json_and_owner(jsondict['subject'], self, Patient.Patient)
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])


class DocumentReferenceRelatesTo(FHIRElement.FHIRElement):
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
            self.target = FHIRReference.FHIRReference.with_json_and_owner(jsondict['target'], self, DocumentReference)


class DocumentReferenceService(FHIRElement.FHIRElement):
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
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])


class DocumentReferenceServiceParameter(FHIRElement.FHIRElement):
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


class DocumentReferenceContext(FHIRElement.FHIRElement):
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
            self.event = CodeableConcept.CodeableConcept.with_json(jsondict['event'])
        if 'facilityType' in jsondict:
            self.facilityType = CodeableConcept.CodeableConcept.with_json(jsondict['facilityType'])
        if 'period' in jsondict:
            self.period = Period.Period.with_json(jsondict['period'])

