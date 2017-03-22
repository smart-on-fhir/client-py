#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Patient) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Patient(domainresource.DomainResource):
    """ Information about an individual or animal receiving health care services.
    
    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """
    
    resource_type = "Patient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this patient's record is in active use.
        Type `bool`. """
        
        self.address = None
        """ Addresses for the individual.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.animal = None
        """ This patient is known to be an animal (non-human).
        Type `PatientAnimal` (represented as `dict` in JSON). """
        
        self.birthDate = None
        """ The date of birth for the individual.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.communication = None
        """ A list of Languages which may be used to communicate with the
        patient about his or her health.
        List of `PatientCommunication` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ A contact party (e.g. guardian, partner, friend) for the patient.
        List of `PatientContact` items (represented as `dict` in JSON). """
        
        self.deceasedBoolean = None
        """ Indicates if the individual is deceased or not.
        Type `bool`. """
        
        self.deceasedDateTime = None
        """ Indicates if the individual is deceased or not.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.generalPractitioner = None
        """ Patient's nominated primary care provider.
        List of `FHIRReference` items referencing `Organization, Practitioner` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ An identifier for this patient.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.link = None
        """ Link to another patient resource that concerns the same actual
        person.
        List of `PatientLink` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization that is the custodian of the patient record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.maritalStatus = None
        """ Marital (civil) status of a patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.multipleBirthBoolean = None
        """ Whether patient is part of a multiple birth.
        Type `bool`. """
        
        self.multipleBirthInteger = None
        """ Whether patient is part of a multiple birth.
        Type `int`. """
        
        self.name = None
        """ A name associated with the patient.
        List of `HumanName` items (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the patient.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the individual.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Patient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Patient, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("animal", "animal", PatientAnimal, False, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("communication", "communication", PatientCommunication, True, None, False),
            ("contact", "contact", PatientContact, True, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedDateTime", "deceasedDateTime", fhirdate.FHIRDate, False, "deceased", False),
            ("gender", "gender", str, False, None, False),
            ("generalPractitioner", "generalPractitioner", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("link", "link", PatientLink, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("maritalStatus", "maritalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("multipleBirthBoolean", "multipleBirthBoolean", bool, False, "multipleBirth", False),
            ("multipleBirthInteger", "multipleBirthInteger", int, False, "multipleBirth", False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class PatientAnimal(backboneelement.BackboneElement):
    """ This patient is known to be an animal (non-human).
    
    This patient is known to be an animal.
    """
    
    resource_type = "PatientAnimal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.breed = None
        """ E.g. Poodle, Angus.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.genderStatus = None
        """ E.g. Neutered, Intact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.species = None
        """ E.g. Dog, Cow.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PatientAnimal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientAnimal, self).elementProperties()
        js.extend([
            ("breed", "breed", codeableconcept.CodeableConcept, False, None, False),
            ("genderStatus", "genderStatus", codeableconcept.CodeableConcept, False, None, False),
            ("species", "species", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class PatientCommunication(backboneelement.BackboneElement):
    """ A list of Languages which may be used to communicate with the patient about
    his or her health.
    
    Languages which may be used to communicate with the patient about his or
    her health.
    """
    
    resource_type = "PatientCommunication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ The language which can be used to communicate with the patient
        about his or her health.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.preferred = None
        """ Language preference indicator.
        Type `bool`. """
        
        super(PatientCommunication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
        ])
        return js


class PatientContact(backboneelement.BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """
    
    resource_type = "PatientContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Address for the contact person.
        Type `Address` (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.name = None
        """ A name associated with the contact person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Organization that is associated with the contact.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period during which this contact person or organization is
        valid to be contacted relating to this patient.
        Type `Period` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ The kind of relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(PatientContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class PatientLink(backboneelement.BackboneElement):
    """ Link to another patient resource that concerns the same actual person.
    
    Link to another patient resource that concerns the same actual patient.
    """
    
    resource_type = "PatientLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.other = None
        """ The other patient or related person resource that the link refers
        to.
        Type `FHIRReference` referencing `Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.type = None
        """ replaced-by | replaces | refer | seealso - type of link.
        Type `str`. """
        
        super(PatientLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend([
            ("other", "other", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
