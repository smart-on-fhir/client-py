#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/ProcedureRequest) on 2015-09-24.
#  2015, SMART Health IT.


from . import annotation
from . import codeableconcept
from . import domainresource
from . import fhirdate
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
        """ Preconditions for procedure.
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Preconditions for procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ What part of body to perform on.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ What procedure to perform.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter request created during.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier for the request.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Additional information about desired procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.orderedOn = None
        """ When request was created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.orderer = None
        """ Who made request.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson, Device` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who should perform the procedure.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | stat | asap.
        Type `str`. """
        
        self.reasonCodeableConcept = None
        """ Why procedure should occur.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why procedure should occur.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.scheduledDateTime = None
        """ When procedure should occur.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.scheduledPeriod = None
        """ When procedure should occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scheduledTiming = None
        """ When procedure should occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | draft | requested | received | accepted | in-progress |
        completed | suspended | rejected | aborted.
        Type `str`. """
        
        self.subject = None
        """ Who the procedure should be done to.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        super(ProcedureRequest, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProcedureRequest, self).elementProperties()
        js.extend([
            ("asNeededBoolean", "asNeededBoolean", bool, False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True),
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("notes", "notes", annotation.Annotation, True),
            ("orderedOn", "orderedOn", fhirdate.FHIRDate, False),
            ("orderer", "orderer", fhirreference.FHIRReference, False),
            ("performer", "performer", fhirreference.FHIRReference, False),
            ("priority", "priority", str, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False),
            ("scheduledDateTime", "scheduledDateTime", fhirdate.FHIRDate, False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False),
            ("scheduledTiming", "scheduledTiming", timing.Timing, False),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
        ])
        return js

