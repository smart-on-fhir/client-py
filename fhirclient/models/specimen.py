#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Specimen) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity


class Specimen(domainresource.DomainResource):
    """ Sample for analysis.
    
    A sample to be used for analysis.
    """
    
    resource_name = "Specimen"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.accessionIdentifier = None
        """ Identifier assigned by the lab.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.collection = None
        """ Collection details.
        Type `SpecimenCollection` (represented as `dict` in JSON). """
        
        self.container = None
        """ Direct container of specimen (tube/slide, etc.).
        List of `SpecimenContainer` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.parent = None
        """ Specimen from which this specimen originated.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.receivedTime = None
        """ The time when specimen was received for processing.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ available | unavailable | unsatisfactory | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Where the specimen came from. This may be from the patient(s) or
        from the environment or a device.
        Type `FHIRReference` referencing `Patient, Group, Device, Substance` (represented as `dict` in JSON). """
        
        self.treatment = None
        """ Treatment and processing step details.
        List of `SpecimenTreatment` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of material that forms the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Specimen, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Specimen, self).elementProperties()
        js.extend([
            ("accessionIdentifier", "accessionIdentifier", identifier.Identifier, False),
            ("collection", "collection", SpecimenCollection, False),
            ("container", "container", SpecimenContainer, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("parent", "parent", fhirreference.FHIRReference, True),
            ("receivedTime", "receivedTime", fhirdate.FHIRDate, False),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("treatment", "treatment", SpecimenTreatment, True),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


class SpecimenCollection(fhirelement.FHIRElement):
    """ Collection details.
    
    Details concerning the specimen collection.
    """
    
    resource_name = "SpecimenCollection"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySite = None
        """ Anatomical collection site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.collectedDateTime = None
        """ Collection time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.collectedPeriod = None
        """ Collection time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.collector = None
        """ Who collected the specimen.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Collector comments.
        List of `str` items. """
        
        self.method = None
        """ Technique used to perform collection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The quantity of specimen collected.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        super(SpecimenCollection, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SpecimenCollection, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False),
            ("collectedDateTime", "collectedDateTime", fhirdate.FHIRDate, False),
            ("collectedPeriod", "collectedPeriod", period.Period, False),
            ("collector", "collector", fhirreference.FHIRReference, False),
            ("comment", "comment", str, True),
            ("method", "method", codeableconcept.CodeableConcept, False),
            ("quantity", "quantity", quantity.Quantity, False),
        ])
        return js


class SpecimenContainer(fhirelement.FHIRElement):
    """ Direct container of specimen (tube/slide, etc.).
    
    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    
    resource_name = "SpecimenContainer"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additiveCodeableConcept = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference = None
        """ Additive associated with container.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """
        
        self.capacity = None
        """ Container volume or size.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.description = None
        """ Textual description of the container.
        Type `str`. """
        
        self.identifier = None
        """ Id for the container.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.specimenQuantity = None
        """ Quantity of specimen within container.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of container directly associated with specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenContainer, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SpecimenContainer, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False),
            ("capacity", "capacity", quantity.Quantity, False),
            ("description", "description", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("specimenQuantity", "specimenQuantity", quantity.Quantity, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


class SpecimenTreatment(fhirelement.FHIRElement):
    """ Treatment and processing step details.
    
    Details concerning treatment and processing steps for the specimen.
    """
    
    resource_name = "SpecimenTreatment"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additive = None
        """ Material used in the processing step.
        List of `FHIRReference` items referencing `Substance` (represented as `dict` in JSON). """
        
        self.description = None
        """ Textual description of procedure.
        Type `str`. """
        
        self.procedure = None
        """ Indicates the treatment or processing step  applied to the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenTreatment, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SpecimenTreatment, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, True),
            ("description", "description", str, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False),
        ])
        return js

