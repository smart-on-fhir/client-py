#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/RelatedPerson) on 2015-07-06.
#  2015, SMART Health IT.


from . import address
from . import attachment
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirreference
from . import humanname
from . import identifier
from . import period


class RelatedPerson(domainresource.DomainResource):
    """ An person that is related to a patient, but who is not a direct target of
    care.
    
    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """
    
    resource_name = "RelatedPerson"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Address where the related person can be contacted or visited.
        Type `Address` (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None
        """ A Human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient this person is related to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period of time that this relationship is considered valid.
        Type `Period` (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.relationship = None
        """ The nature of the relationship.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(RelatedPerson, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(RelatedPerson, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False),
            ("gender", "gender", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("name", "name", humanname.HumanName, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("photo", "photo", attachment.Attachment, True),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js

