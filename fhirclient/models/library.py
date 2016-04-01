#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/Library) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class Library(domainresource.DomainResource):
    """ Represents a library of quality improvement components.
    
    The Library resource provides a representation container for knowledge
    artifact component definitions. It is effectively an exposure of the header
    information for a CQL/ELM library.
    """
    
    resource_name = "Library"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None
        """ A code system used by the library.
        List of `LibraryCodeSystem` items (represented as `dict` in JSON). """
        
        self.dataRequirement = None
        """ Data requirements of the library.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.document = None
        """ The content of the library.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.library = None
        """ A library referenced by this library.
        List of `LibraryLibrary` items (represented as `dict` in JSON). """
        
        self.model = None
        """ A model used by the library.
        List of `LibraryModel` items (represented as `dict` in JSON). """
        
        self.moduleMetadata = None
        """ The metadata information for the library.
        Type `ModuleMetadata` (represented as `dict` in JSON). """
        
        self.parameter = None
        """ Parameters defined by the library.
        List of `ParameterDefinition` items (represented as `dict` in JSON). """
        
        self.valueSet = None
        """ A value set used by the library.
        List of `LibraryValueSet` items (represented as `dict` in JSON). """
        
        super(Library, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Library, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", LibraryCodeSystem, True, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("document", "document", attachment.Attachment, False, None, True),
            ("library", "library", LibraryLibrary, True, None, False),
            ("model", "model", LibraryModel, True, None, False),
            ("moduleMetadata", "moduleMetadata", modulemetadata.ModuleMetadata, False, None, False),
            ("parameter", "parameter", parameterdefinition.ParameterDefinition, True, None, False),
            ("valueSet", "valueSet", LibraryValueSet, True, None, False),
        ])
        return js


from . import backboneelement

class LibraryCodeSystem(backboneelement.BackboneElement):
    """ A code system used by the library.
    
    A code system definition used within the library.
    """
    
    resource_name = "LibraryCodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ The identifier of the code system.
        Type `str`. """
        
        self.name = None
        """ Name of the code system.
        Type `str`. """
        
        self.version = None
        """ The version of the code system, if any.
        Type `str`. """
        
        super(LibraryCodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LibraryCodeSystem, self).elementProperties()
        js.extend([
            ("identifier", "identifier", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class LibraryLibrary(backboneelement.BackboneElement):
    """ A library referenced by this library.
    
    A library element describes a library referenced by this library.
    """
    
    resource_name = "LibraryLibrary"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentAttachment = None
        """ The content of the library.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.documentReference = None
        """ The content of the library.
        Type `FHIRReference` referencing `ModuleDefinition` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ The identifier of the library.
        Type `str`. """
        
        self.name = None
        """ Name of the library.
        Type `str`. """
        
        self.version = None
        """ The version of the library, if any.
        Type `str`. """
        
        super(LibraryLibrary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LibraryLibrary, self).elementProperties()
        js.extend([
            ("documentAttachment", "documentAttachment", attachment.Attachment, False, "document", False),
            ("documentReference", "documentReference", fhirreference.FHIRReference, False, "document", False),
            ("identifier", "identifier", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class LibraryModel(backboneelement.BackboneElement):
    """ A model used by the library.
    
    A model element describes the model and version used by the library.
    """
    
    resource_name = "LibraryModel"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ The identifier of the model.
        Type `str`. """
        
        self.name = None
        """ Name of the model.
        Type `str`. """
        
        self.version = None
        """ The version of the model, if any.
        Type `str`. """
        
        super(LibraryModel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LibraryModel, self).elementProperties()
        js.extend([
            ("identifier", "identifier", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class LibraryValueSet(backboneelement.BackboneElement):
    """ A value set used by the library.
    
    A value set definition referenced by the library.
    """
    
    resource_name = "LibraryValueSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None
        """ The code system binding for this value set definition.
        List of `str` items. """
        
        self.identifier = None
        """ The identifier of the value set.
        Type `str`. """
        
        self.name = None
        """ Name of the value set.
        Type `str`. """
        
        self.version = None
        """ The version of the value set.
        Type `str`. """
        
        super(LibraryValueSet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LibraryValueSet, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", str, True, None, False),
            ("identifier", "identifier", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import attachment
from . import datarequirement
from . import fhirreference
from . import modulemetadata
from . import parameterdefinition
