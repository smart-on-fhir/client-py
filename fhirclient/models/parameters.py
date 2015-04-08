#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Parameters) on 2015-04-08.
#  2015, SMART Health IT.


import address
import attachment
import codeableconcept
import coding
import contactpoint
import fhirdate
import fhirelement
import fhirreference
import humanname
import identifier
import period
import quantity
import range
import ratio
import resource
import signature
import timing


class Parameters(resource.Resource):
    """ Operation Request or Response.
    
    This special resource type is used to represent
    [operation](operations.html] request and response. It has no other use, and
    there is no RESTful end=point associated with it.
    """
    
    resource_name = "Parameters"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.parameter = None
        """ Operation Parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        super(Parameters, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Parameters, self).update_with_json(jsondict)
        if 'parameter' in jsondict:
            self.parameter = ParametersParameter.with_json_and_owner(jsondict['parameter'], self)


class ParametersParameter(fhirelement.FHIRElement):
    """ Operation Parameter.
    
    A parameter passed to or received from the operation.
    """
    
    resource_name = "ParametersParameter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name from the definition.
        Type `str`. """
        
        self.part = None
        """ Named part of a parameter (e.g. Tuple).
        List of `ParametersParameterPart` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ If parameter is a data type.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueBoolean = False
        """ If parameter is a data type.
        Type `bool`. """
        
        self.valueCode = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ If parameter is a data type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ If parameter is a data type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ If parameter is a data type.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ If parameter is a data type.
        Type `float`. """
        
        self.valueHumanName = None
        """ If parameter is a data type.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ If parameter is a data type.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ If parameter is a data type.
        Type `int`. """
        
        self.valuePeriod = None
        """ If parameter is a data type.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ If parameter is a data type.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ If parameter is a data type.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ If parameter is a data type.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ If parameter is a data type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ If parameter is a data type.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueTime = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        """ If parameter is a data type.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueUri = None
        """ If parameter is a data type.
        Type `str`. """
        
        super(ParametersParameter, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ParametersParameter, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'part' in jsondict:
            self.part = ParametersParameterPart.with_json_and_owner(jsondict['part'], self)
        if 'resource' in jsondict:
            self.resource = resource.Resource.with_json_and_owner(jsondict['resource'], self)
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
        if 'valueContactPoint' in jsondict:
            self.valueContactPoint = contactpoint.ContactPoint.with_json_and_owner(jsondict['valueContactPoint'], self)
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
        if 'valueReference' in jsondict:
            self.valueReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['valueReference'], self)
        if 'valueSignature' in jsondict:
            self.valueSignature = signature.Signature.with_json_and_owner(jsondict['valueSignature'], self)
        if 'valueString' in jsondict:
            self.valueString = jsondict['valueString']
        if 'valueTime' in jsondict:
            self.valueTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueTime'], self)
        if 'valueTiming' in jsondict:
            self.valueTiming = timing.Timing.with_json_and_owner(jsondict['valueTiming'], self)
        if 'valueUri' in jsondict:
            self.valueUri = jsondict['valueUri']


class ParametersParameterPart(fhirelement.FHIRElement):
    """ Named part of a parameter (e.g. Tuple).
    
    A named part of a parameter. In many implementation context, a set of named
    parts is known as a "Tuple".
    """
    
    resource_name = "ParametersParameterPart"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name from the definition.
        Type `str`. """
        
        self.resource = None
        """ If part is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        """ Value of the part.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Value of the part.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ Value of the part.
        Type `str`. """
        
        self.valueBoolean = False
        """ Value of the part.
        Type `bool`. """
        
        self.valueCode = None
        """ Value of the part.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ Value of the part.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Value of the part.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ Value of the part.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ Value of the part.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Value of the part.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Value of the part.
        Type `float`. """
        
        self.valueHumanName = None
        """ Value of the part.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ Value of the part.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ Value of the part.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Value of the part.
        Type `int`. """
        
        self.valuePeriod = None
        """ Value of the part.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value of the part.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value of the part.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Value of the part.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Value of the part.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ Value of the part.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Value of the part.
        Type `str`. """
        
        self.valueTime = None
        """ Value of the part.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        """ Value of the part.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueUri = None
        """ Value of the part.
        Type `str`. """
        
        super(ParametersParameterPart, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ParametersParameterPart, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'resource' in jsondict:
            self.resource = resource.Resource.with_json_and_owner(jsondict['resource'], self)
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
        if 'valueContactPoint' in jsondict:
            self.valueContactPoint = contactpoint.ContactPoint.with_json_and_owner(jsondict['valueContactPoint'], self)
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
        if 'valueReference' in jsondict:
            self.valueReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['valueReference'], self)
        if 'valueSignature' in jsondict:
            self.valueSignature = signature.Signature.with_json_and_owner(jsondict['valueSignature'], self)
        if 'valueString' in jsondict:
            self.valueString = jsondict['valueString']
        if 'valueTime' in jsondict:
            self.valueTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueTime'], self)
        if 'valueTiming' in jsondict:
            self.valueTiming = timing.Timing.with_json_and_owner(jsondict['valueTiming'], self)
        if 'valueUri' in jsondict:
            self.valueUri = jsondict['valueUri']

