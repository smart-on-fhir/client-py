#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import medicinalproductpharmaceutical
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class MedicinalProductPharmaceuticalTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductPharmaceutical", js["resourceType"])
        return medicinalproductpharmaceutical.MedicinalProductPharmaceutical(js)
    
    def testMedicinalProductPharmaceutical1(self):
        inst = self.instantiate_from("medicinalproductpharmaceutical-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductPharmaceutical instance")
        self.implMedicinalProductPharmaceutical1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductPharmaceutical", js["resourceType"])
        inst2 = medicinalproductpharmaceutical.MedicinalProductPharmaceutical(js)
        self.implMedicinalProductPharmaceutical1(inst2)
    
    def implMedicinalProductPharmaceutical1(self, inst):
        self.assertEqual(inst.administrableDoseForm.coding[0].code, "Film-coatedtablet")
        self.assertEqual(inst.administrableDoseForm.coding[0].system, "http://ema.europa.eu/example/administrabledoseform")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://ema.europa.eu/example/phpididentifiersets")
        self.assertEqual(inst.identifier[0].value, "{PhPID}")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].code, "OralUse")
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].system, "http://ema.europa.eu/example/routeofadministration")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.unitOfPresentation.coding[0].code, "Tablet")
        self.assertEqual(inst.unitOfPresentation.coding[0].system, "http://ema.europa.eu/example/unitofpresentation")

