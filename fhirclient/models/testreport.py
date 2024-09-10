# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TestReport).
# 2024, SMART Health IT.


from . import domainresource

class TestReport(domainresource.DomainResource):
    """ Describes the results of a TestScript execution.
    
    A summary of information based on the results of executing a TestScript.
    """
    
    resource_type = "TestReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.issued = None
        """ When the TestScript was executed and this TestReport was generated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._issued = None
        """ Primitive extension for issued. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Informal name of the executed TestScript.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.participant = None
        """ A participant in the test execution, either the execution engine, a
        client, or a server.
        List of `TestReportParticipant` items (represented as `dict` in JSON). """
        self._participant = None
        """ Primitive extension for participant. Type `FHIRPrimitiveExtension` """
        
        self.result = None
        """ pass | fail | pending.
        Type `str`. """
        self._result = None
        """ Primitive extension for result. Type `FHIRPrimitiveExtension` """
        
        self.score = None
        """ The final score (percentage of tests passed) resulting from the
        execution of the TestScript.
        Type `float`. """
        self._score = None
        """ Primitive extension for score. Type `FHIRPrimitiveExtension` """
        
        self.setup = None
        """ The results of the series of required setup operations before the
        tests were executed.
        Type `TestReportSetup` (represented as `dict` in JSON). """
        self._setup = None
        """ Primitive extension for setup. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ completed | in-progress | waiting | stopped | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.teardown = None
        """ The results of running the series of required clean up steps.
        Type `TestReportTeardown` (represented as `dict` in JSON). """
        self._teardown = None
        """ Primitive extension for teardown. Type `FHIRPrimitiveExtension` """
        
        self.test = None
        """ A test executed from the test script.
        List of `TestReportTest` items (represented as `dict` in JSON). """
        self._test = None
        """ Primitive extension for test. Type `FHIRPrimitiveExtension` """
        
        self.testScript = None
        """ Reference to the  version-specific TestScript that was executed to
        produce this TestReport.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._testScript = None
        """ Primitive extension for testScript. Type `FHIRPrimitiveExtension` """
        
        self.tester = None
        """ Name of the tester producing this report (Organization or
        individual).
        Type `str`. """
        self._tester = None
        """ Primitive extension for tester. Type `FHIRPrimitiveExtension` """
        
        super(TestReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issued", "issued", fhirdatetime.FHIRDateTime, False, None, False),
            ("_issued", "_issued", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participant", "participant", TestReportParticipant, True, None, False),
            ("_participant", "_participant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("result", "result", str, False, None, True),
            ("_result", "_result", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("score", "score", float, False, None, False),
            ("_score", "_score", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("setup", "setup", TestReportSetup, False, None, False),
            ("_setup", "_setup", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("teardown", "teardown", TestReportTeardown, False, None, False),
            ("_teardown", "_teardown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("test", "test", TestReportTest, True, None, False),
            ("_test", "_test", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("testScript", "testScript", fhirreference.FHIRReference, False, None, True),
            ("_testScript", "_testScript", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("tester", "tester", str, False, None, False),
            ("_tester", "_tester", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class TestReportParticipant(backboneelement.BackboneElement):
    """ A participant in the test execution, either the execution engine, a client,
    or a server.
    """
    
    resource_type = "TestReportParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.display = None
        """ The display name of the participant.
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ test-engine | client | server.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.uri = None
        """ The uri of the participant. An absolute URL is preferred.
        Type `str`. """
        self._uri = None
        """ Primitive extension for uri. Type `FHIRPrimitiveExtension` """
        
        super(TestReportParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportParticipant, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("uri", "uri", str, False, None, True),
            ("_uri", "_uri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestReportSetup(backboneelement.BackboneElement):
    """ The results of the series of required setup operations before the tests
    were executed.
    """
    
    resource_type = "TestReportSetup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A setup operation or assert that was executed.
        List of `TestReportSetupAction` items (represented as `dict` in JSON). """
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        super(TestReportSetup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestReportSetupAction, True, None, True),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestReportSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert that was executed.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_type = "TestReportSetupAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ The assertion to perform.
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """
        self._assert_fhir = None
        """ Primitive extension for assert_fhir. Type `FHIRPrimitiveExtension` """
        
        self.operation = None
        """ The operation to perform.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        self._operation = None
        """ Primitive extension for operation. Type `FHIRPrimitiveExtension` """
        
        super(TestReportSetupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetupAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
            ("_assert_fhir", "_assert_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
            ("_operation", "_operation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestReportSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.
    
    The results of the assertion performed on the previous operations.
    """
    
    resource_type = "TestReportSetupActionAssert"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detail = None
        """ A link to further details on the result.
        Type `str`. """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.message = None
        """ A message associated with the result.
        Type `str`. """
        self._message = None
        """ Primitive extension for message. Type `FHIRPrimitiveExtension` """
        
        self.result = None
        """ pass | skip | fail | warning | error.
        Type `str`. """
        self._result = None
        """ Primitive extension for result. Type `FHIRPrimitiveExtension` """
        
        super(TestReportSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetupActionAssert, self).elementProperties()
        js.extend([
            ("detail", "detail", str, False, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("message", "message", str, False, None, False),
            ("_message", "_message", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("result", "result", str, False, None, True),
            ("_result", "_result", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """ The operation to perform.
    
    The operation performed.
    """
    
    resource_type = "TestReportSetupActionOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detail = None
        """ A link to further details on the result.
        Type `str`. """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.message = None
        """ A message associated with the result.
        Type `str`. """
        self._message = None
        """ Primitive extension for message. Type `FHIRPrimitiveExtension` """
        
        self.result = None
        """ pass | skip | fail | warning | error.
        Type `str`. """
        self._result = None
        """ Primitive extension for result. Type `FHIRPrimitiveExtension` """
        
        super(TestReportSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetupActionOperation, self).elementProperties()
        js.extend([
            ("detail", "detail", str, False, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("message", "message", str, False, None, False),
            ("_message", "_message", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("result", "result", str, False, None, True),
            ("_result", "_result", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestReportTeardown(backboneelement.BackboneElement):
    """ The results of running the series of required clean up steps.
    
    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """
    
    resource_type = "TestReportTeardown"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ One or more teardown operations performed.
        List of `TestReportTeardownAction` items (represented as `dict` in JSON). """
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        super(TestReportTeardown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTeardownAction, True, None, True),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestReportTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations performed.
    
    The teardown action will only contain an operation.
    """
    
    resource_type = "TestReportTeardownAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ The teardown operation performed.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        self._operation = None
        """ Primitive extension for operation. Type `FHIRPrimitiveExtension` """
        
        super(TestReportTeardownAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, True),
            ("_operation", "_operation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestReportTest(backboneelement.BackboneElement):
    """ A test executed from the test script.
    """
    
    resource_type = "TestReportTest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A test operation or assert that was performed.
        List of `TestReportTestAction` items (represented as `dict` in JSON). """
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Tracking/reporting short description of the test.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Tracking/logging name of this test.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        super(TestReportTest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTest, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTestAction, True, None, True),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestReportTestAction(backboneelement.BackboneElement):
    """ A test operation or assert that was performed.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_type = "TestReportTestAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ The assertion performed.
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """
        self._assert_fhir = None
        """ Primitive extension for assert_fhir. Type `FHIRPrimitiveExtension` """
        
        self.operation = None
        """ The operation performed.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        self._operation = None
        """ Primitive extension for operation. Type `FHIRPrimitiveExtension` """
        
        super(TestReportTestAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTestAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
            ("_assert_fhir", "_assert_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
            ("_operation", "_operation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import fhirdatetime
from . import fhirreference
from . import identifier