#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Coding) on 2015-07-06.
#  2015, SMART Health IT.


from . import fhirelement


class Coding(fhirelement.FHIRElement):
    """ A reference to a code defined by a terminology system.
    """
    
    resource_name = "Coding"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Symbol in syntax defined by the system.
        Type `str`. """
        
        self.display = None
        """ Representation defined by the system.
        Type `str`. """
        
        self.primary = None
        """ If this code was chosen directly by the user.
        Type `bool`. """
        
        self.system = None
        """ Identity of the terminology system.
        Type `str`. """
        
        self.version = None
        """ Version of the system - if relevant.
        Type `str`. """
        
        super(Coding, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Coding, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("display", "display", str, False),
            ("primary", "primary", bool, False),
            ("system", "system", str, False),
            ("version", "version", str, False),
        ])
        return js

