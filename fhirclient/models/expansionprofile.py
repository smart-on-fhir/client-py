#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/ExpansionProfile) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class ExpansionProfile(domainresource.DomainResource):
    """ Defines behaviour and contraints on the ValueSet Expansion operation.
    
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """
    
    resource_type = "ExpansionProfile"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.activeOnly = None
        """ Include or exclude inactive concepts in the expansion.
        Type `bool`. """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the expansion profile.
        Type `str`. """
        
        self.designation = None
        """ When the expansion profile imposes designation contraints.
        Type `ExpansionProfileDesignation` (represented as `dict` in JSON). """
        
        self.displayLanguage = None
        """ Specify the language for the display element of codes in the value
        set expansion.
        Type `str`. """
        
        self.excludeNested = None
        """ Nested codes in the expansion or not.
        Type `bool`. """
        
        self.excludeNotForUI = None
        """ Include or exclude codes which cannot be rendered in user
        interfaces in the value set expansion.
        Type `bool`. """
        
        self.excludePostCoordinated = None
        """ Include or exclude codes which are post coordinated expressions in
        the value set expansion.
        Type `bool`. """
        
        self.excludedSystem = None
        """ Systems/Versions to be exclude.
        Type `ExpansionProfileExcludedSystem` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.fixedVersion = None
        """ Fix use of a code system to a particular version.
        List of `ExpansionProfileFixedVersion` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the expansion profile.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.includeDefinition = None
        """ Include or exclude the value set definition in the expansion.
        Type `bool`. """
        
        self.includeDesignations = None
        """ Whether the expansion should include concept designations.
        Type `bool`. """
        
        self.jurisdiction = None
        """ Intended jurisdiction for expansion profile (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.limitedExpansion = None
        """ Controls behaviour of the value set expand operation when value
        sets are too large to be completely expanded.
        Type `bool`. """
        
        self.name = None
        """ Name for this expansion profile (computer friendly).
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.url = None
        """ Logical URI to reference this expansion profile (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ Context the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the expansion profile.
        Type `str`. """
        
        super(ExpansionProfile, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfile, self).elementProperties()
        js.extend([
            ("activeOnly", "activeOnly", bool, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("designation", "designation", ExpansionProfileDesignation, False, None, False),
            ("displayLanguage", "displayLanguage", str, False, None, False),
            ("excludeNested", "excludeNested", bool, False, None, False),
            ("excludeNotForUI", "excludeNotForUI", bool, False, None, False),
            ("excludePostCoordinated", "excludePostCoordinated", bool, False, None, False),
            ("excludedSystem", "excludedSystem", ExpansionProfileExcludedSystem, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fixedVersion", "fixedVersion", ExpansionProfileFixedVersion, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("includeDefinition", "includeDefinition", bool, False, None, False),
            ("includeDesignations", "includeDesignations", bool, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("limitedExpansion", "limitedExpansion", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ExpansionProfileDesignation(backboneelement.BackboneElement):
    """ When the expansion profile imposes designation contraints.
    
    A set of criteria that provide the constraints imposed on the value set
    expansion by including or excluding designations.
    """
    
    resource_type = "ExpansionProfileDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exclude = None
        """ Designations to be excluded.
        Type `ExpansionProfileDesignationExclude` (represented as `dict` in JSON). """
        
        self.include = None
        """ Designations to be included.
        Type `ExpansionProfileDesignationInclude` (represented as `dict` in JSON). """
        
        super(ExpansionProfileDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileDesignation, self).elementProperties()
        js.extend([
            ("exclude", "exclude", ExpansionProfileDesignationExclude, False, None, False),
            ("include", "include", ExpansionProfileDesignationInclude, False, None, False),
        ])
        return js


class ExpansionProfileDesignationExclude(backboneelement.BackboneElement):
    """ Designations to be excluded.
    """
    
    resource_type = "ExpansionProfileDesignationExclude"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.designation = None
        """ The designation to be excluded.
        List of `ExpansionProfileDesignationExcludeDesignation` items (represented as `dict` in JSON). """
        
        super(ExpansionProfileDesignationExclude, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileDesignationExclude, self).elementProperties()
        js.extend([
            ("designation", "designation", ExpansionProfileDesignationExcludeDesignation, True, None, False),
        ])
        return js


class ExpansionProfileDesignationExcludeDesignation(backboneelement.BackboneElement):
    """ The designation to be excluded.
    
    A data group for each designation to be excluded.
    """
    
    resource_type = "ExpansionProfileDesignationExcludeDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ Human language of the designation to be excluded.
        Type `str`. """
        
        self.use = None
        """ What kind of Designation to exclude.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExpansionProfileDesignationExcludeDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileDesignationExcludeDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
        ])
        return js


class ExpansionProfileDesignationInclude(backboneelement.BackboneElement):
    """ Designations to be included.
    """
    
    resource_type = "ExpansionProfileDesignationInclude"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.designation = None
        """ The designation to be included.
        List of `ExpansionProfileDesignationIncludeDesignation` items (represented as `dict` in JSON). """
        
        super(ExpansionProfileDesignationInclude, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileDesignationInclude, self).elementProperties()
        js.extend([
            ("designation", "designation", ExpansionProfileDesignationIncludeDesignation, True, None, False),
        ])
        return js


class ExpansionProfileDesignationIncludeDesignation(backboneelement.BackboneElement):
    """ The designation to be included.
    
    A data group for each designation to be included.
    """
    
    resource_type = "ExpansionProfileDesignationIncludeDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ Human language of the designation to be included.
        Type `str`. """
        
        self.use = None
        """ What kind of Designation to include.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExpansionProfileDesignationIncludeDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileDesignationIncludeDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
        ])
        return js


class ExpansionProfileExcludedSystem(backboneelement.BackboneElement):
    """ Systems/Versions to be exclude.
    
    Code system, or a particular version of a code system to be excluded from
    value set expansions.
    """
    
    resource_type = "ExpansionProfileExcludedSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.system = None
        """ The specific code system to be excluded.
        Type `str`. """
        
        self.version = None
        """ Specific version of the code system referred to.
        Type `str`. """
        
        super(ExpansionProfileExcludedSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileExcludedSystem, self).elementProperties()
        js.extend([
            ("system", "system", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class ExpansionProfileFixedVersion(backboneelement.BackboneElement):
    """ Fix use of a code system to a particular version.
    
    Fix use of a particular code system to a particular version.
    """
    
    resource_type = "ExpansionProfileFixedVersion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode = None
        """ default | check | override.
        Type `str`. """
        
        self.system = None
        """ System to have its version fixed.
        Type `str`. """
        
        self.version = None
        """ Specific version of the code system referred to.
        Type `str`. """
        
        super(ExpansionProfileFixedVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileFixedVersion, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("system", "system", str, False, None, True),
            ("version", "version", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
