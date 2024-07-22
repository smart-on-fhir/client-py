# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Evidence).
# 2024, SMART Health IT.


from . import domainresource

class Evidence(domainresource.DomainResource):
    """ A research context or question.
    
    The Evidence resource describes the conditional state (population and any
    exposures being compared within the population) and outcome (if specified)
    that the knowledge (evidence, assertion, recommendation) is about.
    """
    
    resource_type = "Evidence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ When the evidence was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
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
        """ Natural language description of the evidence.
        Type `str`. """
        
        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        """ When the evidence is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.exposureBackground = None
        """ What population?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.exposureVariant = None
        """ What exposure?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the evidence.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for evidence (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ When the evidence was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this evidence (computer friendly).
        Type `str`. """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ What outcome?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
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
        
        self.subtitle = None
        """ Subordinate title of the Evidence.
        Type `str`. """
        
        self.title = None
        """ Name for this evidence (human friendly).
        Type `str`. """
        
        self.topic = None
        """ The category of the Evidence, such as Education, Treatment,
        Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Canonical identifier for this evidence, represented as a URI
        (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the evidence.
        Type `str`. """
        
        super(Evidence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Evidence, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("exposureBackground", "exposureBackground", fhirreference.FHIRReference, False, None, True),
            ("exposureVariant", "exposureVariant", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", fhirreference.FHIRReference, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
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
