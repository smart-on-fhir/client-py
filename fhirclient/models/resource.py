#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Resource) on 2016-06-23.
#  2016, SMART Health IT.


from . import fhirabstractresource

class Resource(fhirabstractresource.FHIRAbstractResource):
    """ Base Resource.
    
    This is the base resource type for everything.
    """
    
    resource_name = "Resource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.id = None
        """ Logical id of this artifact.
        Type `str`. """
        
        self.implicitRules = None
        """ A set of rules under which this content was created.
        Type `str`. """
        
        self.language = None
        """ Language of the resource content.
        Type `str`. """
        
        self.meta = None
        """ Metadata about the resource.
        Type `Meta` (represented as `dict` in JSON). """
        
        super(Resource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Resource, self).elementProperties()
        js.extend([
            ("id", "id", str, False, None, False),
            ("implicitRules", "implicitRules", str, False, None, False),
            ("language", "language", str, False, None, False),
            ("meta", "meta", meta.Meta, False, None, False),
        ])
        return js


from . import meta
