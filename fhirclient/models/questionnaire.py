#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2015-09-24.
#  2015, SMART Health IT.


from . import coding
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


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
        """ External identifiers for this questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Organization/individual who designed the questionnaire.
        Type `str`. """
        
        self.status = None
        """ draft | published | retired.
        Type `str`. """
        
        self.subjectType = None
        """ Resource that can be subject of QuestionnaireResponse.
        List of `str` items. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical identifier for this version of Questionnaire.
        Type `str`. """
        
        super(Questionnaire, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False),
            ("group", "group", QuestionnaireGroup, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("publisher", "publisher", str, False),
            ("status", "status", str, False),
            ("subjectType", "subjectType", str, True),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
            ("version", "version", str, False),
        ])
        return js


class QuestionnaireGroup(fhirelement.FHIRElement):
    """ Grouped questions.
    
    A collection of related questions (or further groupings of questions).
    """
    
    resource_name = "QuestionnaireGroup"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.concept = None
        """ Concept that represents this section in a questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.group = None
        """ Nested questionnaire group.
        List of `QuestionnaireGroup` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ To link questionnaire with questionnaire response.
        Type `str`. """
        
        self.question = None
        """ Questions in this group.
        List of `QuestionnaireGroupQuestion` items (represented as `dict` in JSON). """
        
        self.repeats = None
        """ Whether the group may repeat.
        Type `bool`. """
        
        self.required = None
        """ Whether the group must be included in data results.
        Type `bool`. """
        
        self.text = None
        """ Additional text for the group.
        Type `str`. """
        
        self.title = None
        """ Name to be displayed for group.
        Type `str`. """
        
        super(QuestionnaireGroup, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(QuestionnaireGroup, self).elementProperties()
        js.extend([
            ("concept", "concept", coding.Coding, True),
            ("group", "group", QuestionnaireGroup, True),
            ("linkId", "linkId", str, False),
            ("question", "question", QuestionnaireGroupQuestion, True),
            ("repeats", "repeats", bool, False),
            ("required", "required", bool, False),
            ("text", "text", str, False),
            ("title", "title", str, False),
        ])
        return js


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
        """ Nested questionnaire group.
        List of `QuestionnaireGroup` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ To link questionnaire with questionnaire response.
        Type `str`. """
        
        self.option = None
        """ Permitted answer.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.options = None
        """ Valueset containing permitted answers.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.repeats = None
        """ Whether the question  can have multiple answers.
        Type `bool`. """
        
        self.required = None
        """ Whether the question must be answered in data results.
        Type `bool`. """
        
        self.text = None
        """ Text of the question as it is shown to the user.
        Type `str`. """
        
        self.type = None
        """ boolean | decimal | integer | date | dateTime +.
        Type `str`. """
        
        super(QuestionnaireGroupQuestion, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(QuestionnaireGroupQuestion, self).elementProperties()
        js.extend([
            ("concept", "concept", coding.Coding, True),
            ("group", "group", QuestionnaireGroup, True),
            ("linkId", "linkId", str, False),
            ("option", "option", coding.Coding, True),
            ("options", "options", fhirreference.FHIRReference, False),
            ("repeats", "repeats", bool, False),
            ("required", "required", bool, False),
            ("text", "text", str, False),
            ("type", "type", str, False),
        ])
        return js

