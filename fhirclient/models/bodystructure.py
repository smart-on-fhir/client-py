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
        
        self.description = None
        """ Text description.
        Type `str`. """
        
        self.identifier = None
        """ Bodystructure identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.image = None
        """ Attached images.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationQualifier = None
        """ Body site modifier.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.morphology = None
        """ Kind of Structure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who this is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(BodyStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BodyStructure, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("location", "location", codeableconcept.CodeableConcept, False, None, False),
            ("locationQualifier", "locationQualifier", codeableconcept.CodeableConcept, True, None, False),
            ("morphology", "morphology", codeableconcept.CodeableConcept, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import fhirreference
from . import identifier
