#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/Sequence) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class Sequence(domainresource.DomainResource):
    """ A Sequence.
    
    Variation and Sequence data.
    """
    
    resource_name = "Sequence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allelicFrequency = None
        """ Allele frequencies.
        Type `float`. """
        
        self.allelicState = None
        """ The level of occurrence of a single DNA Sequence Variation within a
        set of chromosomes: Heteroplasmic / Homoplasmic / Homozygous /
        Heterozygous / Hemizygous.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.copyNumberEvent = None
        """ Copy Number Event: Values: amplificaiton / deletion / LOH.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.device = None
        """ The method for sequencing.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.observation = None
        """ Observation-genetics.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        self.observedSeq = None
        """ Observed Sequence.
        Type `str`. """
        
        self.patient = None
        """ Who and/or what this is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.pointer = None
        """ Pointer to next atomic sequence.
        List of `FHIRReference` items referencing `Sequence` (represented as `dict` in JSON). """
        
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
        
        self.referenceSeq = None
        """ Reference sequence.
        List of `SequenceReferenceSeq` items (represented as `dict` in JSON). """
        
        self.repository = None
        """ External repository.
        List of `SequenceRepository` items (represented as `dict` in JSON). """
        
        self.species = None
        """ Supporting tests of human, viruses, and bacteria.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimen used for sequencing.
        Type `FHIRReference` referencing `Specimen` (represented as `dict` in JSON). """
        
        self.structureVariation = None
        """ None.
        Type `SequenceStructureVariation` (represented as `dict` in JSON). """
        
        self.type = None
        """ AA | DNA | RNA.
        Type `str`. """
        
        self.variation = None
        """ Variation info in this sequence.
        Type `SequenceVariation` (represented as `dict` in JSON). """
        
        super(Sequence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Sequence, self).elementProperties()
        js.extend([
            ("allelicFrequency", "allelicFrequency", float, False, None, False),
            ("allelicState", "allelicState", codeableconcept.CodeableConcept, False, None, False),
            ("copyNumberEvent", "copyNumberEvent", codeableconcept.CodeableConcept, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("observation", "observation", fhirreference.FHIRReference, False, None, False),
            ("observedSeq", "observedSeq", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("pointer", "pointer", fhirreference.FHIRReference, True, None, False),
            ("quality", "quality", SequenceQuality, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("referenceSeq", "referenceSeq", SequenceReferenceSeq, True, None, False),
            ("repository", "repository", SequenceRepository, True, None, False),
            ("species", "species", codeableconcept.CodeableConcept, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("structureVariation", "structureVariation", SequenceStructureVariation, False, None, False),
            ("type", "type", str, False, None, True),
            ("variation", "variation", SequenceVariation, False, None, False),
        ])
        return js


from . import backboneelement

class SequenceQuality(backboneelement.BackboneElement):
    """ Sequence Quality.
    
    Quality for sequence quality vary by platform reflecting differences in
    sequencing chemistry and digital processing.
    """
    
    resource_name = "SequenceQuality"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        """ 0-based end position (exclusive) of the sequence.
        Type `int`. """
        
        self.method = None
        """ Method for quality.
        Type `str`. """
        
        self.score = None
        """ Quality score.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.start = None
        """ 0-based start position (inclusive) of the sequence.
        Type `int`. """
        
        super(SequenceQuality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceQuality, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("method", "method", str, False, None, False),
            ("score", "score", quantity.Quantity, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


class SequenceReferenceSeq(backboneelement.BackboneElement):
    """ Reference sequence.
    
    Reference Sequence. It can be described in two ways. One is provide the
    unique identifier of reference sequence submitted to NCBI. The start and
    end position of window on reference sequence should be defined.  The other
    way is using  genome build, chromosome number,and also the start, end
    position of window (this method is specifically for DNA reference sequence)
    .
    """
    
    resource_name = "SequenceReferenceSeq"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chromosome = None
        """ The chromosome containing the genetic finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.genomeBuild = None
        """ The Genome Build used for reference, following GRCh build versions
        e.g. 'GRCh 37'.
        Type `str`. """
        
        self.referenceSeqId = None
        """ Reference identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.referenceSeqPointer = None
        """ A Pointer to another Sequence entity as refence sequence.
        Type `FHIRReference` referencing `Sequence` (represented as `dict` in JSON). """
        
        self.referenceSeqString = None
        """ A Reference Sequence string.
        Type `str`. """
        
        self.windowEnd = None
        """ 0-based end position (exclusive) of the window on the reference
        sequence.
        Type `int`. """
        
        self.windowStart = None
        """ 0-based start position (inclusive) of the window on the  reference
        sequence.
        Type `int`. """
        
        super(SequenceReferenceSeq, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("referenceSeqId", "referenceSeqId", codeableconcept.CodeableConcept, False, None, True),
            ("referenceSeqPointer", "referenceSeqPointer", fhirreference.FHIRReference, False, None, False),
            ("referenceSeqString", "referenceSeqString", str, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, True),
            ("windowStart", "windowStart", int, False, None, True),
        ])
        return js


class SequenceRepository(backboneelement.BackboneElement):
    """ External repository.
    
    Configurations of the external repository.
    """
    
    resource_name = "SequenceRepository"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of the repository.
        Type `str`. """
        
        self.readId = None
        """ Id of the read.
        Type `str`. """
        
        self.url = None
        """ URI of the repository.
        Type `str`. """
        
        self.variantId = None
        """ Id of the variant.
        Type `str`. """
        
        super(SequenceRepository, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceRepository, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("readId", "readId", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("variantId", "variantId", str, False, None, False),
        ])
        return js


class SequenceStructureVariation(backboneelement.BackboneElement):
    """ None.
    
    Structural variant.
    """
    
    resource_name = "SequenceStructureVariation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.inner = None
        """ None.
        Type `SequenceStructureVariationInner` (represented as `dict` in JSON). """
        
        self.length = None
        """ Structural Variant Length.
        Type `int`. """
        
        self.outer = None
        """ None.
        Type `SequenceStructureVariationOuter` (represented as `dict` in JSON). """
        
        self.precisionOfBoundaries = None
        """ Precision of boundaries.
        Type `str`. """
        
        self.reportedaCGHRatio = None
        """ Structural Variant reported aCGH ratio.
        Type `float`. """
        
        super(SequenceStructureVariation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceStructureVariation, self).elementProperties()
        js.extend([
            ("inner", "inner", SequenceStructureVariationInner, False, None, False),
            ("length", "length", int, False, None, False),
            ("outer", "outer", SequenceStructureVariationOuter, False, None, False),
            ("precisionOfBoundaries", "precisionOfBoundaries", str, False, None, False),
            ("reportedaCGHRatio", "reportedaCGHRatio", float, False, None, False),
        ])
        return js


class SequenceStructureVariationInner(backboneelement.BackboneElement):
    """ None.
    
    Structural variant inner.
    """
    
    resource_name = "SequenceStructureVariationInner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        """ Structural Variant Inner Start-End.
        Type `int`. """
        
        self.start = None
        """ Structural Variant Inner Start-End.
        Type `int`. """
        
        super(SequenceStructureVariationInner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceStructureVariationInner, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


class SequenceStructureVariationOuter(backboneelement.BackboneElement):
    """ None.
    
    Structural variant outer.
    """
    
    resource_name = "SequenceStructureVariationOuter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        """ Structural Variant Outer Start-End.
        Type `int`. """
        
        self.start = None
        """ Structural Variant Outer Start-End.
        Type `int`. """
        
        super(SequenceStructureVariationOuter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceStructureVariationOuter, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


class SequenceVariation(backboneelement.BackboneElement):
    """ Variation info in this sequence.
    """
    
    resource_name = "SequenceVariation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cigar = None
        """ Extended CIGAR string for aligning the sequence with reference
        bases.
        Type `str`. """
        
        self.end = None
        """ 0-based end position (exclusive) of the variation on the reference
        sequence.
        Type `int`. """
        
        self.observedAllele = None
        """ Nucleotide(s)/amino acids from start position to stop position of
        observed variation.
        Type `str`. """
        
        self.referenceAllele = None
        """ Nucleotide(s)/amino acids from start position to stop position of
        reference variation.
        Type `str`. """
        
        self.start = None
        """ 0-based start position (inclusive) of the variation on the
        reference sequence.
        Type `int`. """
        
        super(SequenceVariation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceVariation, self).elementProperties()
        js.extend([
            ("cigar", "cigar", str, False, None, False),
            ("end", "end", int, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import quantity
