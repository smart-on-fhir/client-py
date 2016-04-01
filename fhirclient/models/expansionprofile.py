#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/ExpansionProfile) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class ExpansionProfile(domainresource.DomainResource):
    """ Defines behaviour and contraints on the ValueSet Expansion operation.
    
    Resource to define constraints on the Expansion of a FHIR ValueSet.
    """
    
    resource_name = "ExpansionProfile"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None
        """ When the expansion profile imposes code system contraints.
        Type `ExpansionProfileCodeSystem` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ExpansionProfileContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Human language description of the expansion profile.
        Type `str`. """
        
        self.designation = None
        """ When the expansion profile imposes designation contraints.
        Type `ExpansionProfileDesignation` (represented as `dict` in JSON). """
        
        self.displayLanguage = None
        """ Specify the language for the display element of codes in the value
        set expansion.
        Type `str`. """
        
        self.excludeNested = None
        """ Include or exclude nested codes in the value set expansion.
        Type `bool`. """
        
        self.excludeNotForUI = None
        """ Include or exclude codes which cannot be rendered in user
        interfaces in the value set expansion.
        Type `bool`. """
        
        self.excludePostCoordinated = None
        """ Include or exclude codes which are post coordinated expressions in
        the value set expansion.
        Type `bool`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Additional identifier for the expansion profile (e.g. an Object
        Identifier).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.includeDefinition = None
        """ Include or exclude the value set definition in the expansion.
        Type `bool`. """
        
        self.includeDesignations = None
        """ Whether the expansion should include concept designations.
        Type `bool`. """
        
        self.includeInactive = None
        """ Include or exclude inactive concepts in the expansion.
        Type `bool`. """
        
        self.limitedExpansion = None
        """ Controls behaviour of the value set expand operation when value
        sets are too large to be completely expanded.
        Type `bool`. """
        
        self.name = None
        """ Informal name for this expansion profile.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.url = None
        """ Globally unique logical identifier for  expansion profile.
        Type `str`. """
        
        self.version = None
        """ Logical identifier for this version of the expansion profile.
        Type `str`. """
        
        super(ExpansionProfile, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfile, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", ExpansionProfileCodeSystem, False, None, False),
            ("contact", "contact", ExpansionProfileContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("designation", "designation", ExpansionProfileDesignation, False, None, False),
            ("displayLanguage", "displayLanguage", str, False, None, False),
            ("excludeNested", "excludeNested", bool, False, None, False),
            ("excludeNotForUI", "excludeNotForUI", bool, False, None, False),
            ("excludePostCoordinated", "excludePostCoordinated", bool, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("includeDefinition", "includeDefinition", bool, False, None, False),
            ("includeDesignations", "includeDesignations", bool, False, None, False),
            ("includeInactive", "includeInactive", bool, False, None, False),
            ("limitedExpansion", "limitedExpansion", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ExpansionProfileCodeSystem(backboneelement.BackboneElement):
    """ When the expansion profile imposes code system contraints.
    
    A set of criteria that provide the constraints imposed on the value set
    expansion by including or excluding codes from specific code systems (or
    versions).
    """
    
    resource_name = "ExpansionProfileCodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exclude = None
        """ Code systems to be excluded.
        Type `ExpansionProfileCodeSystemExclude` (represented as `dict` in JSON). """
        
        self.include = None
        """ Code systems to be included.
        Type `ExpansionProfileCodeSystemInclude` (represented as `dict` in JSON). """
        
        super(ExpansionProfileCodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileCodeSystem, self).elementProperties()
        js.extend([
            ("exclude", "exclude", ExpansionProfileCodeSystemExclude, False, None, False),
            ("include", "include", ExpansionProfileCodeSystemInclude, False, None, False),
        ])
        return js


class ExpansionProfileCodeSystemExclude(backboneelement.BackboneElement):
    """ Code systems to be excluded.
    
    Code systems to be excluded from value set expansions.
    """
    
    resource_name = "ExpansionProfileCodeSystemExclude"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None
        """ The code systems to be excluded.
        List of `ExpansionProfileCodeSystemExcludeCodeSystem` items (represented as `dict` in JSON). """
        
        super(ExpansionProfileCodeSystemExclude, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileCodeSystemExclude, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", ExpansionProfileCodeSystemExcludeCodeSystem, True, None, True),
        ])
        return js


class ExpansionProfileCodeSystemExcludeCodeSystem(backboneelement.BackboneElement):
    """ The code systems to be excluded.
    
    A data group for each code system to be excluded.
    """
    
    resource_name = "ExpansionProfileCodeSystemExcludeCodeSystem"
    
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
        
        super(ExpansionProfileCodeSystemExcludeCodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileCodeSystemExcludeCodeSystem, self).elementProperties()
        js.extend([
            ("system", "system", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class ExpansionProfileCodeSystemInclude(backboneelement.BackboneElement):
    """ Code systems to be included.
    
    Code systems to be included in value set expansions.
    """
    
    resource_name = "ExpansionProfileCodeSystemInclude"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None
        """ The code systems to be included.
        List of `ExpansionProfileCodeSystemIncludeCodeSystem` items (represented as `dict` in JSON). """
        
        super(ExpansionProfileCodeSystemInclude, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileCodeSystemInclude, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", ExpansionProfileCodeSystemIncludeCodeSystem, True, None, True),
        ])
        return js


class ExpansionProfileCodeSystemIncludeCodeSystem(backboneelement.BackboneElement):
    """ The code systems to be included.
    
    A data group for each code system to be included.
    """
    
    resource_name = "ExpansionProfileCodeSystemIncludeCodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.system = None
        """ The specific code system to be included.
        Type `str`. """
        
        self.version = None
        """ Specific version of the code system referred to.
        Type `str`. """
        
        super(ExpansionProfileCodeSystemIncludeCodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileCodeSystemIncludeCodeSystem, self).elementProperties()
        js.extend([
            ("system", "system", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class ExpansionProfileContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "ExpansionProfileContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of an individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ExpansionProfileContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ExpansionProfileDesignation(backboneelement.BackboneElement):
    """ When the expansion profile imposes designation contraints.
    
    A set of criteria that provide the constraints imposed on the value set
    expansion by including or excluding designations.
    """
    
    resource_name = "ExpansionProfileDesignation"
    
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
    
    resource_name = "ExpansionProfileDesignationExclude"
    
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
    
    resource_name = "ExpansionProfileDesignationExcludeDesignation"
    
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
        """ Designation use.
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
    
    resource_name = "ExpansionProfileDesignationInclude"
    
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
    
    resource_name = "ExpansionProfileDesignationIncludeDesignation"
    
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
        """ Designation use.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExpansionProfileDesignationIncludeDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExpansionProfileDesignationIncludeDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
        ])
        return js


from . import coding
from . import contactpoint
from . import fhirdate
from . import identifier
