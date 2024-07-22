#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import communication
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class CommunicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Communication", js["resourceType"])
        return communication.Communication(js)
    
    def testCommunication1(self):
        inst = self.instantiate_from("communication-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Communication instance")
        self.implCommunication1(inst)
        
        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication1(inst2)
    
    def implCommunication1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "Alert")
        self.assertEqual(inst.category[0].coding[0].system, "http://acme.org/messagetypes")
        self.assertEqual(inst.category[0].text, "Alert")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.text, "Paging System")
        self.assertEqual(inst.identifier[0].value, "2345678901")
        self.assertEqual(inst.instantiatesUri[0], "http://example.org/hyperkalemia")
        self.assertEqual(inst.medium[0].coding[0].code, "WRITTEN")
        self.assertEqual(inst.medium[0].coding[0].display, "written")
        self.assertEqual(inst.medium[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-ParticipationMode")
        self.assertEqual(inst.medium[0].text, "written")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.payload[0].contentString, "Patient 1 has a very high serum potassium value (7.2 mmol/L on 2014-Dec-12 at 5:55 pm)")
        self.assertEqual(inst.received.datetime, FHIRDateTime("2014-12-12T18:01:11-08:00").datetime)
        self.assertEqual(inst.received.as_json(), "2014-12-12T18:01:11-08:00")
        self.assertEqual(inst.sent.datetime, FHIRDateTime("2014-12-12T18:01:10-08:00").datetime)
        self.assertEqual(inst.sent.as_json(), "2014-12-12T18:01:10-08:00")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Patient has very high serum potassium</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCommunication2(self):
        inst = self.instantiate_from("communication-example-fm-attachment.json")
        self.assertIsNotNone(inst, "Must have instantiated a Communication instance")
        self.implCommunication2(inst)
        
        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication2(inst2)
    
    def implCommunication2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "SolicitedAttachment")
        self.assertEqual(inst.category[0].coding[0].system, "http://acme.org/messagetypes")
        self.assertEqual(inst.id, "fm-attachment")
        self.assertEqual(inst.identifier[0].system, "http://www.providerco.com/communication")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.payload[0].contentAttachment.contentType, "application/pdf")
        self.assertEqual(inst.payload[0].contentAttachment.creation.datetime, FHIRDateTime("2010-02-01T11:50:23-05:00").datetime)
        self.assertEqual(inst.payload[0].contentAttachment.creation.as_json(), "2010-02-01T11:50:23-05:00")
        self.assertEqual(inst.payload[0].contentAttachment.data, "SGVsbG8=")
        self.assertEqual(inst.payload[0].contentAttachment.title, "accident notes 20100201.pdf")
        self.assertEqual(inst.payload[1].contentAttachment.contentType, "application/pdf")
        self.assertEqual(inst.payload[1].contentAttachment.creation.datetime, FHIRDateTime("2010-02-01T10:57:34+01:00").datetime)
        self.assertEqual(inst.payload[1].contentAttachment.creation.as_json(), "2010-02-01T10:57:34+01:00")
        self.assertEqual(inst.payload[1].contentAttachment.hash, "SGVsbG8gdGhlcmU=")
        self.assertEqual(inst.payload[1].contentAttachment.size, 104274)
        self.assertEqual(inst.payload[1].contentAttachment.url, "http://example.org/docs/AB12345")
        self.assertEqual(inst.sent.datetime, FHIRDateTime("2016-06-12T18:01:10-08:00").datetime)
        self.assertEqual(inst.sent.as_json(), "2016-06-12T18:01:10-08:00")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Attachment which is unsolicited</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCommunication3(self):
        inst = self.instantiate_from("communication-example-fm-solicited-attachment.json")
        self.assertIsNotNone(inst, "Must have instantiated a Communication instance")
        self.implCommunication3(inst)
        
        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication3(inst2)
    
    def implCommunication3(self, inst):
        self.assertEqual(inst.category[0].coding[0].code, "SolicitedAttachment")
        self.assertEqual(inst.category[0].coding[0].system, "http://acme.org/messagetypes")
        self.assertEqual(inst.contained[0].id, "provider")
        self.assertEqual(inst.contained[1].id, "payor")
        self.assertEqual(inst.contained[2].id, "request")
        self.assertEqual(inst.id, "fm-solicited")
        self.assertEqual(inst.identifier[0].system, "http://www.providerco.com/communication")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.payload[0].contentAttachment.contentType, "application/pdf")
        self.assertEqual(inst.payload[0].contentAttachment.creation.datetime, FHIRDateTime("2010-02-01T11:50:23-05:00").datetime)
        self.assertEqual(inst.payload[0].contentAttachment.creation.as_json(), "2010-02-01T11:50:23-05:00")
        self.assertEqual(inst.payload[0].contentAttachment.data, "SGVsbG8=")
        self.assertEqual(inst.payload[0].contentAttachment.title, "accident notes 20100201.pdf")
        self.assertEqual(inst.payload[1].contentAttachment.contentType, "application/pdf")
        self.assertEqual(inst.payload[1].contentAttachment.creation.datetime, FHIRDateTime("2010-02-01T10:57:34+01:00").datetime)
        self.assertEqual(inst.payload[1].contentAttachment.creation.as_json(), "2010-02-01T10:57:34+01:00")
        self.assertEqual(inst.payload[1].contentAttachment.hash, "SGVsbG8gdGhlcmU=")
        self.assertEqual(inst.payload[1].contentAttachment.size, 104274)
        self.assertEqual(inst.payload[1].contentAttachment.url, "http://happyvalley.com/docs/AB12345")
        self.assertEqual(inst.sent.datetime, FHIRDateTime("2016-06-12T18:01:10-08:00").datetime)
        self.assertEqual(inst.sent.as_json(), "2016-06-12T18:01:10-08:00")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Attachment in response to a Request</div>")
        self.assertEqual(inst.text.status, "generated")

