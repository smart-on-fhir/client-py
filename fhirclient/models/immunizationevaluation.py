# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation).
# 2024, SMART Health IT.


from . import domainresource

class ImmunizationEvaluation(domainresource.DomainResource):
    """ Immunization evaluation information.
    
    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """
    
    resource_type = "ImmunizationEvaluation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ Who is responsible for publishing the recommendations.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._authority = None
        """ Primitive extension for authority. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date evaluation was performed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Evaluation notes.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.doseNumberPositiveInt = None
        """ Dose number within series.
        Type `int`. """
        self._doseNumberPositiveInt = None
        """ Primitive extension for doseNumberPositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.doseNumberString = None
        """ Dose number within series.
        Type `str`. """
        self._doseNumberString = None
        """ Primitive extension for doseNumberString. Type `FHIRPrimitiveExtension` """
        
        self.doseStatus = None
        """ Status of the dose relative to published recommendations.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._doseStatus = None
        """ Primitive extension for doseStatus. Type `FHIRPrimitiveExtension` """
        
        self.doseStatusReason = None
        """ Reason for the dose status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._doseStatusReason = None
        """ Primitive extension for doseStatusReason. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.immunizationEvent = None
        """ Immunization being evaluated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._immunizationEvent = None
        """ Primitive extension for immunizationEvent. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Who this evaluation is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.series = None
        """ Name of vaccine series.
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
        
        self.status = None
        """ completed | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.targetDisease = None
        """ Evaluation target disease.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._targetDisease = None
        """ Primitive extension for targetDisease. Type `FHIRPrimitiveExtension` """
        
        super(ImmunizationEvaluation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationEvaluation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("_authority", "_authority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("_doseNumberPositiveInt", "_doseNumberPositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("_doseNumberString", "_doseNumberString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, False, None, True),
            ("_doseStatus", "_doseStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, True, None, False),
            ("_doseStatusReason", "_doseStatusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("immunizationEvent", "immunizationEvent", fhirreference.FHIRReference, False, None, True),
            ("_immunizationEvent", "_immunizationEvent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("series", "series", str, False, None, False),
            ("_series", "_series", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("_seriesDosesPositiveInt", "_seriesDosesPositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("_seriesDosesString", "_seriesDosesString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, True),
            ("_targetDisease", "_targetDisease", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier