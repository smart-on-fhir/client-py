#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory) on 2015-09-24.
#  2015, SMART Health IT.


from . import annotation
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range


class FamilyMemberHistory(domainresource.DomainResource):
    """ Information about patient's relatives, relevant for patient.
    
    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """
    
    resource_name = "FamilyMemberHistory"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.ageQuantity = None
        """ (approximate) age.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
        
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
        List of `FamilyMemberHistoryCondition` items (represented as `dict` in JSON). """
        
        self.date = None
        """ When history was captured/updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedBoolean = None
        """ Dead? How old/when?.
        Type `bool`. """
        
        self.deceasedDate = None
        """ Dead? How old/when?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedQuantity = None
        """ Dead? How old/when?.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
        
        self.deceasedRange = None
        """ Dead? How old/when?.
        Type `Range` (represented as `dict` in JSON). """
        
        self.deceasedString = None
        """ Dead? How old/when?.
        Type `str`. """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None
        """ External Id(s) for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ The family member described.
        Type `str`. """
        
        self.note = None
        """ General note about related person.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient history is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ Relationship to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ partial | completed | entered-in-error | health-unknown.
        Type `str`. """
        
        super(FamilyMemberHistory, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("ageQuantity", "ageQuantity", quantity.Quantity, False),
            ("ageRange", "ageRange", range.Range, False),
            ("ageString", "ageString", str, False),
            ("bornDate", "bornDate", fhirdate.FHIRDate, False),
            ("bornPeriod", "bornPeriod", period.Period, False),
            ("bornString", "bornString", str, False),
            ("condition", "condition", FamilyMemberHistoryCondition, True),
            ("date", "date", fhirdate.FHIRDate, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False),
            ("deceasedDate", "deceasedDate", fhirdate.FHIRDate, False),
            ("deceasedQuantity", "deceasedQuantity", quantity.Quantity, False),
            ("deceasedRange", "deceasedRange", range.Range, False),
            ("deceasedString", "deceasedString", str, False),
            ("gender", "gender", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("name", "name", str, False),
            ("note", "note", annotation.Annotation, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False),
            ("status", "status", str, False),
        ])
        return js


class FamilyMemberHistoryCondition(fhirelement.FHIRElement):
    """ Condition that the related person had.
    
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    
    resource_name = "FamilyMemberHistoryCondition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Condition suffered by relation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None
        """ Extra information about condition.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.onsetPeriod = None
        """ When condition first manifested.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetQuantity = None
        """ When condition first manifested.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        """ When condition first manifested.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None
        """ When condition first manifested.
        Type `str`. """
        
        self.outcome = None
        """ deceased | permanent disability | etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(FamilyMemberHistoryCondition, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("note", "note", annotation.Annotation, False),
            ("onsetPeriod", "onsetPeriod", period.Period, False),
            ("onsetQuantity", "onsetQuantity", quantity.Quantity, False),
            ("onsetRange", "onsetRange", range.Range, False),
            ("onsetString", "onsetString", str, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False),
        ])
        return js

