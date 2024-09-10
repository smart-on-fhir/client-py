# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Composition).
# 2024, SMART Health IT.


from . import domainresource

class Composition(domainresource.DomainResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.
    
    A set of healthcare-related information that is assembled together into a
    single logical package that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. A Composition defines the structure
    and narrative content necessary for a document. However, a Composition
    alone does not constitute a document. Rather, the Composition must be the
    first entry in a Bundle where Bundle.type=document, and any other resources
    referenced from Composition must be included as subsequent entries in the
    Bundle (for example Patient, Practitioner, Encounter, etc.).
    """
    
    resource_type = "Composition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attester = None
        """ Attests to accuracy of composition.
        List of `CompositionAttester` items (represented as `dict` in JSON). """
        self._attester = None
        """ Primitive extension for attester. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Who and/or what authored the composition.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Categorization of Composition.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.confidentiality = None
        """ As defined by affinity domain.
        Type `str`. """
        self._confidentiality = None
        """ Primitive extension for confidentiality. Type `FHIRPrimitiveExtension` """
        
        self.custodian = None
        """ Organization which maintains the composition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._custodian = None
        """ Primitive extension for custodian. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Composition editing time.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Context of the Composition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.event = None
        """ The clinical service(s) being documented.
        List of `CompositionEvent` items (represented as `dict` in JSON). """
        self._event = None
        """ Primitive extension for event. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Version-independent identifier for the Composition.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.relatesTo = None
        """ Relationships to other compositions/documents.
        List of `CompositionRelatesTo` items (represented as `dict` in JSON). """
        self._relatesTo = None
        """ Primitive extension for relatesTo. Type `FHIRPrimitiveExtension` """
        
        self.section = None
        """ Composition is broken into sections.
        List of `CompositionSection` items (represented as `dict` in JSON). """
        self._section = None
        """ Primitive extension for section. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ preliminary | final | amended | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who and/or what the composition is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Human Readable name/title.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Kind of composition (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Composition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Composition, self).elementProperties()
        js.extend([
            ("attester", "attester", CompositionAttester, True, None, False),
            ("_attester", "_attester", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, True),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("confidentiality", "confidentiality", str, False, None, False),
            ("_confidentiality", "_confidentiality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("_custodian", "_custodian", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, True),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("event", "event", CompositionEvent, True, None, False),
            ("_event", "_event", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatesTo", "relatesTo", CompositionRelatesTo, True, None, False),
            ("_relatesTo", "_relatesTo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("_section", "_section", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, True),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class CompositionAttester(backboneelement.BackboneElement):
    """ Attests to accuracy of composition.
    
    A participant who has attested to the accuracy of the composition/document.
    """
    
    resource_type = "CompositionAttester"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode = None
        """ personal | professional | legal | official.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.party = None
        """ Who attested the composition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._party = None
        """ Primitive extension for party. Type `FHIRPrimitiveExtension` """
        
        self.time = None
        """ When the composition was attested.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._time = None
        """ Primitive extension for time. Type `FHIRPrimitiveExtension` """
        
        super(CompositionAttester, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompositionAttester, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("_party", "_party", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("time", "time", fhirdatetime.FHIRDateTime, False, None, False),
            ("_time", "_time", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CompositionEvent(backboneelement.BackboneElement):
    """ The clinical service(s) being documented.
    
    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """
    
    resource_type = "CompositionEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code(s) that apply to the event being documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ The event(s) being documented.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ The period covered by the documentation.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        super(CompositionEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompositionEvent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CompositionRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other compositions/documents.
    
    Relationships that this composition has with other compositions or
    documents that already exist.
    """
    
    resource_type = "CompositionRelatesTo"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ replaces | transforms | signs | appends.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.targetIdentifier = None
        """ Target of the relationship.
        Type `Identifier` (represented as `dict` in JSON). """
        self._targetIdentifier = None
        """ Primitive extension for targetIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.targetReference = None
        """ Target of the relationship.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._targetReference = None
        """ Primitive extension for targetReference. Type `FHIRPrimitiveExtension` """
        
        super(CompositionRelatesTo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompositionRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetIdentifier", "targetIdentifier", identifier.Identifier, False, "target", True),
            ("_targetIdentifier", "_targetIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", True),
            ("_targetReference", "_targetReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CompositionSection(backboneelement.BackboneElement):
    """ Composition is broken into sections.
    
    The root of the sections that make up the composition.
    """
    
    resource_type = "CompositionSection"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ Who and/or what authored the section.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Classification of section (recommended).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.emptyReason = None
        """ Why the section is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._emptyReason = None
        """ Primitive extension for emptyReason. Type `FHIRPrimitiveExtension` """
        
        self.entry = None
        """ A reference to data that supports this section.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._entry = None
        """ Primitive extension for entry. Type `FHIRPrimitiveExtension` """
        
        self.focus = None
        """ Who/what the section is about, when it is not about the subject of
        composition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._focus = None
        """ Primitive extension for focus. Type `FHIRPrimitiveExtension` """
        
        self.mode = None
        """ working | snapshot | changes.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.orderedBy = None
        """ Order of section entries.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._orderedBy = None
        """ Primitive extension for orderedBy. Type `FHIRPrimitiveExtension` """
        
        self.section = None
        """ Nested Section.
        List of `CompositionSection` items (represented as `dict` in JSON). """
        self._section = None
        """ Primitive extension for section. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Text summary of the section, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Label for section (e.g. for ToC).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        super(CompositionSection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompositionSection, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("_emptyReason", "_emptyReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("entry", "entry", fhirreference.FHIRReference, True, None, False),
            ("_entry", "_entry", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("_focus", "_focus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("_orderedBy", "_orderedBy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("_section", "_section", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", narrative.Narrative, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import narrative
from . import period