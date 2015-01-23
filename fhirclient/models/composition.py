#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (composition.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period


class Composition(fhirresource.FHIRResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.
    
    A set of healthcare-related information that is assembled together into a
    single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement.
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
        List of `FHIRReference` items referencing `Practitioner, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
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
        """ The clinical service(s) being documented.
        List of `CompositionEvent` items (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device, Location` (represented as `dict` in JSON). """
        
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
            self.attester = CompositionAttester.with_json_and_owner(jsondict['attester'], self)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'confidentiality' in jsondict:
            self.confidentiality = coding.Coding.with_json_and_owner(jsondict['confidentiality'], self)
        if 'custodian' in jsondict:
            self.custodian = fhirreference.FHIRReference.with_json_and_owner(jsondict['custodian'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'event' in jsondict:
            self.event = CompositionEvent.with_json_and_owner(jsondict['event'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'klass' in jsondict:
            self.klass = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['klass'], self)
        if 'section' in jsondict:
            self.section = CompositionSection.with_json_and_owner(jsondict['section'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'title' in jsondict:
            self.title = jsondict['title']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class CompositionAttester(fhirelement.FHIRElement):
    """ Attests to accuracy of composition.
    
    A participant who has attested to the accuracy of the composition/document.
    """
    
    resource_name = "CompositionAttester"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.mode = None
        """ personal | professional | legal | official.
        List of `str` items. """
        
        self.party = None
        """ Who attested the composition.
        Type `FHIRReference` referencing `Patient, Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.time = None
        """ When composition attested.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(CompositionAttester, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CompositionAttester, self).update_with_json(jsondict)
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'party' in jsondict:
            self.party = fhirreference.FHIRReference.with_json_and_owner(jsondict['party'], self)
        if 'time' in jsondict:
            self.time = fhirdate.FHIRDate.with_json_and_owner(jsondict['time'], self)


class CompositionEvent(fhirelement.FHIRElement):
    """ The clinical service(s) being documented.
    
    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """
    
    resource_name = "CompositionEvent"
    
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
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'detail' in jsondict:
            self.detail = fhirreference.FHIRReference.with_json_and_owner(jsondict['detail'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)


class CompositionSection(fhirelement.FHIRElement):
    """ Composition is broken into sections.
    
    The root of the sections that make up the composition.
    """
    
    resource_name = "CompositionSection"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Classification of section (recommended).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ The Content of the section.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.section = None
        """ Composition is broken into sections.
        List of `CompositionSection` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Label for section (e.g. for ToC).
        Type `str`. """
        
        super(CompositionSection, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CompositionSection, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'content' in jsondict:
            self.content = fhirreference.FHIRReference.with_json_and_owner(jsondict['content'], self)
        if 'section' in jsondict:
            self.section = CompositionSection.with_json_and_owner(jsondict['section'], self)
        if 'title' in jsondict:
            self.title = jsondict['title']

