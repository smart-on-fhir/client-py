#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Practitioner) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Practitioner(domainresource.DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.
    
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """
    
    resource_name = "Practitioner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this practitioner's record is in active use.
        Type `bool`. """
        
        self.address = None
        """ Where practitioner can be found/visited.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.birthDate = None
        """ The date  on which the practitioner was born.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.communication = None
        """ A language the practitioner is able to use in patient communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None
        """ A identifier for the person as this agent.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.practitionerRole = None
        """ Roles/organizations the practitioner is associated with.
        List of `PractitionerPractitionerRole` items (represented as `dict` in JSON). """
        
        self.qualification = None
        """ Qualifications obtained by training and certification.
        List of `PractitionerQualification` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the practitioner.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Practitioner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Practitioner, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("communication", "communication", codeableconcept.CodeableConcept, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("practitionerRole", "practitionerRole", PractitionerPractitionerRole, True, None, False),
            ("qualification", "qualification", PractitionerQualification, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class PractitionerPractitionerRole(backboneelement.BackboneElement):
    """ Roles/organizations the practitioner is associated with.
    
    The list of roles/organizations that the practitioner is associated with.
    """
    
    resource_name = "PractitionerPractitionerRole"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.healthcareService = None
        """ The list of healthcare services that this worker provides for this
        role's Organization/Location(s).
        List of `FHIRReference` items referencing `HealthcareService` (represented as `dict` in JSON). """
        
        self.location = None
        """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization where the roles are performed.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """
        
        self.role = None
        """ Roles which this practitioner may perform.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(PractitionerPractitionerRole, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerPractitionerRole, self).elementProperties()
        js.extend([
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class PractitionerQualification(backboneelement.BackboneElement):
    """ Qualifications obtained by training and certification.
    """
    
    resource_name = "PractitionerQualification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Coded representation of the qualification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ An identifier for this qualification for the practitioner.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issuer = None
        """ Organization that regulates and issues the qualification.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period during which the qualification is valid.
        Type `Period` (represented as `dict` in JSON). """
        
        super(PractitionerQualification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerQualification, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period
