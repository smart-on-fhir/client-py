#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/Sequence) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class Sequence(domainresource.DomainResource):
    """ A Sequence.
    
    Variation and Sequence data.
    """
    
    resource_name = "Sequence"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.allelicFrequency = None
        """ Allele frequencies.
        Type `float`. """
        
        self.allelicState = None
        """ The level of occurrence of a single DNA Sequence Variation within a
        set of chromosomes: Heteroplasmic / Homoplasmic / Homozygous /
        Heterozygous / Hemizygous.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.chip = None
        """ Information of chip.
        Type `SequenceChip` (represented as `dict` in JSON). """
        
        self.cigar = None
        """ Extended CIGAR string for aligning the sequence with reference
        bases.
        Type `str`. """
        
        self.coordinate = None
        """ The coordinate of the variant.
        List of `SequenceCoordinate` items (represented as `dict` in JSON). """
        
        self.copyNumberEvent = None
        """ Copy Number Event: Values: amplificaiton / deletion / LOH.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.observedAllele = None
        """ Nucleotide(s)/amino acids from start position of sequence to stop
        position of observed sequence.
        Type `str`. """
        
        self.quality = None
        """ Sequence Quality.
        List of `SequenceQuality` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Quantity of the sequence.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.readCoverage = None
        """ Average number of reads representing a given nucleotide in the
        reconstructed sequence.
        Type `int`. """
        
        self.referenceAllele = None
        """ Nucleotide(s)/amino acids from start position of sequence to stop
        position of reference sequence.
        Type `str`. """
        
        self.referenceSeq = None
        """ Reference identifier.  It must match the type in the Sequence.type
        field.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.repository = None
        """ External repository.
        List of `SequenceRepository` items (represented as `dict` in JSON). """
        
        self.species = None
        """ Supporting tests of human, viruses, and bacteria.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ AA | DNA | RNA.
        Type `str`. """
        
        self.variationID = None
        """ Identifier for variant and ClinVar, dbSNP or COSMIC identifier
        should be used.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Sequence, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Sequence, self).elementProperties()
        js.extend([
            ("allelicFrequency", "allelicFrequency", float, False, None, False),
            ("allelicState", "allelicState", codeableconcept.CodeableConcept, False, None, False),
            ("chip", "chip", SequenceChip, False, None, False),
            ("cigar", "cigar", str, False, None, False),
            ("coordinate", "coordinate", SequenceCoordinate, True, None, False),
            ("copyNumberEvent", "copyNumberEvent", codeableconcept.CodeableConcept, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("quality", "quality", SequenceQuality, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("referenceSeq", "referenceSeq", codeableconcept.CodeableConcept, False, None, False),
            ("repository", "repository", SequenceRepository, True, None, False),
            ("species", "species", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
            ("variationID", "variationID", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class SequenceChip(backboneelement.BackboneElement):
    """ Information of chip.
    """
    
    resource_name = "SequenceChip"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.chipId = None
        """ Chip id.
        Type `str`. """
        
        self.manufacturerId = None
        """ Chip manufacturer id.
        Type `str`. """
        
        self.version = None
        """ Chip version.
        Type `str`. """
        
        super(SequenceChip, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SequenceChip, self).elementProperties()
        js.extend([
            ("chipId", "chipId", str, False, None, False),
            ("manufacturerId", "manufacturerId", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class SequenceCoordinate(backboneelement.BackboneElement):
    """ The coordinate of the variant.
    """
    
    resource_name = "SequenceCoordinate"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.chromosome = None
        """ The chromosome containing the genetic finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.end = None
        """ 0-based end position (exclusive) of the sequence.
        Type `int`. """
        
        self.genomeBuild = None
        """ The Genome Build used for reference, following GRCh build versions
        e.g. 'GRCh 37'.
        Type `str`. """
        
        self.start = None
        """ 0-based start position (inclusive) of the sequence.
        Type `int`. """
        
        super(SequenceCoordinate, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SequenceCoordinate, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False),
            ("end", "end", int, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


class SequenceQuality(backboneelement.BackboneElement):
    """ Sequence Quality.
    
    Quality for sequence quality vary by platform reflecting differences in
    sequencing chemistry and digital processing.
    """
    
    resource_name = "SequenceQuality"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.end = None
        """ 0-based end position (exclusive) of the sequence.
        Type `int`. """
        
        self.platform = None
        """ Platform.
        Type `str`. """
        
        self.score = None
        """ Quality score.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.start = None
        """ 0-based start position (inclusive) of the sequence.
        Type `int`. """
        
        super(SequenceQuality, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SequenceQuality, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("platform", "platform", str, False, None, False),
            ("score", "score", quantity.Quantity, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


class SequenceRepository(backboneelement.BackboneElement):
    """ External repository.
    """
    
    resource_name = "SequenceRepository"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of the repository.
        Type `str`. """
        
        self.readGroupSetId = None
        """ Id of a GA4GH read group.
        Type `str`. """
        
        self.structure = None
        """ URI of the page containing information about the structure of the
        repository.
        Type `str`. """
        
        self.url = None
        """ URI of the repository.
        Type `str`. """
        
        self.variantId = None
        """ Id of a GA4GH variant.
        Type `str`. """
        
        super(SequenceRepository, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SequenceRepository, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("readGroupSetId", "readGroupSetId", str, False, None, False),
            ("structure", "structure", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("variantId", "variantId", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import quantity
