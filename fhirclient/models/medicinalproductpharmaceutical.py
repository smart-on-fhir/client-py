# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical).
# 2024, SMART Health IT.


from . import domainresource

class MedicinalProductPharmaceutical(domainresource.DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    
    resource_type = "MedicinalProductPharmaceutical"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.administrableDoseForm = None
        """ The administrable dose form, after necessary reconstitution.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._administrableDoseForm = None
        """ Primitive extension for administrableDoseForm. Type `FHIRPrimitiveExtension` """
        
        self.characteristics = None
        """ Characteristics e.g. a products onset of action.
        List of `MedicinalProductPharmaceuticalCharacteristics` items (represented as `dict` in JSON). """
        self._characteristics = None
        """ Primitive extension for characteristics. Type `FHIRPrimitiveExtension` """
        
        self.device = None
        """ Accompanying device.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._device = None
        """ Primitive extension for device. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ An identifier for the pharmaceutical medicinal product.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.ingredient = None
        """ Ingredient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._ingredient = None
        """ Primitive extension for ingredient. Type `FHIRPrimitiveExtension` """
        
        self.routeOfAdministration = None
        """ The path by which the pharmaceutical product is taken into or makes
        contact with the body.
        List of `MedicinalProductPharmaceuticalRouteOfAdministration` items (represented as `dict` in JSON). """
        self._routeOfAdministration = None
        """ Primitive extension for routeOfAdministration. Type `FHIRPrimitiveExtension` """
        
        self.unitOfPresentation = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._unitOfPresentation = None
        """ Primitive extension for unitOfPresentation. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductPharmaceutical, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceutical, self).elementProperties()
        js.extend([
            ("administrableDoseForm", "administrableDoseForm", codeableconcept.CodeableConcept, False, None, True),
            ("_administrableDoseForm", "_administrableDoseForm", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("characteristics", "characteristics", MedicinalProductPharmaceuticalCharacteristics, True, None, False),
            ("_characteristics", "_characteristics", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("_device", "_device", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ingredient", "ingredient", fhirreference.FHIRReference, True, None, False),
            ("_ingredient", "_ingredient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("routeOfAdministration", "routeOfAdministration", MedicinalProductPharmaceuticalRouteOfAdministration, True, None, True),
            ("_routeOfAdministration", "_routeOfAdministration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
            ("_unitOfPresentation", "_unitOfPresentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductPharmaceuticalCharacteristics(backboneelement.BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    
    resource_type = "MedicinalProductPharmaceuticalCharacteristics"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ A coded characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ The status of characteristic e.g. assigned or pending.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductPharmaceuticalCharacteristics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalCharacteristics, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductPharmaceuticalRouteOfAdministration(backboneelement.BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    
    resource_type = "MedicinalProductPharmaceuticalRouteOfAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Coded expression for the route.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.firstDose = None
        """ The first dose (dose quantity) administered in humans can be
        specified, for a product under investigation, using a numerical
        value and its unit of measurement.
        Type `Quantity` (represented as `dict` in JSON). """
        self._firstDose = None
        """ Primitive extension for firstDose. Type `FHIRPrimitiveExtension` """
        
        self.maxDosePerDay = None
        """ The maximum dose per day (maximum dose quantity to be administered
        in any one 24-h period) that can be administered as per the
        protocol referenced in the clinical trial authorisation.
        Type `Quantity` (represented as `dict` in JSON). """
        self._maxDosePerDay = None
        """ Primitive extension for maxDosePerDay. Type `FHIRPrimitiveExtension` """
        
        self.maxDosePerTreatmentPeriod = None
        """ The maximum dose per treatment period that can be administered as
        per the protocol referenced in the clinical trial authorisation.
        Type `Ratio` (represented as `dict` in JSON). """
        self._maxDosePerTreatmentPeriod = None
        """ Primitive extension for maxDosePerTreatmentPeriod. Type `FHIRPrimitiveExtension` """
        
        self.maxSingleDose = None
        """ The maximum single dose that can be administered as per the
        protocol of a clinical trial can be specified using a numerical
        value and its unit of measurement.
        Type `Quantity` (represented as `dict` in JSON). """
        self._maxSingleDose = None
        """ Primitive extension for maxSingleDose. Type `FHIRPrimitiveExtension` """
        
        self.maxTreatmentPeriod = None
        """ The maximum treatment period during which an Investigational
        Medicinal Product can be administered as per the protocol
        referenced in the clinical trial authorisation.
        Type `Duration` (represented as `dict` in JSON). """
        self._maxTreatmentPeriod = None
        """ Primitive extension for maxTreatmentPeriod. Type `FHIRPrimitiveExtension` """
        
        self.targetSpecies = None
        """ A species for which this route applies.
        List of `MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies` items (represented as `dict` in JSON). """
        self._targetSpecies = None
        """ Primitive extension for targetSpecies. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministration, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("firstDose", "firstDose", quantity.Quantity, False, None, False),
            ("_firstDose", "_firstDose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxDosePerDay", "maxDosePerDay", quantity.Quantity, False, None, False),
            ("_maxDosePerDay", "_maxDosePerDay", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxDosePerTreatmentPeriod", "maxDosePerTreatmentPeriod", ratio.Ratio, False, None, False),
            ("_maxDosePerTreatmentPeriod", "_maxDosePerTreatmentPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxSingleDose", "maxSingleDose", quantity.Quantity, False, None, False),
            ("_maxSingleDose", "_maxSingleDose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxTreatmentPeriod", "maxTreatmentPeriod", duration.Duration, False, None, False),
            ("_maxTreatmentPeriod", "_maxTreatmentPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetSpecies", "targetSpecies", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, True, None, False),
            ("_targetSpecies", "_targetSpecies", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(backboneelement.BackboneElement):
    """ A species for which this route applies.
    """
    
    resource_type = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Coded expression for the species.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.withdrawalPeriod = None
        """ A species specific time during which consumption of animal product
        is not appropriate.
        List of `MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod` items (represented as `dict` in JSON). """
        self._withdrawalPeriod = None
        """ Primitive extension for withdrawalPeriod. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("withdrawalPeriod", "withdrawalPeriod", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, True, None, False),
            ("_withdrawalPeriod", "_withdrawalPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(backboneelement.BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    
    resource_type = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.supportingInformation = None
        """ Extra information about the withdrawal period.
        Type `str`. """
        self._supportingInformation = None
        """ Primitive extension for supportingInformation. Type `FHIRPrimitiveExtension` """
        
        self.tissue = None
        """ Coded expression for the type of tissue for which the withdrawal
        period applues, e.g. meat, milk.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._tissue = None
        """ Primitive extension for tissue. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ A value for the time.
        Type `Quantity` (represented as `dict` in JSON). """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).elementProperties()
        js.extend([
            ("supportingInformation", "supportingInformation", str, False, None, False),
            ("_supportingInformation", "_supportingInformation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("tissue", "tissue", codeableconcept.CodeableConcept, False, None, True),
            ("_tissue", "_tissue", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", quantity.Quantity, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import duration
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio