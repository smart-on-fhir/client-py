#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/MeasureReport) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class MeasureReport(domainresource.DomainResource):
    """ Results of a measure evaluation.
    
    The MeasureReport resource contains the results of evaluating a measure.
    """
    
    resource_name = "MeasureReport"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.evaluatedResources = None
        """ Evaluated Resources.
        Type `MeasureReportEvaluatedResources` (represented as `dict` in JSON). """
        
        self.measure = None
        """ Measure that was evaluated.
        Type `FHIRReference` referencing `Measure` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Optional Patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ Reporting period.
        Type `Period` (represented as `dict` in JSON). """
        
        self.populationReport = None
        """ Population Report.
        List of `MeasureReportPopulationReport` items (represented as `dict` in JSON). """
        
        self.reportingOrganization = None
        """ Reporting Organization.
        Type `str`. """
        
        self.status = None
        """ complete | pending | error.
        Type `str`. """
        
        self.type = None
        """ individual | patient-list | summary.
        Type `str`. """
        
        super(MeasureReport, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureReport, self).elementProperties()
        js.extend([
            ("evaluatedResources", "evaluatedResources", MeasureReportEvaluatedResources, False, None, False),
            ("measure", "measure", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("populationReport", "populationReport", MeasureReportPopulationReport, True, None, False),
            ("reportingOrganization", "reportingOrganization", str, False, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


from . import backboneelement

class MeasureReportEvaluatedResources(backboneelement.BackboneElement):
    """ Evaluated Resources.
    
    Resources used in the evaluation of this response.
    """
    
    resource_name = "MeasureReportEvaluatedResources"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.url = None
        """ Evaluated Resources URL.
        Type `str`. """
        
        self.value = None
        """ Evaluated Resources value.
        Type `str`. """
        
        super(MeasureReportEvaluatedResources, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureReportEvaluatedResources, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class MeasureReportPopulationReport(backboneelement.BackboneElement):
    """ Population Report.
    """
    
    resource_name = "MeasureReportPopulationReport"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Identifier of the population group being reported.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.measureScore = None
        """ The measure score.
        Type `float`. """
        
        self.population = None
        """ The populations in the group.
        List of `MeasureReportPopulationReportPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ Stratification results.
        List of `MeasureReportPopulationReportStratifier` items (represented as `dict` in JSON). """
        
        self.supplementalData = None
        """ Supplemental data elements for the measure.
        List of `MeasureReportPopulationReportSupplementalData` items (represented as `dict` in JSON). """
        
        super(MeasureReportPopulationReport, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureReportPopulationReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("measureScore", "measureScore", float, False, None, False),
            ("population", "population", MeasureReportPopulationReportPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureReportPopulationReportStratifier, True, None, False),
            ("supplementalData", "supplementalData", MeasureReportPopulationReportSupplementalData, True, None, False),
        ])
        return js


class MeasureReportPopulationReportPopulation(backboneelement.BackboneElement):
    """ The populations in the group.
    
    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """
    
    resource_name = "MeasureReportPopulationReportPopulation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.count = None
        """ Size of the population.
        Type `int`. """
        
        self.patients = None
        """ Bundle of MeasureResponse resources, one per patient.
        Type `FHIRReference` referencing `Bundle` (represented as `dict` in JSON). """
        
        self.type = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-score.
        Type `str`. """
        
        super(MeasureReportPopulationReportPopulation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureReportPopulationReportPopulation, self).elementProperties()
        js.extend([
            ("count", "count", int, False, None, False),
            ("patients", "patients", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class MeasureReportPopulationReportStratifier(backboneelement.BackboneElement):
    """ Stratification results.
    
    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """
    
    resource_name = "MeasureReportPopulationReportStratifier"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Identifier of the stratum.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.measureScore = None
        """ The measure score.
        Type `float`. """
        
        self.population = None
        """ The populations in the stratifier.
        List of `MeasureReportPopulationReportStratifierPopulation` items (represented as `dict` in JSON). """
        
        super(MeasureReportPopulationReportStratifier, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureReportPopulationReportStratifier, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("measureScore", "measureScore", float, False, None, False),
            ("population", "population", MeasureReportPopulationReportStratifierPopulation, True, None, False),
        ])
        return js


class MeasureReportPopulationReportStratifierPopulation(backboneelement.BackboneElement):
    """ The populations in the stratifier.
    
    The populations that make up the stratifier, one for each type of
    population appropriate to the measure.
    """
    
    resource_name = "MeasureReportPopulationReportStratifierPopulation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.count = None
        """ Size of the population.
        Type `int`. """
        
        self.patients = None
        """ Bundle of MeasureResponse resources, one per patient.
        Type `FHIRReference` referencing `Bundle` (represented as `dict` in JSON). """
        
        self.type = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-score.
        Type `str`. """
        
        super(MeasureReportPopulationReportStratifierPopulation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureReportPopulationReportStratifierPopulation, self).elementProperties()
        js.extend([
            ("count", "count", int, False, None, False),
            ("patients", "patients", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class MeasureReportPopulationReportSupplementalData(backboneelement.BackboneElement):
    """ Supplemental data elements for the measure.
    
    Supplemental data elements for the measure provide additional information
    requested by the measure for each patient involved in the populations.
    """
    
    resource_name = "MeasureReportPopulationReportSupplementalData"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.count = None
        """ Number of patients in the group.
        Type `int`. """
        
        self.identifier = None
        """ Identifier of the supplemental data element.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patients = None
        """ Bundle of patients.
        Type `FHIRReference` referencing `Bundle` (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ Supplemental data strata.
        List of `MeasureReportPopulationReportSupplementalDataStratifier` items (represented as `dict` in JSON). """
        
        super(MeasureReportPopulationReportSupplementalData, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureReportPopulationReportSupplementalData, self).elementProperties()
        js.extend([
            ("count", "count", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("patients", "patients", fhirreference.FHIRReference, False, None, False),
            ("stratifier", "stratifier", MeasureReportPopulationReportSupplementalDataStratifier, True, None, False),
        ])
        return js


class MeasureReportPopulationReportSupplementalDataStratifier(backboneelement.BackboneElement):
    """ Supplemental data strata.
    
    The supplemental data for a stratum of the measure.
    """
    
    resource_name = "MeasureReportPopulationReportSupplementalDataStratifier"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.count = None
        """ Size of the population in this stratum.
        Type `int`. """
        
        self.identifier = None
        """ Identifier of the stratum.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patients = None
        """ Bundle of MeasureResponse resources, one per patient.
        Type `FHIRReference` referencing `Bundle` (represented as `dict` in JSON). """
        
        super(MeasureReportPopulationReportSupplementalDataStratifier, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MeasureReportPopulationReportSupplementalDataStratifier, self).elementProperties()
        js.extend([
            ("count", "count", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("patients", "patients", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import fhirreference
from . import identifier
from . import period
