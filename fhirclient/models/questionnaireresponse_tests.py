#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import questionnaireresponse
from .fhirdate import FHIRDate


class QuestionnaireResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("QuestionnaireResponse", js["resourceType"])
        return questionnaireresponse.QuestionnaireResponse(js)
    
    def testQuestionnaireResponse1(self):
        inst = self.instantiate_from("questionnaireresponse-example-bluebook.json")
        self.assertIsNotNone(inst, "Must have instantiated a QuestionnaireResponse instance")
        self.implQuestionnaireResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("QuestionnaireResponse", js["resourceType"])
        inst2 = questionnaireresponse.QuestionnaireResponse(js)
        self.implQuestionnaireResponse1(inst2)
    
    def implQuestionnaireResponse1(self, inst):
        self.assertEqual(inst.authored.date, FHIRDate("2013-02-19T14:15:00+10:00").date)
        self.assertEqual(inst.authored.as_json(), "2013-02-19T14:15:00+10:00")
        self.assertEqual(inst.group.group[0].group[0].question[0].answer[0].valueString, "Cathy Jones")
        self.assertEqual(inst.group.group[0].group[0].question[0].linkId, "nameOfChild")
        self.assertEqual(inst.group.group[0].group[0].question[0].text, "Name of child")
        self.assertEqual(inst.group.group[0].group[0].question[1].answer[0].valueCoding.code, "f")
        self.assertEqual(inst.group.group[0].group[0].question[1].linkId, "sex")
        self.assertEqual(inst.group.group[0].group[0].question[1].text, "Sex")
        self.assertEqual(inst.group.group[0].group[1].linkId, "neonatalInformation")
        self.assertEqual(inst.group.group[0].group[1].question[0].answer[0].valueDecimal, 3.25)
        self.assertEqual(inst.group.group[0].group[1].question[0].linkId, "birthWeight")
        self.assertEqual(inst.group.group[0].group[1].question[0].text, "Birth weight (kg)")
        self.assertEqual(inst.group.group[0].group[1].question[1].answer[0].valueDecimal, 44.3)
        self.assertEqual(inst.group.group[0].group[1].question[1].linkId, "birthLength")
        self.assertEqual(inst.group.group[0].group[1].question[1].text, "Birth length (cm)")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].extension[0].url, "http://example.org/Profile/questionnaire#visibilityCondition")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].extension[0].valueString, "HAS_VALUE(../choice/code) AND NEQ(../choice/code,'NO')")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].linkId, "vitaminKgivenDoses")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].question[0].answer[0].valueDate.date, FHIRDate("1972-11-30").date)
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].question[0].answer[0].valueDate.as_json(), "1972-11-30")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].question[0].linkId, "vitaminiKDose1")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].question[0].text, "1st dose")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].question[1].answer[0].valueDate.date, FHIRDate("1972-12-11").date)
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].question[1].answer[0].valueDate.as_json(), "1972-12-11")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].question[1].linkId, "vitaminiKDose2")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].group[0].question[1].text, "2nd dose")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].valueCoding.code, "INJECTION")
        self.assertEqual(inst.group.group[0].group[1].question[2].linkId, "vitaminKgiven")
        self.assertEqual(inst.group.group[0].group[1].question[2].text, "Vitamin K given")
        self.assertEqual(inst.group.group[0].group[1].question[3].answer[0].group[0].linkId, "hepBgivenDate")
        self.assertEqual(inst.group.group[0].group[1].question[3].answer[0].group[0].question[0].answer[0].valueDate.date, FHIRDate("1972-12-04").date)
        self.assertEqual(inst.group.group[0].group[1].question[3].answer[0].group[0].question[0].answer[0].valueDate.as_json(), "1972-12-04")
        self.assertEqual(inst.group.group[0].group[1].question[3].answer[0].group[0].question[0].text, "Date given")
        self.assertTrue(inst.group.group[0].group[1].question[3].answer[0].valueBoolean)
        self.assertEqual(inst.group.group[0].group[1].question[3].linkId, "hepBgiven")
        self.assertEqual(inst.group.group[0].group[1].question[3].text, "Hep B given y / n")
        self.assertEqual(inst.group.group[0].group[1].question[4].answer[0].valueString, "Already able to speak Chinese")
        self.assertEqual(inst.group.group[0].group[1].question[4].linkId, "abnormalitiesAtBirth")
        self.assertEqual(inst.group.group[0].group[1].question[4].text, "Abnormalities noted at birth")
        self.assertEqual(inst.group.group[0].group[1].title, "Neonatal Information")
        self.assertEqual(inst.group.group[0].linkId, "birthDetails")
        self.assertEqual(inst.group.group[0].title, "Birth details - To be completed by health professional")
        self.assertEqual(inst.group.linkId, "PHR")
        self.assertEqual(inst.group.title, "NSW Government My Personal Health Record, january 2013")
        self.assertEqual(inst.id, "bb")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testQuestionnaireResponse2(self):
        inst = self.instantiate_from("questionnaireresponse-example-f201-lifelines.json")
        self.assertIsNotNone(inst, "Must have instantiated a QuestionnaireResponse instance")
        self.implQuestionnaireResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("QuestionnaireResponse", js["resourceType"])
        inst2 = questionnaireresponse.QuestionnaireResponse(js)
        self.implQuestionnaireResponse2(inst2)
    
    def implQuestionnaireResponse2(self, inst):
        self.assertEqual(inst.authored.date, FHIRDate("2013-06-18T00:00:00+01:00").date)
        self.assertEqual(inst.authored.as_json(), "2013-06-18T00:00:00+01:00")
        self.assertEqual(inst.group.group[0].linkId, "1")
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueString, "I am allergic to house dust")
        self.assertEqual(inst.group.group[0].question[0].linkId, "1.1")
        self.assertEqual(inst.group.group[0].question[0].text, "Do you have allergies?")
        self.assertEqual(inst.group.group[1].linkId, "2")
        self.assertEqual(inst.group.group[1].question[0].answer[0].valueString, "Male")
        self.assertEqual(inst.group.group[1].question[0].linkId, "2.1")
        self.assertEqual(inst.group.group[1].question[0].text, "What is your gender?")
        self.assertEqual(inst.group.group[1].question[1].answer[0].valueDate.date, FHIRDate("1960-03-13").date)
        self.assertEqual(inst.group.group[1].question[1].answer[0].valueDate.as_json(), "1960-03-13")
        self.assertEqual(inst.group.group[1].question[1].linkId, "2.2")
        self.assertEqual(inst.group.group[1].question[1].text, "What is your date of birth?")
        self.assertEqual(inst.group.group[1].question[2].answer[0].valueString, "The Netherlands")
        self.assertEqual(inst.group.group[1].question[2].linkId, "2.3")
        self.assertEqual(inst.group.group[1].question[2].text, "What is your country of birth?")
        self.assertEqual(inst.group.group[1].question[3].answer[0].valueString, "married")
        self.assertEqual(inst.group.group[1].question[3].linkId, "2.4")
        self.assertEqual(inst.group.group[1].question[3].text, "What is your marital status?")
        self.assertEqual(inst.group.group[1].title, "General questions")
        self.assertEqual(inst.group.group[2].linkId, "3")
        self.assertEqual(inst.group.group[2].question[0].answer[0].valueString, "No")
        self.assertEqual(inst.group.group[2].question[0].linkId, "3.1")
        self.assertEqual(inst.group.group[2].question[0].text, "Do you smoke?")
        self.assertEqual(inst.group.group[2].question[1].answer[0].valueString, "No, but I used to drink")
        self.assertEqual(inst.group.group[2].question[1].linkId, "3.2")
        self.assertEqual(inst.group.group[2].question[1].text, "Do you drink alchohol?")
        self.assertEqual(inst.group.group[2].title, "Intoxications")
        self.assertEqual(inst.group.linkId, "root")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testQuestionnaireResponse3(self):
        inst = self.instantiate_from("questionnaireresponse-example-gcs.json")
        self.assertIsNotNone(inst, "Must have instantiated a QuestionnaireResponse instance")
        self.implQuestionnaireResponse3(inst)
        
        js = inst.as_json()
        self.assertEqual("QuestionnaireResponse", js["resourceType"])
        inst2 = questionnaireresponse.QuestionnaireResponse(js)
        self.implQuestionnaireResponse3(inst2)
    
    def implQuestionnaireResponse3(self, inst):
        self.assertEqual(inst.authored.date, FHIRDate("2014-12-11T04:44:16Z").date)
        self.assertEqual(inst.authored.as_json(), "2014-12-11T04:44:16Z")
        self.assertEqual(inst.group.linkId, "1")
        self.assertEqual(inst.group.question[0].answer[0].valueCoding.code, "LA6560-2")
        self.assertEqual(inst.group.question[0].answer[0].valueCoding.display, "Confused")
        self.assertEqual(inst.group.question[0].answer[0].valueCoding.extension[0].url, "http://hl7.org/fhir/StructureDefinition/iso21090-CO-value")
        self.assertEqual(inst.group.question[0].answer[0].valueCoding.extension[0].valueDecimal, 4)
        self.assertEqual(inst.group.question[0].answer[0].valueCoding.system, "http://loinc.org")
        self.assertEqual(inst.group.question[0].linkId, "1.1")
        self.assertEqual(inst.group.question[1].answer[0].valueCoding.code, "LA6566-9")
        self.assertEqual(inst.group.question[1].answer[0].valueCoding.display, "Localizing pain")
        self.assertEqual(inst.group.question[1].answer[0].valueCoding.extension[0].url, "http://hl7.org/fhir/StructureDefinition/iso21090-CO-value")
        self.assertEqual(inst.group.question[1].answer[0].valueCoding.extension[0].valueDecimal, 5)
        self.assertEqual(inst.group.question[1].answer[0].valueCoding.system, "http://loinc.org")
        self.assertEqual(inst.group.question[1].linkId, "1.2")
        self.assertEqual(inst.group.question[2].answer[0].valueCoding.code, "LA6556-0")
        self.assertEqual(inst.group.question[2].answer[0].valueCoding.display, "Eyes open spontaneously")
        self.assertEqual(inst.group.question[2].answer[0].valueCoding.extension[0].url, "http://hl7.org/fhir/StructureDefinition/iso21090-CO-value")
        self.assertEqual(inst.group.question[2].answer[0].valueCoding.extension[0].valueDecimal, 4)
        self.assertEqual(inst.group.question[2].answer[0].valueCoding.system, "http://loinc.org")
        self.assertEqual(inst.group.question[2].linkId, "1.3")
        self.assertEqual(inst.group.title, "Glasgow Coma Score")
        self.assertEqual(inst.id, "gcs")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testQuestionnaireResponse4(self):
        inst = self.instantiate_from("questionnaireresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a QuestionnaireResponse instance")
        self.implQuestionnaireResponse4(inst)
        
        js = inst.as_json()
        self.assertEqual("QuestionnaireResponse", js["resourceType"])
        inst2 = questionnaireresponse.QuestionnaireResponse(js)
        self.implQuestionnaireResponse4(inst2)
    
    def implQuestionnaireResponse4(self, inst):
        self.assertEqual(inst.authored.date, FHIRDate("2013-02-19T14:15:00-05:00").date)
        self.assertEqual(inst.authored.as_json(), "2013-02-19T14:15:00-05:00")
        self.assertEqual(inst.contained[0].id, "patsub")
        self.assertEqual(inst.contained[1].id, "questauth")
        self.assertEqual(inst.contained[2].id, "obs.pt-category")
        self.assertEqual(inst.group.group[0].question[0].answer[0].group[0].question[0].answer[0].valueCoding.code, "1")
        self.assertEqual(inst.group.group[0].question[0].answer[0].group[0].question[0].answer[0].valueCoding.system, "http://cancer.questionnaire.org/system/code/yesno")
        self.assertEqual(inst.group.group[0].question[0].answer[0].group[0].question[1].answer[0].valueCoding.code, "1")
        self.assertEqual(inst.group.group[0].question[0].answer[0].group[0].question[1].answer[0].valueCoding.system, "http://cancer.questionnaire.org/system/code/yesno")
        self.assertEqual(inst.group.group[0].question[0].answer[0].group[0].question[2].answer[0].valueCoding.code, "0")
        self.assertEqual(inst.group.group[0].question[0].answer[0].group[0].question[2].answer[0].valueCoding.system, "http://cancer.questionnaire.org/system/code/yesno")
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueCoding.code, "1")
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueCoding.display, "Yes")
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueCoding.system, "http://cancer.questionnaire.org/system/code/yesno")
        self.assertEqual(inst.group.title, "Cancer Quality Forum Questionnaire 2012")
        self.assertEqual(inst.id, "3141")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")

