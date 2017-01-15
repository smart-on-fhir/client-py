#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/StructureMap) on 2017-01-15.
#  2017, SMART Health IT.


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
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the structure map.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.group = None
        """ Named sections for reader convenience.
        List of `StructureMapGroup` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the structure map.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.import_fhir = None
        """ Other maps used by this map (canonical URLs).
        List of `str` items. """
        
        self.jurisdiction = None
        """ Intended jurisdiction for structure map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this structure map (Computer friendly).
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Why this structure map is defined.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.structure = None
        """ Structure Definition used by this map.
        List of `StructureMapStructure` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Name for this structure map (Human friendly).
        Type `str`. """
        
        self.url = None
        """ Logical uri to reference this structure map (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the structure map.
        Type `str`. """
        
        super(StructureMap, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", StructureMapGroup, True, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("import_fhir", "import", str, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("structure", "structure", StructureMapStructure, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class StructureMapGroup(backboneelement.BackboneElement):
    """ Named sections for reader convenience.
    """
    
    resource_type = "StructureMapGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ Documentation for this group.
        Type `str`. """
        
        self.extends = None
        """ Another group that this group adds rules to.
        Type `str`. """
        
        self.input = None
        """ Named instance provided when invoking the map.
        List of `StructureMapGroupInput` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Descriptive name for a user.
        Type `str`. """
        
        self.rule = None
        """ Transform Rule from source to target.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        
        super(StructureMapGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroup, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("extends", "extends", str, False, None, False),
            ("input", "input", StructureMapGroupInput, True, None, True),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, True),
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
        
        self.mode = None
        """ source | target.
        Type `str`. """
        
        self.name = None
        """ Name for this instance of data.
        Type `str`. """
        
        self.type = None
        """ Type for this instance of data.
        Type `str`. """
        
        super(StructureMapGroupInput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupInput, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, False),
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
        
        self.documentation = None
        """ Documentation for this instance of data.
        Type `str`. """
        
        self.name = None
        """ Name of the rule for internal references.
        Type `str`. """
        
        self.rule = None
        """ Rules contained in this rule.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Source inputs to the mapping.
        List of `StructureMapGroupRuleSource` items (represented as `dict` in JSON). """
        
        self.target = None
        """ Content to create because of this mapping rule.
        List of `StructureMapGroupRuleTarget` items (represented as `dict` in JSON). """
        
        super(StructureMapGroupRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRule, self).elementProperties()
        js.extend([
            ("dependent", "dependent", StructureMapGroupRuleDependent, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, False),
            ("source", "source", StructureMapGroupRuleSource, True, None, True),
            ("target", "target", StructureMapGroupRuleTarget, True, None, False),
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
        
        self.variable = None
        """ Names of variables to pass to the rule or group.
        List of `str` items. """
        
        super(StructureMapGroupRuleDependent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleDependent, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("variable", "variable", str, True, None, True),
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
        """ FluentPath expression  - must be true or the mapping engine throws
        an error instead of completing.
        Type `str`. """
        
        self.condition = None
        """ FluentPath expression  - must be true or the rule does not apply.
        Type `str`. """
        
        self.context = None
        """ Type or variable this rule applies to.
        Type `str`. """
        
        self.contextType = None
        """ type | variable.
        Type `str`. """
        
        self.element = None
        """ Optional field for this source.
        Type `str`. """
        
        self.listMode = None
        """ first | share | last.
        Type `str`. """
        
        self.max = None
        """ Specified maximum cardinality (number or *).
        Type `str`. """
        
        self.min = None
        """ Specified minimum cardinality.
        Type `int`. """
        
        self.required = None
        """ Whether this rule applies if the source isn't found.
        Type `bool`. """
        
        self.type = None
        """ Type for this source.
        Type `str`. """
        
        self.variable = None
        """ Named context for field, if a field is specified.
        Type `str`. """
        
        super(StructureMapGroupRuleSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleSource, self).elementProperties()
        js.extend([
            ("check", "check", str, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", str, False, None, True),
            ("contextType", "contextType", str, False, None, True),
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("required", "required", bool, False, None, True),
            ("type", "type", str, False, None, False),
            ("variable", "variable", str, False, None, False),
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
        
        self.contextType = None
        """ type | variable.
        Type `str`. """
        
        self.element = None
        """ Field to create in the context.
        Type `str`. """
        
        self.listMode = None
        """ first | share | last.
        List of `str` items. """
        
        self.listRuleId = None
        """ Internal rule reference for shared list items.
        Type `str`. """
        
        self.parameter = None
        """ Parameters to the transform.
        List of `StructureMapGroupRuleTargetParameter` items (represented as `dict` in JSON). """
        
        self.transform = None
        """ create | copy +.
        Type `str`. """
        
        self.variable = None
        """ Named context for field, if desired, and a field is specified.
        Type `str`. """
        
        super(StructureMapGroupRuleTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleTarget, self).elementProperties()
        js.extend([
            ("context", "context", str, False, None, False),
            ("contextType", "contextType", str, False, None, False),
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, True, None, False),
            ("listRuleId", "listRuleId", str, False, None, False),
            ("parameter", "parameter", StructureMapGroupRuleTargetParameter, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("variable", "variable", str, False, None, False),
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
        
        self.valueDecimal = None
        """ Parameter value - variable or literal.
        Type `float`. """
        
        self.valueId = None
        """ Parameter value - variable or literal.
        Type `str`. """
        
        self.valueInteger = None
        """ Parameter value - variable or literal.
        Type `int`. """
        
        self.valueString = None
        """ Parameter value - variable or literal.
        Type `str`. """
        
        super(StructureMapGroupRuleTargetParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleTargetParameter, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
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
        
        self.documentation = None
        """ Documentation on use of structure.
        Type `str`. """
        
        self.mode = None
        """ source | queried | target | produced.
        Type `str`. """
        
        self.url = None
        """ Canonical URL for structure definition.
        Type `str`. """
        
        super(StructureMapStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapStructure, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import identifier
from . import usagecontext
