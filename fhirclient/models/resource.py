# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Resource).
# 2024, SMART Health IT.


from . import fhirabstractresource

class Resource(fhirabstractresource.FHIRAbstractResource):
    """ Base Resource.
    
    This is the base resource type for everything.
    """
    
    resource_type = "Resource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.id = None
        """ Logical id of this artifact.
        Type `str`. """
        self._id = None
        """ Primitive extension for id. Type `FHIRPrimitiveExtension` """
        
        self.implicitRules = None
        """ A set of rules under which this content was created.
        Type `str`. """
        self._implicitRules = None
        """ Primitive extension for implicitRules. Type `FHIRPrimitiveExtension` """
        
        self.language = None
        """ Language of the resource content.
        Type `str`. """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        self.meta = None
        """ Metadata about the resource.
        Type `Meta` (represented as `dict` in JSON). """
        self._meta = None
        """ Primitive extension for meta. Type `FHIRPrimitiveExtension` """
        
        super(Resource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Resource, self).elementProperties()
        js.extend([
            ("id", "id", str, False, None, False),
            ("_id", "_id", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("implicitRules", "implicitRules", str, False, None, False),
            ("_implicitRules", "_implicitRules", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("language", "language", str, False, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("meta", "meta", meta.Meta, False, None, False),
            ("_meta", "_meta", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import meta