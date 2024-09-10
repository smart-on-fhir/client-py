# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Person).
# 2024, SMART Health IT.


from . import domainresource

class Person(domainresource.DomainResource):
    """ A generic person record.
    
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """
    
    resource_type = "Person"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ This person's record is in active use.
        Type `bool`. """
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.address = None
        """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.birthDate = None
        """ The date on which the person was born.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._birthDate = None
        """ Primitive extension for birthDate. Type `FHIRPrimitiveExtension` """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        self._gender = None
        """ Primitive extension for gender. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.link = None
        """ Link to a resource that concerns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """
        self._link = None
        """ Primitive extension for link. Type `FHIRPrimitiveExtension` """
        
        self.managingOrganization = None
        """ The organization that is the custodian of the person record.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._managingOrganization = None
        """ Primitive extension for managingOrganization. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.photo = None
        """ Image of the person.
        Type `Attachment` (represented as `dict` in JSON). """
        self._photo = None
        """ Primitive extension for photo. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        super(Person, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("_birthDate", "_birthDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("_gender", "_gender", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("link", "link", PersonLink, True, None, False),
            ("_link", "_link", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("_managingOrganization", "_managingOrganization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("_photo", "_photo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """
    
    resource_type = "PersonLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assurance = None
        """ level1 | level2 | level3 | level4.
        Type `str`. """
        self._assurance = None
        """ Primitive extension for assurance. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ The resource to which this actual person is associated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        super(PersonLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend([
            ("assurance", "assurance", str, False, None, False),
            ("_assurance", "_assurance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, True),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import address
from . import attachment
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier