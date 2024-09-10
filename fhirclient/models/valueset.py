# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ValueSet).
# 2024, SMART Health IT.


from . import domainresource

class ValueSet(domainresource.DomainResource):
    """ A set of codes drawn from one or more code systems.
    
    A ValueSet resource instance specifies a set of codes drawn from one or
    more code systems, intended for use in a particular context. Value sets
    link between [CodeSystem](codesystem.html) definitions and their use in
    [coded elements](terminologies.html).
    """
    
    resource_type = "ValueSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compose = None
        """ Content logical definition of the value set (CLD).
        Type `ValueSetCompose` (represented as `dict` in JSON). """
        self._compose = None
        """ Primitive extension for compose. Type `FHIRPrimitiveExtension` """
        
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
        """ Natural language description of the value set.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.expansion = None
        """ Used when the value set is "expanded".
        Type `ValueSetExpansion` (represented as `dict` in JSON). """
        self._expansion = None
        """ Primitive extension for expansion. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the value set (business identifier).
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.immutable = None
        """ Indicates whether or not any change to the content logical
        definition may occur.
        Type `bool`. """
        self._immutable = None
        """ Primitive extension for immutable. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for value set (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this value set (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this value set is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this value set (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this value set, represented as a URI
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
        """ Business version of the value set.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ValueSet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSet, self).elementProperties()
        js.extend([
            ("compose", "compose", ValueSetCompose, False, None, False),
            ("_compose", "_compose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expansion", "expansion", ValueSetExpansion, False, None, False),
            ("_expansion", "_expansion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("immutable", "immutable", bool, False, None, False),
            ("_immutable", "_immutable", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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

class ValueSetCompose(backboneelement.BackboneElement):
    """ Content logical definition of the value set (CLD).
    
    A set of criteria that define the contents of the value set by including or
    excluding codes selected from the specified code system(s) that the value
    set draws from. This is also known as the Content Logical Definition (CLD).
    """
    
    resource_type = "ValueSetCompose"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exclude = None
        """ Explicitly exclude codes from a code system or other value sets.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        self._exclude = None
        """ Primitive extension for exclude. Type `FHIRPrimitiveExtension` """
        
        self.inactive = None
        """ Whether inactive codes are in the value set.
        Type `bool`. """
        self._inactive = None
        """ Primitive extension for inactive. Type `FHIRPrimitiveExtension` """
        
        self.include = None
        """ Include one or more codes from a code system or other value set(s).
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        self._include = None
        """ Primitive extension for include. Type `FHIRPrimitiveExtension` """
        
        self.lockedDate = None
        """ Fixed date for references with no specified version (transitive).
        Type `FHIRDate` (represented as `str` in JSON). """
        self._lockedDate = None
        """ Primitive extension for lockedDate. Type `FHIRPrimitiveExtension` """
        
        super(ValueSetCompose, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetCompose, self).elementProperties()
        js.extend([
            ("exclude", "exclude", ValueSetComposeInclude, True, None, False),
            ("_exclude", "_exclude", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("_inactive", "_inactive", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("include", "include", ValueSetComposeInclude, True, None, True),
            ("_include", "_include", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lockedDate", "lockedDate", fhirdate.FHIRDate, False, None, False),
            ("_lockedDate", "_lockedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """ Include one or more codes from a code system or other value set(s).
    """
    
    resource_type = "ValueSetComposeInclude"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.concept = None
        """ A concept defined in the system.
        List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON). """
        self._concept = None
        """ Primitive extension for concept. Type `FHIRPrimitiveExtension` """
        
        self.filter = None
        """ Select codes/concepts by their properties (including relationships).
        List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON). """
        self._filter = None
        """ Primitive extension for filter. Type `FHIRPrimitiveExtension` """
        
        self.system = None
        """ The system the codes come from.
        Type `str`. """
        self._system = None
        """ Primitive extension for system. Type `FHIRPrimitiveExtension` """
        
        self.valueSet = None
        """ Select the contents included in this value set.
        List of `str` items. """
        self._valueSet = None
        """ Primitive extension for valueSet. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Specific version of the code system referred to.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ValueSetComposeInclude, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeInclude, self).elementProperties()
        js.extend([
            ("concept", "concept", ValueSetComposeIncludeConcept, True, None, False),
            ("_concept", "_concept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("filter", "filter", ValueSetComposeIncludeFilter, True, None, False),
            ("_filter", "_filter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSet", "valueSet", str, True, None, False),
            ("_valueSet", "_valueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """ A concept defined in the system.
    
    Specifies a concept to be included or excluded.
    """
    
    resource_type = "ValueSetComposeIncludeConcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code or expression from system.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.designation = None
        """ Additional representations for this concept.
        List of `ValueSetComposeIncludeConceptDesignation` items (represented as `dict` in JSON). """
        self._designation = None
        """ Primitive extension for designation. Type `FHIRPrimitiveExtension` """
        
        self.display = None
        """ Text to display for this code for this value set in this valueset.
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        super(ValueSetComposeIncludeConcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
            ("_designation", "_designation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ValueSetComposeIncludeConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for this concept.
    
    Additional representations for this concept when used in this value set -
    other languages, aliases, specialized purposes, used for particular
    purposes, etc.
    """
    
    resource_type = "ValueSetComposeIncludeConceptDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ Human language of the designation.
        Type `str`. """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ Types of uses of designations.
        Type `Coding` (represented as `dict` in JSON). """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The text value for this designation.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(ValueSetComposeIncludeConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """ Select codes/concepts by their properties (including relationships).
    
    Select concepts by specify a matching criterion based on the properties
    (including relationships) defined by the system, or on filters defined by
    the system. If multiple filters are specified, they SHALL all be true.
    """
    
    resource_type = "ValueSetComposeIncludeFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.op = None
        """ = | is-a | descendent-of | is-not-a | regex | in | not-in |
        generalizes | exists.
        Type `str`. """
        self._op = None
        """ Primitive extension for op. Type `FHIRPrimitiveExtension` """
        
        self.property = None
        """ A property/filter defined by the code system.
        Type `str`. """
        self._property = None
        """ Primitive extension for property. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ Code from the system, or regex criteria, or boolean value for
        exists.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(ValueSetComposeIncludeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeFilter, self).elementProperties()
        js.extend([
            ("op", "op", str, False, None, True),
            ("_op", "_op", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("property", "property", str, False, None, True),
            ("_property", "_property", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ValueSetExpansion(backboneelement.BackboneElement):
    """ Used when the value set is "expanded".
    
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """
    
    resource_type = "ValueSetExpansion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contains = None
        """ Codes in the value set.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        self._contains = None
        """ Primitive extension for contains. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifies the value set expansion (business identifier).
        Type `str`. """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.offset = None
        """ Offset at which this resource starts.
        Type `int`. """
        self._offset = None
        """ Primitive extension for offset. Type `FHIRPrimitiveExtension` """
        
        self.parameter = None
        """ Parameter that controlled the expansion process.
        List of `ValueSetExpansionParameter` items (represented as `dict` in JSON). """
        self._parameter = None
        """ Primitive extension for parameter. Type `FHIRPrimitiveExtension` """
        
        self.timestamp = None
        """ Time ValueSet expansion happened.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._timestamp = None
        """ Primitive extension for timestamp. Type `FHIRPrimitiveExtension` """
        
        self.total = None
        """ Total number of codes in the expansion.
        Type `int`. """
        self._total = None
        """ Primitive extension for total. Type `FHIRPrimitiveExtension` """
        
        super(ValueSetExpansion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansion, self).elementProperties()
        js.extend([
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("_contains", "_contains", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", str, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("_offset", "_offset", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parameter", "parameter", ValueSetExpansionParameter, True, None, False),
            ("_parameter", "_parameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timestamp", "timestamp", fhirdatetime.FHIRDateTime, False, None, True),
            ("_timestamp", "_timestamp", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("total", "total", int, False, None, False),
            ("_total", "_total", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """ Codes in the value set.
    
    The codes that are contained in the value set expansion.
    """
    
    resource_type = "ValueSetExpansionContains"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abstract = None
        """ If user cannot select this entry.
        Type `bool`. """
        self._abstract = None
        """ Primitive extension for abstract. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Code - if blank, this is not a selectable code.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.contains = None
        """ Codes contained under this entry.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        self._contains = None
        """ Primitive extension for contains. Type `FHIRPrimitiveExtension` """
        
        self.designation = None
        """ Additional representations for this item.
        List of `ValueSetComposeIncludeConceptDesignation` items (represented as `dict` in JSON). """
        self._designation = None
        """ Primitive extension for designation. Type `FHIRPrimitiveExtension` """
        
        self.display = None
        """ User display for the concept.
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        self.inactive = None
        """ If concept is inactive in the code system.
        Type `bool`. """
        self._inactive = None
        """ Primitive extension for inactive. Type `FHIRPrimitiveExtension` """
        
        self.system = None
        """ System value for the code.
        Type `str`. """
        self._system = None
        """ Primitive extension for system. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Version in which this code/display is defined.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ValueSetExpansionContains, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionContains, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, False),
            ("_abstract", "_abstract", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", str, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("_contains", "_contains", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
            ("_designation", "_designation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("_inactive", "_inactive", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """ Parameter that controlled the expansion process.
    
    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """
    
    resource_type = "ValueSetExpansionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name as assigned by the client or server.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Value of the named parameter.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCode = None
        """ Value of the named parameter.
        Type `str`. """
        self._valueCode = None
        """ Primitive extension for valueCode. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ Value of the named parameter.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ Value of the named parameter.
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Value of the named parameter.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Value of the named parameter.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueUri = None
        """ Value of the named parameter.
        Type `str`. """
        self._valueUri = None
        """ Primitive extension for valueUri. Type `FHIRPrimitiveExtension` """
        
        super(ValueSetExpansionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("_valueCode", "_valueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", False),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("_valueDecimal", "_valueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("_valueUri", "_valueUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirdatetime
from . import identifier
from . import usagecontext