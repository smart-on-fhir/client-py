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
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Additional identifier for the example scenario.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ Each resource and each version that is present in the workflow.
        List of `ExampleScenarioInstance` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for example scenario (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this example scenario (computer friendly).
        Type `str`. """
        
        self.process = None
        """ Each major process - a group of operations.
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ The purpose of the example, e.g. to illustrate a scenario.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.url = None
        """ Canonical identifier for this example scenario, represented as a
        URI (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the example scenario.
        Type `str`. """
        
        self.workflow = None
        """ Another nested workflow.
        List of `str` items. """
        
        super(ExampleScenario, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenario, self).elementProperties()
        js.extend([
            ("actor", "actor", ExampleScenarioActor, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instance", "instance", ExampleScenarioInstance, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("workflow", "workflow", str, True, None, False),
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
        
        self.description = None
        """ The description of the actor.
        Type `str`. """
        
        self.name = None
        """ The name of the actor as shown in the page.
        Type `str`. """
        
        self.type = None
        """ person | entity.
        Type `str`. """
        
        super(ExampleScenarioActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioActor, self).elementProperties()
        js.extend([
            ("actorId", "actorId", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("type", "type", str, False, None, True),
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
        
        self.description = None
        """ Human-friendly description of the resource instance.
        Type `str`. """
        
        self.name = None
        """ A short name for the resource instance.
        Type `str`. """
        
        self.resourceId = None
        """ The id of the resource for referencing.
        Type `str`. """
        
        self.resourceType = None
        """ The type of the resource.
        Type `str`. """
        
        self.version = None
        """ A specific version of the resource.
        List of `ExampleScenarioInstanceVersion` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstance, self).elementProperties()
        js.extend([
            ("containedInstance", "containedInstance", ExampleScenarioInstanceContainedInstance, True, None, False),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("resourceId", "resourceId", str, False, None, True),
            ("resourceType", "resourceType", str, False, None, True),
            ("version", "version", ExampleScenarioInstanceVersion, True, None, False),
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
        
        self.versionId = None
        """ A specific version of a resource contained in the instance.
        Type `str`. """
        
        super(ExampleScenarioInstanceContainedInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstanceContainedInstance, self).elementProperties()
        js.extend([
            ("resourceId", "resourceId", str, False, None, True),
            ("versionId", "versionId", str, False, None, False),
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
        
        self.versionId = None
        """ The identifier of a specific version of a resource.
        Type `str`. """
        
        super(ExampleScenarioInstanceVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstanceVersion, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("versionId", "versionId", str, False, None, True),
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
        
        self.postConditions = None
        """ Description of final status after the process ends.
        Type `str`. """
        
        self.preConditions = None
        """ Description of initial status before the process starts.
        Type `str`. """
        
        self.step = None
        """ Each step of the process.
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        
        self.title = None
        """ The diagram title of the group of operations.
        Type `str`. """
        
        super(ExampleScenarioProcess, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcess, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("postConditions", "postConditions", str, False, None, False),
            ("preConditions", "preConditions", str, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("title", "title", str, False, None, True),
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
        
        self.operation = None
        """ Each interaction or action.
        Type `ExampleScenarioProcessStepOperation` (represented as `dict` in JSON). """
        
        self.pause = None
        """ If there is a pause in the flow.
        Type `bool`. """
        
        self.process = None
        """ Nested process.
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioProcessStep, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStep, self).elementProperties()
        js.extend([
            ("alternative", "alternative", ExampleScenarioProcessStepAlternative, True, None, False),
            ("operation", "operation", ExampleScenarioProcessStepOperation, False, None, False),
            ("pause", "pause", bool, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
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
        
        self.step = None
        """ What happens in each alternative option.
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Label for alternative.
        Type `str`. """
        
        super(ExampleScenarioProcessStepAlternative, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStepAlternative, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("title", "title", str, False, None, True),
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
        
        self.initiator = None
        """ Who starts the transaction.
        Type `str`. """
        
        self.initiatorActive = None
        """ Whether the initiator is deactivated right after the transaction.
        Type `bool`. """
        
        self.name = None
        """ The human-friendly name of the interaction.
        Type `str`. """
        
        self.number = None
        """ The sequential number of the interaction.
        Type `str`. """
        
        self.receiver = None
        """ Who receives the transaction.
        Type `str`. """
        
        self.receiverActive = None
        """ Whether the receiver is deactivated right after the transaction.
        Type `bool`. """
        
        self.request = None
        """ Each resource instance used by the initiator.
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        
        self.response = None
        """ Each resource instance used by the responder.
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of operation - CRUD.
        Type `str`. """
        
        super(ExampleScenarioProcessStepOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStepOperation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("initiator", "initiator", str, False, None, False),
            ("initiatorActive", "initiatorActive", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("number", "number", str, False, None, True),
            ("receiver", "receiver", str, False, None, False),
            ("receiverActive", "receiverActive", bool, False, None, False),
            ("request", "request", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("response", "response", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import identifier
from . import usagecontext
