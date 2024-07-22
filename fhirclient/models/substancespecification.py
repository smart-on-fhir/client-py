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
        
        self.comment = None
        """ Textual comment about this record of a substance.
        Type `str`. """
        
        self.description = None
        """ Textual description of the substance.
        Type `str`. """
        
        self.domain = None
        """ If the substance applies to only human or veterinary use.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier by which this substance is known.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.moiety = None
        """ Moiety, for structural modifications.
        List of `SubstanceSpecificationMoiety` items (represented as `dict` in JSON). """
        
        self.molecularWeight = None
        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
        List of `SubstanceSpecificationStructureIsotopeMolecularWeight` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Names applicable to this substance.
        List of `SubstanceSpecificationName` items (represented as `dict` in JSON). """
        
        self.nucleicAcid = None
        """ Data items specific to nucleic acids.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.polymer = None
        """ Data items specific to polymers.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.property = None
        """ General specifications for this substance, including how it is
        related to other substances.
        List of `SubstanceSpecificationProperty` items (represented as `dict` in JSON). """
        
        self.protein = None
        """ Data items specific to proteins.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referenceInformation = None
        """ General information detailing this substance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ A link between this substance and another, with details of the
        relationship.
        List of `SubstanceSpecificationRelationship` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.sourceMaterial = None
        """ Material or taxonomic/anatomical source for the substance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ Status of substance within the catalogue e.g. approved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.structure = None
        """ Structural information.
        Type `SubstanceSpecificationStructure` (represented as `dict` in JSON). """
        
        self.type = None
        """ High level categorization, e.g. polymer or nucleic acid.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecification, self).elementProperties()
        js.extend([
            ("code", "code", SubstanceSpecificationstr, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("moiety", "moiety", SubstanceSpecificationMoiety, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, True, None, False),
            ("name", "name", SubstanceSpecificationName, True, None, False),
            ("nucleicAcid", "nucleicAcid", fhirreference.FHIRReference, False, None, False),
            ("polymer", "polymer", fhirreference.FHIRReference, False, None, False),
            ("property", "property", SubstanceSpecificationProperty, True, None, False),
            ("protein", "protein", fhirreference.FHIRReference, False, None, False),
            ("referenceInformation", "referenceInformation", fhirreference.FHIRReference, False, None, False),
            ("relationship", "relationship", SubstanceSpecificationRelationship, True, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("sourceMaterial", "sourceMaterial", fhirreference.FHIRReference, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("structure", "structure", SubstanceSpecificationStructure, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.amountString = None
        """ Quantitative value for this moiety.
        Type `str`. """
        
        self.identifier = None
        """ Identifier by which this moiety substance is known.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.molecularFormula = None
        """ Molecular formula.
        Type `str`. """
        
        self.name = None
        """ Textual name for this moiety substance.
        Type `str`. """
        
        self.opticalActivity = None
        """ Optical activity type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.role = None
        """ Role that the moiety is playing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.stereochemistry = None
        """ Stereochemistry type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationMoiety, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationMoiety, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.jurisdiction = None
        """ The jurisdiction where this name applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.language = None
        """ Language of the name.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ The actual name.
        Type `str`. """
        
        self.official = None
        """ Details of the official nature of this name.
        List of `SubstanceSpecificationNameOfficial` items (represented as `dict` in JSON). """
        
        self.preferred = None
        """ If this is the preferred name for this substance.
        Type `bool`. """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ The status of the name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.synonym = None
        """ A synonym of this name.
        List of `SubstanceSpecificationName` items (represented as `dict` in JSON). """
        
        self.translation = None
        """ A translation for this name.
        List of `SubstanceSpecificationName` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Name type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationName, self).elementProperties()
        js.extend([
            ("domain", "domain", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("language", "language", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("official", "official", SubstanceSpecificationNameOfficial, True, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("synonym", "synonym", SubstanceSpecificationName, True, None, False),
            ("translation", "translation", SubstanceSpecificationName, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.date = None
        """ Date of official name change.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.status = None
        """ The status of the official name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationNameOfficial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationNameOfficial, self).elementProperties()
        js.extend([
            ("authority", "authority", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.amountString = None
        """ Quantitative value for this property.
        Type `str`. """
        
        self.category = None
        """ A category for this property, e.g. Physical, Chemical, Enzymatic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Property type e.g. viscosity, pH, isoelectric point.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definingSubstanceCodeableConcept = None
        """ A substance upon which a defining property depends (e.g. for
        solubility: in water, in alcohol).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definingSubstanceReference = None
        """ A substance upon which a defining property depends (e.g. for
        solubility: in water, in alcohol).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.parameters = None
        """ Parameters that were used in the measurement of a property (e.g.
        for viscosity: measured at 20C with a pH of 7.1).
        Type `str`. """
        
        super(SubstanceSpecificationProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationProperty, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("definingSubstanceCodeableConcept", "definingSubstanceCodeableConcept", codeableconcept.CodeableConcept, False, "definingSubstance", False),
            ("definingSubstanceReference", "definingSubstanceReference", fhirreference.FHIRReference, False, "definingSubstance", False),
            ("parameters", "parameters", str, False, None, False),
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
        
        self.amountRange = None
        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
        Type `Range` (represented as `dict` in JSON). """
        
        self.amountRatio = None
        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.amountRatioLowLimit = None
        """ For use when the numeric.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.amountString = None
        """ A numeric factor for the relationship, for instance to express that
        the salt of a substance has some percentage of the active substance
        in relation to some other.
        Type `str`. """
        
        self.amountType = None
        """ An operator for the amount, for example "average", "approximately",
        "less than".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.isDefining = None
        """ For example where an enzyme strongly bonds with a particular
        substance, this is a defining relationship for that enzyme, out of
        several possible substance relationships.
        Type `bool`. """
        
        self.relationship = None
        """ For example "salt to parent", "active moiety", "starting material".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.substanceCodeableConcept = None
        """ A pointer to another substance, as a resource or just a
        representational code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.substanceReference = None
        """ A pointer to another substance, as a resource or just a
        representational code.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationRelationship, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationRelationship, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountRange", "amountRange", range.Range, False, "amount", False),
            ("amountRatio", "amountRatio", ratio.Ratio, False, "amount", False),
            ("amountRatioLowLimit", "amountRatioLowLimit", ratio.Ratio, False, None, False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", False),
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", False),
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
        
        self.molecularFormula = None
        """ Molecular formula.
        Type `str`. """
        
        self.molecularFormulaByMoiety = None
        """ Specified per moiety according to the Hill system, i.e. first C,
        then H, then alphabetical, each moiety separated by a dot.
        Type `str`. """
        
        self.molecularWeight = None
        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
        Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON). """
        
        self.opticalActivity = None
        """ Optical activity type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.representation = None
        """ Molecular structural representation.
        List of `SubstanceSpecificationStructureRepresentation` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.stereochemistry = None
        """ Stereochemistry type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructure, self).elementProperties()
        js.extend([
            ("isotope", "isotope", SubstanceSpecificationStructureIsotope, True, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("molecularFormulaByMoiety", "molecularFormulaByMoiety", str, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("representation", "representation", SubstanceSpecificationStructureRepresentation, True, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.identifier = None
        """ Substance identifier for each non-natural or radioisotope.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.molecularWeight = None
        """ The molecular weight or weight range (for proteins, polymers or
        nucleic acids).
        Type `SubstanceSpecificationStructureIsotopeMolecularWeight` (represented as `dict` in JSON). """
        
        self.name = None
        """ Substance name for each non-natural or radioisotope.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.substitution = None
        """ The type of isotopic substitution present in a single substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructureIsotope, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotope, self).elementProperties()
        js.extend([
            ("halfLife", "halfLife", quantity.Quantity, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("name", "name", codeableconcept.CodeableConcept, False, None, False),
            ("substitution", "substitution", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.method = None
        """ The method by which the molecular weight was determined.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of molecular weight such as exact, average (also known as.
        number average), weight average.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.representation = None
        """ The structural representation as text string in a format e.g.
        InChI, SMILES, MOLFILE, CDX.
        Type `str`. """
        
        self.type = None
        """ The type of structure (e.g. Full, Partial, Representative).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSpecificationStructureRepresentation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationStructureRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.comment = None
        """ Any comment can be provided in this field, if necessary.
        Type `str`. """
        
        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ Status of the code assignment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.statusDate = None
        """ The date at which the code status is changed as part of the
        terminology maintenance.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        super(SubstanceSpecificationstr, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSpecificationstr, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdatetime.FHIRDateTime, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio
