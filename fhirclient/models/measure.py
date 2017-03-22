#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Measure) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Measure(domainresource.DomainResource):
    """ A quality measure definition.
    
    The Measure resource provides the definition of a quality measure.
    """
    
    resource_type = "Measure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ When the measure was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.clinicalRecommendationStatement = None
        """ Summary of clinical guidelines.
        Type `str`. """
        
        self.compositeScoring = None
        """ opportunity | all-or-nothing | linear | weighted.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.contributor = None
        """ A content contributor.
        List of `Contributor` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.definition = None
        """ Defined terms used in the measure documentation.
        List of `str` items. """
        
        self.description = None
        """ Natural language description of the measure.
        Type `str`. """
        
        self.disclaimer = None
        """ Disclaimer for use of the measure or its referenced content.
        Type `str`. """
        
        self.effectivePeriod = None
        """ When the measure is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.group = None
        """ Population criteria group.
        List of `MeasureGroup` items (represented as `dict` in JSON). """
        
        self.guidance = None
        """ Additional guidance for implementers.
        Type `str`. """
        
        self.identifier = None
        """ Additional identifier for the measure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.improvementNotation = None
        """ Improvement notation for the measure, e.g. higher score indicates
        better quality.
        Type `str`. """
        
        self.jurisdiction = None
        """ Intended jurisdiction for measure (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ When the measure was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.library = None
        """ Logic used by the measure.
        List of `FHIRReference` items referencing `Library` (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this measure (computer friendly).
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Why this measure is defined.
        Type `str`. """
        
        self.rateAggregation = None
        """ How is rate aggregation performed for this measure.
        Type `str`. """
        
        self.rationale = None
        """ Why does this measure exist.
        Type `str`. """
        
        self.relatedArtifact = None
        """ Additional documentation, citations, etc.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.riskAdjustment = None
        """ How is risk adjustment applied for this measure.
        Type `str`. """
        
        self.scoring = None
        """ proportion | ratio | continuous-variable | cohort.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.set = None
        """ The measure set, e.g. Preventive Care and Screening.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.supplementalData = None
        """ What other data should be reported with the measure.
        List of `MeasureSupplementalData` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Name for this measure (human friendly).
        Type `str`. """
        
        self.topic = None
        """ E.g. Education, Treatment, Assessment, etc.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ process | outcome | structure | patient-reported-outcome |
        composite.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Logical URI to reference this measure (globally unique).
        Type `str`. """
        
        self.usage = None
        """ Describes the clinical usage of the measure.
        Type `str`. """
        
        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the measure.
        Type `str`. """
        
        super(Measure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Measure, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("clinicalRecommendationStatement", "clinicalRecommendationStatement", str, False, None, False),
            ("compositeScoring", "compositeScoring", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("contributor", "contributor", contributor.Contributor, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("definition", "definition", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("disclaimer", "disclaimer", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", MeasureGroup, True, None, False),
            ("guidance", "guidance", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("improvementNotation", "improvementNotation", str, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("rateAggregation", "rateAggregation", str, False, None, False),
            ("rationale", "rationale", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("riskAdjustment", "riskAdjustment", str, False, None, False),
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False),
            ("set", "set", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("supplementalData", "supplementalData", MeasureSupplementalData, True, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class MeasureGroup(backboneelement.BackboneElement):
    """ Population criteria group.
    
    A group of population criteria for the measure.
    """
    
    resource_type = "MeasureGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Summary description.
        Type `str`. """
        
        self.identifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.name = None
        """ Short name.
        Type `str`. """
        
        self.population = None
        """ Population criteria.
        List of `MeasureGroupPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ Stratifier criteria for the measure.
        List of `MeasureGroupStratifier` items (represented as `dict` in JSON). """
        
        super(MeasureGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroup, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("name", "name", str, False, None, False),
            ("population", "population", MeasureGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureGroupStratifier, True, None, False),
        ])
        return js


class MeasureGroupPopulation(backboneelement.BackboneElement):
    """ Population criteria.
    
    A population criteria for the measure.
    """
    
    resource_type = "MeasureGroupPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criteria = None
        """ The name of a valid referenced CQL expression (may be namespaced)
        that defines this population criteria.
        Type `str`. """
        
        self.description = None
        """ The human readable description of this population criteria.
        Type `str`. """
        
        self.identifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.name = None
        """ Short name.
        Type `str`. """
        
        super(MeasureGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("name", "name", str, False, None, False),
        ])
        return js


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """ Stratifier criteria for the measure.
    
    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library, or a
    valid FHIR Resource Path.
    """
    
    resource_type = "MeasureGroupStratifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.criteria = None
        """ How the measure should be stratified.
        Type `str`. """
        
        self.identifier = None
        """ The identifier for the stratifier used to coordinate the reported
        data back to this stratifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.path = None
        """ Path to the stratifier.
        Type `str`. """
        
        super(MeasureGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupStratifier, self).elementProperties()
        js.extend([
            ("criteria", "criteria", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("path", "path", str, False, None, False),
        ])
        return js


class MeasureSupplementalData(backboneelement.BackboneElement):
    """ What other data should be reported with the measure.
    
    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """
    
    resource_type = "MeasureSupplementalData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.criteria = None
        """ Expression describing additional data to be reported.
        Type `str`. """
        
        self.identifier = None
        """ Identifier, unique within the measure.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.path = None
        """ Path to the supplemental data element.
        Type `str`. """
        
        self.usage = None
        """ supplemental-data | risk-adjustment-factor.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(MeasureSupplementalData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureSupplementalData, self).elementProperties()
        js.extend([
            ("criteria", "criteria", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("path", "path", str, False, None, False),
            ("usage", "usage", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import contributor
except ImportError:
    contributor = sys.modules[__package__ + '.contributor']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
