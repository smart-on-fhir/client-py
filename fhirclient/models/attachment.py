#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Attachment) on 2015-04-08.
#  2015, SMART Health IT.


import fhirdate
import fhirelement


class Attachment(fhirelement.FHIRElement):
    """ Content in a format defined elsewhere.
    
    For referring to data content defined in other formats.
    """
    
    resource_name = "Attachment"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contentType = None
        """ Mime type of the content, with charset etc..
        Type `str`. """
        
        self.creation = None
        """ Date attachment was first created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.data = None
        """ Data inline, base64ed.
        Type `str`. """
        
        self.hash = None
        """ Hash of the data (sha-1, base64ed ).
        Type `str`. """
        
        self.language = None
        """ Human language of the content (BCP-47).
        Type `str`. """
        
        self.size = None
        """ Number of bytes of content (if url provided).
        Type `int`. """
        
        self.title = None
        """ Label to display in place of the data.
        Type `str`. """
        
        self.url = None
        """ Uri where the data can be found.
        Type `str`. """
        
        super(Attachment, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Attachment, self).update_with_json(jsondict)
        if 'contentType' in jsondict:
            self.contentType = jsondict['contentType']
        if 'creation' in jsondict:
            self.creation = fhirdate.FHIRDate.with_json_and_owner(jsondict['creation'], self)
        if 'data' in jsondict:
            self.data = jsondict['data']
        if 'hash' in jsondict:
            self.hash = jsondict['hash']
        if 'language' in jsondict:
            self.language = jsondict['language']
        if 'size' in jsondict:
            self.size = jsondict['size']
        if 'title' in jsondict:
            self.title = jsondict['title']
        if 'url' in jsondict:
            self.url = jsondict['url']

