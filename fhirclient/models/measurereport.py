# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MeasureReport).
# 2024, SMART Health IT.


from . import domainresource

class MeasureReport(domainresource.DomainResource):
    """ Results of a measure evaluation.
    
    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
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
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.evaluatedResource = None
        """ What data was used to calculate the measure score.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._evaluatedResource = None
        """ Primitive extension for evaluatedResource. Type `FHIRPrimitiveExtension` """
        
        self.group = None
        """ Measure results for each group.
        List of `MeasureReportGroup` items (represented as `dict` in JSON). """
        self._group = None
        """ Primitive extension for group. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the MeasureReport.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.improvementNotation = None
        """ increase | decrease.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._improvementNotation = None
        """ Primitive extension for improvementNotation. Type `FHIRPrimitiveExtension` """
        
        self.measure = None
        """ What measure was calculated.
        Type `str`. """
        self._measure = None
        """ Primitive extension for measure. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ What period the report covers.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.reporter = None
        """ Who is reporting the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._reporter = None
        """ Primitive extension for reporter. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ complete | pending | error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ What individual(s) the report is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ individual | subject-list | summary | data-collection.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MeasureReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReport, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("evaluatedResource", "evaluatedResource", fhirreference.FHIRReference, True, None, False),
            ("_evaluatedResource", "_evaluatedResource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("group", "group", MeasureReportGroup, True, None, False),
            ("_group", "_group", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("improvementNotation", "improvementNotation", codeableconcept.CodeableConcept, False, None, False),
            ("_improvementNotation", "_improvementNotation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("measure", "measure", str, False, None, True),
            ("_measure", "_measure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, True),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reporter", "reporter", fhirreference.FHIRReference, False, None, False),
            ("_reporter", "_reporter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        
        self.code = None
        """ Meaning of the group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.measureScore = None
        """ What score this group achieved.
        Type `Quantity` (represented as `dict` in JSON). """
        self._measureScore = None
        """ Primitive extension for measureScore. Type `FHIRPrimitiveExtension` """
        
        self.population = None
        """ The populations in the group.
        List of `MeasureReportGroupPopulation` items (represented as `dict` in JSON). """
        self._population = None
        """ Primitive extension for population. Type `FHIRPrimitiveExtension` """
        
        self.stratifier = None
        """ Stratification results.
        List of `MeasureReportGroupStratifier` items (represented as `dict` in JSON). """
        self._stratifier = None
        """ Primitive extension for stratifier. Type `FHIRPrimitiveExtension` """
        
        super(MeasureReportGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroup, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("measureScore", "measureScore", quantity.Quantity, False, None, False),
            ("_measureScore", "_measureScore", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("population", "population", MeasureReportGroupPopulation, True, None, False),
            ("_population", "_population", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("stratifier", "stratifier", MeasureReportGroupStratifier, True, None, False),
            ("_stratifier", "_stratifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        population | measure-population-exclusion | measure-observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.count = None
        """ Size of the population.
        Type `int`. """
        self._count = None
        """ Primitive extension for count. Type `FHIRPrimitiveExtension` """
        
        self.subjectResults = None
        """ For subject-list reports, the subject results in this population.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subjectResults = None
        """ Primitive extension for subjectResults. Type `FHIRPrimitiveExtension` """
        
        super(MeasureReportGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("count", "count", int, False, None, False),
            ("_count", "_count", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, False, None, False),
            ("_subjectResults", "_subjectResults", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        
        self.code = None
        """ What stratifier of the group.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.stratum = None
        """ Stratum results, one for each unique value, or set of values, in
        the stratifier, or stratifier components.
        List of `MeasureReportGroupStratifierStratum` items (represented as `dict` in JSON). """
        self._stratum = None
        """ Primitive extension for stratum. Type `FHIRPrimitiveExtension` """
        
        super(MeasureReportGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("stratum", "stratum", MeasureReportGroupStratifierStratum, True, None, False),
            ("_stratum", "_stratum", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """ Stratum results, one for each unique value, or set of values, in the
    stratifier, or stratifier components.
    
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
        
        self.component = None
        """ Stratifier component values.
        List of `MeasureReportGroupStratifierStratumComponent` items (represented as `dict` in JSON). """
        self._component = None
        """ Primitive extension for component. Type `FHIRPrimitiveExtension` """
        
        self.measureScore = None
        """ What score this stratum achieved.
        Type `Quantity` (represented as `dict` in JSON). """
        self._measureScore = None
        """ Primitive extension for measureScore. Type `FHIRPrimitiveExtension` """
        
        self.population = None
        """ Population results in this stratum.
        List of `MeasureReportGroupStratifierStratumPopulation` items (represented as `dict` in JSON). """
        self._population = None
        """ Primitive extension for population. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The stratum value, e.g. male.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(MeasureReportGroupStratifierStratum, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratum, self).elementProperties()
        js.extend([
            ("component", "component", MeasureReportGroupStratifierStratumComponent, True, None, False),
            ("_component", "_component", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("measureScore", "measureScore", quantity.Quantity, False, None, False),
            ("_measureScore", "_measureScore", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("population", "population", MeasureReportGroupStratifierStratumPopulation, True, None, False),
            ("_population", "_population", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", codeableconcept.CodeableConcept, False, None, False),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    """ Stratifier component values.
    
    A stratifier component value.
    """
    
    resource_type = "MeasureReportGroupStratifierStratumComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ What stratifier component of the group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The stratum component value, e.g. male.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(MeasureReportGroupStratifierStratumComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", codeableconcept.CodeableConcept, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        population | measure-population-exclusion | measure-observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.count = None
        """ Size of the population.
        Type `int`. """
        self._count = None
        """ Primitive extension for count. Type `FHIRPrimitiveExtension` """
        
        self.subjectResults = None
        """ For subject-list reports, the subject results in this population.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subjectResults = None
        """ Primitive extension for subjectResults. Type `FHIRPrimitiveExtension` """
        
        super(MeasureReportGroupStratifierStratumPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("count", "count", int, False, None, False),
            ("_count", "_count", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, False, None, False),
            ("_subjectResults", "_subjectResults", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity