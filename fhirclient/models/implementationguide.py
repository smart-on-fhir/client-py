#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference


class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.
    
    A set of rules or how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole, and to publish a computable definition of all the parts.
    """
    
    resource_name = "ImplementationGuide"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.binary = None
        """ Image, css, script, etc..
        List of `str` items. """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ImplementationGuideContact` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date for this version of the Implementation Guide.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dependency = None
        """ Another Implementation guide this depends on.
        List of `ImplementationGuideDependency` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the Implementation Guide.
        Type `str`. """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None
        """ FHIR Version this Implementation Guide targets.
        Type `str`. """
        
        self.global_fhir = None
        """ Profiles that apply globally.
        List of `ImplementationGuideGlobal` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Informal name for this Implementation Guide.
        Type `str`. """
        
        self.package = None
        """ Group of resources as used in .page.package.
        List of `ImplementationGuidePackage` items (represented as `dict` in JSON). """
        
        self.page = None
        """ Page/Section in the Guide.
        Type `ImplementationGuidePage` (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.url = None
        """ Absolute URL used to reference this Implementation Guide.
        Type `str`. """
        
        self.useContext = None
        """ The implementation guide is intended to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the Implementation Guide.
        Type `str`. """
        
        super(ImplementationGuide, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImplementationGuide, self).elementProperties()
        js.extend([
            ("binary", "binary", str, True),
            ("contact", "contact", ImplementationGuideContact, True),
            ("copyright", "copyright", str, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("dependency", "dependency", ImplementationGuideDependency, True),
            ("description", "description", str, False),
            ("experimental", "experimental", bool, False),
            ("fhirVersion", "fhirVersion", str, False),
            ("global_fhir", "global", ImplementationGuideGlobal, True),
            ("name", "name", str, False),
            ("package", "package", ImplementationGuidePackage, True),
            ("page", "page", ImplementationGuidePage, False),
            ("publisher", "publisher", str, False),
            ("status", "status", str, False),
            ("url", "url", str, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True),
            ("version", "version", str, False),
        ])
        return js


class ImplementationGuideContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "ImplementationGuideContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ImplementationGuideContact, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImplementationGuideContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class ImplementationGuideDependency(fhirelement.FHIRElement):
    """ Another Implementation guide this depends on.
    
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    
    resource_name = "ImplementationGuideDependency"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.type = None
        """ reference | inclusion.
        Type `str`. """
        
        self.uri = None
        """ Where to find dependency.
        Type `str`. """
        
        super(ImplementationGuideDependency, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDependency, self).elementProperties()
        js.extend([
            ("type", "type", str, False),
            ("uri", "uri", str, False),
        ])
        return js


class ImplementationGuideGlobal(fhirelement.FHIRElement):
    """ Profiles that apply globally.
    
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    
    resource_name = "ImplementationGuideGlobal"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.profile = None
        """ Profile that all resources must conform to.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type this profiles applies to.
        Type `str`. """
        
        super(ImplementationGuideGlobal, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend([
            ("profile", "profile", fhirreference.FHIRReference, False),
            ("type", "type", str, False),
        ])
        return js


class ImplementationGuidePackage(fhirelement.FHIRElement):
    """ Group of resources as used in .page.package.
    
    A logical group of resources. Logical groups can be used when building
    pages.
    """
    
    resource_name = "ImplementationGuidePackage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Human readable text describing the package.
        Type `str`. """
        
        self.name = None
        """ Name used .page.package.
        Type `str`. """
        
        self.resource = None
        """ Resource in the implementation guide.
        List of `ImplementationGuidePackageResource` items (represented as `dict` in JSON). """
        
        super(ImplementationGuidePackage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePackage, self).elementProperties()
        js.extend([
            ("description", "description", str, False),
            ("name", "name", str, False),
            ("resource", "resource", ImplementationGuidePackageResource, True),
        ])
        return js


class ImplementationGuidePackageResource(fhirelement.FHIRElement):
    """ Resource in the implementation guide.
    
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, conformance statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    resource_name = "ImplementationGuidePackageResource"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.acronym = None
        """ Short code to identify the resource.
        Type `str`. """
        
        self.description = None
        """ Reason why included in guide.
        Type `str`. """
        
        self.exampleFor = None
        """ Resource this is an example of (if applicable).
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.name = None
        """ Human Name for the resource.
        Type `str`. """
        
        self.purpose = None
        """ example | terminology | profile | extension | dictionary | logical.
        Type `str`. """
        
        self.sourceReference = None
        """ Location of the resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.sourceUri = None
        """ Location of the resource.
        Type `str`. """
        
        super(ImplementationGuidePackageResource, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePackageResource, self).elementProperties()
        js.extend([
            ("acronym", "acronym", str, False),
            ("description", "description", str, False),
            ("exampleFor", "exampleFor", fhirreference.FHIRReference, False),
            ("name", "name", str, False),
            ("purpose", "purpose", str, False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False),
            ("sourceUri", "sourceUri", str, False),
        ])
        return js


class ImplementationGuidePage(fhirelement.FHIRElement):
    """ Page/Section in the Guide.
    
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    
    resource_name = "ImplementationGuidePage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.format = None
        """ Format of the page (e.g. html, markdown, etc.).
        Type `str`. """
        
        self.kind = None
        """ page | example | list | include | directory | dictionary | toc |
        resource.
        Type `str`. """
        
        self.name = None
        """ Short name shown for navigational assistance.
        Type `str`. """
        
        self.package = None
        """ Name of package to include.
        List of `str` items. """
        
        self.page = None
        """ Nested Pages / Sections.
        List of `ImplementationGuidePage` items (represented as `dict` in JSON). """
        
        self.source = None
        """ Where to find that page.
        Type `str`. """
        
        self.type = None
        """ Kind of resource to include in the list.
        List of `str` items. """
        
        super(ImplementationGuidePage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePage, self).elementProperties()
        js.extend([
            ("format", "format", str, False),
            ("kind", "kind", str, False),
            ("name", "name", str, False),
            ("package", "package", str, True),
            ("page", "page", ImplementationGuidePage, True),
            ("source", "source", str, False),
            ("type", "type", str, True),
        ])
        return js

