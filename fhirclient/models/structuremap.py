# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/StructureMap).
# 2024, SMART Health IT.


from . import domainresource

class StructureMap(domainresource.DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform
    data.
    """
    
    resource_type = "StructureMap"
    
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
        """ Natural language description of the structure map.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.group = None
        """ Named sections for reader convenience.
        List of `StructureMapGroup` items (represented as `dict` in JSON). """
        self._group = None
        """ Primitive extension for group. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the structure map.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.import_fhir = None
        """ Other maps used by this map (canonical URLs).
        List of `str` items. """
        self._import_fhir = None
        """ Primitive extension for import_fhir. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for structure map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this structure map (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this structure map is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.structure = None
        """ Structure Definition used by this map.
        List of `StructureMapStructure` items (represented as `dict` in JSON). """
        self._structure = None
        """ Primitive extension for structure. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this structure map (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this structure map, represented as a URI
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
        """ Business version of the structure map.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(StructureMap, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("group", "group", StructureMapGroup, True, None, True),
            ("_group", "_group", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("import_fhir", "import", str, True, None, False),
            ("_import_fhir", "_import_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("structure", "structure", StructureMapStructure, True, None, False),
            ("_structure", "_structure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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

class StructureMapGroup(backboneelement.BackboneElement):
    """ Named sections for reader convenience.
    
    Organizes the mapping into manageable chunks for human review/ease of
    maintenance.
    """
    
    resource_type = "StructureMapGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ Additional description/explanation for group.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.extends = None
        """ Another group that this group adds rules to.
        Type `str`. """
        self._extends = None
        """ Primitive extension for extends. Type `FHIRPrimitiveExtension` """
        
        self.input = None
        """ Named instance provided when invoking the map.
        List of `StructureMapGroupInput` items (represented as `dict` in JSON). """
        self._input = None
        """ Primitive extension for input. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Human-readable label.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.rule = None
        """ Transform Rule from source to target.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        self._rule = None
        """ Primitive extension for rule. Type `FHIRPrimitiveExtension` """
        
        self.typeMode = None
        """ none | types | type-and-types.
        Type `str`. """
        self._typeMode = None
        """ Primitive extension for typeMode. Type `FHIRPrimitiveExtension` """
        
        super(StructureMapGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroup, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("extends", "extends", str, False, None, False),
            ("_extends", "_extends", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("input", "input", StructureMapGroupInput, True, None, True),
            ("_input", "_input", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rule", "rule", StructureMapGroupRule, True, None, True),
            ("_rule", "_rule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("typeMode", "typeMode", str, False, None, True),
            ("_typeMode", "_typeMode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureMapGroupInput(backboneelement.BackboneElement):
    """ Named instance provided when invoking the map.
    
    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """
    
    resource_type = "StructureMapGroupInput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ Documentation for this instance of data.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.mode = None
        """ source | target.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this instance of data.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type for this instance of data.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(StructureMapGroupInput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupInput, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureMapGroupRule(backboneelement.BackboneElement):
    """ Transform Rule from source to target.
    """
    
    resource_type = "StructureMapGroupRule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dependent = None
        """ Which other rules to apply in the context of this rule.
        List of `StructureMapGroupRuleDependent` items (represented as `dict` in JSON). """
        self._dependent = None
        """ Primitive extension for dependent. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Documentation for this instance of data.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name of the rule for internal references.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.rule = None
        """ Rules contained in this rule.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        self._rule = None
        """ Primitive extension for rule. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Source inputs to the mapping.
        List of `StructureMapGroupRuleSource` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Content to create because of this mapping rule.
        List of `StructureMapGroupRuleTarget` items (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        super(StructureMapGroupRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRule, self).elementProperties()
        js.extend([
            ("dependent", "dependent", StructureMapGroupRuleDependent, True, None, False),
            ("_dependent", "_dependent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rule", "rule", StructureMapGroupRule, True, None, False),
            ("_rule", "_rule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", StructureMapGroupRuleSource, True, None, True),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", StructureMapGroupRuleTarget, True, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """ Which other rules to apply in the context of this rule.
    """
    
    resource_type = "StructureMapGroupRuleDependent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of a rule or group to apply.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.variable = None
        """ Variable to pass to the rule or group.
        List of `str` items. """
        self._variable = None
        """ Primitive extension for variable. Type `FHIRPrimitiveExtension` """
        
        super(StructureMapGroupRuleDependent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleDependent, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variable", "variable", str, True, None, True),
            ("_variable", "_variable", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """ Source inputs to the mapping.
    """
    
    resource_type = "StructureMapGroupRuleSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.check = None
        """ FHIRPath expression  - must be true or the mapping engine throws an
        error instead of completing.
        Type `str`. """
        self._check = None
        """ Primitive extension for check. Type `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ FHIRPath expression  - must be true or the rule does not apply.
        Type `str`. """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.context = None
        """ Type or variable this rule applies to.
        Type `str`. """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueAddress = None
        """ Default value if no value exists.
        Type `Address` (represented as `dict` in JSON). """
        self._defaultValueAddress = None
        """ Primitive extension for defaultValueAddress. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueAge = None
        """ Default value if no value exists.
        Type `Age` (represented as `dict` in JSON). """
        self._defaultValueAge = None
        """ Primitive extension for defaultValueAge. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueAnnotation = None
        """ Default value if no value exists.
        Type `Annotation` (represented as `dict` in JSON). """
        self._defaultValueAnnotation = None
        """ Primitive extension for defaultValueAnnotation. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueAttachment = None
        """ Default value if no value exists.
        Type `Attachment` (represented as `dict` in JSON). """
        self._defaultValueAttachment = None
        """ Primitive extension for defaultValueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueBase64Binary = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueBase64Binary = None
        """ Primitive extension for defaultValueBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueBoolean = None
        """ Default value if no value exists.
        Type `bool`. """
        self._defaultValueBoolean = None
        """ Primitive extension for defaultValueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCanonical = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueCanonical = None
        """ Primitive extension for defaultValueCanonical. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCode = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueCode = None
        """ Primitive extension for defaultValueCode. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCodeableConcept = None
        """ Default value if no value exists.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._defaultValueCodeableConcept = None
        """ Primitive extension for defaultValueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCoding = None
        """ Default value if no value exists.
        Type `Coding` (represented as `dict` in JSON). """
        self._defaultValueCoding = None
        """ Primitive extension for defaultValueCoding. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueContactDetail = None
        """ Default value if no value exists.
        Type `ContactDetail` (represented as `dict` in JSON). """
        self._defaultValueContactDetail = None
        """ Primitive extension for defaultValueContactDetail. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueContactPoint = None
        """ Default value if no value exists.
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._defaultValueContactPoint = None
        """ Primitive extension for defaultValueContactPoint. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueContributor = None
        """ Default value if no value exists.
        Type `Contributor` (represented as `dict` in JSON). """
        self._defaultValueContributor = None
        """ Primitive extension for defaultValueContributor. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCount = None
        """ Default value if no value exists.
        Type `Count` (represented as `dict` in JSON). """
        self._defaultValueCount = None
        """ Primitive extension for defaultValueCount. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDataRequirement = None
        """ Default value if no value exists.
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._defaultValueDataRequirement = None
        """ Primitive extension for defaultValueDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDate = None
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._defaultValueDate = None
        """ Primitive extension for defaultValueDate. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDateTime = None
        """ Default value if no value exists.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._defaultValueDateTime = None
        """ Primitive extension for defaultValueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDecimal = None
        """ Default value if no value exists.
        Type `float`. """
        self._defaultValueDecimal = None
        """ Primitive extension for defaultValueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDistance = None
        """ Default value if no value exists.
        Type `Distance` (represented as `dict` in JSON). """
        self._defaultValueDistance = None
        """ Primitive extension for defaultValueDistance. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDosage = None
        """ Default value if no value exists.
        Type `Dosage` (represented as `dict` in JSON). """
        self._defaultValueDosage = None
        """ Primitive extension for defaultValueDosage. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDuration = None
        """ Default value if no value exists.
        Type `Duration` (represented as `dict` in JSON). """
        self._defaultValueDuration = None
        """ Primitive extension for defaultValueDuration. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueExpression = None
        """ Default value if no value exists.
        Type `Expression` (represented as `dict` in JSON). """
        self._defaultValueExpression = None
        """ Primitive extension for defaultValueExpression. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueHumanName = None
        """ Default value if no value exists.
        Type `HumanName` (represented as `dict` in JSON). """
        self._defaultValueHumanName = None
        """ Primitive extension for defaultValueHumanName. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueId = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueId = None
        """ Primitive extension for defaultValueId. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueIdentifier = None
        """ Default value if no value exists.
        Type `Identifier` (represented as `dict` in JSON). """
        self._defaultValueIdentifier = None
        """ Primitive extension for defaultValueIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueInstant = None
        """ Default value if no value exists.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._defaultValueInstant = None
        """ Primitive extension for defaultValueInstant. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueInteger = None
        """ Default value if no value exists.
        Type `int`. """
        self._defaultValueInteger = None
        """ Primitive extension for defaultValueInteger. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueMarkdown = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueMarkdown = None
        """ Primitive extension for defaultValueMarkdown. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueMeta = None
        """ Default value if no value exists.
        Type `Meta` (represented as `dict` in JSON). """
        self._defaultValueMeta = None
        """ Primitive extension for defaultValueMeta. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueMoney = None
        """ Default value if no value exists.
        Type `Money` (represented as `dict` in JSON). """
        self._defaultValueMoney = None
        """ Primitive extension for defaultValueMoney. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueOid = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueOid = None
        """ Primitive extension for defaultValueOid. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueParameterDefinition = None
        """ Default value if no value exists.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        self._defaultValueParameterDefinition = None
        """ Primitive extension for defaultValueParameterDefinition. Type `FHIRPrimitiveExtension` """
        
        self.defaultValuePeriod = None
        """ Default value if no value exists.
        Type `Period` (represented as `dict` in JSON). """
        self._defaultValuePeriod = None
        """ Primitive extension for defaultValuePeriod. Type `FHIRPrimitiveExtension` """
        
        self.defaultValuePositiveInt = None
        """ Default value if no value exists.
        Type `int`. """
        self._defaultValuePositiveInt = None
        """ Primitive extension for defaultValuePositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueQuantity = None
        """ Default value if no value exists.
        Type `Quantity` (represented as `dict` in JSON). """
        self._defaultValueQuantity = None
        """ Primitive extension for defaultValueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueRange = None
        """ Default value if no value exists.
        Type `Range` (represented as `dict` in JSON). """
        self._defaultValueRange = None
        """ Primitive extension for defaultValueRange. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueRatio = None
        """ Default value if no value exists.
        Type `Ratio` (represented as `dict` in JSON). """
        self._defaultValueRatio = None
        """ Primitive extension for defaultValueRatio. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueReference = None
        """ Default value if no value exists.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._defaultValueReference = None
        """ Primitive extension for defaultValueReference. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueRelatedArtifact = None
        """ Default value if no value exists.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        self._defaultValueRelatedArtifact = None
        """ Primitive extension for defaultValueRelatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueSampledData = None
        """ Default value if no value exists.
        Type `SampledData` (represented as `dict` in JSON). """
        self._defaultValueSampledData = None
        """ Primitive extension for defaultValueSampledData. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueSignature = None
        """ Default value if no value exists.
        Type `Signature` (represented as `dict` in JSON). """
        self._defaultValueSignature = None
        """ Primitive extension for defaultValueSignature. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueString = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueString = None
        """ Primitive extension for defaultValueString. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueTime = None
        """ Default value if no value exists.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._defaultValueTime = None
        """ Primitive extension for defaultValueTime. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueTiming = None
        """ Default value if no value exists.
        Type `Timing` (represented as `dict` in JSON). """
        self._defaultValueTiming = None
        """ Primitive extension for defaultValueTiming. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueTriggerDefinition = None
        """ Default value if no value exists.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        self._defaultValueTriggerDefinition = None
        """ Primitive extension for defaultValueTriggerDefinition. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUnsignedInt = None
        """ Default value if no value exists.
        Type `int`. """
        self._defaultValueUnsignedInt = None
        """ Primitive extension for defaultValueUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUri = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueUri = None
        """ Primitive extension for defaultValueUri. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUrl = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueUrl = None
        """ Primitive extension for defaultValueUrl. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUsageContext = None
        """ Default value if no value exists.
        Type `UsageContext` (represented as `dict` in JSON). """
        self._defaultValueUsageContext = None
        """ Primitive extension for defaultValueUsageContext. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUuid = None
        """ Default value if no value exists.
        Type `str`. """
        self._defaultValueUuid = None
        """ Primitive extension for defaultValueUuid. Type `FHIRPrimitiveExtension` """
        
        self.element = None
        """ Optional field for this source.
        Type `str`. """
        self._element = None
        """ Primitive extension for element. Type `FHIRPrimitiveExtension` """
        
        self.listMode = None
        """ first | not_first | last | not_last | only_one.
        Type `str`. """
        self._listMode = None
        """ Primitive extension for listMode. Type `FHIRPrimitiveExtension` """
        
        self.logMessage = None
        """ Message to put in log if source exists (FHIRPath).
        Type `str`. """
        self._logMessage = None
        """ Primitive extension for logMessage. Type `FHIRPrimitiveExtension` """
        
        self.max = None
        """ Specified maximum cardinality (number or *).
        Type `str`. """
        self._max = None
        """ Primitive extension for max. Type `FHIRPrimitiveExtension` """
        
        self.min = None
        """ Specified minimum cardinality.
        Type `int`. """
        self._min = None
        """ Primitive extension for min. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Rule only applies if source has this type.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.variable = None
        """ Named context for field, if a field is specified.
        Type `str`. """
        self._variable = None
        """ Primitive extension for variable. Type `FHIRPrimitiveExtension` """
        
        super(StructureMapGroupRuleSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleSource, self).elementProperties()
        js.extend([
            ("check", "check", str, False, None, False),
            ("_check", "_check", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("context", "context", str, False, None, True),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False),
            ("_defaultValueAddress", "_defaultValueAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueAge", "defaultValueAge", age.Age, False, "defaultValue", False),
            ("_defaultValueAge", "_defaultValueAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False),
            ("_defaultValueAnnotation", "_defaultValueAnnotation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False),
            ("_defaultValueAttachment", "_defaultValueAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("_defaultValueBase64Binary", "_defaultValueBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("_defaultValueBoolean", "_defaultValueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("_defaultValueCanonical", "_defaultValueCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("_defaultValueCode", "_defaultValueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False),
            ("_defaultValueCodeableConcept", "_defaultValueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False),
            ("_defaultValueCoding", "_defaultValueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, False, "defaultValue", False),
            ("_defaultValueContactDetail", "_defaultValueContactDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False),
            ("_defaultValueContactPoint", "_defaultValueContactPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, False, "defaultValue", False),
            ("_defaultValueContributor", "_defaultValueContributor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCount", "defaultValueCount", count.Count, False, "defaultValue", False),
            ("_defaultValueCount", "_defaultValueCount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, False, "defaultValue", False),
            ("_defaultValueDataRequirement", "_defaultValueDataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, False, "defaultValue", False),
            ("_defaultValueDate", "_defaultValueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdatetime.FHIRDateTime, False, "defaultValue", False),
            ("_defaultValueDateTime", "_defaultValueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("_defaultValueDecimal", "_defaultValueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, False, "defaultValue", False),
            ("_defaultValueDistance", "_defaultValueDistance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, False, "defaultValue", False),
            ("_defaultValueDosage", "_defaultValueDosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, False, "defaultValue", False),
            ("_defaultValueDuration", "_defaultValueDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, False, "defaultValue", False),
            ("_defaultValueExpression", "_defaultValueExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False),
            ("_defaultValueHumanName", "_defaultValueHumanName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("_defaultValueId", "_defaultValueId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False),
            ("_defaultValueIdentifier", "_defaultValueIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueInstant", "defaultValueInstant", fhirinstant.FHIRInstant, False, "defaultValue", False),
            ("_defaultValueInstant", "_defaultValueInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("_defaultValueInteger", "_defaultValueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("_defaultValueMarkdown", "_defaultValueMarkdown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueMeta", "defaultValueMeta", meta.Meta, False, "defaultValue", False),
            ("_defaultValueMeta", "_defaultValueMeta", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, False, "defaultValue", False),
            ("_defaultValueMoney", "_defaultValueMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("_defaultValueOid", "_defaultValueOid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, False, "defaultValue", False),
            ("_defaultValueParameterDefinition", "_defaultValueParameterDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False),
            ("_defaultValuePeriod", "_defaultValuePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("_defaultValuePositiveInt", "_defaultValuePositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False),
            ("_defaultValueQuantity", "_defaultValueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False),
            ("_defaultValueRange", "_defaultValueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False),
            ("_defaultValueRatio", "_defaultValueRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False),
            ("_defaultValueReference", "_defaultValueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, False, "defaultValue", False),
            ("_defaultValueRelatedArtifact", "_defaultValueRelatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False),
            ("_defaultValueSampledData", "_defaultValueSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False),
            ("_defaultValueSignature", "_defaultValueSignature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("_defaultValueString", "_defaultValueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueTime", "defaultValueTime", fhirtime.FHIRTime, False, "defaultValue", False),
            ("_defaultValueTime", "_defaultValueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False),
            ("_defaultValueTiming", "_defaultValueTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "defaultValue", False),
            ("_defaultValueTriggerDefinition", "_defaultValueTriggerDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("_defaultValueUnsignedInt", "_defaultValueUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("_defaultValueUri", "_defaultValueUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("_defaultValueUrl", "_defaultValueUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, False, "defaultValue", False),
            ("_defaultValueUsageContext", "_defaultValueUsageContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("_defaultValueUuid", "_defaultValueUuid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("element", "element", str, False, None, False),
            ("_element", "_element", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("listMode", "listMode", str, False, None, False),
            ("_listMode", "_listMode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("logMessage", "logMessage", str, False, None, False),
            ("_logMessage", "_logMessage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("max", "max", str, False, None, False),
            ("_max", "_max", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("min", "min", int, False, None, False),
            ("_min", "_min", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variable", "variable", str, False, None, False),
            ("_variable", "_variable", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """ Content to create because of this mapping rule.
    """
    
    resource_type = "StructureMapGroupRuleTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.context = None
        """ Type or variable this rule applies to.
        Type `str`. """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.contextType = None
        """ type | variable.
        Type `str`. """
        self._contextType = None
        """ Primitive extension for contextType. Type `FHIRPrimitiveExtension` """
        
        self.element = None
        """ Field to create in the context.
        Type `str`. """
        self._element = None
        """ Primitive extension for element. Type `FHIRPrimitiveExtension` """
        
        self.listMode = None
        """ first | share | last | collate.
        List of `str` items. """
        self._listMode = None
        """ Primitive extension for listMode. Type `FHIRPrimitiveExtension` """
        
        self.listRuleId = None
        """ Internal rule reference for shared list items.
        Type `str`. """
        self._listRuleId = None
        """ Primitive extension for listRuleId. Type `FHIRPrimitiveExtension` """
        
        self.parameter = None
        """ Parameters to the transform.
        List of `StructureMapGroupRuleTargetParameter` items (represented as `dict` in JSON). """
        self._parameter = None
        """ Primitive extension for parameter. Type `FHIRPrimitiveExtension` """
        
        self.transform = None
        """ create | copy +.
        Type `str`. """
        self._transform = None
        """ Primitive extension for transform. Type `FHIRPrimitiveExtension` """
        
        self.variable = None
        """ Named context for field, if desired, and a field is specified.
        Type `str`. """
        self._variable = None
        """ Primitive extension for variable. Type `FHIRPrimitiveExtension` """
        
        super(StructureMapGroupRuleTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleTarget, self).elementProperties()
        js.extend([
            ("context", "context", str, False, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contextType", "contextType", str, False, None, False),
            ("_contextType", "_contextType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("element", "element", str, False, None, False),
            ("_element", "_element", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("listMode", "listMode", str, True, None, False),
            ("_listMode", "_listMode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("listRuleId", "listRuleId", str, False, None, False),
            ("_listRuleId", "_listRuleId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parameter", "parameter", StructureMapGroupRuleTargetParameter, True, None, False),
            ("_parameter", "_parameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("transform", "transform", str, False, None, False),
            ("_transform", "_transform", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("variable", "variable", str, False, None, False),
            ("_variable", "_variable", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """ Parameters to the transform.
    """
    
    resource_type = "StructureMapGroupRuleTargetParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueBoolean = None
        """ Parameter value - variable or literal.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ Parameter value - variable or literal.
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueId = None
        """ Parameter value - variable or literal.
        Type `str`. """
        self._valueId = None
        """ Primitive extension for valueId. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Parameter value - variable or literal.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Parameter value - variable or literal.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        super(StructureMapGroupRuleTargetParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleTargetParameter, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueId", "valueId", str, False, "value", True),
            ("_valueId", "_valueId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class StructureMapStructure(backboneelement.BackboneElement):
    """ Structure Definition used by this map.
    
    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """
    
    resource_type = "StructureMapStructure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias = None
        """ Name for type in this map.
        Type `str`. """
        self._alias = None
        """ Primitive extension for alias. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Documentation on use of structure.
        Type `str`. """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.mode = None
        """ source | queried | target | produced.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical reference to structure definition.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(StructureMapStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapStructure, self).elementProperties()
        js.extend([
            ("alias", "alias", str, False, None, False),
            ("_alias", "_alias", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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