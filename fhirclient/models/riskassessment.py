# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RiskAssessment).
# 2024, SMART Health IT.


from . import domainresource

class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.
    
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """
    
    resource_type = "RiskAssessment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ Request fulfilled by this assessment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.basis = None
        """ Information used in assessment.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basis = None
        """ Primitive extension for basis. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Type of assessment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ Condition assessed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Where was assessment performed?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Unique identifier for the assessment.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ Evaluation mechanism.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.mitigation = None
        """ How to reduce risk.
        Type `str`. """
        self._mitigation = None
        """ Primitive extension for mitigation. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments on the risk assessment.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceDateTime = None
        """ When was assessment made?.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._occurrenceDateTime = None
        """ Primitive extension for occurrenceDateTime. Type `FHIRPrimitiveExtension` """
        
        self.occurrencePeriod = None
        """ When was assessment made?.
        Type `Period` (represented as `dict` in JSON). """
        self._occurrencePeriod = None
        """ Primitive extension for occurrencePeriod. Type `FHIRPrimitiveExtension` """
        
        self.parent = None
        """ Part of this occurrence.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._parent = None
        """ Primitive extension for parent. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Who did assessment?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.prediction = None
        """ Outcome predicted.
        List of `RiskAssessmentPrediction` items (represented as `dict` in JSON). """
        self._prediction = None
        """ Primitive extension for prediction. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why the assessment was necessary?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why the assessment was necessary?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ registered | preliminary | final | amended +.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who/what does assessment apply to?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        super(RiskAssessment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskAssessment, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, False, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basis", "basis", fhirreference.FHIRReference, True, None, False),
            ("_basis", "_basis", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("condition", "condition", fhirreference.FHIRReference, False, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mitigation", "mitigation", str, False, None, False),
            ("_mitigation", "_mitigation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", False),
            ("_occurrenceDateTime", "_occurrenceDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("_occurrencePeriod", "_occurrencePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("_parent", "_parent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prediction", "prediction", RiskAssessmentPrediction, True, None, False),
            ("_prediction", "_prediction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ Outcome predicted.
    
    Describes the expected outcome for the subject.
    """
    
    resource_type = "RiskAssessmentPrediction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.outcome = None
        """ Possible outcome for the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.probabilityDecimal = None
        """ Likelihood of specified outcome.
        Type `float`. """
        self._probabilityDecimal = None
        """ Primitive extension for probabilityDecimal. Type `FHIRPrimitiveExtension` """
        
        self.probabilityRange = None
        """ Likelihood of specified outcome.
        Type `Range` (represented as `dict` in JSON). """
        self._probabilityRange = None
        """ Primitive extension for probabilityRange. Type `FHIRPrimitiveExtension` """
        
        self.qualitativeRisk = None
        """ Likelihood of specified outcome as a qualitative value.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._qualitativeRisk = None
        """ Primitive extension for qualitativeRisk. Type `FHIRPrimitiveExtension` """
        
        self.rationale = None
        """ Explanation of prediction.
        Type `str`. """
        self._rationale = None
        """ Primitive extension for rationale. Type `FHIRPrimitiveExtension` """
        
        self.relativeRisk = None
        """ Relative likelihood.
        Type `float`. """
        self._relativeRisk = None
        """ Primitive extension for relativeRisk. Type `FHIRPrimitiveExtension` """
        
        self.whenPeriod = None
        """ Timeframe or age range.
        Type `Period` (represented as `dict` in JSON). """
        self._whenPeriod = None
        """ Primitive extension for whenPeriod. Type `FHIRPrimitiveExtension` """
        
        self.whenRange = None
        """ Timeframe or age range.
        Type `Range` (represented as `dict` in JSON). """
        self._whenRange = None
        """ Primitive extension for whenRange. Type `FHIRPrimitiveExtension` """
        
        super(RiskAssessmentPrediction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskAssessmentPrediction, self).elementProperties()
        js.extend([
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("probabilityDecimal", "probabilityDecimal", float, False, "probability", False),
            ("_probabilityDecimal", "_probabilityDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("probabilityRange", "probabilityRange", range.Range, False, "probability", False),
            ("_probabilityRange", "_probabilityRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("qualitativeRisk", "qualitativeRisk", codeableconcept.CodeableConcept, False, None, False),
            ("_qualitativeRisk", "_qualitativeRisk", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rationale", "rationale", str, False, None, False),
            ("_rationale", "_rationale", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relativeRisk", "relativeRisk", float, False, None, False),
            ("_relativeRisk", "_relativeRisk", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("whenPeriod", "whenPeriod", period.Period, False, "when", False),
            ("_whenPeriod", "_whenPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("whenRange", "whenRange", range.Range, False, "when", False),
            ("_whenRange", "_whenRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import range