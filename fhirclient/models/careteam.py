#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/CareTeam) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class CareTeam(domainresource.DomainResource):
    """ Planned participants in the coordination and delivery of care for a patient
    or group.
    
    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """
    
    resource_type = "CareTeam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Type of team.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or episode associated with CareTeam.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this team.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization responsible for the care team.
        List of `FHIRReference` items referencing `Organization` (represented as `dict` in JSON). """
        
        self.name = None
        """ Name of the team, such as crisis assessment team.
        Type `str`. """
        
        self.note = None
        """ Comments made about the CareTeam.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.participant = None
        """ Members of the team.
        List of `CareTeamParticipant` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period team covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why the care team exists.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why the care team exists.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | active | suspended | inactive | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Who care team is for.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        super(CareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CareTeam, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("participant", "participant", CareTeamParticipant, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class CareTeamParticipant(backboneelement.BackboneElement):
    """ Members of the team.
    
    Identifies all people and organizations who are expected to be involved in
    the care team.
    """
    
    resource_type = "CareTeamParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.member = None
        """ Who is involved.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Organization, CareTeam` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ Organization of the practitioner.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period of participant.
        Type `Period` (represented as `dict` in JSON). """
        
        self.role = None
        """ Type of involvement.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CareTeamParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CareTeamParticipant, self).elementProperties()
        js.extend([
            ("member", "member", fhirreference.FHIRReference, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
