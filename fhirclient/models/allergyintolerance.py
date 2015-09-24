#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance) on 2015-09-24.
#  2015, SMART Health IT.


from . import annotation
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


class AllergyIntolerance(domainresource.DomainResource):
    """ Allergy or Intolerance (generally: Risk Of Adverse reaction to a substance).
    
    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    
    resource_name = "AllergyIntolerance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ food | medication | environment | other - Category of Substance.
        Type `str`. """
        
        self.criticality = None
        """ CRITL | CRITH | CRITU.
        Type `str`. """
        
        self.identifier = None
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastOccurence = None
        """ Date(/time) of last known occurrence of a reaction.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.note = None
        """ Additional text not captured in other fields.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.onset = None
        """ Date(/time) when manifestations showed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patient = None
        """ Who the sensitivity is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.reaction = None
        """ Adverse Reaction Events linked to exposure to substance.
        List of `AllergyIntoleranceReaction` items (represented as `dict` in JSON). """
        
        self.recordedDate = None
        """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recorder = None
        """ Who recorded the sensitivity.
        Type `FHIRReference` referencing `Practitioner, Patient` (represented as `dict` in JSON). """
        
        self.reporter = None
        """ Source of the information about the allergy.
        Type `FHIRReference` referencing `Patient, RelatedPerson, Practitioner` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | unconfirmed | confirmed | inactive | resolved | refuted |
        entered-in-error.
        Type `str`. """
        
        self.substance = None
        """ Substance, (or class) considered to be responsible for risk.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ allergy | intolerance - Underlying mechanism (if known).
        Type `str`. """
        
        super(AllergyIntolerance, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("category", "category", str, False),
            ("criticality", "criticality", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("lastOccurence", "lastOccurence", fhirdate.FHIRDate, False),
            ("note", "note", annotation.Annotation, False),
            ("onset", "onset", fhirdate.FHIRDate, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("reaction", "reaction", AllergyIntoleranceReaction, True),
            ("recordedDate", "recordedDate", fhirdate.FHIRDate, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False),
            ("reporter", "reporter", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False),
            ("type", "type", str, False),
        ])
        return js


class AllergyIntoleranceReaction(fhirelement.FHIRElement):
    """ Adverse Reaction Events linked to exposure to substance.
    
    Details about each adverse reaction event linked to exposure to the
    identified Substance.
    """
    
    resource_name = "AllergyIntoleranceReaction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.certainty = None
        """ unlikely | likely | confirmed - clinical certainty about the
        specific substance.
        Type `str`. """
        
        self.description = None
        """ Description of the event as a whole.
        Type `str`. """
        
        self.exposureRoute = None
        """ How the subject was exposed to the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manifestation = None
        """ Clinical symptoms/signs associated with the Event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Text about event not captured in other fields.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.onset = None
        """ Date(/time) when manifestations showed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.severity = None
        """ mild | moderate | severe (of event as a whole).
        Type `str`. """
        
        self.substance = None
        """ Specific substance considered to be responsible for event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AllergyIntoleranceReaction, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("certainty", "certainty", str, False),
            ("description", "description", str, False),
            ("exposureRoute", "exposureRoute", codeableconcept.CodeableConcept, False),
            ("manifestation", "manifestation", codeableconcept.CodeableConcept, True),
            ("note", "note", annotation.Annotation, False),
            ("onset", "onset", fhirdate.FHIRDate, False),
            ("severity", "severity", str, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False),
        ])
        return js

