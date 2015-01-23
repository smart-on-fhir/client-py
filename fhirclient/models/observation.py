#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (observation.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import attachment
import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period
import quantity
import range
import ratio
import sampleddata


class Observation(fhirresource.FHIRResource):
    """ Measurements and simple assertions.
    
    Measurements and simple assertions made about a patient, device or other
    subject.
    """
    
    resource_name = "Observation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.appliesDateTime = None
        """ Physiologically Relevant time/time-period for observation.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.appliesPeriod = None
        """ Physiologically Relevant time/time-period for observation.
        Type `Period` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Observed body part.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comments = None
        """ Comments about result.
        Type `str`. """
        
        self.dataAbsentReason = None
        """ unknown | asked | temp | notasked +.
        Type `str`. """
        
        self.encounter = None
        """ Healthcare event related to the observation.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique Id for this particular observation.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.interpretation = None
        """ High, low, normal, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Date/Time this was made available.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.method = None
        """ How it was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.name = None
        """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who did the observation.
        List of `FHIRReference` items referencing `Practitioner, Device, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.referenceRange = None
        """ Provides guide for interpretation.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
        
        self.related = None
        """ Observations related to this observation.
        List of `ObservationRelated` items (represented as `dict` in JSON). """
        
        self.reliability = None
        """ ok | ongoing | early | questionable | calibrating | error +.
        Type `str`. """
        
        self.specimen = None
        """ Specimen used for this observation.
        Type `FHIRReference` referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | preliminary | final | amended +.
        Type `str`. """
        
        self.subject = None
        """ Who and/or what this is about.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Actual result.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Actual result.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueDateTime = None
        """ Actual result.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valuePeriod = None
        """ Actual result.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Actual result.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Actual result.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ Actual result.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Actual result.
        Type `str`. """
        
        self.valueTime = None
        """ Actual result.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Observation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Observation, self).update_with_json(jsondict)
        if 'appliesDateTime' in jsondict:
            self.appliesDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['appliesDateTime'], self)
        if 'appliesPeriod' in jsondict:
            self.appliesPeriod = period.Period.with_json_and_owner(jsondict['appliesPeriod'], self)
        if 'bodySite' in jsondict:
            self.bodySite = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['bodySite'], self)
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'dataAbsentReason' in jsondict:
            self.dataAbsentReason = jsondict['dataAbsentReason']
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'interpretation' in jsondict:
            self.interpretation = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['interpretation'], self)
        if 'issued' in jsondict:
            self.issued = fhirdate.FHIRDate.with_json_and_owner(jsondict['issued'], self)
        if 'method' in jsondict:
            self.method = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['method'], self)
        if 'name' in jsondict:
            self.name = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['name'], self)
        if 'performer' in jsondict:
            self.performer = fhirreference.FHIRReference.with_json_and_owner(jsondict['performer'], self)
        if 'referenceRange' in jsondict:
            self.referenceRange = ObservationReferenceRange.with_json_and_owner(jsondict['referenceRange'], self)
        if 'related' in jsondict:
            self.related = ObservationRelated.with_json_and_owner(jsondict['related'], self)
        if 'reliability' in jsondict:
            self.reliability = jsondict['reliability']
        if 'specimen' in jsondict:
            self.specimen = fhirreference.FHIRReference.with_json_and_owner(jsondict['specimen'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'valueAttachment' in jsondict:
            self.valueAttachment = attachment.Attachment.with_json_and_owner(jsondict['valueAttachment'], self)
        if 'valueCodeableConcept' in jsondict:
            self.valueCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['valueCodeableConcept'], self)
        if 'valueDateTime' in jsondict:
            self.valueDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueDateTime'], self)
        if 'valuePeriod' in jsondict:
            self.valuePeriod = period.Period.with_json_and_owner(jsondict['valuePeriod'], self)
        if 'valueQuantity' in jsondict:
            self.valueQuantity = quantity.Quantity.with_json_and_owner(jsondict['valueQuantity'], self)
        if 'valueRatio' in jsondict:
            self.valueRatio = ratio.Ratio.with_json_and_owner(jsondict['valueRatio'], self)
        if 'valueSampledData' in jsondict:
            self.valueSampledData = sampleddata.SampledData.with_json_and_owner(jsondict['valueSampledData'], self)
        if 'valueString' in jsondict:
            self.valueString = jsondict['valueString']
        if 'valueTime' in jsondict:
            self.valueTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['valueTime'], self)


class ObservationReferenceRange(fhirelement.FHIRElement):
    """ Provides guide for interpretation.
    
    Guidance on how to interpret the value by comparison to a normal or
    recommended range.
    """
    
    resource_name = "ObservationReferenceRange"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.age = None
        """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.high = None
        """ High Range, if relevant.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.low = None
        """ Low Range, if relevant.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.meaning = None
        """ Indicates the meaning/use of this range of this range.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text based reference range in an observation.
        Type `str`. """
        
        super(ObservationReferenceRange, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ObservationReferenceRange, self).update_with_json(jsondict)
        if 'age' in jsondict:
            self.age = range.Range.with_json_and_owner(jsondict['age'], self)
        if 'high' in jsondict:
            self.high = quantity.Quantity.with_json_and_owner(jsondict['high'], self)
        if 'low' in jsondict:
            self.low = quantity.Quantity.with_json_and_owner(jsondict['low'], self)
        if 'meaning' in jsondict:
            self.meaning = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['meaning'], self)
        if 'text' in jsondict:
            self.text = jsondict['text']


class ObservationRelated(fhirelement.FHIRElement):
    """ Observations related to this observation.
    
    Related observations - either components, or previous observations, or
    statements of derivation.
    """
    
    resource_name = "ObservationRelated"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.target = None
        """ Observation that is related to this one.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        self.type = None
        """ has-component | has-member | derived-from | sequel-to | replaces |
        qualified-by | interfered-by.
        Type `str`. """
        
        super(ObservationRelated, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ObservationRelated, self).update_with_json(jsondict)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']

