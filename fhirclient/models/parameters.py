#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Parameters) on 2015-07-06.
#  2015, SMART Health IT.


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import humanname
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import resource
from . import signature
from . import timing


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
    
    def elementProperties(self):
        js = super(Parameters, self).elementProperties()
        js.extend([
            ("parameter", "parameter", ParametersParameter, True),
        ])
        return js


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
        
        self.valueBoolean = None
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
    
    def elementProperties(self):
        js = super(ParametersParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("part", "part", ParametersParameterPart, True),
            ("resource", "resource", resource.Resource, False),
            ("valueAddress", "valueAddress", address.Address, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False),
            ("valueBase64Binary", "valueBase64Binary", str, False),
            ("valueBoolean", "valueBoolean", bool, False),
            ("valueCode", "valueCode", str, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False),
            ("valueCoding", "valueCoding", coding.Coding, False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False),
            ("valueDecimal", "valueDecimal", float, False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False),
            ("valueInteger", "valueInteger", int, False),
            ("valuePeriod", "valuePeriod", period.Period, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False),
            ("valueRange", "valueRange", range.Range, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False),
            ("valueSignature", "valueSignature", signature.Signature, False),
            ("valueString", "valueString", str, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False),
            ("valueTiming", "valueTiming", timing.Timing, False),
            ("valueUri", "valueUri", str, False),
        ])
        return js


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
        
        self.valueBoolean = None
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
    
    def elementProperties(self):
        js = super(ParametersParameterPart, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("resource", "resource", resource.Resource, False),
            ("valueAddress", "valueAddress", address.Address, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False),
            ("valueBase64Binary", "valueBase64Binary", str, False),
            ("valueBoolean", "valueBoolean", bool, False),
            ("valueCode", "valueCode", str, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False),
            ("valueCoding", "valueCoding", coding.Coding, False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False),
            ("valueDecimal", "valueDecimal", float, False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False),
            ("valueInteger", "valueInteger", int, False),
            ("valuePeriod", "valuePeriod", period.Period, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False),
            ("valueRange", "valueRange", range.Range, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False),
            ("valueSignature", "valueSignature", signature.Signature, False),
            ("valueString", "valueString", str, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False),
            ("valueTiming", "valueTiming", timing.Timing, False),
            ("valueUri", "valueUri", str, False),
        ])
        return js

