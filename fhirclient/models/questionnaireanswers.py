#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (questionnaireanswers.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import attachment
import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import quantity


class QuestionnaireAnswers(fhirresource.FHIRResource):
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
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
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
        """ in progress | completed | amended.
        Type `str`. """
        
        self.subject = None
        """ The subject of the questions.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        super(QuestionnaireAnswers, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(QuestionnaireAnswers, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'authored' in jsondict:
            self.authored = fhirdate.FHIRDate.with_json_and_owner(jsondict['authored'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'group' in jsondict:
            self.group = QuestionnaireAnswersGroup.with_json_and_owner(jsondict['group'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'questionnaire' in jsondict:
            self.questionnaire = fhirreference.FHIRReference.with_json_and_owner(jsondict['questionnaire'], self)
        if 'source' in jsondict:
            self.source = fhirreference.FHIRReference.with_json_and_owner(jsondict['source'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)


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
        """ Grouped questions.
        List of `QuestionnaireAnswersGroup` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Corresponding group within Questionnaire.
        Type `str`. """
        
        self.question = None
        """ Questions in this group.
        List of `QuestionnaireAnswersGroupQuestion` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ The subject this group's answers are about.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.text = None
        """ Additional text for the group.
        Type `str`. """
        
        self.title = None
        """ Name for this group.
        Type `str`. """
        
        super(QuestionnaireAnswersGroup, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(QuestionnaireAnswersGroup, self).update_with_json(jsondict)
        if 'group' in jsondict:
            self.group = QuestionnaireAnswersGroup.with_json_and_owner(jsondict['group'], self)
        if 'linkId' in jsondict:
            self.linkId = jsondict['linkId']
        if 'question' in jsondict:
            self.question = QuestionnaireAnswersGroupQuestion.with_json_and_owner(jsondict['question'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'title' in jsondict:
            self.title = jsondict['title']


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
        """ Grouped questions.
        List of `QuestionnaireAnswersGroup` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Corresponding question within Questionnaire.
        Type `str`. """
        
        self.text = None
        """ Text of the question as it is shown to the user.
        Type `str`. """
        
        super(QuestionnaireAnswersGroupQuestion, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(QuestionnaireAnswersGroupQuestion, self).update_with_json(jsondict)
        if 'answer' in jsondict:
            self.answer = QuestionnaireAnswersGroupQuestionAnswer.with_json_and_owner(jsondict['answer'], self)
        if 'group' in jsondict:
            self.group = QuestionnaireAnswersGroup.with_json_and_owner(jsondict['group'], self)
        if 'linkId' in jsondict:
            self.linkId = jsondict['linkId']
        if 'text' in jsondict:
            self.text = jsondict['text']


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
        
        self.valueBoolean = False
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
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Single-valued answer to the question.
        Type `str`. """
        
        self.valueTime = None
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(QuestionnaireAnswersGroupQuestionAnswer, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(QuestionnaireAnswersGroupQuestionAnswer, self).update_with_json(jsondict)
        if 'valueAttachment' in jsondict:
            self.valueAttachment = attachment.Attachment.with_json_and_owner(jsondict['valueAttachment'], self)
        if 'valueBoolean' in jsondict:
            self.valueBoolean = jsondict['valueBoolean']
        if 'valueCoding' in jsondict:
            self.valueCoding = coding.Coding.with_json_and_owner(jsondict['valueCoding'], self)
        if 'valueDate' in jsondict:
            self.valueDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueDate'], self)
        if 'valueDateTime' in jsondict:
            self.valueDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueDateTime'], self)
        if 'valueDecimal' in jsondict:
            self.valueDecimal = jsondict['valueDecimal']
        if 'valueInstant' in jsondict:
            self.valueInstant = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueInstant'], self)
        if 'valueInteger' in jsondict:
            self.valueInteger = jsondict['valueInteger']
        if 'valueQuantity' in jsondict:
            self.valueQuantity = quantity.Quantity.with_json_and_owner(jsondict['valueQuantity'], self)
        if 'valueReference' in jsondict:
            self.valueReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['valueReference'], self)
        if 'valueString' in jsondict:
            self.valueString = jsondict['valueString']
        if 'valueTime' in jsondict:
            self.valueTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueTime'], self)

