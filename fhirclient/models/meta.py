# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Meta).
# 2024, SMART Health IT.


from . import element

class Meta(element.Element):
    """ Metadata about a resource.
    
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """
    
    resource_type = "Meta"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.lastUpdated = None
        """ When the resource version last changed.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._lastUpdated = None
        """ Primitive extension for lastUpdated. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ Profiles this resource claims to conform to.
        List of `str` items. """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        self.security = None
        """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        self._security = None
        """ Primitive extension for security. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Identifies where the resource comes from.
        Type `str`. """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.tag = None
        """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        self._tag = None
        """ Primitive extension for tag. Type `FHIRPrimitiveExtension` """
        
        self.versionId = None
        """ Version specific identifier.
        Type `str`. """
        self._versionId = None
        """ Primitive extension for versionId. Type `FHIRPrimitiveExtension` """
        
        super(Meta, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend([
            ("lastUpdated", "lastUpdated", fhirinstant.FHIRInstant, False, None, False),
            ("_lastUpdated", "_lastUpdated", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("security", "security", coding.Coding, True, None, False),
            ("_security", "_security", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", str, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("tag", "tag", coding.Coding, True, None, False),
            ("_tag", "_tag", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("versionId", "versionId", str, False, None, False),
            ("_versionId", "_versionId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import coding
from . import fhirinstant