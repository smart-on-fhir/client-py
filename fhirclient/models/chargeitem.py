# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ChargeItem).
# 2024, SMART Health IT.


from . import domainresource

class ChargeItem(domainresource.DomainResource):
    """ Item containing charge code(s) associated with the provision of healthcare
    provider products.
    
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._account = None
        """ Primitive extension for account. Type `FHIRPrimitiveExtension` """
        
        self.bodysite = None
        """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._bodysite = None
        """ Primitive extension for bodysite. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ A code that identifies the charge, like a billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.context = None
        """ Encounter / Episode associated with event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.costCenter = None
        """ Organization that has ownership of the (potential, future) revenue.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._costCenter = None
        """ Primitive extension for costCenter. Type `FHIRPrimitiveExtension` """
        
        self.definitionCanonical = None
        """ Resource defining the code of this ChargeItem.
        List of `str` items. """
        self._definitionCanonical = None
        """ Primitive extension for definitionCanonical. Type `FHIRPrimitiveExtension` """
        
        self.definitionUri = None
        """ Defining information about the code of this charge item.
        List of `str` items. """
        self._definitionUri = None
        """ Primitive extension for definitionUri. Type `FHIRPrimitiveExtension` """
        
        self.enteredDate = None
        """ Date the charge item was entered.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._enteredDate = None
        """ Primitive extension for enteredDate. Type `FHIRPrimitiveExtension` """
        
        self.enterer = None
        """ Individual who was entering.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._enterer = None
        """ Primitive extension for enterer. Type `FHIRPrimitiveExtension` """
        
        self.factorOverride = None
        """ Factor overriding the associated rules.
        Type `float`. """
        self._factorOverride = None
        """ Primitive extension for factorOverride. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments made about the ChargeItem.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceDateTime = None
        """ When the charged service was applied.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._occurrenceDateTime = None
        """ Primitive extension for occurrenceDateTime. Type `FHIRPrimitiveExtension` """
        
        self.occurrencePeriod = None
        """ When the charged service was applied.
        Type `Period` (represented as `dict` in JSON). """
        self._occurrencePeriod = None
        """ Primitive extension for occurrencePeriod. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceTiming = None
        """ When the charged service was applied.
        Type `Timing` (represented as `dict` in JSON). """
        self._occurrenceTiming = None
        """ Primitive extension for occurrenceTiming. Type `FHIRPrimitiveExtension` """
        
        self.overrideReason = None
        """ Reason for overriding the list price/factor.
        Type `str`. """
        self._overrideReason = None
        """ Primitive extension for overrideReason. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Part of referenced ChargeItem.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Who performed charged service.
        List of `ChargeItemPerformer` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.performingOrganization = None
        """ Organization providing the charged service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._performingOrganization = None
        """ Primitive extension for performingOrganization. Type `FHIRPrimitiveExtension` """
        
        self.priceOverride = None
        """ Price overriding the associated rules.
        Type `Money` (represented as `dict` in JSON). """
        self._priceOverride = None
        """ Primitive extension for priceOverride. Type `FHIRPrimitiveExtension` """
        
        self.productCodeableConcept = None
        """ Product charged.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productCodeableConcept = None
        """ Primitive extension for productCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.productReference = None
        """ Product charged.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._productReference = None
        """ Primitive extension for productReference. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Quantity of which the charge item has been serviced.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.reason = None
        """ Why was the charged  service rendered?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reason = None
        """ Primitive extension for reason. Type `FHIRPrimitiveExtension` """
        
        self.requestingOrganization = None
        """ Organization requesting the charged service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requestingOrganization = None
        """ Primitive extension for requestingOrganization. Type `FHIRPrimitiveExtension` """
        
        self.service = None
        """ Which rendered service is being charged?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._service = None
        """ Primitive extension for service. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ planned | billable | not-billable | aborted | billed | entered-in-
        error | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Individual service was done for/to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.supportingInformation = None
        """ Further information supporting this charge.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingInformation = None
        """ Primitive extension for supportingInformation. Type `FHIRPrimitiveExtension` """
        
        super(ChargeItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItem, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, True, None, False),
            ("_account", "_account", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodysite", "bodysite", codeableconcept.CodeableConcept, True, None, False),
            ("_bodysite", "_bodysite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("costCenter", "costCenter", fhirreference.FHIRReference, False, None, False),
            ("_costCenter", "_costCenter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definitionCanonical", "definitionCanonical", str, True, None, False),
            ("_definitionCanonical", "_definitionCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definitionUri", "definitionUri", str, True, None, False),
            ("_definitionUri", "_definitionUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enteredDate", "enteredDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_enteredDate", "_enteredDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("_enterer", "_enterer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factorOverride", "factorOverride", float, False, None, False),
            ("_factorOverride", "_factorOverride", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", False),
            ("_occurrenceDateTime", "_occurrenceDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("_occurrencePeriod", "_occurrencePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("_occurrenceTiming", "_occurrenceTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("overrideReason", "overrideReason", str, False, None, False),
            ("_overrideReason", "_overrideReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", ChargeItemPerformer, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performingOrganization", "performingOrganization", fhirreference.FHIRReference, False, None, False),
            ("_performingOrganization", "_performingOrganization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priceOverride", "priceOverride", money.Money, False, None, False),
            ("_priceOverride", "_priceOverride", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("_productCodeableConcept", "_productCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("_productReference", "_productReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestingOrganization", "requestingOrganization", fhirreference.FHIRReference, False, None, False),
            ("_requestingOrganization", "_requestingOrganization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("service", "service", fhirreference.FHIRReference, True, None, False),
            ("_service", "_service", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("_supportingInformation", "_supportingInformation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ChargeItemPerformer(backboneelement.BackboneElement):
    """ Who performed charged service.
    
    Indicates who or what performed or participated in the charged service.
    """
    
    resource_type = "ChargeItemPerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Individual who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.function = None
        """ What type of performance was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._function = None
        """ Primitive extension for function. Type `FHIRPrimitiveExtension` """
        
        super(ChargeItemPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("_function", "_function", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
from . import timing