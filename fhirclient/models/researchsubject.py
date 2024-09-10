# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ResearchSubject).
# 2024, SMART Health IT.


from . import domainresource

class ResearchSubject(domainresource.DomainResource):
    """ Physical entity which is the primary unit of interest in the study.
    
    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """
    
    resource_type = "ResearchSubject"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actualArm = None
        """ What path was followed.
        Type `str`. """
        self._actualArm = None
        """ Primitive extension for actualArm. Type `FHIRPrimitiveExtension` """
        
        self.assignedArm = None
        """ What path should be followed.
        Type `str`. """
        self._assignedArm = None
        """ Primitive extension for assignedArm. Type `FHIRPrimitiveExtension` """
        
        self.consent = None
        """ Agreement to participate in study.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._consent = None
        """ Primitive extension for consent. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for research subject in a study.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.individual = None
        """ Who is part of study.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._individual = None
        """ Primitive extension for individual. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Start and end of participation.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ candidate | eligible | follow-up | ineligible | not-registered |
        off-study | on-study | on-study-intervention | on-study-observation
        | pending-on-study | potential-candidate | screening | withdrawn.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.study = None
        """ Study subject is part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._study = None
        """ Primitive extension for study. Type `FHIRPrimitiveExtension` """
        
        super(ResearchSubject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchSubject, self).elementProperties()
        js.extend([
            ("actualArm", "actualArm", str, False, None, False),
            ("_actualArm", "_actualArm", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("assignedArm", "assignedArm", str, False, None, False),
            ("_assignedArm", "_assignedArm", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("consent", "consent", fhirreference.FHIRReference, False, None, False),
            ("_consent", "_consent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("individual", "individual", fhirreference.FHIRReference, False, None, True),
            ("_individual", "_individual", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("study", "study", fhirreference.FHIRReference, False, None, True),
            ("_study", "_study", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import fhirreference
from . import identifier
from . import period