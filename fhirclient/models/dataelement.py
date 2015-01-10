#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (dataelement.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import address
import attachment
import codeableconcept
import coding
import contactpoint
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import humanname
import identifier
import period
import quantity
import range
import ratio
import timing


class DataElement(fhirresource.FHIRResource):
    """ Resource data element.
    
    The formal description of a single piece of information that can be
    gathered and reported.
    """
    
    resource_name = "DataElement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `DataElementBinding` (represented as `dict` in JSON). """
        
        self.category = None
        """ Assist with indexing and finding.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Identifying concept.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.comments = None
        """ Comments about the use of this element.
        Type `str`. """
        
        self.date = None
        """ Date for this version of the data element.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.definition = None
        """ Definition/description as narrative text.
        Type `str`. """
        
        self.exampleAddress = None
        """ Example value: [as defined for type].
        Type `Address` (represented as `dict` in JSON). """
        
        self.exampleAttachment = None
        """ Example value: [as defined for type].
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.exampleBase64Binary = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleBoolean = False
        """ Example value: [as defined for type].
        Type `bool`. """
        
        self.exampleCode = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleCodeableConcept = None
        """ Example value: [as defined for type].
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.exampleCoding = None
        """ Example value: [as defined for type].
        Type `Coding` (represented as `dict` in JSON). """
        
        self.exampleContactPoint = None
        """ Example value: [as defined for type].
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.exampleDate = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleDateTime = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleDecimal = None
        """ Example value: [as defined for type].
        Type `float`. """
        
        self.exampleHumanName = None
        """ Example value: [as defined for type].
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.exampleIdentifier = None
        """ Example value: [as defined for type].
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.exampleInstant = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleInteger = None
        """ Example value: [as defined for type].
        Type `int`. """
        
        self.examplePeriod = None
        """ Example value: [as defined for type].
        Type `Period` (represented as `dict` in JSON). """
        
        self.exampleQuantity = None
        """ Example value: [as defined for type].
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.exampleRange = None
        """ Example value: [as defined for type].
        Type `Range` (represented as `dict` in JSON). """
        
        self.exampleRatio = None
        """ Example value: [as defined for type].
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.exampleReference = None
        """ Example value: [as defined for type].
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.exampleString = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleTime = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleTiming = None
        """ Example value: [as defined for type].
        Type `Timing` (represented as `dict` in JSON). """
        
        self.exampleUri = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.granularity = None
        """ comparable | fully specified | equivalent | convertable | scaleable
        | flexible.
        Type `str`. """
        
        self.identifier = None
        """ Logical id to reference this data element.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.label = None
        """ Name for element to display with or prompt for element.
        Type `str`. """
        
        self.mapping = None
        """ Map element to another set of definitions.
        List of `DataElementMapping` items (represented as `dict` in JSON). """
        
        self.maxLength = None
        """ Length for strings.
        Type `int`. """
        
        self.name = None
        """ Descriptive label for this element definition.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.question = None
        """ Prompt for element phrased as question.
        Type `str`. """
        
        self.requirements = None
        """ Why is this needed?.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.synonym = None
        """ Other names.
        List of `str` items. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Name of Data type.
        Type `str`. """
        
        self.unitsCodeableConcept = None
        """ Units to use for measured value.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unitsReference = None
        """ Units to use for measured value.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the data element.
        Type `str`. """
        
        super(DataElement, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DataElement, self).update_with_json(jsondict)
        if 'binding' in jsondict:
            self.binding = DataElementBinding.with_json_and_owner(jsondict['binding'], self)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'definition' in jsondict:
            self.definition = jsondict['definition']
        if 'exampleAddress' in jsondict:
            self.exampleAddress = address.Address.with_json_and_owner(jsondict['exampleAddress'], self)
        if 'exampleAttachment' in jsondict:
            self.exampleAttachment = attachment.Attachment.with_json_and_owner(jsondict['exampleAttachment'], self)
        if 'exampleBase64Binary' in jsondict:
            self.exampleBase64Binary = jsondict['exampleBase64Binary']
        if 'exampleBoolean' in jsondict:
            self.exampleBoolean = jsondict['exampleBoolean']
        if 'exampleCode' in jsondict:
            self.exampleCode = jsondict['exampleCode']
        if 'exampleCodeableConcept' in jsondict:
            self.exampleCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['exampleCodeableConcept'], self)
        if 'exampleCoding' in jsondict:
            self.exampleCoding = coding.Coding.with_json_and_owner(jsondict['exampleCoding'], self)
        if 'exampleContactPoint' in jsondict:
            self.exampleContactPoint = contactpoint.ContactPoint.with_json_and_owner(jsondict['exampleContactPoint'], self)
        if 'exampleDate' in jsondict:
            self.exampleDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['exampleDate'], self)
        if 'exampleDateTime' in jsondict:
            self.exampleDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['exampleDateTime'], self)
        if 'exampleDecimal' in jsondict:
            self.exampleDecimal = jsondict['exampleDecimal']
        if 'exampleHumanName' in jsondict:
            self.exampleHumanName = humanname.HumanName.with_json_and_owner(jsondict['exampleHumanName'], self)
        if 'exampleIdentifier' in jsondict:
            self.exampleIdentifier = identifier.Identifier.with_json_and_owner(jsondict['exampleIdentifier'], self)
        if 'exampleInstant' in jsondict:
            self.exampleInstant = fhirdate.FHIRDate.with_json_and_owner(jsondict['exampleInstant'], self)
        if 'exampleInteger' in jsondict:
            self.exampleInteger = jsondict['exampleInteger']
        if 'examplePeriod' in jsondict:
            self.examplePeriod = period.Period.with_json_and_owner(jsondict['examplePeriod'], self)
        if 'exampleQuantity' in jsondict:
            self.exampleQuantity = quantity.Quantity.with_json_and_owner(jsondict['exampleQuantity'], self)
        if 'exampleRange' in jsondict:
            self.exampleRange = range.Range.with_json_and_owner(jsondict['exampleRange'], self)
        if 'exampleRatio' in jsondict:
            self.exampleRatio = ratio.Ratio.with_json_and_owner(jsondict['exampleRatio'], self)
        if 'exampleReference' in jsondict:
            self.exampleReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['exampleReference'], self)
        if 'exampleString' in jsondict:
            self.exampleString = jsondict['exampleString']
        if 'exampleTime' in jsondict:
            self.exampleTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['exampleTime'], self)
        if 'exampleTiming' in jsondict:
            self.exampleTiming = timing.Timing.with_json_and_owner(jsondict['exampleTiming'], self)
        if 'exampleUri' in jsondict:
            self.exampleUri = jsondict['exampleUri']
        if 'granularity' in jsondict:
            self.granularity = jsondict['granularity']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'label' in jsondict:
            self.label = jsondict['label']
        if 'mapping' in jsondict:
            self.mapping = DataElementMapping.with_json_and_owner(jsondict['mapping'], self)
        if 'maxLength' in jsondict:
            self.maxLength = jsondict['maxLength']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'question' in jsondict:
            self.question = jsondict['question']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'synonym' in jsondict:
            self.synonym = jsondict['synonym']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'unitsCodeableConcept' in jsondict:
            self.unitsCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['unitsCodeableConcept'], self)
        if 'unitsReference' in jsondict:
            self.unitsReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['unitsReference'], self)
        if 'version' in jsondict:
            self.version = jsondict['version']


