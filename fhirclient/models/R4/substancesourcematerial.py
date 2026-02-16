# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial).
# 2024, SMART Health IT.


from . import domainresource

class SubstanceSourceMaterial(domainresource.DomainResource):
    """ Source material shall capture information on the taxonomic and anatomical
    origins as well as the fraction of a material that can result in or can be
    modified to form a substance. This set of data elements shall be used to
    define polymer substances isolated from biological matrices. Taxonomic and
    anatomical origins shall be described using a controlled vocabulary as
    required. This information is captured for naturally derived polymers ( .
    starch) and structurally diverse substances. For Organisms belonging to the
    Kingdom Plantae the Substance level defines the fresh material of a single
    species or infraspecies, the Herbal Drug and the Herbal preparation. For
    Herbal preparations, the fraction information will be captured at the
    Substance information level and additional information for herbal extracts
    will be captured at the Specified Substance Group 1 information level. See
    for further explanation the Substance Class: Structurally Diverse and the
    herbal annex.
    """
    
    resource_type = "SubstanceSourceMaterial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.countryOfOrigin = None
        """ The country where the plant material is harvested or the countries
        where the plasma is sourced from as laid down in accordance with
        the Plasma Master File. For “Plasma-derived substances” the
        attribute country of origin provides information about the
        countries used for the manufacturing of the Cryopoor plama or
        Crioprecipitate.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.developmentStage = None
        """ Stage of life for animals, plants, insects and microorganisms. This
        information shall be provided only when the substance is
        significantly different in these stages (e.g. foetal bovine serum).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fractionDescription = None
        """ Many complex materials are fractions of parts of plants, animals,
        or minerals. Fraction elements are often necessary to define both
        Substances and Specified Group 1 Substances. For substances derived
        from Plants, fraction information will be captured at the Substance
        information level ( . Oils, Juices and Exudates). Additional
        information for Extracts, such as extraction solvent composition,
        will be captured at the Specified Substance Group 1 information
        level. For plasma-derived products fraction information will be
        captured at the Substance and the Specified Substance Group 1
        levels.
        List of `SubstanceSourceMaterialFractionDescription` items (represented as `dict` in JSON). """
        
        self.geographicalLocation = None
        """ The place/region where the plant is harvested or the places/regions
        where the animal source material has its habitat.
        List of `str` items. """
        
        self.organism = None
        """ This subclause describes the organism which the substance is
        derived from. For vaccines, the parent organism shall be specified
        based on these subclause elements. As an example, full taxonomy
        will be described for the Substance Name: ., Leaf.
        Type `SubstanceSourceMaterialOrganism` (represented as `dict` in JSON). """
        
        self.organismId = None
        """ The unique identifier associated with the source material parent
        organism shall be specified.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organismName = None
        """ The organism accepted Scientific name shall be provided based on
        the organism taxonomy.
        Type `str`. """
        
        self.parentSubstanceId = None
        """ The parent of the herbal drug Ginkgo biloba, Leaf is the substance
        ID of the substance (fresh) of Ginkgo biloba L. or Ginkgo biloba L.
        (Whole plant).
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.parentSubstanceName = None
        """ The parent substance of the Herbal Drug, or Herbal preparation.
        List of `str` items. """
        
        self.partDescription = None
        """ To do.
        List of `SubstanceSourceMaterialPartDescription` items (represented as `dict` in JSON). """
        
        self.sourceMaterialClass = None
        """ General high level classification of the source material specific
        to the origin of the material.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sourceMaterialState = None
        """ The state of the source material when extracted.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sourceMaterialType = None
        """ The type of the source material shall be specified based on a
        controlled vocabulary. For vaccines, this subclause refers to the
        class of infectious agent.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSourceMaterial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSourceMaterial, self).elementProperties()
        js.extend([
            ("countryOfOrigin", "countryOfOrigin", codeableconcept.CodeableConcept, True, None, False),
            ("developmentStage", "developmentStage", codeableconcept.CodeableConcept, False, None, False),
            ("fractionDescription", "fractionDescription", SubstanceSourceMaterialFractionDescription, True, None, False),
            ("geographicalLocation", "geographicalLocation", str, True, None, False),
            ("organism", "organism", SubstanceSourceMaterialOrganism, False, None, False),
            ("organismId", "organismId", identifier.Identifier, False, None, False),
            ("organismName", "organismName", str, False, None, False),
            ("parentSubstanceId", "parentSubstanceId", identifier.Identifier, True, None, False),
            ("parentSubstanceName", "parentSubstanceName", str, True, None, False),
            ("partDescription", "partDescription", SubstanceSourceMaterialPartDescription, True, None, False),
            ("sourceMaterialClass", "sourceMaterialClass", codeableconcept.CodeableConcept, False, None, False),
            ("sourceMaterialState", "sourceMaterialState", codeableconcept.CodeableConcept, False, None, False),
            ("sourceMaterialType", "sourceMaterialType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class SubstanceSourceMaterialFractionDescription(backboneelement.BackboneElement):
    """ Many complex materials are fractions of parts of plants, animals, or
    minerals. Fraction elements are often necessary to define both Substances
    and Specified Group 1 Substances. For substances derived from Plants,
    fraction information will be captured at the Substance information level (
    . Oils, Juices and Exudates). Additional information for Extracts, such as
    extraction solvent composition, will be captured at the Specified Substance
    Group 1 information level. For plasma-derived products fraction information
    will be captured at the Substance and the Specified Substance Group 1
    levels.
    """
    
    resource_type = "SubstanceSourceMaterialFractionDescription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fraction = None
        """ This element is capturing information about the fraction of a plant
        part, or human plasma for fractionation.
        Type `str`. """
        
        self.materialType = None
        """ The specific type of the material constituting the component. For
        Herbal preparations the particulars of the extracts (liquid/dry) is
        described in Specified Substance Group 1.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSourceMaterialFractionDescription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSourceMaterialFractionDescription, self).elementProperties()
        js.extend([
            ("fraction", "fraction", str, False, None, False),
            ("materialType", "materialType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSourceMaterialOrganism(backboneelement.BackboneElement):
    """ This subclause describes the organism which the substance is derived from.
    For vaccines, the parent organism shall be specified based on these
    subclause elements. As an example, full taxonomy will be described for the
    Substance Name: ., Leaf.
    """
    
    resource_type = "SubstanceSourceMaterialOrganism"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ 4.9.13.6.1 Author type (Conditional).
        List of `SubstanceSourceMaterialOrganismAuthor` items (represented as `dict` in JSON). """
        
        self.family = None
        """ The family of an organism shall be specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.genus = None
        """ The genus of an organism shall be specified; refers to the Latin
        epithet of the genus element of the plant/animal scientific name;
        it is present in names for genera, species and infraspecies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.hybrid = None
        """ 4.9.13.8.1 Hybrid species maternal organism ID (Optional).
        Type `SubstanceSourceMaterialOrganismHybrid` (represented as `dict` in JSON). """
        
        self.intraspecificDescription = None
        """ The intraspecific description of an organism shall be specified
        based on a controlled vocabulary. For Influenza Vaccine, the
        intraspecific description shall contain the syntax of the antigen
        in line with the WHO convention.
        Type `str`. """
        
        self.intraspecificType = None
        """ The Intraspecific type of an organism shall be specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.organismGeneral = None
        """ 4.9.13.7.1 Kingdom (Conditional).
        Type `SubstanceSourceMaterialOrganismOrganismGeneral` (represented as `dict` in JSON). """
        
        self.species = None
        """ The species of an organism shall be specified; refers to the Latin
        epithet of the species of the plant/animal; it is present in names
        for species and infraspecies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSourceMaterialOrganism, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSourceMaterialOrganism, self).elementProperties()
        js.extend([
            ("author", "author", SubstanceSourceMaterialOrganismAuthor, True, None, False),
            ("family", "family", codeableconcept.CodeableConcept, False, None, False),
            ("genus", "genus", codeableconcept.CodeableConcept, False, None, False),
            ("hybrid", "hybrid", SubstanceSourceMaterialOrganismHybrid, False, None, False),
            ("intraspecificDescription", "intraspecificDescription", str, False, None, False),
            ("intraspecificType", "intraspecificType", codeableconcept.CodeableConcept, False, None, False),
            ("organismGeneral", "organismGeneral", SubstanceSourceMaterialOrganismOrganismGeneral, False, None, False),
            ("species", "species", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSourceMaterialOrganismAuthor(backboneelement.BackboneElement):
    """ 4.9.13.6.1 Author type (Conditional).
    """
    
    resource_type = "SubstanceSourceMaterialOrganismAuthor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorDescription = None
        """ The author of an organism species shall be specified. The author
        year of an organism shall also be specified when applicable; refers
        to the year in which the first author(s) published the
        infraspecific plant/animal name (of any rank).
        Type `str`. """
        
        self.authorType = None
        """ The type of author of an organism species shall be specified. The
        parenthetical author of an organism species refers to the first
        author who published the plant/animal name (of any rank). The
        primary author of an organism species refers to the first
        author(s), who validly published the plant/animal name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSourceMaterialOrganismAuthor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSourceMaterialOrganismAuthor, self).elementProperties()
        js.extend([
            ("authorDescription", "authorDescription", str, False, None, False),
            ("authorType", "authorType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSourceMaterialOrganismHybrid(backboneelement.BackboneElement):
    """ 4.9.13.8.1 Hybrid species maternal organism ID (Optional).
    """
    
    resource_type = "SubstanceSourceMaterialOrganismHybrid"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.hybridType = None
        """ The hybrid type of an organism shall be specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.maternalOrganismId = None
        """ The identifier of the maternal species constituting the hybrid
        organism shall be specified based on a controlled vocabulary. For
        plants, the parents aren’t always known, and it is unlikely that it
        will be known which is maternal and which is paternal.
        Type `str`. """
        
        self.maternalOrganismName = None
        """ The name of the maternal species constituting the hybrid organism
        shall be specified. For plants, the parents aren’t always known,
        and it is unlikely that it will be known which is maternal and
        which is paternal.
        Type `str`. """
        
        self.paternalOrganismId = None
        """ The identifier of the paternal species constituting the hybrid
        organism shall be specified based on a controlled vocabulary.
        Type `str`. """
        
        self.paternalOrganismName = None
        """ The name of the paternal species constituting the hybrid organism
        shall be specified.
        Type `str`. """
        
        super(SubstanceSourceMaterialOrganismHybrid, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSourceMaterialOrganismHybrid, self).elementProperties()
        js.extend([
            ("hybridType", "hybridType", codeableconcept.CodeableConcept, False, None, False),
            ("maternalOrganismId", "maternalOrganismId", str, False, None, False),
            ("maternalOrganismName", "maternalOrganismName", str, False, None, False),
            ("paternalOrganismId", "paternalOrganismId", str, False, None, False),
            ("paternalOrganismName", "paternalOrganismName", str, False, None, False),
        ])
        return js


class SubstanceSourceMaterialOrganismOrganismGeneral(backboneelement.BackboneElement):
    """ 4.9.13.7.1 Kingdom (Conditional).
    """
    
    resource_type = "SubstanceSourceMaterialOrganismOrganismGeneral"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.class_fhir = None
        """ The class of an organism shall be specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.kingdom = None
        """ The kingdom of an organism shall be specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.order = None
        """ The order of an organism shall be specified,.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.phylum = None
        """ The phylum of an organism shall be specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSourceMaterialOrganismOrganismGeneral, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSourceMaterialOrganismOrganismGeneral, self).elementProperties()
        js.extend([
            ("class_fhir", "class", codeableconcept.CodeableConcept, False, None, False),
            ("kingdom", "kingdom", codeableconcept.CodeableConcept, False, None, False),
            ("order", "order", codeableconcept.CodeableConcept, False, None, False),
            ("phylum", "phylum", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceSourceMaterialPartDescription(backboneelement.BackboneElement):
    """ To do.
    """
    
    resource_type = "SubstanceSourceMaterialPartDescription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.part = None
        """ Entity of anatomical origin of source material within an organism.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.partLocation = None
        """ The detailed anatomic location when the part can be extracted from
        different anatomical locations of the organism. Multiple
        alternative locations may apply.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceSourceMaterialPartDescription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceSourceMaterialPartDescription, self).elementProperties()
        js.extend([
            ("part", "part", codeableconcept.CodeableConcept, False, None, False),
            ("partLocation", "partLocation", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import identifier
