# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Observation).
# 2024, SMART Health IT.


from . import domainresource

class Observation(domainresource.DomainResource):
    """ Measurements and simple assertions.
    
    Measurements and simple assertions made about a patient, device or other
    subject.
    """
    
    resource_type = "Observation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ Fulfills plan, proposal or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.bodySite = None
        """ Observed body part.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Classification of  type of observation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.component = None
        """ Component results.
        List of `ObservationComponent` items (represented as `dict` in JSON). """
        self._component = None
        """ Primitive extension for component. Type `FHIRPrimitiveExtension` """
        
        self.dataAbsentReason = None
        """ Why the result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._dataAbsentReason = None
        """ Primitive extension for dataAbsentReason. Type `FHIRPrimitiveExtension` """
        
        self.derivedFrom = None
        """ Related measurements the observation is made from.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._derivedFrom = None
        """ Primitive extension for derivedFrom. Type `FHIRPrimitiveExtension` """
        
        self.device = None
        """ (Measurement) Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._device = None
        """ Primitive extension for device. Type `FHIRPrimitiveExtension` """
        
        self.effectiveDateTime = None
        """ Clinically relevant time/time-period for observation.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._effectiveDateTime = None
        """ Primitive extension for effectiveDateTime. Type `FHIRPrimitiveExtension` """
        
        self.effectiveInstant = None
        """ Clinically relevant time/time-period for observation.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._effectiveInstant = None
        """ Primitive extension for effectiveInstant. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ Clinically relevant time/time-period for observation.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.effectiveTiming = None
        """ Clinically relevant time/time-period for observation.
        Type `Timing` (represented as `dict` in JSON). """
        self._effectiveTiming = None
        """ Primitive extension for effectiveTiming. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Healthcare event during which this observation is made.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.focus = None
        """ What the observation is about, when it is not about the subject of
        record.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._focus = None
        """ Primitive extension for focus. Type `FHIRPrimitiveExtension` """
        
        self.hasMember = None
        """ Related resource that belongs to the Observation group.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._hasMember = None
        """ Primitive extension for hasMember. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for observation.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.interpretation = None
        """ High, low, normal, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._interpretation = None
        """ Primitive extension for interpretation. Type `FHIRPrimitiveExtension` """
        
        self.issued = None
        """ Date/Time this version was made available.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._issued = None
        """ Primitive extension for issued. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ How it was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments about the observation.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Who is responsible for the observation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.referenceRange = None
        """ Provides guide for interpretation.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
        self._referenceRange = None
        """ Primitive extension for referenceRange. Type `FHIRPrimitiveExtension` """
        
        self.specimen = None
        """ Specimen used for this observation.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._specimen = None
        """ Primitive extension for specimen. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ registered | preliminary | final | amended +.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who and/or what the observation is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Actual result.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Actual result.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ Actual result.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Actual result.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valuePeriod = None
        """ Actual result.
        Type `Period` (represented as `dict` in JSON). """
        self._valuePeriod = None
        """ Primitive extension for valuePeriod. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Actual result.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ Actual result.
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        self.valueRatio = None
        """ Actual result.
        Type `Ratio` (represented as `dict` in JSON). """
        self._valueRatio = None
        """ Primitive extension for valueRatio. Type `FHIRPrimitiveExtension` """
        
        self.valueSampledData = None
        """ Actual result.
        Type `SampledData` (represented as `dict` in JSON). """
        self._valueSampledData = None
        """ Primitive extension for valueSampledData. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Actual result.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ Actual result.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        super(Observation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Observation, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("component", "component", ObservationComponent, True, None, False),
            ("_component", "_component", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("_dataAbsentReason", "_dataAbsentReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("_derivedFrom", "_derivedFrom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("_device", "_device", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdatetime.FHIRDateTime, False, "effective", False),
            ("_effectiveDateTime", "_effectiveDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectiveInstant", "effectiveInstant", fhirinstant.FHIRInstant, False, "effective", False),
            ("_effectiveInstant", "_effectiveInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectiveTiming", "effectiveTiming", timing.Timing, False, "effective", False),
            ("_effectiveTiming", "_effectiveTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("_focus", "_focus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("hasMember", "hasMember", fhirreference.FHIRReference, True, None, False),
            ("_hasMember", "_hasMember", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("interpretation", "interpretation", codeableconcept.CodeableConcept, True, None, False),
            ("_interpretation", "_interpretation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issued", "issued", fhirinstant.FHIRInstant, False, None, False),
            ("_issued", "_issued", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("_referenceRange", "_referenceRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("_specimen", "_specimen", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", False),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("_valuePeriod", "_valuePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("_valueRange", "_valueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("_valueRatio", "_valueRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("_valueSampledData", "_valueSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", False),
            ("_valueTime", "_valueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
    
    resource_type = "ObservationComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of component observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.dataAbsentReason = None
        """ Why the component result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._dataAbsentReason = None
        """ Primitive extension for dataAbsentReason. Type `FHIRPrimitiveExtension` """
        
        self.interpretation = None
        """ High, low, normal, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._interpretation = None
        """ Primitive extension for interpretation. Type `FHIRPrimitiveExtension` """
        
        self.referenceRange = None
        """ Provides guide for interpretation of component result.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
        self._referenceRange = None
        """ Primitive extension for referenceRange. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Actual component result.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Actual component result.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ Actual component result.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Actual component result.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valuePeriod = None
        """ Actual component result.
        Type `Period` (represented as `dict` in JSON). """
        self._valuePeriod = None
        """ Primitive extension for valuePeriod. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Actual component result.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ Actual component result.
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        self.valueRatio = None
        """ Actual component result.
        Type `Ratio` (represented as `dict` in JSON). """
        self._valueRatio = None
        """ Primitive extension for valueRatio. Type `FHIRPrimitiveExtension` """
        
        self.valueSampledData = None
        """ Actual component result.
        Type `SampledData` (represented as `dict` in JSON). """
        self._valueSampledData = None
        """ Primitive extension for valueSampledData. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Actual component result.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ Actual component result.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        super(ObservationComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("_dataAbsentReason", "_dataAbsentReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("interpretation", "interpretation", codeableconcept.CodeableConcept, True, None, False),
            ("_interpretation", "_interpretation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("_referenceRange", "_referenceRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", False),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("_valuePeriod", "_valuePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("_valueRange", "_valueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("_valueRatio", "_valueRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("_valueSampledData", "_valueSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", False),
            ("_valueTime", "_valueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ObservationReferenceRange(backboneelement.BackboneElement):
    """ Provides guide for interpretation.
    
    Guidance on how to interpret the value by comparison to a normal or
    recommended range.  Multiple reference ranges are interpreted as an "OR".
    In other words, to represent two distinct target populations, two
    `referenceRange` elements would be used.
    """
    
    resource_type = "ObservationReferenceRange"
    
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
        """ Reference range population.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._appliesTo = None
        """ Primitive extension for appliesTo. Type `FHIRPrimitiveExtension` """
        
        self.high = None
        """ High Range, if relevant.
        Type `Quantity` (represented as `dict` in JSON). """
        self._high = None
        """ Primitive extension for high. Type `FHIRPrimitiveExtension` """
        
        self.low = None
        """ Low Range, if relevant.
        Type `Quantity` (represented as `dict` in JSON). """
        self._low = None
        """ Primitive extension for low. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Text based reference range in an observation.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Reference range qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ObservationReferenceRange, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationReferenceRange, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("_age", "_age", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("_appliesTo", "_appliesTo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("high", "high", quantity.Quantity, False, None, False),
            ("_high", "_high", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("low", "low", quantity.Quantity, False, None, False),
            ("_low", "_low", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import fhirtime
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata
from . import timing