#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/ResearchSubject) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class ResearchSubject(domainresource.DomainResource):
    """ Investigation to increase healthcare-related patient-independent knowledge.
    
    A process where a researcher or organization plans and then executes a
    series of steps intended to increase the field of healthcare-related
    knowledge.  This includes studies of safety, efficacy, comparative
    effectiveness and other information about medications, devices, therapies
    and other interventional and investigative techniques.  A ResearchStudy
    involves the gathering of information about human or animal subjects.
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
        
        self.assignedArm = None
        """ What path should be followed.
        Type `str`. """
        
        self.consent = None
        """ Agreement to participate in study.
        Type `FHIRReference` referencing `Consent` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier for research subject.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.individual = None
        """ Who is part of study.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ Start and end of participation.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ candidate | enrolled | active | suspended | withdrawn | completed.
        Type `str`. """
        
        self.study = None
        """ Study subject is part of.
        Type `FHIRReference` referencing `ResearchStudy` (represented as `dict` in JSON). """
        
        super(ResearchSubject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchSubject, self).elementProperties()
        js.extend([
            ("actualArm", "actualArm", str, False, None, False),
            ("assignedArm", "assignedArm", str, False, None, False),
            ("consent", "consent", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("individual", "individual", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("status", "status", str, False, None, True),
            ("study", "study", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
