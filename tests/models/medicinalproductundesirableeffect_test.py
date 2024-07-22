#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import medicinalproductundesirableeffect
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class MedicinalProductUndesirableEffectTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductUndesirableEffect", js["resourceType"])
        return medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(js)
    
    def testMedicinalProductUndesirableEffect1(self):
        inst = self.instantiate_from("medicinalproductundesirableeffect-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductUndesirableEffect instance")
        self.implMedicinalProductUndesirableEffect1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductUndesirableEffect", js["resourceType"])
        inst2 = medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(js)
        self.implMedicinalProductUndesirableEffect1(inst2)
    
    def implMedicinalProductUndesirableEffect1(self, inst):
        self.assertEqual(inst.classification.coding[0].code, "Bloodandlymphaticsystemdisorders")
        self.assertEqual(inst.classification.coding[0].system, "http://ema.europa.eu/example/symptom-condition-effectclassification")
        self.assertEqual(inst.frequencyOfOccurrence.coding[0].code, "Common")
        self.assertEqual(inst.frequencyOfOccurrence.coding[0].system, "http://ema.europa.eu/example/frequencyofoccurrence")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.symptomConditionEffect.coding[0].code, "Anaemia")
        self.assertEqual(inst.symptomConditionEffect.coding[0].system, "http://ema.europa.eu/example/undesirableeffectassymptom-condition-effect")
        self.assertEqual(inst.symptomConditionEffect.text, "Prevention of\\nVTE in adult\\npatients who have\\nundergone\\nelective hip or\\nknee replacement\\nsurgery (VTEp)")
        self.assertEqual(inst.text.status, "generated")

