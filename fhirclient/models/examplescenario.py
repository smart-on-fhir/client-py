# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ExampleScenario).
# 2024, SMART Health IT.


from . import domainresource

class ExampleScenario(domainresource.DomainResource):
    """ Example of workflow instance.
    """
    
    resource_type = "ExampleScenario"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Actor participating in the resource.
        List of `ExampleScenarioActor` items (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
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
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the example scenario.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.instance = None
        """ Each resource and each version that is present in the workflow.
        List of `ExampleScenarioInstance` items (represented as `dict` in JSON). """
        self._instance = None
        """ Primitive extension for instance. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for example scenario (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this example scenario (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.process = None
        """ Each major process - a group of operations.
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        self._process = None
        """ Primitive extension for process. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ The purpose of the example, e.g. to illustrate a scenario.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this example scenario, represented as a
        URI (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the example scenario.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        self.workflow = None
        """ Another nested workflow.
        List of `str` items. """
        self._workflow = None
        """ Primitive extension for workflow. Type `FHIRPrimitiveExtension` """
        
        super(ExampleScenario, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenario, self).elementProperties()
        js.extend([
            ("actor", "actor", ExampleScenarioActor, True, None, False),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instance", "instance", ExampleScenarioInstance, True, None, False),
            ("_instance", "_instance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
            ("_process", "_process", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("workflow", "workflow", str, True, None, False),
            ("_workflow", "_workflow", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ExampleScenarioActor(backboneelement.BackboneElement):
    """ Actor participating in the resource.
    """
    
    resource_type = "ExampleScenarioActor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actorId = None
        """ ID or acronym of the actor.
        Type `str`. """
        self._actorId = None
        """ Primitive extension for actorId. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ The description of the actor.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ The name of the actor as shown in the page.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ person | entity.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ExampleScenarioActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioActor, self).elementProperties()
        js.extend([
            ("actorId", "actorId", str, False, None, True),
            ("_actorId", "_actorId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExampleScenarioInstance(backboneelement.BackboneElement):
    """ Each resource and each version that is present in the workflow.
    """
    
    resource_type = "ExampleScenarioInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.containedInstance = None
        """ Resources contained in the instance.
        List of `ExampleScenarioInstanceContainedInstance` items (represented as `dict` in JSON). """
        self._containedInstance = None
        """ Primitive extension for containedInstance. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Human-friendly description of the resource instance.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ A short name for the resource instance.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.resourceId = None
        """ The id of the resource for referencing.
        Type `str`. """
        self._resourceId = None
        """ Primitive extension for resourceId. Type `FHIRPrimitiveExtension` """
        
        self.resourceType = None
        """ The type of the resource.
        Type `str`. """
        self._resourceType = None
        """ Primitive extension for resourceType. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ A specific version of the resource.
        List of `ExampleScenarioInstanceVersion` items (represented as `dict` in JSON). """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ExampleScenarioInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstance, self).elementProperties()
        js.extend([
            ("containedInstance", "containedInstance", ExampleScenarioInstanceContainedInstance, True, None, False),
            ("_containedInstance", "_containedInstance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resourceId", "resourceId", str, False, None, True),
            ("_resourceId", "_resourceId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resourceType", "resourceType", str, False, None, True),
            ("_resourceType", "_resourceType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", ExampleScenarioInstanceVersion, True, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    """ Resources contained in the instance.
    
    Resources contained in the instance (e.g. the observations contained in a
    bundle).
    """
    
    resource_type = "ExampleScenarioInstanceContainedInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.resourceId = None
        """ Each resource contained in the instance.
        Type `str`. """
        self._resourceId = None
        """ Primitive extension for resourceId. Type `FHIRPrimitiveExtension` """
        
        self.versionId = None
        """ A specific version of a resource contained in the instance.
        Type `str`. """
        self._versionId = None
        """ Primitive extension for versionId. Type `FHIRPrimitiveExtension` """
        
        super(ExampleScenarioInstanceContainedInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstanceContainedInstance, self).elementProperties()
        js.extend([
            ("resourceId", "resourceId", str, False, None, True),
            ("_resourceId", "_resourceId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("versionId", "versionId", str, False, None, False),
            ("_versionId", "_versionId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    """ A specific version of the resource.
    """
    
    resource_type = "ExampleScenarioInstanceVersion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ The description of the resource version.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.versionId = None
        """ The identifier of a specific version of a resource.
        Type `str`. """
        self._versionId = None
        """ Primitive extension for versionId. Type `FHIRPrimitiveExtension` """
        
        super(ExampleScenarioInstanceVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstanceVersion, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("versionId", "versionId", str, False, None, True),
            ("_versionId", "_versionId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExampleScenarioProcess(backboneelement.BackboneElement):
    """ Each major process - a group of operations.
    """
    
    resource_type = "ExampleScenarioProcess"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ A longer description of the group of operations.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.postConditions = None
        """ Description of final status after the process ends.
        Type `str`. """
        self._postConditions = None
        """ Primitive extension for postConditions. Type `FHIRPrimitiveExtension` """
        
        self.preConditions = None
        """ Description of initial status before the process starts.
        Type `str`. """
        self._preConditions = None
        """ Primitive extension for preConditions. Type `FHIRPrimitiveExtension` """
        
        self.step = None
        """ Each step of the process.
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        self._step = None
        """ Primitive extension for step. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ The diagram title of the group of operations.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        super(ExampleScenarioProcess, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcess, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("postConditions", "postConditions", str, False, None, False),
            ("_postConditions", "_postConditions", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preConditions", "preConditions", str, False, None, False),
            ("_preConditions", "_preConditions", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("_step", "_step", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, True),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    """ Each step of the process.
    """
    
    resource_type = "ExampleScenarioProcessStep"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alternative = None
        """ Alternate non-typical step action.
        List of `ExampleScenarioProcessStepAlternative` items (represented as `dict` in JSON). """
        self._alternative = None
        """ Primitive extension for alternative. Type `FHIRPrimitiveExtension` """
        
        self.operation = None
        """ Each interaction or action.
        Type `ExampleScenarioProcessStepOperation` (represented as `dict` in JSON). """
        self._operation = None
        """ Primitive extension for operation. Type `FHIRPrimitiveExtension` """
        
        self.pause = None
        """ If there is a pause in the flow.
        Type `bool`. """
        self._pause = None
        """ Primitive extension for pause. Type `FHIRPrimitiveExtension` """
        
        self.process = None
        """ Nested process.
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        self._process = None
        """ Primitive extension for process. Type `FHIRPrimitiveExtension` """
        
        super(ExampleScenarioProcessStep, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStep, self).elementProperties()
        js.extend([
            ("alternative", "alternative", ExampleScenarioProcessStepAlternative, True, None, False),
            ("_alternative", "_alternative", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operation", "operation", ExampleScenarioProcessStepOperation, False, None, False),
            ("_operation", "_operation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("pause", "pause", bool, False, None, False),
            ("_pause", "_pause", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
            ("_process", "_process", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    """ Alternate non-typical step action.
    
    Indicates an alternative step that can be taken instead of the operations
    on the base step in exceptional/atypical circumstances.
    """
    
    resource_type = "ExampleScenarioProcessStepAlternative"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ A human-readable description of each option.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.step = None
        """ What happens in each alternative option.
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        self._step = None
        """ Primitive extension for step. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Label for alternative.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        super(ExampleScenarioProcessStepAlternative, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStepAlternative, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("_step", "_step", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, True),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    """ Each interaction or action.
    """
    
    resource_type = "ExampleScenarioProcessStepOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ A comment to be inserted in the diagram.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.initiator = None
        """ Who starts the transaction.
        Type `str`. """
        self._initiator = None
        """ Primitive extension for initiator. Type `FHIRPrimitiveExtension` """
        
        self.initiatorActive = None
        """ Whether the initiator is deactivated right after the transaction.
        Type `bool`. """
        self._initiatorActive = None
        """ Primitive extension for initiatorActive. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ The human-friendly name of the interaction.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.number = None
        """ The sequential number of the interaction.
        Type `str`. """
        self._number = None
        """ Primitive extension for number. Type `FHIRPrimitiveExtension` """
        
        self.receiver = None
        """ Who receives the transaction.
        Type `str`. """
        self._receiver = None
        """ Primitive extension for receiver. Type `FHIRPrimitiveExtension` """
        
        self.receiverActive = None
        """ Whether the receiver is deactivated right after the transaction.
        Type `bool`. """
        self._receiverActive = None
        """ Primitive extension for receiverActive. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Each resource instance used by the initiator.
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.response = None
        """ Each resource instance used by the responder.
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        self._response = None
        """ Primitive extension for response. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of operation - CRUD.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ExampleScenarioProcessStepOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStepOperation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("initiator", "initiator", str, False, None, False),
            ("_initiator", "_initiator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("initiatorActive", "initiatorActive", bool, False, None, False),
            ("_initiatorActive", "_initiatorActive", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("number", "number", str, False, None, True),
            ("_number", "_number", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("receiver", "receiver", str, False, None, False),
            ("_receiver", "_receiver", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("receiverActive", "receiverActive", bool, False, None, False),
            ("_receiverActive", "_receiverActive", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("response", "response", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("_response", "_response", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import identifier
from . import usagecontext