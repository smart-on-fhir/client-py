#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (questionnaire.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import address
import attachment
import codeableconcept
import coding
import contact
import encounter
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import humanname
import identifier
import narrative
import patient
import period
import practitioner
import quantity
import range
import ratio
import schedule
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
        
        self.dataAddress = None
        """ Structured answer.
        Type `Address` (represented as `dict` in JSON). """
        
        self.dataAttachment = None
        """ Structured answer.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.dataBase64Binary = None
        """ Structured answer.
        Type `str`. """
        
        self.dataBoolean = False
        """ Structured answer.
        Type `bool`. """
        
        self.dataCode = None
        """ Structured answer.
        Type `str`. """
        
        self.dataCodeableConcept = None
        """ Structured answer.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dataCoding = None
        """ Structured answer.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.dataContact = None
        """ Structured answer.
        Type `Contact` (represented as `dict` in JSON). """
        
        self.dataDate = None
        """ Structured answer.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dataDateTime = None
        """ Structured answer.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dataDecimal = None
        """ Structured answer.
        Type `float`. """
        
        self.dataHumanName = None
        """ Structured answer.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.dataIdentifier = None
        """ Structured answer.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.dataInstant = None
        """ Structured answer.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dataInteger = None
        """ Structured answer.
        Type `int`. """
        
        self.dataPeriod = None
        """ Structured answer.
        Type `Period` (represented as `dict` in JSON). """
        
        self.dataQuantity = None
        """ Structured answer.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.dataRange = None
        """ Structured answer.
        Type `Range` (represented as `dict` in JSON). """
        
        self.dataRatio = None
        """ Structured answer.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.dataResource = None
        """ Structured answer.
        Type `FHIRResource` (represented as `dict` in JSON). """
        
        self.dataSchedule = None
        """ Structured answer.
        Type `Schedule` (represented as `dict` in JSON). """
        
        self.dataString = None
        """ Structured answer.
        Type `str`. """
        
        self.dataUri = None
        """ Structured answer.
        Type `str`. """
        
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
        if 'dataAddress' in jsondict:
            self.dataAddress = address.Address.with_json(jsondict['dataAddress'])
        if 'dataAttachment' in jsondict:
            self.dataAttachment = attachment.Attachment.with_json(jsondict['dataAttachment'])
        if 'dataBase64Binary' in jsondict:
            self.dataBase64Binary = jsondict['dataBase64Binary']
        if 'dataBoolean' in jsondict:
            self.dataBoolean = jsondict['dataBoolean']
        if 'dataCode' in jsondict:
            self.dataCode = jsondict['dataCode']
        if 'dataCodeableConcept' in jsondict:
            self.dataCodeableConcept = codeableconcept.CodeableConcept.with_json(jsondict['dataCodeableConcept'])
        if 'dataCoding' in jsondict:
            self.dataCoding = coding.Coding.with_json(jsondict['dataCoding'])
        if 'dataContact' in jsondict:
            self.dataContact = contact.Contact.with_json(jsondict['dataContact'])
        if 'dataDate' in jsondict:
            self.dataDate = fhirdate.FHIRDate.with_json(jsondict['dataDate'])
        if 'dataDateTime' in jsondict:
            self.dataDateTime = fhirdate.FHIRDate.with_json(jsondict['dataDateTime'])
        if 'dataDecimal' in jsondict:
            self.dataDecimal = jsondict['dataDecimal']
        if 'dataHumanName' in jsondict:
            self.dataHumanName = humanname.HumanName.with_json(jsondict['dataHumanName'])
        if 'dataIdentifier' in jsondict:
            self.dataIdentifier = identifier.Identifier.with_json(jsondict['dataIdentifier'])
        if 'dataInstant' in jsondict:
            self.dataInstant = fhirdate.FHIRDate.with_json(jsondict['dataInstant'])
        if 'dataInteger' in jsondict:
            self.dataInteger = jsondict['dataInteger']
        if 'dataPeriod' in jsondict:
            self.dataPeriod = period.Period.with_json(jsondict['dataPeriod'])
        if 'dataQuantity' in jsondict:
            self.dataQuantity = quantity.Quantity.with_json(jsondict['dataQuantity'])
        if 'dataRange' in jsondict:
            self.dataRange = range.Range.with_json(jsondict['dataRange'])
        if 'dataRatio' in jsondict:
            self.dataRatio = ratio.Ratio.with_json(jsondict['dataRatio'])
        if 'dataResource' in jsondict:
            self.dataResource = fhirresource.FHIRResource.with_json(jsondict['dataResource'])
        if 'dataSchedule' in jsondict:
            self.dataSchedule = schedule.Schedule.with_json(jsondict['dataSchedule'])
        if 'dataString' in jsondict:
            self.dataString = jsondict['dataString']
        if 'dataUri' in jsondict:
            self.dataUri = jsondict['dataUri']
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

