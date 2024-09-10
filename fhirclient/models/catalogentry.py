# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CatalogEntry).
# 2024, SMART Health IT.


from . import domainresource

class CatalogEntry(domainresource.DomainResource):
    """ An entry in a catalog.
    
    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    
    resource_type = "CatalogEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additionalCharacteristic = None
        """ Additional characteristics of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._additionalCharacteristic = None
        """ Primitive extension for additionalCharacteristic. Type `FHIRPrimitiveExtension` """
        
        self.additionalClassification = None
        """ Additional classification of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._additionalClassification = None
        """ Primitive extension for additionalClassification. Type `FHIRPrimitiveExtension` """
        
        self.additionalIdentifier = None
        """ Any additional identifier(s) for the catalog item, in the same
        granularity or concept.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._additionalIdentifier = None
        """ Primitive extension for additionalIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.classification = None
        """ Classification (category or class) of the item entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._classification = None
        """ Primitive extension for classification. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Unique identifier of the catalog item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.lastUpdated = None
        """ When was this catalog last updated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._lastUpdated = None
        """ Primitive extension for lastUpdated. Type `FHIRPrimitiveExtension` """
        
        self.orderable = None
        """ Whether the entry represents an orderable item.
        Type `bool`. """
        self._orderable = None
        """ Primitive extension for orderable. Type `FHIRPrimitiveExtension` """
        
        self.referencedItem = None
        """ The item that is being defined.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._referencedItem = None
        """ Primitive extension for referencedItem. Type `FHIRPrimitiveExtension` """
        
        self.relatedEntry = None
        """ An item that this catalog entry is related to.
        List of `CatalogEntryRelatedEntry` items (represented as `dict` in JSON). """
        self._relatedEntry = None
        """ Primitive extension for relatedEntry. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of item - medication, device, service, protocol or other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.validTo = None
        """ The date until which this catalog entry is expected to be active.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._validTo = None
        """ Primitive extension for validTo. Type `FHIRPrimitiveExtension` """
        
        self.validityPeriod = None
        """ The time period in which this catalog entry is expected to be
        active.
        Type `Period` (represented as `dict` in JSON). """
        self._validityPeriod = None
        """ Primitive extension for validityPeriod. Type `FHIRPrimitiveExtension` """
        
        super(CatalogEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("additionalCharacteristic", "additionalCharacteristic", codeableconcept.CodeableConcept, True, None, False),
            ("_additionalCharacteristic", "_additionalCharacteristic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("additionalClassification", "additionalClassification", codeableconcept.CodeableConcept, True, None, False),
            ("_additionalClassification", "_additionalClassification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("additionalIdentifier", "additionalIdentifier", identifier.Identifier, True, None, False),
            ("_additionalIdentifier", "_additionalIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("_classification", "_classification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lastUpdated", "lastUpdated", fhirdatetime.FHIRDateTime, False, None, False),
            ("_lastUpdated", "_lastUpdated", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("orderable", "orderable", bool, False, None, True),
            ("_orderable", "_orderable", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referencedItem", "referencedItem", fhirreference.FHIRReference, False, None, True),
            ("_referencedItem", "_referencedItem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, True, None, False),
            ("_relatedEntry", "_relatedEntry", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("validTo", "validTo", fhirdatetime.FHIRDateTime, False, None, False),
            ("_validTo", "_validTo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
            ("_validityPeriod", "_validityPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """ An item that this catalog entry is related to.
    
    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    
    resource_type = "CatalogEntryRelatedEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.item = None
        """ The reference to the related item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        self.relationtype = None
        """ triggers | is-replaced-by.
        Type `str`. """
        self._relationtype = None
        """ Primitive extension for relationtype. Type `FHIRPrimitiveExtension` """
        
        super(CatalogEntryRelatedEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("item", "item", fhirreference.FHIRReference, False, None, True),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationtype", "relationtype", str, False, None, True),
            ("_relationtype", "_relationtype", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period