# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ResearchStudy).
# 2024, SMART Health IT.


from . import domainresource

class ResearchStudy(domainresource.DomainResource):
    """ Investigation to increase healthcare-related patient-independent knowledge.
    
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
    """
    
    resource_type = "ResearchStudy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.arm = None
        """ Defined path through the study for a subject.
        List of `ResearchStudyArm` items (represented as `dict` in JSON). """
        self._arm = None
        """ Primitive extension for arm. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Classifications for the study.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ Condition being studied.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the study.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ What this is study doing.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.enrollment = None
        """ Inclusion & exclusion criteria.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._enrollment = None
        """ Primitive extension for enrollment. Type `FHIRPrimitiveExtension` """
        
        self.focus = None
        """ Drugs, devices, etc. under study.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._focus = None
        """ Primitive extension for focus. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for study.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.keyword = None
        """ Used to search for the study.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._keyword = None
        """ Primitive extension for keyword. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Geographic region(s) for study.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments made about the study.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.objective = None
        """ A goal for the study.
        List of `ResearchStudyObjective` items (represented as `dict` in JSON). """
        self._objective = None
        """ Primitive extension for objective. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Part of larger study.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ When the study began and ended.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.phase = None
        """ n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 |
        phase-2-phase-3 | phase-3 | phase-4.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._phase = None
        """ Primitive extension for phase. Type `FHIRPrimitiveExtension` """
        
        self.primaryPurposeType = None
        """ treatment | prevention | diagnostic | supportive-care | screening |
        health-services-research | basic-science | device-feasibility.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._primaryPurposeType = None
        """ Primitive extension for primaryPurposeType. Type `FHIRPrimitiveExtension` """
        
        self.principalInvestigator = None
        """ Researcher who oversees multiple aspects of the study.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._principalInvestigator = None
        """ Primitive extension for principalInvestigator. Type `FHIRPrimitiveExtension` """
        
        self.protocol = None
        """ Steps followed in executing study.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._protocol = None
        """ Primitive extension for protocol. Type `FHIRPrimitiveExtension` """
        
        self.reasonStopped = None
        """ accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-
        study-progress | temporarily-closed-per-study-design.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._reasonStopped = None
        """ Primitive extension for reasonStopped. Type `FHIRPrimitiveExtension` """
        
        self.relatedArtifact = None
        """ References and dependencies.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        self._relatedArtifact = None
        """ Primitive extension for relatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.site = None
        """ Facility where study activities are conducted.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._site = None
        """ Primitive extension for site. Type `FHIRPrimitiveExtension` """
        
        self.sponsor = None
        """ Organization that initiates and is legally responsible for the
        study.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._sponsor = None
        """ Primitive extension for sponsor. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | administratively-completed | approved | closed-to-accrual
        | closed-to-accrual-and-intervention | completed | disapproved |
        in-review | temporarily-closed-to-accrual | temporarily-closed-to-
        accrual-and-intervention | withdrawn.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this study.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        super(ResearchStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchStudy, self).elementProperties()
        js.extend([
            ("arm", "arm", ResearchStudyArm, True, None, False),
            ("_arm", "_arm", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("condition", "condition", codeableconcept.CodeableConcept, True, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enrollment", "enrollment", fhirreference.FHIRReference, True, None, False),
            ("_enrollment", "_enrollment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focus", "focus", codeableconcept.CodeableConcept, True, None, False),
            ("_focus", "_focus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("keyword", "keyword", codeableconcept.CodeableConcept, True, None, False),
            ("_keyword", "_keyword", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", codeableconcept.CodeableConcept, True, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("objective", "objective", ResearchStudyObjective, True, None, False),
            ("_objective", "_objective", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("phase", "phase", codeableconcept.CodeableConcept, False, None, False),
            ("_phase", "_phase", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("primaryPurposeType", "primaryPurposeType", codeableconcept.CodeableConcept, False, None, False),
            ("_primaryPurposeType", "_primaryPurposeType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("principalInvestigator", "principalInvestigator", fhirreference.FHIRReference, False, None, False),
            ("_principalInvestigator", "_principalInvestigator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("protocol", "protocol", fhirreference.FHIRReference, True, None, False),
            ("_protocol", "_protocol", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonStopped", "reasonStopped", codeableconcept.CodeableConcept, False, None, False),
            ("_reasonStopped", "_reasonStopped", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("_relatedArtifact", "_relatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("site", "site", fhirreference.FHIRReference, True, None, False),
            ("_site", "_site", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sponsor", "sponsor", fhirreference.FHIRReference, False, None, False),
            ("_sponsor", "_sponsor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ResearchStudyArm(backboneelement.BackboneElement):
    """ Defined path through the study for a subject.
    
    Describes an expected sequence of events for one of the participants of a
    study.  E.g. Exposure to drug A, wash-out, exposure to drug B, wash-out,
    follow-up.
    """
    
    resource_type = "ResearchStudyArm"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Short explanation of study path.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Label for study arm.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Categorization of study arm.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ResearchStudyArm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchStudyArm, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ResearchStudyObjective(backboneelement.BackboneElement):
    """ A goal for the study.
    
    A goal that the study is aiming to achieve in terms of a scientific
    question to be answered by the analysis of data collected during the study.
    """
    
    resource_type = "ResearchStudyObjective"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Label for the objective.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ primary | secondary | exploratory.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ResearchStudyObjective, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchStudyObjective, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import contactdetail
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact