#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/StructureDefinition) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import coding
from . import contactpoint
from . import domainresource
from . import elementdefinition
from . import fhirdate
from . import fhirelement
from . import identifier


class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.
    
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions, and constraints on resources and data types.
    """
    
    resource_name = "StructureDefinition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.abstract = None
        """ Whether the structure is abstract.
        Type `bool`. """
        
        self.base = None
        """ Structure that this set of constraints applies to.
        Type `str`. """
        
        self.code = None
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.constrainedType = None
        """ Any datatype or resource, including abstract ones.
        Type `str`. """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `StructureDefinitionContact` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Where the extension can be used in instances.
        List of `str` items. """
        
        self.contextType = None
        """ resource | datatype | mapping | extension.
        Type `str`. """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date for this version of the StructureDefinition.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the StructureDefinition.
        Type `str`. """
        
        self.differential = None
        """ Differential view of the structure.
        Type `StructureDefinitionDifferential` (represented as `dict` in JSON). """
        
        self.display = None
        """ Use this name when displaying the value.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None
        """ FHIR Version this StructureDefinition targets.
        Type `str`. """
        
        self.identifier = None
        """ Other identifiers for the StructureDefinition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.kind = None
        """ datatype | resource | logical.
        Type `str`. """
        
        self.mapping = None
        """ External specification that the content is mapped to.
        List of `StructureDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name for this StructureDefinition.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Scope and Usage this structure definition is for.
        Type `str`. """
        
        self.snapshot = None
        """ Snapshot view of the structure.
        Type `StructureDefinitionSnapshot` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.url = None
        """ Absolute URL used to reference this StructureDefinition.
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the StructureDefinition.
        Type `str`. """
        
        super(StructureDefinition, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(StructureDefinition, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False),
            ("base", "base", str, False),
            ("code", "code", coding.Coding, True),
            ("constrainedType", "constrainedType", str, False),
            ("contact", "contact", StructureDefinitionContact, True),
            ("context", "context", str, True),
            ("contextType", "contextType", str, False),
            ("copyright", "copyright", str, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("differential", "differential", StructureDefinitionDifferential, False),
            ("display", "display", str, False),
            ("experimental", "experimental", bool, False),
            ("fhirVersion", "fhirVersion", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("kind", "kind", str, False),
            ("mapping", "mapping", StructureDefinitionMapping, True),
            ("name", "name", str, False),
            ("publisher", "publisher", str, False),
            ("requirements", "requirements", str, False),
            ("snapshot", "snapshot", StructureDefinitionSnapshot, False),
            ("status", "status", str, False),
            ("url", "url", str, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True),
            ("version", "version", str, False),
        ])
        return js


class StructureDefinitionContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "StructureDefinitionContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionContact, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(StructureDefinitionContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class StructureDefinitionDifferential(fhirelement.FHIRElement):
    """ Differential view of the structure.
    
    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """
    
    resource_name = "StructureDefinitionDifferential"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionDifferential, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(StructureDefinitionDifferential, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True),
        ])
        return js


class StructureDefinitionMapping(fhirelement.FHIRElement):
    """ External specification that the content is mapped to.
    
    An external specification that the content is mapped to.
    """
    
    resource_name = "StructureDefinitionMapping"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comments = None
        """ Versions, Issues, Scope limitations etc..
        Type `str`. """
        
        self.identity = None
        """ Internal id when this mapping is used.
        Type `str`. """
        
        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """
        
        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """
        
        super(StructureDefinitionMapping, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(StructureDefinitionMapping, self).elementProperties()
        js.extend([
            ("comments", "comments", str, False),
            ("identity", "identity", str, False),
            ("name", "name", str, False),
            ("uri", "uri", str, False),
        ])
        return js


class StructureDefinitionSnapshot(fhirelement.FHIRElement):
    """ Snapshot view of the structure.
    
    A snapshot view is expressed in a stand alone form that can be used and
    interpreted without considering the base StructureDefinition.
    """
    
    resource_name = "StructureDefinitionSnapshot"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionSnapshot, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(StructureDefinitionSnapshot, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True),
        ])
        return js

