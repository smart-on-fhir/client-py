# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation).
# 2024, SMART Health IT.


from . import domainresource

class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.
    
    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """
    
    resource_type = "ImmunizationRecommendation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ Who is responsible for protocol.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._authority = None
        """ Primitive extension for authority. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date recommendation(s) created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Who this profile is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.recommendation = None
        """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """
        self._recommendation = None
        """ Primitive extension for recommendation. Type `FHIRPrimitiveExtension` """
        
        super(ImmunizationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("_authority", "_authority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, True),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True, None, True),
            ("_recommendation", "_recommendation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """
    
    resource_type = "ImmunizationRecommendationRecommendation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contraindicatedVaccineCode = None
        """ Vaccine which is contraindicated to fulfill the recommendation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._contraindicatedVaccineCode = None
        """ Primitive extension for contraindicatedVaccineCode. Type `FHIRPrimitiveExtension` """
        
        self.dateCriterion = None
        """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """
        self._dateCriterion = None
        """ Primitive extension for dateCriterion. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Protocol details.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.doseNumberPositiveInt = None
        """ Recommended dose number within series.
        Type `int`. """
        self._doseNumberPositiveInt = None
        """ Primitive extension for doseNumberPositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.doseNumberString = None
        """ Recommended dose number within series.
        Type `str`. """
        self._doseNumberString = None
        """ Primitive extension for doseNumberString. Type `FHIRPrimitiveExtension` """
        
        self.forecastReason = None
        """ Vaccine administration status reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._forecastReason = None
        """ Primitive extension for forecastReason. Type `FHIRPrimitiveExtension` """
        
        self.forecastStatus = None
        """ Vaccine recommendation status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._forecastStatus = None
        """ Primitive extension for forecastStatus. Type `FHIRPrimitiveExtension` """
        
        self.series = None
        """ Name of vaccination series.
        Type `str`. """
        self._series = None
        """ Primitive extension for series. Type `FHIRPrimitiveExtension` """
        
        self.seriesDosesPositiveInt = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        self._seriesDosesPositiveInt = None
        """ Primitive extension for seriesDosesPositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.seriesDosesString = None
        """ Recommended number of doses for immunity.
        Type `str`. """
        self._seriesDosesString = None
        """ Primitive extension for seriesDosesString. Type `FHIRPrimitiveExtension` """
        
        self.supportingImmunization = None
        """ Past immunizations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingImmunization = None
        """ Primitive extension for supportingImmunization. Type `FHIRPrimitiveExtension` """
        
        self.supportingPatientInformation = None
        """ Patient observations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingPatientInformation = None
        """ Primitive extension for supportingPatientInformation. Type `FHIRPrimitiveExtension` """
        
        self.targetDisease = None
        """ Disease to be immunized against.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._targetDisease = None
        """ Primitive extension for targetDisease. Type `FHIRPrimitiveExtension` """
        
        self.vaccineCode = None
        """ Vaccine  or vaccine group recommendation applies to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._vaccineCode = None
        """ Primitive extension for vaccineCode. Type `FHIRPrimitiveExtension` """
        
        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", codeableconcept.CodeableConcept, True, None, False),
            ("_contraindicatedVaccineCode", "_contraindicatedVaccineCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True, None, False),
            ("_dateCriterion", "_dateCriterion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("_doseNumberPositiveInt", "_doseNumberPositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("_doseNumberString", "_doseNumberString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("forecastReason", "forecastReason", codeableconcept.CodeableConcept, True, None, False),
            ("_forecastReason", "_forecastReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, False, None, True),
            ("_forecastStatus", "_forecastStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("series", "series", str, False, None, False),
            ("_series", "_series", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("_seriesDosesPositiveInt", "_seriesDosesPositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("_seriesDosesString", "_seriesDosesString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, True, None, False),
            ("_supportingImmunization", "_supportingImmunization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, True, None, False),
            ("_supportingPatientInformation", "_supportingPatientInformation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, False),
            ("_targetDisease", "_targetDisease", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, True, None, False),
            ("_vaccineCode", "_vaccineCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.
    
    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    
    resource_type = "ImmunizationRecommendationRecommendationDateCriterion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ Recommended date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", fhirdatetime.FHIRDateTime, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier