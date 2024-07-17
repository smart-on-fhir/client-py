#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import medicinalproductpackaged
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class MedicinalProductPackagedTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductPackaged", js["resourceType"])
        return medicinalproductpackaged.MedicinalProductPackaged(js)
    
    def testMedicinalProductPackaged1(self):
        inst = self.instantiate_from("medicinalproductpackaged-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductPackaged instance")
        self.implMedicinalProductPackaged1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductPackaged", js["resourceType"])
        inst2 = medicinalproductpackaged.MedicinalProductPackaged(js)
        self.implMedicinalProductPackaged1(inst2)
    
    def implMedicinalProductPackaged1(self, inst):
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.period.end.datetime, FHIRDateTime("2016-06-06").datetime)
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.period.end.as_json(), "2016-06-06")
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.system, "http://ema.europa.eu/example/baid1")
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.value, "AAF5699")
        self.assertEqual(inst.description, "ALU-PVC/PVDC BLISTERS. CARTONS OF 10 FILM-COATED TABLETS. ")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://ema.europa.eu/example/pcid")
        self.assertEqual(inst.identifier[0].value, "{PCID}")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.packageItem[0].material[0].coding[0].code, "PVC")
        self.assertEqual(inst.packageItem[0].material[0].coding[0].system, "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.packageItem[0].material[1].coding[0].code, "PVDC")
        self.assertEqual(inst.packageItem[0].material[1].coding[0].system, "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.packageItem[0].material[2].coding[0].code, "alu")
        self.assertEqual(inst.packageItem[0].material[2].coding[0].system, "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.packageItem[0].packageItem[0].material[0].coding[0].code, "Paperboard")
        self.assertEqual(inst.packageItem[0].packageItem[0].material[0].coding[0].system, "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.height.unit, "mm")
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.height.value, 125)
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.width.unit, "mm")
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.width.value, 45)
        self.assertEqual(inst.packageItem[0].packageItem[0].quantity.unit, "1")
        self.assertEqual(inst.packageItem[0].packageItem[0].quantity.value, 1)
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].period.unit, "a")
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].period.value, 3)
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].code, "Thismedicinalproductdoesnotrequireanyspecialstoragecondition.")
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].system, "http://ema.europa.eu/example/specialprecautionsforstorage")
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].code, "ShelfLifeofPackagedMedicinalProduct")
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].system, "http://ema.europa.eu/example/shelfLifeTypePlaceHolder")
        self.assertEqual(inst.packageItem[0].packageItem[0].type.coding[0].code, "Blister")
        self.assertEqual(inst.packageItem[0].packageItem[0].type.coding[0].system, "http://ema.europa.eu/example/packageitemcontainertype")
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.depth.unit, "mm")
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.depth.value, 23.5)
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.height.unit, "mm")
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.height.value, 50)
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.width.unit, "mm")
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.width.value, 136)
        self.assertEqual(inst.packageItem[0].quantity.unit, "1")
        self.assertEqual(inst.packageItem[0].quantity.value, 1)
        self.assertEqual(inst.packageItem[0].type.coding[0].code, "Carton")
        self.assertEqual(inst.packageItem[0].type.coding[0].system, "http://ema.europa.eu/example/packageitemcontainertype")
        self.assertEqual(inst.text.status, "generated")

