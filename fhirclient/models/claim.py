# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Claim).
# 2024, SMART Health IT.


from . import domainresource

class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    
    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """
    
    resource_type = "Claim"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident = None
        """ Details of the event.
        Type `ClaimAccident` (represented as `dict` in JSON). """
        self._accident = None
        """ Primitive extension for accident. Type `FHIRPrimitiveExtension` """
        
        self.billablePeriod = None
        """ Relevant time frame for the claim.
        Type `Period` (represented as `dict` in JSON). """
        self._billablePeriod = None
        """ Primitive extension for billablePeriod. Type `FHIRPrimitiveExtension` """
        
        self.careTeam = None
        """ Members of the care team.
        List of `ClaimCareTeam` items (represented as `dict` in JSON). """
        self._careTeam = None
        """ Primitive extension for careTeam. Type `FHIRPrimitiveExtension` """
        
        self.created = None
        """ Resource creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.diagnosis = None
        """ Pertinent diagnosis information.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
        self._diagnosis = None
        """ Primitive extension for diagnosis. Type `FHIRPrimitiveExtension` """
        
        self.enterer = None
        """ Author of the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._enterer = None
        """ Primitive extension for enterer. Type `FHIRPrimitiveExtension` """
        
        self.facility = None
        """ Servicing facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._facility = None
        """ Primitive extension for facility. Type `FHIRPrimitiveExtension` """
        
        self.fundsReserve = None
        """ For whom to reserve funds.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._fundsReserve = None
        """ Primitive extension for fundsReserve. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for claim.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.insurance = None
        """ Patient insurance information.
        List of `ClaimInsurance` items (represented as `dict` in JSON). """
        self._insurance = None
        """ Primitive extension for insurance. Type `FHIRPrimitiveExtension` """
        
        self.insurer = None
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._insurer = None
        """ Primitive extension for insurer. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Product or service provided.
        List of `ClaimItem` items (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        self.originalPrescription = None
        """ Original prescription if superseded by fulfiller.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._originalPrescription = None
        """ Primitive extension for originalPrescription. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ The recipient of the products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.payee = None
        """ Recipient of benefits payable.
        Type `ClaimPayee` (represented as `dict` in JSON). """
        self._payee = None
        """ Primitive extension for payee. Type `FHIRPrimitiveExtension` """
        
        self.prescription = None
        """ Prescription authorizing services and products.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._prescription = None
        """ Primitive extension for prescription. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ Desired processing ugency.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.procedure = None
        """ Clinical procedures performed.
        List of `ClaimProcedure` items (represented as `dict` in JSON). """
        self._procedure = None
        """ Primitive extension for procedure. Type `FHIRPrimitiveExtension` """
        
        self.provider = None
        """ Party responsible for the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._provider = None
        """ Primitive extension for provider. Type `FHIRPrimitiveExtension` """
        
        self.referral = None
        """ Treatment referral.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._referral = None
        """ Primitive extension for referral. Type `FHIRPrimitiveExtension` """
        
        self.related = None
        """ Prior or corollary claims.
        List of `ClaimRelated` items (represented as `dict` in JSON). """
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
        List of `ClaimSupportingInfo` items (represented as `dict` in JSON). """
        self._supportingInfo = None
        """ Primitive extension for supportingInfo. Type `FHIRPrimitiveExtension` """
        
        self.total = None
        """ Total claim cost.
        Type `Money` (represented as `dict` in JSON). """
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
        
        super(Claim, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("accident", "accident", ClaimAccident, False, None, False),
            ("_accident", "_accident", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("_billablePeriod", "_billablePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("careTeam", "careTeam", ClaimCareTeam, True, None, False),
            ("_careTeam", "_careTeam", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("_diagnosis", "_diagnosis", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("_enterer", "_enterer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("_facility", "_facility", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("_fundsReserve", "_fundsReserve", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurance", "insurance", ClaimInsurance, True, None, True),
            ("_insurance", "_insurance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("_insurer", "_insurer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("_originalPrescription", "_originalPrescription", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("_payee", "_payee", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("_prescription", "_prescription", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, True),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("procedure", "procedure", ClaimProcedure, True, None, False),
            ("_procedure", "_procedure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("_provider", "_provider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("_referral", "_referral", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("related", "related", ClaimRelated, True, None, False),
            ("_related", "_related", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("_subType", "_subType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInfo", "supportingInfo", ClaimSupportingInfo, True, None, False),
            ("_supportingInfo", "_supportingInfo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("total", "total", money.Money, False, None, False),
            ("_total", "_total", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", str, False, None, True),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ClaimAccident(backboneelement.BackboneElement):
    """ Details of the event.
    
    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    
    resource_type = "ClaimAccident"
    
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
        
        super(ClaimAccident, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("_locationAddress", "_locationAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("_locationReference", "_locationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimCareTeam(backboneelement.BackboneElement):
    """ Members of the care team.
    
    The members of the team who provided the products and services.
    """
    
    resource_type = "ClaimCareTeam"
    
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
        
        super(ClaimCareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimCareTeam, self).elementProperties()
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


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.
    
    Information about diagnoses relevant to the claim items.
    """
    
    resource_type = "ClaimDiagnosis"
    
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
        
        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
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


class ClaimInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    
    resource_type = "ClaimInsurance"
    
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
        
        self.identifier = None
        """ Pre-assigned Claim number.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.preAuthRef = None
        """ Prior authorization reference number.
        List of `str` items. """
        self._preAuthRef = None
        """ Primitive extension for preAuthRef. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Insurance instance identifier.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        super(ClaimInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("_businessArrangement", "_businessArrangement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("_claimResponse", "_claimResponse", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("_coverage", "_coverage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focal", "focal", bool, False, None, True),
            ("_focal", "_focal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("_preAuthRef", "_preAuthRef", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimItem(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """
    
    resource_type = "ClaimItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite = None
        """ Anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.careTeamSequence = None
        """ Applicable careTeam members.
        List of `int` items. """
        self._careTeamSequence = None
        """ Primitive extension for careTeamSequence. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Product or service provided.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """
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
        
        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("_careTeamSequence", "_careTeamSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
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


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    
    resource_type = "ClaimItemDetail"
    
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
        
        self.subDetail = None
        """ Product or service provided.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
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
        
        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("_net", "_net", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
            ("_subDetail", "_subDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("_udi", "_udi", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    
    resource_type = "ClaimItemDetailSubDetail"
    
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
        
        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("net", "net", money.Money, False, None, False),
            ("_net", "_net", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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


class ClaimPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.
    
    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    
    resource_type = "ClaimPayee"
    
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
        
        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("_party", "_party", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.
    
    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    
    resource_type = "ClaimProcedure"
    
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
        
        super(ClaimProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
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


class ClaimRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.
    
    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    
    resource_type = "ClaimRelated"
    
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
        
        super(ClaimRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("_claim", "_claim", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClaimSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    
    resource_type = "ClaimSupportingInfo"
    
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
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
        
        super(ClaimSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
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