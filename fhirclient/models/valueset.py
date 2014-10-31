#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (valueset.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import contact
import fhirdate
import fhirelement
import fhirresource
import identifier
import narrative


class ValueSet(fhirresource.FHIRResource):
    """ A set of codes drawn from one or more code systems.
    
    Scope and Usage Value sets may be constructed in one of two ways:
    
    * A value set can define its own codes, and/or
    * A value set can be composed of codes defined in other code systems,
    either by listing the codes or by providing a set of selection criteria
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This operation is performed to
    produce a collection of codes that are ready to use for data entry or
    validation. An expanded value set may also contain the original definition
    as well.
    """
    
    resource_name = "ValueSet"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.compose = None
        """ When value set includes codes from elsewhere.
        Type `ValueSetCompose` (represented as `dict` in JSON). """
        
        self.copyright = None
        """ About the value set or its content.
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
        """ When value set is an expansion.
        Type `ValueSetExpansion` (represented as `dict` in JSON). """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.extensible = False
        """ Whether this is intended to be used with an extensible binding.
        Type `bool`. """
        
        self.identifier = None
        """ Logical id to reference this value set.
        Type `str`. """
        
        self.name = None
        """ Informal name for this value set.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `Contact` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the value set.
        Type `str`. """
        
        super(ValueSet, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSet, self).update_with_json(jsondict)
        if 'compose' in jsondict:
            self.compose = ValueSetCompose.with_json(jsondict['compose'])
        if 'copyright' in jsondict:
            self.copyright = jsondict['copyright']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'define' in jsondict:
            self.define = ValueSetDefine.with_json(jsondict['define'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'expansion' in jsondict:
            self.expansion = ValueSetExpansion.with_json(jsondict['expansion'])
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'extensible' in jsondict:
            self.extensible = jsondict['extensible']
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'telecom' in jsondict:
            self.telecom = contact.Contact.with_json(jsondict['telecom'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'version' in jsondict:
            self.version = jsondict['version']


class ValueSetDefine(fhirelement.FHIRElement):
    """ When value set defines its own codes.
    """
    
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
            self.concept = ValueSetDefineConcept.with_json(jsondict['concept'])
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'version' in jsondict:
            self.version = jsondict['version']


class ValueSetDefineConcept(fhirelement.FHIRElement):
    """ Concepts in the code system.
    """
    
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
        """ Child Concepts (is-a / contains).
        List of `ValueSetDefineConceptConcept` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ Formal Definition.
        Type `str`. """
        
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
            self.concept = ValueSetDefineConceptConcept.with_json(jsondict['concept'])
        if 'definition' in jsondict:
            self.definition = jsondict['definition']
        if 'display' in jsondict:
            self.display = jsondict['display']


class ValueSetDefineConceptConcept(fhirelement.FHIRElement):
    """ Child Concepts (is-a / contains).
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(ValueSetDefineConceptConcept, self).__init__(jsondict)


class ValueSetCompose(fhirelement.FHIRElement):
    """ When value set includes codes from elsewhere.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.exclude = None
        """ Explicitly exclude codes.
        List of `ValueSetComposeExclude` items (represented as `dict` in JSON). """
        
        self.importFrom = None
        """ Import the contents of another value set.
        List of `str` items. """
        
        self.include = None
        """ Include one or more codes from a code system.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        super(ValueSetCompose, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetCompose, self).update_with_json(jsondict)
        if 'exclude' in jsondict:
            self.exclude = ValueSetComposeExclude.with_json(jsondict['exclude'])
        if 'importFrom' in jsondict:
            self.importFrom = jsondict['importFrom']
        if 'include' in jsondict:
            self.include = ValueSetComposeInclude.with_json(jsondict['include'])


class ValueSetComposeInclude(fhirelement.FHIRElement):
    """ Include one or more codes from a code system.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code or concept from system.
        List of `str` items. """
        
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
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'filter' in jsondict:
            self.filter = ValueSetComposeIncludeFilter.with_json(jsondict['filter'])
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'version' in jsondict:
            self.version = jsondict['version']


class ValueSetComposeIncludeFilter(fhirelement.FHIRElement):
    """ Select codes/concepts by their properties (including relationships).
    
    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """
    
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


class ValueSetComposeExclude(fhirelement.FHIRElement):
    """ Explicitly exclude codes.
    
    Exclude one or more codes from the value set.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(ValueSetComposeExclude, self).__init__(jsondict)


class ValueSetExpansion(fhirelement.FHIRElement):
    """ When value set is an expansion.
    """
    
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
            self.contains = ValueSetExpansionContains.with_json(jsondict['contains'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'timestamp' in jsondict:
            self.timestamp = fhirdate.FHIRDate.with_json(jsondict['timestamp'])


class ValueSetExpansionContains(fhirelement.FHIRElement):
    """ Codes in the value set.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code - if blank, this is not a choosable code.
        Type `str`. """
        
        self.contains = None
        """ Codes contained in this concept.
        List of `ValueSetExpansionContainsContains` items (represented as `dict` in JSON). """
        
        self.display = None
        """ User display for the concept.
        Type `str`. """
        
        self.system = None
        """ System value for the code.
        Type `str`. """
        
        super(ValueSetExpansionContains, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ValueSetExpansionContains, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'contains' in jsondict:
            self.contains = ValueSetExpansionContainsContains.with_json(jsondict['contains'])
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'system' in jsondict:
            self.system = jsondict['system']


class ValueSetExpansionContainsContains(fhirelement.FHIRElement):
    """ Codes contained in this concept.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(ValueSetExpansionContainsContains, self).__init__(jsondict)

