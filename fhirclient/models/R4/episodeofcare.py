#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare) on 2019-05-07.
#  2019, SMART Health IT.


from . import domainresource

class EpisodeOfCare(domainresource.DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.
    
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """
    
    resource_type = "EpisodeOfCare"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.account = None
        """ The set of accounts that may be used for billing for this
        EpisodeOfCare.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.careManager = None
        """ Care manager/care coordinator for the patient.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.diagnosis = None
        """ The list of diagnosis relevant to this episode of care.
        List of `EpisodeOfCareDiagnosis` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier(s) relevant for this EpisodeOfCare.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization that assumes care.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient who is the focus of this episode of care.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ Interval during responsibility is assumed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.referralRequest = None
        """ Originating Referral Request(s).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled |
        entered-in-error.
        Type `str`. """
        
        self.statusHistory = None
        """ Past list of status codes (the current status may be included to
        cover the start date of the status).
        List of `EpisodeOfCareStatusHistory` items (represented as `dict` in JSON). """
        
        self.team = None
        """ Other practitioners facilitating this episode of care.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type/class  - e.g. specialist referral, disease management.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EpisodeOfCare, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCare, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, True, None, False),
            ("careManager", "careManager", fhirreference.FHIRReference, False, None, False),
            ("diagnosis", "diagnosis", EpisodeOfCareDiagnosis, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("referralRequest", "referralRequest", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusHistory", "statusHistory", EpisodeOfCareStatusHistory, True, None, False),
            ("team", "team", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    """ The list of diagnosis relevant to this episode of care.
    """
    
    resource_type = "EpisodeOfCareDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.condition = None
        """ Conditions/problems/diagnoses this episode of care is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.rank = None
        """ Ranking of the diagnosis (for each role type).
        Type `int`. """
        
        self.role = None
        """ Role that this diagnosis has within the episode of care (e.g.
        admission, billing, discharge …).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EpisodeOfCareDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", fhirreference.FHIRReference, False, None, True),
            ("rank", "rank", int, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """ Past list of status codes (the current status may be included to cover the
    start date of the status).
    
    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """
    
    resource_type = "EpisodeOfCareStatusHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ Duration the EpisodeOfCare was in the specified status.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled |
        entered-in-error.
        Type `str`. """
        
        super(EpisodeOfCareStatusHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareStatusHistory, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
