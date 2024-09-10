# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DiagnosticReport).
# 2024, SMART Health IT.


from . import domainresource

class DiagnosticReport(domainresource.DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    
    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """
    
    resource_type = "DiagnosticReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ What was requested.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Service category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Name/Code for this diagnostic report.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.conclusion = None
        """ Clinical conclusion (interpretation) of test results.
        Type `str`. """
        self._conclusion = None
        """ Primitive extension for conclusion. Type `FHIRPrimitiveExtension` """
        
        self.conclusionCode = None
        """ Codes for the clinical conclusion of test results.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._conclusionCode = None
        """ Primitive extension for conclusionCode. Type `FHIRPrimitiveExtension` """
        
        self.effectiveDateTime = None
        """ Clinically relevant time/time-period for report.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._effectiveDateTime = None
        """ Primitive extension for effectiveDateTime. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ Clinically relevant time/time-period for report.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Health care event when test ordered.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier for report.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.imagingStudy = None
        """ Reference to full details of imaging associated with the diagnostic
        report.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._imagingStudy = None
        """ Primitive extension for imagingStudy. Type `FHIRPrimitiveExtension` """
        
        self.issued = None
        """ DateTime this version was made.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._issued = None
        """ Primitive extension for issued. Type `FHIRPrimitiveExtension` """
        
        self.media = None
        """ Key images associated with this report.
        List of `DiagnosticReportMedia` items (represented as `dict` in JSON). """
        self._media = None
        """ Primitive extension for media. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Responsible Diagnostic Service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.presentedForm = None
        """ Entire report as issued.
        List of `Attachment` items (represented as `dict` in JSON). """
        self._presentedForm = None
        """ Primitive extension for presentedForm. Type `FHIRPrimitiveExtension` """
        
        self.result = None
        """ Observations.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._result = None
        """ Primitive extension for result. Type `FHIRPrimitiveExtension` """
        
        self.resultsInterpreter = None
        """ Primary result interpreter.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._resultsInterpreter = None
        """ Primitive extension for resultsInterpreter. Type `FHIRPrimitiveExtension` """
        
        self.specimen = None
        """ Specimens this report is based on.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._specimen = None
        """ Primitive extension for specimen. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ registered | partial | preliminary | final +.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ The subject of the report - usually, but not always, the patient.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        super(DiagnosticReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticReport, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("conclusion", "conclusion", str, False, None, False),
            ("_conclusion", "_conclusion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("conclusionCode", "conclusionCode", codeableconcept.CodeableConcept, True, None, False),
            ("_conclusionCode", "_conclusionCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdatetime.FHIRDateTime, False, "effective", False),
            ("_effectiveDateTime", "_effectiveDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, True, None, False),
            ("_imagingStudy", "_imagingStudy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issued", "issued", fhirinstant.FHIRInstant, False, None, False),
            ("_issued", "_issued", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("media", "media", DiagnosticReportMedia, True, None, False),
            ("_media", "_media", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("presentedForm", "presentedForm", attachment.Attachment, True, None, False),
            ("_presentedForm", "_presentedForm", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("result", "result", fhirreference.FHIRReference, True, None, False),
            ("_result", "_result", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resultsInterpreter", "resultsInterpreter", fhirreference.FHIRReference, True, None, False),
            ("_resultsInterpreter", "_resultsInterpreter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("_specimen", "_specimen", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class DiagnosticReportMedia(backboneelement.BackboneElement):
    """ Key images associated with this report.
    
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    
    resource_type = "DiagnosticReportMedia"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Comment about the image (e.g. explanation).
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.link = None
        """ Reference to the image source.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._link = None
        """ Primitive extension for link. Type `FHIRPrimitiveExtension` """
        
        super(DiagnosticReportMedia, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticReportMedia, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("link", "link", fhirreference.FHIRReference, False, None, True),
            ("_link", "_link", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment
from . import codeableconcept
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import identifier
from . import period