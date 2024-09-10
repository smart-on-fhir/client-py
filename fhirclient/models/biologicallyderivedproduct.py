# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct).
# 2024, SMART Health IT.


from . import domainresource

class BiologicallyDerivedProduct(domainresource.DomainResource):
    """ A material substance originating from a biological entity.
    
    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """
    
    resource_type = "BiologicallyDerivedProduct"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collection = None
        """ How this product was collected.
        Type `BiologicallyDerivedProductCollection` (represented as `dict` in JSON). """
        self._collection = None
        """ Primitive extension for collection. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.manipulation = None
        """ Any manipulation of product post-collection.
        Type `BiologicallyDerivedProductManipulation` (represented as `dict` in JSON). """
        self._manipulation = None
        """ Primitive extension for manipulation. Type `FHIRPrimitiveExtension` """
        
        self.parent = None
        """ BiologicallyDerivedProduct parent.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._parent = None
        """ Primitive extension for parent. Type `FHIRPrimitiveExtension` """
        
        self.processing = None
        """ Any processing of the product during collection.
        List of `BiologicallyDerivedProductProcessing` items (represented as `dict` in JSON). """
        self._processing = None
        """ Primitive extension for processing. Type `FHIRPrimitiveExtension` """
        
        self.productCategory = None
        """ organ | tissue | fluid | cells | biologicalAgent.
        Type `str`. """
        self._productCategory = None
        """ Primitive extension for productCategory. Type `FHIRPrimitiveExtension` """
        
        self.productCode = None
        """ What this biologically derived product is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productCode = None
        """ Primitive extension for productCode. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ The amount of this biologically derived product.
        Type `int`. """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Procedure request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ available | unavailable.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.storage = None
        """ Product storage.
        List of `BiologicallyDerivedProductStorage` items (represented as `dict` in JSON). """
        self._storage = None
        """ Primitive extension for storage. Type `FHIRPrimitiveExtension` """
        
        super(BiologicallyDerivedProduct, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProduct, self).elementProperties()
        js.extend([
            ("collection", "collection", BiologicallyDerivedProductCollection, False, None, False),
            ("_collection", "_collection", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manipulation", "manipulation", BiologicallyDerivedProductManipulation, False, None, False),
            ("_manipulation", "_manipulation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("_parent", "_parent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("processing", "processing", BiologicallyDerivedProductProcessing, True, None, False),
            ("_processing", "_processing", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productCategory", "productCategory", str, False, None, False),
            ("_productCategory", "_productCategory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productCode", "productCode", codeableconcept.CodeableConcept, False, None, False),
            ("_productCode", "_productCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("storage", "storage", BiologicallyDerivedProductStorage, True, None, False),
            ("_storage", "_storage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """ How this product was collected.
    """
    
    resource_type = "BiologicallyDerivedProductCollection"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collectedDateTime = None
        """ Time of product collection.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._collectedDateTime = None
        """ Primitive extension for collectedDateTime. Type `FHIRPrimitiveExtension` """
        
        self.collectedPeriod = None
        """ Time of product collection.
        Type `Period` (represented as `dict` in JSON). """
        self._collectedPeriod = None
        """ Primitive extension for collectedPeriod. Type `FHIRPrimitiveExtension` """
        
        self.collector = None
        """ Individual performing collection.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._collector = None
        """ Primitive extension for collector. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Who is product from.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        super(BiologicallyDerivedProductCollection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductCollection, self).elementProperties()
        js.extend([
            ("collectedDateTime", "collectedDateTime", fhirdatetime.FHIRDateTime, False, "collected", False),
            ("_collectedDateTime", "_collectedDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
            ("_collectedPeriod", "_collectedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("_collector", "_collector", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    """ Any manipulation of product post-collection.
    
    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """
    
    resource_type = "BiologicallyDerivedProductManipulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of manipulation.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.timeDateTime = None
        """ Time of manipulation.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._timeDateTime = None
        """ Primitive extension for timeDateTime. Type `FHIRPrimitiveExtension` """
        
        self.timePeriod = None
        """ Time of manipulation.
        Type `Period` (represented as `dict` in JSON). """
        self._timePeriod = None
        """ Primitive extension for timePeriod. Type `FHIRPrimitiveExtension` """
        
        super(BiologicallyDerivedProductManipulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductManipulation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdatetime.FHIRDateTime, False, "time", False),
            ("_timeDateTime", "_timeDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
            ("_timePeriod", "_timePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    """ Any processing of the product during collection.
    
    Any processing of the product during collection that does not change the
    fundamental nature of the product. For example adding anti-coagulants
    during the collection of Peripheral Blood Stem Cells.
    """
    
    resource_type = "BiologicallyDerivedProductProcessing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive = None
        """ Substance added during processing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._additive = None
        """ Primitive extension for additive. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Description of of processing.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.procedure = None
        """ Procesing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._procedure = None
        """ Primitive extension for procedure. Type `FHIRPrimitiveExtension` """
        
        self.timeDateTime = None
        """ Time of processing.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._timeDateTime = None
        """ Primitive extension for timeDateTime. Type `FHIRPrimitiveExtension` """
        
        self.timePeriod = None
        """ Time of processing.
        Type `Period` (represented as `dict` in JSON). """
        self._timePeriod = None
        """ Primitive extension for timePeriod. Type `FHIRPrimitiveExtension` """
        
        super(BiologicallyDerivedProductProcessing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, False, None, False),
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


class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    """ Product storage.
    """
    
    resource_type = "BiologicallyDerivedProductStorage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of storage.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.duration = None
        """ Storage timeperiod.
        Type `Period` (represented as `dict` in JSON). """
        self._duration = None
        """ Primitive extension for duration. Type `FHIRPrimitiveExtension` """
        
        self.scale = None
        """ farenheit | celsius | kelvin.
        Type `str`. """
        self._scale = None
        """ Primitive extension for scale. Type `FHIRPrimitiveExtension` """
        
        self.temperature = None
        """ Storage temperature.
        Type `float`. """
        self._temperature = None
        """ Primitive extension for temperature. Type `FHIRPrimitiveExtension` """
        
        super(BiologicallyDerivedProductStorage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductStorage, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("duration", "duration", period.Period, False, None, False),
            ("_duration", "_duration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("scale", "scale", str, False, None, False),
            ("_scale", "_scale", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("temperature", "temperature", float, False, None, False),
            ("_temperature", "_temperature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period