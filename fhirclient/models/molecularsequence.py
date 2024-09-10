# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MolecularSequence).
# 2024, SMART Health IT.


from . import domainresource

class MolecularSequence(domainresource.DomainResource):
    """ Information about a biological sequence.
    
    Raw data describing a biological sequence.
    """
    
    resource_type = "MolecularSequence"
    
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
        self._coordinateSystem = None
        """ Primitive extension for coordinateSystem. Type `FHIRPrimitiveExtension` """
        
        self.device = None
        """ The method for sequencing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._device = None
        """ Primitive extension for device. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Unique ID for this particular sequence. This is a FHIR-defined id.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.observedSeq = None
        """ Sequence that was observed.
        Type `str`. """
        self._observedSeq = None
        """ Primitive extension for observedSeq. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Who and/or what this is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Who should be responsible for test result.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.pointer = None
        """ Pointer to next atomic sequence.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._pointer = None
        """ Primitive extension for pointer. Type `FHIRPrimitiveExtension` """
        
        self.quality = None
        """ An set of value as quality of sequence.
        List of `MolecularSequenceQuality` items (represented as `dict` in JSON). """
        self._quality = None
        """ Primitive extension for quality. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ The number of copies of the sequence of interest.  (RNASeq).
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.readCoverage = None
        """ Average number of reads representing a given nucleotide in the
        reconstructed sequence.
        Type `int`. """
        self._readCoverage = None
        """ Primitive extension for readCoverage. Type `FHIRPrimitiveExtension` """
        
        self.referenceSeq = None
        """ A sequence used as reference.
        Type `MolecularSequenceReferenceSeq` (represented as `dict` in JSON). """
        self._referenceSeq = None
        """ Primitive extension for referenceSeq. Type `FHIRPrimitiveExtension` """
        
        self.repository = None
        """ External repository which contains detailed report related with
        observedSeq in this resource.
        List of `MolecularSequenceRepository` items (represented as `dict` in JSON). """
        self._repository = None
        """ Primitive extension for repository. Type `FHIRPrimitiveExtension` """
        
        self.specimen = None
        """ Specimen used for sequencing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._specimen = None
        """ Primitive extension for specimen. Type `FHIRPrimitiveExtension` """
        
        self.structureVariant = None
        """ Structural variant.
        List of `MolecularSequenceStructureVariant` items (represented as `dict` in JSON). """
        self._structureVariant = None
        """ Primitive extension for structureVariant. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ aa | dna | rna.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.variant = None
        """ Variant in sequence.
        List of `MolecularSequenceVariant` items (represented as `dict` in JSON). """
        self._variant = None
        """ Primitive extension for variant. Type `FHIRPrimitiveExtension` """
        
        super(MolecularSequence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequence, self).elementProperties()
        js.extend([
            ("coordinateSystem", "coordinateSystem", int, False, None, True),
            ("_coordinateSystem", "_coordinateSystem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("_device", "_device", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("observedSeq", "observedSeq", str, False, None, False),
            ("_observedSeq", "_observedSeq", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("pointer", "pointer", fhirreference.FHIRReference, True, None, False),
            ("_pointer", "_pointer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quality", "quality", MolecularSequenceQuality, True, None, False),
            ("_quality", "_quality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("_readCoverage", "_readCoverage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceSeq", "referenceSeq", MolecularSequenceReferenceSeq, False, None, False),
            ("_referenceSeq", "_referenceSeq", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("repository", "repository", MolecularSequenceRepository, True, None, False),
            ("_repository", "_repository", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("_specimen", "_specimen", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("structureVariant", "structureVariant", MolecularSequenceStructureVariant, True, None, False),
            ("_structureVariant", "_structureVariant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variant", "variant", MolecularSequenceVariant, True, None, False),
            ("_variant", "_variant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MolecularSequenceQuality(backboneelement.BackboneElement):
    """ An set of value as quality of sequence.
    
    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    
    resource_type = "MolecularSequenceQuality"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        """ End position of the sequence.
        Type `int`. """
        self._end = None
        """ Primitive extension for end. Type `FHIRPrimitiveExtension` """
        
        self.fScore = None
        """ F-score.
        Type `float`. """
        self._fScore = None
        """ Primitive extension for fScore. Type `FHIRPrimitiveExtension` """
        
        self.gtFP = None
        """ False positives where the non-REF alleles in the Truth and Query
        Call Sets match.
        Type `float`. """
        self._gtFP = None
        """ Primitive extension for gtFP. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ Method to get quality.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.precision = None
        """ Precision of comparison.
        Type `float`. """
        self._precision = None
        """ Primitive extension for precision. Type `FHIRPrimitiveExtension` """
        
        self.queryFP = None
        """ False positives.
        Type `float`. """
        self._queryFP = None
        """ Primitive extension for queryFP. Type `FHIRPrimitiveExtension` """
        
        self.queryTP = None
        """ True positives from the perspective of the query data.
        Type `float`. """
        self._queryTP = None
        """ Primitive extension for queryTP. Type `FHIRPrimitiveExtension` """
        
        self.recall = None
        """ Recall of comparison.
        Type `float`. """
        self._recall = None
        """ Primitive extension for recall. Type `FHIRPrimitiveExtension` """
        
        self.roc = None
        """ Receiver Operator Characteristic (ROC) Curve.
        Type `MolecularSequenceQualityRoc` (represented as `dict` in JSON). """
        self._roc = None
        """ Primitive extension for roc. Type `FHIRPrimitiveExtension` """
        
        self.score = None
        """ Quality score for the comparison.
        Type `Quantity` (represented as `dict` in JSON). """
        self._score = None
        """ Primitive extension for score. Type `FHIRPrimitiveExtension` """
        
        self.standardSequence = None
        """ Standard sequence for comparison.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._standardSequence = None
        """ Primitive extension for standardSequence. Type `FHIRPrimitiveExtension` """
        
        self.start = None
        """ Start position of the sequence.
        Type `int`. """
        self._start = None
        """ Primitive extension for start. Type `FHIRPrimitiveExtension` """
        
        self.truthFN = None
        """ False negatives.
        Type `float`. """
        self._truthFN = None
        """ Primitive extension for truthFN. Type `FHIRPrimitiveExtension` """
        
        self.truthTP = None
        """ True positives from the perspective of the truth data.
        Type `float`. """
        self._truthTP = None
        """ Primitive extension for truthTP. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ indel | snp | unknown.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MolecularSequenceQuality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceQuality, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("_end", "_end", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fScore", "fScore", float, False, None, False),
            ("_fScore", "_fScore", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("gtFP", "gtFP", float, False, None, False),
            ("_gtFP", "_gtFP", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("precision", "precision", float, False, None, False),
            ("_precision", "_precision", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("queryFP", "queryFP", float, False, None, False),
            ("_queryFP", "_queryFP", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("queryTP", "queryTP", float, False, None, False),
            ("_queryTP", "_queryTP", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recall", "recall", float, False, None, False),
            ("_recall", "_recall", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("roc", "roc", MolecularSequenceQualityRoc, False, None, False),
            ("_roc", "_roc", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("score", "score", quantity.Quantity, False, None, False),
            ("_score", "_score", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("standardSequence", "standardSequence", codeableconcept.CodeableConcept, False, None, False),
            ("_standardSequence", "_standardSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("start", "start", int, False, None, False),
            ("_start", "_start", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("truthFN", "truthFN", float, False, None, False),
            ("_truthFN", "_truthFN", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("truthTP", "truthTP", float, False, None, False),
            ("_truthTP", "_truthTP", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
    """ Receiver Operator Characteristic (ROC) Curve.
    
    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """
    
    resource_type = "MolecularSequenceQualityRoc"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fMeasure = None
        """ FScore of the GQ score.
        List of `float` items. """
        self._fMeasure = None
        """ Primitive extension for fMeasure. Type `FHIRPrimitiveExtension` """
        
        self.numFN = None
        """ Roc score false negative numbers.
        List of `int` items. """
        self._numFN = None
        """ Primitive extension for numFN. Type `FHIRPrimitiveExtension` """
        
        self.numFP = None
        """ Roc score false positive numbers.
        List of `int` items. """
        self._numFP = None
        """ Primitive extension for numFP. Type `FHIRPrimitiveExtension` """
        
        self.numTP = None
        """ Roc score true positive numbers.
        List of `int` items. """
        self._numTP = None
        """ Primitive extension for numTP. Type `FHIRPrimitiveExtension` """
        
        self.precision = None
        """ Precision of the GQ score.
        List of `float` items. """
        self._precision = None
        """ Primitive extension for precision. Type `FHIRPrimitiveExtension` """
        
        self.score = None
        """ Genotype quality score.
        List of `int` items. """
        self._score = None
        """ Primitive extension for score. Type `FHIRPrimitiveExtension` """
        
        self.sensitivity = None
        """ Sensitivity of the GQ score.
        List of `float` items. """
        self._sensitivity = None
        """ Primitive extension for sensitivity. Type `FHIRPrimitiveExtension` """
        
        super(MolecularSequenceQualityRoc, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceQualityRoc, self).elementProperties()
        js.extend([
            ("fMeasure", "fMeasure", float, True, None, False),
            ("_fMeasure", "_fMeasure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numFN", "numFN", int, True, None, False),
            ("_numFN", "_numFN", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numFP", "numFP", int, True, None, False),
            ("_numFP", "_numFP", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numTP", "numTP", int, True, None, False),
            ("_numTP", "_numTP", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("precision", "precision", float, True, None, False),
            ("_precision", "_precision", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("score", "score", int, True, None, False),
            ("_score", "_score", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sensitivity", "sensitivity", float, True, None, False),
            ("_sensitivity", "_sensitivity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    """ A sequence used as reference.
    
    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    
    resource_type = "MolecularSequenceReferenceSeq"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chromosome = None
        """ Chromosome containing genetic finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._chromosome = None
        """ Primitive extension for chromosome. Type `FHIRPrimitiveExtension` """
        
        self.genomeBuild = None
        """ The Genome Build used for reference, following GRCh build versions
        e.g. 'GRCh 37'.
        Type `str`. """
        self._genomeBuild = None
        """ Primitive extension for genomeBuild. Type `FHIRPrimitiveExtension` """
        
        self.orientation = None
        """ sense | antisense.
        Type `str`. """
        self._orientation = None
        """ Primitive extension for orientation. Type `FHIRPrimitiveExtension` """
        
        self.referenceSeqId = None
        """ Reference identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._referenceSeqId = None
        """ Primitive extension for referenceSeqId. Type `FHIRPrimitiveExtension` """
        
        self.referenceSeqPointer = None
        """ A pointer to another MolecularSequence entity as reference sequence.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._referenceSeqPointer = None
        """ Primitive extension for referenceSeqPointer. Type `FHIRPrimitiveExtension` """
        
        self.referenceSeqString = None
        """ A string to represent reference sequence.
        Type `str`. """
        self._referenceSeqString = None
        """ Primitive extension for referenceSeqString. Type `FHIRPrimitiveExtension` """
        
        self.strand = None
        """ watson | crick.
        Type `str`. """
        self._strand = None
        """ Primitive extension for strand. Type `FHIRPrimitiveExtension` """
        
        self.windowEnd = None
        """ End position of the window on the reference sequence.
        Type `int`. """
        self._windowEnd = None
        """ Primitive extension for windowEnd. Type `FHIRPrimitiveExtension` """
        
        self.windowStart = None
        """ Start position of the window on the  reference sequence.
        Type `int`. """
        self._windowStart = None
        """ Primitive extension for windowStart. Type `FHIRPrimitiveExtension` """
        
        super(MolecularSequenceReferenceSeq, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False),
            ("_chromosome", "_chromosome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("_genomeBuild", "_genomeBuild", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("orientation", "orientation", str, False, None, False),
            ("_orientation", "_orientation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceSeqId", "referenceSeqId", codeableconcept.CodeableConcept, False, None, False),
            ("_referenceSeqId", "_referenceSeqId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceSeqPointer", "referenceSeqPointer", fhirreference.FHIRReference, False, None, False),
            ("_referenceSeqPointer", "_referenceSeqPointer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceSeqString", "referenceSeqString", str, False, None, False),
            ("_referenceSeqString", "_referenceSeqString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("strand", "strand", str, False, None, False),
            ("_strand", "_strand", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, False),
            ("_windowEnd", "_windowEnd", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("windowStart", "windowStart", int, False, None, False),
            ("_windowStart", "_windowStart", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MolecularSequenceRepository(backboneelement.BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.
    
    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """
    
    resource_type = "MolecularSequenceRepository"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.datasetId = None
        """ Id of the dataset that used to call for dataset in repository.
        Type `str`. """
        self._datasetId = None
        """ Primitive extension for datasetId. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Repository's name.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.readsetId = None
        """ Id of the read.
        Type `str`. """
        self._readsetId = None
        """ Primitive extension for readsetId. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ directlink | openapi | login | oauth | other.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ URI of the repository.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.variantsetId = None
        """ Id of the variantset that used to call for variantset in repository.
        Type `str`. """
        self._variantsetId = None
        """ Primitive extension for variantsetId. Type `FHIRPrimitiveExtension` """
        
        super(MolecularSequenceRepository, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceRepository, self).elementProperties()
        js.extend([
            ("datasetId", "datasetId", str, False, None, False),
            ("_datasetId", "_datasetId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("readsetId", "readsetId", str, False, None, False),
            ("_readsetId", "_readsetId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variantsetId", "variantsetId", str, False, None, False),
            ("_variantsetId", "_variantsetId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
    """ Structural variant.
    
    Information about chromosome structure variation.
    """
    
    resource_type = "MolecularSequenceStructureVariant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exact = None
        """ Does the structural variant have base pair resolution breakpoints?.
        Type `bool`. """
        self._exact = None
        """ Primitive extension for exact. Type `FHIRPrimitiveExtension` """
        
        self.inner = None
        """ Structural variant inner.
        Type `MolecularSequenceStructureVariantInner` (represented as `dict` in JSON). """
        self._inner = None
        """ Primitive extension for inner. Type `FHIRPrimitiveExtension` """
        
        self.length = None
        """ Structural variant length.
        Type `int`. """
        self._length = None
        """ Primitive extension for length. Type `FHIRPrimitiveExtension` """
        
        self.outer = None
        """ Structural variant outer.
        Type `MolecularSequenceStructureVariantOuter` (represented as `dict` in JSON). """
        self._outer = None
        """ Primitive extension for outer. Type `FHIRPrimitiveExtension` """
        
        self.variantType = None
        """ Structural variant change type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._variantType = None
        """ Primitive extension for variantType. Type `FHIRPrimitiveExtension` """
        
        super(MolecularSequenceStructureVariant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceStructureVariant, self).elementProperties()
        js.extend([
            ("exact", "exact", bool, False, None, False),
            ("_exact", "_exact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("inner", "inner", MolecularSequenceStructureVariantInner, False, None, False),
            ("_inner", "_inner", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("length", "length", int, False, None, False),
            ("_length", "_length", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outer", "outer", MolecularSequenceStructureVariantOuter, False, None, False),
            ("_outer", "_outer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variantType", "variantType", codeableconcept.CodeableConcept, False, None, False),
            ("_variantType", "_variantType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
    """ Structural variant inner.
    """
    
    resource_type = "MolecularSequenceStructureVariantInner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        """ Structural variant inner end.
        Type `int`. """
        self._end = None
        """ Primitive extension for end. Type `FHIRPrimitiveExtension` """
        
        self.start = None
        """ Structural variant inner start.
        Type `int`. """
        self._start = None
        """ Primitive extension for start. Type `FHIRPrimitiveExtension` """
        
        super(MolecularSequenceStructureVariantInner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantInner, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("_end", "_end", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("start", "start", int, False, None, False),
            ("_start", "_start", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
    """ Structural variant outer.
    """
    
    resource_type = "MolecularSequenceStructureVariantOuter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        """ Structural variant outer end.
        Type `int`. """
        self._end = None
        """ Primitive extension for end. Type `FHIRPrimitiveExtension` """
        
        self.start = None
        """ Structural variant outer start.
        Type `int`. """
        self._start = None
        """ Primitive extension for start. Type `FHIRPrimitiveExtension` """
        
        super(MolecularSequenceStructureVariantOuter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantOuter, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("_end", "_end", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("start", "start", int, False, None, False),
            ("_start", "_start", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MolecularSequenceVariant(backboneelement.BackboneElement):
    """ Variant in sequence.
    
    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """
    
    resource_type = "MolecularSequenceVariant"
    
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
        self._cigar = None
        """ Primitive extension for cigar. Type `FHIRPrimitiveExtension` """
        
        self.end = None
        """ End position of the variant on the reference sequence.
        Type `int`. """
        self._end = None
        """ Primitive extension for end. Type `FHIRPrimitiveExtension` """
        
        self.observedAllele = None
        """ Allele that was observed.
        Type `str`. """
        self._observedAllele = None
        """ Primitive extension for observedAllele. Type `FHIRPrimitiveExtension` """
        
        self.referenceAllele = None
        """ Allele in the reference sequence.
        Type `str`. """
        self._referenceAllele = None
        """ Primitive extension for referenceAllele. Type `FHIRPrimitiveExtension` """
        
        self.start = None
        """ Start position of the variant on the  reference sequence.
        Type `int`. """
        self._start = None
        """ Primitive extension for start. Type `FHIRPrimitiveExtension` """
        
        self.variantPointer = None
        """ Pointer to observed variant information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._variantPointer = None
        """ Primitive extension for variantPointer. Type `FHIRPrimitiveExtension` """
        
        super(MolecularSequenceVariant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MolecularSequenceVariant, self).elementProperties()
        js.extend([
            ("cigar", "cigar", str, False, None, False),
            ("_cigar", "_cigar", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("end", "end", int, False, None, False),
            ("_end", "_end", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("_observedAllele", "_observedAllele", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("_referenceAllele", "_referenceAllele", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("start", "start", int, False, None, False),
            ("_start", "_start", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variantPointer", "variantPointer", fhirreference.FHIRReference, False, None, False),
            ("_variantPointer", "_variantPointer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import identifier
from . import quantity