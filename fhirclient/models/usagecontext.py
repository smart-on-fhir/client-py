#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 (http://hl7.org/fhir/StructureDefinition/UsageContext) on 2016-08-31.
#  2016, SMART Health IT.


from . import element

class UsageContext(element.Element):
    """ Describes the context of use for a module.
    
    Specifies clinical metadata that can be used to retrieve, index and/or
    categorize the knowledge artifact. This metadata can either be specific to
    the applicable population (e.g., age category, DRG) or the specific context
    of care (e.g., venue, care setting, provider of care).
    """
    
    resource_name = "UsageContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.clinicalFocus = None
        """ Clinical concepts addressed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.clinicalVenue = None
        """ Applicable venue.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.patientAgeGroup = None
        """ Demographic category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.patientGender = None
        """ Patient gender.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.targetUser = None
        """ Target user type.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.workflowSetting = None
        """ Workflow setting.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.workflowTask = None
        """ Clinical task context.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(UsageContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(UsageContext, self).elementProperties()
        js.extend([
            ("clinicalFocus", "clinicalFocus", codeableconcept.CodeableConcept, True, None, False),
            ("clinicalVenue", "clinicalVenue", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("patientAgeGroup", "patientAgeGroup", codeableconcept.CodeableConcept, True, None, False),
            ("patientGender", "patientGender", codeableconcept.CodeableConcept, True, None, False),
            ("targetUser", "targetUser", codeableconcept.CodeableConcept, True, None, False),
            ("workflowSetting", "workflowSetting", codeableconcept.CodeableConcept, True, None, False),
            ("workflowTask", "workflowTask", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import codeableconcept
