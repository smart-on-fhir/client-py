#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/MeasureReport) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class MeasureReport(domainresource.DomainResource):
    """ Results of a measure evaluation.
    
    The MeasureReport resource contains the results of evaluating a measure.
    """
    
    resource_name = "MeasureReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ Date the report was generated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.evaluatedResources = None
        """ Evaluated Resources.
        Type `FHIRReference` referencing `Bundle` (represented as `dict` in JSON). """
        
        self.group = None
        """ Measure results for each group.
        List of `MeasureReportGroup` items (represented as `dict` in JSON). """
        
        self.measure = None
        """ Measure that was evaluated.
        Type `FHIRReference` referencing `Measure` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Optional Patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ Reporting period.
        Type `Period` (represented as `dict` in JSON). """
        
        self.reportingOrganization = None
        """ Reporting Organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.status = None
        """ complete | pending | error.
        Type `str`. """
        
        self.type = None
        """ individual | patient-list | summary.
        Type `str`. """
        
        super(MeasureReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReport, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("evaluatedResources", "evaluatedResources", fhirreference.FHIRReference, False, None, False),
            ("group", "group", MeasureReportGroup, True, None, False),
            ("measure", "measure", fhirreference.FHIRReference, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, True),
            ("reportingOrganization", "reportingOrganization", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import backboneelement

class MeasureReportGroup(backboneelement.BackboneElement):
    """ Measure results for each group.
    
    The results of the calculation, one for each population group in the
    measure.
    """
    
    resource_name = "MeasureReportGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifier of the population group being reported.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.measureScore = None
        """ The measure score.
        Type `float`. """
        
        self.population = None
        """ The populations in the group.
        List of `MeasureReportGroupPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ Stratification results.
        List of `MeasureReportGroupStratifier` items (represented as `dict` in JSON). """
        
        self.supplementalData = None
        """ Supplemental data elements for the measure.
        List of `MeasureReportGroupSupplementalData` items (represented as `dict` in JSON). """
        
        super(MeasureReportGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroup, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("measureScore", "measureScore", float, False, None, False),
            ("population", "population", MeasureReportGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureReportGroupStratifier, True, None, False),
            ("supplementalData", "supplementalData", MeasureReportGroupSupplementalData, True, None, False),
        ])
        return js


class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    """ The populations in the group.
    
    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """
    
    resource_name = "MeasureReportGroupPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.count = None
        """ Size of the population.
        Type `int`. """
        
        self.patients = None
        """ For patient-list reports, the patients in this population.
        Type `FHIRReference` referencing `List` (represented as `dict` in JSON). """
        
        self.type = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-score.
        Type `str`. """
        
        super(MeasureReportGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupPopulation, self).elementProperties()
        js.extend([
            ("count", "count", int, False, None, False),
            ("patients", "patients", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """ Stratification results.
    
    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """
    
    resource_name = "MeasureReportGroupStratifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.group = None
        """ Stratum results, one for each unique value in the stratifier.
        List of `MeasureReportGroupStratifierGroup` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier of the stratifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifier, self).elementProperties()
        js.extend([
            ("group", "group", MeasureReportGroupStratifierGroup, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
        ])
        return js


class MeasureReportGroupStratifierGroup(backboneelement.BackboneElement):
    """ Stratum results, one for each unique value in the stratifier.
    
    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """
    
    resource_name = "MeasureReportGroupStratifierGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.measureScore = None
        """ The measure score.
        Type `float`. """
        
        self.population = None
        """ Population results in this stratum.
        List of `MeasureReportGroupStratifierGroupPopulation` items (represented as `dict` in JSON). """
        
        self.value = None
        """ The stratum value, e.g. male.
        Type `str`. """
        
        super(MeasureReportGroupStratifierGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierGroup, self).elementProperties()
        js.extend([
            ("measureScore", "measureScore", float, False, None, False),
            ("population", "population", MeasureReportGroupStratifierGroupPopulation, True, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


class MeasureReportGroupStratifierGroupPopulation(backboneelement.BackboneElement):
    """ Population results in this stratum.
    
    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """
    
    resource_name = "MeasureReportGroupStratifierGroupPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.count = None
        """ Size of the population.
        Type `int`. """
        
        self.patients = None
        """ For patient-list reports, the patients in this population.
        Type `FHIRReference` referencing `List` (represented as `dict` in JSON). """
        
        self.type = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-score.
        Type `str`. """
        
        super(MeasureReportGroupStratifierGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierGroupPopulation, self).elementProperties()
        js.extend([
            ("count", "count", int, False, None, False),
            ("patients", "patients", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class MeasureReportGroupSupplementalData(backboneelement.BackboneElement):
    """ Supplemental data elements for the measure.
    
    Supplemental data elements for the measure provide additional information
    requested by the measure for each patient involved in the populations.
    """
    
    resource_name = "MeasureReportGroupSupplementalData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.group = None
        """ Supplemental data results, one for each unique supplemental data
        value.
        List of `MeasureReportGroupSupplementalDataGroup` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier of the supplemental data element.
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupSupplementalData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupSupplementalData, self).elementProperties()
        js.extend([
            ("group", "group", MeasureReportGroupSupplementalDataGroup, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, True),
        ])
        return js


class MeasureReportGroupSupplementalDataGroup(backboneelement.BackboneElement):
    """ Supplemental data results, one for each unique supplemental data value.
    
    This element contains the results for a single value within the
    supplemental data. For example, when reporting supplemental data for
    administrative gender, there will be four groups, one for each possible
    gender value.
    """
    
    resource_name = "MeasureReportGroupSupplementalDataGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.count = None
        """ Number of members in the group.
        Type `int`. """
        
        self.patients = None
        """ For patient-list reports, the patients in this population.
        Type `FHIRReference` referencing `List` (represented as `dict` in JSON). """
        
        self.value = None
        """ The data value, e.g. male.
        Type `str`. """
        
        super(MeasureReportGroupSupplementalDataGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupSupplementalDataGroup, self).elementProperties()
        js.extend([
            ("count", "count", int, False, None, False),
            ("patients", "patients", fhirreference.FHIRReference, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
