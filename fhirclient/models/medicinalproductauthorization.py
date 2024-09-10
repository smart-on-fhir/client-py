# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization).
# 2024, SMART Health IT.


from . import domainresource

class MedicinalProductAuthorization(domainresource.DomainResource):
    """ The regulatory authorization of a medicinal product.
    """
    
    resource_type = "MedicinalProductAuthorization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ The country in which the marketing authorization has been granted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._country = None
        """ Primitive extension for country. Type `FHIRPrimitiveExtension` """
        
        self.dataExclusivityPeriod = None
        """ A period of time after authorization before generic product
        applicatiosn can be submitted.
        Type `Period` (represented as `dict` in JSON). """
        self._dataExclusivityPeriod = None
        """ Primitive extension for dataExclusivityPeriod. Type `FHIRPrimitiveExtension` """
        
        self.dateOfFirstAuthorization = None
        """ The date when the first authorization was granted by a Medicines
        Regulatory Agency.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._dateOfFirstAuthorization = None
        """ Primitive extension for dateOfFirstAuthorization. Type `FHIRPrimitiveExtension` """
        
        self.holder = None
        """ Marketing Authorization Holder.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._holder = None
        """ Primitive extension for holder. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier for the marketing authorization, as assigned by
        a regulator.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.internationalBirthDate = None
        """ Date of first marketing authorization for a company's new medicinal
        product in any country in the World.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._internationalBirthDate = None
        """ Primitive extension for internationalBirthDate. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Jurisdiction within a country.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.jurisdictionalAuthorization = None
        """ Authorization in areas within a country.
        List of `MedicinalProductAuthorizationJurisdictionalAuthorization` items (represented as `dict` in JSON). """
        self._jurisdictionalAuthorization = None
        """ Primitive extension for jurisdictionalAuthorization. Type `FHIRPrimitiveExtension` """
        
        self.legalBasis = None
        """ The legal framework against which this authorization is granted.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._legalBasis = None
        """ Primitive extension for legalBasis. Type `FHIRPrimitiveExtension` """
        
        self.procedure = None
        """ The regulatory procedure for granting or amending a marketing
        authorization.
        Type `MedicinalProductAuthorizationProcedure` (represented as `dict` in JSON). """
        self._procedure = None
        """ Primitive extension for procedure. Type `FHIRPrimitiveExtension` """
        
        self.regulator = None
        """ Medicines Regulatory Agency.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._regulator = None
        """ Primitive extension for regulator. Type `FHIRPrimitiveExtension` """
        
        self.restoreDate = None
        """ The date when a suspended the marketing or the marketing
        authorization of the product is anticipated to be restored.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._restoreDate = None
        """ Primitive extension for restoreDate. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ The status of the marketing authorization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusDate = None
        """ The date at which the given status has become applicable.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._statusDate = None
        """ Primitive extension for statusDate. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ The medicinal product that is being authorized.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.validityPeriod = None
        """ The beginning of the time period in which the marketing
        authorization is in the specific status shall be specified A
        complete date consisting of day, month and year shall be specified
        using the ISO 8601 date format.
        Type `Period` (represented as `dict` in JSON). """
        self._validityPeriod = None
        """ Primitive extension for validityPeriod. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductAuthorization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("_country", "_country", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dataExclusivityPeriod", "dataExclusivityPeriod", period.Period, False, None, False),
            ("_dataExclusivityPeriod", "_dataExclusivityPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dateOfFirstAuthorization", "dateOfFirstAuthorization", fhirdatetime.FHIRDateTime, False, None, False),
            ("_dateOfFirstAuthorization", "_dateOfFirstAuthorization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("holder", "holder", fhirreference.FHIRReference, False, None, False),
            ("_holder", "_holder", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("internationalBirthDate", "internationalBirthDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_internationalBirthDate", "_internationalBirthDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdictionalAuthorization", "jurisdictionalAuthorization", MedicinalProductAuthorizationJurisdictionalAuthorization, True, None, False),
            ("_jurisdictionalAuthorization", "_jurisdictionalAuthorization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("legalBasis", "legalBasis", codeableconcept.CodeableConcept, False, None, False),
            ("_legalBasis", "_legalBasis", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("procedure", "procedure", MedicinalProductAuthorizationProcedure, False, None, False),
            ("_procedure", "_procedure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, False),
            ("_regulator", "_regulator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("restoreDate", "restoreDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_restoreDate", "_restoreDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusDate", "statusDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_statusDate", "_statusDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
            ("_validityPeriod", "_validityPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductAuthorizationJurisdictionalAuthorization(backboneelement.BackboneElement):
    """ Authorization in areas within a country.
    """
    
    resource_type = "MedicinalProductAuthorizationJurisdictionalAuthorization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ Country of authorization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._country = None
        """ Primitive extension for country. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ The assigned number for the marketing authorization.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Jurisdiction within a country.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.legalStatusOfSupply = None
        """ The legal status of supply in a jurisdiction or region.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._legalStatusOfSupply = None
        """ Primitive extension for legalStatusOfSupply. Type `FHIRPrimitiveExtension` """
        
        self.validityPeriod = None
        """ The start and expected end date of the authorization.
        Type `Period` (represented as `dict` in JSON). """
        self._validityPeriod = None
        """ Primitive extension for validityPeriod. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, False),
            ("_country", "_country", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("_legalStatusOfSupply", "_legalStatusOfSupply", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
            ("_validityPeriod", "_validityPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductAuthorizationProcedure(backboneelement.BackboneElement):
    """ The regulatory procedure for granting or amending a marketing authorization.
    """
    
    resource_type = "MedicinalProductAuthorizationProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.application = None
        """ Applcations submitted to obtain a marketing authorization.
        List of `MedicinalProductAuthorizationProcedure` items (represented as `dict` in JSON). """
        self._application = None
        """ Primitive extension for application. Type `FHIRPrimitiveExtension` """
        
        self.dateDateTime = None
        """ Date of procedure.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._dateDateTime = None
        """ Primitive extension for dateDateTime. Type `FHIRPrimitiveExtension` """
        
        self.datePeriod = None
        """ Date of procedure.
        Type `Period` (represented as `dict` in JSON). """
        self._datePeriod = None
        """ Primitive extension for datePeriod. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifier for this procedure.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductAuthorizationProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorizationProcedure, self).elementProperties()
        js.extend([
            ("application", "application", MedicinalProductAuthorizationProcedure, True, None, False),
            ("_application", "_application", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dateDateTime", "dateDateTime", fhirdatetime.FHIRDateTime, False, "date", False),
            ("_dateDateTime", "_dateDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("datePeriod", "datePeriod", period.Period, False, "date", False),
            ("_datePeriod", "_datePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period