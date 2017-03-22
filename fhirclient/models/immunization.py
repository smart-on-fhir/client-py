#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Immunization) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Immunization(domainresource.DomainResource):
    """ Immunization event information.
    
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """
    
    resource_type = "Immunization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ Vaccination administration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.doseQuantity = None
        """ Amount of vaccine administered.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.expirationDate = None
        """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.explanation = None
        """ Administration/non-administration reasons.
        Type `ImmunizationExplanation` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where vaccination occurred.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        """ Vaccine lot number.
        Type `str`. """
        
        self.manufacturer = None
        """ Vaccine manufacturer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.notGiven = None
        """ Flag for whether immunization was given.
        Type `bool`. """
        
        self.note = None
        """ Vaccination notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who was immunized.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.practitioner = None
        """ Who performed event.
        List of `ImmunizationPractitioner` items (represented as `dict` in JSON). """
        
        self.primarySource = None
        """ Indicates context the data was recorded in.
        Type `bool`. """
        
        self.reaction = None
        """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
        
        self.reportOrigin = None
        """ Indicates the source of a secondarily reported record.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.route = None
        """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ completed | entered-in-error.
        Type `str`. """
        
        self.vaccinationProtocol = None
        """ What protocol was followed.
        List of `ImmunizationVaccinationProtocol` items (represented as `dict` in JSON). """
        
        self.vaccineCode = None
        """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Immunization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("explanation", "explanation", ImmunizationExplanation, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("notGiven", "notGiven", bool, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("practitioner", "practitioner", ImmunizationPractitioner, True, None, False),
            ("primarySource", "primarySource", bool, False, None, True),
            ("reaction", "reaction", ImmunizationReaction, True, None, False),
            ("reportOrigin", "reportOrigin", codeableconcept.CodeableConcept, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("vaccinationProtocol", "vaccinationProtocol", ImmunizationVaccinationProtocol, True, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationExplanation(backboneelement.BackboneElement):
    """ Administration/non-administration reasons.
    
    Reasons why a vaccine was or was not administered.
    """
    
    resource_type = "ImmunizationExplanation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reason = None
        """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonNotGiven = None
        """ Why immunization did not occur.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationExplanation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationExplanation, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("reasonNotGiven", "reasonNotGiven", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ImmunizationPractitioner(backboneelement.BackboneElement):
    """ Who performed event.
    
    Indicates who or what performed the event.
    """
    
    resource_type = "ImmunizationPractitioner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Individual who was performing.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.role = None
        """ What type of performance was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationPractitioner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationPractitioner, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.
    
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    
    resource_type = "ImmunizationReaction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When reaction started.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ Additional information on reaction.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        self.reported = None
        """ Indicates self-reported reaction.
        Type `bool`. """
        
        super(ImmunizationReaction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, False, None, False),
            ("reported", "reported", bool, False, None, False),
        ])
        return js


class ImmunizationVaccinationProtocol(backboneelement.BackboneElement):
    """ What protocol was followed.
    
    Contains information about the protocol(s) under which the vaccine was
    administered.
    """
    
    resource_type = "ImmunizationVaccinationProtocol"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ Who is responsible for protocol.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.description = None
        """ Details of vaccine protocol.
        Type `str`. """
        
        self.doseSequence = None
        """ Dose number within series.
        Type `int`. """
        
        self.doseStatus = None
        """ Indicates if dose counts towards immunity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseStatusReason = None
        """ Why dose does (not) count.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.series = None
        """ Name of vaccine series.
        Type `str`. """
        
        self.seriesDoses = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        self.targetDisease = None
        """ Disease immunized against.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationVaccinationProtocol, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationVaccinationProtocol, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("doseSequence", "doseSequence", int, False, None, False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, False, None, True),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, False, None, False),
            ("series", "series", str, False, None, False),
            ("seriesDoses", "seriesDoses", int, False, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, True, None, True),
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
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
