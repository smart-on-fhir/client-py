#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import observation
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class ObservationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Observation", js["resourceType"])
        return observation.Observation(js)
    
    def testObservation1(self):
        inst = self.instantiate_from("observation-example-body-temperature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation1(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation1(inst2)
    
    def implObservation1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.category[0].text, "Vital Signs")
        self.assertEqual(inst.code.coding[0].code, "8310-5")
        self.assertEqual(inst.code.coding[0].display, "Body temperature")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Body temperature")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("1999-07-02").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(inst.id, "body-temperature")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/vitalsigns")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "Cel")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "C")
        self.assertEqual(inst.valueQuantity.value, 36.5)
    
    def testObservation2(self):
        inst = self.instantiate_from("observation-example-bgpanel.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation2(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation2(inst2)
    
    def implObservation2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "laboratory")
        self.assertEqual(inst.category[0].coding[0].display, "Laboratory")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.category[0].text, "Laboratory")
        self.assertEqual(inst.code.coding[0].code, "34532-2")
        self.assertEqual(inst.code.coding[0].display, " Blood type and Indirect antibody screen panel - Blood")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Blood Group Panel")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("2018-03-11T16:07:54+00:00").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2018-03-11T16:07:54+00:00")
        self.assertEqual(inst.id, "bgpanel")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation3(self):
        inst = self.instantiate_from("observation-example-f002-excess.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation3(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation3(inst2)
    
    def implObservation3(self, inst):
        self.assertEqual(inst.code.coding[0].code, "11555-0")
        self.assertEqual(inst.code.coding[0].display, "Base excess in Blood by calculation")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.effectivePeriod.end.datetime, FHIRDateTime("2013-04-05T10:30:10+01:00").datetime)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2013-04-05T10:30:10+01:00")
        self.assertEqual(inst.effectivePeriod.start.datetime, FHIRDateTime("2013-04-02T10:30:10+01:00").datetime)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2013-04-02T10:30:10+01:00")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.identifier[0].system, "http://www.bmc.nl/zorgportal/identifiers/observations")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "6324")
        self.assertEqual(inst.interpretation[0].coding[0].code, "H")
        self.assertEqual(inst.interpretation[0].coding[0].display, "High")
        self.assertEqual(inst.interpretation[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2013-04-03T15:30:10+01:00").datetime)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.referenceRange[0].high.code, "mmol/L")
        self.assertEqual(inst.referenceRange[0].high.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[0].high.unit, "mmol/l")
        self.assertEqual(inst.referenceRange[0].high.value, 11.2)
        self.assertEqual(inst.referenceRange[0].low.code, "mmol/L")
        self.assertEqual(inst.referenceRange[0].low.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.referenceRange[0].low.unit, "mmol/l")
        self.assertEqual(inst.referenceRange[0].low.value, 7.1)
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "mmol/L")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "mmol/l")
        self.assertEqual(inst.valueQuantity.value, 12.6)
    
    def testObservation4(self):
        inst = self.instantiate_from("observation-example-heart-rate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation4(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation4(inst2)
    
    def implObservation4(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.category[0].text, "Vital Signs")
        self.assertEqual(inst.code.coding[0].code, "8867-4")
        self.assertEqual(inst.code.coding[0].display, "Heart rate")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Heart rate")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("1999-07-02").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(inst.id, "heart-rate")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/vitalsigns")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "/min")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "beats/minute")
        self.assertEqual(inst.valueQuantity.value, 44)
    
    def testObservation5(self):
        inst = self.instantiate_from("observation-example-secondsmoke.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation5(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation5(inst2)
    
    def implObservation5(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "social-history")
        self.assertEqual(inst.category[0].coding[0].display, "Social History")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.category[0].text, "Social History")
        self.assertEqual(inst.code.coding[0].code, "39243-1")
        self.assertEqual(inst.code.coding[0].display, "Second hand smoke exposure CPHS")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.coding[1].code, "102409004")
        self.assertEqual(inst.code.coding[1].display, "Second hand cigarette smoke (substance)")
        self.assertEqual(inst.code.coding[1].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Second hand smoke exposure")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("2016-05-18T22:33:22Z").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-05-18T22:33:22Z")
        self.assertEqual(inst.id, "secondsmoke")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueCodeableConcept.coding[0].code, "373066001")
        self.assertEqual(inst.valueCodeableConcept.coding[0].display, "Yes (qualifier value)")
        self.assertEqual(inst.valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.valueCodeableConcept.text, "YES")
    
    def testObservation6(self):
        inst = self.instantiate_from("observation-example-bloodpressure-dar.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation6(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation6(inst2)
    
    def implObservation6(self, inst):
        self.assertEqual(inst.bodySite.coding[0].code, "368209003")
        self.assertEqual(inst.bodySite.coding[0].display, "Right arm")
        self.assertEqual(inst.bodySite.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.code.coding[0].code, "85354-9")
        self.assertEqual(inst.code.coding[0].display, "Blood pressure panel with all children optional")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Blood pressure systolic & diastolic")
        self.assertEqual(inst.component[0].code.coding[0].code, "8480-6")
        self.assertEqual(inst.component[0].code.coding[0].display, "Systolic blood pressure")
        self.assertEqual(inst.component[0].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[0].code.coding[1].code, "271649006")
        self.assertEqual(inst.component[0].code.coding[1].display, "Systolic blood pressure")
        self.assertEqual(inst.component[0].code.coding[1].system, "http://snomed.info/sct")
        self.assertEqual(inst.component[0].code.coding[2].code, "bp-s")
        self.assertEqual(inst.component[0].code.coding[2].display, "Systolic Blood pressure")
        self.assertEqual(inst.component[0].code.coding[2].system, "http://acme.org/devices/clinical-codes")
        self.assertEqual(inst.component[0].valueQuantity.code, "mm[Hg]")
        self.assertEqual(inst.component[0].valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.component[0].valueQuantity.unit, "mmHg")
        self.assertEqual(inst.component[0].valueQuantity.value, 107)
        self.assertEqual(inst.component[1].code.coding[0].code, "8462-4")
        self.assertEqual(inst.component[1].code.coding[0].display, "Diastolic blood pressure")
        self.assertEqual(inst.component[1].code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.component[1].dataAbsentReason.coding[0].code, "not-performed")
        self.assertEqual(inst.component[1].dataAbsentReason.coding[0].display, "Not Performed")
        self.assertEqual(inst.component[1].dataAbsentReason.coding[0].system, "http://terminology.hl7.org/CodeSystem/data-absent-reason")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("2012-09-17").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2012-09-17")
        self.assertEqual(inst.id, "blood-pressure-dar")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:uuid:187e0c12-8dd2-67e2-99b2-bf273c878281")
        self.assertEqual(inst.interpretation[0].coding[0].code, "L")
        self.assertEqual(inst.interpretation[0].coding[0].display, "low")
        self.assertEqual(inst.interpretation[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation")
        self.assertEqual(inst.interpretation[0].text, "Below low normal")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/vitalsigns")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation7(self):
        inst = self.instantiate_from("observation-example-respiratory-rate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation7(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation7(inst2)
    
    def implObservation7(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "vital-signs")
        self.assertEqual(inst.category[0].coding[0].display, "Vital Signs")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/observation-category")
        self.assertEqual(inst.category[0].text, "Vital Signs")
        self.assertEqual(inst.code.coding[0].code, "9279-1")
        self.assertEqual(inst.code.coding[0].display, "Respiratory rate")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.text, "Respiratory rate")
        self.assertEqual(inst.effectiveDateTime.datetime, FHIRDateTime("1999-07-02").datetime)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(inst.id, "respiratory-rate")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/vitalsigns")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "/min")
        self.assertEqual(inst.valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.valueQuantity.unit, "breaths/minute")
        self.assertEqual(inst.valueQuantity.value, 26)
    
    def testObservation8(self):
        inst = self.instantiate_from("observation-example-f203-bicarbonate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation8(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation8(inst2)
    
    def implObservation8(self, inst):
        self.assertEqual(inst.code.coding[0].code, "1963-8")
        self.assertEqual(inst.code.coding[0].display, "Bicarbonate [Moles/?volume] in Serum")
        self.assertEqual(inst.code.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.code.coding[1].code, "365722008")
        self.assertEqual(inst.code.coding[1].display, "Bicarbonate level")
        self.assertEqual(inst.code.coding[1].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.identifier[0].system, "https://intranet.aumc.nl/labvalues")
        self.assertEqual(inst.identifier[0].value, "1304-03720-Bicarbonate")
        self.assertEqual(inst.interpretation[0].coding[0].code, "166698001")
        self.assertEqual(inst.interpretation[0].coding[0].display, "Serum bicarbonate level normal")
        self.assertEqual(inst.interpretation[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.interpretation[0].coding[1].code, "N")
        self.assertEqual(inst.interpretation[0].coding[1].system, "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2013-04-04T14:34:00+01:00").datetime)
        self.assertEqual(inst.issued.as_json(), "2013-04-04T14:34:00+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.method.text, "enzymatic method")
        self.assertEqual(inst.referenceRange[0].high.value, 29)
        self.assertEqual(inst.referenceRange[0].low.value, 22)
        self.assertEqual(inst.referenceRange[0].type.coding[0].code, "normal")
        self.assertEqual(inst.referenceRange[0].type.coding[0].display, "Normal Range")
        self.assertEqual(inst.referenceRange[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/referencerange-meaning")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueQuantity.code, "258813002")
        self.assertEqual(inst.valueQuantity.system, "http://snomed.info/sct")
        self.assertEqual(inst.valueQuantity.unit, "mmol/L")
        self.assertEqual(inst.valueQuantity.value, 28)
    
    def testObservation9(self):
        inst = self.instantiate_from("observation-example-diplotype1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation9(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation9(inst2)
    
    def implObservation9(self, inst):
        self.assertEqual(inst.code.coding[0].code, "363779003")
        self.assertEqual(inst.code.coding[0].display, "Genotype determination")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Diplotype Call")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/observation-geneticsGene")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "2623")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "CYP2C9")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.id, "example-diplotype1")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2013-04-03T15:30:10+01:00").datetime)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "final")
        self.assertEqual(inst.text.status, "generated")
    
    def testObservation10(self):
        inst = self.instantiate_from("observation-example-TPMT-haplotype-one.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation10(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation10(inst2)
    
    def implObservation10(self, inst):
        self.assertEqual(inst.code.coding[0].code, "363779003")
        self.assertEqual(inst.code.coding[0].display, "Genotype determination")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Haplotype Call")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/observation-geneticsGene")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "12014")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "TPMT")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://www.genenames.org")
        self.assertEqual(inst.id, "example-TPMT-haplotype-one")
        self.assertEqual(inst.issued.datetime, FHIRInstant("2013-04-03T15:30:10+01:00").datetime)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "unknown")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.valueCodeableConcept.coding[0].code, "PA166128347")
        self.assertEqual(inst.valueCodeableConcept.coding[0].display, "*1")
        self.assertEqual(inst.valueCodeableConcept.coding[0].system, "http://pharmakb.org")

