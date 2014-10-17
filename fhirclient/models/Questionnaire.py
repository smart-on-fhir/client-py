#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (questionnaire.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import codeableconcept
import coding
import encounter
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import practitioner
import valueset


class Questionnaire(fhirresource.FHIRResource):
    """ A structured set of questions and their answers.
    
    Scope and Usage The Questionnaire may be a single list of questions, or can
    be hierarchically organized in groups and sub-groups, each containing
    questions. Questions may contain and single answer, which can take the form
    of simple text, numbers, dates or a set of coded choices.
    
    Questionnaires cover the need to communicate data originating from forms
    used in medical history examinations, research questionnaires and sometimes
    full clinical speciality records. In many systems this data is collected
    using user-defined screens and forms. Questionnaires record specifics about
    data capture - exactly what questions were asked, in what order, what
    choices for answers were, etc. Each of these questions are part of the
    Questionnaire, and as such the Questionnaire is a separately identifiable
    Resource, whereas the individual questions are not.
    
    Examples of Questionnaires include:
    
    * Past medical history (PMH)
    * Family diseases
    * Social history
    * Research questionnaires
    * Quality and evaluation forms
    Support for validation is outside the scope of this Resource, although
    basic structural features can be defined using the Questionnaire core
    extensions.
    """
    
    resource_name = "Questionnaire"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Person who received and recorded the answers.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.authored = None
        """ Date this version was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None
        """ Primary encounter during which the answers were collected.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.group = None
        """ Grouped questions.
        Type `QuestionnaireGroup` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name/code for a predefined list of questions.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ The person who answered the questions.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | published | retired | in progress | completed | amended.
        Type `str`. """
        
        self.subject = None
        """ The subject of the questions.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(Questionnaire, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Questionnaire, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self, practitioner.Practitioner)
        if 'authored' in jsondict:
            self.authored = fhirdate.FHIRDate.with_json(jsondict['authored'])
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self, encounter.Encounter)
        if 'group' in jsondict:
            self.group = QuestionnaireGroup.with_json(jsondict['group'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'name' in jsondict:
            self.name = codeableconcept.CodeableConcept.with_json(jsondict['name'])
        if 'source' in jsondict:
            self.source = fhirreference.FHIRReference.with_json_and_owner(jsondict['source'], self, patient.Patient)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class QuestionnaireGroup(fhirelement.FHIRElement):
    """ Grouped questions.
    
    A group of questions to a possibly similarly grouped set of questions in
    the questionnaire.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.group = None
        """ Nested questionnaire group.
        List of `QuestionnaireGroupGroup` items (represented as `dict` in JSON). """
        
        self.header = None
        """ Text that is displayed above the contents of the group.
        Type `str`. """
        
        self.name = None
        """ Code or name of the section on a questionnaire.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.question = None
        """ Questions in this group.
        List of `QuestionnaireGroupQuestion` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ The subject this group's answers are about.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.text = None
        """ Additional text for the group.
        Type `str`. """
        
        super(QuestionnaireGroup, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(QuestionnaireGroup, self).update_with_json(jsondict)
        if 'group' in jsondict:
            self.group = QuestionnaireGroupGroup.with_json(jsondict['group'])
        if 'header' in jsondict:
            self.header = jsondict['header']
        if 'name' in jsondict:
            self.name = codeableconcept.CodeableConcept.with_json(jsondict['name'])
        if 'question' in jsondict:
            self.question = QuestionnaireGroupQuestion.with_json(jsondict['question'])
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, fhirresource.FHIRResource)
        if 'text' in jsondict:
            self.text = jsondict['text']


class QuestionnaireGroupGroup(fhirelement.FHIRElement):
    """ Nested questionnaire group.
    
    A sub-group within a group. The ordering of groups within this group is
    relevant.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(QuestionnaireGroupGroup, self).__init__(jsondict)


class QuestionnaireGroupQuestion(fhirelement.FHIRElement):
    """ Questions in this group.
    
    Set of questions within this group. The order of questions within the group
    is relevant.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.answerBoolean = False
        """ Single-valued answer to the question.
        Type `bool`. """
        
        self.answerDate = None
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDateTime = None
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDecimal = None
        """ Single-valued answer to the question.
        Type `float`. """
        
        self.answerInstant = None
        """ Single-valued answer to the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerInteger = None
        """ Single-valued answer to the question.
        Type `int`. """
        
        self.answerString = None
        """ Single-valued answer to the question.
        Type `str`. """
        
        self.choice = None
        """ Selected options.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.data = None
        """ Structured answer.
        Type `FHIRElement` (represented as `dict` in JSON). """
        
        self.group = None
        """ Nested questionnaire group.
        List of `QuestionnaireGroupQuestionGroup` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Code or name of the question.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.options = None
        """ Valueset containing the possible options.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.remarks = None
        """ Remarks about the answer given.
        Type `str`. """
        
        self.text = None
        """ Text of the question as it is shown to the user.
        Type `str`. """
        
        super(QuestionnaireGroupQuestion, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(QuestionnaireGroupQuestion, self).update_with_json(jsondict)
        if 'answerBoolean' in jsondict:
            self.answerBoolean = jsondict['answerBoolean']
        if 'answerDate' in jsondict:
            self.answerDate = fhirdate.FHIRDate.with_json(jsondict['answerDate'])
        if 'answerDateTime' in jsondict:
            self.answerDateTime = fhirdate.FHIRDate.with_json(jsondict['answerDateTime'])
        if 'answerDecimal' in jsondict:
            self.answerDecimal = jsondict['answerDecimal']
        if 'answerInstant' in jsondict:
            self.answerInstant = fhirdate.FHIRDate.with_json(jsondict['answerInstant'])
        if 'answerInteger' in jsondict:
            self.answerInteger = jsondict['answerInteger']
        if 'answerString' in jsondict:
            self.answerString = jsondict['answerString']
        if 'choice' in jsondict:
            self.choice = coding.Coding.with_json(jsondict['choice'])
        if 'data' in jsondict:
            self.data = fhirelement.FHIRElement.with_json(jsondict['data'])
        if 'group' in jsondict:
            self.group = QuestionnaireGroupQuestionGroup.with_json(jsondict['group'])
        if 'name' in jsondict:
            self.name = codeableconcept.CodeableConcept.with_json(jsondict['name'])
        if 'options' in jsondict:
            self.options = fhirreference.FHIRReference.with_json_and_owner(jsondict['options'], self, valueset.ValueSet)
        if 'remarks' in jsondict:
            self.remarks = jsondict['remarks']
        if 'text' in jsondict:
            self.text = jsondict['text']


class QuestionnaireGroupQuestionGroup(fhirelement.FHIRElement):
    """ Nested questionnaire group.
    
    Nested group, containing nested question for this question. The order of
    groups within the question is relevant.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(QuestionnaireGroupQuestionGroup, self).__init__(jsondict)

