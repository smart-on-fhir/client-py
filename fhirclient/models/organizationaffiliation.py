# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation).
# 2024, SMART Health IT.


from . import domainresource

class OrganizationAffiliation(domainresource.DomainResource):
    """ Defines an affiliation/assotiation/relationship between 2 distinct
    oganizations, that is not a part-of relationship/sub-division relationship.
    """
    
    resource_type = "OrganizationAffiliation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this organization affiliation record is in active use.
        Type `bool`. """
        
        self.code = None
        """ Definition of the role the participatingOrganization plays.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ Technical endpoints providing access to services operated for this
        role.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.healthcareService = None
        """ Healthcare services provided through the role.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifiers that are specific to this role.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ The location(s) at which the role occurs.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.network = None
        """ Health insurance provider network in which the
        participatingOrganization provides the role's services (if defined)
        at the indicated locations (if defined).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Organization where the role is available.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.participatingOrganization = None
        """ Organization that provides/performs the role (e.g. providing
        services or is a member of).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period during which the participatingOrganization is affiliated
        with the primary organization.
        Type `Period` (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Specific specialty of the participatingOrganization in the context
        of the role.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact details at the participatingOrganization relevant to this
        Affiliation.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(OrganizationAffiliation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrganizationAffiliation, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("participatingOrganization", "participatingOrganization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
from . import period
