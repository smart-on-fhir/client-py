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
        
        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.certainty = None
        """ How certain is the effect.
        List of `EffectEvidenceSynthesisCertainty` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the effect evidence synthesis.
        Type `str`. """
        
        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectEstimate = None
        """ What was the estimated effect.
        List of `EffectEvidenceSynthesisEffectEstimate` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        """ When the effect evidence synthesis is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.exposure = None
        """ What exposure?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.exposureAlternative = None
        """ What comparison exposure?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the effect evidence synthesis.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for effect evidence synthesis (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ When the effect evidence synthesis was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this effect evidence synthesis (computer friendly).
        Type `str`. """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ What outcome?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.population = None
        """ What population?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.resultsByExposure = None
        """ What was the result per exposure?.
        List of `EffectEvidenceSynthesisResultsByExposure` items (represented as `dict` in JSON). """
        
        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.sampleSize = None
        """ What sample size was involved?.
        Type `EffectEvidenceSynthesisSampleSize` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.studyType = None
        """ Type of study.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.synthesisType = None
        """ Type of synthesis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.title = None
        """ Name for this effect evidence synthesis (human friendly).
        Type `str`. """
        
        self.topic = None
        """ The category of the EffectEvidenceSynthesis, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Canonical identifier for this effect evidence synthesis,
        represented as a URI (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the effect evidence synthesis.
        Type `str`. """
        
        super(EffectEvidenceSynthesis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesis, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("certainty", "certainty", EffectEvidenceSynthesisCertainty, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectEstimate", "effectEstimate", EffectEvidenceSynthesisEffectEstimate, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("exposure", "exposure", fhirreference.FHIRReference, False, None, True),
            ("exposureAlternative", "exposureAlternative", fhirreference.FHIRReference, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", fhirreference.FHIRReference, False, None, True),
            ("population", "population", fhirreference.FHIRReference, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("resultsByExposure", "resultsByExposure", EffectEvidenceSynthesisResultsByExposure, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("sampleSize", "sampleSize", EffectEvidenceSynthesisSampleSize, False, None, False),
            ("status", "status", str, False, None, True),
            ("studyType", "studyType", codeableconcept.CodeableConcept, False, None, False),
            ("synthesisType", "synthesisType", codeableconcept.CodeableConcept, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
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
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.rating = None
        """ Certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EffectEvidenceSynthesisCertainty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisCertainty, self).elementProperties()
        js.extend([
            ("certaintySubcomponent", "certaintySubcomponent", EffectEvidenceSynthesisCertaintyCertaintySubcomponent, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
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
        
        self.rating = None
        """ Subcomponent certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of subcomponent of certainty rating.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EffectEvidenceSynthesisCertaintyCertaintySubcomponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("note", "note", annotation.Annotation, True, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.precisionEstimate = None
        """ How precise the estimate is.
        List of `EffectEvidenceSynthesisEffectEstimatePrecisionEstimate` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of efffect estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unitOfMeasure = None
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ Point estimate.
        Type `float`. """
        
        self.variantState = None
        """ Variant exposure states.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EffectEvidenceSynthesisEffectEstimate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisEffectEstimate, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("precisionEstimate", "precisionEstimate", EffectEvidenceSynthesisEffectEstimatePrecisionEstimate, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
            ("variantState", "variantState", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.level = None
        """ Level of confidence interval.
        Type `float`. """
        
        self.to = None
        """ Upper bound.
        Type `float`. """
        
        self.type = None
        """ Type of precision estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EffectEvidenceSynthesisEffectEstimatePrecisionEstimate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisEffectEstimatePrecisionEstimate, self).elementProperties()
        js.extend([
            ("from_fhir", "from", float, False, None, False),
            ("level", "level", float, False, None, False),
            ("to", "to", float, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.exposureState = None
        """ exposure | exposure-alternative.
        Type `str`. """
        
        self.riskEvidenceSynthesis = None
        """ Risk evidence synthesis.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.variantState = None
        """ Variant exposure states.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EffectEvidenceSynthesisResultsByExposure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisResultsByExposure, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("exposureState", "exposureState", str, False, None, False),
            ("riskEvidenceSynthesis", "riskEvidenceSynthesis", fhirreference.FHIRReference, False, None, True),
            ("variantState", "variantState", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.numberOfParticipants = None
        """ How many participants?.
        Type `int`. """
        
        self.numberOfStudies = None
        """ How many studies?.
        Type `int`. """
        
        super(EffectEvidenceSynthesisSampleSize, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EffectEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
        ])
        return js


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
