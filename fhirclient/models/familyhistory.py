#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (familyhistory.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import age
import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import period
import range


class FamilyHistory(fhirresource.FHIRResource):
    """ Information about patient's relatives, relevant for patient.
    
    Scope and Usage This resource records significant health events and
    conditions for people related to the subject. This information can be known
    to different levels of accuracy. Sometimes the exact condition ('asthma')
    is known, and sometimes it is less precise ('some sort of cancer').
    Equally, sometimes the person can be identified ('my aunt Agatha') and
    sometimes all that is known is that the person was an uncle.
    
    This resource represents a simple structure used to capture an 'elementary'
    family history. However, it can also be the basis for capturing a more
    rigorous history useful for genetic and other analysis - refer to the
    Genetic Pedigree profile for an example.
    
    The entire family history for an individual is stored in a single resource.
    """
    
    resource_name = "FamilyHistory"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ External Id(s) for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional details not covered elsewhere.
        Type `str`. """
        
        self.relation = None
        """ Relative described by history.
        List of `FamilyHistoryRelation` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Patient history is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(FamilyHistory, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(FamilyHistory, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'note' in jsondict:
            self.note = jsondict['note']
        if 'relation' in jsondict:
            self.relation = FamilyHistoryRelation.with_json(jsondict['relation'])
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class FamilyHistoryRelation(fhirelement.FHIRElement):
    """ Relative described by history.
    
    The related person. Each FamilyHistory resource contains the entire family
    history for a single person.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bornDate = None
        """ (approximate) date of birth.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.bornPeriod = None
        """ (approximate) date of birth.
        Type `Period` (represented as `dict` in JSON). """
        
        self.bornString = None
        """ (approximate) date of birth.
        Type `str`. """
        
        self.condition = None
        """ Condition that the related person had.
        List of `FamilyHistoryRelationCondition` items (represented as `dict` in JSON). """
        
        self.deceasedAge = None
        """ Dead? How old/when?.
        Type `Age` (represented as `dict` in JSON). """
        
        self.deceasedBoolean = False
        """ Dead? How old/when?.
        Type `bool`. """
        
        self.deceasedDate = None
        """ Dead? How old/when?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedRange = None
        """ Dead? How old/when?.
        Type `Range` (represented as `dict` in JSON). """
        
        self.deceasedString = None
        """ Dead? How old/when?.
        Type `str`. """
        
        self.name = None
        """ The family member described.
        Type `str`. """
        
        self.note = None
        """ General note about related person.
        Type `str`. """
        
        self.relationship = None
        """ Relationship to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(FamilyHistoryRelation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(FamilyHistoryRelation, self).update_with_json(jsondict)
        if 'bornDate' in jsondict:
            self.bornDate = fhirdate.FHIRDate.with_json(jsondict['bornDate'])
        if 'bornPeriod' in jsondict:
            self.bornPeriod = period.Period.with_json(jsondict['bornPeriod'])
        if 'bornString' in jsondict:
            self.bornString = jsondict['bornString']
        if 'condition' in jsondict:
            self.condition = FamilyHistoryRelationCondition.with_json(jsondict['condition'])
        if 'deceasedAge' in jsondict:
            self.deceasedAge = age.Age.with_json(jsondict['deceasedAge'])
        if 'deceasedBoolean' in jsondict:
            self.deceasedBoolean = jsondict['deceasedBoolean']
        if 'deceasedDate' in jsondict:
            self.deceasedDate = fhirdate.FHIRDate.with_json(jsondict['deceasedDate'])
        if 'deceasedRange' in jsondict:
            self.deceasedRange = range.Range.with_json(jsondict['deceasedRange'])
        if 'deceasedString' in jsondict:
            self.deceasedString = jsondict['deceasedString']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'note' in jsondict:
            self.note = jsondict['note']
        if 'relationship' in jsondict:
            self.relationship = codeableconcept.CodeableConcept.with_json(jsondict['relationship'])


class FamilyHistoryRelationCondition(fhirelement.FHIRElement):
    """ Condition that the related person had.
    
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.note = None
        """ Extra information about condition.
        Type `str`. """
        
        self.onsetAge = None
        """ When condition first manifested.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        """ When condition first manifested.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None
        """ When condition first manifested.
        Type `str`. """
        
        self.outcome = None
        """ deceased | permanent disability | etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Condition suffered by relation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(FamilyHistoryRelationCondition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(FamilyHistoryRelationCondition, self).update_with_json(jsondict)
        if 'note' in jsondict:
            self.note = jsondict['note']
        if 'onsetAge' in jsondict:
            self.onsetAge = age.Age.with_json(jsondict['onsetAge'])
        if 'onsetRange' in jsondict:
            self.onsetRange = range.Range.with_json(jsondict['onsetRange'])
        if 'onsetString' in jsondict:
            self.onsetString = jsondict['onsetString']
        if 'outcome' in jsondict:
            self.outcome = codeableconcept.CodeableConcept.with_json(jsondict['outcome'])
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])

