# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Specimen).
# 2024, SMART Health IT.


from . import domainresource

class Specimen(domainresource.DomainResource):
    """ Sample for analysis.
    
    A sample to be used for analysis.
    """
    
    resource_type = "Specimen"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accessionIdentifier = None
        """ Identifier assigned by the lab.
        Type `Identifier` (represented as `dict` in JSON). """
        self._accessionIdentifier = None
        """ Primitive extension for accessionIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.collection = None
        """ Collection details.
        Type `SpecimenCollection` (represented as `dict` in JSON). """
        self._collection = None
        """ Primitive extension for collection. Type `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ State of the specimen.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.container = None
        """ Direct container of specimen (tube/slide, etc.).
        List of `SpecimenContainer` items (represented as `dict` in JSON). """
        self._container = None
        """ Primitive extension for container. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.parent = None
        """ Specimen from which this specimen originated.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._parent = None
        """ Primitive extension for parent. Type `FHIRPrimitiveExtension` """
        
        self.processing = None
        """ Processing and processing step details.
        List of `SpecimenProcessing` items (represented as `dict` in JSON). """
        self._processing = None
        """ Primitive extension for processing. Type `FHIRPrimitiveExtension` """
        
        self.receivedTime = None
        """ The time when specimen was received for processing.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._receivedTime = None
        """ Primitive extension for receivedTime. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Why the specimen was collected.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ available | unavailable | unsatisfactory | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Where the specimen came from. This may be from patient(s), from a
        location (e.g., the source of an environmental sample), or a
        sampling of a substance or a device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Kind of material that forms the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Specimen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Specimen, self).elementProperties()
        js.extend([
            ("accessionIdentifier", "accessionIdentifier", identifier.Identifier, False, None, False),
            ("_accessionIdentifier", "_accessionIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("collection", "collection", SpecimenCollection, False, None, False),
            ("_collection", "_collection", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("condition", "condition", codeableconcept.CodeableConcept, True, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("container", "container", SpecimenContainer, True, None, False),
            ("_container", "_container", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("_parent", "_parent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("processing", "processing", SpecimenProcessing, True, None, False),
            ("_processing", "_processing", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("receivedTime", "receivedTime", fhirdatetime.FHIRDateTime, False, None, False),
            ("_receivedTime", "_receivedTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class SpecimenCollection(backboneelement.BackboneElement):
    """ Collection details.
    
    Details concerning the specimen collection.
    """
    
    resource_type = "SpecimenCollection"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite = None
        """ Anatomical collection site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.collectedDateTime = None
        """ Collection time.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._collectedDateTime = None
        """ Primitive extension for collectedDateTime. Type `FHIRPrimitiveExtension` """
        
        self.collectedPeriod = None
        """ Collection time.
        Type `Period` (represented as `dict` in JSON). """
        self._collectedPeriod = None
        """ Primitive extension for collectedPeriod. Type `FHIRPrimitiveExtension` """
        
        self.collector = None
        """ Who collected the specimen.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._collector = None
        """ Primitive extension for collector. Type `FHIRPrimitiveExtension` """
        
        self.duration = None
        """ How long it took to collect specimen.
        Type `Duration` (represented as `dict` in JSON). """
        self._duration = None
        """ Primitive extension for duration. Type `FHIRPrimitiveExtension` """
        
        self.fastingStatusCodeableConcept = None
        """ Whether or how long patient abstained from food and/or drink.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._fastingStatusCodeableConcept = None
        """ Primitive extension for fastingStatusCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.fastingStatusDuration = None
        """ Whether or how long patient abstained from food and/or drink.
        Type `Duration` (represented as `dict` in JSON). """
        self._fastingStatusDuration = None
        """ Primitive extension for fastingStatusDuration. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ Technique used to perform collection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ The quantity of specimen collected.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        super(SpecimenCollection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenCollection, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("collectedDateTime", "collectedDateTime", fhirdatetime.FHIRDateTime, False, "collected", False),
            ("_collectedDateTime", "_collectedDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
            ("_collectedPeriod", "_collectedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("_collector", "_collector", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("duration", "duration", duration.Duration, False, None, False),
            ("_duration", "_duration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fastingStatusCodeableConcept", "fastingStatusCodeableConcept", codeableconcept.CodeableConcept, False, "fastingStatus", False),
            ("_fastingStatusCodeableConcept", "_fastingStatusCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fastingStatusDuration", "fastingStatusDuration", duration.Duration, False, "fastingStatus", False),
            ("_fastingStatusDuration", "_fastingStatusDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SpecimenContainer(backboneelement.BackboneElement):
    """ Direct container of specimen (tube/slide, etc.).
    
    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    
    resource_type = "SpecimenContainer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveCodeableConcept = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._additiveCodeableConcept = None
        """ Primitive extension for additiveCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.additiveReference = None
        """ Additive associated with container.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._additiveReference = None
        """ Primitive extension for additiveReference. Type `FHIRPrimitiveExtension` """
        
        self.capacity = None
        """ Container volume or size.
        Type `Quantity` (represented as `dict` in JSON). """
        self._capacity = None
        """ Primitive extension for capacity. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Textual description of the container.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Id for the container.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.specimenQuantity = None
        """ Quantity of specimen within container.
        Type `Quantity` (represented as `dict` in JSON). """
        self._specimenQuantity = None
        """ Primitive extension for specimenQuantity. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Kind of container directly associated with specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SpecimenContainer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenContainer, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", False),
            ("_additiveCodeableConcept", "_additiveCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", False),
            ("_additiveReference", "_additiveReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("capacity", "capacity", quantity.Quantity, False, None, False),
            ("_capacity", "_capacity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specimenQuantity", "specimenQuantity", quantity.Quantity, False, None, False),
            ("_specimenQuantity", "_specimenQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SpecimenProcessing(backboneelement.BackboneElement):
    """ Processing and processing step details.
    
    Details concerning processing and processing steps for the specimen.
    """
    
    resource_type = "SpecimenProcessing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive = None
        """ Material used in the processing step.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._additive = None
        """ Primitive extension for additive. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Textual description of procedure.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.procedure = None
        """ Indicates the treatment step  applied to the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._procedure = None
        """ Primitive extension for procedure. Type `FHIRPrimitiveExtension` """
        
        self.timeDateTime = None
        """ Date and time of specimen processing.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._timeDateTime = None
        """ Primitive extension for timeDateTime. Type `FHIRPrimitiveExtension` """
        
        self.timePeriod = None
        """ Date and time of specimen processing.
        Type `Period` (represented as `dict` in JSON). """
        self._timePeriod = None
        """ Primitive extension for timePeriod. Type `FHIRPrimitiveExtension` """
        
        super(SpecimenProcessing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, True, None, False),
            ("_additive", "_additive", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False),
            ("_procedure", "_procedure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdatetime.FHIRDateTime, False, "time", False),
            ("_timeDateTime", "_timeDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
            ("_timePeriod", "_timePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import duration
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity