# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit).
# 2024, SMART Health IT.


from . import domainresource

class ExplanationOfBenefit(domainresource.DomainResource):
    """ Explanation of Benefit resource.
    
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    
    resource_type = "ExplanationOfBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident = None
        """ Details of the event.
        Type `ExplanationOfBenefitAccident` (represented as `dict` in JSON). """
        self._accident = None
        """ Primitive extension for accident. Type `FHIRPrimitiveExtension` """
        
        self.addItem = None
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItem` items (represented as `dict` in JSON). """
        self._addItem = None
        """ Primitive extension for addItem. Type `FHIRPrimitiveExtension` """
        
        self.adjudication = None
        """ Header-level adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.benefitBalance = None
        """ Balance by Benefit Category.
        List of `ExplanationOfBenefitBenefitBalance` items (represented as `dict` in JSON). """
        self._benefitBalance = None
        """ Primitive extension for benefitBalance. Type `FHIRPrimitiveExtension` """
        
        self.benefitPeriod = None
        """ When the benefits are applicable.
        Type `Period` (represented as `dict` in JSON). """
        self._benefitPeriod = None
        """ Primitive extension for benefitPeriod. Type `FHIRPrimitiveExtension` """
        
        self.billablePeriod = None
        """ Relevant time frame for the claim.
        Type `Period` (represented as `dict` in JSON). """
        self._billablePeriod = None
        """ Primitive extension for billablePeriod. Type `FHIRPrimitiveExtension` """
        
        self.careTeam = None
        """ Care Team members.
        List of `ExplanationOfBenefitCareTeam` items (represented as `dict` in JSON). """
        self._careTeam = None
        """ Primitive extension for careTeam. Type `FHIRPrimitiveExtension` """
        
        self.claim = None
        """ Claim reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._claim = None
        """ Primitive extension for claim. Type `FHIRPrimitiveExtension` """
        
        self.claimResponse = None
        """ Claim response reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._claimResponse = None
        """ Primitive extension for claimResponse. Type `FHIRPrimitiveExtension` """
        
        self.created = None
        """ Response creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.diagnosis = None
        """ Pertinent diagnosis information.
        List of `ExplanationOfBenefitDiagnosis` items (represented as `dict` in JSON). """
        self._diagnosis = None
        """ Primitive extension for diagnosis. Type `FHIRPrimitiveExtension` """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        self._disposition = None
        """ Primitive extension for disposition. Type `FHIRPrimitiveExtension` """
        
        self.enterer = None
        """ Author of the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._enterer = None
        """ Primitive extension for enterer. Type `FHIRPrimitiveExtension` """
        
        self.facility = None
        """ Servicing Facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._facility = None
        """ Primitive extension for facility. Type `FHIRPrimitiveExtension` """
        
        self.form = None
        """ Printed reference or actual form.
        Type `Attachment` (represented as `dict` in JSON). """
        self._form = None
        """ Primitive extension for form. Type `FHIRPrimitiveExtension` """
        
        self.formCode = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._formCode = None
        """ Primitive extension for formCode. Type `FHIRPrimitiveExtension` """
        
        self.fundsReserve = None
        """ Funds reserved status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._fundsReserve = None
        """ Primitive extension for fundsReserve. Type `FHIRPrimitiveExtension` """
        
        self.fundsReserveRequested = None
        """ For whom to reserve funds.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._fundsReserveRequested = None
        """ Primitive extension for fundsReserveRequested. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for the resource.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.insurance = None
        """ Patient insurance information.
        List of `ExplanationOfBenefitInsurance` items (represented as `dict` in JSON). """
        self._insurance = None
        """ Primitive extension for insurance. Type `FHIRPrimitiveExtension` """
        
        self.insurer = None
        """ Party responsible for reimbursement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._insurer = None
        """ Primitive extension for insurer. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Product or service provided.
        List of `ExplanationOfBenefitItem` items (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        self.originalPrescription = None
        """ Original prescription if superceded by fulfiller.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._originalPrescription = None
        """ Primitive extension for originalPrescription. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ queued | complete | error | partial.
        Type `str`. """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ The recipient of the products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.payee = None
        """ Recipient of benefits payable.
        Type `ExplanationOfBenefitPayee` (represented as `dict` in JSON). """
        self._payee = None
        """ Primitive extension for payee. Type `FHIRPrimitiveExtension` """
        
        self.payment = None
        """ Payment Details.
        Type `ExplanationOfBenefitPayment` (represented as `dict` in JSON). """
        self._payment = None
        """ Primitive extension for payment. Type `FHIRPrimitiveExtension` """
        
        self.preAuthRef = None
        """ Preauthorization reference.
        List of `str` items. """
        self._preAuthRef = None
        """ Primitive extension for preAuthRef. Type `FHIRPrimitiveExtension` """
        
        self.preAuthRefPeriod = None
        """ Preauthorization in-effect period.
        List of `Period` items (represented as `dict` in JSON). """
        self._preAuthRefPeriod = None
        """ Primitive extension for preAuthRefPeriod. Type `FHIRPrimitiveExtension` """
        
        self.precedence = None
        """ Precedence (primary, secondary, etc.).
        Type `int`. """
        self._precedence = None
        """ Primitive extension for precedence. Type `FHIRPrimitiveExtension` """
        
        self.prescription = None
        """ Prescription authorizing services or products.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._prescription = None
        """ Primitive extension for prescription. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ Desired processing urgency.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.procedure = None
        """ Clinical procedures performed.
        List of `ExplanationOfBenefitProcedure` items (represented as `dict` in JSON). """
        self._procedure = None
        """ Primitive extension for procedure. Type `FHIRPrimitiveExtension` """
        
        self.processNote = None
        """ Note concerning adjudication.
        List of `ExplanationOfBenefitProcessNote` items (represented as `dict` in JSON). """
        self._processNote = None
        """ Primitive extension for processNote. Type `FHIRPrimitiveExtension` """
        
        self.provider = None
        """ Party responsible for the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._provider = None
        """ Primitive extension for provider. Type `FHIRPrimitiveExtension` """
        
        self.referral = None
        """ Treatment Referral.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._referral = None
        """ Primitive extension for referral. Type `FHIRPrimitiveExtension` """
        
        self.related = None
        """ Prior or corollary claims.
        List of `ExplanationOfBenefitRelated` items (represented as `dict` in JSON). """
        self._related = None
        """ Primitive extension for related. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subType = None
        """ More granular claim type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._subType = None
        """ Primitive extension for subType. Type `FHIRPrimitiveExtension` """
        
        self.supportingInfo = None
        """ Supporting information.
        List of `ExplanationOfBenefitSupportingInfo` items (represented as `dict` in JSON). """
        self._supportingInfo = None
        """ Primitive extension for supportingInfo. Type `FHIRPrimitiveExtension` """
        
        self.total = None
        """ Adjudication totals.
        List of `ExplanationOfBenefitTotal` items (represented as `dict` in JSON). """
        self._total = None
        """ Primitive extension for total. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Category or discipline.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ claim | preauthorization | predetermination.
        Type `str`. """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("accident", "accident", ExplanationOfBenefitAccident, False, None, False),
            ("_accident", "_accident", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("addItem", "addItem", ExplanationOfBenefitAddItem, True, None, False),
            ("_addItem", "_addItem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("benefitBalance", "benefitBalance", ExplanationOfBenefitBenefitBalance, True, None, False),
            ("_benefitBalance", "_benefitBalance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("benefitPeriod", "benefitPeriod", period.Period, False, None, False),
            ("_benefitPeriod", "_benefitPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("_billablePeriod", "_billablePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("careTeam", "careTeam", ExplanationOfBenefitCareTeam, True, None, False),
            ("_careTeam", "_careTeam", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("_claim", "_claim", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("_claimResponse", "_claimResponse", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("diagnosis", "diagnosis", ExplanationOfBenefitDiagnosis, True, None, False),
            ("_diagnosis", "_diagnosis", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("_enterer", "_enterer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("_facility", "_facility", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("form", "form", attachment.Attachment, False, None, False),
            ("_form", "_form", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("_formCode", "_formCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("_fundsReserve", "_fundsReserve", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fundsReserveRequested", "fundsReserveRequested", codeableconcept.CodeableConcept, False, None, False),
            ("_fundsReserveRequested", "_fundsReserveRequested", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurance", "insurance", ExplanationOfBenefitInsurance, True, None, True),
            ("_insurance", "_insurance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("_insurer", "_insurer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("_originalPrescription", "_originalPrescription", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payee", "payee", ExplanationOfBenefitPayee, False, None, False),
            ("_payee", "_payee", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payment", "payment", ExplanationOfBenefitPayment, False, None, False),
            ("_payment", "_payment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("_preAuthRef", "_preAuthRef", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preAuthRefPeriod", "preAuthRefPeriod", period.Period, True, None, False),
            ("_preAuthRefPeriod", "_preAuthRefPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("precedence", "precedence", int, False, None, False),
            ("_precedence", "_precedence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("_prescription", "_prescription", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("procedure", "procedure", ExplanationOfBenefitProcedure, True, None, False),
            ("_procedure", "_procedure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("processNote", "processNote", ExplanationOfBenefitProcessNote, True, None, False),
            ("_processNote", "_processNote", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("_provider", "_provider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("_referral", "_referral", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("related", "related", ExplanationOfBenefitRelated, True, None, False),
            ("_related", "_related", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("_subType", "_subType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInfo", "supportingInfo", ExplanationOfBenefitSupportingInfo, True, None, False),
            ("_supportingInfo", "_supportingInfo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("total", "total", ExplanationOfBenefitTotal, True, None, False),
            ("_total", "_total", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", str, False, None, True),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """ Details of the event.
    
    Details of a accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    
    resource_type = "ExplanationOfBenefitAccident"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the incident occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.locationAddress = None
        """ Where the event occurred.
        Type `Address` (represented as `dict` in JSON). """
        self._locationAddress = None
        """ Primitive extension for locationAddress. Type `FHIRPrimitiveExtension` """
        
        self.locationReference = None
        """ Where the event occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._locationReference = None
        """ Primitive extension for locationReference. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The nature of the accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitAccident, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("_locationAddress", "_locationAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("_locationReference", "_locationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The first-tier service adjudications for payor added product or service
    lines.
    """
    
    resource_type = "ExplanationOfBenefitAddItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.bodySite = None
        """ Anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItemDetail` items (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.detailSequence = None
        """ Detail sequence number.
        List of `int` items. """
        self._detailSequence = None
        """ Primitive extension for detailSequence. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.itemSequence = None
        """ Item sequence number.
        List of `int` items. """
        self._itemSequence = None
        """ Primitive extension for itemSequence. Type `FHIRPrimitiveExtension` """
        
        self.locationAddress = None
        """ Place of service or where product was supplied.
        Type `Address` (represented as `dict` in JSON). """
        self._locationAddress = None
        """ Primitive extension for locationAddress. Type `FHIRPrimitiveExtension` """
        
        self.locationCodeableConcept = None
        """ Place of service or where product was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._locationCodeableConcept = None
        """ Primitive extension for locationCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.locationReference = None
        """ Place of service or where product was supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._locationReference = None
        """ Primitive extension for locationReference. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        self._net = None
        """ Primitive extension for net. Type `FHIRPrimitiveExtension` """
        
        self.noteNumber = None
        """ Applicable note numbers.
        List of `int` items. """
        self._noteNumber = None
        """ Primitive extension for noteNumber. Type `FHIRPrimitiveExtension` """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productOrService = None
        """ Primitive extension for productOrService. Type `FHIRPrimitiveExtension` """
        
        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._programCode = None
        """ Primitive extension for programCode. Type `FHIRPrimitiveExtension` """
        
        self.provider = None
        """ Authorized providers.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._provider = None
        """ Primitive extension for provider. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.servicedDate = None
        """ Date or dates of service or product delivery.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._servicedDate = None
        """ Primitive extension for servicedDate. Type `FHIRPrimitiveExtension` """
        
        self.servicedPeriod = None
        """ Date or dates of service or product delivery.
        Type `Period` (represented as `dict` in JSON). """
        self._servicedPeriod = None
        """ Primitive extension for servicedPeriod. Type `FHIRPrimitiveExtension` """
        
        self.subDetailSequence = None
        """ Subdetail sequence number.
        List of `int` items. """
        self._subDetailSequence = None
        """ Primitive extension for subDetailSequence. Type `FHIRPrimitiveExtension` """
        
        self.subSite = None
        """ Anatomical sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._subSite = None
        """ Primitive extension for subSite. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitAddItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", ExplanationOfBenefitAddItemDetail, True, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailSequence", "detailSequence", int, True, None, False),
            ("_detailSequence", "_detailSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemSequence", "itemSequence", int, True, None, False),
            ("_itemSequence", "_itemSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("_locationAddress", "_locationAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("_locationCodeableConcept", "_locationCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("_locationReference", "_locationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("_net", "_net", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("_productOrService", "_productOrService", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("_programCode", "_programCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, True, None, False),
            ("_provider", "_provider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("_servicedDate", "_servicedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("_servicedPeriod", "_servicedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subDetailSequence", "subDetailSequence", int, True, None, False),
            ("_subDetailSequence", "_subDetailSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("_subSite", "_subSite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The second-tier service adjudications for payor added services.
    """
    
    resource_type = "ExplanationOfBenefitAddItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        self._net = None
        """ Primitive extension for net. Type `FHIRPrimitiveExtension` """
        
        self.noteNumber = None
        """ Applicable note numbers.
        List of `int` items. """
        self._noteNumber = None
        """ Primitive extension for noteNumber. Type `FHIRPrimitiveExtension` """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productOrService = None
        """ Primitive extension for productOrService. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.subDetail = None
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItemDetailSubDetail` items (represented as `dict` in JSON). """
        self._subDetail = None
        """ Primitive extension for subDetail. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitAddItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("_net", "_net", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("_productOrService", "_productOrService", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subDetail", "subDetail", ExplanationOfBenefitAddItemDetailSubDetail, True, None, False),
            ("_subDetail", "_subDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The third-tier service adjudications for payor added services.
    """
    
    resource_type = "ExplanationOfBenefitAddItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        self._net = None
        """ Primitive extension for net. Type `FHIRPrimitiveExtension` """
        
        self.noteNumber = None
        """ Applicable note numbers.
        List of `int` items. """
        self._noteNumber = None
        """ Primitive extension for noteNumber. Type `FHIRPrimitiveExtension` """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productOrService = None
        """ Primitive extension for productOrService. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitAddItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("_net", "_net", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("_productOrService", "_productOrService", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """ Balance by Benefit Category.
    """
    
    resource_type = "ExplanationOfBenefitBenefitBalance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Description of the benefit or services covered.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.excluded = None
        """ Excluded from the plan.
        Type `bool`. """
        self._excluded = None
        """ Primitive extension for excluded. Type `FHIRPrimitiveExtension` """
        
        self.financial = None
        """ Benefit Summary.
        List of `ExplanationOfBenefitBenefitBalanceFinancial` items (represented as `dict` in JSON). """
        self._financial = None
        """ Primitive extension for financial. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Short name for the benefit.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.network = None
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._network = None
        """ Primitive extension for network. Type `FHIRPrimitiveExtension` """
        
        self.term = None
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._term = None
        """ Primitive extension for term. Type `FHIRPrimitiveExtension` """
        
        self.unit = None
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._unit = None
        """ Primitive extension for unit. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitBenefitBalance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("_excluded", "_excluded", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("financial", "financial", ExplanationOfBenefitBenefitBalanceFinancial, True, None, False),
            ("_financial", "_financial", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("_network", "_network", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("_term", "_term", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
            ("_unit", "_unit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits Used to date.
    """
    
    resource_type = "ExplanationOfBenefitBenefitBalanceFinancial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedMoney = None
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """
        self._allowedMoney = None
        """ Primitive extension for allowedMoney. Type `FHIRPrimitiveExtension` """
        
        self.allowedString = None
        """ Benefits allowed.
        Type `str`. """
        self._allowedString = None
        """ Primitive extension for allowedString. Type `FHIRPrimitiveExtension` """
        
        self.allowedUnsignedInt = None
        """ Benefits allowed.
        Type `int`. """
        self._allowedUnsignedInt = None
        """ Primitive extension for allowedUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.usedMoney = None
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """
        self._usedMoney = None
        """ Primitive extension for usedMoney. Type `FHIRPrimitiveExtension` """
        
        self.usedUnsignedInt = None
        """ Benefits used.
        Type `int`. """
        self._usedUnsignedInt = None
        """ Primitive extension for usedUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitBenefitBalanceFinancial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False),
            ("_allowedMoney", "_allowedMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("_allowedString", "_allowedString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("_allowedUnsignedInt", "_allowedUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usedMoney", "usedMoney", money.Money, False, "used", False),
            ("_usedMoney", "_usedMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
            ("_usedUnsignedInt", "_usedUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitCareTeam(backboneelement.BackboneElement):
    """ Care Team members.
    
    The members of the team who provided the products and services.
    """
    
    resource_type = "ExplanationOfBenefitCareTeam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.provider = None
        """ Practitioner or organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._provider = None
        """ Primitive extension for provider. Type `FHIRPrimitiveExtension` """
        
        self.qualification = None
        """ Practitioner credential or specialization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._qualification = None
        """ Primitive extension for qualification. Type `FHIRPrimitiveExtension` """
        
        self.responsible = None
        """ Indicator of the lead practitioner.
        Type `bool`. """
        self._responsible = None
        """ Primitive extension for responsible. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ Function within the team.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Order of care team.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitCareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("_provider", "_provider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("qualification", "qualification", codeableconcept.CodeableConcept, False, None, False),
            ("_qualification", "_qualification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("_responsible", "_responsible", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.
    
    Information about diagnoses relevant to the claim items.
    """
    
    resource_type = "ExplanationOfBenefitDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosisCodeableConcept = None
        """ Nature of illness or problem.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._diagnosisCodeableConcept = None
        """ Primitive extension for diagnosisCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.diagnosisReference = None
        """ Nature of illness or problem.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._diagnosisReference = None
        """ Primitive extension for diagnosisReference. Type `FHIRPrimitiveExtension` """
        
        self.onAdmission = None
        """ Present on admission.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._onAdmission = None
        """ Primitive extension for onAdmission. Type `FHIRPrimitiveExtension` """
        
        self.packageCode = None
        """ Package billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._packageCode = None
        """ Primitive extension for packageCode. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Diagnosis instance identifier.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Timing or nature of the diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", True),
            ("_diagnosisCodeableConcept", "_diagnosisCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", True),
            ("_diagnosisReference", "_diagnosisReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("_onAdmission", "_onAdmission", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, False, None, False),
            ("_packageCode", "_packageCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    
    resource_type = "ExplanationOfBenefitInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._coverage = None
        """ Primitive extension for coverage. Type `FHIRPrimitiveExtension` """
        
        self.focal = None
        """ Coverage to be used for adjudication.
        Type `bool`. """
        self._focal = None
        """ Primitive extension for focal. Type `FHIRPrimitiveExtension` """
        
        self.preAuthRef = None
        """ Prior authorization reference number.
        List of `str` items. """
        self._preAuthRef = None
        """ Primitive extension for preAuthRef. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitInsurance, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("_coverage", "_coverage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focal", "focal", bool, False, None, True),
            ("_focal", "_focal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("_preAuthRef", "_preAuthRef", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    
    resource_type = "ExplanationOfBenefitItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.bodySite = None
        """ Anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.careTeamSequence = None
        """ Applicable care team members.
        List of `int` items. """
        self._careTeamSequence = None
        """ Primitive extension for careTeamSequence. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Additional items.
        List of `ExplanationOfBenefitItemDetail` items (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.diagnosisSequence = None
        """ Applicable diagnoses.
        List of `int` items. """
        self._diagnosisSequence = None
        """ Primitive extension for diagnosisSequence. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounters related to this billed item.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.informationSequence = None
        """ Applicable exception and supporting information.
        List of `int` items. """
        self._informationSequence = None
        """ Primitive extension for informationSequence. Type `FHIRPrimitiveExtension` """
        
        self.locationAddress = None
        """ Place of service or where product was supplied.
        Type `Address` (represented as `dict` in JSON). """
        self._locationAddress = None
        """ Primitive extension for locationAddress. Type `FHIRPrimitiveExtension` """
        
        self.locationCodeableConcept = None
        """ Place of service or where product was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._locationCodeableConcept = None
        """ Primitive extension for locationCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.locationReference = None
        """ Place of service or where product was supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._locationReference = None
        """ Primitive extension for locationReference. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        self._net = None
        """ Primitive extension for net. Type `FHIRPrimitiveExtension` """
        
        self.noteNumber = None
        """ Applicable note numbers.
        List of `int` items. """
        self._noteNumber = None
        """ Primitive extension for noteNumber. Type `FHIRPrimitiveExtension` """
        
        self.procedureSequence = None
        """ Applicable procedures.
        List of `int` items. """
        self._procedureSequence = None
        """ Primitive extension for procedureSequence. Type `FHIRPrimitiveExtension` """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productOrService = None
        """ Primitive extension for productOrService. Type `FHIRPrimitiveExtension` """
        
        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._programCode = None
        """ Primitive extension for programCode. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._revenue = None
        """ Primitive extension for revenue. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Item instance identifier.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        self.servicedDate = None
        """ Date or dates of service or product delivery.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._servicedDate = None
        """ Primitive extension for servicedDate. Type `FHIRPrimitiveExtension` """
        
        self.servicedPeriod = None
        """ Date or dates of service or product delivery.
        Type `Period` (represented as `dict` in JSON). """
        self._servicedPeriod = None
        """ Primitive extension for servicedPeriod. Type `FHIRPrimitiveExtension` """
        
        self.subSite = None
        """ Anatomical sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._subSite = None
        """ Primitive extension for subSite. Type `FHIRPrimitiveExtension` """
        
        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._udi = None
        """ Primitive extension for udi. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("_careTeamSequence", "_careTeamSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", ExplanationOfBenefitItemDetail, True, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("_diagnosisSequence", "_diagnosisSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("_informationSequence", "_informationSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("_locationAddress", "_locationAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("_locationCodeableConcept", "_locationCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("_locationReference", "_locationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("_net", "_net", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("procedureSequence", "procedureSequence", int, True, None, False),
            ("_procedureSequence", "_procedureSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("_productOrService", "_productOrService", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("_programCode", "_programCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("_revenue", "_revenue", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("_servicedDate", "_servicedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("_servicedPeriod", "_servicedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("_subSite", "_subSite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("_udi", "_udi", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    
    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    
    resource_type = "ExplanationOfBenefitItemAdjudication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Money` (represented as `dict` in JSON). """
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Type of adjudication information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.reason = None
        """ Explanation of adjudication outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._reason = None
        """ Primitive extension for reason. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ Non-monitary value.
        Type `float`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitItemAdjudication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", float, False, None, False),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second-tier of goods and services.
    """
    
    resource_type = "ExplanationOfBenefitItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Detail level adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        self._net = None
        """ Primitive extension for net. Type `FHIRPrimitiveExtension` """
        
        self.noteNumber = None
        """ Applicable note numbers.
        List of `int` items. """
        self._noteNumber = None
        """ Primitive extension for noteNumber. Type `FHIRPrimitiveExtension` """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productOrService = None
        """ Primitive extension for productOrService. Type `FHIRPrimitiveExtension` """
        
        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._programCode = None
        """ Primitive extension for programCode. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._revenue = None
        """ Primitive extension for revenue. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Product or service provided.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        self.subDetail = None
        """ Additional items.
        List of `ExplanationOfBenefitItemDetailSubDetail` items (represented as `dict` in JSON). """
        self._subDetail = None
        """ Primitive extension for subDetail. Type `FHIRPrimitiveExtension` """
        
        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._udi = None
        """ Primitive extension for udi. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("_net", "_net", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("_productOrService", "_productOrService", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("_programCode", "_programCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("_revenue", "_revenue", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subDetail", "subDetail", ExplanationOfBenefitItemDetailSubDetail, True, None, False),
            ("_subDetail", "_subDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("_udi", "_udi", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third-tier of goods and services.
    """
    
    resource_type = "ExplanationOfBenefitItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Subdetail level adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        self._net = None
        """ Primitive extension for net. Type `FHIRPrimitiveExtension` """
        
        self.noteNumber = None
        """ Applicable note numbers.
        List of `int` items. """
        self._noteNumber = None
        """ Primitive extension for noteNumber. Type `FHIRPrimitiveExtension` """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productOrService = None
        """ Primitive extension for productOrService. Type `FHIRPrimitiveExtension` """
        
        self.programCode = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._programCode = None
        """ Primitive extension for programCode. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._revenue = None
        """ Primitive extension for revenue. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Product or service provided.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._udi = None
        """ Primitive extension for udi. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("_net", "_net", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("_productOrService", "_productOrService", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("_programCode", "_programCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("_revenue", "_revenue", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("_udi", "_udi", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.
    
    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    
    resource_type = "ExplanationOfBenefitPayee"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party = None
        """ Recipient reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._party = None
        """ Primitive extension for party. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Category of recipient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitPayee, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("_party", "_party", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """ Payment Details.
    
    Payment details for the adjudication of the claim.
    """
    
    resource_type = "ExplanationOfBenefitPayment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjustment = None
        """ Payment adjustment for non-claim issues.
        Type `Money` (represented as `dict` in JSON). """
        self._adjustment = None
        """ Primitive extension for adjustment. Type `FHIRPrimitiveExtension` """
        
        self.adjustmentReason = None
        """ Explanation for the variance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._adjustmentReason = None
        """ Primitive extension for adjustmentReason. Type `FHIRPrimitiveExtension` """
        
        self.amount = None
        """ Payable amount after adjustment.
        Type `Money` (represented as `dict` in JSON). """
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Expected date of payment.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier for the payment.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Partial or complete payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitPayment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitPayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("_adjustment", "_adjustment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, False, None, False),
            ("_adjustmentReason", "_adjustmentReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amount", "amount", money.Money, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.
    
    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    
    resource_type = "ExplanationOfBenefitProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the procedure was performed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.procedureCodeableConcept = None
        """ Specific clinical procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._procedureCodeableConcept = None
        """ Primitive extension for procedureCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.procedureReference = None
        """ Specific clinical procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._procedureReference = None
        """ Primitive extension for procedureReference. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Procedure instance identifier.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Category of Procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.udi = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._udi = None
        """ Primitive extension for udi. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, False, "procedure", True),
            ("_procedureCodeableConcept", "_procedureCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("_procedureReference", "_procedureReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("_udi", "_udi", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitProcessNote(backboneelement.BackboneElement):
    """ Note concerning adjudication.
    
    A note that describes or explains adjudication results in a human readable
    form.
    """
    
    resource_type = "ExplanationOfBenefitProcessNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ Language of the text.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        self.number = None
        """ Note instance identifier.
        Type `int`. """
        self._number = None
        """ Primitive extension for number. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Note explanatory text.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ display | print | printoper.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("number", "number", int, False, None, False),
            ("_number", "_number", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.
    
    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    
    resource_type = "ExplanationOfBenefitRelated"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.claim = None
        """ Reference to the related claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._claim = None
        """ Primitive extension for claim. Type `FHIRPrimitiveExtension` """
        
        self.reference = None
        """ File or case reference.
        Type `Identifier` (represented as `dict` in JSON). """
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        self.relationship = None
        """ How the reference claim is related.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._relationship = None
        """ Primitive extension for relationship. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("_claim", "_claim", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    
    resource_type = "ExplanationOfBenefitSupportingInfo"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Classification of the supplied information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Type of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.reason = None
        """ Explanation for the information.
        Type `Coding` (represented as `dict` in JSON). """
        self._reason = None
        """ Primitive extension for reason. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Information instance identifier.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        self.timingDate = None
        """ When it occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._timingDate = None
        """ Primitive extension for timingDate. Type `FHIRPrimitiveExtension` """
        
        self.timingPeriod = None
        """ When it occurred.
        Type `Period` (represented as `dict` in JSON). """
        self._timingPeriod = None
        """ Primitive extension for timingPeriod. Type `FHIRPrimitiveExtension` """
        
        self.valueAttachment = None
        """ Data to be provided.
        Type `Attachment` (represented as `dict` in JSON). """
        self._valueAttachment = None
        """ Primitive extension for valueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Data to be provided.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Data to be provided.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ Data to be provided.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Data to be provided.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", coding.Coding, False, None, False),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("_timingDate", "_timingDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("_timingPeriod", "_timingPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("_valueAttachment", "_valueAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("_valueReference", "_valueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ExplanationOfBenefitTotal(backboneelement.BackboneElement):
    """ Adjudication totals.
    
    Categorized monetary totals for the adjudication.
    """
    
    resource_type = "ExplanationOfBenefitTotal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Financial total for the category.
        Type `Money` (represented as `dict` in JSON). """
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Type of adjudication information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        super(ExplanationOfBenefitTotal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity