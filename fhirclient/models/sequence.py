#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Sequence) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Sequence(domainresource.DomainResource):
    """ Information about a biological sequence.
    
    Raw data describing a biological sequence.
    """
    
    resource_type = "Sequence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coordinateSystem = None
        """ Base number of coordinate system (0 for 0-based numbering or
        coordinates, inclusive start, exclusive end, 1 for 1-based
        numbering, inclusive start, inclusive end).
        Type `int`. """
        
        self.device = None
        """ The method for sequencing.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique ID for this particular sequence. This is a FHIR-defined id.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.observedSeq = None
        """ Sequence that was observed.
        Type `str`. """
        
        self.patient = None
        """ Who and/or what this is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who should be responsible for test result.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.pointer = None
        """ Pointer to next atomic sequence.
        List of `FHIRReference` items referencing `Sequence` (represented as `dict` in JSON). """
        
        self.quality = None
        """ An set of value as quality of sequence.
        List of `SequenceQuality` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The number of copies of the seqeunce of interest.  (RNASeq).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.readCoverage = None
        """ Average number of reads representing a given nucleotide in the
        reconstructed sequence.
        Type `int`. """
        
        self.referenceSeq = None
        """ A sequence used as reference.
        Type `SequenceReferenceSeq` (represented as `dict` in JSON). """
        
        self.repository = None
        """ External repository which contains detailed report related with
        observedSeq in this resource.
        List of `SequenceRepository` items (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimen used for sequencing.
        Type `FHIRReference` referencing `Specimen` (represented as `dict` in JSON). """
        
        self.type = None
        """ aa | dna | rna.
        Type `str`. """
        
        self.variant = None
        """ Variant in sequence.
        List of `SequenceVariant` items (represented as `dict` in JSON). """
        
        super(Sequence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Sequence, self).elementProperties()
        js.extend([
            ("coordinateSystem", "coordinateSystem", int, False, None, True),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("observedSeq", "observedSeq", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("pointer", "pointer", fhirreference.FHIRReference, True, None, False),
            ("quality", "quality", SequenceQuality, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("referenceSeq", "referenceSeq", SequenceReferenceSeq, False, None, False),
            ("repository", "repository", SequenceRepository, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, False),
            ("variant", "variant", SequenceVariant, True, None, False),
        ])
        return js


from . import backboneelement

class SequenceQuality(backboneelement.BackboneElement):
    """ An set of value as quality of sequence.
    
    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    
    resource_type = "SequenceQuality"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        """ End position of the sequence.
        Type `int`. """
        
        self.fScore = None
        """ F-score.
        Type `float`. """
        
        self.gtFP = None
        """ False positives where the non-REF alleles in the Truth and Query
        Call Sets match.
        Type `float`. """
        
        self.method = None
        """ Method to get quality.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.precision = None
        """ Precision of comparison.
        Type `float`. """
        
        self.queryFP = None
        """ False positives.
        Type `float`. """
        
        self.queryTP = None
        """ True positives from the perspective of the query data.
        Type `float`. """
        
        self.recall = None
        """ Recall of comparison.
        Type `float`. """
        
        self.score = None
        """ Quality score for the comparison.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.standardSequence = None
        """ Standard sequence for comparison.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.start = None
        """ Start position of the sequence.
        Type `int`. """
        
        self.truthFN = None
        """ False negatives.
        Type `float`. """
        
        self.truthTP = None
        """ True positives from the perspective of the truth data.
        Type `float`. """
        
        self.type = None
        """ indel | snp | unknown.
        Type `str`. """
        
        super(SequenceQuality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceQuality, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("fScore", "fScore", float, False, None, False),
            ("gtFP", "gtFP", float, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("precision", "precision", float, False, None, False),
            ("queryFP", "queryFP", float, False, None, False),
            ("queryTP", "queryTP", float, False, None, False),
            ("recall", "recall", float, False, None, False),
            ("score", "score", quantity.Quantity, False, None, False),
            ("standardSequence", "standardSequence", codeableconcept.CodeableConcept, False, None, False),
            ("start", "start", int, False, None, False),
            ("truthFN", "truthFN", float, False, None, False),
            ("truthTP", "truthTP", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class SequenceReferenceSeq(backboneelement.BackboneElement):
    """ A sequence used as reference.
    
    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    
    resource_type = "SequenceReferenceSeq"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chromosome = None
        """ Chromosome containing genetic finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.genomeBuild = None
        """ The Genome Build used for reference, following GRCh build versions
        e.g. 'GRCh 37'.
        Type `str`. """
        
        self.referenceSeqId = None
        """ Reference identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.referenceSeqPointer = None
        """ A Pointer to another Sequence entity as reference sequence.
        Type `FHIRReference` referencing `Sequence` (represented as `dict` in JSON). """
        
        self.referenceSeqString = None
        """ A string to represent reference sequence.
        Type `str`. """
        
        self.strand = None
        """ Directionality of DNA ( +1/-1).
        Type `int`. """
        
        self.windowEnd = None
        """ End position of the window on the reference sequence.
        Type `int`. """
        
        self.windowStart = None
        """ Start position of the window on the  reference sequence.
        Type `int`. """
        
        super(SequenceReferenceSeq, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("referenceSeqId", "referenceSeqId", codeableconcept.CodeableConcept, False, None, False),
            ("referenceSeqPointer", "referenceSeqPointer", fhirreference.FHIRReference, False, None, False),
            ("referenceSeqString", "referenceSeqString", str, False, None, False),
            ("strand", "strand", int, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, True),
            ("windowStart", "windowStart", int, False, None, True),
        ])
        return js


class SequenceRepository(backboneelement.BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.
    
    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """
    
    resource_type = "SequenceRepository"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.datasetId = None
        """ Id of the dataset that used to call for dataset in repository.
        Type `str`. """
        
        self.name = None
        """ Repository's name.
        Type `str`. """
        
        self.readsetId = None
        """ Id of the read.
        Type `str`. """
        
        self.type = None
        """ directlink | openapi | login | oauth | other.
        Type `str`. """
        
        self.url = None
        """ URI of the repository.
        Type `str`. """
        
        self.variantsetId = None
        """ Id of the variantset that used to call for variantset in repository.
        Type `str`. """
        
        super(SequenceRepository, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceRepository, self).elementProperties()
        js.extend([
            ("datasetId", "datasetId", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("readsetId", "readsetId", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("variantsetId", "variantsetId", str, False, None, False),
        ])
        return js


class SequenceVariant(backboneelement.BackboneElement):
    """ Variant in sequence.
    
    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """
    
    resource_type = "SequenceVariant"
    
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
        """ End position of the variant on the reference sequence.
        Type `int`. """
        
        self.observedAllele = None
        """ Allele that was observed.
        Type `str`. """
        
        self.referenceAllele = None
        """ Allele in the reference sequence.
        Type `str`. """
        
        self.start = None
        """ Start position of the variant on the  reference sequence.
        Type `int`. """
        
        self.variantPointer = None
        """ Pointer to observed variant information.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        super(SequenceVariant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SequenceVariant, self).elementProperties()
        js.extend([
            ("cigar", "cigar", str, False, None, False),
            ("end", "end", int, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("start", "start", int, False, None, False),
            ("variantPointer", "variantPointer", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
