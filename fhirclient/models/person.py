#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Person) on 2015-09-24.
#  2015, SMART Health IT.


from . import address
from . import attachment
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import humanname
from . import identifier


class Person(domainresource.DomainResource):
    """ A generic person record.
    
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """
    
    resource_name = "Person"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.active = None
        """ This person's record is in active use.
        Type `bool`. """
        
        self.address = None
        """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.birthDate = None
        """ The date on which the person was born.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None
        """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.link = None
        """ Link to a resource that concerns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ The organization that is the custodian of the person record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Person, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend([
            ("active", "active", bool, False),
            ("address", "address", address.Address, True),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False),
            ("gender", "gender", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("link", "link", PersonLink, True),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False),
            ("name", "name", humanname.HumanName, True),
            ("photo", "photo", attachment.Attachment, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class PersonLink(fhirelement.FHIRElement):
    """ Link to a resource that concerns the same actual person.
    """
    
    resource_name = "PersonLink"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.assurance = None
        """ level1 | level2 | level3 | level4.
        Type `str`. """
        
        self.target = None
        """ The resource to which this actual person is associated.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Person` (represented as `dict` in JSON). """
        
        super(PersonLink, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend([
            ("assurance", "assurance", str, False),
            ("target", "target", fhirreference.FHIRReference, False),
        ])
        return js

