#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import invoice
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class InvoiceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Invoice", js["resourceType"])
        return invoice.Invoice(js)
    
    def testInvoice1(self):
        inst = self.instantiate_from("invoice-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Invoice instance")
        self.implInvoice1(inst)
        
        js = inst.as_json()
        self.assertEqual("Invoice", js["resourceType"])
        inst2 = invoice.Invoice(js)
        self.implInvoice1(inst2)
    
    def implInvoice1(self, inst):
        self.assertEqual(inst.date.datetime, FHIRDateTime("2017-01-25T08:00:00+01:00").datetime)
        self.assertEqual(inst.date.as_json(), "2017-01-25T08:00:00+01:00")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://myHospital.org/Invoices")
        self.assertEqual(inst.identifier[0].value, "654321")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participant[0].role.coding[0].code, "17561000")
        self.assertEqual(inst.participant[0].role.coding[0].display, "Cardiologist")
        self.assertEqual(inst.participant[0].role.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "issued")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Example of Invoice</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.totalGross.currency, "EUR")
        self.assertEqual(inst.totalGross.value, 48)
        self.assertEqual(inst.totalNet.currency, "EUR")
        self.assertEqual(inst.totalNet.value, 40)

