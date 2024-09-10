# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Practitioner).
# 2024, SMART Health IT.


from . import domainresource

class Practitioner(domainresource.DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.
    
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """
    
    resource_type = "Practitioner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this practitioner's record is in active use.
        Type `bool`. """
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.address = None
        """ Address(es) of the practitioner that are not role specific
        (typically home address).
        List of `Address` items (represented as `dict` in JSON). """
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.birthDate = None
        """ The date  on which the practitioner was born.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._birthDate = None
        """ Primitive extension for birthDate. Type `FHIRPrimitiveExtension` """
        
        self.communication = None
        """ A language the practitioner can use in patient communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._communication = None
        """ Primitive extension for communication. Type `FHIRPrimitiveExtension` """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        self._gender = None
        """ Primitive extension for gender. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ An identifier for the person as this agent.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ The name(s) associated with the practitioner.
        List of `HumanName` items (represented as `dict` in JSON). """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        self._photo = None
        """ Primitive extension for photo. Type `FHIRPrimitiveExtension` """
        
        self.qualification = None
        """ Certification, licenses, or training pertaining to the provision of
        care.
        List of `PractitionerQualification` items (represented as `dict` in JSON). """
        self._qualification = None
        """ Primitive extension for qualification. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ A contact detail for the practitioner (that apply to all roles).
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        super(Practitioner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Practitioner, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("_birthDate", "_birthDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("communication", "communication", codeableconcept.CodeableConcept, True, None, False),
            ("_communication", "_communication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("_gender", "_gender", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("_photo", "_photo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("qualification", "qualification", PractitionerQualification, True, None, False),
            ("_qualification", "_qualification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class PractitionerQualification(backboneelement.BackboneElement):
    """ Certification, licenses, or training pertaining to the provision of care.
    
    The official certifications, training, and licenses that authorize or
    otherwise pertain to the provision of care by the practitioner.  For
    example, a medical license issued by a medical board authorizing the
    practitioner to practice medicine within a certian locality.
    """
    
    resource_type = "PractitionerQualification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Coded representation of the qualification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ An identifier for this qualification for the practitioner.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.issuer = None
        """ Organization that regulates and issues the qualification.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._issuer = None
        """ Primitive extension for issuer. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Period during which the qualification is valid.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        super(PractitionerQualification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerQualification, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False),
            ("_issuer", "_issuer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period