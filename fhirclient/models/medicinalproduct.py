# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProduct).
# 2024, SMART Health IT.


from . import domainresource

class MedicinalProduct(domainresource.DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than
    direct patient care (e.g. regulatory use).
    """
    
    resource_type = "MedicinalProduct"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additionalMonitoringIndicator = None
        """ Whether the Medicinal Product is subject to additional monitoring
        for regulatory reasons.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._additionalMonitoringIndicator = None
        """ Primitive extension for additionalMonitoringIndicator. Type `FHIRPrimitiveExtension` """
        
        self.attachedDocument = None
        """ Supporting documentation, typically for regulatory submission.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._attachedDocument = None
        """ Primitive extension for attachedDocument. Type `FHIRPrimitiveExtension` """
        
        self.clinicalTrial = None
        """ Clinical trials or studies that this product is involved in.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._clinicalTrial = None
        """ Primitive extension for clinicalTrial. Type `FHIRPrimitiveExtension` """
        
        self.combinedPharmaceuticalDoseForm = None
        """ The dose form for a single part product, or combined form of a
        multiple part product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._combinedPharmaceuticalDoseForm = None
        """ Primitive extension for combinedPharmaceuticalDoseForm. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ A product specific contact, person (in a role), or an organization.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.crossReference = None
        """ Reference to another product, e.g. for linking authorised to
        investigational product.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._crossReference = None
        """ Primitive extension for crossReference. Type `FHIRPrimitiveExtension` """
        
        self.domain = None
        """ If this medicine applies to human or veterinary uses.
        Type `Coding` (represented as `dict` in JSON). """
        self._domain = None
        """ Primitive extension for domain. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier for this product. Could be an MPID.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.legalStatusOfSupply = None
        """ The legal status of supply of the medicinal product as classified
        by the regulator.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._legalStatusOfSupply = None
        """ Primitive extension for legalStatusOfSupply. Type `FHIRPrimitiveExtension` """
        
        self.manufacturingBusinessOperation = None
        """ An operation applied to the product, for manufacturing or
        adminsitrative purpose.
        List of `MedicinalProductManufacturingBusinessOperation` items (represented as `dict` in JSON). """
        self._manufacturingBusinessOperation = None
        """ Primitive extension for manufacturingBusinessOperation. Type `FHIRPrimitiveExtension` """
        
        self.marketingStatus = None
        """ Marketing status of the medicinal product, in contrast to marketing
        authorizaton.
        List of `MarketingStatus` items (represented as `dict` in JSON). """
        self._marketingStatus = None
        """ Primitive extension for marketingStatus. Type `FHIRPrimitiveExtension` """
        
        self.masterFile = None
        """ A master file for to the medicinal product (e.g. Pharmacovigilance
        System Master File).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._masterFile = None
        """ Primitive extension for masterFile. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ The product's name, including full name and possibly coded parts.
        List of `MedicinalProductName` items (represented as `dict` in JSON). """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.packagedMedicinalProduct = None
        """ Package representation for the product.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._packagedMedicinalProduct = None
        """ Primitive extension for packagedMedicinalProduct. Type `FHIRPrimitiveExtension` """
        
        self.paediatricUseIndicator = None
        """ If authorised for use in children.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._paediatricUseIndicator = None
        """ Primitive extension for paediatricUseIndicator. Type `FHIRPrimitiveExtension` """
        
        self.pharmaceuticalProduct = None
        """ Pharmaceutical aspects of product.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._pharmaceuticalProduct = None
        """ Primitive extension for pharmaceuticalProduct. Type `FHIRPrimitiveExtension` """
        
        self.productClassification = None
        """ Allows the product to be classified by various systems.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._productClassification = None
        """ Primitive extension for productClassification. Type `FHIRPrimitiveExtension` """
        
        self.specialDesignation = None
        """ Indicates if the medicinal product has an orphan designation for
        the treatment of a rare disease.
        List of `MedicinalProductSpecialDesignation` items (represented as `dict` in JSON). """
        self._specialDesignation = None
        """ Primitive extension for specialDesignation. Type `FHIRPrimitiveExtension` """
        
        self.specialMeasures = None
        """ Whether the Medicinal Product is subject to special measures for
        regulatory reasons.
        List of `str` items. """
        self._specialMeasures = None
        """ Primitive extension for specialMeasures. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Regulatory type, e.g. Investigational or Authorized.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProduct, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProduct, self).elementProperties()
        js.extend([
            ("additionalMonitoringIndicator", "additionalMonitoringIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("_additionalMonitoringIndicator", "_additionalMonitoringIndicator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("attachedDocument", "attachedDocument", fhirreference.FHIRReference, True, None, False),
            ("_attachedDocument", "_attachedDocument", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("clinicalTrial", "clinicalTrial", fhirreference.FHIRReference, True, None, False),
            ("_clinicalTrial", "_clinicalTrial", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("combinedPharmaceuticalDoseForm", "combinedPharmaceuticalDoseForm", codeableconcept.CodeableConcept, False, None, False),
            ("_combinedPharmaceuticalDoseForm", "_combinedPharmaceuticalDoseForm", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", fhirreference.FHIRReference, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("crossReference", "crossReference", identifier.Identifier, True, None, False),
            ("_crossReference", "_crossReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("domain", "domain", coding.Coding, False, None, False),
            ("_domain", "_domain", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("_legalStatusOfSupply", "_legalStatusOfSupply", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturingBusinessOperation", "manufacturingBusinessOperation", MedicinalProductManufacturingBusinessOperation, True, None, False),
            ("_manufacturingBusinessOperation", "_manufacturingBusinessOperation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("_marketingStatus", "_marketingStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("masterFile", "masterFile", fhirreference.FHIRReference, True, None, False),
            ("_masterFile", "_masterFile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", MedicinalProductName, True, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("packagedMedicinalProduct", "packagedMedicinalProduct", fhirreference.FHIRReference, True, None, False),
            ("_packagedMedicinalProduct", "_packagedMedicinalProduct", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paediatricUseIndicator", "paediatricUseIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("_paediatricUseIndicator", "_paediatricUseIndicator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("pharmaceuticalProduct", "pharmaceuticalProduct", fhirreference.FHIRReference, True, None, False),
            ("_pharmaceuticalProduct", "_pharmaceuticalProduct", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productClassification", "productClassification", codeableconcept.CodeableConcept, True, None, False),
            ("_productClassification", "_productClassification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialDesignation", "specialDesignation", MedicinalProductSpecialDesignation, True, None, False),
            ("_specialDesignation", "_specialDesignation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialMeasures", "specialMeasures", str, True, None, False),
            ("_specialMeasures", "_specialMeasures", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductManufacturingBusinessOperation(backboneelement.BackboneElement):
    """ An operation applied to the product, for manufacturing or adminsitrative
    purpose.
    """
    
    resource_type = "MedicinalProductManufacturingBusinessOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorisationReferenceNumber = None
        """ Regulatory authorization reference number.
        Type `Identifier` (represented as `dict` in JSON). """
        self._authorisationReferenceNumber = None
        """ Primitive extension for authorisationReferenceNumber. Type `FHIRPrimitiveExtension` """
        
        self.confidentialityIndicator = None
        """ To indicate if this proces is commercially confidential.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._confidentialityIndicator = None
        """ Primitive extension for confidentialityIndicator. Type `FHIRPrimitiveExtension` """
        
        self.effectiveDate = None
        """ Regulatory authorization date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._effectiveDate = None
        """ Primitive extension for effectiveDate. Type `FHIRPrimitiveExtension` """
        
        self.manufacturer = None
        """ The manufacturer or establishment associated with the process.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._manufacturer = None
        """ Primitive extension for manufacturer. Type `FHIRPrimitiveExtension` """
        
        self.operationType = None
        """ The type of manufacturing operation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._operationType = None
        """ Primitive extension for operationType. Type `FHIRPrimitiveExtension` """
        
        self.regulator = None
        """ A regulator which oversees the operation.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._regulator = None
        """ Primitive extension for regulator. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductManufacturingBusinessOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductManufacturingBusinessOperation, self).elementProperties()
        js.extend([
            ("authorisationReferenceNumber", "authorisationReferenceNumber", identifier.Identifier, False, None, False),
            ("_authorisationReferenceNumber", "_authorisationReferenceNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("confidentialityIndicator", "confidentialityIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("_confidentialityIndicator", "_confidentialityIndicator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectiveDate", "effectiveDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_effectiveDate", "_effectiveDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("_manufacturer", "_manufacturer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operationType", "operationType", codeableconcept.CodeableConcept, False, None, False),
            ("_operationType", "_operationType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, False),
            ("_regulator", "_regulator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductName(backboneelement.BackboneElement):
    """ The product's name, including full name and possibly coded parts.
    """
    
    resource_type = "MedicinalProductName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.countryLanguage = None
        """ Country where the name applies.
        List of `MedicinalProductNameCountryLanguage` items (represented as `dict` in JSON). """
        self._countryLanguage = None
        """ Primitive extension for countryLanguage. Type `FHIRPrimitiveExtension` """
        
        self.namePart = None
        """ Coding words or phrases of the name.
        List of `MedicinalProductNameNamePart` items (represented as `dict` in JSON). """
        self._namePart = None
        """ Primitive extension for namePart. Type `FHIRPrimitiveExtension` """
        
        self.productName = None
        """ The full product name.
        Type `str`. """
        self._productName = None
        """ Primitive extension for productName. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductName, self).elementProperties()
        js.extend([
            ("countryLanguage", "countryLanguage", MedicinalProductNameCountryLanguage, True, None, False),
            ("_countryLanguage", "_countryLanguage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("namePart", "namePart", MedicinalProductNameNamePart, True, None, False),
            ("_namePart", "_namePart", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productName", "productName", str, False, None, True),
            ("_productName", "_productName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductNameCountryLanguage(backboneelement.BackboneElement):
    """ Country where the name applies.
    """
    
    resource_type = "MedicinalProductNameCountryLanguage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ Country code for where this name applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._country = None
        """ Primitive extension for country. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Jurisdiction code for where this name applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.language = None
        """ Language code for this name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductNameCountryLanguage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductNameCountryLanguage, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, True),
            ("_country", "_country", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, False, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductNameNamePart(backboneelement.BackboneElement):
    """ Coding words or phrases of the name.
    """
    
    resource_type = "MedicinalProductNameNamePart"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.part = None
        """ A fragment of a product name.
        Type `str`. """
        self._part = None
        """ Primitive extension for part. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Idenifying type for this part of the name (e.g. strength part).
        Type `Coding` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductNameNamePart, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductNameNamePart, self).elementProperties()
        js.extend([
            ("part", "part", str, False, None, True),
            ("_part", "_part", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductSpecialDesignation(backboneelement.BackboneElement):
    """ Indicates if the medicinal product has an orphan designation for the
    treatment of a rare disease.
    """
    
    resource_type = "MedicinalProductSpecialDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ Date when the designation was granted.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifier for the designation, or procedure number.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.indicationCodeableConcept = None
        """ Condition for which the medicinal use applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._indicationCodeableConcept = None
        """ Primitive extension for indicationCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.indicationReference = None
        """ Condition for which the medicinal use applies.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._indicationReference = None
        """ Primitive extension for indicationReference. Type `FHIRPrimitiveExtension` """
        
        self.intendedUse = None
        """ The intended use of the product, e.g. prevention, treatment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._intendedUse = None
        """ Primitive extension for intendedUse. Type `FHIRPrimitiveExtension` """
        
        self.species = None
        """ Animal species for which this applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._species = None
        """ Primitive extension for species. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ For example granted, pending, expired or withdrawn.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of special designation, e.g. orphan drug, minor use.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductSpecialDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductSpecialDesignation, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", codeableconcept.CodeableConcept, False, "indication", False),
            ("_indicationCodeableConcept", "_indicationCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("indicationReference", "indicationReference", fhirreference.FHIRReference, False, "indication", False),
            ("_indicationReference", "_indicationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("intendedUse", "intendedUse", codeableconcept.CodeableConcept, False, None, False),
            ("_intendedUse", "_intendedUse", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("species", "species", codeableconcept.CodeableConcept, False, None, False),
            ("_species", "_species", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import marketingstatus