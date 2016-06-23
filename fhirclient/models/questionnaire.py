#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.
    
    A structured set of questions intended to guide the collection of answers.
    The questions are ordered and grouped into coherent subsets, corresponding
    to the structure of the grouping of the underlying questions.
    """
    
    resource_name = "Questionnaire"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("group", "group", QuestionnaireGroup, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectType", "subjectType", str, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireGroup(backboneelement.BackboneElement):
    """ Grouped questions.
    
    A collection of related questions (or further groupings of questions).
    """
    
    resource_name = "QuestionnaireGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(QuestionnaireGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireGroup, self).elementProperties()
        js.extend([
            ("concept", "concept", coding.Coding, True, None, False),
            ("group", "group", QuestionnaireGroup, True, None, False),
            ("linkId", "linkId", str, False, None, False),
            ("question", "question", QuestionnaireGroupQuestion, True, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("required", "required", bool, False, None, False),
            ("text", "text", str, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


class QuestionnaireGroupQuestion(backboneelement.BackboneElement):
    """ Questions in this group.
    
    Set of questions within this group. The order of questions within the group
    is relevant.
    """
    
    resource_name = "QuestionnaireGroupQuestion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(QuestionnaireGroupQuestion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireGroupQuestion, self).elementProperties()
        js.extend([
            ("concept", "concept", coding.Coding, True, None, False),
            ("group", "group", QuestionnaireGroup, True, None, False),
            ("linkId", "linkId", str, False, None, False),
            ("option", "option", coding.Coding, True, None, False),
            ("options", "options", fhirreference.FHIRReference, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("required", "required", bool, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
