#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (valueset.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import coding
import contactpoint
import fhirdate
import fhirelement
import fhirresource
import identifier


class ValueSet(fhirresource.FHIRResource):
    """ A set of codes drawn from one or more code systems.
    
    A value set specifies a set of codes drawn from one or more code systems.
    """
    
    resource_name = "ValueSet"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.compose = None
        """ When value set includes codes from elsewhere.
        Type `ValueSetCompose` (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Publishing restrictions for the value set.
        Type `str`. """
        
        self.date = None
        """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.define = None
        """ When value set defines its own codes.
        Type `ValueSetDefine` (represented as `dict` in JSON). """
        
        self.description = None
        """ Human language description of the value set.
        Type `str`. """
        
        self.expansion = None
        """ Used when the value set is "expanded".
        Type `ValueSetExpansion` (represented as `dict` in JSON). """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.extensible = False
        """ Whether this is intended to be used with an extensible binding.
        Type `bool`. """
        
        self.identifier = None
        """ Globally unique logical id for  value set.
        Type `str`. """
        
        self.immutable = False
        """ Indicates whether or not any change to the content logical
        definition may occur.
        Type `bool`. """
        
        self.name = None
        """ Informal name for this value set.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Textual description of the intended scope and use.
        Type `str`. """
        
        self.stableDate = None
        """ Fixed date for the version of all referenced code systems and value
        sets.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the value set.
        Type `str`. """
        
        super(ValueSet, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSet, self).update_with_json(jsondict)
        if 'compose' in jsondict:
            self.compose = ValueSetCompose.with_json_and_owner(jsondict['compose'], self)
        if 'copyright' in jsondict:
            self.copyright = jsondict['copyright']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'define' in jsondict:
            self.define = ValueSetDefine.with_json_and_owner(jsondict['define'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'expansion' in jsondict:
            self.expansion = ValueSetExpansion.with_json_and_owner(jsondict['expansion'], self)
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'extensible' in jsondict:
            self.extensible = jsondict['extensible']
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'immutable' in jsondict:
            self.immutable = jsondict['immutable']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'purpose' in jsondict:
            self.purpose = jsondict['purpose']
        if 'stableDate' in jsondict:
            self.stableDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['stableDate'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'version' in jsondict:
            self.version = jsondict['version']


class ValueSetCompose(fhirelement.FHIRElement):
    """ When value set includes codes from elsewhere.
    """
    
    resource_name = "ValueSetCompose"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.importFrom = None
        """ Import the contents of another value set.
        List of `str` items. """
        
        self.include = None
        """ Include one or more codes from a code system.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        super(ValueSetCompose, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetCompose, self).update_with_json(jsondict)
        if 'importFrom' in jsondict:
            self.importFrom = jsondict['importFrom']
        if 'include' in jsondict:
            self.include = ValueSetComposeInclude.with_json_and_owner(jsondict['include'], self)


class ValueSetComposeInclude(fhirelement.FHIRElement):
    """ Include one or more codes from a code system.
    """
    
    resource_name = "ValueSetComposeInclude"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.concept = None
        """ A concept defined in the system.
        List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON). """
        
        self.filter = None
        """ Select codes/concepts by their properties (including relationships).
        List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON). """
        
        self.system = None
        """ The system the codes come from.
        Type `str`. """
        
        self.version = None
        """ Specific version of the code system referred to.
        Type `str`. """
        
        super(ValueSetComposeInclude, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetComposeInclude, self).update_with_json(jsondict)
        if 'concept' in jsondict:
            self.concept = ValueSetComposeIncludeConcept.with_json_and_owner(jsondict['concept'], self)
        if 'filter' in jsondict:
            self.filter = ValueSetComposeIncludeFilter.with_json_and_owner(jsondict['filter'], self)
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'version' in jsondict:
            self.version = jsondict['version']


