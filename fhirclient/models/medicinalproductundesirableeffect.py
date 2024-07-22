# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect).
# 2024, SMART Health IT.


from . import domainresource

class MedicinalProductUndesirableEffect(domainresource.DomainResource):
    """ MedicinalProductUndesirableEffect.
    
    Describe the undesirable effects of the medicinal product.
    """
    
    resource_type = "MedicinalProductUndesirableEffect"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
        """ Classification of the effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.frequencyOfOccurrence = None
        """ The frequency of occurrence of the effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.population = None
        """ The population group to which this applies.
        List of `Population` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ The medication for which this is an indication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.symptomConditionEffect = None
        """ The symptom, condition or undesirable effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductUndesirableEffect, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductUndesirableEffect, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False),
            ("frequencyOfOccurrence", "frequencyOfOccurrence", codeableconcept.CodeableConcept, False, None, False),
            ("population", "population", population.Population, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("symptomConditionEffect", "symptomConditionEffect", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import population
