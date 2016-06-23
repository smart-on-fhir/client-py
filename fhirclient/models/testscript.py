#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/TestScript) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class TestScript(domainresource.DomainResource):
    """ Describes a set of tests.
    
    TestScript is a resource that specifies a suite of tests against a FHIR
    server implementation to determine compliance against the FHIR
    specification.
    """
    
    resource_name = "TestScript"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `TestScriptContact` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date for this version of the TestScript.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the TestScript.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.fixture = None
        """ Fixture in the test script - by reference (uri).
        List of `TestScriptFixture` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.metadata = None
        """ Required capability that is assumed to function correctly on the
        FHIR server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """
        
        self.multiserver = None
        """ Whether or not the tests apply to more than one FHIR server.
        Type `bool`. """
        
        self.name = None
        """ Informal name for this TestScript.
        Type `str`. """
        
        self.profile = None
        """ Reference of the validation profile.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Scope and Usage this Test Script is for.
        Type `str`. """
        
        self.setup = None
        """ A series of required setup operations before tests are executed.
        Type `TestScriptSetup` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.teardown = None
        """ A series of required clean up steps.
        Type `TestScriptTeardown` (represented as `dict` in JSON). """
        
        self.test = None
        """ A test in this script.
        List of `TestScriptTest` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Absolute URL used to reference this TestScript.
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.variable = None
        """ Placeholder for evaluated elements.
        List of `TestScriptVariable` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the TestScript.
        Type `str`. """
        
        super(TestScript, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScript, self).elementProperties()
        js.extend([
            ("contact", "contact", TestScriptContact, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fixture", "fixture", TestScriptFixture, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("metadata", "metadata", TestScriptMetadata, False, None, False),
            ("multiserver", "multiserver", bool, False, None, False),
            ("name", "name", str, False, None, True),
            ("profile", "profile", fhirreference.FHIRReference, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("setup", "setup", TestScriptSetup, False, None, False),
            ("status", "status", str, False, None, True),
            ("teardown", "teardown", TestScriptTeardown, False, None, False),
            ("test", "test", TestScriptTest, True, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
            ("variable", "variable", TestScriptVariable, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class TestScriptContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "TestScriptContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(TestScriptContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class TestScriptFixture(backboneelement.BackboneElement):
    """ Fixture in the test script - by reference (uri).
    
    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """
    
    resource_name = "TestScriptFixture"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.autocreate = None
        """ Whether or not to implicitly create the fixture during setup.
        Type `bool`. """
        
        self.autodelete = None
        """ Whether or not to implicitly delete the fixture during teardown.
        Type `bool`. """
        
        self.resource = None
        """ Reference of the resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(TestScriptFixture, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptFixture, self).elementProperties()
        js.extend([
            ("autocreate", "autocreate", bool, False, None, False),
            ("autodelete", "autodelete", bool, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class TestScriptMetadata(backboneelement.BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.
    
    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """
    
    resource_name = "TestScriptMetadata"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.capability = None
        """ Capabilities  that are assumed to function correctly on the FHIR
        server being tested.
        List of `TestScriptMetadataCapability` items (represented as `dict` in JSON). """
        
        self.link = None
        """ Links to the FHIR specification.
        List of `TestScriptMetadataLink` items (represented as `dict` in JSON). """
        
        super(TestScriptMetadata, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadata, self).elementProperties()
        js.extend([
            ("capability", "capability", TestScriptMetadataCapability, True, None, True),
            ("link", "link", TestScriptMetadataLink, True, None, False),
        ])
        return js


class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.
    
    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """
    
    resource_name = "TestScriptMetadataCapability"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conformance = None
        """ Required Conformance.
        Type `FHIRReference` referencing `Conformance` (represented as `dict` in JSON). """
        
        self.description = None
        """ The expected capabilities of the server.
        Type `str`. """
        
        self.destination = None
        """ Which server these requirements apply to.
        Type `int`. """
        
        self.link = None
        """ Links to the FHIR specification.
        List of `str` items. """
        
        self.required = None
        """ Are the capabilities required?.
        Type `bool`. """
        
        self.validated = None
        """ Are the capabilities validated?.
        Type `bool`. """
        
        super(TestScriptMetadataCapability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadataCapability, self).elementProperties()
        js.extend([
            ("conformance", "conformance", fhirreference.FHIRReference, False, None, True),
            ("description", "description", str, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("link", "link", str, True, None, False),
            ("required", "required", bool, False, None, False),
            ("validated", "validated", bool, False, None, False),
        ])
        return js


class TestScriptMetadataLink(backboneelement.BackboneElement):
    """ Links to the FHIR specification.
    
    A link to the FHIR specification that this test is covering.
    """
    
    resource_name = "TestScriptMetadataLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Short description.
        Type `str`. """
        
        self.url = None
        """ URL to the specification.
        Type `str`. """
        
        super(TestScriptMetadataLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadataLink, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("url", "url", str, False, None, True),
        ])
        return js


class TestScriptSetup(backboneelement.BackboneElement):
    """ A series of required setup operations before tests are executed.
    """
    
    resource_name = "TestScriptSetup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A setup operation or assert to perform.
        List of `TestScriptSetupAction` items (represented as `dict` in JSON). """
        
        self.metadata = None
        """ Capabilities  that are assumed to function correctly on the FHIR
        server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """
        
        super(TestScriptSetup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptSetupAction, True, None, True),
            ("metadata", "metadata", TestScriptMetadata, False, None, False),
        ])
        return js


class TestScriptSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert to perform.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_name = "TestScriptSetupAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ The assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptSetupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
        ])
        return js


class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.
    
    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """
    
    resource_name = "TestScriptSetupActionAssert"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compareToSourceId = None
        """ Id of fixture used to compare the "sourceId/path" evaluations to.
        Type `str`. """
        
        self.compareToSourcePath = None
        """ XPath or JSONPath expression against fixture used to compare the
        "sourceId/path" evaluations to.
        Type `str`. """
        
        self.contentType = None
        """ xml | json.
        Type `str`. """
        
        self.description = None
        """ Tracking/reporting assertion description.
        Type `str`. """
        
        self.direction = None
        """ response | request.
        Type `str`. """
        
        self.headerField = None
        """ HTTP header field name.
        Type `str`. """
        
        self.label = None
        """ Tracking/logging assertion label.
        Type `str`. """
        
        self.minimumId = None
        """ Fixture Id of minimum content resource.
        Type `str`. """
        
        self.navigationLinks = None
        """ Perform validation on navigation links?.
        Type `bool`. """
        
        self.operator = None
        """ equals | notEquals | in | notIn | greaterThan | lessThan | empty |
        notEmpty | contains | notContains.
        Type `str`. """
        
        self.path = None
        """ XPath or JSONPath expression.
        Type `str`. """
        
        self.resource = None
        """ Resource type.
        Type `str`. """
        
        self.response = None
        """ okay | created | noContent | notModified | bad | forbidden |
        notFound | methodNotAllowed | conflict | gone | preconditionFailed
        | unprocessable.
        Type `str`. """
        
        self.responseCode = None
        """ HTTP response code to test.
        Type `str`. """
        
        self.sourceId = None
        """ Fixture Id of source expression or headerField.
        Type `str`. """
        
        self.validateProfileId = None
        """ Profile Id of validation profile reference.
        Type `str`. """
        
        self.value = None
        """ The value to compare to.
        Type `str`. """
        
        self.warningOnly = None
        """ Will this assert produce a warning only on error?.
        Type `bool`. """
        
        super(TestScriptSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionAssert, self).elementProperties()
        js.extend([
            ("compareToSourceId", "compareToSourceId", str, False, None, False),
            ("compareToSourcePath", "compareToSourcePath", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("direction", "direction", str, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("label", "label", str, False, None, False),
            ("minimumId", "minimumId", str, False, None, False),
            ("navigationLinks", "navigationLinks", bool, False, None, False),
            ("operator", "operator", str, False, None, False),
            ("path", "path", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("response", "response", str, False, None, False),
            ("responseCode", "responseCode", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("validateProfileId", "validateProfileId", str, False, None, False),
            ("value", "value", str, False, None, False),
            ("warningOnly", "warningOnly", bool, False, None, False),
        ])
        return js


class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """ The setup operation to perform.
    
    The operation to perform.
    """
    
    resource_name = "TestScriptSetupActionOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accept = None
        """ xml | json.
        Type `str`. """
        
        self.contentType = None
        """ xml | json.
        Type `str`. """
        
        self.description = None
        """ Tracking/reporting operation description.
        Type `str`. """
        
        self.destination = None
        """ Which server to perform the operation on.
        Type `int`. """
        
        self.encodeRequestUrl = None
        """ Whether or not to send the request url in encoded format.
        Type `bool`. """
        
        self.label = None
        """ Tracking/logging operation label.
        Type `str`. """
        
        self.params = None
        """ Explicitly defined path parameters.
        Type `str`. """
        
        self.requestHeader = None
        """ Each operation can have one ore more header elements.
        List of `TestScriptSetupActionOperationRequestHeader` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ Resource type.
        Type `str`. """
        
        self.responseId = None
        """ Fixture Id of mapped response.
        Type `str`. """
        
        self.sourceId = None
        """ Fixture Id of body for PUT and POST requests.
        Type `str`. """
        
        self.targetId = None
        """ Id of fixture used for extracting the [id],  [type], and [vid] for
        GET requests.
        Type `str`. """
        
        self.type = None
        """ The setup operation type that will be executed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.url = None
        """ Request URL.
        Type `str`. """
        
        super(TestScriptSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionOperation, self).elementProperties()
        js.extend([
            ("accept", "accept", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("encodeRequestUrl", "encodeRequestUrl", bool, False, None, False),
            ("label", "label", str, False, None, False),
            ("params", "params", str, False, None, False),
            ("requestHeader", "requestHeader", TestScriptSetupActionOperationRequestHeader, True, None, False),
            ("resource", "resource", str, False, None, False),
            ("responseId", "responseId", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("targetId", "targetId", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """ Each operation can have one ore more header elements.
    
    Header elements would be used to set HTTP headers.
    """
    
    resource_name = "TestScriptSetupActionOperationRequestHeader"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.field = None
        """ HTTP header field name.
        Type `str`. """
        
        self.value = None
        """ HTTP headerfield value.
        Type `str`. """
        
        super(TestScriptSetupActionOperationRequestHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionOperationRequestHeader, self).elementProperties()
        js.extend([
            ("field", "field", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class TestScriptTeardown(backboneelement.BackboneElement):
    """ A series of required clean up steps.
    
    A series of operations required to clean up after the all the tests are
    executed (successfully or otherwise).
    """
    
    resource_name = "TestScriptTeardown"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ One or more teardown operations to perform.
        List of `TestScriptTeardownAction` items (represented as `dict` in JSON). """
        
        super(TestScriptTeardown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTeardownAction, True, None, True),
        ])
        return js


class TestScriptTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations to perform.
    
    The teardown action will only contain an operation.
    """
    
    resource_name = "TestScriptTeardownAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ The teardown operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptTeardownAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
        ])
        return js


class TestScriptTest(backboneelement.BackboneElement):
    """ A test in this script.
    """
    
    resource_name = "TestScriptTest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A test operation or assert to perform.
        List of `TestScriptTestAction` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Tracking/reporting short description of the test.
        Type `str`. """
        
        self.metadata = None
        """ Capabilities  that are expected to function correctly on the FHIR
        server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """
        
        self.name = None
        """ Tracking/logging name of this test.
        Type `str`. """
        
        super(TestScriptTest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTest, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTestAction, True, None, True),
            ("description", "description", str, False, None, False),
            ("metadata", "metadata", TestScriptMetadata, False, None, False),
            ("name", "name", str, False, None, False),
        ])
        return js


class TestScriptTestAction(backboneelement.BackboneElement):
    """ A test operation or assert to perform.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_name = "TestScriptTestAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ The setup assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptTestAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTestAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
        ])
        return js


class TestScriptVariable(backboneelement.BackboneElement):
    """ Placeholder for evaluated elements.
    
    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """
    
    resource_name = "TestScriptVariable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.headerField = None
        """ HTTP header field name for source.
        Type `str`. """
        
        self.name = None
        """ Descriptive name for this variable.
        Type `str`. """
        
        self.path = None
        """ XPath or JSONPath against the fixture body.
        Type `str`. """
        
        self.sourceId = None
        """ Fixture Id of source expression or headerField within this variable.
        Type `str`. """
        
        super(TestScriptVariable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptVariable, self).elementProperties()
        js.extend([
            ("headerField", "headerField", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("path", "path", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
