#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Composition) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period


class Composition(domainresource.DomainResource):
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
        Type `str`. """
        
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
        """ preliminary | final | appended | amended | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Who and/or what the composition is about.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.title = None
        """ Human Readable name/title.
        Type `str`. """
        
        self.type = None
        """ Kind of composition (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Composition, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Composition, self).elementProperties()
        js.extend([
            ("attester", "attester", CompositionAttester, True),
            ("author", "author", fhirreference.FHIRReference, True),
            ("confidentiality", "confidentiality", str, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("event", "event", CompositionEvent, True),
            ("identifier", "identifier", identifier.Identifier, False),
            ("klass", "class", codeableconcept.CodeableConcept, False),
            ("section", "section", CompositionSection, True),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("title", "title", str, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(CompositionAttester, self).elementProperties()
        js.extend([
            ("mode", "mode", str, True),
            ("party", "party", fhirreference.FHIRReference, False),
            ("time", "time", fhirdate.FHIRDate, False),
        ])
        return js


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
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period covered by the documentation.
        Type `Period` (represented as `dict` in JSON). """
        
        super(CompositionEvent, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(CompositionEvent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True),
            ("detail", "detail", fhirreference.FHIRReference, True),
            ("period", "period", period.Period, False),
        ])
        return js


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
        """ The Content of the section (narrative + data entries).
        Type `FHIRReference` referencing `List` (represented as `dict` in JSON). """
        
        self.section = None
        """ Nested Section.
        List of `CompositionSection` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Label for section (e.g. for ToC).
        Type `str`. """
        
        super(CompositionSection, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(CompositionSection, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("content", "content", fhirreference.FHIRReference, False),
            ("section", "section", CompositionSection, True),
            ("title", "title", str, False),
        ])
        return js

