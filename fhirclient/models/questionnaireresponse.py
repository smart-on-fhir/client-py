#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class QuestionnaireResponse(domainresource.DomainResource):
    """ A structured set of questions and their answers.
    
    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the questionnaire being responded to.
    """
    
    resource_type = "QuestionnaireResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ Person who received and recorded the answers.
        Type `FHIRReference` referencing `Device, Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.authored = None
        """ Date the answers were gathered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Request fulfilled by this QuestionnaireResponse.
        List of `FHIRReference` items referencing `ReferralRequest, CarePlan, ProcedureRequest` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or Episode during which questionnaire was completed.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique id for this set of answers.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.item = None
        """ Groups and questions.
        List of `QuestionnaireResponseItem` items (represented as `dict` in JSON). """
        
        self.parent = None
        """ Part of this action.
        List of `FHIRReference` items referencing `Observation, Procedure` (represented as `dict` in JSON). """
        
        self.questionnaire = None
        """ Form being answered.
        Type `FHIRReference` referencing `Questionnaire` (represented as `dict` in JSON). """
        
        self.source = None
        """ The person who answered the questions.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | completed | amended | entered-in-error | stopped.
        Type `str`. """
        
        self.subject = None
        """ The subject of the questions.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(QuestionnaireResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireResponse, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authored", "authored", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("item", "item", QuestionnaireResponseItem, True, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("questionnaire", "questionnaire", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireResponseItem(backboneelement.BackboneElement):
    """ Groups and questions.
    
    A group or question item from the original questionnaire for which answers
    are provided.
    """
    
    resource_type = "QuestionnaireResponseItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answer = None
        """ The response(s) to the question.
        List of `QuestionnaireResponseItemAnswer` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ ElementDefinition - details for the item.
        Type `str`. """
        
        self.item = None
        """ Nested questionnaire response items.
        List of `QuestionnaireResponseItem` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Pointer to specific item from Questionnaire.
        Type `str`. """
        
        self.subject = None
        """ The subject this group's answers are about.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.text = None
        """ Name for group or question text.
        Type `str`. """
        
        super(QuestionnaireResponseItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireResponseItem, self).elementProperties()
        js.extend([
            ("answer", "answer", QuestionnaireResponseItemAnswer, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("item", "item", QuestionnaireResponseItem, True, None, False),
            ("linkId", "linkId", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class QuestionnaireResponseItemAnswer(backboneelement.BackboneElement):
    """ The response(s) to the question.
    
    The respondent's answer(s) to the question.
    """
    
    resource_type = "QuestionnaireResponseItemAnswer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.item = None
        """ Nested groups and questions.
        List of `QuestionnaireResponseItem` items (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Single-valued answer to the question.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ Single-valued answer to the question.
        Type `bool`. """
        
        self.valueCoding = None
        """ Single-valued answer to the question.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Single-valued answer to the question.
        Type `float`. """
        
        self.valueInteger = None
        """ Single-valued answer to the question.
        Type `int`. """
        
        self.valueQuantity = None
        """ Single-valued answer to the question.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Single-valued answer to the question.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Single-valued answer to the question.
        Type `str`. """
        
        self.valueTime = None
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueUri = None
        """ Single-valued answer to the question.
        Type `str`. """
        
        super(QuestionnaireResponseItemAnswer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireResponseItemAnswer, self).elementProperties()
        js.extend([
            ("item", "item", QuestionnaireResponseItem, True, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
