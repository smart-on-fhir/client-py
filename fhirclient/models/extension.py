#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Extension.profile.json) on 2014-11-11.
#  2014, SMART Platforms.


import address
import attachment
import codeableconcept
import coding
import contact
import fhirdate
import fhirelement
import fhirresource
import humanname
import identifier
import period
import quantity
import range
import ratio
import schedule


class Extension(fhirelement.FHIRElement):
    """ Optional Extensions Element - found in all resources..
    """
    
    resource_name = "Extension"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.url = None
        """ identifies the meaning of the extension.
        Type `str`. """
        
        self.valueAddress = None
        """ Value of extension.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Value of extension.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ Value of extension.
        Type `str`. """
        
        self.valueBoolean = False
        """ Value of extension.
        Type `bool`. """
        
        self.valueCode = None
        """ Value of extension.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ Value of extension.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Value of extension.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContact = None
        """ Value of extension.
        Type `Contact` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Value of extension.
        Type `float`. """
        
        self.valueHumanName = None
        """ Value of extension.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ Value of extension.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Value of extension.
        Type `int`. """
        
        self.valuePeriod = None
        """ Value of extension.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value of extension.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value of extension.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Value of extension.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueResource = None
        """ Value of extension.
        Type `FHIRResource` (represented as `dict` in JSON). """
        
        self.valueSchedule = None
        """ Value of extension.
        Type `Schedule` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Value of extension.
        Type `str`. """
        
        self.valueUri = None
        """ Value of extension.
        Type `str`. """
        
        super(Extension, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Extension, self).update_with_json(jsondict)
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'valueAddress' in jsondict:
            self.valueAddress = address.Address.with_json_and_owner(jsondict['valueAddress'], self)
        if 'valueAttachment' in jsondict:
            self.valueAttachment = attachment.Attachment.with_json_and_owner(jsondict['valueAttachment'], self)
        if 'valueBase64Binary' in jsondict:
            self.valueBase64Binary = jsondict['valueBase64Binary']
        if 'valueBoolean' in jsondict:
            self.valueBoolean = jsondict['valueBoolean']
        if 'valueCode' in jsondict:
            self.valueCode = jsondict['valueCode']
        if 'valueCodeableConcept' in jsondict:
            self.valueCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['valueCodeableConcept'], self)
        if 'valueCoding' in jsondict:
            self.valueCoding = coding.Coding.with_json_and_owner(jsondict['valueCoding'], self)
        if 'valueContact' in jsondict:
            self.valueContact = contact.Contact.with_json_and_owner(jsondict['valueContact'], self)
        if 'valueDate' in jsondict:
            self.valueDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueDate'], self)
        if 'valueDateTime' in jsondict:
            self.valueDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueDateTime'], self)
        if 'valueDecimal' in jsondict:
            self.valueDecimal = jsondict['valueDecimal']
        if 'valueHumanName' in jsondict:
            self.valueHumanName = humanname.HumanName.with_json_and_owner(jsondict['valueHumanName'], self)
        if 'valueIdentifier' in jsondict:
            self.valueIdentifier = identifier.Identifier.with_json_and_owner(jsondict['valueIdentifier'], self)
        if 'valueInstant' in jsondict:
            self.valueInstant = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueInstant'], self)
        if 'valueInteger' in jsondict:
            self.valueInteger = jsondict['valueInteger']
        if 'valuePeriod' in jsondict:
            self.valuePeriod = period.Period.with_json_and_owner(jsondict['valuePeriod'], self)
        if 'valueQuantity' in jsondict:
            self.valueQuantity = quantity.Quantity.with_json_and_owner(jsondict['valueQuantity'], self)
        if 'valueRange' in jsondict:
            self.valueRange = range.Range.with_json_and_owner(jsondict['valueRange'], self)
        if 'valueRatio' in jsondict:
            self.valueRatio = ratio.Ratio.with_json_and_owner(jsondict['valueRatio'], self)
        if 'valueResource' in jsondict:
            self.valueResource = fhirresource.FHIRResource.with_json_and_owner(jsondict['valueResource'], self)
        if 'valueSchedule' in jsondict:
            self.valueSchedule = schedule.Schedule.with_json_and_owner(jsondict['valueSchedule'], self)
        if 'valueString' in jsondict:
            self.valueString = jsondict['valueString']
        if 'valueUri' in jsondict:
            self.valueUri = jsondict['valueUri']

