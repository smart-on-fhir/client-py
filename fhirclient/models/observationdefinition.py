# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ObservationDefinition).
# 2024, SMART Health IT.


from . import domainresource

class ObservationDefinition(domainresource.DomainResource):
    """ Definition of an observation.
    
    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    
    resource_type = "ObservationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abnormalCodedValueSet = None
        """ Value set of abnormal coded values for the observations conforming
        to this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._abnormalCodedValueSet = None
        """ Primitive extension for abnormalCodedValueSet. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Category of observation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.criticalCodedValueSet = None
        """ Value set of critical coded values for the observations conforming
        to this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._criticalCodedValueSet = None
        """ Primitive extension for criticalCodedValueSet. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier for this ObservationDefinition instance.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ Method used to produce the observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.multipleResultsAllowed = None
        """ Multiple results allowed.
        Type `bool`. """
        self._multipleResultsAllowed = None
        """ Primitive extension for multipleResultsAllowed. Type `FHIRPrimitiveExtension` """
        
        self.normalCodedValueSet = None
        """ Value set of normal coded values for the observations conforming to
        this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._normalCodedValueSet = None
        """ Primitive extension for normalCodedValueSet. Type `FHIRPrimitiveExtension` """
        
        self.permittedDataType = None
        """ Quantity | CodeableConcept | string | boolean | integer | Range |
        Ratio | SampledData | time | dateTime | Period.
        List of `str` items. """
        self._permittedDataType = None
        """ Primitive extension for permittedDataType. Type `FHIRPrimitiveExtension` """
        
        self.preferredReportName = None
        """ Preferred report name.
        Type `str`. """
        self._preferredReportName = None
        """ Primitive extension for preferredReportName. Type `FHIRPrimitiveExtension` """
        
        self.qualifiedInterval = None
        """ Qualified range for continuous and ordinal observation results.
        List of `ObservationDefinitionQualifiedInterval` items (represented as `dict` in JSON). """
        self._qualifiedInterval = None
        """ Primitive extension for qualifiedInterval. Type `FHIRPrimitiveExtension` """
        
        self.quantitativeDetails = None
        """ Characteristics of quantitative results.
        Type `ObservationDefinitionQuantitativeDetails` (represented as `dict` in JSON). """
        self._quantitativeDetails = None
        """ Primitive extension for quantitativeDetails. Type `FHIRPrimitiveExtension` """
        
        self.validCodedValueSet = None
        """ Value set of valid coded values for the observations conforming to
        this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._validCodedValueSet = None
        """ Primitive extension for validCodedValueSet. Type `FHIRPrimitiveExtension` """
        
        super(ObservationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("abnormalCodedValueSet", "abnormalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("_abnormalCodedValueSet", "_abnormalCodedValueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("criticalCodedValueSet", "criticalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("_criticalCodedValueSet", "_criticalCodedValueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False),
            ("_multipleResultsAllowed", "_multipleResultsAllowed", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("normalCodedValueSet", "normalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("_normalCodedValueSet", "_normalCodedValueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("permittedDataType", "permittedDataType", str, True, None, False),
            ("_permittedDataType", "_permittedDataType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preferredReportName", "preferredReportName", str, False, None, False),
            ("_preferredReportName", "_preferredReportName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
            ("_qualifiedInterval", "_qualifiedInterval", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("_quantitativeDetails", "_quantitativeDetails", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("validCodedValueSet", "validCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("_validCodedValueSet", "_validCodedValueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """ Qualified range for continuous and ordinal observation results.
    
    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    
    resource_type = "ObservationDefinitionQualifiedInterval"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.age = None
        """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        self._age = None
        """ Primitive extension for age. Type `FHIRPrimitiveExtension` """
        
        self.appliesTo = None
        """ Targetted population of the range.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._appliesTo = None
        """ Primitive extension for appliesTo. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ reference | critical | absolute.
        Type `str`. """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ Condition associated with the reference range.
        Type `str`. """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.context = None
        """ Range context qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        self._gender = None
        """ Primitive extension for gender. Type `FHIRPrimitiveExtension` """
        
        self.gestationalAge = None
        """ Applicable gestational age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        self._gestationalAge = None
        """ Primitive extension for gestationalAge. Type `FHIRPrimitiveExtension` """
        
        self.range = None
        """ The interval itself, for continuous or ordinal observations.
        Type `Range` (represented as `dict` in JSON). """
        self._range = None
        """ Primitive extension for range. Type `FHIRPrimitiveExtension` """
        
        super(ObservationDefinitionQualifiedInterval, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("_age", "_age", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("_appliesTo", "_appliesTo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", str, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("context", "context", codeableconcept.CodeableConcept, False, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("_gender", "_gender", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("gestationalAge", "gestationalAge", range.Range, False, None, False),
            ("_gestationalAge", "_gestationalAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("range", "range", range.Range, False, None, False),
            ("_range", "_range", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """ Characteristics of quantitative results.
    
    Characteristics for quantitative results of this observation.
    """
    
    resource_type = "ObservationDefinitionQuantitativeDetails"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conversionFactor = None
        """ SI to Customary unit conversion factor.
        Type `float`. """
        self._conversionFactor = None
        """ Primitive extension for conversionFactor. Type `FHIRPrimitiveExtension` """
        
        self.customaryUnit = None
        """ Customary unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._customaryUnit = None
        """ Primitive extension for customaryUnit. Type `FHIRPrimitiveExtension` """
        
        self.decimalPrecision = None
        """ Decimal precision of observation quantitative results.
        Type `int`. """
        self._decimalPrecision = None
        """ Primitive extension for decimalPrecision. Type `FHIRPrimitiveExtension` """
        
        self.unit = None
        """ SI unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._unit = None
        """ Primitive extension for unit. Type `FHIRPrimitiveExtension` """
        
        super(ObservationDefinitionQuantitativeDetails, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("conversionFactor", "conversionFactor", float, False, None, False),
            ("_conversionFactor", "_conversionFactor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("customaryUnit", "customaryUnit", codeableconcept.CodeableConcept, False, None, False),
            ("_customaryUnit", "_customaryUnit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("decimalPrecision", "decimalPrecision", int, False, None, False),
            ("_decimalPrecision", "_decimalPrecision", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
            ("_unit", "_unit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import identifier
from . import range