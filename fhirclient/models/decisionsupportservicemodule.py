#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 (http://hl7.org/fhir/StructureDefinition/DecisionSupportServiceModule) on 2016-08-31.
#  2016, SMART Health IT.


from . import domainresource

class DecisionSupportServiceModule(domainresource.DomainResource):
    """ A description of decision support service functionality.
    
    The DecisionSupportServiceModule describes a unit of decision support
    functionality that is made available as a service, such as immunization
    modules or drug-drug interaction checking.
    """
    
    resource_name = "DecisionSupportServiceModule"
    
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
        
        self.dataRequirement = None
        """ Data requirements for the module.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
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
        
        self.parameter = None
        """ Parameters to the module.
        List of `ParameterDefinition` items (represented as `dict` in JSON). """
        
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
        
        self.trigger = None
        """ "when" the module should be invoked.
        List of `TriggerDefinition` items (represented as `dict` in JSON). """
        
        self.url = None
        """ Logical URL to reference this module.
        Type `str`. """
        
        self.usage = None
        """ Describes the clinical usage of the module.
        Type `str`. """
        
        self.version = None
        """ The version of the module, if any.
        Type `str`. """
        
        super(DecisionSupportServiceModule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DecisionSupportServiceModule, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("contributor", "contributor", contributor.Contributor, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("coverage", "coverage", usagecontext.UsageContext, True, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("parameter", "parameter", parameterdefinition.ParameterDefinition, True, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedResource", "relatedResource", relatedresource.RelatedResource, True, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("trigger", "trigger", triggerdefinition.TriggerDefinition, True, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import contributor
from . import datarequirement
from . import fhirdate
from . import identifier
from . import parameterdefinition
from . import period
from . import relatedresource
from . import triggerdefinition
from . import usagecontext
