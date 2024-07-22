# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition).
# 2024, SMART Health IT.


from . import domainresource

class ResearchElementDefinition(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.
    
    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """
    
    resource_type = "ResearchElementDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ When the research element definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.characteristic = None
        """ What defines the members of the research element.
        List of `ResearchElementDefinitionCharacteristic` items (represented as `dict` in JSON). """
        
        self.comment = None
        """ Used for footnotes or explanatory notes.
        List of `str` items. """
        
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
        """ Natural language description of the research element definition.
        Type `str`. """
        
        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        """ When the research element definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Additional identifier for the research element definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for research element definition (if
        applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ When the research element definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.library = None
        """ Logic used by the ResearchElementDefinition.
        List of `str` items. """
        
        self.name = None
        """ Name for this research element definition (computer friendly).
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Why this research element definition is defined.
        Type `str`. """
        
        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.shortTitle = None
        """ Title for use in informal contexts.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.subjectCodeableConcept = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subtitle = None
        """ Subordinate title of the ResearchElementDefinition.
        Type `str`. """
        
        self.title = None
        """ Name for this research element definition (human friendly).
        Type `str`. """
        
        self.topic = None
        """ The category of the ResearchElementDefinition, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ population | exposure | outcome.
        Type `str`. """
        
        self.url = None
        """ Canonical identifier for this research element definition,
        represented as a URI (globally unique).
        Type `str`. """
        
        self.usage = None
        """ Describes the clinical usage of the ResearchElementDefinition.
        Type `str`. """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.variableType = None
        """ dichotomous | continuous | descriptive.
        Type `str`. """
        
        self.version = None
        """ Business version of the research element definition.
        Type `str`. """
        
        super(ResearchElementDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchElementDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("characteristic", "characteristic", ResearchElementDefinitionCharacteristic, True, None, True),
            ("comment", "comment", str, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("variableType", "variableType", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the research element.
    
    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """
    
    resource_type = "ResearchElementDefinitionCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definitionCanonical = None
        """ What code or expression defines members?.
        Type `str`. """
        
        self.definitionCodeableConcept = None
        """ What code or expression defines members?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definitionDataRequirement = None
        """ What code or expression defines members?.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.definitionExpression = None
        """ What code or expression defines members?.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.exclude = None
        """ Whether the characteristic includes or excludes members.
        Type `bool`. """
        
        self.participantEffectiveDateTime = None
        """ What time period do participants cover.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.participantEffectiveDescription = None
        """ What time period do participants cover.
        Type `str`. """
        
        self.participantEffectiveDuration = None
        """ What time period do participants cover.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.participantEffectiveGroupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """
        
        self.participantEffectivePeriod = None
        """ What time period do participants cover.
        Type `Period` (represented as `dict` in JSON). """
        
        self.participantEffectiveTimeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.participantEffectiveTiming = None
        """ What time period do participants cover.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.studyEffectiveDateTime = None
        """ What time period does the study cover.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.studyEffectiveDescription = None
        """ What time period does the study cover.
        Type `str`. """
        
        self.studyEffectiveDuration = None
        """ What time period does the study cover.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.studyEffectiveGroupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """
        
        self.studyEffectivePeriod = None
        """ What time period does the study cover.
        Type `Period` (represented as `dict` in JSON). """
        
        self.studyEffectiveTimeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.studyEffectiveTiming = None
        """ What time period does the study cover.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.unitOfMeasure = None
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.usageContext = None
        """ What code/value pairs define members?.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        super(ResearchElementDefinitionCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchElementDefinitionCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, False, "definition", True),
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True),
            ("exclude", "exclude", bool, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdatetime.FHIRDateTime, False, "participantEffective", False),
            ("participantEffectiveDescription", "participantEffectiveDescription", str, False, None, False),
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, False, "participantEffective", False),
            ("participantEffectiveGroupMeasure", "participantEffectiveGroupMeasure", str, False, None, False),
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, False, "participantEffective", False),
            ("participantEffectiveTimeFromStart", "participantEffectiveTimeFromStart", duration.Duration, False, None, False),
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, False, "participantEffective", False),
            ("studyEffectiveDateTime", "studyEffectiveDateTime", fhirdatetime.FHIRDateTime, False, "studyEffective", False),
            ("studyEffectiveDescription", "studyEffectiveDescription", str, False, None, False),
            ("studyEffectiveDuration", "studyEffectiveDuration", duration.Duration, False, "studyEffective", False),
            ("studyEffectiveGroupMeasure", "studyEffectiveGroupMeasure", str, False, None, False),
            ("studyEffectivePeriod", "studyEffectivePeriod", period.Period, False, "studyEffective", False),
            ("studyEffectiveTimeFromStart", "studyEffectiveTimeFromStart", duration.Duration, False, None, False),
            ("studyEffectiveTiming", "studyEffectiveTiming", timing.Timing, False, "studyEffective", False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("usageContext", "usageContext", usagecontext.UsageContext, True, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import datarequirement
from . import duration
from . import expression
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import relatedartifact
from . import timing
from . import usagecontext
