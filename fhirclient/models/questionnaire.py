# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Questionnaire).
# 2024, SMART Health IT.


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
        self._approvalDate = None
        """ Primitive extension for approvalDate. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Concept that represents the overall questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        self._copyright = None
        """ Primitive extension for copyright. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.derivedFrom = None
        """ Instantiates protocol or definition.
        List of `str` items. """
        self._derivedFrom = None
        """ Primitive extension for derivedFrom. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the questionnaire.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ When the questionnaire is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Questions and sections within the Questionnaire.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for questionnaire (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.lastReviewDate = None
        """ When the questionnaire was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._lastReviewDate = None
        """ Primitive extension for lastReviewDate. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this questionnaire (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this questionnaire is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subjectType = None
        """ Resource that can be subject of QuestionnaireResponse.
        List of `str` items. """
        self._subjectType = None
        """ Primitive extension for subjectType. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this questionnaire (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this questionnaire, represented as a URI
        (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the questionnaire.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("_approvalDate", "_approvalDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("derivedFrom", "derivedFrom", str, True, None, False),
            ("_derivedFrom", "_derivedFrom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("_lastReviewDate", "_lastReviewDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectType", "subjectType", str, True, None, False),
            ("_subjectType", "_subjectType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        
        self.answerOption = None
        """ Permitted answer.
        List of `QuestionnaireItemAnswerOption` items (represented as `dict` in JSON). """
        self._answerOption = None
        """ Primitive extension for answerOption. Type `FHIRPrimitiveExtension` """
        
        self.answerValueSet = None
        """ Valueset containing permitted answers.
        Type `str`. """
        self._answerValueSet = None
        """ Primitive extension for answerValueSet. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Corresponding concept for this item in a terminology.
        List of `Coding` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.definition = None
        """ ElementDefinition - details for the item.
        Type `str`. """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.enableBehavior = None
        """ all | any.
        Type `str`. """
        self._enableBehavior = None
        """ Primitive extension for enableBehavior. Type `FHIRPrimitiveExtension` """
        
        self.enableWhen = None
        """ Only allow data when.
        List of `QuestionnaireItemEnableWhen` items (represented as `dict` in JSON). """
        self._enableWhen = None
        """ Primitive extension for enableWhen. Type `FHIRPrimitiveExtension` """
        
        self.initial = None
        """ Initial value(s) when item is first rendered.
        List of `QuestionnaireItemInitial` items (represented as `dict` in JSON). """
        self._initial = None
        """ Primitive extension for initial. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Nested questionnaire items.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        self.linkId = None
        """ Unique id for item in questionnaire.
        Type `str`. """
        self._linkId = None
        """ Primitive extension for linkId. Type `FHIRPrimitiveExtension` """
        
        self.maxLength = None
        """ No more than this many characters.
        Type `int`. """
        self._maxLength = None
        """ Primitive extension for maxLength. Type `FHIRPrimitiveExtension` """
        
        self.prefix = None
        """ E.g. "1(a)", "2.5.3".
        Type `str`. """
        self._prefix = None
        """ Primitive extension for prefix. Type `FHIRPrimitiveExtension` """
        
        self.readOnly = None
        """ Don't allow human editing.
        Type `bool`. """
        self._readOnly = None
        """ Primitive extension for readOnly. Type `FHIRPrimitiveExtension` """
        
        self.repeats = None
        """ Whether the item may repeat.
        Type `bool`. """
        self._repeats = None
        """ Primitive extension for repeats. Type `FHIRPrimitiveExtension` """
        
        self.required = None
        """ Whether the item must be included in data results.
        Type `bool`. """
        self._required = None
        """ Primitive extension for required. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Primary text for the item.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ group | display | boolean | decimal | integer | date | dateTime +.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(QuestionnaireItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("answerOption", "answerOption", QuestionnaireItemAnswerOption, True, None, False),
            ("_answerOption", "_answerOption", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerValueSet", "answerValueSet", str, False, None, False),
            ("_answerValueSet", "_answerValueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enableBehavior", "enableBehavior", str, False, None, False),
            ("_enableBehavior", "_enableBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, True, None, False),
            ("_enableWhen", "_enableWhen", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("initial", "initial", QuestionnaireItemInitial, True, None, False),
            ("_initial", "_initial", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("linkId", "linkId", str, False, None, True),
            ("_linkId", "_linkId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("_maxLength", "_maxLength", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("_prefix", "_prefix", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("readOnly", "readOnly", bool, False, None, False),
            ("_readOnly", "_readOnly", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("_repeats", "_repeats", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("required", "required", bool, False, None, False),
            ("_required", "_required", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """ Permitted answer.
    
    One of the permitted answers for a "choice" or "open-choice" question.
    """
    
    resource_type = "QuestionnaireItemAnswerOption"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.initialSelected = None
        """ Whether option is selected by default.
        Type `bool`. """
        self._initialSelected = None
        """ Primitive extension for initialSelected. Type `FHIRPrimitiveExtension` """
        
        self.valueCoding = None
        """ Answer value.
        Type `Coding` (represented as `dict` in JSON). """
        self._valueCoding = None
        """ Primitive extension for valueCoding. Type `FHIRPrimitiveExtension` """
        
        self.valueDate = None
        """ Answer value.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._valueDate = None
        """ Primitive extension for valueDate. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Answer value.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ Answer value.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Answer value.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ Answer value.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        super(QuestionnaireItemAnswerOption, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemAnswerOption, self).elementProperties()
        js.extend([
            ("initialSelected", "initialSelected", bool, False, None, False),
            ("_initialSelected", "_initialSelected", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("_valueCoding", "_valueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("_valueDate", "_valueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("_valueReference", "_valueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
            ("_valueTime", "_valueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        
        self.answerBoolean = None
        """ Value for question comparison based on operator.
        Type `bool`. """
        self._answerBoolean = None
        """ Primitive extension for answerBoolean. Type `FHIRPrimitiveExtension` """
        
        self.answerCoding = None
        """ Value for question comparison based on operator.
        Type `Coding` (represented as `dict` in JSON). """
        self._answerCoding = None
        """ Primitive extension for answerCoding. Type `FHIRPrimitiveExtension` """
        
        self.answerDate = None
        """ Value for question comparison based on operator.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._answerDate = None
        """ Primitive extension for answerDate. Type `FHIRPrimitiveExtension` """
        
        self.answerDateTime = None
        """ Value for question comparison based on operator.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._answerDateTime = None
        """ Primitive extension for answerDateTime. Type `FHIRPrimitiveExtension` """
        
        self.answerDecimal = None
        """ Value for question comparison based on operator.
        Type `float`. """
        self._answerDecimal = None
        """ Primitive extension for answerDecimal. Type `FHIRPrimitiveExtension` """
        
        self.answerInteger = None
        """ Value for question comparison based on operator.
        Type `int`. """
        self._answerInteger = None
        """ Primitive extension for answerInteger. Type `FHIRPrimitiveExtension` """
        
        self.answerQuantity = None
        """ Value for question comparison based on operator.
        Type `Quantity` (represented as `dict` in JSON). """
        self._answerQuantity = None
        """ Primitive extension for answerQuantity. Type `FHIRPrimitiveExtension` """
        
        self.answerReference = None
        """ Value for question comparison based on operator.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._answerReference = None
        """ Primitive extension for answerReference. Type `FHIRPrimitiveExtension` """
        
        self.answerString = None
        """ Value for question comparison based on operator.
        Type `str`. """
        self._answerString = None
        """ Primitive extension for answerString. Type `FHIRPrimitiveExtension` """
        
        self.answerTime = None
        """ Value for question comparison based on operator.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._answerTime = None
        """ Primitive extension for answerTime. Type `FHIRPrimitiveExtension` """
        
        self.operator = None
        """ exists | = | != | > | < | >= | <=.
        Type `str`. """
        self._operator = None
        """ Primitive extension for operator. Type `FHIRPrimitiveExtension` """
        
        self.question = None
        """ Question that determines whether item is enabled.
        Type `str`. """
        self._question = None
        """ Primitive extension for question. Type `FHIRPrimitiveExtension` """
        
        super(QuestionnaireItemEnableWhen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("answerBoolean", "answerBoolean", bool, False, "answer", True),
            ("_answerBoolean", "_answerBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerCoding", "answerCoding", coding.Coding, False, "answer", True),
            ("_answerCoding", "_answerCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerDate", "answerDate", fhirdate.FHIRDate, False, "answer", True),
            ("_answerDate", "_answerDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerDateTime", "answerDateTime", fhirdatetime.FHIRDateTime, False, "answer", True),
            ("_answerDateTime", "_answerDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerDecimal", "answerDecimal", float, False, "answer", True),
            ("_answerDecimal", "_answerDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerInteger", "answerInteger", int, False, "answer", True),
            ("_answerInteger", "_answerInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerQuantity", "answerQuantity", quantity.Quantity, False, "answer", True),
            ("_answerQuantity", "_answerQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerReference", "answerReference", fhirreference.FHIRReference, False, "answer", True),
            ("_answerReference", "_answerReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerString", "answerString", str, False, "answer", True),
            ("_answerString", "_answerString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("answerTime", "answerTime", fhirtime.FHIRTime, False, "answer", True),
            ("_answerTime", "_answerTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operator", "operator", str, False, None, True),
            ("_operator", "_operator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("question", "question", str, False, None, True),
            ("_question", "_question", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """ Initial value(s) when item is first rendered.
    
    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """
    
    resource_type = "QuestionnaireItemInitial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueAttachment = None
        """ Actual value for initializing the question.
        Type `Attachment` (represented as `dict` in JSON). """
        self._valueAttachment = None
        """ Primitive extension for valueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Actual value for initializing the question.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCoding = None
        """ Actual value for initializing the question.
        Type `Coding` (represented as `dict` in JSON). """
        self._valueCoding = None
        """ Primitive extension for valueCoding. Type `FHIRPrimitiveExtension` """
        
        self.valueDate = None
        """ Actual value for initializing the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._valueDate = None
        """ Primitive extension for valueDate. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ Actual value for initializing the question.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ Actual value for initializing the question.
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Actual value for initializing the question.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Actual value for initializing the question.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ Actual value for initializing the question.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Actual value for initializing the question.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ Actual value for initializing the question.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        self.valueUri = None
        """ Actual value for initializing the question.
        Type `str`. """
        self._valueUri = None
        """ Primitive extension for valueUri. Type `FHIRPrimitiveExtension` """
        
        super(QuestionnaireItemInitial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(QuestionnaireItemInitial, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("_valueAttachment", "_valueAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("_valueCoding", "_valueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("_valueDate", "_valueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", True),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("_valueReference", "_valueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
            ("_valueTime", "_valueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUri", "valueUri", str, False, "value", True),
            ("_valueUri", "_valueUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import fhirtime
from . import identifier
from . import period
from . import quantity
from . import usagecontext