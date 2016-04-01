#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/ModuleMetadata) on 2016-04-01.
#  2016, SMART Health IT.


from . import element

class ModuleMetadata(element.Element):
    """ Defines common metadata used by quality artifacts.
    
    The ModuleMetadata structure defines the common metadata elements used by
    quality improvement artifacts. This information includes descriptive and
    topical metadata to enable repository searches, as well as governance and
    evidentiary support information.
    """
    
    resource_name = "ModuleMetadata"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `ModuleMetadataContact` items (represented as `dict` in JSON). """
        
        self.contributor = None
        """ A content contributor.
        List of `ModuleMetadataContributor` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.coverage = None
        """ Describes the context of use for this module.
        List of `ModuleMetadataCoverage` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the module.
        Type `str`. """
        
        self.effectivePeriod = None
        """ The effective date range for the module.
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Logical identifier(s) for the module.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ Last review date for the module.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ A machine-friendly name for the module.
        Type `str`. """
        
        self.publicationDate = None
        """ Publication date for this version of the module.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.purpose = None
        """ Describes the purpose of the module.
        Type `str`. """
        
        self.relatedResource = None
        """ Related resources for the module.
        List of `ModuleMetadataRelatedResource` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | inactive.
        Type `str`. """
        
        self.title = None
        """ A user-friendly title for the module.
        Type `str`. """
        
        self.topic = None
        """ Descriptional topics for the module.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ module | library | decision-support-rule | documentation-template |
        order-set.
        Type `str`. """
        
        self.url = None
        """ Logical URL to reference this module.
        Type `str`. """
        
        self.usage = None
        """ Describes the clinical usage of the module.
        Type `str`. """
        
        self.version = None
        """ The version of the module, if any.
        Type `str`. """
        
        super(ModuleMetadata, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleMetadata, self).elementProperties()
        js.extend([
            ("contact", "contact", ModuleMetadataContact, True, None, False),
            ("contributor", "contributor", ModuleMetadataContributor, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("coverage", "coverage", ModuleMetadataCoverage, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedResource", "relatedResource", ModuleMetadataRelatedResource, True, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class ModuleMetadataContact(element.Element):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "ModuleMetadataContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of an individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for an individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ModuleMetadataContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleMetadataContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ModuleMetadataContributor(element.Element):
    """ A content contributor.
    
    A contributor to the content of the module, including authors, editors,
    reviewers, and endorsers.
    """
    
    resource_name = "ModuleMetadataContributor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details of the contributor.
        List of `ModuleMetadataContributorContact` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name of the contributor.
        Type `str`. """
        
        self.type = None
        """ author | editor | reviewer | endorser.
        Type `str`. """
        
        super(ModuleMetadataContributor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleMetadataContributor, self).elementProperties()
        js.extend([
            ("contact", "contact", ModuleMetadataContributorContact, True, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class ModuleMetadataContributorContact(element.Element):
    """ Contact details of the contributor.
    
    Contacts to assist a user in finding and communicating with the
    contributor.
    """
    
    resource_name = "ModuleMetadataContributorContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of an individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for an individual or contributor.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ModuleMetadataContributorContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleMetadataContributorContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ModuleMetadataCoverage(element.Element):
    """ Describes the context of use for this module.
    
    Specifies various attributes of the patient population for whom and/or
    environment of care in which, the knowledge module is applicable.
    """
    
    resource_name = "ModuleMetadataCoverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.focus = None
        """ patient-gender | patient-age-group | clinical-focus | target-user |
        workflow-setting | workflow-task | clinical-venue | jurisdiction.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Value of the coverage attribute.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ModuleMetadataCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleMetadataCoverage, self).elementProperties()
        js.extend([
            ("focus", "focus", coding.Coding, False, None, True),
            ("value", "value", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ModuleMetadataRelatedResource(element.Element):
    """ Related resources for the module.
    
    Related resources such as additional documentation, justification, or
    bibliographic references.
    """
    
    resource_name = "ModuleMetadataRelatedResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.document = None
        """ The related document.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.resource = None
        """ The related resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.type = None
        """ documentation | justification | citation | predecessor | successor
        | derived-from.
        Type `str`. """
        
        super(ModuleMetadataRelatedResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ModuleMetadataRelatedResource, self).elementProperties()
        js.extend([
            ("document", "document", attachment.Attachment, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
