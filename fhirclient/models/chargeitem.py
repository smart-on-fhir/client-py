#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.10959 (http://hl7.org/fhir/StructureDefinition/ChargeItem) on 2017-02-01.
#  2017, SMART Health IT.


from . import domainresource

class ChargeItem(domainresource.DomainResource):
    """ ChargeItem.
    """
    
    resource_type = "ChargeItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.account = None
        """ Account to place this charge.
        Type `FHIRReference` referencing `Account` (represented as `dict` in JSON). """
        
        self.bodysite = None
        """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Code of the ChargeItem.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter / Episode associated with event.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.definition = None
        """ Definition of the Charge Item.
        List of `FHIRReference` items referencing `Definition` (represented as `dict` in JSON). """
        
        self.enteredDate = None
        """ Date the charge item was entered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.enterer = None
        """ Individual who was entering.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, Device, RelatedPerson` (represented as `dict` in JSON). """
        
        self.factorOverride = None
        """ Factor overriding the associated rules.
        Type `float`. """
        
        self.identifier = None
        """ Business Identifer for item.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the ChargeItem.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When the charged service was applied.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When the charged service was applied.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ When the charged service was applied.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.overrideReason = None
        """ Reason for overriding the list price/factor.
        Type `str`. """
        
        self.partOf = None
        """ Part of referenced ChargeItem.
        List of `FHIRReference` items referencing `ChargeItem` (represented as `dict` in JSON). """
        
        self.participant = None
        """ Who performed charged service.
        List of `ChargeItemParticipant` items (represented as `dict` in JSON). """
        
        self.performingOrganization = None
        """ Organization providing the charged sevice.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.priceOverride = None
        """ Price overriding the associated rules.
        Type `Money` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Quantity of which the charge item has been serviced.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Why was the charged service rendered?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requestingOrganization = None
        """ Organization requesting the charged service.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.service = None
        """ Which rendered service is being charged?.
        List of `FHIRReference` items referencing `DiagnosticReport, ImagingStudy, Immunization, MedicationAdministration, MedicationDispense, Observation, Procedure, SupplyDelivery` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Individual service was done for/to.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Further information supporting the this charge.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(ChargeItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItem, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, False, None, False),
            ("bodysite", "bodysite", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", fhirreference.FHIRReference, True, None, False),
            ("enteredDate", "enteredDate", fhirdate.FHIRDate, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("factorOverride", "factorOverride", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("overrideReason", "overrideReason", str, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("participant", "participant", ChargeItemParticipant, True, None, False),
            ("performingOrganization", "performingOrganization", fhirreference.FHIRReference, False, None, False),
            ("priceOverride", "priceOverride", money.Money, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("requestingOrganization", "requestingOrganization", fhirreference.FHIRReference, False, None, False),
            ("service", "service", fhirreference.FHIRReference, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class ChargeItemParticipant(backboneelement.BackboneElement):
    """ Who performed charged service.
    
    Indicates who or what performed or participated in the charged service.
    """
    
    resource_type = "ChargeItemParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Individual who was performing.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, Device, RelatedPerson` (represented as `dict` in JSON). """
        
        self.role = None
        """ What type of performance was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ChargeItemParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
from . import timing
