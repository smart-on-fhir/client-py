#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import questionnaireanswers
from .fhirdate import FHIRDate


class QuestionnaireAnswersTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("QuestionnaireAnswers", js["resourceType"])
        return questionnaireanswers.QuestionnaireAnswers(js)
    
    def testQuestionnaireAnswers1(self):
        inst = self.instantiate_from("questionnaireanswers-example-bluebook.json")
        self.assertIsNotNone(inst, "Must have instantiated a QuestionnaireAnswers instance")
        self.implQuestionnaireAnswers1(inst)
        
        js = inst.as_json()
        self.assertEqual("QuestionnaireAnswers", js["resourceType"])
        inst2 = questionnaireanswers.QuestionnaireAnswers(js)
        self.implQuestionnaireAnswers1(inst2)
    
    def implQuestionnaireAnswers1(self, inst):
        self.assertEqual(inst.authored.date, FHIRDate("2013-02-19T14:15:00+10:00").date)
        self.assertEqual(inst.authored.as_json(), "2013-02-19T14:15:00+10:00")
        self.assertEqual(inst.group.group[0].group[0].question[0].answer[0].valueString, "Cathy Jones")
        self.assertEqual(inst.group.group[0].group[0].question[0].text, "Name of child")
        self.assertEqual(inst.group.group[0].group[0].question[1].answer[0].valueCoding.code, "f")
        self.assertEqual(inst.group.group[0].group[0].question[1].text, "Sex")
        self.assertEqual(inst.group.group[0].group[1].question[0].answer[0].valueDecimal, 3.25)
        self.assertEqual(inst.group.group[0].group[1].question[0].text, "Birth weight (kg)")
        self.assertEqual(inst.group.group[0].group[1].question[1].answer[0].valueDecimal, 44.3)
        self.assertEqual(inst.group.group[0].group[1].question[1].text, "Birth length (cm)")
        self.assertEqual(inst.group.group[0].group[1].question[2].answer[0].valueCoding.code, "INJECTION")
        self.assertEqual(inst.group.group[0].group[1].question[2].group[0].extension[0].url, "http://example.org/Profile/questionnaire#visibilityCondition")
        self.assertEqual(inst.group.group[0].group[1].question[2].group[0].extension[0].valueString, "HAS_VALUE(../choice/code) AND NEQ(../choice/code,'NO')")
        self.assertEqual(inst.group.group[0].group[1].question[2].group[0].question[0].answer[0].valueDate.date, FHIRDate("1972-11-30").date)
        self.assertEqual(inst.group.group[0].group[1].question[2].group[0].question[0].answer[0].valueDate.as_json(), "1972-11-30")
        self.assertEqual(inst.group.group[0].group[1].question[2].group[0].question[0].text, "1st dose")
        self.assertEqual(inst.group.group[0].group[1].question[2].group[0].question[1].answer[0].valueDate.date, FHIRDate("1972-12-11").date)
        self.assertEqual(inst.group.group[0].group[1].question[2].group[0].question[1].answer[0].valueDate.as_json(), "1972-12-11")
        self.assertEqual(inst.group.group[0].group[1].question[2].group[0].question[1].text, "2nd dose")
        self.assertEqual(inst.group.group[0].group[1].question[2].text, "Vitamin K given")
        self.assertTrue(inst.group.group[0].group[1].question[3].answer[0].valueBoolean)
        self.assertEqual(inst.group.group[0].group[1].question[3].group[0].question[0].answer[0].valueDate.date, FHIRDate("1972-12-04").date)
        self.assertEqual(inst.group.group[0].group[1].question[3].group[0].question[0].answer[0].valueDate.as_json(), "1972-12-04")
        self.assertEqual(inst.group.group[0].group[1].question[3].group[0].question[0].text, "Date given")
        self.assertEqual(inst.group.group[0].group[1].question[3].text, "Hep B given y / n")
        self.assertEqual(inst.group.group[0].group[1].question[4].answer[0].valueString, "Already able to speak Chinese")
        self.assertEqual(inst.group.group[0].group[1].question[4].text, "Abnormalities noted at birth")
        self.assertEqual(inst.group.group[0].group[1].title, "Neonatal Information")
        self.assertEqual(inst.group.group[0].title, "Birth details - To be completed by health professional")
        self.assertEqual(inst.group.title, "NSW Government My Personal Health Record, january 2013")
        self.assertEqual(inst.id, "bb")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testQuestionnaireAnswers2(self):
        inst = self.instantiate_from("questionnaireanswers-example-f201-lifelines.json")
        self.assertIsNotNone(inst, "Must have instantiated a QuestionnaireAnswers instance")
        self.implQuestionnaireAnswers2(inst)
        
        js = inst.as_json()
        self.assertEqual("QuestionnaireAnswers", js["resourceType"])
        inst2 = questionnaireanswers.QuestionnaireAnswers(js)
        self.implQuestionnaireAnswers2(inst2)
    
    def implQuestionnaireAnswers2(self, inst):
        self.assertEqual(inst.authored.date, FHIRDate("2013-06-18T00:00:00+01:00").date)
        self.assertEqual(inst.authored.as_json(), "2013-06-18T00:00:00+01:00")
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueString, "I am allergic to house dust")
        self.assertEqual(inst.group.group[0].question[0].text, "Do you have allergies?")
        self.assertEqual(inst.group.group[1].question[0].answer[0].valueString, "Male")
        self.assertEqual(inst.group.group[1].question[0].text, "What is your gender?")
        self.assertEqual(inst.group.group[1].question[1].answer[0].valueDate.date, FHIRDate("1960-03-13").date)
        self.assertEqual(inst.group.group[1].question[1].answer[0].valueDate.as_json(), "1960-03-13")
        self.assertEqual(inst.group.group[1].question[1].text, "What is your date of birth?")
        self.assertEqual(inst.group.group[1].question[2].answer[0].valueString, "The Netherlands")
        self.assertEqual(inst.group.group[1].question[2].text, "What is your country of birth?")
        self.assertEqual(inst.group.group[1].question[3].answer[0].valueString, "married")
        self.assertEqual(inst.group.group[1].question[3].text, "What is your marital status?")
        self.assertEqual(inst.group.group[1].title, "General questions")
        self.assertEqual(inst.group.group[2].question[0].answer[0].valueString, "No")
        self.assertEqual(inst.group.group[2].question[0].text, "Do you smoke?")
        self.assertEqual(inst.group.group[2].question[1].answer[0].valueString, "No, but I used to drink")
        self.assertEqual(inst.group.group[2].question[1].text, "Do you drink alchohol?")
        self.assertEqual(inst.group.group[2].title, "Intoxications")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testQuestionnaireAnswers3(self):
        inst = self.instantiate_from("questionnaireanswers-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a QuestionnaireAnswers instance")
        self.implQuestionnaireAnswers3(inst)
        
        js = inst.as_json()
        self.assertEqual("QuestionnaireAnswers", js["resourceType"])
        inst2 = questionnaireanswers.QuestionnaireAnswers(js)
        self.implQuestionnaireAnswers3(inst2)
    
    def implQuestionnaireAnswers3(self, inst):
        self.assertEqual(inst.authored.date, FHIRDate("2013-02-19T14:15:00-05:00").date)
        self.assertEqual(inst.authored.as_json(), "2013-02-19T14:15:00-05:00")
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueCoding.code, "1")
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueCoding.display, "Yes")
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueCoding.system, "http://cancer.questionnaire.org/system/code/yesno")
        self.assertEqual(inst.group.group[0].question[0].group[0].question[0].answer[0].valueCoding.code, "1")
        self.assertEqual(inst.group.group[0].question[0].group[0].question[0].answer[0].valueCoding.system, "http://cancer.questionnaire.org/system/code/yesno")
        self.assertEqual(inst.group.group[0].question[0].group[0].question[1].answer[0].valueCoding.code, "1")
        self.assertEqual(inst.group.group[0].question[0].group[0].question[1].answer[0].valueCoding.system, "http://cancer.questionnaire.org/system/code/yesno")
        self.assertEqual(inst.group.group[0].question[0].group[0].question[2].answer[0].valueCoding.code, "0")
        self.assertEqual(inst.group.group[0].question[0].group[0].question[2].answer[0].valueCoding.system, "http://cancer.questionnaire.org/system/code/yesno")
        self.assertEqual(inst.group.title, "Cancer Quality Forum Questionnaire 2012")
        self.assertEqual(inst.id, "3141")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")
    
    def testQuestionnaireAnswers4(self):
        inst = self.instantiate_from("questionnaireanswers-sdc-profile-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a QuestionnaireAnswers instance")
        self.implQuestionnaireAnswers4(inst)
        
        js = inst.as_json()
        self.assertEqual("QuestionnaireAnswers", js["resourceType"])
        inst2 = questionnaireanswers.QuestionnaireAnswers(js)
        self.implQuestionnaireAnswers4(inst2)
    
    def implQuestionnaireAnswers4(self, inst):
        self.assertEqual(inst.authored.date, FHIRDate("2014-01-21").date)
        self.assertEqual(inst.authored.as_json(), "2014-01-21")
        self.assertEqual(inst.group.group[0].linkId, "3921053v1.0")
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueDate.date, FHIRDate("2003-02-18").date)
        self.assertEqual(inst.group.group[0].question[0].answer[0].valueDate.as_json(), "2003-02-18")
        self.assertEqual(inst.group.group[0].question[0].linkId, "3921059v1.0")
        self.assertEqual(inst.group.group[0].question[0].text, "Date of Current Pathologic Diagnosis")
        self.assertEqual(inst.group.group[0].question[1].answer[0].valueCoding.code, "1")
        self.assertEqual(inst.group.group[0].question[1].answer[0].valueCoding.display, "Primary Diagnosis")
        self.assertEqual(inst.group.group[0].question[1].answer[0].valueCoding.system, "http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3921060v1.0-cs")
        self.assertEqual(inst.group.group[0].question[1].linkId, "3921060v1.0")
        self.assertEqual(inst.group.group[0].question[1].text, "Diagnosis Type")
        self.assertEqual(inst.group.group[0].question[2].answer[0].valueString, "Left Ovary")
        self.assertEqual(inst.group.group[0].question[2].linkId, "3921053v1.0")
        self.assertEqual(inst.group.group[0].question[2].text, "Primary Site")
        self.assertEqual(inst.group.group[0].text, "These items must be included when this data is collected for reporting.")
        self.assertEqual(inst.group.group[0].title, "Mandatory Diagnosis Questions")
        self.assertEqual(inst.group.group[1].linkId, "3921066v1.0")
        self.assertEqual(inst.group.group[1].question[0].answer[0].valueCoding.code, "3")
        self.assertEqual(inst.group.group[1].question[0].answer[0].valueCoding.display, "Restaging")
        self.assertEqual(inst.group.group[1].question[0].answer[0].valueCoding.system, "http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3921066v1.0-cs")
        self.assertEqual(inst.group.group[1].question[0].text, "Diagnosis Time Point")
        self.assertEqual(inst.group.group[1].text, "There are business rules to indicate situations under which these elements should be used on a case report form.")
        self.assertEqual(inst.group.group[1].title, "Conditional Diagnosis Questions")
        self.assertEqual(inst.group.group[2].linkId, "3921077v1.0")
        self.assertEqual(inst.group.group[2].question[0].answer[0].valueString, "Harold Ornada")
        self.assertEqual(inst.group.group[2].question[0].linkId, "3921079v1.0")
        self.assertEqual(inst.group.group[2].question[0].text, "Reviewing Pathologist")
        self.assertEqual(inst.group.group[2].question[1].linkId, "3921080v1.0")
        self.assertEqual(inst.group.group[2].question[1].text, "MedDRA disease code")
        self.assertEqual(inst.group.group[2].question[2].answer[0].valueCoding.code, "2")
        self.assertEqual(inst.group.group[2].question[2].answer[0].valueCoding.display, "Histological Procedure")
        self.assertEqual(inst.group.group[2].question[2].answer[0].valueCoding.system, "http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3921081v1.0-cs")
        self.assertEqual(inst.group.group[2].question[2].linkId, "3921081v1.0")
        self.assertEqual(inst.group.group[2].question[2].text, "Assessment Method")
        self.assertEqual(inst.group.group[2].question[3].answer[0].valueCoding.code, "2")
        self.assertEqual(inst.group.group[2].question[3].answer[0].valueCoding.display, "Moderately Differentiated")
        self.assertEqual(inst.group.group[2].question[3].answer[0].valueCoding.system, "http://nci.nih.gov/xml/owl/cadsr/data_element_scoped_identifier#3921085v1.0-cs")
        self.assertEqual(inst.group.group[2].question[3].linkId, "3921085v1.0")
        self.assertEqual(inst.group.group[2].question[3].text, "Tumor grade")
        self.assertEqual(inst.group.group[2].title, "Optional Diagnosis Questions")
        self.assertEqual(inst.group.title, "Diagnosis NCI Standard Template")
        self.assertEqual(inst.id, "sdc")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")

