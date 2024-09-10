# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MarketingStatus).
# 2024, SMART Health IT.


from . import backboneelement

class MarketingStatus(backboneelement.BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    
    resource_type = "MarketingStatus"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ The country in which the marketing authorisation has been granted
        shall be specified It should be specified using the ISO 3166 ‑ 1
        alpha-2 code elements.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._country = None
        """ Primitive extension for country. Type `FHIRPrimitiveExtension` """
        
        self.dateRange = None
        """ The date when the Medicinal Product is placed on the market by the
        Marketing Authorisation Holder (or where applicable, the
        manufacturer/distributor) in a country and/or jurisdiction shall be
        provided A complete date consisting of day, month and year shall be
        specified using the ISO 8601 date format NOTE “Placed on the
        market” refers to the release of the Medicinal Product into the
        distribution chain.
        Type `Period` (represented as `dict` in JSON). """
        self._dateRange = None
        """ Primitive extension for dateRange. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Where a Medicines Regulatory Agency has granted a marketing
        authorisation for which specific provisions within a jurisdiction
        apply, the jurisdiction can be specified using an appropriate
        controlled terminology The controlled term and the controlled term
        identifier shall be specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.restoreDate = None
        """ The date when the Medicinal Product is placed on the market by the
        Marketing Authorisation Holder (or where applicable, the
        manufacturer/distributor) in a country and/or jurisdiction shall be
        provided A complete date consisting of day, month and year shall be
        specified using the ISO 8601 date format NOTE “Placed on the
        market” refers to the release of the Medicinal Product into the
        distribution chain.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._restoreDate = None
        """ Primitive extension for restoreDate. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ This attribute provides information on the status of the marketing
        of the medicinal product See ISO/TS 20443 for more information and
        examples.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(MarketingStatus, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MarketingStatus, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, True),
            ("_country", "_country", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dateRange", "dateRange", period.Period, False, None, True),
            ("_dateRange", "_dateRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, False, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("restoreDate", "restoreDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_restoreDate", "_restoreDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import period