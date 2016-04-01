#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/Measure) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class Measure(domainresource.DomainResource):
    """ A quality measure.
    
    The Measure resource provides the definition of a quality measure.
    """
    
    resource_name = "Measure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.clinicalRecommendationStatement = None
        """ Clinical recommendation.
        Type `str`. """
        
        self.definition = None
        """ A natural language definition of the measure.
        Type `str`. """
        
        self.disclaimer = None
        """ Disclaimer for the measure.
        Type `str`. """
        
        self.group = None
        """ Population criteria group.
        List of `MeasureGroup` items (represented as `dict` in JSON). """
        
        self.guidance = None
        """ The guidance for the measure.
        Type `str`. """
        
        self.improvementNotation = None
        """ Improvement notation for the measure, e.g. higher score indicates
        better quality.
        Type `str`. """
        
        self.library = None
        """ Logic used by the measure.
        List of `FHIRReference` items referencing `Library` (represented as `dict` in JSON). """
        
        self.moduleMetadata = None
        """ Metadata for the measure.
        Type `ModuleMetadata` (represented as `dict` in JSON). """
        
        self.rateAggregation = None
        """ How is rate aggregation performed for this measure.
        Type `str`. """
        
        self.rationale = None
        """ Why does this measure exist.
        Type `str`. """
        
        self.riskAdjustment = None
        """ How is risk adjustment applied for this measure.
        Type `str`. """
        
        self.scoring = None
        """ proportion | ratio | continuous-variable | cohort.
        Type `str`. """
        
        self.set = None
        """ The measure set, e.g. Preventive Care and Screening.
        Type `str`. """
        
        self.supplementalData = None
        """ Supplemental data.
        List of `MeasureSupplementalData` items (represented as `dict` in JSON). """
        
        self.type = None
        """ process | outcome.
        List of `str` items. """
        
        super(Measure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Measure, self).elementProperties()
        js.extend([
            ("clinicalRecommendationStatement", "clinicalRecommendationStatement", str, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("disclaimer", "disclaimer", str, False, None, False),
            ("group", "group", MeasureGroup, True, None, False),
            ("guidance", "guidance", str, False, None, False),
            ("improvementNotation", "improvementNotation", str, False, None, False),
            ("library", "library", fhirreference.FHIRReference, True, None, False),
            ("moduleMetadata", "moduleMetadata", modulemetadata.ModuleMetadata, False, None, False),
            ("rateAggregation", "rateAggregation", str, False, None, False),
            ("rationale", "rationale", str, False, None, False),
            ("riskAdjustment", "riskAdjustment", str, False, None, False),
            ("scoring", "scoring", str, False, None, False),
            ("set", "set", str, False, None, False),
            ("supplementalData", "supplementalData", MeasureSupplementalData, True, None, False),
            ("type", "type", str, True, None, False),
        ])
        return js


from . import backboneelement

class MeasureGroup(backboneelement.BackboneElement):
    """ Population criteria group.
    
    A group of population criteria for the measure.
    """
    
    resource_name = "MeasureGroup"
    
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
    
    resource_name = "MeasureGroupPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        self.type = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-score.
        Type `str`. """
        
        super(MeasureGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupPopulation, self).elementProperties()
        js.extend([
            ("criteria", "criteria", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("name", "name", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """ Stratifier criteria for the measure.
    
    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library, or a
    valid FHIR Resource Path.
    """
    
    resource_name = "MeasureGroupStratifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.criteria = None
        """ Stratifier criteria.
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
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("path", "path", str, False, None, False),
        ])
        return js


class MeasureSupplementalData(backboneelement.BackboneElement):
    """ Supplemental data.
    
    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """
    
    resource_name = "MeasureSupplementalData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.criteria = None
        """ Supplemental data criteria.
        Type `str`. """
        
        self.identifier = None
        """ Identifier, unique within the measure.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.path = None
        """ Path to the supplemental data element.
        Type `str`. """
        
        self.usage = None
        """ supplemental-data | risk-adjustment-factor.
        List of `str` items. """
        
        super(MeasureSupplementalData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureSupplementalData, self).elementProperties()
        js.extend([
            ("criteria", "criteria", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("path", "path", str, False, None, False),
            ("usage", "usage", str, True, None, False),
        ])
        return js


from . import fhirreference
from . import identifier
from . import modulemetadata
