#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Binary) on 2015-04-08.
#  2015, SMART Health IT.


import resource


class Binary(resource.Resource):
    """ Pure binary content defined by sime other format than FHIR.
    
    A binary resource can contain any content, whether text, image, pdf, zip
    archive, etc.
    """
    
    resource_name = "Binary"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.content = None
        """ The actual content.
        Type `str`. """
        
        self.contentType = None
        """ MimeType of the binary content.
        Type `str`. """
        
        super(Binary, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Binary, self).update_with_json(jsondict)
        if 'content' in jsondict:
            self.content = jsondict['content']
        if 'contentType' in jsondict:
            self.contentType = jsondict['contentType']

