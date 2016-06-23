#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Composition) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Composition(domainresource.DomainResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.
    
    A set of healthcare-related information that is assembled together into a
    single logical document that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. While a Composition defines the
    structure, it does not actually contain the content: rather the full
    content of a document is contained in a Bundle, of which the Composition is
    the first resource contained.
    """
    
    resource_name = "Composition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attester = None
        """ Attests to accuracy of composition.
        List of `CompositionAttester` items (represented as `dict` in JSON). """
        
        self.author = None
        """ Who and/or what authored the composition.
        List of `FHIRReference` items referencing `Practitioner, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.class_fhir = None
        """ Categorization of Composition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.confidentiality = None
        """ As defined by affinity domain.
        Type `str`. """
        
        self.custodian = None
        """ Organization which maintains the composition.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.date = None
        """ Composition editing time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None
        """ Context of the Composition.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.event = None
        """ The clinical service(s) being documented.
        List of `CompositionEvent` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Logical identifier of composition (version-independent).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.section = None
        """ Composition is broken into sections.
        List of `CompositionSection` items (represented as `dict` in JSON). """
        
        self.status = None
        """ preliminary | final | amended | entered-in-error.
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
        
        super(Composition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Composition, self).elementProperties()
        js.extend([
            ("attester", "attester", CompositionAttester, True, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, True),
            ("class_fhir", "class", codeableconcept.CodeableConcept, False, None, False),
            ("confidentiality", "confidentiality", str, False, None, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("event", "event", CompositionEvent, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("title", "title", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import backboneelement

class CompositionAttester(backboneelement.BackboneElement):
    """ Attests to accuracy of composition.
    
    A participant who has attested to the accuracy of the composition/document.
    """
    
    resource_name = "CompositionAttester"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(CompositionAttester, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompositionAttester, self).elementProperties()
        js.extend([
            ("mode", "mode", str, True, None, True),
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class CompositionEvent(backboneelement.BackboneElement):
    """ The clinical service(s) being documented.
    
    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """
    
    resource_name = "CompositionEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code(s) that apply to the event being documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ The event(s) being documented.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period covered by the documentation.
        Type `Period` (represented as `dict` in JSON). """
        
        super(CompositionEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompositionEvent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


class CompositionSection(backboneelement.BackboneElement):
    """ Composition is broken into sections.
    
    The root of the sections that make up the composition.
    """
    
    resource_name = "CompositionSection"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Classification of section (recommended).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.emptyReason = None
        """ Why the section is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.entry = None
        """ A reference to data that supports this section.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.mode = None
        """ working | snapshot | changes.
        Type `str`. """
        
        self.orderedBy = None
        """ Order of section entries.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.section = None
        """ Nested Section.
        List of `CompositionSection` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the section, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.title = None
        """ Label for section (e.g. for ToC).
        Type `str`. """
        
        super(CompositionSection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompositionSection, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("entry", "entry", fhirreference.FHIRReference, True, None, False),
            ("mode", "mode", str, False, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("text", "text", narrative.Narrative, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import narrative
from . import period
