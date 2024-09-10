# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TestScript).
# 2024, SMART Health IT.


from . import domainresource

class TestScript(domainresource.DomainResource):
    """ Describes a set of tests.
    
    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """
    
    resource_type = "TestScript"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        self.description = None
        """ Natural language description of the test script.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.destination = None
        """ An abstract server representing a destination or receiver in a
        message exchange.
        List of `TestScriptDestination` items (represented as `dict` in JSON). """
        self._destination = None
        """ Primitive extension for destination. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.fixture = None
        """ Fixture in the test script - by reference (uri).
        List of `TestScriptFixture` items (represented as `dict` in JSON). """
        self._fixture = None
        """ Primitive extension for fixture. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the test script.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for test script (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.metadata = None
        """ Required capability that is assumed to function correctly on the
        FHIR server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """
        self._metadata = None
        """ Primitive extension for metadata. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this test script (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.origin = None
        """ An abstract server representing a client or sender in a message
        exchange.
        List of `TestScriptOrigin` items (represented as `dict` in JSON). """
        self._origin = None
        """ Primitive extension for origin. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ Reference of the validation profile.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this test script is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.setup = None
        """ A series of required setup operations before tests are executed.
        Type `TestScriptSetup` (represented as `dict` in JSON). """
        self._setup = None
        """ Primitive extension for setup. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.teardown = None
        """ A series of required clean up steps.
        Type `TestScriptTeardown` (represented as `dict` in JSON). """
        self._teardown = None
        """ Primitive extension for teardown. Type `FHIRPrimitiveExtension` """
        
        self.test = None
        """ A test in this script.
        List of `TestScriptTest` items (represented as `dict` in JSON). """
        self._test = None
        """ Primitive extension for test. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this test script (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this test script, represented as a URI
        (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.variable = None
        """ Placeholder for evaluated elements.
        List of `TestScriptVariable` items (represented as `dict` in JSON). """
        self._variable = None
        """ Primitive extension for variable. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the test script.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(TestScript, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScript, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("destination", "destination", TestScriptDestination, True, None, False),
            ("_destination", "_destination", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixture", "fixture", TestScriptFixture, True, None, False),
            ("_fixture", "_fixture", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("metadata", "metadata", TestScriptMetadata, False, None, False),
            ("_metadata", "_metadata", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("origin", "origin", TestScriptOrigin, True, None, False),
            ("_origin", "_origin", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", fhirreference.FHIRReference, True, None, False),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("setup", "setup", TestScriptSetup, False, None, False),
            ("_setup", "_setup", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("teardown", "teardown", TestScriptTeardown, False, None, False),
            ("_teardown", "_teardown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("test", "test", TestScriptTest, True, None, False),
            ("_test", "_test", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variable", "variable", TestScriptVariable, True, None, False),
            ("_variable", "_variable", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class TestScriptDestination(backboneelement.BackboneElement):
    """ An abstract server representing a destination or receiver in a message
    exchange.
    
    An abstract server used in operations within this test script in the
    destination element.
    """
    
    resource_type = "TestScriptDestination"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.index = None
        """ The index of the abstract destination server starting at 1.
        Type `int`. """
        self._index = None
        """ Primitive extension for index. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-
        SDC-FormProcessor.
        Type `Coding` (represented as `dict` in JSON). """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptDestination, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptDestination, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("_index", "_index", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", coding.Coding, False, None, True),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptFixture(backboneelement.BackboneElement):
    """ Fixture in the test script - by reference (uri).
    
    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """
    
    resource_type = "TestScriptFixture"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.autocreate = None
        """ Whether or not to implicitly create the fixture during setup.
        Type `bool`. """
        self._autocreate = None
        """ Primitive extension for autocreate. Type `FHIRPrimitiveExtension` """
        
        self.autodelete = None
        """ Whether or not to implicitly delete the fixture during teardown.
        Type `bool`. """
        self._autodelete = None
        """ Primitive extension for autodelete. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ Reference of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptFixture, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptFixture, self).elementProperties()
        js.extend([
            ("autocreate", "autocreate", bool, False, None, True),
            ("_autocreate", "_autocreate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("autodelete", "autodelete", bool, False, None, True),
            ("_autodelete", "_autodelete", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptMetadata(backboneelement.BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.
    
    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """
    
    resource_type = "TestScriptMetadata"
    
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
        self._capability = None
        """ Primitive extension for capability. Type `FHIRPrimitiveExtension` """
        
        self.link = None
        """ Links to the FHIR specification.
        List of `TestScriptMetadataLink` items (represented as `dict` in JSON). """
        self._link = None
        """ Primitive extension for link. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptMetadata, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadata, self).elementProperties()
        js.extend([
            ("capability", "capability", TestScriptMetadataCapability, True, None, True),
            ("_capability", "_capability", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("link", "link", TestScriptMetadataLink, True, None, False),
            ("_link", "_link", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.
    
    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """
    
    resource_type = "TestScriptMetadataCapability"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.capabilities = None
        """ Required Capability Statement.
        Type `str`. """
        self._capabilities = None
        """ Primitive extension for capabilities. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ The expected capabilities of the server.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.destination = None
        """ Which server these requirements apply to.
        Type `int`. """
        self._destination = None
        """ Primitive extension for destination. Type `FHIRPrimitiveExtension` """
        
        self.link = None
        """ Links to the FHIR specification.
        List of `str` items. """
        self._link = None
        """ Primitive extension for link. Type `FHIRPrimitiveExtension` """
        
        self.origin = None
        """ Which origin server these requirements apply to.
        List of `int` items. """
        self._origin = None
        """ Primitive extension for origin. Type `FHIRPrimitiveExtension` """
        
        self.required = None
        """ Are the capabilities required?.
        Type `bool`. """
        self._required = None
        """ Primitive extension for required. Type `FHIRPrimitiveExtension` """
        
        self.validated = None
        """ Are the capabilities validated?.
        Type `bool`. """
        self._validated = None
        """ Primitive extension for validated. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptMetadataCapability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadataCapability, self).elementProperties()
        js.extend([
            ("capabilities", "capabilities", str, False, None, True),
            ("_capabilities", "_capabilities", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("_destination", "_destination", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("link", "link", str, True, None, False),
            ("_link", "_link", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("origin", "origin", int, True, None, False),
            ("_origin", "_origin", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("required", "required", bool, False, None, True),
            ("_required", "_required", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("validated", "validated", bool, False, None, True),
            ("_validated", "_validated", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptMetadataLink(backboneelement.BackboneElement):
    """ Links to the FHIR specification.
    
    A link to the FHIR specification that this test is covering.
    """
    
    resource_type = "TestScriptMetadataLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Short description.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ URL to the specification.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptMetadataLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadataLink, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptOrigin(backboneelement.BackboneElement):
    """ An abstract server representing a client or sender in a message exchange.
    
    An abstract server used in operations within this test script in the origin
    element.
    """
    
    resource_type = "TestScriptOrigin"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.index = None
        """ The index of the abstract origin server starting at 1.
        Type `int`. """
        self._index = None
        """ Primitive extension for index. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ FHIR-Client | FHIR-SDC-FormFiller.
        Type `Coding` (represented as `dict` in JSON). """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptOrigin, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptOrigin, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("_index", "_index", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", coding.Coding, False, None, True),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptSetup(backboneelement.BackboneElement):
    """ A series of required setup operations before tests are executed.
    """
    
    resource_type = "TestScriptSetup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A setup operation or assert to perform.
        List of `TestScriptSetupAction` items (represented as `dict` in JSON). """
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptSetup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptSetupAction, True, None, True),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert to perform.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_type = "TestScriptSetupAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ The assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        self._assert_fhir = None
        """ Primitive extension for assert_fhir. Type `FHIRPrimitiveExtension` """
        
        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        self._operation = None
        """ Primitive extension for operation. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptSetupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
            ("_assert_fhir", "_assert_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
            ("_operation", "_operation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.
    
    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """
    
    resource_type = "TestScriptSetupActionAssert"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compareToSourceExpression = None
        """ The FHIRPath expression to evaluate against the source fixture.
        Type `str`. """
        self._compareToSourceExpression = None
        """ Primitive extension for compareToSourceExpression. Type `FHIRPrimitiveExtension` """
        
        self.compareToSourceId = None
        """ Id of the source fixture to be evaluated.
        Type `str`. """
        self._compareToSourceId = None
        """ Primitive extension for compareToSourceId. Type `FHIRPrimitiveExtension` """
        
        self.compareToSourcePath = None
        """ XPath or JSONPath expression to evaluate against the source fixture.
        Type `str`. """
        self._compareToSourcePath = None
        """ Primitive extension for compareToSourcePath. Type `FHIRPrimitiveExtension` """
        
        self.contentType = None
        """ Mime type to compare against the 'Content-Type' header.
        Type `str`. """
        self._contentType = None
        """ Primitive extension for contentType. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Tracking/reporting assertion description.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.direction = None
        """ response | request.
        Type `str`. """
        self._direction = None
        """ Primitive extension for direction. Type `FHIRPrimitiveExtension` """
        
        self.expression = None
        """ The FHIRPath expression to be evaluated.
        Type `str`. """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.headerField = None
        """ HTTP header field name.
        Type `str`. """
        self._headerField = None
        """ Primitive extension for headerField. Type `FHIRPrimitiveExtension` """
        
        self.label = None
        """ Tracking/logging assertion label.
        Type `str`. """
        self._label = None
        """ Primitive extension for label. Type `FHIRPrimitiveExtension` """
        
        self.minimumId = None
        """ Fixture Id of minimum content resource.
        Type `str`. """
        self._minimumId = None
        """ Primitive extension for minimumId. Type `FHIRPrimitiveExtension` """
        
        self.navigationLinks = None
        """ Perform validation on navigation links?.
        Type `bool`. """
        self._navigationLinks = None
        """ Primitive extension for navigationLinks. Type `FHIRPrimitiveExtension` """
        
        self.operator = None
        """ equals | notEquals | in | notIn | greaterThan | lessThan | empty |
        notEmpty | contains | notContains | eval.
        Type `str`. """
        self._operator = None
        """ Primitive extension for operator. Type `FHIRPrimitiveExtension` """
        
        self.path = None
        """ XPath or JSONPath expression.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        self.requestMethod = None
        """ delete | get | options | patch | post | put | head.
        Type `str`. """
        self._requestMethod = None
        """ Primitive extension for requestMethod. Type `FHIRPrimitiveExtension` """
        
        self.requestURL = None
        """ Request URL comparison value.
        Type `str`. """
        self._requestURL = None
        """ Primitive extension for requestURL. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ Resource type.
        Type `str`. """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.response = None
        """ okay | created | noContent | notModified | bad | forbidden |
        notFound | methodNotAllowed | conflict | gone | preconditionFailed
        | unprocessable.
        Type `str`. """
        self._response = None
        """ Primitive extension for response. Type `FHIRPrimitiveExtension` """
        
        self.responseCode = None
        """ HTTP response code to test.
        Type `str`. """
        self._responseCode = None
        """ Primitive extension for responseCode. Type `FHIRPrimitiveExtension` """
        
        self.sourceId = None
        """ Fixture Id of source expression or headerField.
        Type `str`. """
        self._sourceId = None
        """ Primitive extension for sourceId. Type `FHIRPrimitiveExtension` """
        
        self.validateProfileId = None
        """ Profile Id of validation profile reference.
        Type `str`. """
        self._validateProfileId = None
        """ Primitive extension for validateProfileId. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The value to compare to.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        self.warningOnly = None
        """ Will this assert produce a warning only on error?.
        Type `bool`. """
        self._warningOnly = None
        """ Primitive extension for warningOnly. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionAssert, self).elementProperties()
        js.extend([
            ("compareToSourceExpression", "compareToSourceExpression", str, False, None, False),
            ("_compareToSourceExpression", "_compareToSourceExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("compareToSourceId", "compareToSourceId", str, False, None, False),
            ("_compareToSourceId", "_compareToSourceId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("compareToSourcePath", "compareToSourcePath", str, False, None, False),
            ("_compareToSourcePath", "_compareToSourcePath", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("_contentType", "_contentType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("direction", "direction", str, False, None, False),
            ("_direction", "_direction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("_headerField", "_headerField", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("label", "label", str, False, None, False),
            ("_label", "_label", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minimumId", "minimumId", str, False, None, False),
            ("_minimumId", "_minimumId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("navigationLinks", "navigationLinks", bool, False, None, False),
            ("_navigationLinks", "_navigationLinks", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operator", "operator", str, False, None, False),
            ("_operator", "_operator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("path", "path", str, False, None, False),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestMethod", "requestMethod", str, False, None, False),
            ("_requestMethod", "_requestMethod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestURL", "requestURL", str, False, None, False),
            ("_requestURL", "_requestURL", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("response", "response", str, False, None, False),
            ("_response", "_response", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("responseCode", "responseCode", str, False, None, False),
            ("_responseCode", "_responseCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("_sourceId", "_sourceId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("validateProfileId", "validateProfileId", str, False, None, False),
            ("_validateProfileId", "_validateProfileId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, False),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("warningOnly", "warningOnly", bool, False, None, True),
            ("_warningOnly", "_warningOnly", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """ The setup operation to perform.
    
    The operation to perform.
    """
    
    resource_type = "TestScriptSetupActionOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accept = None
        """ Mime type to accept in the payload of the response, with charset
        etc..
        Type `str`. """
        self._accept = None
        """ Primitive extension for accept. Type `FHIRPrimitiveExtension` """
        
        self.contentType = None
        """ Mime type of the request payload contents, with charset etc..
        Type `str`. """
        self._contentType = None
        """ Primitive extension for contentType. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Tracking/reporting operation description.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.destination = None
        """ Server responding to the request.
        Type `int`. """
        self._destination = None
        """ Primitive extension for destination. Type `FHIRPrimitiveExtension` """
        
        self.encodeRequestUrl = None
        """ Whether or not to send the request url in encoded format.
        Type `bool`. """
        self._encodeRequestUrl = None
        """ Primitive extension for encodeRequestUrl. Type `FHIRPrimitiveExtension` """
        
        self.label = None
        """ Tracking/logging operation label.
        Type `str`. """
        self._label = None
        """ Primitive extension for label. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ delete | get | options | patch | post | put | head.
        Type `str`. """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.origin = None
        """ Server initiating the request.
        Type `int`. """
        self._origin = None
        """ Primitive extension for origin. Type `FHIRPrimitiveExtension` """
        
        self.params = None
        """ Explicitly defined path parameters.
        Type `str`. """
        self._params = None
        """ Primitive extension for params. Type `FHIRPrimitiveExtension` """
        
        self.requestHeader = None
        """ Each operation can have one or more header elements.
        List of `TestScriptSetupActionOperationRequestHeader` items (represented as `dict` in JSON). """
        self._requestHeader = None
        """ Primitive extension for requestHeader. Type `FHIRPrimitiveExtension` """
        
        self.requestId = None
        """ Fixture Id of mapped request.
        Type `str`. """
        self._requestId = None
        """ Primitive extension for requestId. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ Resource type.
        Type `str`. """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.responseId = None
        """ Fixture Id of mapped response.
        Type `str`. """
        self._responseId = None
        """ Primitive extension for responseId. Type `FHIRPrimitiveExtension` """
        
        self.sourceId = None
        """ Fixture Id of body for PUT and POST requests.
        Type `str`. """
        self._sourceId = None
        """ Primitive extension for sourceId. Type `FHIRPrimitiveExtension` """
        
        self.targetId = None
        """ Id of fixture used for extracting the [id],  [type], and [vid] for
        GET requests.
        Type `str`. """
        self._targetId = None
        """ Primitive extension for targetId. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The operation code type that will be executed.
        Type `Coding` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Request URL.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionOperation, self).elementProperties()
        js.extend([
            ("accept", "accept", str, False, None, False),
            ("_accept", "_accept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("_contentType", "_contentType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("_destination", "_destination", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encodeRequestUrl", "encodeRequestUrl", bool, False, None, True),
            ("_encodeRequestUrl", "_encodeRequestUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("label", "label", str, False, None, False),
            ("_label", "_label", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", str, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("origin", "origin", int, False, None, False),
            ("_origin", "_origin", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("params", "params", str, False, None, False),
            ("_params", "_params", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestHeader", "requestHeader", TestScriptSetupActionOperationRequestHeader, True, None, False),
            ("_requestHeader", "_requestHeader", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestId", "requestId", str, False, None, False),
            ("_requestId", "_requestId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("responseId", "responseId", str, False, None, False),
            ("_responseId", "_responseId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("_sourceId", "_sourceId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetId", "targetId", str, False, None, False),
            ("_targetId", "_targetId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """ Each operation can have one or more header elements.
    
    Header elements would be used to set HTTP headers.
    """
    
    resource_type = "TestScriptSetupActionOperationRequestHeader"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.field = None
        """ HTTP header field name.
        Type `str`. """
        self._field = None
        """ Primitive extension for field. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ HTTP headerfield value.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptSetupActionOperationRequestHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionOperationRequestHeader, self).elementProperties()
        js.extend([
            ("field", "field", str, False, None, True),
            ("_field", "_field", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptTeardown(backboneelement.BackboneElement):
    """ A series of required clean up steps.
    
    A series of operations required to clean up after all the tests are
    executed (successfully or otherwise).
    """
    
    resource_type = "TestScriptTeardown"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ One or more teardown operations to perform.
        List of `TestScriptTeardownAction` items (represented as `dict` in JSON). """
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptTeardown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTeardownAction, True, None, True),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations to perform.
    
    The teardown action will only contain an operation.
    """
    
    resource_type = "TestScriptTeardownAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ The teardown operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        self._operation = None
        """ Primitive extension for operation. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptTeardownAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, True),
            ("_operation", "_operation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptTest(backboneelement.BackboneElement):
    """ A test in this script.
    """
    
    resource_type = "TestScriptTest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A test operation or assert to perform.
        List of `TestScriptTestAction` items (represented as `dict` in JSON). """
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
        
        super(TestScriptTest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTest, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTestAction, True, None, True),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptTestAction(backboneelement.BackboneElement):
    """ A test operation or assert to perform.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_type = "TestScriptTestAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ The setup assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        self._assert_fhir = None
        """ Primitive extension for assert_fhir. Type `FHIRPrimitiveExtension` """
        
        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        self._operation = None
        """ Primitive extension for operation. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptTestAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTestAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
            ("_assert_fhir", "_assert_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
            ("_operation", "_operation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class TestScriptVariable(backboneelement.BackboneElement):
    """ Placeholder for evaluated elements.
    
    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """
    
    resource_type = "TestScriptVariable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.defaultValue = None
        """ Default, hard-coded, or user-defined value for this variable.
        Type `str`. """
        self._defaultValue = None
        """ Primitive extension for defaultValue. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the variable.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.expression = None
        """ The FHIRPath expression against the fixture body.
        Type `str`. """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.headerField = None
        """ HTTP header field name for source.
        Type `str`. """
        self._headerField = None
        """ Primitive extension for headerField. Type `FHIRPrimitiveExtension` """
        
        self.hint = None
        """ Hint help text for default value to enter.
        Type `str`. """
        self._hint = None
        """ Primitive extension for hint. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Descriptive name for this variable.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.path = None
        """ XPath or JSONPath against the fixture body.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        self.sourceId = None
        """ Fixture Id of source expression or headerField within this variable.
        Type `str`. """
        self._sourceId = None
        """ Primitive extension for sourceId. Type `FHIRPrimitiveExtension` """
        
        super(TestScriptVariable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptVariable, self).elementProperties()
        js.extend([
            ("defaultValue", "defaultValue", str, False, None, False),
            ("_defaultValue", "_defaultValue", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("_headerField", "_headerField", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("hint", "hint", str, False, None, False),
            ("_hint", "_hint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("path", "path", str, False, None, False),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("_sourceId", "_sourceId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import usagecontext