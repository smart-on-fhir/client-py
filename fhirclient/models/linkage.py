#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/Linkage) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class Linkage(domainresource.DomainResource):
    """ Links records for 'same' item.
    
    Identifies two or more records (resource instances) that are referring to
    the same real-world "occurrence".
    """
    
    resource_name = "Linkage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who is responsible for linkages.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.item = None
        """ Item to be linked.
        List of `LinkageItem` items (represented as `dict` in JSON). """
        
        super(Linkage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Linkage, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("item", "item", LinkageItem, True, None, True),
        ])
        return js


from . import backboneelement

class LinkageItem(backboneelement.BackboneElement):
    """ Item to be linked.
    
    Identifies one of the records that is considered to refer to the same real-
    world occurrence as well as how the items hould be evaluated within the
    collection of linked items.
    """
    
    resource_name = "LinkageItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.resource = None
        """ Resource being linked.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ source | alternate | historical.
        Type `str`. """
        
        super(LinkageItem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(LinkageItem, self).elementProperties()
        js.extend([
            ("resource", "resource", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import fhirreference
