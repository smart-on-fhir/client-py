# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ClaimResponse).
# 2024, SMART Health IT.


from . import domainresource

class ClaimResponse(domainresource.DomainResource):
    """ Response to a claim predetermination or preauthorization.
    
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    
    resource_type = "ClaimResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.addItem = None
        """ Insurer added line items.
        List of `ClaimResponseAddItem` items (represented as `dict` in JSON). """
        self._addItem = None
        """ Primitive extension for addItem. Type `FHIRPrimitiveExtension` """
        
        self.adjudication = None
        """ Header-level adjudication.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.communicationRequest = None
        """ Request for additional information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._communicationRequest = None
        """ Primitive extension for communicationRequest. Type `FHIRPrimitiveExtension` """
        
        self.created = None
        """ Response creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        self._disposition = None
        """ Primitive extension for disposition. Type `FHIRPrimitiveExtension` """
        
        self.error = None
        """ Processing errors.
        List of `ClaimResponseError` items (represented as `dict` in JSON). """
        self._error = None
        """ Primitive extension for error. Type `FHIRPrimitiveExtension` """
        
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
        
        self.identifier = None
        """ Business Identifier for a claim response.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.insurance = None
        """ Patient insurance information.
        List of `ClaimResponseInsurance` items (represented as `dict` in JSON). """
        self._insurance = None
        """ Primitive extension for insurance. Type `FHIRPrimitiveExtension` """
        
        self.insurer = None
        """ Party responsible for reimbursement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._insurer = None
        """ Primitive extension for insurer. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Adjudication for claim line items.
        List of `ClaimResponseItem` items (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
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
        
        self.payeeType = None
        """ Party to be paid any benefits payable.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._payeeType = None
        """ Primitive extension for payeeType. Type `FHIRPrimitiveExtension` """
        
        self.payment = None
        """ Payment Details.
        Type `ClaimResponsePayment` (represented as `dict` in JSON). """
        self._payment = None
        """ Primitive extension for payment. Type `FHIRPrimitiveExtension` """
        
        self.preAuthPeriod = None
        """ Preauthorization reference effective period.
        Type `Period` (represented as `dict` in JSON). """
        self._preAuthPeriod = None
        """ Primitive extension for preAuthPeriod. Type `FHIRPrimitiveExtension` """
        
        self.preAuthRef = None
        """ Preauthorization reference.
        Type `str`. """
        self._preAuthRef = None
        """ Primitive extension for preAuthRef. Type `FHIRPrimitiveExtension` """
        
        self.processNote = None
        """ Note concerning adjudication.
        List of `ClaimResponseProcessNote` items (represented as `dict` in JSON). """
        self._processNote = None
        """ Primitive extension for processNote. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Id of resource triggering adjudication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.requestor = None
        """ Party responsible for the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requestor = None
        """ Primitive extension for requestor. Type `FHIRPrimitiveExtension` """
        
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
        
        self.total = None
        """ Adjudication totals.
        List of `ClaimResponseTotal` items (represented as `dict` in JSON). """
        self._total = None
        """ Primitive extension for total. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ More granular claim type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ claim | preauthorization | predetermination.
        Type `str`. """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        super(ClaimResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponse, self).elementProperties()
        js.extend([
            ("addItem", "addItem", ClaimResponseAddItem, True, None, False),
            ("_addItem", "_addItem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("communicationRequest", "communicationRequest", fhirreference.FHIRReference, True, None, False),
            ("_communicationRequest", "_communicationRequest", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("error", "error", ClaimResponseError, True, None, False),
            ("_error", "_error", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("form", "form", attachment.Attachment, False, None, False),
            ("_form", "_form", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("_formCode", "_formCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("_fundsReserve", "_fundsReserve", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurance", "insurance", ClaimResponseInsurance, True, None, False),
            ("_insurance", "_insurance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("_insurer", "_insurer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", ClaimResponseItem, True, None, False),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payeeType", "payeeType", codeableconcept.CodeableConcept, False, None, False),
            ("_payeeType", "_payeeType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payment", "payment", ClaimResponsePayment, False, None, False),
            ("_payment", "_payment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preAuthPeriod", "preAuthPeriod", period.Period, False, None, False),
            ("_preAuthPeriod", "_preAuthPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("_preAuthRef", "_preAuthRef", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("processNote", "processNote", ClaimResponseProcessNote, True, None, False),
            ("_processNote", "_processNote", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("_requestor", "_requestor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("_subType", "_subType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("total", "total", ClaimResponseTotal, True, None, False),
            ("_total", "_total", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", str, False, None, True),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ClaimResponseAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The first-tier service adjudications for payor added product or service
    lines.
    """
    
    resource_type = "ClaimResponseAddItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items adjudication.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.bodySite = None
        """ Anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Insurer added line details.
        List of `ClaimResponseAddItemDetail` items (represented as `dict` in JSON). """
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
        
        self.subSite = None
        """ Anatomical sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._subSite = None
        """ Primitive extension for subSite. Type `FHIRPrimitiveExtension` """
        
        self.subdetailSequence = None
        """ Subdetail sequence number.
        List of `int` items. """
        self._subdetailSequence = None
        """ Primitive extension for subdetailSequence. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(ClaimResponseAddItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", ClaimResponseAddItemDetail, True, None, False),
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
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("_subSite", "_subSite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subdetailSequence", "subdetailSequence", int, True, None, False),
            ("_subdetailSequence", "_subdetailSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """ Insurer added line details.
    
    The second-tier service adjudications for payor added services.
    """
    
    resource_type = "ClaimResponseAddItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items detail adjudication.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
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
        List of `ClaimResponseAddItemDetailSubDetail` items (represented as `dict` in JSON). """
        self._subDetail = None
        """ Primitive extension for subDetail. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(ClaimResponseAddItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
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
            ("subDetail", "subDetail", ClaimResponseAddItemDetailSubDetail, True, None, False),
            ("_subDetail", "_subDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimResponseAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The third-tier service adjudications for payor added services.
    """
    
    resource_type = "ClaimResponseAddItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items detail adjudication.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
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
        
        super(ClaimResponseAddItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
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


class ClaimResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Errors encountered during the processing of the adjudication.
    """
    
    resource_type = "ClaimResponseError"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.detailSequence = None
        """ Detail sequence number.
        Type `int`. """
        self._detailSequence = None
        """ Primitive extension for detailSequence. Type `FHIRPrimitiveExtension` """
        
        self.itemSequence = None
        """ Item sequence number.
        Type `int`. """
        self._itemSequence = None
        """ Primitive extension for itemSequence. Type `FHIRPrimitiveExtension` """
        
        self.subDetailSequence = None
        """ Subdetail sequence number.
        Type `int`. """
        self._subDetailSequence = None
        """ Primitive extension for subDetailSequence. Type `FHIRPrimitiveExtension` """
        
        super(ClaimResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailSequence", "detailSequence", int, False, None, False),
            ("_detailSequence", "_detailSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemSequence", "itemSequence", int, False, None, False),
            ("_itemSequence", "_itemSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, False),
            ("_subDetailSequence", "_subDetailSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    
    resource_type = "ClaimResponseInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement = None
        """ Additional provider contract number.
        Type `str`. """
        self._businessArrangement = None
        """ Primitive extension for businessArrangement. Type `FHIRPrimitiveExtension` """
        
        self.claimResponse = None
        """ Adjudication results.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._claimResponse = None
        """ Primitive extension for claimResponse. Type `FHIRPrimitiveExtension` """
        
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
        
        self.sequence = None
        """ Insurance instance identifier.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        super(ClaimResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("_businessArrangement", "_businessArrangement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("_claimResponse", "_claimResponse", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("_coverage", "_coverage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focal", "focal", bool, False, None, True),
            ("_focal", "_focal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimResponseItem(backboneelement.BackboneElement):
    """ Adjudication for claim line items.
    
    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    
    resource_type = "ClaimResponseItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Adjudication for claim details.
        List of `ClaimResponseItemDetail` items (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.itemSequence = None
        """ Claim item instance identifier.
        Type `int`. """
        self._itemSequence = None
        """ Primitive extension for itemSequence. Type `FHIRPrimitiveExtension` """
        
        self.noteNumber = None
        """ Applicable note numbers.
        List of `int` items. """
        self._noteNumber = None
        """ Primitive extension for noteNumber. Type `FHIRPrimitiveExtension` """
        
        super(ClaimResponseItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", ClaimResponseItemDetail, True, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemSequence", "itemSequence", int, False, None, True),
            ("_itemSequence", "_itemSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    
    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    
    resource_type = "ClaimResponseItemAdjudication"
    
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
        """ Non-monetary value.
        Type `float`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(ClaimResponseItemAdjudication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemAdjudication, self).elementProperties()
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


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """ Adjudication for claim details.
    
    A claim detail. Either a simple (a product or service) or a 'group' of sub-
    details which are simple items.
    """
    
    resource_type = "ClaimResponseItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Detail level adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.detailSequence = None
        """ Claim detail instance identifier.
        Type `int`. """
        self._detailSequence = None
        """ Primitive extension for detailSequence. Type `FHIRPrimitiveExtension` """
        
        self.noteNumber = None
        """ Applicable note numbers.
        List of `int` items. """
        self._noteNumber = None
        """ Primitive extension for noteNumber. Type `FHIRPrimitiveExtension` """
        
        self.subDetail = None
        """ Adjudication for claim sub-details.
        List of `ClaimResponseItemDetailSubDetail` items (represented as `dict` in JSON). """
        self._subDetail = None
        """ Primitive extension for subDetail. Type `FHIRPrimitiveExtension` """
        
        super(ClaimResponseItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailSequence", "detailSequence", int, False, None, True),
            ("_detailSequence", "_detailSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subDetail", "subDetail", ClaimResponseItemDetailSubDetail, True, None, False),
            ("_subDetail", "_subDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """ Adjudication for claim sub-details.
    
    A sub-detail adjudication of a simple product or service.
    """
    
    resource_type = "ClaimResponseItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Subdetail level adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        self._adjudication = None
        """ Primitive extension for adjudication. Type `FHIRPrimitiveExtension` """
        
        self.noteNumber = None
        """ Applicable note numbers.
        List of `int` items. """
        self._noteNumber = None
        """ Primitive extension for noteNumber. Type `FHIRPrimitiveExtension` """
        
        self.subDetailSequence = None
        """ Claim sub-detail instance identifier.
        Type `int`. """
        self._subDetailSequence = None
        """ Primitive extension for subDetailSequence. Type `FHIRPrimitiveExtension` """
        
        super(ClaimResponseItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("_adjudication", "_adjudication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("_noteNumber", "_noteNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, True),
            ("_subDetailSequence", "_subDetailSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimResponsePayment(backboneelement.BackboneElement):
    """ Payment Details.
    
    Payment details for the adjudication of the claim.
    """
    
    resource_type = "ClaimResponsePayment"
    
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
        """ Explanation for the adjustment.
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
        
        super(ClaimResponsePayment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponsePayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("_adjustment", "_adjustment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, False, None, False),
            ("_adjustmentReason", "_adjustmentReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amount", "amount", money.Money, False, None, True),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """ Note concerning adjudication.
    
    A note that describes or explains adjudication results in a human readable
    form.
    """
    
    resource_type = "ClaimResponseProcessNote"
    
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
        
        super(ClaimResponseProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("number", "number", int, False, None, False),
            ("_number", "_number", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, True),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimResponseTotal(backboneelement.BackboneElement):
    """ Adjudication totals.
    
    Categorized monetary totals for the adjudication.
    """
    
    resource_type = "ClaimResponseTotal"
    
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
        
        super(ClaimResponseTotal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseTotal, self).elementProperties()
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
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity