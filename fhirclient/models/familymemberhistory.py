# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory).
# 2024, SMART Health IT.


from . import domainresource

class FamilyMemberHistory(domainresource.DomainResource):
    """ Information about patient's relatives, relevant for patient.
    
    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """
    
    resource_type = "FamilyMemberHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ageAge = None
        """ (approximate) age.
        Type `Age` (represented as `dict` in JSON). """
        self._ageAge = None
        """ Primitive extension for ageAge. Type `FHIRPrimitiveExtension` """
        
        self.ageRange = None
        """ (approximate) age.
        Type `Range` (represented as `dict` in JSON). """
        self._ageRange = None
        """ Primitive extension for ageRange. Type `FHIRPrimitiveExtension` """
        
        self.ageString = None
        """ (approximate) age.
        Type `str`. """
        self._ageString = None
        """ Primitive extension for ageString. Type `FHIRPrimitiveExtension` """
        
        self.bornDate = None
        """ (approximate) date of birth.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._bornDate = None
        """ Primitive extension for bornDate. Type `FHIRPrimitiveExtension` """
        
        self.bornPeriod = None
        """ (approximate) date of birth.
        Type `Period` (represented as `dict` in JSON). """
        self._bornPeriod = None
        """ Primitive extension for bornPeriod. Type `FHIRPrimitiveExtension` """
        
        self.bornString = None
        """ (approximate) date of birth.
        Type `str`. """
        self._bornString = None
        """ Primitive extension for bornString. Type `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ Condition that the related person had.
        List of `FamilyMemberHistoryCondition` items (represented as `dict` in JSON). """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.dataAbsentReason = None
        """ subject-unknown | withheld | unable-to-obtain | deferred.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._dataAbsentReason = None
        """ Primitive extension for dataAbsentReason. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ When history was recorded or last updated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.deceasedAge = None
        """ Dead? How old/when?.
        Type `Age` (represented as `dict` in JSON). """
        self._deceasedAge = None
        """ Primitive extension for deceasedAge. Type `FHIRPrimitiveExtension` """
        
        self.deceasedBoolean = None
        """ Dead? How old/when?.
        Type `bool`. """
        self._deceasedBoolean = None
        """ Primitive extension for deceasedBoolean. Type `FHIRPrimitiveExtension` """
        
        self.deceasedDate = None
        """ Dead? How old/when?.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._deceasedDate = None
        """ Primitive extension for deceasedDate. Type `FHIRPrimitiveExtension` """
        
        self.deceasedRange = None
        """ Dead? How old/when?.
        Type `Range` (represented as `dict` in JSON). """
        self._deceasedRange = None
        """ Primitive extension for deceasedRange. Type `FHIRPrimitiveExtension` """
        
        self.deceasedString = None
        """ Dead? How old/when?.
        Type `str`. """
        self._deceasedString = None
        """ Primitive extension for deceasedString. Type `FHIRPrimitiveExtension` """
        
        self.estimatedAge = None
        """ Age is estimated?.
        Type `bool`. """
        self._estimatedAge = None
        """ Primitive extension for estimatedAge. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Id(s) for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        self._instantiatesCanonical = None
        """ Primitive extension for instantiatesCanonical. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        self._instantiatesUri = None
        """ Primitive extension for instantiatesUri. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ The family member described.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ General note about related person.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Patient history is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why was family member history performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why was family member history performed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.relationship = None
        """ Relationship to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._relationship = None
        """ Primitive extension for relationship. Type `FHIRPrimitiveExtension` """
        
        self.sex = None
        """ male | female | other | unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._sex = None
        """ Primitive extension for sex. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ partial | completed | entered-in-error | health-unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(FamilyMemberHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("ageAge", "ageAge", age.Age, False, "age", False),
            ("_ageAge", "_ageAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("_ageRange", "_ageRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ageString", "ageString", str, False, "age", False),
            ("_ageString", "_ageString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bornDate", "bornDate", fhirdate.FHIRDate, False, "born", False),
            ("_bornDate", "_bornDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bornPeriod", "bornPeriod", period.Period, False, "born", False),
            ("_bornPeriod", "_bornPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bornString", "bornString", str, False, "born", False),
            ("_bornString", "_bornString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("condition", "condition", FamilyMemberHistoryCondition, True, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("_dataAbsentReason", "_dataAbsentReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deceasedAge", "deceasedAge", age.Age, False, "deceased", False),
            ("_deceasedAge", "_deceasedAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("_deceasedBoolean", "_deceasedBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deceasedDate", "deceasedDate", fhirdate.FHIRDate, False, "deceased", False),
            ("_deceasedDate", "_deceasedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deceasedRange", "deceasedRange", range.Range, False, "deceased", False),
            ("_deceasedRange", "_deceasedRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deceasedString", "deceasedString", str, False, "deceased", False),
            ("_deceasedString", "_deceasedString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("estimatedAge", "estimatedAge", bool, False, None, False),
            ("_estimatedAge", "_estimatedAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, True),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sex", "sex", codeableconcept.CodeableConcept, False, None, False),
            ("_sex", "_sex", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """ Condition that the related person had.
    
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    
    resource_type = "FamilyMemberHistoryCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Condition suffered by relation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.contributedToDeath = None
        """ Whether the condition contributed to the cause of death.
        Type `bool`. """
        self._contributedToDeath = None
        """ Primitive extension for contributedToDeath. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Extra information about condition.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.onsetAge = None
        """ When condition first manifested.
        Type `Age` (represented as `dict` in JSON). """
        self._onsetAge = None
        """ Primitive extension for onsetAge. Type `FHIRPrimitiveExtension` """
        
        self.onsetPeriod = None
        """ When condition first manifested.
        Type `Period` (represented as `dict` in JSON). """
        self._onsetPeriod = None
        """ Primitive extension for onsetPeriod. Type `FHIRPrimitiveExtension` """
        
        self.onsetRange = None
        """ When condition first manifested.
        Type `Range` (represented as `dict` in JSON). """
        self._onsetRange = None
        """ Primitive extension for onsetRange. Type `FHIRPrimitiveExtension` """
        
        self.onsetString = None
        """ When condition first manifested.
        Type `str`. """
        self._onsetString = None
        """ Primitive extension for onsetString. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ deceased | permanent disability | etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        super(FamilyMemberHistoryCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contributedToDeath", "contributedToDeath", bool, False, None, False),
            ("_contributedToDeath", "_contributedToDeath", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("_onsetAge", "_onsetAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("_onsetPeriod", "_onsetPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("_onsetRange", "_onsetRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("_onsetString", "_onsetString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import age
from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import range