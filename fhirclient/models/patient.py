# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Patient).
# 2024, SMART Health IT.


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
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.address = None
        """ An address for the individual.
        List of `Address` items (represented as `dict` in JSON). """
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.birthDate = None
        """ The date of birth for the individual.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._birthDate = None
        """ Primitive extension for birthDate. Type `FHIRPrimitiveExtension` """
        
        self.communication = None
        """ A language which may be used to communicate with the patient about
        his or her health.
        List of `PatientCommunication` items (represented as `dict` in JSON). """
        self._communication = None
        """ Primitive extension for communication. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ A contact party (e.g. guardian, partner, friend) for the patient.
        List of `PatientContact` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.deceasedBoolean = None
        """ Indicates if the individual is deceased or not.
        Type `bool`. """
        self._deceasedBoolean = None
        """ Primitive extension for deceasedBoolean. Type `FHIRPrimitiveExtension` """
        
        self.deceasedDateTime = None
        """ Indicates if the individual is deceased or not.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._deceasedDateTime = None
        """ Primitive extension for deceasedDateTime. Type `FHIRPrimitiveExtension` """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        self._gender = None
        """ Primitive extension for gender. Type `FHIRPrimitiveExtension` """
        
        self.generalPractitioner = None
        """ Patient's nominated primary care provider.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._generalPractitioner = None
        """ Primitive extension for generalPractitioner. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ An identifier for this patient.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.link = None
        """ Link to another patient resource that concerns the same actual
        person.
        List of `PatientLink` items (represented as `dict` in JSON). """
        self._link = None
        """ Primitive extension for link. Type `FHIRPrimitiveExtension` """
        
        self.managingOrganization = None
        """ Organization that is the custodian of the patient record.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._managingOrganization = None
        """ Primitive extension for managingOrganization. Type `FHIRPrimitiveExtension` """
        
        self.maritalStatus = None
        """ Marital (civil) status of a patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._maritalStatus = None
        """ Primitive extension for maritalStatus. Type `FHIRPrimitiveExtension` """
        
        self.multipleBirthBoolean = None
        """ Whether patient is part of a multiple birth.
        Type `bool`. """
        self._multipleBirthBoolean = None
        """ Primitive extension for multipleBirthBoolean. Type `FHIRPrimitiveExtension` """
        
        self.multipleBirthInteger = None
        """ Whether patient is part of a multiple birth.
        Type `int`. """
        self._multipleBirthInteger = None
        """ Primitive extension for multipleBirthInteger. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ A name associated with the patient.
        List of `HumanName` items (represented as `dict` in JSON). """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.photo = None
        """ Image of the patient.
        List of `Attachment` items (represented as `dict` in JSON). """
        self._photo = None
        """ Primitive extension for photo. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ A contact detail for the individual.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        super(Patient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Patient, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("_birthDate", "_birthDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("communication", "communication", PatientCommunication, True, None, False),
            ("_communication", "_communication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", PatientContact, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("_deceasedBoolean", "_deceasedBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deceasedDateTime", "deceasedDateTime", fhirdatetime.FHIRDateTime, False, "deceased", False),
            ("_deceasedDateTime", "_deceasedDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("_gender", "_gender", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("generalPractitioner", "generalPractitioner", fhirreference.FHIRReference, True, None, False),
            ("_generalPractitioner", "_generalPractitioner", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("link", "link", PatientLink, True, None, False),
            ("_link", "_link", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("_managingOrganization", "_managingOrganization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maritalStatus", "maritalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("_maritalStatus", "_maritalStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("multipleBirthBoolean", "multipleBirthBoolean", bool, False, "multipleBirth", False),
            ("_multipleBirthBoolean", "_multipleBirthBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("multipleBirthInteger", "multipleBirthInteger", int, False, "multipleBirth", False),
            ("_multipleBirthInteger", "_multipleBirthInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("_photo", "_photo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class PatientCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with the patient about his or
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
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        self.preferred = None
        """ Language preference indicator.
        Type `bool`. """
        self._preferred = None
        """ Primitive extension for preferred. Type `FHIRPrimitiveExtension` """
        
        super(PatientCommunication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("_preferred", "_preferred", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        self._gender = None
        """ Primitive extension for gender. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ A name associated with the contact person.
        Type `HumanName` (represented as `dict` in JSON). """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.organization = None
        """ Organization that is associated with the contact.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._organization = None
        """ Primitive extension for organization. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ The period during which this contact person or organization is
        valid to be contacted relating to this patient.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.relationship = None
        """ The kind of relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._relationship = None
        """ Primitive extension for relationship. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        super(PatientContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("_gender", "_gender", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("_organization", "_organization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._other = None
        """ Primitive extension for other. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ replaced-by | replaces | refer | seealso.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(PatientLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend([
            ("other", "other", fhirreference.FHIRReference, False, None, True),
            ("_other", "_other", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import humanname
from . import identifier
from . import period