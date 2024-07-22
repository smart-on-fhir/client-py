#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import medicinalproductauthorization
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class MedicinalProductAuthorizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductAuthorization", js["resourceType"])
        return medicinalproductauthorization.MedicinalProductAuthorization(js)
    
    def testMedicinalProductAuthorization1(self):
        inst = self.instantiate_from("medicinalproductauthorization-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductAuthorization instance")
        self.implMedicinalProductAuthorization1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductAuthorization", js["resourceType"])
        inst2 = medicinalproductauthorization.MedicinalProductAuthorization(js)
        self.implMedicinalProductAuthorization1(inst2)
    
    def implMedicinalProductAuthorization1(self, inst):
        self.assertEqual(inst.country[0].coding[0].code, "EU")
        self.assertEqual(inst.country[0].coding[0].system, "http://ema.europa.eu/example/country")
        self.assertEqual(inst.dataExclusivityPeriod.end.datetime, FHIRDateTime("2020-08-15").datetime)
        self.assertEqual(inst.dataExclusivityPeriod.end.as_json(), "2020-08-15")
        self.assertEqual(inst.dataExclusivityPeriod.start.datetime, FHIRDateTime("2010-08-15").datetime)
        self.assertEqual(inst.dataExclusivityPeriod.start.as_json(), "2010-08-15")
        self.assertEqual(inst.dateOfFirstAuthorization.datetime, FHIRDateTime("2010-08-15").datetime)
        self.assertEqual(inst.dateOfFirstAuthorization.as_json(), "2010-08-15")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://ema.europa.eu/example/marketingAuthorisationNumber")
        self.assertEqual(inst.identifier[0].value, "EU/1/11/999/001")
        self.assertEqual(inst.internationalBirthDate.datetime, FHIRDateTime("2010-08-15").datetime)
        self.assertEqual(inst.internationalBirthDate.as_json(), "2010-08-15")
        self.assertEqual(inst.jurisdictionalAuthorization[0].country.coding[0].code, "NO")
        self.assertEqual(inst.jurisdictionalAuthorization[0].country.coding[0].system, "http://ema.europa.eu/example/countryCode")
        self.assertEqual(inst.jurisdictionalAuthorization[0].id, "1")
        self.assertEqual(inst.jurisdictionalAuthorization[0].identifier[0].system, "http://ema.europa.eu/example/marketingauthorisationnumber")
        self.assertEqual(inst.jurisdictionalAuthorization[0].identifier[0].value, "123-456-789")
        self.assertEqual(inst.jurisdictionalAuthorization[1].country.coding[0].code, "NO")
        self.assertEqual(inst.jurisdictionalAuthorization[1].country.coding[0].system, "http://ema.europa.eu/example/countryCode")
        self.assertEqual(inst.jurisdictionalAuthorization[1].id, "2")
        self.assertEqual(inst.jurisdictionalAuthorization[1].identifier[0].system, "http://ema.europa.eu/example/marketingauthorisationnumber")
        self.assertEqual(inst.jurisdictionalAuthorization[1].identifier[0].value, "123-456-123")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.procedure.application[0].dateDateTime.datetime, FHIRDateTime("2015-08-01").datetime)
        self.assertEqual(inst.procedure.application[0].dateDateTime.as_json(), "2015-08-01")
        self.assertEqual(inst.procedure.application[0].identifier.system, "http://ema.europa.eu/example/applicationidentifier-number")
        self.assertEqual(inst.procedure.application[0].identifier.value, "IA38G")
        self.assertEqual(inst.procedure.application[0].type.coding[0].code, "GroupTypeIAVariationNotification")
        self.assertEqual(inst.procedure.application[0].type.coding[0].system, "http://ema.europa.eu/example/marketingAuthorisationApplicationType")
        self.assertEqual(inst.procedure.datePeriod.end.datetime, FHIRDateTime("2015-08-21").datetime)
        self.assertEqual(inst.procedure.datePeriod.end.as_json(), "2015-08-21")
        self.assertEqual(inst.procedure.datePeriod.start.datetime, FHIRDateTime("2015-08-02").datetime)
        self.assertEqual(inst.procedure.datePeriod.start.as_json(), "2015-08-02")
        self.assertEqual(inst.procedure.identifier.system, "http://ema.europa.eu/example/procedureidentifier-number")
        self.assertEqual(inst.procedure.identifier.value, "EMEA/H/C/009999/IA/0099/G")
        self.assertEqual(inst.procedure.type.coding[0].code, "VariationTypeIA")
        self.assertEqual(inst.procedure.type.coding[0].system, "http://ema.europa.eu/example/marketingAuthorisationProcedureType")
        self.assertEqual(inst.status.coding[0].code, "active")
        self.assertEqual(inst.status.coding[0].system, "http://ema.europa.eu/example/authorisationstatus")
        self.assertEqual(inst.statusDate.datetime, FHIRDateTime("2015-01-14").datetime)
        self.assertEqual(inst.statusDate.as_json(), "2015-01-14")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.validityPeriod.end.datetime, FHIRDateTime("2020-05-20").datetime)
        self.assertEqual(inst.validityPeriod.end.as_json(), "2020-05-20")
        self.assertEqual(inst.validityPeriod.start.datetime, FHIRDateTime("2015-08-16").datetime)
        self.assertEqual(inst.validityPeriod.start.as_json(), "2015-08-16")

