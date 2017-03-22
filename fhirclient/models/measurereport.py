#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/MeasureReport) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class MeasureReport(domainresource.DomainResource):
    """ Results of a measure evaluation.
    
    The MeasureReport resource contains the results of evaluating a measure.
    """
    
    resource_type = "MeasureReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the report was generated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.evaluatedResources = None
        """ What data was evaluated to produce the measure score.
        Type `FHIRReference` referencing `Bundle` (represented as `dict` in JSON). """
        
        self.group = None
        """ Measure results for each group.
        List of `MeasureReportGroup` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the Report.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.measure = None
        """ What measure was evaluated.
        Type `FHIRReference` referencing `Measure` (represented as `dict` in JSON). """
        
        self.patient = None
        """ What patient the report is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ What period the report covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.reportingOrganization = None
        """ Who is reporting the data.
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
            ("identifier", "identifier", identifier.Identifier, False, None, False),
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
    
    resource_type = "MeasureReportGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ What group of the measure.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.measureScore = None
        """ What score this group achieved.
        Type `float`. """
        
        self.population = None
        """ The populations in the group.
        List of `MeasureReportGroupPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ Stratification results.
        List of `MeasureReportGroupStratifier` items (represented as `dict` in JSON). """
        
        super(MeasureReportGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroup, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("measureScore", "measureScore", float, False, None, False),
            ("population", "population", MeasureReportGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureReportGroupStratifier, True, None, False),
        ])
        return js


class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    """ The populations in the group.
    
    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """
    
    resource_type = "MeasureReportGroupPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-score.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.count = None
        """ Size of the population.
        Type `int`. """
        
        self.identifier = None
        """ Population identifier as defined in the measure.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patients = None
        """ For patient-list reports, the patients in this population.
        Type `FHIRReference` referencing `List` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("patients", "patients", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """ Stratification results.
    
    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """
    
    resource_type = "MeasureReportGroupStratifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ What stratifier of the group.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.stratum = None
        """ Stratum results, one for each unique value in the stratifier.
        List of `MeasureReportGroupStratifierStratum` items (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifier, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("stratum", "stratum", MeasureReportGroupStratifierStratum, True, None, False),
        ])
        return js


class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """ Stratum results, one for each unique value in the stratifier.
    
    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """
    
    resource_type = "MeasureReportGroupStratifierStratum"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.measureScore = None
        """ What score this stratum achieved.
        Type `float`. """
        
        self.population = None
        """ Population results in this stratum.
        List of `MeasureReportGroupStratifierStratumPopulation` items (represented as `dict` in JSON). """
        
        self.value = None
        """ The stratum value, e.g. male.
        Type `str`. """
        
        super(MeasureReportGroupStratifierStratum, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratum, self).elementProperties()
        js.extend([
            ("measureScore", "measureScore", float, False, None, False),
            ("population", "population", MeasureReportGroupStratifierStratumPopulation, True, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    """ Population results in this stratum.
    
    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """
    
    resource_type = "MeasureReportGroupStratifierStratumPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-score.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.count = None
        """ Size of the population.
        Type `int`. """
        
        self.identifier = None
        """ Population identifier as defined in the measure.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patients = None
        """ For patient-list reports, the patients in this population.
        Type `FHIRReference` referencing `List` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifierStratumPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("patients", "patients", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
