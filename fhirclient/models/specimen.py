#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (specimen.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import period
import practitioner
import quantity
import substance


class Specimen(fhirresource.FHIRResource):
    """ Sample for analysis.
    
    Scope and Usage Any material sample:
    
    * taken from a biological entity, living or dead
    * taken from a physical object or the environment
    Biospecimen can contain one or more components including but not limited to
    cellular molecules, cells, tissues, organs, body fluids, embryos, and body
    excretory products (source: NCIt, modified).
    
    The specimen resource covers substances used for diagnostic and
    environmental testing. The focus of the specimen resource is the process
    for gathering, maintaining and processing the specimen as well as where the
    specimen originated. This is distinct from the use of Substance which is
    only used when these other aspects are not relevant.
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
        """ Direct container of specimen (tube/slide, etc).
        List of `SpecimenContainer` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.receivedTime = None
        """ The time when specimen was received for processing.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.source = None
        """ Parent of specimen.
        List of `SpecimenSource` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Where the specimen came from. This may be the patient(s) or from
        the environment or  a device.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.treatment = None
        """ Treatment and processing step details.
        List of `SpecimenTreatment` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of material that forms the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Specimen, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Specimen, self).update_with_json(jsondict)
        if 'accessionIdentifier' in jsondict:
            self.accessionIdentifier = identifier.Identifier.with_json(jsondict['accessionIdentifier'])
        if 'collection' in jsondict:
            self.collection = SpecimenCollection.with_json(jsondict['collection'])
        if 'container' in jsondict:
            self.container = SpecimenContainer.with_json(jsondict['container'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'receivedTime' in jsondict:
            self.receivedTime = fhirdate.FHIRDate.with_json(jsondict['receivedTime'])
        if 'source' in jsondict:
            self.source = SpecimenSource.with_json(jsondict['source'])
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'treatment' in jsondict:
            self.treatment = SpecimenTreatment.with_json(jsondict['treatment'])
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])


class SpecimenSource(fhirelement.FHIRElement):
    """ Parent of specimen.
    
    Parent specimen from which the focal specimen was a component.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.relationship = None
        """ parent | child.
        Type `str`. """
        
        self.target = None
        """ The subject of the relationship.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        super(SpecimenSource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SpecimenSource, self).update_with_json(jsondict)
        if 'relationship' in jsondict:
            self.relationship = jsondict['relationship']
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self, Specimen)


class SpecimenCollection(fhirelement.FHIRElement):
    """ Collection details.
    
    Details concerning the specimen collection.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
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
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.sourceSite = None
        """ Anatomical collection site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenCollection, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SpecimenCollection, self).update_with_json(jsondict)
        if 'collectedDateTime' in jsondict:
            self.collectedDateTime = fhirdate.FHIRDate.with_json(jsondict['collectedDateTime'])
        if 'collectedPeriod' in jsondict:
            self.collectedPeriod = period.Period.with_json(jsondict['collectedPeriod'])
        if 'collector' in jsondict:
            self.collector = fhirreference.FHIRReference.with_json_and_owner(jsondict['collector'], self, practitioner.Practitioner)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'method' in jsondict:
            self.method = codeableconcept.CodeableConcept.with_json(jsondict['method'])
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json(jsondict['quantity'])
        if 'sourceSite' in jsondict:
            self.sourceSite = codeableconcept.CodeableConcept.with_json(jsondict['sourceSite'])


class SpecimenTreatment(fhirelement.FHIRElement):
    """ Treatment and processing step details.
    
    Details concerning treatment and processing steps for the specimen.
    """
    
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
    
    def update_with_json(self, jsondict):
        super(SpecimenTreatment, self).update_with_json(jsondict)
        if 'additive' in jsondict:
            self.additive = fhirreference.FHIRReference.with_json_and_owner(jsondict['additive'], self, substance.Substance)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'procedure' in jsondict:
            self.procedure = codeableconcept.CodeableConcept.with_json(jsondict['procedure'])


class SpecimenContainer(fhirelement.FHIRElement):
    """ Direct container of specimen (tube/slide, etc).
    
    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additive = None
        """ Additive associated with container.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """
        
        self.capacity = None
        """ Container volume or size.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description = None
        """ Textual description of the container.
        Type `str`. """
        
        self.identifier = None
        """ Id for the container.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.specimenQuantity = None
        """ Quantity of specimen within container.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of container directly associated with specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenContainer, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SpecimenContainer, self).update_with_json(jsondict)
        if 'additive' in jsondict:
            self.additive = fhirreference.FHIRReference.with_json_and_owner(jsondict['additive'], self, substance.Substance)
        if 'capacity' in jsondict:
            self.capacity = quantity.Quantity.with_json(jsondict['capacity'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'specimenQuantity' in jsondict:
            self.specimenQuantity = quantity.Quantity.with_json(jsondict['specimenQuantity'])
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])

