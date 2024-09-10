# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/List).
# 2024, SMART Health IT.


from . import domainresource

class List(domainresource.DomainResource):
    """ A list is a curated collection of resources.
    """
    
    resource_type = "List"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ What the purpose of this list is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ When the list was prepared.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.emptyReason = None
        """ Why list is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._emptyReason = None
        """ Primitive extension for emptyReason. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Context in which list created.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.entry = None
        """ Entries in the list.
        List of `ListEntry` items (represented as `dict` in JSON). """
        self._entry = None
        """ Primitive extension for entry. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.mode = None
        """ working | snapshot | changes.
        Type `str`. """
        self._mode = None
        """ Primitive extension for mode. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments about the list.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.orderedBy = None
        """ What order the list has.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._orderedBy = None
        """ Primitive extension for orderedBy. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Who and/or what defined the list contents (aka Author).
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ current | retired | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ If all resources have the same subject.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Descriptive name for the list.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        super(List, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("_emptyReason", "_emptyReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("entry", "entry", ListEntry, True, None, False),
            ("_entry", "_entry", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("_mode", "_mode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("_orderedBy", "_orderedBy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ListEntry(backboneelement.BackboneElement):
    """ Entries in the list.
    
    Entries in this list.
    """
    
    resource_type = "ListEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When item added to list.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.deleted = None
        """ If this item is actually marked as deleted.
        Type `bool`. """
        self._deleted = None
        """ Primitive extension for deleted. Type `FHIRPrimitiveExtension` """
        
        self.flag = None
        """ Status/Workflow information about this item.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._flag = None
        """ Primitive extension for flag. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Actual entry.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        super(ListEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deleted", "deleted", bool, False, None, False),
            ("_deleted", "_deleted", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("flag", "flag", codeableconcept.CodeableConcept, False, None, False),
            ("_flag", "_flag", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", fhirreference.FHIRReference, False, None, True),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier