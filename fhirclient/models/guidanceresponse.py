#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.
    
    A guidance response is the formal response to a previous guidance request.
    It is a derivative of the knowledge response that provides additional
    information relevant specifically to clinical decision support such as a
    description of any proposed actions to be taken.
    """
    
    resource_name = "GuidanceResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ None.
        List of `GuidanceResponseAction` items (represented as `dict` in JSON). """
        
        self.dataRequirement = None
        """ None.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.evaluationMessage = None
        """ Messages resulting from the evaluation of the artifact or artifacts.
        List of `FHIRReference` items referencing `OperationOutcome` (represented as `dict` in JSON). """
        
        self.module = None
        """ A reference to a knowledge module.
        Type `FHIRReference` referencing `DecisionSupportServiceModule, DecisionSupportRule` (represented as `dict` in JSON). """
        
        self.outputParameters = None
        """ The output parameters of the evaluation, if any.
        Type `FHIRReference` referencing `Parameters` (represented as `dict` in JSON). """
        
        self.requestId = None
        """ The id of the request associated with this response, if any.
        Type `str`. """
        
        self.status = None
        """ success | data-requested | data-required | in-progress | failure.
        Type `str`. """
        
        super(GuidanceResponse, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("action", "action", GuidanceResponseAction, True, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False),
            ("module", "module", fhirreference.FHIRReference, False, None, True),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False),
            ("requestId", "requestId", str, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class GuidanceResponseAction(backboneelement.BackboneElement):
    """ None.
    
    The actions, if any, produced by the evaluation of the artifact.
    """
    
    resource_name = "GuidanceResponseAction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actionIdentifier = None
        """ None.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.actions = None
        """ None.
        List of `GuidanceResponseAction` items (represented as `dict` in JSON). """
        
        self.concept = None
        """ None.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ None.
        Type `str`. """
        
        self.documentation = None
        """ None.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.number = None
        """ None.
        Type `str`. """
        
        self.participant = None
        """ None.
        List of `FHIRReference` items referencing `Patient, Person, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.resource = None
        """ None.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.supportingEvidence = None
        """ None.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.textEquivalent = None
        """ None.
        Type `str`. """
        
        self.title = None
        """ None.
        Type `str`. """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `str`. """
        
        super(GuidanceResponseAction, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(GuidanceResponseAction, self).elementProperties()
        js.extend([
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, False),
            ("actions", "actions", GuidanceResponseAction, True, None, False),
            ("concept", "concept", codeableconcept.CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", attachment.Attachment, True, None, False),
            ("number", "number", str, False, None, False),
            ("participant", "participant", fhirreference.FHIRReference, True, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("supportingEvidence", "supportingEvidence", attachment.Attachment, True, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import datarequirement
from . import fhirreference
from . import identifier
