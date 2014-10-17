#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (composition.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import CodeableConcept
import Coding
import Encounter
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Narrative
import Organization
import Patient
import Period
import Practitioner


class Composition(FHIRResource.FHIRResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.
    
    Scope and Usage A Composition is also the basic structure from which FHIR
    Documents - immutable bundles with attested narrative - are built. A single
    logical composition may be associated with a series of derived documents,
    each of which is a frozen copy of the composition.
    
    Note: EN 13606 uses the term "Composition" to refer to a single commit to
    an EHR system, and offers some common examples: a consultation note, a
    progress note, a report or a letter, an investigation report, a
    prescription form and a set of bedside nursing observations. These logical
    examples are all valid uses of a Composition resource, but it is not
    required that all the resources are updated in a single commit.
    """
    
    resource_name = "Composition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.attester = None
        """ Attests to accuracy of composition.
        List of `CompositionAttester` items (represented as `dict` in JSON). """
        
        self.author = None
        """ Who and/or what authored the composition.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.confidentiality = None
        """ As defined by affinity domain.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.custodian = None
        """ Org which maintains the composition.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.date = None
        """ Composition editing time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None
        """ Context of the conposition.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.event = None
        """ The clinical event/act/item being documented.
        Type `CompositionEvent` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Logical identifier of composition (version-independent).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.klass = None
        """ Categorization of Composition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.section = None
        """ Composition is broken into sections.
        List of `CompositionSection` items (represented as `dict` in JSON). """
        
        self.status = None
        """ preliminary | final | appended | amended | entered in error.
        Type `str`. """
        
        self.subject = None
        """ Who and/or what the composition is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.title = None
        """ Human Readable name/title.
        Type `str`. """
        
        self.type = None
        """ Kind of composition (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Composition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Composition, self).update_with_json(jsondict)
        if 'attester' in jsondict:
            self.attester = CompositionAttester.with_json(jsondict['attester'])
        if 'author' in jsondict:
            self.author = FHIRReference.FHIRReference.with_json_and_owner(jsondict['author'], self, Practitioner.Practitioner)
        if 'confidentiality' in jsondict:
            self.confidentiality = Coding.Coding.with_json(jsondict['confidentiality'])
        if 'custodian' in jsondict:
            self.custodian = FHIRReference.FHIRReference.with_json_and_owner(jsondict['custodian'], self, Organization.Organization)
        if 'date' in jsondict:
            self.date = FHIRDate.FHIRDate.with_json(jsondict['date'])
        if 'encounter' in jsondict:
            self.encounter = FHIRReference.FHIRReference.with_json_and_owner(jsondict['encounter'], self, Encounter.Encounter)
        if 'event' in jsondict:
            self.event = CompositionEvent.with_json(jsondict['event'])
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'klass' in jsondict:
            self.klass = CodeableConcept.CodeableConcept.with_json(jsondict['klass'])
        if 'section' in jsondict:
            self.section = CompositionSection.with_json(jsondict['section'])
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = FHIRReference.FHIRReference.with_json_and_owner(jsondict['subject'], self, Patient.Patient)
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'title' in jsondict:
            self.title = jsondict['title']
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])


class CompositionAttester(FHIRElement.FHIRElement):
    """ Attests to accuracy of composition.
    
    A participant who has attested to the accuracy of the composition/document.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.mode = None
        """ personal | professional | legal | official.
        List of `str` items. """
        
        self.party = None
        """ Who attested the composition.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.time = None
        """ When composition attested.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(CompositionAttester, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CompositionAttester, self).update_with_json(jsondict)
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'party' in jsondict:
            self.party = FHIRReference.FHIRReference.with_json_and_owner(jsondict['party'], self, Patient.Patient)
        if 'time' in jsondict:
            self.time = FHIRDate.FHIRDate.with_json(jsondict['time'])


class CompositionEvent(FHIRElement.FHIRElement):
    """ The clinical event/act/item being documented.
    
    The main event/act/item, such as a colonoscopy or an appendectomy, being
    documented.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code(s) that apply to the event being documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Full details for the event(s) the composition consents.
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period covered by the documentation.
        Type `Period` (represented as `dict` in JSON). """
        
        super(CompositionEvent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CompositionEvent, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = CodeableConcept.CodeableConcept.with_json(jsondict['code'])
        if 'detail' in jsondict:
            self.detail = FHIRReference.FHIRReference.with_json_and_owner(jsondict['detail'], self, FHIRResource.FHIRResource)
        if 'period' in jsondict:
            self.period = Period.Period.with_json(jsondict['period'])


class CompositionSection(FHIRElement.FHIRElement):
    """ Composition is broken into sections.
    
    The root of the sections that make up the composition.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Classification of section (recommended).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ The actual data for the section.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.section = None
        """ Nested Section.
        List of `CompositionSectionSection` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ If section different to composition.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.title = None
        """ Label for section.
        Type `str`. """
        
        super(CompositionSection, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CompositionSection, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = CodeableConcept.CodeableConcept.with_json(jsondict['code'])
        if 'content' in jsondict:
            self.content = FHIRReference.FHIRReference.with_json_and_owner(jsondict['content'], self, FHIRResource.FHIRResource)
        if 'section' in jsondict:
            self.section = CompositionSectionSection.with_json(jsondict['section'])
        if 'subject' in jsondict:
            self.subject = FHIRReference.FHIRReference.with_json_and_owner(jsondict['subject'], self, Patient.Patient)
        if 'title' in jsondict:
            self.title = jsondict['title']


class CompositionSectionSection(FHIRElement.FHIRElement):
    """ Nested Section.
    
    A nested sub-section within this section.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(CompositionSectionSection, self).__init__(jsondict)

