# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/BodyStructure).
# 2024, SMART Health IT.


from . import domainresource

class BodyStructure(domainresource.DomainResource):
    """ Specific and identified anatomical structure.
    
    Record details about an anatomical structure.  This resource may be used
    when a coded concept does not provide the necessary detail needed for the
    use case.
    """
    
    resource_type = "BodyStructure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this record is in active use.
        Type `bool`. """
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Text description.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Bodystructure identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.image = None
        """ Attached images.
        List of `Attachment` items (represented as `dict` in JSON). """
        self._image = None
        """ Primitive extension for image. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.locationQualifier = None
        """ Body site modifier.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._locationQualifier = None
        """ Primitive extension for locationQualifier. Type `FHIRPrimitiveExtension` """
        
        self.morphology = None
        """ Kind of Structure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._morphology = None
        """ Primitive extension for morphology. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Who this is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        super(BodyStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BodyStructure, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("_image", "_image", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", codeableconcept.CodeableConcept, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationQualifier", "locationQualifier", codeableconcept.CodeableConcept, True, None, False),
            ("_locationQualifier", "_locationQualifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("morphology", "morphology", codeableconcept.CodeableConcept, False, None, False),
            ("_morphology", "_morphology", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment
from . import codeableconcept
from . import fhirreference
from . import identifier