# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance).
# 2024, SMART Health IT.


from . import domainresource

class AllergyIntolerance(domainresource.DomainResource):
    """ Allergy or Intolerance (generally: Risk of adverse reaction to a substance).
    
    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    
    resource_type = "AllergyIntolerance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asserter = None
        """ Source of the information about the allergy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._asserter = None
        """ Primitive extension for asserter. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ food | medication | environment | biologic.
        List of `str` items. """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.clinicalStatus = None
        """ active | inactive | resolved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._clinicalStatus = None
        """ Primitive extension for clinicalStatus. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Code that identifies the allergy or intolerance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.criticality = None
        """ low | high | unable-to-assess.
        Type `str`. """
        self._criticality = None
        """ Primitive extension for criticality. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter when the allergy or intolerance was asserted.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.lastOccurrence = None
        """ Date(/time) of last known occurrence of a reaction.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._lastOccurrence = None
        """ Primitive extension for lastOccurrence. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Additional text not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.onsetAge = None
        """ When allergy or intolerance was identified.
        Type `Age` (represented as `dict` in JSON). """
        self._onsetAge = None
        """ Primitive extension for onsetAge. Type `FHIRPrimitiveExtension` """
        
        self.onsetDateTime = None
        """ When allergy or intolerance was identified.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._onsetDateTime = None
        """ Primitive extension for onsetDateTime. Type `FHIRPrimitiveExtension` """
        
        self.onsetPeriod = None
        """ When allergy or intolerance was identified.
        Type `Period` (represented as `dict` in JSON). """
        self._onsetPeriod = None
        """ Primitive extension for onsetPeriod. Type `FHIRPrimitiveExtension` """
        
        self.onsetRange = None
        """ When allergy or intolerance was identified.
        Type `Range` (represented as `dict` in JSON). """
        self._onsetRange = None
        """ Primitive extension for onsetRange. Type `FHIRPrimitiveExtension` """
        
        self.onsetString = None
        """ When allergy or intolerance was identified.
        Type `str`. """
        self._onsetString = None
        """ Primitive extension for onsetString. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Who the sensitivity is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.reaction = None
        """ Adverse Reaction Events linked to exposure to substance.
        List of `AllergyIntoleranceReaction` items (represented as `dict` in JSON). """
        self._reaction = None
        """ Primitive extension for reaction. Type `FHIRPrimitiveExtension` """
        
        self.recordedDate = None
        """ Date first version of the resource instance was recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._recordedDate = None
        """ Primitive extension for recordedDate. Type `FHIRPrimitiveExtension` """
        
        self.recorder = None
        """ Who recorded the sensitivity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._recorder = None
        """ Primitive extension for recorder. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ allergy | intolerance - Underlying mechanism (if known).
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.verificationStatus = None
        """ unconfirmed | confirmed | refuted | entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._verificationStatus = None
        """ Primitive extension for verificationStatus. Type `FHIRPrimitiveExtension` """
        
        super(AllergyIntolerance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("_asserter", "_asserter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", str, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("_clinicalStatus", "_clinicalStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("criticality", "criticality", str, False, None, False),
            ("_criticality", "_criticality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lastOccurrence", "lastOccurrence", fhirdatetime.FHIRDateTime, False, None, False),
            ("_lastOccurrence", "_lastOccurrence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("_onsetAge", "_onsetAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetDateTime", "onsetDateTime", fhirdatetime.FHIRDateTime, False, "onset", False),
            ("_onsetDateTime", "_onsetDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("_onsetPeriod", "_onsetPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("_onsetRange", "_onsetRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("_onsetString", "_onsetString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reaction", "reaction", AllergyIntoleranceReaction, True, None, False),
            ("_reaction", "_reaction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recordedDate", "recordedDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_recordedDate", "_recordedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("_recorder", "_recorder", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False),
            ("_verificationStatus", "_verificationStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.
    
    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """
    
    resource_type = "AllergyIntoleranceReaction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of the event as a whole.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.exposureRoute = None
        """ How the subject was exposed to the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._exposureRoute = None
        """ Primitive extension for exposureRoute. Type `FHIRPrimitiveExtension` """
        
        self.manifestation = None
        """ Clinical symptoms/signs associated with the Event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._manifestation = None
        """ Primitive extension for manifestation. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Text about event not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.onset = None
        """ Date(/time) when manifestations showed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._onset = None
        """ Primitive extension for onset. Type `FHIRPrimitiveExtension` """
        
        self.severity = None
        """ mild | moderate | severe (of event as a whole).
        Type `str`. """
        self._severity = None
        """ Primitive extension for severity. Type `FHIRPrimitiveExtension` """
        
        self.substance = None
        """ Specific substance or pharmaceutical product considered to be
        responsible for event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._substance = None
        """ Primitive extension for substance. Type `FHIRPrimitiveExtension` """
        
        super(AllergyIntoleranceReaction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("exposureRoute", "exposureRoute", codeableconcept.CodeableConcept, False, None, False),
            ("_exposureRoute", "_exposureRoute", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manifestation", "manifestation", codeableconcept.CodeableConcept, True, None, True),
            ("_manifestation", "_manifestation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onset", "onset", fhirdatetime.FHIRDateTime, False, None, False),
            ("_onset", "_onset", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("_severity", "_severity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False),
            ("_substance", "_substance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import age
from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import range