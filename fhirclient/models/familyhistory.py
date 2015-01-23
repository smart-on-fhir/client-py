#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (familyhistory.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import age
import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period
import range


class FamilyHistory(fhirresource.FHIRResource):
    """ Information about patient's relatives, relevant for patient.
    
    Significant health events and conditions for people related to the subject
    relevant in the context of care for the subject.
    """
    
    resource_name = "FamilyHistory"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ When history was captured/updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ External Id(s) for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional details not covered elsewhere.
        Type `str`. """
        
        self.patient = None
        """ Patient history is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.relation = None
        """ Relative described by history.
        List of `FamilyHistoryRelation` items (represented as `dict` in JSON). """
        
        super(FamilyHistory, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(FamilyHistory, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'note' in jsondict:
            self.note = jsondict['note']
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'relation' in jsondict:
            self.relation = FamilyHistoryRelation.with_json_and_owner(jsondict['relation'], self)


class FamilyHistoryRelation(fhirelement.FHIRElement):
    """ Relative described by history.
    
    The related person. Each FamilyHistory resource contains the entire family
    history for a single person.
    """
    
    resource_name = "FamilyHistoryRelation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.ageAge = None
        """ (approximate) age.
        Type `Age` (represented as `dict` in JSON). """
        
        self.ageRange = None
        """ (approximate) age.
        Type `Range` (represented as `dict` in JSON). """
        
        self.ageString = None
        """ (approximate) age.
        Type `str`. """
        
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
        if 'ageAge' in jsondict:
            self.ageAge = age.Age.with_json_and_owner(jsondict['ageAge'], self)
        if 'ageRange' in jsondict:
            self.ageRange = range.Range.with_json_and_owner(jsondict['ageRange'], self)
        if 'ageString' in jsondict:
            self.ageString = jsondict['ageString']
        if 'bornDate' in jsondict:
            self.bornDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['bornDate'], self)
        if 'bornPeriod' in jsondict:
            self.bornPeriod = period.Period.with_json_and_owner(jsondict['bornPeriod'], self)
        if 'bornString' in jsondict:
            self.bornString = jsondict['bornString']
        if 'condition' in jsondict:
            self.condition = FamilyHistoryRelationCondition.with_json_and_owner(jsondict['condition'], self)
        if 'deceasedAge' in jsondict:
            self.deceasedAge = age.Age.with_json_and_owner(jsondict['deceasedAge'], self)
        if 'deceasedBoolean' in jsondict:
            self.deceasedBoolean = jsondict['deceasedBoolean']
        if 'deceasedDate' in jsondict:
            self.deceasedDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['deceasedDate'], self)
        if 'deceasedRange' in jsondict:
            self.deceasedRange = range.Range.with_json_and_owner(jsondict['deceasedRange'], self)
        if 'deceasedString' in jsondict:
            self.deceasedString = jsondict['deceasedString']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'note' in jsondict:
            self.note = jsondict['note']
        if 'relationship' in jsondict:
            self.relationship = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['relationship'], self)


class FamilyHistoryRelationCondition(fhirelement.FHIRElement):
    """ Condition that the related person had.
    
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    
    resource_name = "FamilyHistoryRelationCondition"
    
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
            self.onsetAge = age.Age.with_json_and_owner(jsondict['onsetAge'], self)
        if 'onsetRange' in jsondict:
            self.onsetRange = range.Range.with_json_and_owner(jsondict['onsetRange'], self)
        if 'onsetString' in jsondict:
            self.onsetString = jsondict['onsetString']
        if 'outcome' in jsondict:
            self.outcome = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['outcome'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

