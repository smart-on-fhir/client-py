#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 (http://hl7.org/fhir/StructureDefinition/ProcessResponse) on 2016-08-31.
#  2016, SMART Health IT.


from . import domainresource

class ProcessResponse(domainresource.DomainResource):
    """ ProcessResponse resource.
    
    This resource provides processing status, errors and notes from the
    processing of a resource.
    """
    
    resource_name = "ProcessResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.error = None
        """ Error code.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.form = None
        """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Notes.
        List of `ProcessResponseNotes` items (represented as `dict` in JSON). """
        
        self.organizationIdentifier = None
        """ Authoring Organization.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organizationReference = None
        """ Authoring Organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ Processing outcome.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.requestIdentifier = None
        """ Request reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestOrganizationIdentifier = None
        """ Responsible organization.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestOrganizationReference = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProviderIdentifier = None
        """ Responsible Practitioner.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestProviderReference = None
        """ Responsible Practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.requestReference = None
        """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(ProcessResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcessResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", coding.Coding, True, None, False),
            ("form", "form", coding.Coding, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("notes", "notes", ProcessResponseNotes, True, None, False),
            ("organizationIdentifier", "organizationIdentifier", identifier.Identifier, False, "organization", False),
            ("organizationReference", "organizationReference", fhirreference.FHIRReference, False, "organization", False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("outcome", "outcome", coding.Coding, False, None, False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, "request", False),
            ("requestOrganizationIdentifier", "requestOrganizationIdentifier", identifier.Identifier, False, "requestOrganization", False),
            ("requestOrganizationReference", "requestOrganizationReference", fhirreference.FHIRReference, False, "requestOrganization", False),
            ("requestProviderIdentifier", "requestProviderIdentifier", identifier.Identifier, False, "requestProvider", False),
            ("requestProviderReference", "requestProviderReference", fhirreference.FHIRReference, False, "requestProvider", False),
            ("requestReference", "requestReference", fhirreference.FHIRReference, False, "request", False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class ProcessResponseNotes(backboneelement.BackboneElement):
    """ Notes.
    
    Suite of processing note or additional requirements is the processing has
    been held.
    """
    
    resource_name = "ProcessResponseNotes"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        """ Notes text.
        Type `str`. """
        
        self.type = None
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ProcessResponseNotes, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcessResponseNotes, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
