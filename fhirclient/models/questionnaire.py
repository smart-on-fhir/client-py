#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

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
        
        self.concept = None
        """ Concept that represents the overall questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date this version was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ External identifiers for this questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Questions and sections within the Questionnaire.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
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
        
        self.title = None
        """ Name for the questionnaire.
        Type `str`. """
        
        self.version = None
        """ Logical identifier for this version of Questionnaire.
        Type `str`. """
        
        super(Questionnaire, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("concept", "concept", coding.Coding, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectType", "subjectType", str, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("title", "title", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.
    
    The questions and groupings of questions that make up the questionnaire.
    """
    
    resource_name = "QuestionnaireItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.concept = None
        """ Concept that represents this item within in a questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Nested questionnaire items.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
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
        """ Whether the group may repeat.
        Type `bool`. """
        
        self.required = None
        """ Whether the group must be included in data results.
        Type `bool`. """
        
        self.text = None
        """ Primary text for the item.
        Type `str`. """
        
        self.type = None
        """ group | display | boolean | decimal | integer | date | dateTime +.
        Type `str`. """
        
        super(QuestionnaireItem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("concept", "concept", coding.Coding, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("linkId", "linkId", str, False, None, False),
            ("option", "option", coding.Coding, True, None, False),
            ("options", "options", fhirreference.FHIRReference, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("required", "required", bool, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
