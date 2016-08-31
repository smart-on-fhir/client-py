#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 (http://hl7.org/fhir/StructureDefinition/PlanDefinition) on 2016-08-31.
#  2016, SMART Health IT.


from . import domainresource

class PlanDefinition(domainresource.DomainResource):
    """ The definition of a plan for a series of actions, independent of any
    specific patient or context.
    
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """
    
    resource_name = "PlanDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionDefinition = None
        """ Action defined by the plan.
        List of `PlanDefinitionActionDefinition` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.contributor = None
        """ A content contributor.
        List of `Contributor` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.coverage = None
        """ Describes the context of use for this asset.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the asset.
        Type `str`. """
        
        self.effectivePeriod = None
        """ The effective date range for the asset.
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Logical identifier(s) for the asset.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ Last review date for the asset.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.library = None
        """ Logic used by the plan definition.
        List of `FHIRReference` items referencing `Library` (represented as `dict` in JSON). """
        
        self.name = None
        """ A machine-friendly name for the asset.
        Type `str`. """
        
        self.publicationDate = None
        """ Publication date for this version of the asset.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Describes the purpose of the asset.
        Type `str`. """
        
        self.relatedResource = None
        """ Related resources for the asset.
        List of `RelatedResource` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | inactive.
        Type `str`. """
        
        self.title = None
        """ A user-friendly title for the asset.
        Type `str`. """
        
        self.topic = None
        """ Descriptional topics for the asset.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ order-set | protocol | eca-rule.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.url = None
        """ Logical URL to reference this asset.
        Type `str`. """
        
        self.usage = None
        """ Describes the clinical usage of the asset.
        Type `str`. """
        
        self.version = None
        """ The version of the asset, if any.
        Type `str`. """
        
        super(PlanDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinition, self).elementProperties()
        js.extend([
            ("actionDefinition", "actionDefinition", PlanDefinitionActionDefinition, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("contributor", "contributor", contributor.Contributor, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("coverage", "coverage", usagecontext.UsageContext, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedResource", "relatedResource", relatedresource.RelatedResource, True, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class PlanDefinitionActionDefinition(backboneelement.BackboneElement):
    """ Action defined by the plan.
    
    An action to be taken as part of the plan.
    """
    
    resource_name = "PlanDefinitionActionDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionDefinition = None
        """ A sub-action.
        List of `PlanDefinitionActionDefinition` items (represented as `dict` in JSON). """
        
        self.actionIdentifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.activityDefinition = None
        """ Description of the activity to be performed.
        Type `FHIRReference` referencing `ActivityDefinition` (represented as `dict` in JSON). """
        
        self.cardinalityBehavior = None
        """ single | multiple.
        Type `str`. """
        
        self.concept = None
        """ The meaning of the action or its sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ Whether or not the action is applicable.
        Type `PlanDefinitionActionDefinitionCondition` (represented as `dict` in JSON). """
        
        self.description = None
        """ Short description of the action.
        Type `str`. """
        
        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `RelatedResource` items (represented as `dict` in JSON). """
        
        self.dynamicValue = None
        """ Dynamic aspects of the definition.
        List of `PlanDefinitionActionDefinitionDynamicValue` items (represented as `dict` in JSON). """
        
        self.groupingBehavior = None
        """ visual-group | logical-group | sentence-group.
        Type `str`. """
        
        self.label = None
        """ User-visible label for the action (e.g. 1. or A.).
        Type `str`. """
        
        self.participantType = None
        """ patient | practitioner | related-person.
        List of `str` items. """
        
        self.precheckBehavior = None
        """ yes | no.
        Type `str`. """
        
        self.relatedAction = None
        """ Relationship to another action.
        List of `PlanDefinitionActionDefinitionRelatedAction` items (represented as `dict` in JSON). """
        
        self.requiredBehavior = None
        """ must | could | must-unless-documented.
        Type `str`. """
        
        self.selectionBehavior = None
        """ any | all | all-or-none | exactly-one | at-most-one | one-or-more.
        Type `str`. """
        
        self.textEquivalent = None
        """ Static text equivalent of the action, used if the dynamic aspects
        cannot be interpreted by the receiving system.
        Type `str`. """
        
        self.timingDateTime = None
        """ When the action should take place.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingDuration = None
        """ When the action should take place.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ When the action should take place.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingRange = None
        """ When the action should take place.
        Type `Range` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ When the action should take place.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.title = None
        """ User-visible title.
        Type `str`. """
        
        self.transform = None
        """ Transform to apply the template.
        Type `FHIRReference` referencing `StructureMap` (represented as `dict` in JSON). """
        
        self.triggerDefinition = None
        """ When the action should be triggered.
        List of `TriggerDefinition` items (represented as `dict` in JSON). """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(PlanDefinitionActionDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDefinition, self).elementProperties()
        js.extend([
            ("actionDefinition", "actionDefinition", PlanDefinitionActionDefinition, True, None, False),
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, False),
            ("activityDefinition", "activityDefinition", fhirreference.FHIRReference, False, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("concept", "concept", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", PlanDefinitionActionDefinitionCondition, False, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", relatedresource.RelatedResource, True, None, False),
            ("dynamicValue", "dynamicValue", PlanDefinitionActionDefinitionDynamicValue, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("label", "label", str, False, None, False),
            ("participantType", "participantType", str, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("relatedAction", "relatedAction", PlanDefinitionActionDefinitionRelatedAction, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("transform", "transform", fhirreference.FHIRReference, False, None, False),
            ("triggerDefinition", "triggerDefinition", triggerdefinition.TriggerDefinition, True, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


class PlanDefinitionActionDefinitionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.
    
    An expression specifying whether or not the action is applicable in a given
    context.
    """
    
    resource_name = "PlanDefinitionActionDefinitionCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Natural language description of the condition.
        Type `str`. """
        
        self.expression = None
        """ Boolean-valued expression.
        Type `str`. """
        
        self.language = None
        """ Language of the expression.
        Type `str`. """
        
        super(PlanDefinitionActionDefinitionCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDefinitionCondition, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, False),
        ])
        return js


class PlanDefinitionActionDefinitionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.
    
    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """
    
    resource_name = "PlanDefinitionActionDefinitionDynamicValue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Natural language description of the dynamic value.
        Type `str`. """
        
        self.expression = None
        """ An expression that provides the dynamic value for the customization.
        Type `str`. """
        
        self.language = None
        """ Language of the expression.
        Type `str`. """
        
        self.path = None
        """ The path to the element to be set dynamically.
        Type `str`. """
        
        super(PlanDefinitionActionDefinitionDynamicValue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDefinitionDynamicValue, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, False),
            ("path", "path", str, False, None, False),
        ])
        return js


class PlanDefinitionActionDefinitionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.
    
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    
    resource_name = "PlanDefinitionActionDefinitionRelatedAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionIdentifier = None
        """ Identifier of the related action.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.anchor = None
        """ start | end.
        Type `str`. """
        
        self.offsetDuration = None
        """ Time offset for the relationship.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.offsetRange = None
        """ Time offset for the relationship.
        Type `Range` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ before | after | concurrent.
        Type `str`. """
        
        super(PlanDefinitionActionDefinitionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDefinitionRelatedAction, self).elementProperties()
        js.extend([
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, True),
            ("anchor", "anchor", str, False, None, False),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactdetail
from . import contributor
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range
from . import relatedresource
from . import timing
from . import triggerdefinition
from . import usagecontext
