#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Observation) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Observation(domainresource.DomainResource):
    """ Measurements and simple assertions.
    
    Measurements and simple assertions made about a patient, device or other
    subject.
    """
    
    resource_name = "Observation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite = None
        """ Observed body part.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ Classification of  type of observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comments = None
        """ Comments about result.
        Type `str`. """
        
        self.component = None
        """ Component results.
        List of `ObservationComponent` items (represented as `dict` in JSON). """
        
        self.dataAbsentReason = None
        """ Why the result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.device = None
        """ (Measurement) Device.
        Type `FHIRReference` referencing `Device, DeviceMetric` (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
        """ Clinically relevant time/time-period for observation.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ Clinically relevant time/time-period for observation.
        Type `Period` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Healthcare event during which this observation is made.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique Id for this particular observation.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interpretation = None
        """ High, low, normal, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Date/Time this was made available.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.method = None
        """ How it was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who is responsible for the observation.
        List of `FHIRReference` items referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.referenceRange = None
        """ Provides guide for interpretation.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
        
        self.related = None
        """ Resource related to this observation.
        List of `ObservationRelated` items (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimen used for this observation.
        Type `FHIRReference` referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | preliminary | final | amended +.
        Type `str`. """
        
        self.subject = None
        """ Who and/or what this is about.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Actual result.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Actual result.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueDateTime = None
        """ Actual result.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valuePeriod = None
        """ Actual result.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Actual result.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Actual result.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Actual result.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ Actual result.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Actual result.
        Type `str`. """
        
        self.valueTime = None
        """ Actual result.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Observation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Observation, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("comments", "comments", str, False, None, False),
            ("component", "component", ObservationComponent, True, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interpretation", "interpretation", codeableconcept.CodeableConcept, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("related", "related", ObservationRelated, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
        ])
        return js


from . import backboneelement

class ObservationComponent(backboneelement.BackboneElement):
    """ Component results.
    
    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """
    
    resource_name = "ObservationComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of component observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dataAbsentReason = None
        """ Why the component result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.referenceRange = None
        """ Provides guide for interpretation of component result.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Actual component result.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Actual component result.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueDateTime = None
        """ Actual component result.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valuePeriod = None
        """ Actual component result.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Actual component result.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Actual component result.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Actual component result.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ Actual component result.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Actual component result.
        Type `str`. """
        
        self.valueTime = None
        """ Actual component result.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ObservationComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
        ])
        return js


class ObservationReferenceRange(backboneelement.BackboneElement):
    """ Provides guide for interpretation.
    
    Guidance on how to interpret the value by comparison to a normal or
    recommended range.
    """
    
    resource_name = "ObservationReferenceRange"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.age = None
        """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.high = None
        """ High Range, if relevant.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.low = None
        """ Low Range, if relevant.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.meaning = None
        """ Indicates the meaning/use of this range of this range.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text based reference range in an observation.
        Type `str`. """
        
        super(ObservationReferenceRange, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationReferenceRange, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("high", "high", quantity.Quantity, False, None, False),
            ("low", "low", quantity.Quantity, False, None, False),
            ("meaning", "meaning", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class ObservationRelated(backboneelement.BackboneElement):
    """ Resource related to this observation.
    
    A  reference to another resource (usually another Observation but could
    also be a QuestionnaireAnswer) whose relationship is defined by the
    relationship type code.
    """
    
    resource_name = "ObservationRelated"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.target = None
        """ Resource that is related to this one.
        Type `FHIRReference` referencing `Observation, QuestionnaireResponse` (represented as `dict` in JSON). """
        
        self.type = None
        """ has-member | derived-from | sequel-to | replaces | qualified-by |
        interfered-by.
        Type `str`. """
        
        super(ObservationRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationRelated, self).elementProperties()
        js.extend([
            ("target", "target", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata
