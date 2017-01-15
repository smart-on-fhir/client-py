#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2017-01-15.
#  2017, SMART Health IT.


from . import domainresource

class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.
    
    A structured set of questions intended to guide the collection of answers.
    The questions are ordered and grouped into coherent subsets, corresponding
    to the structure of the grouping of the underlying questions.
    """
    
    resource_type = "Questionnaire"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        self.url = None
        """ Globally unique logical identifier for  questionnaire.
        Type `str`. """
        
        self.useContext = None
        """ Questionnaire intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical identifier for this version of Questionnaire.
        Type `str`. """
        
        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)
    
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
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.
    
    The questions and groupings of questions that make up the questionnaire.
    """
    
    resource_type = "QuestionnaireItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.concept = None
        """ Concept that represents this item within in a questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ ElementDefinition - details for the item.
        Type `str`. """
        
        self.enableWhen = None
        """ Only allow data when:.
        List of `QuestionnaireItemEnableWhen` items (represented as `dict` in JSON). """
        
        self.initialAttachment = None
        """ Default value when item is first rendered.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.initialBoolean = None
        """ Default value when item is first rendered.
        Type `bool`. """
        
        self.initialCoding = None
        """ Default value when item is first rendered.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.initialDate = None
        """ Default value when item is first rendered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.initialDateTime = None
        """ Default value when item is first rendered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.initialDecimal = None
        """ Default value when item is first rendered.
        Type `float`. """
        
        self.initialInstant = None
        """ Default value when item is first rendered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.initialInteger = None
        """ Default value when item is first rendered.
        Type `int`. """
        
        self.initialQuantity = None
        """ Default value when item is first rendered.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.initialReference = None
        """ Default value when item is first rendered.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.initialString = None
        """ Default value when item is first rendered.
        Type `str`. """
        
        self.initialTime = None
        """ Default value when item is first rendered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.initialUri = None
        """ Default value when item is first rendered.
        Type `str`. """
        
        self.item = None
        """ Nested questionnaire items.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ Unique id for item in questionnaire.
        Type `str`. """
        
        self.maxLength = None
        """ No more than this many characters.
        Type `int`. """
        
        self.option = None
        """ Permitted answer.
        List of `QuestionnaireItemOption` items (represented as `dict` in JSON). """
        
        self.options = None
        """ Valueset containing permitted answers.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.prefix = None
        """ E.g. "1(a)", "2.5.3".
        Type `str`. """
        
        self.readOnly = None
        """ Don't allow human editing.
        Type `bool`. """
        
        self.repeats = None
        """ Whether the item may repeat.
        Type `bool`. """
        
        self.required = None
        """ Whether the item must be included in data results.
        Type `bool`. """
        
        self.text = None
        """ Primary text for the item.
        Type `str`. """
        
        self.type = None
        """ group | display | boolean | decimal | integer | date | dateTime +.
        Type `str`. """
        
        super(QuestionnaireItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("concept", "concept", coding.Coding, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, True, None, False),
            ("initialAttachment", "initialAttachment", attachment.Attachment, False, "initial", False),
            ("initialBoolean", "initialBoolean", bool, False, "initial", False),
            ("initialCoding", "initialCoding", coding.Coding, False, "initial", False),
            ("initialDate", "initialDate", fhirdate.FHIRDate, False, "initial", False),
            ("initialDateTime", "initialDateTime", fhirdate.FHIRDate, False, "initial", False),
            ("initialDecimal", "initialDecimal", float, False, "initial", False),
            ("initialInstant", "initialInstant", fhirdate.FHIRDate, False, "initial", False),
            ("initialInteger", "initialInteger", int, False, "initial", False),
            ("initialQuantity", "initialQuantity", quantity.Quantity, False, "initial", False),
            ("initialReference", "initialReference", fhirreference.FHIRReference, False, "initial", False),
            ("initialString", "initialString", str, False, "initial", False),
            ("initialTime", "initialTime", fhirdate.FHIRDate, False, "initial", False),
            ("initialUri", "initialUri", str, False, "initial", False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("linkId", "linkId", str, False, None, True),
            ("maxLength", "maxLength", int, False, None, False),
            ("option", "option", QuestionnaireItemOption, True, None, False),
            ("options", "options", fhirreference.FHIRReference, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("readOnly", "readOnly", bool, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("required", "required", bool, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ Only allow data when:.
    
    If present, indicates that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """
    
    resource_type = "QuestionnaireItemEnableWhen"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answerAttachment = None
        """ Value question must have.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.answerBoolean = None
        """ Value question must have.
        Type `bool`. """
        
        self.answerCoding = None
        """ Value question must have.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.answerDate = None
        """ Value question must have.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDateTime = None
        """ Value question must have.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDecimal = None
        """ Value question must have.
        Type `float`. """
        
        self.answerInstant = None
        """ Value question must have.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerInteger = None
        """ Value question must have.
        Type `int`. """
        
        self.answerQuantity = None
        """ Value question must have.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.answerReference = None
        """ Value question must have.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.answerString = None
        """ Value question must have.
        Type `str`. """
        
        self.answerTime = None
        """ Value question must have.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerUri = None
        """ Value question must have.
        Type `str`. """
        
        self.hasAnswer = None
        """ Enable when answered or not.
        Type `bool`. """
        
        self.question = None
        """ Question that determines whether item is enabled.
        Type `str`. """
        
        super(QuestionnaireItemEnableWhen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("answerAttachment", "answerAttachment", attachment.Attachment, False, "answer", False),
            ("answerBoolean", "answerBoolean", bool, False, "answer", False),
            ("answerCoding", "answerCoding", coding.Coding, False, "answer", False),
            ("answerDate", "answerDate", fhirdate.FHIRDate, False, "answer", False),
            ("answerDateTime", "answerDateTime", fhirdate.FHIRDate, False, "answer", False),
            ("answerDecimal", "answerDecimal", float, False, "answer", False),
            ("answerInstant", "answerInstant", fhirdate.FHIRDate, False, "answer", False),
            ("answerInteger", "answerInteger", int, False, "answer", False),
            ("answerQuantity", "answerQuantity", quantity.Quantity, False, "answer", False),
            ("answerReference", "answerReference", fhirreference.FHIRReference, False, "answer", False),
            ("answerString", "answerString", str, False, "answer", False),
            ("answerTime", "answerTime", fhirdate.FHIRDate, False, "answer", False),
            ("answerUri", "answerUri", str, False, "answer", False),
            ("hasAnswer", "hasAnswer", bool, False, None, False),
            ("question", "question", str, False, None, True),
        ])
        return js


class QuestionnaireItemOption(backboneelement.BackboneElement):
    """ Permitted answer.
    
    For a "choice" question, identifies one of the permitted answers for the
    question.
    """
    
    resource_type = "QuestionnaireItemOption"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueCoding = None
        """ Answer value.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ Answer value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Answer value.
        Type `int`. """
        
        self.valueString = None
        """ Answer value.
        Type `str`. """
        
        self.valueTime = None
        """ Answer value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(QuestionnaireItemOption, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemOption, self).elementProperties()
        js.extend([
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
