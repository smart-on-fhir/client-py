# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse).
# 2024, SMART Health IT.


from . import domainresource

class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.
    
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    
    resource_type = "GuidanceResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dataRequirement = None
        """ Additional required data.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        self._dataRequirement = None
        """ Primitive extension for dataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter during which the response was returned.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.evaluationMessage = None
        """ Messages resulting from the evaluation of the artifact or artifacts.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._evaluationMessage = None
        """ Primitive extension for evaluationMessage. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.moduleCanonical = None
        """ What guidance was requested.
        Type `str`. """
        self._moduleCanonical = None
        """ Primitive extension for moduleCanonical. Type `FHIRPrimitiveExtension` """
        
        self.moduleCodeableConcept = None
        """ What guidance was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._moduleCodeableConcept = None
        """ Primitive extension for moduleCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.moduleUri = None
        """ What guidance was requested.
        Type `str`. """
        self._moduleUri = None
        """ Primitive extension for moduleUri. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceDateTime = None
        """ When the guidance response was processed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._occurrenceDateTime = None
        """ Primitive extension for occurrenceDateTime. Type `FHIRPrimitiveExtension` """
        
        self.outputParameters = None
        """ The output parameters of the evaluation, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._outputParameters = None
        """ Primitive extension for outputParameters. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Device returning the guidance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why guidance is needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why guidance is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.requestIdentifier = None
        """ The identifier of the request associated with this response, if any.
        Type `Identifier` (represented as `dict` in JSON). """
        self._requestIdentifier = None
        """ Primitive extension for requestIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.result = None
        """ Proposed actions, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._result = None
        """ Primitive extension for result. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ success | data-requested | data-required | in-progress | failure |
        entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Patient the request was performed for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("_dataRequirement", "_dataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False),
            ("_evaluationMessage", "_evaluationMessage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("moduleCanonical", "moduleCanonical", str, False, "module", True),
            ("_moduleCanonical", "_moduleCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("moduleCodeableConcept", "moduleCodeableConcept", codeableconcept.CodeableConcept, False, "module", True),
            ("_moduleCodeableConcept", "_moduleCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("moduleUri", "moduleUri", str, False, "module", True),
            ("_moduleUri", "_moduleUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, None, False),
            ("_occurrenceDateTime", "_occurrenceDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False),
            ("_outputParameters", "_outputParameters", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, None, False),
            ("_requestIdentifier", "_requestIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("result", "result", fhirreference.FHIRReference, False, None, False),
            ("_result", "_result", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import datarequirement
from . import fhirdatetime
from . import fhirreference
from . import identifier