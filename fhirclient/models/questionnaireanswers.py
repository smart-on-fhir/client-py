#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/QuestionnaireAnswers) on 2015-07-06.
#  2015, SMART Health IT.


from . import attachment
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import quantity


class QuestionnaireAnswers(domainresource.DomainResource):
    """ A structured set of questions and their answers.
    
    A structured set of questions and their answers. The questions are ordered
    and grouped into coherent subsets, corresponding to the structure of the
    grouping of the underlying questions.
    """
    
    resource_name = "QuestionnaireAnswers"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Person who received and recorded the answers.
        Type `FHIRReference` referencing `Device, Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.authored = None
        """ Date this version was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None
        """ Primary encounter during which the answers were collected.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.group = None
        """ Grouped questions.
        Type `QuestionnaireAnswersGroup` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique id for this set of answers.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.questionnaire = None
        """ Form being answered.
        Type `FHIRReference` referencing `Questionnaire` (represented as `dict` in JSON). """
        
        self.source = None
        """ The person who answered the questions.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | completed | amended.
        Type `str`. """
        
        self.subject = None
        """ The subject of the questions.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(QuestionnaireAnswers, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(QuestionnaireAnswers, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False),
            ("authored", "authored", fhirdate.FHIRDate, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("group", "group", QuestionnaireAnswersGroup, False),
            ("identifier", "identifier", identifier.Identifier, False),
            ("questionnaire", "questionnaire", fhirreference.FHIRReference, False),
            ("source", "source", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
        ])
        return js


class QuestionnaireAnswersGroup(fhirelement.FHIRElement):
    """ Grouped questions.
    
    A group of questions to a possibly similarly grouped set of questions in
    the questionnaire answers.
    """
    
    resource_name = "QuestionnaireAnswersGroup"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.group = None
        """ Nested questionnaire answers group.
        List of `QuestionnaireAnswersGroup` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Corresponding group within Questionnaire.
        Type `str`. """
        
        self.question = None
        """ Questions in this group.
        List of `QuestionnaireAnswersGroupQuestion` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ The subject this group's answers are about.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.text = None
        """ Additional text for the group.
        Type `str`. """
        
        self.title = None
        """ Name for this group.
        Type `str`. """
        
        super(QuestionnaireAnswersGroup, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(QuestionnaireAnswersGroup, self).elementProperties()
        js.extend([
            ("group", "group", QuestionnaireAnswersGroup, True),
            ("linkId", "linkId", str, False),
            ("question", "question", QuestionnaireAnswersGroupQuestion, True),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("text", "text", str, False),
            ("title", "title", str, False),
        ])
        return js


class QuestionnaireAnswersGroupQuestion(fhirelement.FHIRElement):
    """ Questions in this group.
    
    Set of questions within this group. The order of questions within the group
    is relevant.
    """
    
    resource_name = "QuestionnaireAnswersGroupQuestion"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.answer = None
        """ The response(s) to the question.
        List of `QuestionnaireAnswersGroupQuestionAnswer` items (represented as `dict` in JSON). """
        
        self.group = None
        """ Nested questionnaire group.
        List of `QuestionnaireAnswersGroup` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Corresponding question within Questionnaire.
        Type `str`. """
        
        self.text = None
        """ Text of the question as it is shown to the user.
        Type `str`. """
        
        super(QuestionnaireAnswersGroupQuestion, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(QuestionnaireAnswersGroupQuestion, self).elementProperties()
        js.extend([
            ("answer", "answer", QuestionnaireAnswersGroupQuestionAnswer, True),
            ("group", "group", QuestionnaireAnswersGroup, True),
            ("linkId", "linkId", str, False),
            ("text", "text", str, False),
        ])
        return js


class QuestionnaireAnswersGroupQuestionAnswer(fhirelement.FHIRElement):
    """ The response(s) to the question.
    
    The respondent's answer(s) to the question.
    """
    
    resource_name = "QuestionnaireAnswersGroupQuestionAnswer"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
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
        
        self.valueInstant = None
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        
        super(QuestionnaireAnswersGroupQuestionAnswer, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(QuestionnaireAnswersGroupQuestionAnswer, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, False),
            ("valueBoolean", "valueBoolean", bool, False),
            ("valueCoding", "valueCoding", coding.Coding, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False),
            ("valueDecimal", "valueDecimal", float, False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False),
            ("valueInteger", "valueInteger", int, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False),
            ("valueString", "valueString", str, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False),
            ("valueUri", "valueUri", str, False),
        ])
        return js

