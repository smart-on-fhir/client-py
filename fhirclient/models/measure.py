#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/Measure) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class Measure(domainresource.DomainResource):
    """ A quality measure.
    
    The Measure resource provides the definition of a quality measure.
    """
    
    resource_name = "Measure"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.clinicalRecommendationStatement = None
        """ None.
        Type `str`. """
        
        self.definition = None
        """ None.
        Type `str`. """
        
        self.disclaimer = None
        """ None.
        Type `str`. """
        
        self.group = None
        """ None.
        List of `MeasureGroup` items (represented as `dict` in JSON). """
        
        self.guidance = None
        """ None.
        Type `str`. """
        
        self.improvementNotation = None
        """ None.
        Type `str`. """
        
        self.library = None
        """ Logic used by the measure.
        List of `FHIRReference` items referencing `Library` (represented as `dict` in JSON). """
        
        self.moduleMetadata = None
        """ Metadata for the measure.
        Type `ModuleMetadata` (represented as `dict` in JSON). """
        
        self.rateAggregation = None
        """ None.
        Type `str`. """
        
        self.rationale = None
        """ None.
        Type `str`. """
        
        self.riskAdjustment = None
        """ None.
        Type `str`. """
        
        self.scoring = None
        """ proportion | ratio | continuous-variable | cohort.
        Type `str`. """
        
        self.set = None
        """ None.
        Type `str`. """
        
        self.supplementalData = None
        """ Supplemental data.
        List of `MeasureSupplementalData` items (represented as `dict` in JSON). """
        
        self.type = None
        """ process | outcome.
        List of `str` items. """
        
        super(Measure, self).__init__(jsondict)
    
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
    """ None.
    
    A group of population criteria for the measure.
    """
    
    resource_name = "MeasureGroup"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ None.
        Type `str`. """
        
        self.identifier = None
        """ None.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.name = None
        """ None.
        Type `str`. """
        
        self.population = None
        """ None.
        List of `MeasureGroupPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ None.
        List of `MeasureGroupStratifier` items (represented as `dict` in JSON). """
        
        super(MeasureGroup, self).__init__(jsondict)
    
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
    """ None.
    
    A population criteria for the measure.
    """
    
    resource_name = "MeasureGroupPopulation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.criteria = None
        """ None.
        Type `str`. """
        
        self.description = None
        """ None.
        Type `str`. """
        
        self.identifier = None
        """ None.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.name = None
        """ None.
        Type `str`. """
        
        self.type = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-score.
        Type `str`. """
        
        super(MeasureGroupPopulation, self).__init__(jsondict)
    
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
    """ None.
    
    The stratifier criteria for the measure report, specified as either the
    name of a valid referenced CQL expression or a valid FHIR Resource Path.
    """
    
    resource_name = "MeasureGroupStratifier"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.criteria = None
        """ None.
        Type `str`. """
        
        self.identifier = None
        """ None.
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(MeasureGroupStratifier, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureGroupStratifier, self).elementProperties()
        js.extend([
            ("criteria", "criteria", str, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
        ])
        return js


class MeasureSupplementalData(backboneelement.BackboneElement):
    """ Supplemental data.
    
    Supplemental data to be supplied with the measure report.
    """
    
    resource_name = "MeasureSupplementalData"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Identifier, unique within the measure.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.path = None
        """ Path to the supplemental data element.
        Type `str`. """
        
        super(MeasureSupplementalData, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureSupplementalData, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


from . import fhirreference
from . import identifier
from . import modulemetadata
