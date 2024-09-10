# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Linkage).
# 2024, SMART Health IT.


from . import domainresource

class Linkage(domainresource.DomainResource):
    """ Links records for 'same' item.
    
    Identifies two or more records (resource instances) that refer to the same
    real-world "occurrence".
    """
    
    resource_type = "Linkage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this linkage assertion is active or not.
        Type `bool`. """
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Who is responsible for linkages.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Item to be linked.
        List of `LinkageItem` items (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        super(Linkage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Linkage, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", LinkageItem, True, None, True),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class LinkageItem(backboneelement.BackboneElement):
    """ Item to be linked.
    
    Identifies which record considered as the reference to the same real-world
    occurrence as well as how the items should be evaluated within the
    collection of linked items.
    """
    
    resource_type = "LinkageItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.resource = None
        """ Resource being linked.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ source | alternate | historical.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(LinkageItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LinkageItem, self).elementProperties()
        js.extend([
            ("resource", "resource", fhirreference.FHIRReference, False, None, True),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import fhirreference