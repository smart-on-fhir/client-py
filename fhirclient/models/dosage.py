# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Dosage).
# 2024, SMART Health IT.


from . import backboneelement

class Dosage(backboneelement.BackboneElement):
    """ How the medication is/was taken or should be taken.
    
    Indicates how the medication is/was taken or should be taken by the
    patient.
    """
    
    resource_type = "Dosage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additionalInstruction = None
        """ Supplemental instruction or warnings to the patient - e.g. "with
        meals", "may cause drowsiness".
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._additionalInstruction = None
        """ Primitive extension for additionalInstruction. Type `FHIRPrimitiveExtension` """
        
        self.asNeededBoolean = None
        """ Take "as needed" (for x).
        Type `bool`. """
        self._asNeededBoolean = None
        """ Primitive extension for asNeededBoolean. Type `FHIRPrimitiveExtension` """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._asNeededCodeableConcept = None
        """ Primitive extension for asNeededCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.doseAndRate = None
        """ Amount of medication administered.
        List of `DosageDoseAndRate` items (represented as `dict` in JSON). """
        self._doseAndRate = None
        """ Primitive extension for doseAndRate. Type `FHIRPrimitiveExtension` """
        
        self.maxDosePerAdministration = None
        """ Upper limit on medication per administration.
        Type `Quantity` (represented as `dict` in JSON). """
        self._maxDosePerAdministration = None
        """ Primitive extension for maxDosePerAdministration. Type `FHIRPrimitiveExtension` """
        
        self.maxDosePerLifetime = None
        """ Upper limit on medication per lifetime of the patient.
        Type `Quantity` (represented as `dict` in JSON). """
        self._maxDosePerLifetime = None
        """ Primitive extension for maxDosePerLifetime. Type `FHIRPrimitiveExtension` """
        
        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        self._maxDosePerPeriod = None
        """ Primitive extension for maxDosePerPeriod. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.patientInstruction = None
        """ Patient or consumer oriented instructions.
        Type `str`. """
        self._patientInstruction = None
        """ Primitive extension for patientInstruction. Type `FHIRPrimitiveExtension` """
        
        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._route = None
        """ Primitive extension for route. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ The order of the dosage instructions.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        self.site = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._site = None
        """ Primitive extension for site. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.timing = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        self._timing = None
        """ Primitive extension for timing. Type `FHIRPrimitiveExtension` """
        
        super(Dosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Dosage, self).elementProperties()
        js.extend([
            ("additionalInstruction", "additionalInstruction", codeableconcept.CodeableConcept, True, None, False),
            ("_additionalInstruction", "_additionalInstruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("_asNeededBoolean", "_asNeededBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("_asNeededCodeableConcept", "_asNeededCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseAndRate", "doseAndRate", DosageDoseAndRate, True, None, False),
            ("_doseAndRate", "_doseAndRate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxDosePerAdministration", "maxDosePerAdministration", quantity.Quantity, False, None, False),
            ("_maxDosePerAdministration", "_maxDosePerAdministration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxDosePerLifetime", "maxDosePerLifetime", quantity.Quantity, False, None, False),
            ("_maxDosePerLifetime", "_maxDosePerLifetime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False),
            ("_maxDosePerPeriod", "_maxDosePerPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("_patientInstruction", "_patientInstruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("_route", "_route", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, False),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("_site", "_site", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timing", "timing", timing.Timing, False, None, False),
            ("_timing", "_timing", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import element

class DosageDoseAndRate(element.Element):
    """ Amount of medication administered.
    
    The amount of medication administered.
    """
    
    resource_type = "DosageDoseAndRate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.doseQuantity = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        self._doseQuantity = None
        """ Primitive extension for doseQuantity. Type `FHIRPrimitiveExtension` """
        
        self.doseRange = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
        self._doseRange = None
        """ Primitive extension for doseRange. Type `FHIRPrimitiveExtension` """
        
        self.rateQuantity = None
        """ Amount of medication per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        self._rateQuantity = None
        """ Primitive extension for rateQuantity. Type `FHIRPrimitiveExtension` """
        
        self.rateRange = None
        """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        self._rateRange = None
        """ Primitive extension for rateRange. Type `FHIRPrimitiveExtension` """
        
        self.rateRatio = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        self._rateRatio = None
        """ Primitive extension for rateRatio. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The kind of dose or rate specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(DosageDoseAndRate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, "dose", False),
            ("_doseQuantity", "_doseQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseRange", "doseRange", range.Range, False, "dose", False),
            ("_doseRange", "_doseRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("_rateQuantity", "_rateQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
            ("_rateRange", "_rateRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("_rateRatio", "_rateRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import quantity
from . import range
from . import ratio
from . import timing