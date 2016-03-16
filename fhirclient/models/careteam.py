#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/CareTeam) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class CareTeam(domainresource.DomainResource):
    """ Participants in the coordination and delivery of care for a patient.
    
    A Care Team includes all the people and organizations of interest who
    participate in the coordination and delivery of care for a patient.
    """
    
    resource_name = "CareTeam"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ Type of team.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this team.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name of the team.
        Type `str`. """
        
        self.participant = None
        """ Members of the team.
        List of `CareTeamParticipant` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who care team is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period team covers.
        Type `Period` (represented as `dict` in JSON). """
        
        super(CareTeam, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(CareTeam, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("participant", "participant", CareTeamParticipant, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


from . import backboneelement

class CareTeamParticipant(backboneelement.BackboneElement):
    """ Members of the team.
    
    Identifies all people and organizations who are expected to be involved in
    the care team.
    """
    
    resource_name = "CareTeamParticipant"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.member = None
        """ Who is involved.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period of participant.
        Type `Period` (represented as `dict` in JSON). """
        
        self.role = None
        """ Type of involvement.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CareTeamParticipant, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(CareTeamParticipant, self).elementProperties()
        js.extend([
            ("member", "member", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period
