# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DocumentManifest).
# 2024, SMART Health IT.


from . import domainresource

class DocumentManifest(domainresource.DomainResource):
    """ A list that defines a set of documents.
    
    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """
    
    resource_type = "DocumentManifest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ Who and/or what authored the DocumentManifest.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.content = None
        """ Items in manifest.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._content = None
        """ Primitive extension for content. Type `FHIRPrimitiveExtension` """
        
        self.created = None
        """ When this document manifest created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Human-readable description (title).
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Other identifiers for the manifest.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.masterIdentifier = None
        """ Unique Identifier for the set of documents.
        Type `Identifier` (represented as `dict` in JSON). """
        self._masterIdentifier = None
        """ Primitive extension for masterIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.recipient = None
        """ Intended to get notified about this set of documents.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._recipient = None
        """ Primitive extension for recipient. Type `FHIRPrimitiveExtension` """
        
        self.related = None
        """ Related things.
        List of `DocumentManifestRelated` items (represented as `dict` in JSON). """
        self._related = None
        """ Primitive extension for related. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ The source system/application/software.
        Type `str`. """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ current | superseded | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ The subject of the set of documents.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Kind of document set.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(DocumentManifest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentManifest, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("content", "content", fhirreference.FHIRReference, True, None, True),
            ("_content", "_content", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, False),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False, None, False),
            ("_masterIdentifier", "_masterIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("_recipient", "_recipient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("related", "related", DocumentManifestRelated, True, None, False),
            ("_related", "_related", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", str, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class DocumentManifestRelated(backboneelement.BackboneElement):
    """ Related things.
    
    Related identifiers or resources associated with the DocumentManifest.
    """
    
    resource_type = "DocumentManifestRelated"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifiers of things that are related.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.ref = None
        """ Related Resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._ref = None
        """ Primitive extension for ref. Type `FHIRPrimitiveExtension` """
        
        super(DocumentManifestRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentManifestRelated, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ref", "ref", fhirreference.FHIRReference, False, None, False),
            ("_ref", "_ref", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier