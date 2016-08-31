#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 (http://hl7.org/fhir/StructureDefinition/ActivityDefinition) on 2016-08-31.
#  2016, SMART Health IT.


from . import domainresource

class ActivityDefinition(domainresource.DomainResource):
    """ The definition of a specific activity to be taken, independent of any
    particular patient or context.
    
    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """
    
    resource_name = "ActivityDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ communication | device | diagnostic | diet | drug | encounter |
        immunization | observation | procedure | referral | supply | vision
        | other.
        Type `str`. """
        
        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        
        self.dynamicValue = None
        """ Dynamic aspects of the definition.
        List of `ActivityDefinitionDynamicValue` items (represented as `dict` in JSON). """
        
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
        """ Logic used by the asset.
        List of `FHIRReference` items referencing `Library` (represented as `dict` in JSON). """
        
        self.location = None
        """ Where it should happen.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.name = None
        """ A machine-friendly name for the asset.
        Type `str`. """
        
        self.participantType = None
        """ patient | practitioner | related-person.
        List of `str` items. """
        
        self.productCodeableConcept = None
        """ What's administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productReference = None
        """ What's administered/supplied.
        Type `FHIRReference` referencing `Medication, Substance` (represented as `dict` in JSON). """
        
        self.publicationDate = None
        """ Publication date for this version of the asset.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Describes the purpose of the asset.
        Type `str`. """
        
        self.quantity = None
        """ How much is administered/consumed/supplied.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.relatedResource = None
        """ Related resources for the asset.
        List of `RelatedResource` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | inactive.
        Type `str`. """
        
        self.timingCodeableConcept = None
        """ When activity is to occur.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.title = None
        """ A user-friendly title for the asset.
        Type `str`. """
        
        self.topic = None
        """ Descriptional topics for the asset.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.transform = None
        """ Transform to apply the template.
        Type `FHIRReference` referencing `StructureMap` (represented as `dict` in JSON). """
        
        self.url = None
        """ Logical URL to reference this asset.
        Type `str`. """
        
        self.usage = None
        """ Describes the clinical usage of the asset.
        Type `str`. """
        
        self.version = None
        """ The version of the asset, if any.
        Type `str`. """
        
        super(ActivityDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActivityDefinition, self).elementProperties()
        js.extend([
            ("category", "category", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("contributor", "contributor", contributor.Contributor, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("coverage", "coverage", usagecontext.UsageContext, True, None, False),
            ("description", "description", str, False, None, False),
            ("dynamicValue", "dynamicValue", ActivityDefinitionDynamicValue, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", fhirreference.FHIRReference, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("name", "name", str, False, None, False),
            ("participantType", "participantType", str, True, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("relatedResource", "relatedResource", relatedresource.RelatedResource, True, None, False),
            ("status", "status", str, False, None, True),
            ("timingCodeableConcept", "timingCodeableConcept", codeableconcept.CodeableConcept, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("transform", "transform", fhirreference.FHIRReference, False, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.
    
    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    intent resource that would contain the result.
    """
    
    resource_name = "ActivityDefinitionDynamicValue"
    
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
        
        super(ActivityDefinitionDynamicValue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActivityDefinitionDynamicValue, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, False),
            ("path", "path", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import contributor
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import relatedresource
from . import timing
from . import usagecontext
