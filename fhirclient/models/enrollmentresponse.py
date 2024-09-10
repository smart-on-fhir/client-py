# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse).
# 2024, SMART Health IT.


from . import domainresource

class EnrollmentResponse(domainresource.DomainResource):
    """ EnrollmentResponse resource.
    
    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """
    
    resource_type = "EnrollmentResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        self._disposition = None
        """ Primitive extension for disposition. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.organization = None
        """ Insurer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._organization = None
        """ Primitive extension for organization. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ queued | complete | error | partial.
        Type `str`. """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Claim reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requestProvider = None
        """ Primitive extension for requestProvider. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(EnrollmentResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, False),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("_organization", "_organization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("_requestProvider", "_requestProvider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import fhirdatetime
from . import fhirreference
from . import identifier