class ValueSetComposeIncludeConcept(fhirelement.FHIRElement):
    """ A concept defined in the system.
    
    Specifies a concept to be included or excluded.
    """
    
    resource_name = "ValueSetComposeIncludeConcept"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code or expression from system.
        Type `str`. """
        
        self.designation = None
        """ Additional representations for the concept.
        List of `ValueSetDefineConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        """ Test to display for this code for this value set.
        Type `str`. """
        
        super(ValueSetComposeIncludeConcept, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetComposeIncludeConcept, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'designation' in jsondict:
            self.designation = ValueSetDefineConceptDesignation.with_json_and_owner(jsondict['designation'], self)
        if 'display' in jsondict:
            self.display = jsondict['display']


class ValueSetComposeIncludeFilter(fhirelement.FHIRElement):
    """ Select codes/concepts by their properties (including relationships).
    
    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """
    
    resource_name = "ValueSetComposeIncludeFilter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.op = None
        """ = | is-a | is-not-a | regex | in | not in.
        Type `str`. """
        
        self.property = None
        """ A property defined by the code system.
        Type `str`. """
        
        self.value = None
        """ Code from the system, or regex criteria.
        Type `str`. """
        
        super(ValueSetComposeIncludeFilter, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetComposeIncludeFilter, self).update_with_json(jsondict)
        if 'op' in jsondict:
            self.op = jsondict['op']
        if 'property' in jsondict:
            self.property = jsondict['property']
        if 'value' in jsondict:
            self.value = jsondict['value']


class ValueSetDefine(fhirelement.FHIRElement):
    """ When value set defines its own codes.
    """
    
    resource_name = "ValueSetDefine"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.caseSensitive = False
        """ If code comparison is case sensitive.
        Type `bool`. """
        
        self.concept = None
        """ Concepts in the code system.
        List of `ValueSetDefineConcept` items (represented as `dict` in JSON). """
        
        self.system = None
        """ URI to identify the code system.
        Type `str`. """
        
        self.version = None
        """ Version of this system.
        Type `str`. """
        
        super(ValueSetDefine, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetDefine, self).update_with_json(jsondict)
        if 'caseSensitive' in jsondict:
            self.caseSensitive = jsondict['caseSensitive']
        if 'concept' in jsondict:
            self.concept = ValueSetDefineConcept.with_json_and_owner(jsondict['concept'], self)
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'version' in jsondict:
            self.version = jsondict['version']


class ValueSetDefineConcept(fhirelement.FHIRElement):
    """ Concepts in the code system.
    """
    
    resource_name = "ValueSetDefineConcept"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.abstract = False
        """ If this code is not for use as a real concept.
        Type `bool`. """
        
        self.code = None
        """ Code that identifies concept.
        Type `str`. """
        
        self.concept = None
        """ Concepts in the code system.
        List of `ValueSetDefineConcept` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ Formal Definition.
        Type `str`. """
        
        self.designation = None
        """ Additional representations for the concept.
        List of `ValueSetDefineConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        """ Text to Display to the user.
        Type `str`. """
        
        super(ValueSetDefineConcept, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetDefineConcept, self).update_with_json(jsondict)
        if 'abstract' in jsondict:
            self.abstract = jsondict['abstract']
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'concept' in jsondict:
            self.concept = ValueSetDefineConcept.with_json_and_owner(jsondict['concept'], self)
        if 'definition' in jsondict:
            self.definition = jsondict['definition']
        if 'designation' in jsondict:
            self.designation = ValueSetDefineConceptDesignation.with_json_and_owner(jsondict['designation'], self)
        if 'display' in jsondict:
            self.display = jsondict['display']


class ValueSetDefineConceptDesignation(fhirelement.FHIRElement):
    """ Additional representations for the concept.
    
    Additional representations for the concept - other languages, aliases,
    specialised purposes, used for particular purposes, etc.
    """
    
    resource_name = "ValueSetDefineConceptDesignation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.use = None
        """ Details how this designation would be used.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ The text value for this designation.
        Type `str`. """
        
        super(ValueSetDefineConceptDesignation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetDefineConceptDesignation, self).update_with_json(jsondict)
        if 'use' in jsondict:
            self.use = coding.Coding.with_json_and_owner(jsondict['use'], self)
        if 'value' in jsondict:
            self.value = jsondict['value']


class ValueSetExpansion(fhirelement.FHIRElement):
    """ Used when the value set is "expanded".
    
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """
    
    resource_name = "ValueSetExpansion"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contains = None
        """ Codes in the value set.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Uniquely identifies this expansion.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.timestamp = None
        """ Time valueset expansion happened.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ValueSetExpansion, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetExpansion, self).update_with_json(jsondict)
        if 'contains' in jsondict:
            self.contains = ValueSetExpansionContains.with_json_and_owner(jsondict['contains'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'timestamp' in jsondict:
            self.timestamp = fhirdate.FHIRDate.with_json_and_owner(jsondict['timestamp'], self)


class ValueSetExpansionContains(fhirelement.FHIRElement):
    """ Codes in the value set.
    
    The codes that are contained in the value set expansion.
    """
    
    resource_name = "ValueSetExpansionContains"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.abstract = False
        """ If user cannot select this entry.
        Type `bool`. """
        
        self.code = None
        """ Code - if blank, this is not a choosable code.
        Type `str`. """
        
        self.contains = None
        """ Codes in the value set.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.display = None
        """ User display for the concept.
        Type `str`. """
        
        self.system = None
        """ System value for the code.
        Type `str`. """
        
        self.version = None
        """ Version in which this code / display is defined.
        Type `str`. """
        
        super(ValueSetExpansionContains, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetExpansionContains, self).update_with_json(jsondict)
        if 'abstract' in jsondict:
            self.abstract = jsondict['abstract']
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'contains' in jsondict:
            self.contains = ValueSetExpansionContains.with_json_and_owner(jsondict['contains'], self)
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'version' in jsondict:
            self.version = jsondict['version']

