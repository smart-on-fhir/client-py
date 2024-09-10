# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AdverseEvent).
# 2024, SMART Health IT.


from . import domainresource

class AdverseEvent(domainresource.DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.
    
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """
    
    resource_type = "AdverseEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actuality = None
        """ actual | potential.
        Type `str`. """
        self._actuality = None
        """ Primitive extension for actuality. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ product-problem | product-quality | product-use-error | wrong-dose
        | incorrect-prescribing-information | wrong-technique | wrong-
        route-of-administration | wrong-rate | wrong-duration | wrong-time
        | expired-drug | medical-device-use-error | problem-different-
        manufacturer | unsafe-physical-environment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.contributor = None
        """ Who  was involved in the adverse event or the potential adverse
        event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._contributor = None
        """ Primitive extension for contributor. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ When the event occurred.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.detected = None
        """ When the event was detected.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._detected = None
        """ Primitive extension for detected. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.event = None
        """ Type of the event itself in relation to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._event = None
        """ Primitive extension for event. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier for the event.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Location where adverse event occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ resolved | recovering | ongoing | resolvedWithSequelae | fatal |
        unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.recordedDate = None
        """ When the event was recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._recordedDate = None
        """ Primitive extension for recordedDate. Type `FHIRPrimitiveExtension` """
        
        self.recorder = None
        """ Who recorded the adverse event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._recorder = None
        """ Primitive extension for recorder. Type `FHIRPrimitiveExtension` """
        
        self.referenceDocument = None
        """ AdverseEvent.referenceDocument.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._referenceDocument = None
        """ Primitive extension for referenceDocument. Type `FHIRPrimitiveExtension` """
        
        self.resultingCondition = None
        """ Effect on the subject due to this event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._resultingCondition = None
        """ Primitive extension for resultingCondition. Type `FHIRPrimitiveExtension` """
        
        self.seriousness = None
        """ Seriousness of the event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._seriousness = None
        """ Primitive extension for seriousness. Type `FHIRPrimitiveExtension` """
        
        self.severity = None
        """ mild | moderate | severe.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._severity = None
        """ Primitive extension for severity. Type `FHIRPrimitiveExtension` """
        
        self.study = None
        """ AdverseEvent.study.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._study = None
        """ Primitive extension for study. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Subject impacted by event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.subjectMedicalHistory = None
        """ AdverseEvent.subjectMedicalHistory.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._subjectMedicalHistory = None
        """ Primitive extension for subjectMedicalHistory. Type `FHIRPrimitiveExtension` """
        
        self.suspectEntity = None
        """ The suspected agent causing the adverse event.
        List of `AdverseEventSuspectEntity` items (represented as `dict` in JSON). """
        self._suspectEntity = None
        """ Primitive extension for suspectEntity. Type `FHIRPrimitiveExtension` """
        
        super(AdverseEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AdverseEvent, self).elementProperties()
        js.extend([
            ("actuality", "actuality", str, False, None, True),
            ("_actuality", "_actuality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contributor", "contributor", fhirreference.FHIRReference, True, None, False),
            ("_contributor", "_contributor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detected", "detected", fhirdatetime.FHIRDateTime, False, None, False),
            ("_detected", "_detected", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("event", "event", codeableconcept.CodeableConcept, False, None, False),
            ("_event", "_event", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recordedDate", "recordedDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_recordedDate", "_recordedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("_recorder", "_recorder", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceDocument", "referenceDocument", fhirreference.FHIRReference, True, None, False),
            ("_referenceDocument", "_referenceDocument", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resultingCondition", "resultingCondition", fhirreference.FHIRReference, True, None, False),
            ("_resultingCondition", "_resultingCondition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("seriousness", "seriousness", codeableconcept.CodeableConcept, False, None, False),
            ("_seriousness", "_seriousness", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("_severity", "_severity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("study", "study", fhirreference.FHIRReference, True, None, False),
            ("_study", "_study", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectMedicalHistory", "subjectMedicalHistory", fhirreference.FHIRReference, True, None, False),
            ("_subjectMedicalHistory", "_subjectMedicalHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("suspectEntity", "suspectEntity", AdverseEventSuspectEntity, True, None, False),
            ("_suspectEntity", "_suspectEntity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """ The suspected agent causing the adverse event.
    
    Describes the entity that is suspected to have caused the adverse event.
    """
    
    resource_type = "AdverseEventSuspectEntity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.causality = None
        """ Information on the possible cause of the event.
        List of `AdverseEventSuspectEntityCausality` items (represented as `dict` in JSON). """
        self._causality = None
        """ Primitive extension for causality. Type `FHIRPrimitiveExtension` """
        
        self.instance = None
        """ Refers to the specific entity that caused the adverse event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._instance = None
        """ Primitive extension for instance. Type `FHIRPrimitiveExtension` """
        
        super(AdverseEventSuspectEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend([
            ("causality", "causality", AdverseEventSuspectEntityCausality, True, None, False),
            ("_causality", "_causality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instance", "instance", fhirreference.FHIRReference, False, None, True),
            ("_instance", "_instance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    """ Information on the possible cause of the event.
    """
    
    resource_type = "AdverseEventSuspectEntityCausality"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assessment = None
        """ Assessment of if the entity caused the event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._assessment = None
        """ Primitive extension for assessment. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ AdverseEvent.suspectEntity.causalityAuthor.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ ProbabilityScale | Bayesian | Checklist.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.productRelatedness = None
        """ AdverseEvent.suspectEntity.causalityProductRelatedness.
        Type `str`. """
        self._productRelatedness = None
        """ Primitive extension for productRelatedness. Type `FHIRPrimitiveExtension` """
        
        super(AdverseEventSuspectEntityCausality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AdverseEventSuspectEntityCausality, self).elementProperties()
        js.extend([
            ("assessment", "assessment", codeableconcept.CodeableConcept, False, None, False),
            ("_assessment", "_assessment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productRelatedness", "productRelatedness", str, False, None, False),
            ("_productRelatedness", "_productRelatedness", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier