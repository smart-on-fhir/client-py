# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationStatement).
# 2024, SMART Health IT.


from . import domainresource

class MedicationStatement(domainresource.DomainResource):
    """ Record of medication being taken by a patient.
    
    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now or has taken the medication in the past or will be taking
    the medication in the future.  The source of this information can be the
    patient, significant other (such as a family member or spouse), or a
    clinician.  A common scenario where this information is captured is during
    the history taking process during a patient visit or stay.   The medication
    information may come from sources such as the patient's memory, from a
    prescription bottle,  or from a list of medications the patient, clinician
    or other party maintains.
    
    The primary difference between a medication statement and a medication
    administration is that the medication administration has complete
    administration information and is based on actual administration
    information from the person who administered the medication.  A medication
    statement is often, if not always, less specific.  There is no required
    date/time when the medication was administered, in fact we only know that a
    source has reported the patient is taking this medication, where details
    such as time, quantity, or rate or even medication product may be
    incomplete or missing or less precise.  As stated earlier, the medication
    statement information may come from the patient's memory, from a
    prescription bottle or from a list of medications the patient, clinician or
    other party maintains.  Medication administration is more formal and is not
    missing detailed information.
    """
    
    resource_type = "MedicationStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ Fulfils plan, proposal or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Type of medication usage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.context = None
        """ Encounter / Episode associated with MedicationStatement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.dateAsserted = None
        """ When the statement was asserted?.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._dateAsserted = None
        """ Primitive extension for dateAsserted. Type `FHIRPrimitiveExtension` """
        
        self.derivedFrom = None
        """ Additional supporting information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._derivedFrom = None
        """ Primitive extension for derivedFrom. Type `FHIRPrimitiveExtension` """
        
        self.dosage = None
        """ Details of how medication is/was taken or should be taken.
        List of `Dosage` items (represented as `dict` in JSON). """
        self._dosage = None
        """ Primitive extension for dosage. Type `FHIRPrimitiveExtension` """
        
        self.effectiveDateTime = None
        """ The date/time or interval when the medication is/was/will be taken.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._effectiveDateTime = None
        """ Primitive extension for effectiveDateTime. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ The date/time or interval when the medication is/was/will be taken.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.informationSource = None
        """ Person or organization that provided the information about the
        taking of this medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._informationSource = None
        """ Primitive extension for informationSource. Type `FHIRPrimitiveExtension` """
        
        self.medicationCodeableConcept = None
        """ What medication was taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._medicationCodeableConcept = None
        """ Primitive extension for medicationCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.medicationReference = None
        """ What medication was taken.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._medicationReference = None
        """ Primitive extension for medicationReference. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Further information about the statement.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Reason for why the medication is being/was taken.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Condition or observation that supports why the medication is
        being/was taken.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | completed | entered-in-error | intended | stopped | on-
        hold | unknown | not-taken.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ Reason for current status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who is/was taking  the medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        super(MedicationStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationStatement, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dateAsserted", "dateAsserted", fhirdatetime.FHIRDateTime, False, None, False),
            ("_dateAsserted", "_dateAsserted", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("_derivedFrom", "_derivedFrom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dosage", "dosage", dosage.Dosage, True, None, False),
            ("_dosage", "_dosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdatetime.FHIRDateTime, False, "effective", False),
            ("_effectiveDateTime", "_effectiveDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("informationSource", "informationSource", fhirreference.FHIRReference, False, None, False),
            ("_informationSource", "_informationSource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("_medicationCodeableConcept", "_medicationCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("_medicationReference", "_medicationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import dosage
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period