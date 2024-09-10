# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis).
# 2024, SMART Health IT.


from . import domainresource

class EffectEvidenceSynthesis(domainresource.DomainResource):
    """ A quantified estimate of effect based on a body of evidence.
    
    The EffectEvidenceSynthesis resource describes the difference in an outcome
    between exposures states in a population where the effect estimate is
    derived from a combination of research studies.
    """
    
    resource_type = "EffectEvidenceSynthesis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ When the effect evidence synthesis was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._approvalDate = None
        """ Primitive extension for approvalDate. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.certainty = None
        """ How certain is the effect.
        List of `EffectEvidenceSynthesisCertainty` items (represented as `dict` in JSON). """
        self._certainty = None
        """ Primitive extension for certainty. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        self._copyright = None
        """ Primitive extension for copyright. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the effect evidence synthesis.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._editor = None
        """ Primitive extension for editor. Type `FHIRPrimitiveExtension` """
        
        self.effectEstimate = None
        """ What was the estimated effect.
        List of `EffectEvidenceSynthesisEffectEstimate` items (represented as `dict` in JSON). """
        self._effectEstimate = None
        """ Primitive extension for effectEstimate. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ When the effect evidence synthesis is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._endorser = None
        """ Primitive extension for endorser. Type `FHIRPrimitiveExtension` """
        
        self.exposure = None
        """ What exposure?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._exposure = None
        """ Primitive extension for exposure. Type `FHIRPrimitiveExtension` """
        
        self.exposureAlternative = None
        """ What comparison exposure?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._exposureAlternative = None
        """ Primitive extension for exposureAlternative. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the effect evidence synthesis.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for effect evidence synthesis (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.lastReviewDate = None
        """ When the effect evidence synthesis was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._lastReviewDate = None
        """ Primitive extension for lastReviewDate. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this effect evidence synthesis (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ What outcome?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.population = None
        """ What population?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._population = None
        """ Primitive extension for population. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        self._relatedArtifact = None
        """ Primitive extension for relatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.resultsByExposure = None
        """ What was the result per exposure?.
        List of `EffectEvidenceSynthesisResultsByExposure` items (represented as `dict` in JSON). """
        self._resultsByExposure = None
        """ Primitive extension for resultsByExposure. Type `FHIRPrimitiveExtension` """
        
        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._reviewer = None
        """ Primitive extension for reviewer. Type `FHIRPrimitiveExtension` """
        
        self.sampleSize = None
        """ What sample size was involved?.
        Type `EffectEvidenceSynthesisSampleSize` (represented as `dict` in JSON). """
        self._sampleSize = None
        """ Primitive extension for sampleSize. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.studyType = None
        """ Type of study.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._studyType = None
        """ Primitive extension for studyType. Type `FHIRPrimitiveExtension` """
        
        self.synthesisType = None
        """ Type of synthesis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._synthesisType = None
        """ Primitive extension for synthesisType. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this effect evidence synthesis (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.topic = None
        """ The category of the EffectEvidenceSynthesis, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._topic = None
        """ Primitive extension for topic. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this effect evidence synthesis,
        represented as a URI (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the effect evidence synthesis.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(EffectEvidenceSynthesis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesis, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("_approvalDate", "_approvalDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("certainty", "certainty", EffectEvidenceSynthesisCertainty, True, None, False),
            ("_certainty", "_certainty", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("_editor", "_editor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectEstimate", "effectEstimate", EffectEvidenceSynthesisEffectEstimate, True, None, False),
            ("_effectEstimate", "_effectEstimate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("_endorser", "_endorser", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("exposure", "exposure", fhirreference.FHIRReference, False, None, True),
            ("_exposure", "_exposure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("exposureAlternative", "exposureAlternative", fhirreference.FHIRReference, False, None, True),
            ("_exposureAlternative", "_exposureAlternative", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("_lastReviewDate", "_lastReviewDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", fhirreference.FHIRReference, False, None, True),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("population", "population", fhirreference.FHIRReference, False, None, True),
            ("_population", "_population", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("_relatedArtifact", "_relatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resultsByExposure", "resultsByExposure", EffectEvidenceSynthesisResultsByExposure, True, None, False),
            ("_resultsByExposure", "_resultsByExposure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("_reviewer", "_reviewer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sampleSize", "sampleSize", EffectEvidenceSynthesisSampleSize, False, None, False),
            ("_sampleSize", "_sampleSize", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("studyType", "studyType", codeableconcept.CodeableConcept, False, None, False),
            ("_studyType", "_studyType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("synthesisType", "synthesisType", codeableconcept.CodeableConcept, False, None, False),
            ("_synthesisType", "_synthesisType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("_topic", "_topic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class EffectEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """ How certain is the effect.
    
    A description of the certainty of the effect estimate.
    """
    
    resource_type = "EffectEvidenceSynthesisCertainty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.certaintySubcomponent = None
        """ A component that contributes to the overall certainty.
        List of `EffectEvidenceSynthesisCertaintyCertaintySubcomponent` items (represented as `dict` in JSON). """
        self._certaintySubcomponent = None
        """ Primitive extension for certaintySubcomponent. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.rating = None
        """ Certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._rating = None
        """ Primitive extension for rating. Type `FHIRPrimitiveExtension` """
        
        super(EffectEvidenceSynthesisCertainty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisCertainty, self).elementProperties()
        js.extend([
            ("certaintySubcomponent", "certaintySubcomponent", EffectEvidenceSynthesisCertaintyCertaintySubcomponent, True, None, False),
            ("_certaintySubcomponent", "_certaintySubcomponent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
            ("_rating", "_rating", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EffectEvidenceSynthesisCertaintyCertaintySubcomponent(backboneelement.BackboneElement):
    """ A component that contributes to the overall certainty.
    
    A description of a component of the overall certainty.
    """
    
    resource_type = "EffectEvidenceSynthesisCertaintyCertaintySubcomponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.rating = None
        """ Subcomponent certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._rating = None
        """ Primitive extension for rating. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of subcomponent of certainty rating.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(EffectEvidenceSynthesisCertaintyCertaintySubcomponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
            ("_rating", "_rating", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EffectEvidenceSynthesisEffectEstimate(backboneelement.BackboneElement):
    """ What was the estimated effect.
    
    The estimated effect of the exposure variant.
    """
    
    resource_type = "EffectEvidenceSynthesisEffectEstimate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of effect estimate.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.precisionEstimate = None
        """ How precise the estimate is.
        List of `EffectEvidenceSynthesisEffectEstimatePrecisionEstimate` items (represented as `dict` in JSON). """
        self._precisionEstimate = None
        """ Primitive extension for precisionEstimate. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of efffect estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.unitOfMeasure = None
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._unitOfMeasure = None
        """ Primitive extension for unitOfMeasure. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ Point estimate.
        Type `float`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        self.variantState = None
        """ Variant exposure states.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._variantState = None
        """ Primitive extension for variantState. Type `FHIRPrimitiveExtension` """
        
        super(EffectEvidenceSynthesisEffectEstimate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisEffectEstimate, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("precisionEstimate", "precisionEstimate", EffectEvidenceSynthesisEffectEstimatePrecisionEstimate, True, None, False),
            ("_precisionEstimate", "_precisionEstimate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("_unitOfMeasure", "_unitOfMeasure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", float, False, None, False),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variantState", "variantState", codeableconcept.CodeableConcept, False, None, False),
            ("_variantState", "_variantState", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EffectEvidenceSynthesisEffectEstimatePrecisionEstimate(backboneelement.BackboneElement):
    """ How precise the estimate is.
    
    A description of the precision of the estimate for the effect.
    """
    
    resource_type = "EffectEvidenceSynthesisEffectEstimatePrecisionEstimate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.from_fhir = None
        """ Lower bound.
        Type `float`. """
        self._from_fhir = None
        """ Primitive extension for from_fhir. Type `FHIRPrimitiveExtension` """
        
        self.level = None
        """ Level of confidence interval.
        Type `float`. """
        self._level = None
        """ Primitive extension for level. Type `FHIRPrimitiveExtension` """
        
        self.to = None
        """ Upper bound.
        Type `float`. """
        self._to = None
        """ Primitive extension for to. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of precision estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(EffectEvidenceSynthesisEffectEstimatePrecisionEstimate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisEffectEstimatePrecisionEstimate, self).elementProperties()
        js.extend([
            ("from_fhir", "from", float, False, None, False),
            ("_from_fhir", "_from_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("level", "level", float, False, None, False),
            ("_level", "_level", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("to", "to", float, False, None, False),
            ("_to", "_to", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EffectEvidenceSynthesisResultsByExposure(backboneelement.BackboneElement):
    """ What was the result per exposure?.
    
    A description of the results for each exposure considered in the effect
    estimate.
    """
    
    resource_type = "EffectEvidenceSynthesisResultsByExposure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of results by exposure.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.exposureState = None
        """ exposure | exposure-alternative.
        Type `str`. """
        self._exposureState = None
        """ Primitive extension for exposureState. Type `FHIRPrimitiveExtension` """
        
        self.riskEvidenceSynthesis = None
        """ Risk evidence synthesis.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._riskEvidenceSynthesis = None
        """ Primitive extension for riskEvidenceSynthesis. Type `FHIRPrimitiveExtension` """
        
        self.variantState = None
        """ Variant exposure states.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._variantState = None
        """ Primitive extension for variantState. Type `FHIRPrimitiveExtension` """
        
        super(EffectEvidenceSynthesisResultsByExposure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisResultsByExposure, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("exposureState", "exposureState", str, False, None, False),
            ("_exposureState", "_exposureState", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("riskEvidenceSynthesis", "riskEvidenceSynthesis", fhirreference.FHIRReference, False, None, True),
            ("_riskEvidenceSynthesis", "_riskEvidenceSynthesis", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variantState", "variantState", codeableconcept.CodeableConcept, False, None, False),
            ("_variantState", "_variantState", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class EffectEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """ What sample size was involved?.
    
    A description of the size of the sample involved in the synthesis.
    """
    
    resource_type = "EffectEvidenceSynthesisSampleSize"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of sample size.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.numberOfParticipants = None
        """ How many participants?.
        Type `int`. """
        self._numberOfParticipants = None
        """ Primitive extension for numberOfParticipants. Type `FHIRPrimitiveExtension` """
        
        self.numberOfStudies = None
        """ How many studies?.
        Type `int`. """
        self._numberOfStudies = None
        """ Primitive extension for numberOfStudies. Type `FHIRPrimitiveExtension` """
        
        super(EffectEvidenceSynthesisSampleSize, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
            ("_numberOfParticipants", "_numberOfParticipants", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
            ("_numberOfStudies", "_numberOfStudies", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import usagecontext