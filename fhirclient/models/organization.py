# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Organization).
# 2024, SMART Health IT.


from . import domainresource

class Organization(domainresource.DomainResource):
    """ A grouping of people or organizations with a common purpose.
    
    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, payer/insurer, etc.
    """
    
    resource_type = "Organization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether the organization's record is still in active use.
        Type `bool`. """
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.address = None
        """ An address for the organization.
        List of `Address` items (represented as `dict` in JSON). """
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.alias = None
        """ A list of alternate names that the organization is known as, or was
        known as in the past.
        List of `str` items. """
        self._alias = None
        """ Primitive extension for alias. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact for the organization for a certain purpose.
        List of `OrganizationContact` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        organization.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifies this organization  across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name used for the organization.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ The organization of which this organization forms a part.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ A contact detail for the organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Kind of organization.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Organization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Organization, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("_alias", "_alias", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", OrganizationContact, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class OrganizationContact(backboneelement.BackboneElement):
    """ Contact for the organization for a certain purpose.
    """
    
    resource_type = "OrganizationContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ Contact details (telephone, email, etc.)  for a contact.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        super(OrganizationContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrganizationContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", codeableconcept.CodeableConcept, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import address
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import humanname
from . import identifier