# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Population).
# 2024, SMART Health IT.


from . import backboneelement

class Population(backboneelement.BackboneElement):
    """ A definition of a set of people that apply to some clinically related
    context, for example people contraindicated for a certain medication.
    
    A populatioof people with some set of grouping criteria.
    """
    
    resource_type = "Population"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ageCodeableConcept = None
        """ The age of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._ageCodeableConcept = None
        """ Primitive extension for ageCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.ageRange = None
        """ The age of the specific population.
        Type `Range` (represented as `dict` in JSON). """
        self._ageRange = None
        """ Primitive extension for ageRange. Type `FHIRPrimitiveExtension` """
        
        self.gender = None
        """ The gender of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._gender = None
        """ Primitive extension for gender. Type `FHIRPrimitiveExtension` """
        
        self.physiologicalCondition = None
        """ The existing physiological conditions of the specific population to
        which this applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._physiologicalCondition = None
        """ Primitive extension for physiologicalCondition. Type `FHIRPrimitiveExtension` """
        
        self.race = None
        """ Race of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._race = None
        """ Primitive extension for race. Type `FHIRPrimitiveExtension` """
        
        super(Population, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Population, self).elementProperties()
        js.extend([
            ("ageCodeableConcept", "ageCodeableConcept", codeableconcept.CodeableConcept, False, "age", False),
            ("_ageCodeableConcept", "_ageCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("_ageRange", "_ageRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("gender", "gender", codeableconcept.CodeableConcept, False, None, False),
            ("_gender", "_gender", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("physiologicalCondition", "physiologicalCondition", codeableconcept.CodeableConcept, False, None, False),
            ("_physiologicalCondition", "_physiologicalCondition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("race", "race", codeableconcept.CodeableConcept, False, None, False),
            ("_race", "_race", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import range