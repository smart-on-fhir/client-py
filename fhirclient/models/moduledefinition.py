#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/ModuleDefinition) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class ModuleDefinition(domainresource.DomainResource):
    """ Defines the data requirements information for a quality artifact.
    
    The ModuleDefinition resource defines the data requirements for a quality
    artifact.
    """
    
    resource_name = "ModuleDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None
        """ None.
        List of `ModuleDefinitionCodeSystem` items (represented as `dict` in JSON). """
        
        self.data = None
        """ Describes a required data item.
        List of `ModuleDefinitionData` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Logical identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.library = None
        """ A library referenced by the module.
        List of `ModuleDefinitionLibrary` items (represented as `dict` in JSON). """
        
        self.model = None
        """ None.
        List of `ModuleDefinitionModel` items (represented as `dict` in JSON). """
        
        self.parameter = None
        """ None.
        List of `ModuleDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.valueSet = None
        """ None.
        List of `ModuleDefinitionValueSet` items (represented as `dict` in JSON). """
        
        self.version = None
        """ The version of the module, if any.
        Type `str`. """
        
        super(ModuleDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleDefinition, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", ModuleDefinitionCodeSystem, True, None, False),
            ("data", "data", ModuleDefinitionData, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("library", "library", ModuleDefinitionLibrary, True, None, False),
            ("model", "model", ModuleDefinitionModel, True, None, False),
            ("parameter", "parameter", ModuleDefinitionParameter, True, None, False),
            ("valueSet", "valueSet", ModuleDefinitionValueSet, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ModuleDefinitionCodeSystem(backboneelement.BackboneElement):
    """ None.
    
    A code system definition used within the knowledge module.
    """
    
    resource_name = "ModuleDefinitionCodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ None.
        Type `str`. """
        
        self.name = None
        """ None.
        Type `str`. """
        
        self.version = None
        """ None.
        Type `str`. """
        
        super(ModuleDefinitionCodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleDefinitionCodeSystem, self).elementProperties()
        js.extend([
            ("identifier", "identifier", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class ModuleDefinitionData(backboneelement.BackboneElement):
    """ Describes a required data item.
    
    Describes a required data item for evaluation in terms of the type of data,
    and optional code- or date-based filters of the data.
    """
    
    resource_name = "ModuleDefinitionData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeFilter = None
        """ None.
        List of `ModuleDefinitionDataCodeFilter` items (represented as `dict` in JSON). """
        
        self.dateFilter = None
        """ None.
        List of `ModuleDefinitionDataDateFilter` items (represented as `dict` in JSON). """
        
        self.mustSupport = None
        """ Indicates that specific structure elements are referenced by the
        knowledge module.
        List of `str` items. """
        
        self.profile = None
        """ The profile of the required data.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of the required data.
        Type `str`. """
        
        super(ModuleDefinitionData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleDefinitionData, self).elementProperties()
        js.extend([
            ("codeFilter", "codeFilter", ModuleDefinitionDataCodeFilter, True, None, False),
            ("dateFilter", "dateFilter", ModuleDefinitionDataDateFilter, True, None, False),
            ("mustSupport", "mustSupport", str, True, None, False),
            ("profile", "profile", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class ModuleDefinitionDataCodeFilter(backboneelement.BackboneElement):
    """ None.
    
    Code filters for the required data, if any.
    """
    
    resource_name = "ModuleDefinitionDataCodeFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeableConcept = None
        """ The codeableConcepts for the filter.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.path = None
        """ The code-valued attribute of the filter.
        Type `str`. """
        
        self.valueSetReference = None
        """ The valueset for the code filter.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.valueSetString = None
        """ The valueset for the code filter.
        Type `str`. """
        
        super(ModuleDefinitionDataCodeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleDefinitionDataCodeFilter, self).elementProperties()
        js.extend([
            ("codeableConcept", "codeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("path", "path", str, False, None, True),
            ("valueSetReference", "valueSetReference", fhirreference.FHIRReference, False, "valueSet", False),
            ("valueSetString", "valueSetString", str, False, "valueSet", False),
        ])
        return js


class ModuleDefinitionDataDateFilter(backboneelement.BackboneElement):
    """ None.
    
    Date filters for the required data, if any.
    """
    
    resource_name = "ModuleDefinitionDataDateFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ The date-valued attribute of the filter.
        Type `str`. """
        
        self.valueDateTime = None
        """ The value of the filter, as a Period or dateTime value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valuePeriod = None
        """ The value of the filter, as a Period or dateTime value.
        Type `Period` (represented as `dict` in JSON). """
        
        super(ModuleDefinitionDataDateFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleDefinitionDataDateFilter, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
        ])
        return js


class ModuleDefinitionLibrary(backboneelement.BackboneElement):
    """ A library referenced by the module.
    
    A library referenced by the module. The reference must consist of either an
    id, or a document reference.
    """
    
    resource_name = "ModuleDefinitionLibrary"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentAttachment = None
        """ None.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.documentReference = None
        """ None.
        Type `FHIRReference` referencing `ModuleDefinition` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ None.
        Type `str`. """
        
        self.name = None
        """ The local name for the library.
        Type `str`. """
        
        self.version = None
        """ None.
        Type `str`. """
        
        super(ModuleDefinitionLibrary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleDefinitionLibrary, self).elementProperties()
        js.extend([
            ("documentAttachment", "documentAttachment", attachment.Attachment, False, "document", False),
            ("documentReference", "documentReference", fhirreference.FHIRReference, False, "document", False),
            ("identifier", "identifier", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class ModuleDefinitionModel(backboneelement.BackboneElement):
    """ None.
    
    A model reference used by the content.
    """
    
    resource_name = "ModuleDefinitionModel"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ None.
        Type `str`. """
        
        self.name = None
        """ None.
        Type `str`. """
        
        self.version = None
        """ None.
        Type `str`. """
        
        super(ModuleDefinitionModel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleDefinitionModel, self).elementProperties()
        js.extend([
            ("identifier", "identifier", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class ModuleDefinitionParameter(backboneelement.BackboneElement):
    """ None.
    
    Parameters to the module.
    """
    
    resource_name = "ModuleDefinitionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ None.
        Type `str`. """
        
        self.name = None
        """ None.
        Type `str`. """
        
        self.profile = None
        """ None.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.type = None
        """ None.
        Type `str`. """
        
        self.use = None
        """ None.
        Type `str`. """
        
        super(ModuleDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleDefinitionParameter, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("profile", "profile", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js


class ModuleDefinitionValueSet(backboneelement.BackboneElement):
    """ None.
    
    A value set definition used by the knowledge module.
    """
    
    resource_name = "ModuleDefinitionValueSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None
        """ None.
        List of `str` items. """
        
        self.identifier = None
        """ None.
        Type `str`. """
        
        self.name = None
        """ None.
        Type `str`. """
        
        self.version = None
        """ None.
        Type `str`. """
        
        super(ModuleDefinitionValueSet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleDefinitionValueSet, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", str, True, None, False),
            ("identifier", "identifier", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
