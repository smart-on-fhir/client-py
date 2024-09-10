# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SupplyRequest).
# 2024, SMART Health IT.


from . import domainresource

class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.
    
    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """
    
    resource_type = "SupplyRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        """ When the request was made.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._authoredOn = None
        """ Primitive extension for authoredOn. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ The kind of supply (central, non-stock, etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.deliverFrom = None
        """ The origin of the supply.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._deliverFrom = None
        """ Primitive extension for deliverFrom. Type `FHIRPrimitiveExtension` """
        
        self.deliverTo = None
        """ The destination of the supply.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._deliverTo = None
        """ Primitive extension for deliverTo. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for SupplyRequest.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.itemCodeableConcept = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._itemCodeableConcept = None
        """ Primitive extension for itemCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.itemReference = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._itemReference = None
        """ Primitive extension for itemReference. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceDateTime = None
        """ When the request should be fulfilled.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._occurrenceDateTime = None
        """ Primitive extension for occurrenceDateTime. Type `FHIRPrimitiveExtension` """
        
        self.occurrencePeriod = None
        """ When the request should be fulfilled.
        Type `Period` (represented as `dict` in JSON). """
        self._occurrencePeriod = None
        """ Primitive extension for occurrencePeriod. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceTiming = None
        """ When the request should be fulfilled.
        Type `Timing` (represented as `dict` in JSON). """
        self._occurrenceTiming = None
        """ Primitive extension for occurrenceTiming. Type `FHIRPrimitiveExtension` """
        
        self.parameter = None
        """ Ordered item details.
        List of `SupplyRequestParameter` items (represented as `dict` in JSON). """
        self._parameter = None
        """ Primitive extension for parameter. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ The requested amount of the item indicated.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ The reason why the supply item was requested.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ The reason why the supply item was requested.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.requester = None
        """ Individual making the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requester = None
        """ Primitive extension for requester. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | suspended +.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.supplier = None
        """ Who is intended to fulfill the request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supplier = None
        """ Primitive extension for supplier. Type `FHIRPrimitiveExtension` """
        
        super(SupplyRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("_authoredOn", "_authoredOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deliverFrom", "deliverFrom", fhirreference.FHIRReference, False, None, False),
            ("_deliverFrom", "_deliverFrom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deliverTo", "deliverTo", fhirreference.FHIRReference, False, None, False),
            ("_deliverTo", "_deliverTo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("_itemCodeableConcept", "_itemCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("_itemReference", "_itemReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", False),
            ("_occurrenceDateTime", "_occurrenceDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("_occurrencePeriod", "_occurrencePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("_occurrenceTiming", "_occurrenceTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parameter", "parameter", SupplyRequestParameter, True, None, False),
            ("_parameter", "_parameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("_requester", "_requester", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, True, None, False),
            ("_supplier", "_supplier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class SupplyRequestParameter(backboneelement.BackboneElement):
    """ Ordered item details.
    
    Specific parameters for the ordered item.  For example, the size of the
    indicated item.
    """
    
    resource_type = "SupplyRequestParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Item detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Value of detail.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Value of detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Value of detail.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ Value of detail.
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        super(SupplyRequestParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("_valueRange", "_valueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import timing