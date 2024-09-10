# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Task).
# 2024, SMART Health IT.


from . import domainresource

class Task(domainresource.DomainResource):
    """ A task to be performed.
    """
    
    resource_type = "Task"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        """ Task Creation Date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._authoredOn = None
        """ Primitive extension for authoredOn. Type `FHIRPrimitiveExtension` """
        
        self.basedOn = None
        """ Request fulfilled by this task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.businessStatus = None
        """ E.g. "Specimen collected", "IV prepped".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._businessStatus = None
        """ Primitive extension for businessStatus. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Task Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Human-readable explanation of task.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Healthcare event during which this task originated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.executionPeriod = None
        """ Start and end time of execution.
        Type `Period` (represented as `dict` in JSON). """
        self._executionPeriod = None
        """ Primitive extension for executionPeriod. Type `FHIRPrimitiveExtension` """
        
        self.focus = None
        """ What task is acting on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._focus = None
        """ Primitive extension for focus. Type `FHIRPrimitiveExtension` """
        
        self.for_fhir = None
        """ Beneficiary of the Task.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._for_fhir = None
        """ Primitive extension for for_fhir. Type `FHIRPrimitiveExtension` """
        
        self.groupIdentifier = None
        """ Requisition or grouper id.
        Type `Identifier` (represented as `dict` in JSON). """
        self._groupIdentifier = None
        """ Primitive extension for groupIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Task Instance Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.input = None
        """ Information used to perform task.
        List of `TaskInput` items (represented as `dict` in JSON). """
        self._input = None
        """ Primitive extension for input. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesCanonical = None
        """ Formal definition of task.
        Type `str`. """
        self._instantiatesCanonical = None
        """ Primitive extension for instantiatesCanonical. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesUri = None
        """ Formal definition of task.
        Type `str`. """
        self._instantiatesUri = None
        """ Primitive extension for instantiatesUri. Type `FHIRPrimitiveExtension` """
        
        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._insurance = None
        """ Primitive extension for insurance. Type `FHIRPrimitiveExtension` """
        
        self.intent = None
        """ unknown | proposal | plan | order | original-order | reflex-order |
        filler-order | instance-order | option.
        Type `str`. """
        self._intent = None
        """ Primitive extension for intent. Type `FHIRPrimitiveExtension` """
        
        self.lastModified = None
        """ Task Last Modified Date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._lastModified = None
        """ Primitive extension for lastModified. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Where task occurs.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments made about the task.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.output = None
        """ Information produced as part of task.
        List of `TaskOutput` items (represented as `dict` in JSON). """
        self._output = None
        """ Primitive extension for output. Type `FHIRPrimitiveExtension` """
        
        self.owner = None
        """ Responsible individual.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._owner = None
        """ Primitive extension for owner. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Composite task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.performerType = None
        """ Requested performer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._performerType = None
        """ Primitive extension for performerType. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why task is needed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why task is needed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.relevantHistory = None
        """ Key events in history of the Task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._relevantHistory = None
        """ Primitive extension for relevantHistory. Type `FHIRPrimitiveExtension` """
        
        self.requester = None
        """ Who is asking for task to be done.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requester = None
        """ Primitive extension for requester. Type `FHIRPrimitiveExtension` """
        
        self.restriction = None
        """ Constraints on fulfillment tasks.
        Type `TaskRestriction` (represented as `dict` in JSON). """
        self._restriction = None
        """ Primitive extension for restriction. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | requested | received | accepted | +.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        super(Task, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Task, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("_authoredOn", "_authoredOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("businessStatus", "businessStatus", codeableconcept.CodeableConcept, False, None, False),
            ("_businessStatus", "_businessStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("executionPeriod", "executionPeriod", period.Period, False, None, False),
            ("_executionPeriod", "_executionPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("_focus", "_focus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("for_fhir", "for", fhirreference.FHIRReference, False, None, False),
            ("_for_fhir", "_for_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("_groupIdentifier", "_groupIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("input", "input", TaskInput, True, None, False),
            ("_input", "_input", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, False, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("_instantiatesUri", "_instantiatesUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("_insurance", "_insurance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("intent", "intent", str, False, None, True),
            ("_intent", "_intent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lastModified", "lastModified", fhirdatetime.FHIRDateTime, False, None, False),
            ("_lastModified", "_lastModified", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("output", "output", TaskOutput, True, None, False),
            ("_output", "_output", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("_owner", "_owner", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("_performerType", "_performerType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, False, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("_relevantHistory", "_relevantHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("_requester", "_requester", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("restriction", "restriction", TaskRestriction, False, None, False),
            ("_restriction", "_restriction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class TaskInput(backboneelement.BackboneElement):
    """ Information used to perform task.
    
    Additional information that may be needed in the execution of the task.
    """
    
    resource_type = "TaskInput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Label for the input.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.valueAddress = None
        """ Content to use in performing the task.
        Type `Address` (represented as `dict` in JSON). """
        self._valueAddress = None
        """ Primitive extension for valueAddress. Type `FHIRPrimitiveExtension` """
        
        self.valueAge = None
        """ Content to use in performing the task.
        Type `Age` (represented as `dict` in JSON). """
        self._valueAge = None
        """ Primitive extension for valueAge. Type `FHIRPrimitiveExtension` """
        
        self.valueAnnotation = None
        """ Content to use in performing the task.
        Type `Annotation` (represented as `dict` in JSON). """
        self._valueAnnotation = None
        """ Primitive extension for valueAnnotation. Type `FHIRPrimitiveExtension` """
        
        self.valueAttachment = None
        """ Content to use in performing the task.
        Type `Attachment` (represented as `dict` in JSON). """
        self._valueAttachment = None
        """ Primitive extension for valueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.valueBase64Binary = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueBase64Binary = None
        """ Primitive extension for valueBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Content to use in performing the task.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCanonical = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueCanonical = None
        """ Primitive extension for valueCanonical. Type `FHIRPrimitiveExtension` """
        
        self.valueCode = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueCode = None
        """ Primitive extension for valueCode. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Content to use in performing the task.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueCoding = None
        """ Content to use in performing the task.
        Type `Coding` (represented as `dict` in JSON). """
        self._valueCoding = None
        """ Primitive extension for valueCoding. Type `FHIRPrimitiveExtension` """
        
        self.valueContactDetail = None
        """ Content to use in performing the task.
        Type `ContactDetail` (represented as `dict` in JSON). """
        self._valueContactDetail = None
        """ Primitive extension for valueContactDetail. Type `FHIRPrimitiveExtension` """
        
        self.valueContactPoint = None
        """ Content to use in performing the task.
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._valueContactPoint = None
        """ Primitive extension for valueContactPoint. Type `FHIRPrimitiveExtension` """
        
        self.valueContributor = None
        """ Content to use in performing the task.
        Type `Contributor` (represented as `dict` in JSON). """
        self._valueContributor = None
        """ Primitive extension for valueContributor. Type `FHIRPrimitiveExtension` """
        
        self.valueCount = None
        """ Content to use in performing the task.
        Type `Count` (represented as `dict` in JSON). """
        self._valueCount = None
        """ Primitive extension for valueCount. Type `FHIRPrimitiveExtension` """
        
        self.valueDataRequirement = None
        """ Content to use in performing the task.
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._valueDataRequirement = None
        """ Primitive extension for valueDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.valueDate = None
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._valueDate = None
        """ Primitive extension for valueDate. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ Content to use in performing the task.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ Content to use in performing the task.
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueDistance = None
        """ Content to use in performing the task.
        Type `Distance` (represented as `dict` in JSON). """
        self._valueDistance = None
        """ Primitive extension for valueDistance. Type `FHIRPrimitiveExtension` """
        
        self.valueDosage = None
        """ Content to use in performing the task.
        Type `Dosage` (represented as `dict` in JSON). """
        self._valueDosage = None
        """ Primitive extension for valueDosage. Type `FHIRPrimitiveExtension` """
        
        self.valueDuration = None
        """ Content to use in performing the task.
        Type `Duration` (represented as `dict` in JSON). """
        self._valueDuration = None
        """ Primitive extension for valueDuration. Type `FHIRPrimitiveExtension` """
        
        self.valueExpression = None
        """ Content to use in performing the task.
        Type `Expression` (represented as `dict` in JSON). """
        self._valueExpression = None
        """ Primitive extension for valueExpression. Type `FHIRPrimitiveExtension` """
        
        self.valueHumanName = None
        """ Content to use in performing the task.
        Type `HumanName` (represented as `dict` in JSON). """
        self._valueHumanName = None
        """ Primitive extension for valueHumanName. Type `FHIRPrimitiveExtension` """
        
        self.valueId = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueId = None
        """ Primitive extension for valueId. Type `FHIRPrimitiveExtension` """
        
        self.valueIdentifier = None
        """ Content to use in performing the task.
        Type `Identifier` (represented as `dict` in JSON). """
        self._valueIdentifier = None
        """ Primitive extension for valueIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.valueInstant = None
        """ Content to use in performing the task.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._valueInstant = None
        """ Primitive extension for valueInstant. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Content to use in performing the task.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueMarkdown = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueMarkdown = None
        """ Primitive extension for valueMarkdown. Type `FHIRPrimitiveExtension` """
        
        self.valueMeta = None
        """ Content to use in performing the task.
        Type `Meta` (represented as `dict` in JSON). """
        self._valueMeta = None
        """ Primitive extension for valueMeta. Type `FHIRPrimitiveExtension` """
        
        self.valueMoney = None
        """ Content to use in performing the task.
        Type `Money` (represented as `dict` in JSON). """
        self._valueMoney = None
        """ Primitive extension for valueMoney. Type `FHIRPrimitiveExtension` """
        
        self.valueOid = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueOid = None
        """ Primitive extension for valueOid. Type `FHIRPrimitiveExtension` """
        
        self.valueParameterDefinition = None
        """ Content to use in performing the task.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        self._valueParameterDefinition = None
        """ Primitive extension for valueParameterDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valuePeriod = None
        """ Content to use in performing the task.
        Type `Period` (represented as `dict` in JSON). """
        self._valuePeriod = None
        """ Primitive extension for valuePeriod. Type `FHIRPrimitiveExtension` """
        
        self.valuePositiveInt = None
        """ Content to use in performing the task.
        Type `int`. """
        self._valuePositiveInt = None
        """ Primitive extension for valuePositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Content to use in performing the task.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ Content to use in performing the task.
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        self.valueRatio = None
        """ Content to use in performing the task.
        Type `Ratio` (represented as `dict` in JSON). """
        self._valueRatio = None
        """ Primitive extension for valueRatio. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ Content to use in performing the task.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        self.valueRelatedArtifact = None
        """ Content to use in performing the task.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        self._valueRelatedArtifact = None
        """ Primitive extension for valueRelatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.valueSampledData = None
        """ Content to use in performing the task.
        Type `SampledData` (represented as `dict` in JSON). """
        self._valueSampledData = None
        """ Primitive extension for valueSampledData. Type `FHIRPrimitiveExtension` """
        
        self.valueSignature = None
        """ Content to use in performing the task.
        Type `Signature` (represented as `dict` in JSON). """
        self._valueSignature = None
        """ Primitive extension for valueSignature. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ Content to use in performing the task.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        self.valueTiming = None
        """ Content to use in performing the task.
        Type `Timing` (represented as `dict` in JSON). """
        self._valueTiming = None
        """ Primitive extension for valueTiming. Type `FHIRPrimitiveExtension` """
        
        self.valueTriggerDefinition = None
        """ Content to use in performing the task.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        self._valueTriggerDefinition = None
        """ Primitive extension for valueTriggerDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valueUnsignedInt = None
        """ Content to use in performing the task.
        Type `int`. """
        self._valueUnsignedInt = None
        """ Primitive extension for valueUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.valueUri = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueUri = None
        """ Primitive extension for valueUri. Type `FHIRPrimitiveExtension` """
        
        self.valueUrl = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueUrl = None
        """ Primitive extension for valueUrl. Type `FHIRPrimitiveExtension` """
        
        self.valueUsageContext = None
        """ Content to use in performing the task.
        Type `UsageContext` (represented as `dict` in JSON). """
        self._valueUsageContext = None
        """ Primitive extension for valueUsageContext. Type `FHIRPrimitiveExtension` """
        
        self.valueUuid = None
        """ Content to use in performing the task.
        Type `str`. """
        self._valueUuid = None
        """ Primitive extension for valueUuid. Type `FHIRPrimitiveExtension` """
        
        super(TaskInput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskInput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("_valueAddress", "_valueAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("_valueAge", "_valueAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("_valueAnnotation", "_valueAnnotation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("_valueAttachment", "_valueAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("_valueBase64Binary", "_valueBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("_valueCanonical", "_valueCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCode", "valueCode", str, False, "value", True),
            ("_valueCode", "_valueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("_valueCoding", "_valueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("_valueContactDetail", "_valueContactDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("_valueContactPoint", "_valueContactPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("_valueContributor", "_valueContributor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("_valueCount", "_valueCount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("_valueDataRequirement", "_valueDataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("_valueDate", "_valueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", True),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("_valueDistance", "_valueDistance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("_valueDosage", "_valueDosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("_valueDuration", "_valueDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("_valueExpression", "_valueExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("_valueHumanName", "_valueHumanName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueId", "valueId", str, False, "value", True),
            ("_valueId", "_valueId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("_valueIdentifier", "_valueIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInstant", "valueInstant", fhirinstant.FHIRInstant, False, "value", True),
            ("_valueInstant", "_valueInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("_valueMarkdown", "_valueMarkdown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
            ("_valueMeta", "_valueMeta", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("_valueMoney", "_valueMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueOid", "valueOid", str, False, "value", True),
            ("_valueOid", "_valueOid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("_valueParameterDefinition", "_valueParameterDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("_valuePeriod", "_valuePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("_valuePositiveInt", "_valuePositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("_valueRange", "_valueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("_valueRatio", "_valueRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("_valueReference", "_valueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("_valueRelatedArtifact", "_valueRelatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("_valueSampledData", "_valueSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("_valueSignature", "_valueSignature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
            ("_valueTime", "_valueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("_valueTiming", "_valueTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("_valueTriggerDefinition", "_valueTriggerDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("_valueUnsignedInt", "_valueUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUri", "valueUri", str, False, "value", True),
            ("_valueUri", "_valueUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("_valueUrl", "_valueUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("_valueUsageContext", "_valueUsageContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUuid", "valueUuid", str, False, "value", True),
            ("_valueUuid", "_valueUuid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TaskOutput(backboneelement.BackboneElement):
    """ Information produced as part of task.
    
    Outputs produced by the Task.
    """
    
    resource_type = "TaskOutput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Label for output.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.valueAddress = None
        """ Result of output.
        Type `Address` (represented as `dict` in JSON). """
        self._valueAddress = None
        """ Primitive extension for valueAddress. Type `FHIRPrimitiveExtension` """
        
        self.valueAge = None
        """ Result of output.
        Type `Age` (represented as `dict` in JSON). """
        self._valueAge = None
        """ Primitive extension for valueAge. Type `FHIRPrimitiveExtension` """
        
        self.valueAnnotation = None
        """ Result of output.
        Type `Annotation` (represented as `dict` in JSON). """
        self._valueAnnotation = None
        """ Primitive extension for valueAnnotation. Type `FHIRPrimitiveExtension` """
        
        self.valueAttachment = None
        """ Result of output.
        Type `Attachment` (represented as `dict` in JSON). """
        self._valueAttachment = None
        """ Primitive extension for valueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.valueBase64Binary = None
        """ Result of output.
        Type `str`. """
        self._valueBase64Binary = None
        """ Primitive extension for valueBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Result of output.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCanonical = None
        """ Result of output.
        Type `str`. """
        self._valueCanonical = None
        """ Primitive extension for valueCanonical. Type `FHIRPrimitiveExtension` """
        
        self.valueCode = None
        """ Result of output.
        Type `str`. """
        self._valueCode = None
        """ Primitive extension for valueCode. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Result of output.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueCoding = None
        """ Result of output.
        Type `Coding` (represented as `dict` in JSON). """
        self._valueCoding = None
        """ Primitive extension for valueCoding. Type `FHIRPrimitiveExtension` """
        
        self.valueContactDetail = None
        """ Result of output.
        Type `ContactDetail` (represented as `dict` in JSON). """
        self._valueContactDetail = None
        """ Primitive extension for valueContactDetail. Type `FHIRPrimitiveExtension` """
        
        self.valueContactPoint = None
        """ Result of output.
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._valueContactPoint = None
        """ Primitive extension for valueContactPoint. Type `FHIRPrimitiveExtension` """
        
        self.valueContributor = None
        """ Result of output.
        Type `Contributor` (represented as `dict` in JSON). """
        self._valueContributor = None
        """ Primitive extension for valueContributor. Type `FHIRPrimitiveExtension` """
        
        self.valueCount = None
        """ Result of output.
        Type `Count` (represented as `dict` in JSON). """
        self._valueCount = None
        """ Primitive extension for valueCount. Type `FHIRPrimitiveExtension` """
        
        self.valueDataRequirement = None
        """ Result of output.
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._valueDataRequirement = None
        """ Primitive extension for valueDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.valueDate = None
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._valueDate = None
        """ Primitive extension for valueDate. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ Result of output.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ Result of output.
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueDistance = None
        """ Result of output.
        Type `Distance` (represented as `dict` in JSON). """
        self._valueDistance = None
        """ Primitive extension for valueDistance. Type `FHIRPrimitiveExtension` """
        
        self.valueDosage = None
        """ Result of output.
        Type `Dosage` (represented as `dict` in JSON). """
        self._valueDosage = None
        """ Primitive extension for valueDosage. Type `FHIRPrimitiveExtension` """
        
        self.valueDuration = None
        """ Result of output.
        Type `Duration` (represented as `dict` in JSON). """
        self._valueDuration = None
        """ Primitive extension for valueDuration. Type `FHIRPrimitiveExtension` """
        
        self.valueExpression = None
        """ Result of output.
        Type `Expression` (represented as `dict` in JSON). """
        self._valueExpression = None
        """ Primitive extension for valueExpression. Type `FHIRPrimitiveExtension` """
        
        self.valueHumanName = None
        """ Result of output.
        Type `HumanName` (represented as `dict` in JSON). """
        self._valueHumanName = None
        """ Primitive extension for valueHumanName. Type `FHIRPrimitiveExtension` """
        
        self.valueId = None
        """ Result of output.
        Type `str`. """
        self._valueId = None
        """ Primitive extension for valueId. Type `FHIRPrimitiveExtension` """
        
        self.valueIdentifier = None
        """ Result of output.
        Type `Identifier` (represented as `dict` in JSON). """
        self._valueIdentifier = None
        """ Primitive extension for valueIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.valueInstant = None
        """ Result of output.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._valueInstant = None
        """ Primitive extension for valueInstant. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Result of output.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueMarkdown = None
        """ Result of output.
        Type `str`. """
        self._valueMarkdown = None
        """ Primitive extension for valueMarkdown. Type `FHIRPrimitiveExtension` """
        
        self.valueMeta = None
        """ Result of output.
        Type `Meta` (represented as `dict` in JSON). """
        self._valueMeta = None
        """ Primitive extension for valueMeta. Type `FHIRPrimitiveExtension` """
        
        self.valueMoney = None
        """ Result of output.
        Type `Money` (represented as `dict` in JSON). """
        self._valueMoney = None
        """ Primitive extension for valueMoney. Type `FHIRPrimitiveExtension` """
        
        self.valueOid = None
        """ Result of output.
        Type `str`. """
        self._valueOid = None
        """ Primitive extension for valueOid. Type `FHIRPrimitiveExtension` """
        
        self.valueParameterDefinition = None
        """ Result of output.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        self._valueParameterDefinition = None
        """ Primitive extension for valueParameterDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valuePeriod = None
        """ Result of output.
        Type `Period` (represented as `dict` in JSON). """
        self._valuePeriod = None
        """ Primitive extension for valuePeriod. Type `FHIRPrimitiveExtension` """
        
        self.valuePositiveInt = None
        """ Result of output.
        Type `int`. """
        self._valuePositiveInt = None
        """ Primitive extension for valuePositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Result of output.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ Result of output.
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        self.valueRatio = None
        """ Result of output.
        Type `Ratio` (represented as `dict` in JSON). """
        self._valueRatio = None
        """ Primitive extension for valueRatio. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ Result of output.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        self.valueRelatedArtifact = None
        """ Result of output.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        self._valueRelatedArtifact = None
        """ Primitive extension for valueRelatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.valueSampledData = None
        """ Result of output.
        Type `SampledData` (represented as `dict` in JSON). """
        self._valueSampledData = None
        """ Primitive extension for valueSampledData. Type `FHIRPrimitiveExtension` """
        
        self.valueSignature = None
        """ Result of output.
        Type `Signature` (represented as `dict` in JSON). """
        self._valueSignature = None
        """ Primitive extension for valueSignature. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Result of output.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ Result of output.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        self.valueTiming = None
        """ Result of output.
        Type `Timing` (represented as `dict` in JSON). """
        self._valueTiming = None
        """ Primitive extension for valueTiming. Type `FHIRPrimitiveExtension` """
        
        self.valueTriggerDefinition = None
        """ Result of output.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        self._valueTriggerDefinition = None
        """ Primitive extension for valueTriggerDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valueUnsignedInt = None
        """ Result of output.
        Type `int`. """
        self._valueUnsignedInt = None
        """ Primitive extension for valueUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.valueUri = None
        """ Result of output.
        Type `str`. """
        self._valueUri = None
        """ Primitive extension for valueUri. Type `FHIRPrimitiveExtension` """
        
        self.valueUrl = None
        """ Result of output.
        Type `str`. """
        self._valueUrl = None
        """ Primitive extension for valueUrl. Type `FHIRPrimitiveExtension` """
        
        self.valueUsageContext = None
        """ Result of output.
        Type `UsageContext` (represented as `dict` in JSON). """
        self._valueUsageContext = None
        """ Primitive extension for valueUsageContext. Type `FHIRPrimitiveExtension` """
        
        self.valueUuid = None
        """ Result of output.
        Type `str`. """
        self._valueUuid = None
        """ Primitive extension for valueUuid. Type `FHIRPrimitiveExtension` """
        
        super(TaskOutput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskOutput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("_valueAddress", "_valueAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("_valueAge", "_valueAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("_valueAnnotation", "_valueAnnotation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("_valueAttachment", "_valueAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("_valueBase64Binary", "_valueBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("_valueCanonical", "_valueCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCode", "valueCode", str, False, "value", True),
            ("_valueCode", "_valueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("_valueCoding", "_valueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("_valueContactDetail", "_valueContactDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("_valueContactPoint", "_valueContactPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("_valueContributor", "_valueContributor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("_valueCount", "_valueCount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("_valueDataRequirement", "_valueDataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("_valueDate", "_valueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", True),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("_valueDistance", "_valueDistance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("_valueDosage", "_valueDosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("_valueDuration", "_valueDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("_valueExpression", "_valueExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("_valueHumanName", "_valueHumanName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueId", "valueId", str, False, "value", True),
            ("_valueId", "_valueId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("_valueIdentifier", "_valueIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInstant", "valueInstant", fhirinstant.FHIRInstant, False, "value", True),
            ("_valueInstant", "_valueInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("_valueMarkdown", "_valueMarkdown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
            ("_valueMeta", "_valueMeta", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("_valueMoney", "_valueMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueOid", "valueOid", str, False, "value", True),
            ("_valueOid", "_valueOid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("_valueParameterDefinition", "_valueParameterDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("_valuePeriod", "_valuePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("_valuePositiveInt", "_valuePositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("_valueRange", "_valueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("_valueRatio", "_valueRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("_valueReference", "_valueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("_valueRelatedArtifact", "_valueRelatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("_valueSampledData", "_valueSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("_valueSignature", "_valueSignature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
            ("_valueTime", "_valueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("_valueTiming", "_valueTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("_valueTriggerDefinition", "_valueTriggerDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("_valueUnsignedInt", "_valueUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUri", "valueUri", str, False, "value", True),
            ("_valueUri", "_valueUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("_valueUrl", "_valueUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("_valueUsageContext", "_valueUsageContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUuid", "valueUuid", str, False, "value", True),
            ("_valueUuid", "_valueUuid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TaskRestriction(backboneelement.BackboneElement):
    """ Constraints on fulfillment tasks.
    
    If the Task.focus is a request resource and the task is seeking fulfillment
    (i.e. is asking for the request to be actioned), this element identifies
    any limitations on what parts of the referenced request should be actioned.
    """
    
    resource_type = "TaskRestriction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ When fulfillment sought.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.recipient = None
        """ For whom is fulfillment sought?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._recipient = None
        """ Primitive extension for recipient. Type `FHIRPrimitiveExtension` """
        
        self.repetitions = None
        """ How many times to repeat.
        Type `int`. """
        self._repetitions = None
        """ Primitive extension for repetitions. Type `FHIRPrimitiveExtension` """
        
        super(TaskRestriction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskRestriction, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("_recipient", "_recipient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("repetitions", "repetitions", int, False, None, False),
            ("_repetitions", "_repetitions", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import fhirtime
from . import humanname
from . import identifier
from . import meta
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext