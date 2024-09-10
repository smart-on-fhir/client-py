# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DetectedIssue).
# 2024, SMART Health IT.


from . import domainresource

class DetectedIssue(domainresource.DomainResource):
    """ Clinical issue with action.
    
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    
    resource_type = "DetectedIssue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ The provider or device that identified the issue.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Issue Category, e.g. drug-drug, duplicate therapy, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Description and context.
        Type `str`. """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.evidence = None
        """ Supporting evidence.
        List of `DetectedIssueEvidence` items (represented as `dict` in JSON). """
        self._evidence = None
        """ Primitive extension for evidence. Type `FHIRPrimitiveExtension` """
        
        self.identifiedDateTime = None
        """ When identified.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._identifiedDateTime = None
        """ Primitive extension for identifiedDateTime. Type `FHIRPrimitiveExtension` """
        
        self.identifiedPeriod = None
        """ When identified.
        Type `Period` (represented as `dict` in JSON). """
        self._identifiedPeriod = None
        """ Primitive extension for identifiedPeriod. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Unique id for the detected issue.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.implicated = None
        """ Problem resource.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._implicated = None
        """ Primitive extension for implicated. Type `FHIRPrimitiveExtension` """
        
        self.mitigation = None
        """ Step taken to address.
        List of `DetectedIssueMitigation` items (represented as `dict` in JSON). """
        self._mitigation = None
        """ Primitive extension for mitigation. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Associated patient.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.reference = None
        """ Authority for issue.
        Type `str`. """
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        self.severity = None
        """ high | moderate | low.
        Type `str`. """
        self._severity = None
        """ Primitive extension for severity. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ registered | preliminary | final | amended +.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(DetectedIssue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssue, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", str, False, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("evidence", "evidence", DetectedIssueEvidence, True, None, False),
            ("_evidence", "_evidence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifiedDateTime", "identifiedDateTime", fhirdatetime.FHIRDateTime, False, "identified", False),
            ("_identifiedDateTime", "_identifiedDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifiedPeriod", "identifiedPeriod", period.Period, False, "identified", False),
            ("_identifiedPeriod", "_identifiedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("implicated", "implicated", fhirreference.FHIRReference, True, None, False),
            ("_implicated", "_implicated", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mitigation", "mitigation", DetectedIssueMitigation, True, None, False),
            ("_mitigation", "_mitigation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("_severity", "_severity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class DetectedIssueEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.
    
    Supporting evidence or manifestations that provide the basis for
    identifying the detected issue such as a GuidanceResponse or MeasureReport.
    """
    
    resource_type = "DetectedIssueEvidence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Manifestation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Supporting information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        super(DetectedIssueEvidence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssueEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ Step taken to address.
    
    Indicates an action that has been taken or is committed to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """
    
    resource_type = "DetectedIssueMitigation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ What mitigation?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Who is committing?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date committed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        super(DetectedIssueMitigation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssueMitigation, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, True),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period