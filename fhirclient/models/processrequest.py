#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ProcessRequest) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class ProcessRequest(domainresource.DomainResource):
    """ Process request.
    
    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """
    
    resource_name = "ProcessRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ cancel | poll | reprocess | status.
        Type `str`. """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exclude = None
        """ Resource type(s) to exclude.
        List of `str` items. """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.include = None
        """ Resource type(s) to include.
        List of `str` items. """
        
        self.item = None
        """ Items to re-adjudicate.
        List of `ProcessRequestItem` items (represented as `dict` in JSON). """
        
        self.nullify = None
        """ Nullify.
        Type `bool`. """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period.
        Type `Period` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Reference number/string.
        Type `str`. """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.target = None
        """ Target of the request.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(ProcessRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcessRequest, self).elementProperties()
        js.extend([
            ("action", "action", str, False, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("exclude", "exclude", str, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("include", "include", str, True, None, False),
            ("item", "item", ProcessRequestItem, True, None, False),
            ("nullify", "nullify", bool, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class ProcessRequestItem(backboneelement.BackboneElement):
    """ Items to re-adjudicate.
    
    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """
    
    resource_name = "ProcessRequestItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """
        
        super(ProcessRequestItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcessRequestItem, self).elementProperties()
        js.extend([
            ("sequenceLinkId", "sequenceLinkId", int, False, None, True),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
