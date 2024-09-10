# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceSpecification).
# 2024, SMART Health IT.


from . import domainresource

class SubstanceSpecification(domainresource.DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """
    
    resource_type = "SubstanceSpecification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Codes associated with the substance.
        List of `SubstanceSpecificationstr` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Textual comment about this record of a substance.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Textual description of the substance.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.domain = None
        """ If the substance applies to only human or veterinary use.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._domain = None
        """ Primitive extension for domain. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifier by which this substance is known.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.moiety = None
        """ Moiety, for structural modifications.
        List of `SubstanceSpecificationMoiety` items (represented as `dict` in JSON). """
        self._moiety = None
        """ Primitive extension for moiety. Type `FHIRPrimitiveExtension` """
        
        self.molecularWeight = None
        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
        List of `SubstanceSpecificationStructureIsotopeMolecularWeight` items (represented as `dict` in JSON). """
        self._molecularWeight = None
        """ Primitive extension for molecularWeight. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Names applicable to this substance.
        List of `SubstanceSpecificationName` items (represented as `dict` in JSON). """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.nucleicAcid = None
        """ Data items specific to nucleic acids.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._nucleicAcid = None
        """ Primitive extension for nucleicAcid. Type `FHIRPrimitiveExtension` """
        
        self.polymer = None
        """ Data items specific to polymers.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._polymer = None
        """ Primitive extension for polymer. Type `FHIRPrimitiveExtension` """
        
        self.property = None
        """ General specifications for this substance, including how it is
        related to other substances.
        List of `SubstanceSpecificationProperty` items (represented as `dict` in JSON). """
        self._property = None
        """ Primitive extension for property. Type `FHIRPrimitiveExtension` """
        
        self.protein = None
        """ Data items specific to proteins.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._protein = None
        """ Primitive extension for protein. Type `FHIRPrimitiveExtension` """
        
        self.referenceInformation = None
        """ General information detailing this substance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._referenceInformation = None
        """ Primitive extension for referenceInformation. Type `FHIRPrimitiveExtension` """
        
        self.relationship = None
        """ A link between this substance and another, with details of the
        relationship.
        List of `SubstanceSpecificationRelationship` items (represented as `dict` in JSON). """
        self._relationship = None
        """ Primitive extension for relationship. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.sourceMaterial = None
        """ Material or taxonomic/anatomical source for the substance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._sourceMaterial = None
        """ Primitive extension for sourceMaterial. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ Status of substance within the catalogue e.g. approved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.structure = None
        """ Structural information.
        Type `SubstanceSpecificationStructure` (represented as `dict` in JSON). """
        self._structure = None
        """ Primitive extension for structure. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ High level categorization, e.g. polymer or nucleic acid.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecification, self).elementProperties()
        js.extend([
            ("code", "code", SubstanceSpecificationstr, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False),
            ("_domain", "_domain", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("moiety", "moiety", SubstanceSpecificationMoiety, True, None, False),
            ("_moiety", "_moiety", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, True, None, False),
            ("_molecularWeight", "_molecularWeight", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", SubstanceSpecificationName, True, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("nucleicAcid", "nucleicAcid", fhirreference.FHIRReference, False, None, False),
            ("_nucleicAcid", "_nucleicAcid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("polymer", "polymer", fhirreference.FHIRReference, False, None, False),
            ("_polymer", "_polymer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("property", "property", SubstanceSpecificationProperty, True, None, False),
            ("_property", "_property", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("protein", "protein", fhirreference.FHIRReference, False, None, False),
            ("_protein", "_protein", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceInformation", "referenceInformation", fhirreference.FHIRReference, False, None, False),
            ("_referenceInformation", "_referenceInformation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", SubstanceSpecificationRelationship, True, None, False),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceMaterial", "sourceMaterial", fhirreference.FHIRReference, False, None, False),
            ("_sourceMaterial", "_sourceMaterial", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("structure", "structure", SubstanceSpecificationStructure, False, None, False),
            ("_structure", "_structure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class SubstanceSpecificationMoiety(backboneelement.BackboneElement):
    """ Moiety, for structural modifications.
    """
    
    resource_type = "SubstanceSpecificationMoiety"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amountQuantity = None
        """ Quantitative value for this moiety.
        Type `Quantity` (represented as `dict` in JSON). """
        self._amountQuantity = None
        """ Primitive extension for amountQuantity. Type `FHIRPrimitiveExtension` """
        
        self.amountString = None
        """ Quantitative value for this moiety.
        Type `str`. """
        self._amountString = None
        """ Primitive extension for amountString. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifier by which this moiety substance is known.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.molecularFormula = None
        """ Molecular formula.
        Type `str`. """
        self._molecularFormula = None
        """ Primitive extension for molecularFormula. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Textual name for this moiety substance.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.opticalActivity = None
        """ Optical activity type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._opticalActivity = None
        """ Primitive extension for opticalActivity. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ Role that the moiety is playing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        self.stereochemistry = None
        """ Stereochemistry type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._stereochemistry = None
        """ Primitive extension for stereochemistry. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationMoiety, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationMoiety, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("_amountQuantity", "_amountQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountString", "amountString", str, False, "amount", False),
            ("_amountString", "_amountString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("_molecularFormula", "_molecularFormula", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("_opticalActivity", "_opticalActivity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
            ("_stereochemistry", "_stereochemistry", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceSpecificationName(backboneelement.BackboneElement):
    """ Names applicable to this substance.
    """
    
    resource_type = "SubstanceSpecificationName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.domain = None
        """ The use context of this name for example if there is a different
        name a drug active ingredient as opposed to a food colour additive.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._domain = None
        """ Primitive extension for domain. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ The jurisdiction where this name applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.language = None
        """ Language of the name.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ The actual name.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.official = None
        """ Details of the official nature of this name.
        List of `SubstanceSpecificationNameOfficial` items (represented as `dict` in JSON). """
        self._official = None
        """ Primitive extension for official. Type `FHIRPrimitiveExtension` """
        
        self.preferred = None
        """ If this is the preferred name for this substance.
        Type `bool`. """
        self._preferred = None
        """ Primitive extension for preferred. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ The status of the name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.synonym = None
        """ A synonym of this name.
        List of `SubstanceSpecificationName` items (represented as `dict` in JSON). """
        self._synonym = None
        """ Primitive extension for synonym. Type `FHIRPrimitiveExtension` """
        
        self.translation = None
        """ A translation for this name.
        List of `SubstanceSpecificationName` items (represented as `dict` in JSON). """
        self._translation = None
        """ Primitive extension for translation. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Name type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationName, self).elementProperties()
        js.extend([
            ("domain", "domain", codeableconcept.CodeableConcept, True, None, False),
            ("_domain", "_domain", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, True, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("official", "official", SubstanceSpecificationNameOfficial, True, None, False),
            ("_official", "_official", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("_preferred", "_preferred", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("synonym", "synonym", SubstanceSpecificationName, True, None, False),
            ("_synonym", "_synonym", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("translation", "translation", SubstanceSpecificationName, True, None, False),
            ("_translation", "_translation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceSpecificationNameOfficial(backboneelement.BackboneElement):
    """ Details of the official nature of this name.
    """
    
    resource_type = "SubstanceSpecificationNameOfficial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ Which authority uses this official name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._authority = None
        """ Primitive extension for authority. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date of official name change.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ The status of the official name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationNameOfficial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationNameOfficial, self).elementProperties()
        js.extend([
            ("authority", "authority", codeableconcept.CodeableConcept, False, None, False),
            ("_authority", "_authority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceSpecificationProperty(backboneelement.BackboneElement):
    """ General specifications for this substance, including how it is related to
    other substances.
    """
    
    resource_type = "SubstanceSpecificationProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amountQuantity = None
        """ Quantitative value for this property.
        Type `Quantity` (represented as `dict` in JSON). """
        self._amountQuantity = None
        """ Primitive extension for amountQuantity. Type `FHIRPrimitiveExtension` """
        
        self.amountString = None
        """ Quantitative value for this property.
        Type `str`. """
        self._amountString = None
        """ Primitive extension for amountString. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ A category for this property, e.g. Physical, Chemical, Enzymatic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Property type e.g. viscosity, pH, isoelectric point.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.definingSubstanceCodeableConcept = None
        """ A substance upon which a defining property depends (e.g. for
        solubility: in water, in alcohol).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._definingSubstanceCodeableConcept = None
        """ Primitive extension for definingSubstanceCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.definingSubstanceReference = None
        """ A substance upon which a defining property depends (e.g. for
        solubility: in water, in alcohol).
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._definingSubstanceReference = None
        """ Primitive extension for definingSubstanceReference. Type `FHIRPrimitiveExtension` """
        
        self.parameters = None
        """ Parameters that were used in the measurement of a property (e.g.
        for viscosity: measured at 20C with a pH of 7.1).
        Type `str`. """
        self._parameters = None
        """ Primitive extension for parameters. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationProperty, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("_amountQuantity", "_amountQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountString", "amountString", str, False, "amount", False),
            ("_amountString", "_amountString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definingSubstanceCodeableConcept", "definingSubstanceCodeableConcept", codeableconcept.CodeableConcept, False, "definingSubstance", False),
            ("_definingSubstanceCodeableConcept", "_definingSubstanceCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definingSubstanceReference", "definingSubstanceReference", fhirreference.FHIRReference, False, "definingSubstance", False),
            ("_definingSubstanceReference", "_definingSubstanceReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parameters", "parameters", str, False, None, False),
            ("_parameters", "_parameters", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceSpecificationRelationship(backboneelement.BackboneElement):
    """ A link between this substance and another, with details of the relationship.
    """
    
    resource_type = "SubstanceSpecificationRelationship"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amountQuantity = None
        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
        Type `Quantity` (represented as `dict` in JSON). """
        self._amountQuantity = None
        """ Primitive extension for amountQuantity. Type `FHIRPrimitiveExtension` """
        
        self.amountRange = None
        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
        Type `Range` (represented as `dict` in JSON). """
        self._amountRange = None
        """ Primitive extension for amountRange. Type `FHIRPrimitiveExtension` """
        
        self.amountRatio = None
        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
        Type `Ratio` (represented as `dict` in JSON). """
        self._amountRatio = None
        """ Primitive extension for amountRatio. Type `FHIRPrimitiveExtension` """
        
        self.amountRatioLowLimit = None
        """ For use when the numeric.
        Type `Ratio` (represented as `dict` in JSON). """
        self._amountRatioLowLimit = None
        """ Primitive extension for amountRatioLowLimit. Type `FHIRPrimitiveExtension` """
        
        self.amountString = None
        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
        Type `str`. """
        self._amountString = None
        """ Primitive extension for amountString. Type `FHIRPrimitiveExtension` """
        
        self.amountType = None
        """ An operator for the amount, for example "average", "approximately",
        "less than".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._amountType = None
        """ Primitive extension for amountType. Type `FHIRPrimitiveExtension` """
        
        self.isDefining = None
        """ For example where an enzyme strongly bonds with a particular
        substance, this is a defining relationship for that enzyme, out of
        several possible substance relationships.
        Type `bool`. """
        self._isDefining = None
        """ Primitive extension for isDefining. Type `FHIRPrimitiveExtension` """
        
        self.relationship = None
        """ For example "salt to parent", "active moiety", "starting material".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._relationship = None
        """ Primitive extension for relationship. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.substanceCodeableConcept = None
        """ A pointer to another substance, as a resource or just a
        representational code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._substanceCodeableConcept = None
        """ Primitive extension for substanceCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.substanceReference = None
        """ A pointer to another substance, as a resource or just a
        representational code.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._substanceReference = None
        """ Primitive extension for substanceReference. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationRelationship, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationRelationship, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("_amountQuantity", "_amountQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountRange", "amountRange", range.Range, False, "amount", False),
            ("_amountRange", "_amountRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountRatio", "amountRatio", ratio.Ratio, False, "amount", False),
            ("_amountRatio", "_amountRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountRatioLowLimit", "amountRatioLowLimit", ratio.Ratio, False, None, False),
            ("_amountRatioLowLimit", "_amountRatioLowLimit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountString", "amountString", str, False, "amount", False),
            ("_amountString", "_amountString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False),
            ("_amountType", "_amountType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("_isDefining", "_isDefining", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", False),
            ("_substanceCodeableConcept", "_substanceCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", False),
            ("_substanceReference", "_substanceReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceSpecificationStructure(backboneelement.BackboneElement):
    """ Structural information.
    """
    
    resource_type = "SubstanceSpecificationStructure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.isotope = None
        """ Applicable for single substances that contain a radionuclide or a
        non-natural isotopic ratio.
        List of `SubstanceSpecificationStructureIsotope` items (represented as `dict` in JSON). """
        self._isotope = None
        """ Primitive extension for isotope. Type `FHIRPrimitiveExtension` """
        
        self.molecularFormula = None
        """ Molecular formula.
        Type `str`. """
        self._molecularFormula = None
        """ Primitive extension for molecularFormula. Type `FHIRPrimitiveExtension` """
        
        self.molecularFormulaByMoiety = None
        """ Specified per moiety according to the Hill system, i.e. first C,
        then H, then alphabetical, each moiety separated by a dot.
        Type `str`. """
        self._molecularFormulaByMoiety = None
        """ Primitive extension for molecularFormulaByMoiety. Type `FHIRPrimitiveExtension` """
        
        self.molecularWeight = None
        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
        Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON). """
        self._molecularWeight = None
        """ Primitive extension for molecularWeight. Type `FHIRPrimitiveExtension` """
        
        self.opticalActivity = None
        """ Optical activity type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._opticalActivity = None
        """ Primitive extension for opticalActivity. Type `FHIRPrimitiveExtension` """
        
        self.representation = None
        """ Molecular structural representation.
        List of `SubstanceSpecificationStructureRepresentation` items (represented as `dict` in JSON). """
        self._representation = None
        """ Primitive extension for representation. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.stereochemistry = None
        """ Stereochemistry type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._stereochemistry = None
        """ Primitive extension for stereochemistry. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructure, self).elementProperties()
        js.extend([
            ("isotope", "isotope", SubstanceSpecificationStructureIsotope, True, None, False),
            ("_isotope", "_isotope", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("_molecularFormula", "_molecularFormula", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("molecularFormulaByMoiety", "molecularFormulaByMoiety", str, False, None, False),
            ("_molecularFormulaByMoiety", "_molecularFormulaByMoiety", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("_molecularWeight", "_molecularWeight", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("_opticalActivity", "_opticalActivity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("representation", "representation", SubstanceSpecificationStructureRepresentation, True, None, False),
            ("_representation", "_representation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
            ("_stereochemistry", "_stereochemistry", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceSpecificationStructureIsotope(backboneelement.BackboneElement):
    """ Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """
    
    resource_type = "SubstanceSpecificationStructureIsotope"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.halfLife = None
        """ Half life - for a non-natural nuclide.
        Type `Quantity` (represented as `dict` in JSON). """
        self._halfLife = None
        """ Primitive extension for halfLife. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Substance identifier for each non-natural or radioisotope.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.molecularWeight = None
        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
        Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON). """
        self._molecularWeight = None
        """ Primitive extension for molecularWeight. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Substance name for each non-natural or radioisotope.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.substitution = None
        """ The type of isotopic substitution present in a single substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._substitution = None
        """ Primitive extension for substitution. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationStructureIsotope, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotope, self).elementProperties()
        js.extend([
            ("halfLife", "halfLife", quantity.Quantity, False, None, False),
            ("_halfLife", "_halfLife", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("_molecularWeight", "_molecularWeight", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", codeableconcept.CodeableConcept, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substitution", "substitution", codeableconcept.CodeableConcept, False, None, False),
            ("_substitution", "_substitution", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceSpecificationStructureIsotopeMolecularWeight(backboneelement.BackboneElement):
    """ The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """
    
    resource_type = "SubstanceSpecificationStructureIsotopeMolecularWeight"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Used to capture quantitative values for a variety of elements. If
        only limits are given, the arithmetic mean would be the average. If
        only a single definite value for a given element is given, it would
        be captured in this field.
        Type `Quantity` (represented as `dict` in JSON). """
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ The method by which the molecular weight was determined.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of molecular weight such as exact, average (also known as.
        number average), weight average.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceSpecificationStructureRepresentation(backboneelement.BackboneElement):
    """ Molecular structural representation.
    """
    
    resource_type = "SubstanceSpecificationStructureRepresentation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attachment = None
        """ An attached file with the structural representation.
        Type `Attachment` (represented as `dict` in JSON). """
        self._attachment = None
        """ Primitive extension for attachment. Type `FHIRPrimitiveExtension` """
        
        self.representation = None
        """ The structural representation as text string in a format e.g.
        InChI, SMILES, MOLFILE, CDX.
        Type `str`. """
        self._representation = None
        """ Primitive extension for representation. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of structure (e.g. Full, Partial, Representative).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationStructureRepresentation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, False),
            ("_attachment", "_attachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("_representation", "_representation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceSpecificationstr(backboneelement.BackboneElement):
    """ Codes associated with the substance.
    """
    
    resource_type = "SubstanceSpecificationstr"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ The specific code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Any comment can be provided in this field, if necessary.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ Status of the code assignment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusDate = None
        """ The date at which the code status is changed as part of the
        terminology maintenance.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._statusDate = None
        """ Primitive extension for statusDate. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceSpecificationstr, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationstr, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusDate", "statusDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_statusDate", "_statusDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio