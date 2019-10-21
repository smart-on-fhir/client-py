#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Dosage) on 2019-05-07.
#  2019, SMART Health IT.


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
        
        self.asNeededBoolean = None
        """ Take "as needed" (for x).
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseAndRate = None
        """ Amount of medication administered.
        List of `DosageDoseAndRate` items (represented as `dict` in JSON). """
        
        self.maxDosePerAdministration = None
        """ Upper limit on medication per administration.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerLifetime = None
        """ Upper limit on medication per lifetime of the patient.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patientInstruction = None
        """ Patient or consumer oriented instructions.
        Type `str`. """
        
        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ The order of the dosage instructions.
        Type `int`. """
        
        self.site = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """
        
        self.timing = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(Dosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Dosage, self).elementProperties()
        js.extend([
            ("additionalInstruction", "additionalInstruction", codeableconcept.CodeableConcept, True, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("doseAndRate", "doseAndRate", DosageDoseAndRate, True, None, False),
            ("maxDosePerAdministration", "maxDosePerAdministration", quantity.Quantity, False, None, False),
            ("maxDosePerLifetime", "maxDosePerLifetime", quantity.Quantity, False, None, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("timing", "timing", timing.Timing, False, None, False),
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
        
        self.doseRange = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ Amount of medication per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRange = None
        """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.type = None
        """ The kind of dose or rate specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DosageDoseAndRate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, "dose", False),
            ("doseRange", "doseRange", range.Range, False, "dose", False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
