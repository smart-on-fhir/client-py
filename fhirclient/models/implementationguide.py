# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide).
# 2024, SMART Health IT.


from . import domainresource

class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.
    
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """
    
    resource_type = "ImplementationGuide"
    
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
        
        self.definition = None
        """ Information needed to build the IG.
        Type `ImplementationGuideDefinition` (represented as `dict` in JSON). """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.dependsOn = None
        """ Another Implementation guide this depends on.
        List of `ImplementationGuideDependsOn` items (represented as `dict` in JSON). """
        self._dependsOn = None
        """ Primitive extension for dependsOn. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the implementation guide.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.fhirVersion = None
        """ FHIR Version(s) this Implementation Guide targets.
        List of `str` items. """
        self._fhirVersion = None
        """ Primitive extension for fhirVersion. Type `FHIRPrimitiveExtension` """
        
        self.global_fhir = None
        """ Profiles that apply globally.
        List of `ImplementationGuideGlobal` items (represented as `dict` in JSON). """
        self._global_fhir = None
        """ Primitive extension for global_fhir. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for implementation guide (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.license = None
        """ SPDX license code for this IG (or not-open-source).
        Type `str`. """
        self._license = None
        """ Primitive extension for license. Type `FHIRPrimitiveExtension` """
        
        self.manifest = None
        """ Information about an assembled IG.
        Type `ImplementationGuideManifest` (represented as `dict` in JSON). """
        self._manifest = None
        """ Primitive extension for manifest. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this implementation guide (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.packageId = None
        """ NPM Package name for IG.
        Type `str`. """
        self._packageId = None
        """ Primitive extension for packageId. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this implementation guide (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this implementation guide, represented as
        a URI (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the implementation guide.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuide, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuide, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definition", "definition", ImplementationGuideDefinition, False, None, False),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dependsOn", "dependsOn", ImplementationGuideDependsOn, True, None, False),
            ("_dependsOn", "_dependsOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fhirVersion", "fhirVersion", str, True, None, True),
            ("_fhirVersion", "_fhirVersion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("global_fhir", "global", ImplementationGuideGlobal, True, None, False),
            ("_global_fhir", "_global_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("license", "license", str, False, None, False),
            ("_license", "_license", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manifest", "manifest", ImplementationGuideManifest, False, None, False),
            ("_manifest", "_manifest", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("packageId", "packageId", str, False, None, True),
            ("_packageId", "_packageId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ImplementationGuideDefinition(backboneelement.BackboneElement):
    """ Information needed to build the IG.
    
    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """
    
    resource_type = "ImplementationGuideDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.grouping = None
        """ Grouping used to present related resources in the IG.
        List of `ImplementationGuideDefinitionGrouping` items (represented as `dict` in JSON). """
        self._grouping = None
        """ Primitive extension for grouping. Type `FHIRPrimitiveExtension` """
        
        self.page = None
        """ Page/Section in the Guide.
        Type `ImplementationGuideDefinitionPage` (represented as `dict` in JSON). """
        self._page = None
        """ Primitive extension for page. Type `FHIRPrimitiveExtension` """
        
        self.parameter = None
        """ Defines how IG is built by tools.
        List of `ImplementationGuideDefinitionParameter` items (represented as `dict` in JSON). """
        self._parameter = None
        """ Primitive extension for parameter. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ Resource in the implementation guide.
        List of `ImplementationGuideDefinitionResource` items (represented as `dict` in JSON). """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.template = None
        """ A template for building resources.
        List of `ImplementationGuideDefinitionTemplate` items (represented as `dict` in JSON). """
        self._template = None
        """ Primitive extension for template. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinition, self).elementProperties()
        js.extend([
            ("grouping", "grouping", ImplementationGuideDefinitionGrouping, True, None, False),
            ("_grouping", "_grouping", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("page", "page", ImplementationGuideDefinitionPage, False, None, False),
            ("_page", "_page", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parameter", "parameter", ImplementationGuideDefinitionParameter, True, None, False),
            ("_parameter", "_parameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", ImplementationGuideDefinitionResource, True, None, True),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("template", "template", ImplementationGuideDefinitionTemplate, True, None, False),
            ("_template", "_template", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    """ Grouping used to present related resources in the IG.
    
    A logical group of resources. Logical groups can be used when building
    pages.
    """
    
    resource_type = "ImplementationGuideDefinitionGrouping"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Human readable text describing the package.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Descriptive name for the package.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideDefinitionGrouping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionGrouping, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.
    
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    
    resource_type = "ImplementationGuideDefinitionPage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.generation = None
        """ html | markdown | xml | generated.
        Type `str`. """
        self._generation = None
        """ Primitive extension for generation. Type `FHIRPrimitiveExtension` """
        
        self.nameReference = None
        """ Where to find that page.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._nameReference = None
        """ Primitive extension for nameReference. Type `FHIRPrimitiveExtension` """
        
        self.nameUrl = None
        """ Where to find that page.
        Type `str`. """
        self._nameUrl = None
        """ Primitive extension for nameUrl. Type `FHIRPrimitiveExtension` """
        
        self.page = None
        """ Nested Pages / Sections.
        List of `ImplementationGuideDefinitionPage` items (represented as `dict` in JSON). """
        self._page = None
        """ Primitive extension for page. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Short title shown for navigational assistance.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideDefinitionPage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionPage, self).elementProperties()
        js.extend([
            ("generation", "generation", str, False, None, True),
            ("_generation", "_generation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("nameReference", "nameReference", fhirreference.FHIRReference, False, "name", True),
            ("_nameReference", "_nameReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("nameUrl", "nameUrl", str, False, "name", True),
            ("_nameUrl", "_nameUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("page", "page", ImplementationGuideDefinitionPage, True, None, False),
            ("_page", "_page", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, True),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideDefinitionParameter(backboneelement.BackboneElement):
    """ Defines how IG is built by tools.
    """
    
    resource_type = "ImplementationGuideDefinitionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ apply | path-resource | path-pages | path-tx-cache | expansion-
        parameter | rule-broken-links | generate-xml | generate-json |
        generate-turtle | html-template.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ Value for named type.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionParameter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    resource_type = "ImplementationGuideDefinitionResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Reason why included in guide.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.exampleBoolean = None
        """ Is an example/What is this an example of?.
        Type `bool`. """
        self._exampleBoolean = None
        """ Primitive extension for exampleBoolean. Type `FHIRPrimitiveExtension` """
        
        self.exampleCanonical = None
        """ Is an example/What is this an example of?.
        Type `str`. """
        self._exampleCanonical = None
        """ Primitive extension for exampleCanonical. Type `FHIRPrimitiveExtension` """
        
        self.fhirVersion = None
        """ Versions this applies to (if different to IG).
        List of `str` items. """
        self._fhirVersion = None
        """ Primitive extension for fhirVersion. Type `FHIRPrimitiveExtension` """
        
        self.groupingId = None
        """ Grouping this is part of.
        Type `str`. """
        self._groupingId = None
        """ Primitive extension for groupingId. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Human Name for the resource.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.reference = None
        """ Location of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideDefinitionResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionResource, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("_exampleBoolean", "_exampleBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("_exampleCanonical", "_exampleCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fhirVersion", "fhirVersion", str, True, None, False),
            ("_fhirVersion", "_fhirVersion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("groupingId", "groupingId", str, False, None, False),
            ("_groupingId", "_groupingId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideDefinitionTemplate(backboneelement.BackboneElement):
    """ A template for building resources.
    """
    
    resource_type = "ImplementationGuideDefinitionTemplate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of template specified.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.scope = None
        """ The scope in which the template applies.
        Type `str`. """
        self._scope = None
        """ Primitive extension for scope. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ The source location for the template.
        Type `str`. """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideDefinitionTemplate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionTemplate, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("scope", "scope", str, False, None, False),
            ("_scope", "_scope", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", str, False, None, True),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.
    
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    
    resource_type = "ImplementationGuideDependsOn"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.packageId = None
        """ NPM Package name for IG this depends on.
        Type `str`. """
        self._packageId = None
        """ Primitive extension for packageId. Type `FHIRPrimitiveExtension` """
        
        self.uri = None
        """ Identity of the IG that this depends on.
        Type `str`. """
        self._uri = None
        """ Primitive extension for uri. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Version of the IG.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideDependsOn, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDependsOn, self).elementProperties()
        js.extend([
            ("packageId", "packageId", str, False, None, False),
            ("_packageId", "_packageId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("uri", "uri", str, False, None, True),
            ("_uri", "_uri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.
    
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    
    resource_type = "ImplementationGuideGlobal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.profile = None
        """ Profile that all resources must conform to.
        Type `str`. """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type this profile applies to.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideGlobal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend([
            ("profile", "profile", str, False, None, True),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideManifest(backboneelement.BackboneElement):
    """ Information about an assembled IG.
    
    Information about an assembled implementation guide, created by the
    publication tooling.
    """
    
    resource_type = "ImplementationGuideManifest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.image = None
        """ Image within the IG.
        List of `str` items. """
        self._image = None
        """ Primitive extension for image. Type `FHIRPrimitiveExtension` """
        
        self.other = None
        """ Additional linkable file in IG.
        List of `str` items. """
        self._other = None
        """ Primitive extension for other. Type `FHIRPrimitiveExtension` """
        
        self.page = None
        """ HTML page within the parent IG.
        List of `ImplementationGuideManifestPage` items (represented as `dict` in JSON). """
        self._page = None
        """ Primitive extension for page. Type `FHIRPrimitiveExtension` """
        
        self.rendering = None
        """ Location of rendered implementation guide.
        Type `str`. """
        self._rendering = None
        """ Primitive extension for rendering. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ Resource in the implementation guide.
        List of `ImplementationGuideManifestResource` items (represented as `dict` in JSON). """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideManifest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideManifest, self).elementProperties()
        js.extend([
            ("image", "image", str, True, None, False),
            ("_image", "_image", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("other", "other", str, True, None, False),
            ("_other", "_other", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("page", "page", ImplementationGuideManifestPage, True, None, False),
            ("_page", "_page", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rendering", "rendering", str, False, None, False),
            ("_rendering", "_rendering", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", ImplementationGuideManifestResource, True, None, True),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    """ HTML page within the parent IG.
    
    Information about a page within the IG.
    """
    
    resource_type = "ImplementationGuideManifestPage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.anchor = None
        """ Anchor available on the page.
        List of `str` items. """
        self._anchor = None
        """ Primitive extension for anchor. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ HTML page name.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Title of the page, for references.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideManifestPage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideManifestPage, self).elementProperties()
        js.extend([
            ("anchor", "anchor", str, True, None, False),
            ("_anchor", "_anchor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    resource_type = "ImplementationGuideManifestResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exampleBoolean = None
        """ Is an example/What is this an example of?.
        Type `bool`. """
        self._exampleBoolean = None
        """ Primitive extension for exampleBoolean. Type `FHIRPrimitiveExtension` """
        
        self.exampleCanonical = None
        """ Is an example/What is this an example of?.
        Type `str`. """
        self._exampleCanonical = None
        """ Primitive extension for exampleCanonical. Type `FHIRPrimitiveExtension` """
        
        self.reference = None
        """ Location of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        self.relativePath = None
        """ Relative path for page in IG.
        Type `str`. """
        self._relativePath = None
        """ Primitive extension for relativePath. Type `FHIRPrimitiveExtension` """
        
        super(ImplementationGuideManifestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideManifestResource, self).elementProperties()
        js.extend([
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("_exampleBoolean", "_exampleBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("_exampleCanonical", "_exampleCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relativePath", "relativePath", str, False, None, False),
            ("_relativePath", "_relativePath", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import fhirreference
from . import usagecontext