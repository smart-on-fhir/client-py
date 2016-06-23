#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.
    
    A set of rules or how FHIR is used to solve a particular problem. This
    resource is used to gather all the parts of an implementation guide into a
    logical whole, and to publish a computable definition of all the parts.
    """
    
    resource_name = "ImplementationGuide"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(ImplementationGuide, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuide, self).elementProperties()
        js.extend([
            ("binary", "binary", str, True, None, False),
            ("contact", "contact", ImplementationGuideContact, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("dependency", "dependency", ImplementationGuideDependency, True, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, False),
            ("global_fhir", "global", ImplementationGuideGlobal, True, None, False),
            ("name", "name", str, False, None, True),
            ("package", "package", ImplementationGuidePackage, True, None, True),
            ("page", "page", ImplementationGuidePage, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ImplementationGuideContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "ImplementationGuideContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ImplementationGuideContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ImplementationGuideDependency(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.
    
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    
    resource_name = "ImplementationGuideDependency"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ reference | inclusion.
        Type `str`. """
        
        self.uri = None
        """ Where to find dependency.
        Type `str`. """
        
        super(ImplementationGuideDependency, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDependency, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("uri", "uri", str, False, None, True),
        ])
        return js


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.
    
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    
    resource_name = "ImplementationGuideGlobal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.profile = None
        """ Profile that all resources must conform to.
        Type `FHIRReference` referencing `StructureDefinition` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type this profiles applies to.
        Type `str`. """
        
        super(ImplementationGuideGlobal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend([
            ("profile", "profile", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class ImplementationGuidePackage(backboneelement.BackboneElement):
    """ Group of resources as used in .page.package.
    
    A logical group of resources. Logical groups can be used when building
    pages.
    """
    
    resource_name = "ImplementationGuidePackage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(ImplementationGuidePackage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePackage, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("resource", "resource", ImplementationGuidePackageResource, True, None, True),
        ])
        return js


class ImplementationGuidePackageResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, conformance statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    resource_name = "ImplementationGuidePackageResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(ImplementationGuidePackageResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePackageResource, self).elementProperties()
        js.extend([
            ("acronym", "acronym", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("exampleFor", "exampleFor", fhirreference.FHIRReference, False, None, False),
            ("name", "name", str, False, None, False),
            ("purpose", "purpose", str, False, None, True),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", True),
            ("sourceUri", "sourceUri", str, False, "source", True),
        ])
        return js


class ImplementationGuidePage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.
    
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    
    resource_name = "ImplementationGuidePage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(ImplementationGuidePage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuidePage, self).elementProperties()
        js.extend([
            ("format", "format", str, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("package", "package", str, True, None, False),
            ("page", "page", ImplementationGuidePage, True, None, False),
            ("source", "source", str, False, None, True),
            ("type", "type", str, True, None, False),
        ])
        return js


from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
