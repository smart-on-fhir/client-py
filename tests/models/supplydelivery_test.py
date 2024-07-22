#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import supplydelivery
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class SupplyDeliveryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SupplyDelivery", js["resourceType"])
        return supplydelivery.SupplyDelivery(js)
    
    def testSupplyDelivery1(self):
        inst = self.instantiate_from("supplydelivery-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a SupplyDelivery instance")
        self.implSupplyDelivery1(inst)
        
        js = inst.as_json()
        self.assertEqual("SupplyDelivery", js["resourceType"])
        inst2 = supplydelivery.SupplyDelivery(js)
        self.implSupplyDelivery1(inst2)
    
    def implSupplyDelivery1(self, inst):
        self.assertEqual(inst.id, "simpledelivery")
        self.assertEqual(inst.identifier[0].value, "Order10284")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurrenceDateTime.datetime, FHIRDateTime("2016-12-31").datetime)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-12-31")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.suppliedItem.itemCodeableConcept.coding[0].code, "BlueTubes")
        self.assertEqual(inst.suppliedItem.itemCodeableConcept.coding[0].display, "Blood collect tubes blue cap")
        self.assertEqual(inst.suppliedItem.quantity.value, 10)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "device")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/supply-item-type")
        self.assertEqual(inst.type.text, "Blood collect tubes blue cap")
    
    def testSupplyDelivery2(self):
        inst = self.instantiate_from("supplydelivery-example-pumpdelivery.json")
        self.assertIsNotNone(inst, "Must have instantiated a SupplyDelivery instance")
        self.implSupplyDelivery2(inst)
        
        js = inst.as_json()
        self.assertEqual("SupplyDelivery", js["resourceType"])
        inst2 = supplydelivery.SupplyDelivery(js)
        self.implSupplyDelivery2(inst2)
    
    def implSupplyDelivery2(self, inst):
        self.assertEqual(inst.id, "pumpdelivery")
        self.assertEqual(inst.identifier[0].value, "98398459409")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "in-progress")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

