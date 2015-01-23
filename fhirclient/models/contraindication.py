#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (contraindication.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class Contraindication(fhirresource.FHIRResource):
    """ Clinical issue with action.
    
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient.  E.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    
    resource_name = "Contraindication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who found issue?.
        Type `FHIRReference` referencing `Practitioner, Device` (represented as `dict` in JSON). """
        
        self.category = None
        """ E.g. Drug-drug, duplicate therapy, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ When identified.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ Description and context.
        Type `str`. """
        
        self.identifier = None
        """ Unique id for the contraindication.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.implicated = None
        """ Problem resource.
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.mitigation = None
        """ Step taken to address.
        List of `ContraindicationMitigation` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Associated patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Authority for issue.
        Type `str`. """
        
        self.severity = None
        """ high | medium | low.
        Type `str`. """
        
        super(Contraindication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Contraindication, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'detail' in jsondict:
            self.detail = jsondict['detail']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'implicated' in jsondict:
            self.implicated = fhirreference.FHIRReference.with_json_and_owner(jsondict['implicated'], self)
        if 'mitigation' in jsondict:
            self.mitigation = ContraindicationMitigation.with_json_and_owner(jsondict['mitigation'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'reference' in jsondict:
            self.reference = jsondict['reference']
        if 'severity' in jsondict:
            self.severity = jsondict['severity']


class ContraindicationMitigation(fhirelement.FHIRElement):
    """ Step taken to address.
    
    Indicates an action that has been taken or is committed to to reduce or
    eliminate the likelihood of the risk identified by the contraindicaiton
    from manifesting.  Can also reflect an observation of known mitigating
    factors that may reduce/eliminate the need for any action.
    """
    
    resource_name = "ContraindicationMitigation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ What mitigation?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.author = None
        """ Who is committing?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date committed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ContraindicationMitigation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContraindicationMitigation, self).update_with_json(jsondict)
        if 'action' in jsondict:
            self.action = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['action'], self)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)

