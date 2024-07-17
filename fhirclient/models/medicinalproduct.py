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
        
        self.attachedDocument = None
        """ Supporting documentation, typically for regulatory submission.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.clinicalTrial = None
        """ Clinical trials or studies that this product is involved in.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.combinedPharmaceuticalDoseForm = None
        """ The dose form for a single part product, or combined form of a
        multiple part product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        """ A product specific contact, person (in a role), or an organization.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.crossReference = None
        """ Reference to another product, e.g. for linking authorised to
        investigational product.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.domain = None
        """ If this medicine applies to human or veterinary uses.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier for this product. Could be an MPID.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.legalStatusOfSupply = None
        """ The legal status of supply of the medicinal product as classified
        by the regulator.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manufacturingBusinessOperation = None
        """ An operation applied to the product, for manufacturing or
        adminsitrative purpose.
        List of `MedicinalProductManufacturingBusinessOperation` items (represented as `dict` in JSON). """
        
        self.marketingStatus = None
        """ Marketing status of the medicinal product, in contrast to marketing
        authorizaton.
        List of `MarketingStatus` items (represented as `dict` in JSON). """
        
        self.masterFile = None
        """ A master file for to the medicinal product (e.g. Pharmacovigilance
        System Master File).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.name = None
        """ The product's name, including full name and possibly coded parts.
        List of `MedicinalProductName` items (represented as `dict` in JSON). """
        
        self.packagedMedicinalProduct = None
        """ Package representation for the product.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.paediatricUseIndicator = None
        """ If authorised for use in children.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.pharmaceuticalProduct = None
        """ Pharmaceutical aspects of product.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.productClassification = None
        """ Allows the product to be classified by various systems.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialDesignation = None
        """ Indicates if the medicinal product has an orphan designation for
        the treatment of a rare disease.
        List of `MedicinalProductSpecialDesignation` items (represented as `dict` in JSON). """
        
        self.specialMeasures = None
        """ Whether the Medicinal Product is subject to special measures for
        regulatory reasons.
        List of `str` items. """
        
        self.type = None
        """ Regulatory type, e.g. Investigational or Authorized.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProduct, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProduct, self).elementProperties()
        js.extend([
            ("additionalMonitoringIndicator", "additionalMonitoringIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("attachedDocument", "attachedDocument", fhirreference.FHIRReference, True, None, False),
            ("clinicalTrial", "clinicalTrial", fhirreference.FHIRReference, True, None, False),
            ("combinedPharmaceuticalDoseForm", "combinedPharmaceuticalDoseForm", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", fhirreference.FHIRReference, True, None, False),
            ("crossReference", "crossReference", identifier.Identifier, True, None, False),
            ("domain", "domain", coding.Coding, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("manufacturingBusinessOperation", "manufacturingBusinessOperation", MedicinalProductManufacturingBusinessOperation, True, None, False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("masterFile", "masterFile", fhirreference.FHIRReference, True, None, False),
            ("name", "name", MedicinalProductName, True, None, True),
            ("packagedMedicinalProduct", "packagedMedicinalProduct", fhirreference.FHIRReference, True, None, False),
            ("paediatricUseIndicator", "paediatricUseIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("pharmaceuticalProduct", "pharmaceuticalProduct", fhirreference.FHIRReference, True, None, False),
            ("productClassification", "productClassification", codeableconcept.CodeableConcept, True, None, False),
            ("specialDesignation", "specialDesignation", MedicinalProductSpecialDesignation, True, None, False),
            ("specialMeasures", "specialMeasures", str, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.confidentialityIndicator = None
        """ To indicate if this proces is commercially confidential.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.effectiveDate = None
        """ Regulatory authorization date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.manufacturer = None
        """ The manufacturer or establishment associated with the process.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.operationType = None
        """ The type of manufacturing operation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.regulator = None
        """ A regulator which oversees the operation.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MedicinalProductManufacturingBusinessOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductManufacturingBusinessOperation, self).elementProperties()
        js.extend([
            ("authorisationReferenceNumber", "authorisationReferenceNumber", identifier.Identifier, False, None, False),
            ("confidentialityIndicator", "confidentialityIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("effectiveDate", "effectiveDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("operationType", "operationType", codeableconcept.CodeableConcept, False, None, False),
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, False),
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
        
        self.namePart = None
        """ Coding words or phrases of the name.
        List of `MedicinalProductNameNamePart` items (represented as `dict` in JSON). """
        
        self.productName = None
        """ The full product name.
        Type `str`. """
        
        super(MedicinalProductName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductName, self).elementProperties()
        js.extend([
            ("countryLanguage", "countryLanguage", MedicinalProductNameCountryLanguage, True, None, False),
            ("namePart", "namePart", MedicinalProductNameNamePart, True, None, False),
            ("productName", "productName", str, False, None, True),
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
        
        self.jurisdiction = None
        """ Jurisdiction code for where this name applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.language = None
        """ Language code for this name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductNameCountryLanguage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductNameCountryLanguage, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, True),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
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
        
        self.type = None
        """ Idenifying type for this part of the name (e.g. strength part).
        Type `Coding` (represented as `dict` in JSON). """
        
        super(MedicinalProductNameNamePart, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductNameNamePart, self).elementProperties()
        js.extend([
            ("part", "part", str, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
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
        
        self.identifier = None
        """ Identifier for the designation, or procedure number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indicationCodeableConcept = None
        """ Condition for which the medicinal use applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.indicationReference = None
        """ Condition for which the medicinal use applies.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.intendedUse = None
        """ The intended use of the product, e.g. prevention, treatment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.species = None
        """ Animal species for which this applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ For example granted, pending, expired or withdrawn.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of special designation, e.g. orphan drug, minor use.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductSpecialDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductSpecialDesignation, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", codeableconcept.CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", fhirreference.FHIRReference, False, "indication", False),
            ("intendedUse", "intendedUse", codeableconcept.CodeableConcept, False, None, False),
            ("species", "species", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import marketingstatus
