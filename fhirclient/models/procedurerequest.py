#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ProcedureRequest) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import timing


class ProcedureRequest(domainresource.DomainResource):
    """ A request for a procedure to be performed.
    
    A request for a procedure to be performed. May be a proposal or an order.
    """
    
    resource_name = "ProcedureRequest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.asNeededBoolean = None
        """ PRN.
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ PRN.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Target body sites.
        List of `ProcedureRequestBodySite` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Indication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Notes.
        List of `str` items. """
        
        self.orderedOn = None
        """ When Requested.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.orderer = None
        """ Ordering Party.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson, Device` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Performer.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | stat | asap.
        Type `str`. """
        
        self.status = None
        """ proposed | draft | requested | received | accepted | in-progress |
        completed | suspended | rejected | aborted.
        Type `str`. """
        
        self.subject = None
        """ Subject.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ Procedure timing schedule.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ Procedure timing schedule.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ Procedure timing schedule.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.type = None
        """ Procedure Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProcedureRequest, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProcedureRequest, self).elementProperties()
        js.extend([
            ("asNeededBoolean", "asNeededBoolean", bool, False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False),
            ("bodySite", "bodySite", ProcedureRequestBodySite, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("indication", "indication", codeableconcept.CodeableConcept, True),
            ("notes", "notes", str, True),
            ("orderedOn", "orderedOn", fhirdate.FHIRDate, False),
            ("orderer", "orderer", fhirreference.FHIRReference, False),
            ("performer", "performer", fhirreference.FHIRReference, False),
            ("priority", "priority", str, False),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False),
            ("timingPeriod", "timingPeriod", period.Period, False),
            ("timingTiming", "timingTiming", timing.Timing, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


class ProcedureRequestBodySite(fhirelement.FHIRElement):
    """ Target body sites.
    
    Indicates the sites on the subject's body where the procedure should be
    performed ( i.e. the target sites).
    """
    
    resource_name = "ProcedureRequestBodySite"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.siteCodeableConcept = None
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Target body site.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        super(ProcedureRequestBodySite, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProcedureRequestBodySite, self).elementProperties()
        js.extend([
            ("siteCodeableConcept", "siteCodeableConcept", codeableconcept.CodeableConcept, False),
            ("siteReference", "siteReference", fhirreference.FHIRReference, False),
        ])
        return js

