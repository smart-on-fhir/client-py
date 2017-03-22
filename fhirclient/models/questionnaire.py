#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Questionnaire) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.
    
    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """
    
    resource_type = "Questionnaire"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ When the questionnaire was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.code = None
        """ Concept that represents the overall questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the questionnaire.
        Type `str`. """
        
        self.effectivePeriod = None
        """ When the questionnaire is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Additional identifier for the questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Questions and sections within the Questionnaire.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for questionnaire (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ When the questionnaire was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this questionnaire (computer friendly).
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Why this questionnaire is defined.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.subjectType = None
        """ Resource that can be subject of QuestionnaireResponse.
        List of `str` items. """
        
        self.title = None
        """ Name for this questionnaire (human friendly).
        Type `str`. """
        
        self.url = None
        """ Logical URI to reference this questionnaire (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the questionnaire.
        Type `str`. """
        
        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectType", "subjectType", str, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.
    
    A particular question, question grouping or display text that is part of
    the questionnaire.
    """
    
    resource_type = "QuestionnaireItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Corresponding concept for this item in a terminology.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ ElementDefinition - details for the item.
        Type `str`. """
        
        self.enableWhen = None
        """ Only allow data when.
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
            ("code", "code", coding.Coding, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, True, None, False),
            ("initialAttachment", "initialAttachment", attachment.Attachment, False, "initial", False),
            ("initialBoolean", "initialBoolean", bool, False, "initial", False),
            ("initialCoding", "initialCoding", coding.Coding, False, "initial", False),
            ("initialDate", "initialDate", fhirdate.FHIRDate, False, "initial", False),
            ("initialDateTime", "initialDateTime", fhirdate.FHIRDate, False, "initial", False),
            ("initialDecimal", "initialDecimal", float, False, "initial", False),
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
            ("type", "type", str, False, None, True),
        ])
        return js


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ Only allow data when.
    
    A constraint indicating that this item should only be enabled
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
    
    One of the permitted answers for a "choice" or "open-choice" question.
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


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
