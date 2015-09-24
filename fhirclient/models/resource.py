#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Resource) on 2015-09-24.
#  2015, SMART Health IT.


from . import fhirresource
from . import meta


class Resource(fhirresource.FHIRResource):
    """ Base Resource.
    
    This is the base resource type for everything.
    """
    
    resource_name = "Resource"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.implicitRules = None
        """ A set of rules under which this content was created.
        Type `str`. """
        
        self.language = None
        """ Language of the resource content.
        Type `str`. """
        
        self.meta = None
        """ Metadata about the resource.
        Type `Meta` (represented as `dict` in JSON). """
        
        super(Resource, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Resource, self).elementProperties()
        js.extend([
            ("implicitRules", "implicitRules", str, False),
            ("language", "language", str, False),
            ("meta", "meta", meta.Meta, False),
        ])
        return js

