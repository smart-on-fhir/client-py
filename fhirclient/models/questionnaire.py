#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import contactpoint
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier


class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.
    
    A structured set of questions intended to guide the collection of answers.
    The questions are ordered and grouped into coherent subsets, corresponding
    to the structure of the grouping of the underlying questions.
    """
    
    resource_name = "Questionnaire"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ Date this version was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.group = None
        """ Grouped questions.
        Type `QuestionnaireGroup` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Organization/individual who designed the questionnaire.
        Type `str`. """
        
        self.status = None
        """ draft | published | retired.
        Type `str`. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of Questionnaire.
        Type `str`. """
        
        super(Questionnaire, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Questionnaire, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'group' in jsondict:
            self.group = QuestionnaireGroup.with_json_and_owner(jsondict['group'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'version' in jsondict:
            self.version = jsondict['version']


class QuestionnaireGroup(fhirelement.FHIRElement):
    """ Grouped questions.
    
    A collection of related questions (or further groupings of questions).
    """
    
    resource_name = "QuestionnaireGroup"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.concept = None
        """ Concept that represents this section on a questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.group = None
        """ Grouped questions.
        List of `QuestionnaireGroup` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ To link questionnaire with questionnaire answers.
        Type `str`. """
        
        self.question = None
        """ Questions in this group.
        List of `QuestionnaireGroupQuestion` items (represented as `dict` in JSON). """
        
        self.repeats = False
        """ Whether the group may repeat.
        Type `bool`. """
        
        self.required = False
        """ Must group be included in data results?.
        Type `bool`. """
        
        self.text = None
        """ Additional text for the group.
        Type `str`. """
        
        self.title = None
        """ Name to be displayed for group.
        Type `str`. """
        
        super(QuestionnaireGroup, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(QuestionnaireGroup, self).update_with_json(jsondict)
        if 'concept' in jsondict:
            self.concept = coding.Coding.with_json_and_owner(jsondict['concept'], self)
        if 'group' in jsondict:
            self.group = QuestionnaireGroup.with_json_and_owner(jsondict['group'], self)
        if 'linkId' in jsondict:
            self.linkId = jsondict['linkId']
        if 'question' in jsondict:
            self.question = QuestionnaireGroupQuestion.with_json_and_owner(jsondict['question'], self)
        if 'repeats' in jsondict:
            self.repeats = jsondict['repeats']
        if 'required' in jsondict:
            self.required = jsondict['required']
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'title' in jsondict:
            self.title = jsondict['title']


class QuestionnaireGroupQuestion(fhirelement.FHIRElement):
    """ Questions in this group.
    
    Set of questions within this group. The order of questions within the group
    is relevant.
    """
    
    resource_name = "QuestionnaireGroupQuestion"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.concept = None
        """ Concept that represents this question on a questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.group = None
        """ Grouped questions.
        List of `QuestionnaireGroup` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ To link questionnaire with questionnaire answers.
        Type `str`. """
        
        self.options = None
        """ Valueset containing the possible options.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.repeats = False
        """ Can question  have multiple answers?.
        Type `bool`. """
        
        self.required = False
        """ Must question be answered in data results?.
        Type `bool`. """
        
        self.text = None
        """ Text of the question as it is shown to the user.
        Type `str`. """
        
        self.type = None
        """ boolean | decimal | integer | date | dateTime +.
        Type `str`. """
        
        super(QuestionnaireGroupQuestion, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(QuestionnaireGroupQuestion, self).update_with_json(jsondict)
        if 'concept' in jsondict:
            self.concept = coding.Coding.with_json_and_owner(jsondict['concept'], self)
        if 'group' in jsondict:
            self.group = QuestionnaireGroup.with_json_and_owner(jsondict['group'], self)
        if 'linkId' in jsondict:
            self.linkId = jsondict['linkId']
        if 'options' in jsondict:
            self.options = fhirreference.FHIRReference.with_json_and_owner(jsondict['options'], self)
        if 'repeats' in jsondict:
            self.repeats = jsondict['repeats']
        if 'required' in jsondict:
            self.required = jsondict['required']
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'type' in jsondict:
            self.type = jsondict['type']