class DataElementBinding(fhirelement.FHIRElement):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept).
    """
    
    resource_name = "DataElementBinding"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.conformance = None
        """ required | preferred | example.
        Type `str`. """
        
        self.description = None
        """ Human explanation of the value set.
        Type `str`. """
        
        self.isExtensible = False
        """ Can additional codes be used?.
        Type `bool`. """
        
        self.valueSet = None
        """ Source of value set.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        super(DataElementBinding, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DataElementBinding, self).update_with_json(jsondict)
        if 'conformance' in jsondict:
            self.conformance = jsondict['conformance']
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'isExtensible' in jsondict:
            self.isExtensible = jsondict['isExtensible']
        if 'valueSet' in jsondict:
            self.valueSet = fhirreference.FHIRReference.with_json_and_owner(jsondict['valueSet'], self)


class DataElementMapping(fhirelement.FHIRElement):
    """ Map element to another set of definitions.
    
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    
    resource_name = "DataElementMapping"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comments = None
        """ Versions, Issues, Scope limitations etc.
        Type `str`. """
        
        self.definitional = False
        """ True if mapping defines element.
        Type `bool`. """
        
        self.map = None
        """ Details of the mapping.
        Type `str`. """
        
        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """
        
        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """
        
        super(DataElementMapping, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DataElementMapping, self).update_with_json(jsondict)
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'definitional' in jsondict:
            self.definitional = jsondict['definitional']
        if 'map' in jsondict:
            self.map = jsondict['map']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'uri' in jsondict:
            self.uri = jsondict['uri']

