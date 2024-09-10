# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement).
# 2024, SMART Health IT.


from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ Record of use of a device.
    
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    
    resource_type = "DeviceUseStatement"
    
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
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.derivedFrom = None
        """ Supporting information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._derivedFrom = None
        """ Primitive extension for derivedFrom. Type `FHIRPrimitiveExtension` """
        
        self.device = None
        """ Reference to device used.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._device = None
        """ Primitive extension for device. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External identifier for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Addition details (comments, instructions).
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why device was used.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why was DeviceUseStatement performed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.recordedOn = None
        """ When statement was recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._recordedOn = None
        """ Primitive extension for recordedOn. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Who made the statement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | completed | entered-in-error +.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Patient using device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.timingDateTime = None
        """ How often  the device was used.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._timingDateTime = None
        """ Primitive extension for timingDateTime. Type `FHIRPrimitiveExtension` """
        
        self.timingPeriod = None
        """ How often  the device was used.
        Type `Period` (represented as `dict` in JSON). """
        self._timingPeriod = None
        """ Primitive extension for timingPeriod. Type `FHIRPrimitiveExtension` """
        
        self.timingTiming = None
        """ How often  the device was used.
        Type `Timing` (represented as `dict` in JSON). """
        self._timingTiming = None
        """ Primitive extension for timingTiming. Type `FHIRPrimitiveExtension` """
        
        super(DeviceUseStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("_derivedFrom", "_derivedFrom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("_device", "_device", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recordedOn", "recordedOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("_recordedOn", "_recordedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingDateTime", "timingDateTime", fhirdatetime.FHIRDateTime, False, "timing", False),
            ("_timingDateTime", "_timingDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("_timingPeriod", "_timingPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("_timingTiming", "_timingTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import timing