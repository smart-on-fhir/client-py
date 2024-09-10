# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DocumentReference).
# 2024, SMART Health IT.


from . import domainresource

class DocumentReference(domainresource.DomainResource):
    """ A reference to a document.
    
    A reference to a document of any kind for any purpose. Provides metadata
    about the document so that the document can be discovered and managed. The
    scope of a document is any seralized object with a mime-type, so includes
    formal patient centric documents (CDA), cliical notes, scanned paper, and
    non-patient specific documents like policy text.
    """
    
    resource_type = "DocumentReference"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authenticator = None
        """ Who/what authenticated the document.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._authenticator = None
        """ Primitive extension for authenticator. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Who and/or what authored the document.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Categorization of document.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.content = None
        """ Document referenced.
        List of `DocumentReferenceContent` items (represented as `dict` in JSON). """
        self._content = None
        """ Primitive extension for content. Type `FHIRPrimitiveExtension` """
        
        self.context = None
        """ Clinical context of document.
        Type `DocumentReferenceContext` (represented as `dict` in JSON). """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.custodian = None
        """ Organization which maintains the document.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._custodian = None
        """ Primitive extension for custodian. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ When this document reference was created.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Human-readable description.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.docStatus = None
        """ preliminary | final | amended | entered-in-error.
        Type `str`. """
        self._docStatus = None
        """ Primitive extension for docStatus. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Other identifiers for the document.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.masterIdentifier = None
        """ Master Version Specific Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        self._masterIdentifier = None
        """ Primitive extension for masterIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.relatesTo = None
        """ Relationships to other documents.
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """
        self._relatesTo = None
        """ Primitive extension for relatesTo. Type `FHIRPrimitiveExtension` """
        
        self.securityLabel = None
        """ Document security-tags.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._securityLabel = None
        """ Primitive extension for securityLabel. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ current | superseded | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who/what is the subject of the document.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Kind of document (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(DocumentReference, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentReference, self).elementProperties()
        js.extend([
            ("authenticator", "authenticator", fhirreference.FHIRReference, False, None, False),
            ("_authenticator", "_authenticator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("content", "content", DocumentReferenceContent, True, None, True),
            ("_content", "_content", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("context", "context", DocumentReferenceContext, False, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("_custodian", "_custodian", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirinstant.FHIRInstant, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("docStatus", "docStatus", str, False, None, False),
            ("_docStatus", "_docStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False, None, False),
            ("_masterIdentifier", "_masterIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatesTo", "relatesTo", DocumentReferenceRelatesTo, True, None, False),
            ("_relatesTo", "_relatesTo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("securityLabel", "securityLabel", codeableconcept.CodeableConcept, True, None, False),
            ("_securityLabel", "_securityLabel", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class DocumentReferenceContent(backboneelement.BackboneElement):
    """ Document referenced.
    
    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """
    
    resource_type = "DocumentReferenceContent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attachment = None
        """ Where to access the document.
        Type `Attachment` (represented as `dict` in JSON). """
        self._attachment = None
        """ Primitive extension for attachment. Type `FHIRPrimitiveExtension` """
        
        self.format = None
        """ Format/content rules for the document.
        Type `Coding` (represented as `dict` in JSON). """
        self._format = None
        """ Primitive extension for format. Type `FHIRPrimitiveExtension` """
        
        super(DocumentReferenceContent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentReferenceContent, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, True),
            ("_attachment", "_attachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("format", "format", coding.Coding, False, None, False),
            ("_format", "_format", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DocumentReferenceContext(backboneelement.BackboneElement):
    """ Clinical context of document.
    
    The clinical context in which the document was prepared.
    """
    
    resource_type = "DocumentReferenceContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.encounter = None
        """ Context of the document  content.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.event = None
        """ Main clinical acts documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._event = None
        """ Primitive extension for event. Type `FHIRPrimitiveExtension` """
        
        self.facilityType = None
        """ Kind of facility where patient was seen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._facilityType = None
        """ Primitive extension for facilityType. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Time of service that is being documented.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.practiceSetting = None
        """ Additional details about where the content was created (e.g.
        clinical specialty).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._practiceSetting = None
        """ Primitive extension for practiceSetting. Type `FHIRPrimitiveExtension` """
        
        self.related = None
        """ Related identifiers or resources.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._related = None
        """ Primitive extension for related. Type `FHIRPrimitiveExtension` """
        
        self.sourcePatientInfo = None
        """ Patient demographics from source.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._sourcePatientInfo = None
        """ Primitive extension for sourcePatientInfo. Type `FHIRPrimitiveExtension` """
        
        super(DocumentReferenceContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentReferenceContext, self).elementProperties()
        js.extend([
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("event", "event", codeableconcept.CodeableConcept, True, None, False),
            ("_event", "_event", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("facilityType", "facilityType", codeableconcept.CodeableConcept, False, None, False),
            ("_facilityType", "_facilityType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("practiceSetting", "practiceSetting", codeableconcept.CodeableConcept, False, None, False),
            ("_practiceSetting", "_practiceSetting", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("related", "related", fhirreference.FHIRReference, True, None, False),
            ("_related", "_related", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourcePatientInfo", "sourcePatientInfo", fhirreference.FHIRReference, False, None, False),
            ("_sourcePatientInfo", "_sourcePatientInfo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other documents.
    
    Relationships that this document has with other document references that
    already exist.
    """
    
    resource_type = "DocumentReferenceRelatesTo"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ replaces | transforms | signs | appends.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Target of the relationship.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        super(DocumentReferenceRelatesTo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentReferenceRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, True),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment
from . import codeableconcept
from . import coding
from . import fhirinstant
from . import fhirreference
from . import identifier
from . import period