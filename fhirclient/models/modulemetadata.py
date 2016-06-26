#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8595 (http://hl7.org/fhir/StructureDefinition/ModuleMetadata) on 2016-06-26.
#  2016, SMART Health IT.


from . import element

class ModuleMetadata(element.Element):
    """ Defines common metadata used by quality artifacts.
    
    The ModuleMetadata structure defines the common metadata elements used by
    quality improvement artifacts. This information includes descriptive and
    topical metadata to enable repository searches, as well as governance and
    evidentiary support information.
    """
    
    resource_name = "ModuleMetadata"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.contributor = None
        """ A content contributor.
        List of `Contributor` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.coverage = None
        """ Describes the context of use for this module.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the module.
        Type `str`. """
        
        self.effectivePeriod = None
        """ The effective date range for the module.
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Logical identifier(s) for the module.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ Last review date for the module.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ A machine-friendly name for the module.
        Type `str`. """
        
        self.publicationDate = None
        """ Publication date for this version of the module.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Describes the purpose of the module.
        Type `str`. """
        
        self.relatedResource = None
        """ Related resources for the module.
        List of `RelatedResource` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | inactive.
        Type `str`. """
        
        self.title = None
        """ A user-friendly title for the module.
        Type `str`. """
        
        self.topic = None
        """ Descriptional topics for the module.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ module | library | decision-support-rule | documentation-template |
        order-set.
        Type `str`. """
        
        self.url = None
        """ Logical URL to reference this module.
        Type `str`. """
        
        self.usage = None
        """ Describes the clinical usage of the module.
        Type `str`. """
        
        self.version = None
        """ The version of the module, if any.
        Type `str`. """
        
        super(ModuleMetadata, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleMetadata, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("contributor", "contributor", contributor.Contributor, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("coverage", "coverage", usagecontext.UsageContext, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedResource", "relatedResource", relatedresource.RelatedResource, True, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import contributor
from . import fhirdate
from . import identifier
from . import period
from . import relatedresource
from . import usagecontext
