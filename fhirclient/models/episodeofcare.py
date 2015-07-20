#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period


class EpisodeOfCare(domainresource.DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.
    
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """
    
    resource_name = "EpisodeOfCare"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.careManager = None
        """ The practitioner that is the care manager/care co-ordinator for
        this patient.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ The list of practitioners that may be facilitating this episode of
        care for specific purposes.
        List of `EpisodeOfCareCareTeam` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ A list of conditions/problems/diagnoses that this episode of care
        is intended to be providing care for.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier(s) by which this EpisodeOfCare is known.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ The organization that has assumed the specific responsibilities for
        the specified duration.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient that this EpisodeOfCare applies to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ The interval during which the managing organization assumes the
        defined responsibility.
        Type `Period` (represented as `dict` in JSON). """
        
        self.referralRequest = None
        """ Referral Request(s) that this EpisodeOfCare manages activities
        within.
        List of `FHIRReference` items referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled.
        Type `str`. """
        
        self.statusHistory = None
        """ The status history for the EpisodeOfCare.
        List of `EpisodeOfCareStatusHistory` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Specific type of EpisodeOfCare.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EpisodeOfCare, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(EpisodeOfCare, self).elementProperties()
        js.extend([
            ("careManager", "careManager", fhirreference.FHIRReference, False),
            ("careTeam", "careTeam", EpisodeOfCareCareTeam, True),
            ("condition", "condition", fhirreference.FHIRReference, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("referralRequest", "referralRequest", fhirreference.FHIRReference, True),
            ("status", "status", str, False),
            ("statusHistory", "statusHistory", EpisodeOfCareStatusHistory, True),
            ("type", "type", codeableconcept.CodeableConcept, True),
        ])
        return js


class EpisodeOfCareCareTeam(fhirelement.FHIRElement):
    """ The list of practitioners that may be facilitating this episode of care for
    specific purposes.
    """
    
    resource_name = "EpisodeOfCareCareTeam"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.member = None
        """ The practitioner (or Organization) within the team.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period of time that this practitioner is performing some role
        within the episode of care.
        Type `Period` (represented as `dict` in JSON). """
        
        self.role = None
        """ The role that this team member is taking within this episode of
        care.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EpisodeOfCareCareTeam, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareCareTeam, self).elementProperties()
        js.extend([
            ("member", "member", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("role", "role", codeableconcept.CodeableConcept, True),
        ])
        return js


class EpisodeOfCareStatusHistory(fhirelement.FHIRElement):
    """ The status history for the EpisodeOfCare.
    """
    
    resource_name = "EpisodeOfCareStatusHistory"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.period = None
        """ The period during this EpisodeOfCare that the specific status
        applied.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled.
        Type `str`. """
        
        super(EpisodeOfCareStatusHistory, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareStatusHistory, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False),
            ("status", "status", str, False),
        ])
        return js

