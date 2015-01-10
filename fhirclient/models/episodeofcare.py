#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (episodeofcare.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirelement
import fhirreference
import fhirresource
import identifier
import period


class EpisodeOfCare(fhirresource.FHIRResource):
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
        
        self.currentStatus = None
        """ planned | active | onhold | finished | withdrawn | other.
        Type `str`. """
        
        self.identifier = None
        """ Identifier(s) by which this EpisodeOfCare is known.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ The organization that has assumed the specific responsibilities for
        the specified duration.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient that this episodeofcare applies to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ The interval during which the managing organization assumes the
        defined responsibility.
        Type `Period` (represented as `dict` in JSON). """
        
        self.referralRequest = None
        """ A Referral Request that this EpisodeOfCare manages activities
        within.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.statusHistory = None
        """ The status history for the EpisodeOfCare.
        List of `EpisodeOfCareStatusHistory` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Specific type of EpisodeOfcare.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EpisodeOfCare, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EpisodeOfCare, self).update_with_json(jsondict)
        if 'careManager' in jsondict:
            self.careManager = fhirreference.FHIRReference.with_json_and_owner(jsondict['careManager'], self)
        if 'careTeam' in jsondict:
            self.careTeam = EpisodeOfCareCareTeam.with_json_and_owner(jsondict['careTeam'], self)
        if 'condition' in jsondict:
            self.condition = fhirreference.FHIRReference.with_json_and_owner(jsondict['condition'], self)
        if 'currentStatus' in jsondict:
            self.currentStatus = jsondict['currentStatus']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'managingOrganization' in jsondict:
            self.managingOrganization = fhirreference.FHIRReference.with_json_and_owner(jsondict['managingOrganization'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'referralRequest' in jsondict:
            self.referralRequest = fhirreference.FHIRReference.with_json_and_owner(jsondict['referralRequest'], self)
        if 'statusHistory' in jsondict:
            self.statusHistory = EpisodeOfCareStatusHistory.with_json_and_owner(jsondict['statusHistory'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class EpisodeOfCareCareTeam(fhirelement.FHIRElement):
    """ The list of practitioners that may be facilitating this episode of care for
    specific purposes.
    """
    
    resource_name = "EpisodeOfCareCareTeam"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.member = None
        """ The practitioner within the team.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period of time that this practitioner is performing some role
        within the episode of care.
        Type `Period` (represented as `dict` in JSON). """
        
        self.role = None
        """ The role that this team member is taking within this episode of
        care.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(EpisodeOfCareCareTeam, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EpisodeOfCareCareTeam, self).update_with_json(jsondict)
        if 'member' in jsondict:
            self.member = fhirreference.FHIRReference.with_json_and_owner(jsondict['member'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['role'], self)


class EpisodeOfCareStatusHistory(fhirelement.FHIRElement):
    """ The status history for the EpisodeOfCare.
    """
    
    resource_name = "EpisodeOfCareStatusHistory"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.period = None
        """ The period during this episodeofcare that the specific status
        applied.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | active | onhold | finished | withdrawn | other.
        Type `str`. """
        
        super(EpisodeOfCareStatusHistory, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EpisodeOfCareStatusHistory, self).update_with_json(jsondict)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']

