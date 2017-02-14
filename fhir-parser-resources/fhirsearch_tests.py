#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.fhirsearch import FHIRSearch

if '__main__' == __name__:
    from models.patient import Patient
    print('1 '+FHIRSearch(Patient, {'name': 'Willis'}).construct())
    print('1 '+Patient.where({'name': 'Willis'}).construct())
    # print('1 '+Patient.where().name('Willis').construct())
    print('= Patient?name=Willis')
    print('')
    print('2 '+FHIRSearch(Patient, {'name': {'$exact': 'Willis'}}).construct())
    print('= Patient?name:exact=Willis')
    print('')
    print('3 '+FHIRSearch(Patient, {'name': {'$or': ['Willis', 'Wayne', 'Bruce']}}).construct())
    print('= Patient?name=Willis,Wayne,Bruce')
    print('')
    print('4 '+FHIRSearch(Patient, {'name': {'$and': ['Willis', {'$exact': 'Bruce'}]}}).construct())
    print('= Patient?name=Willis&name:exact=Bruce')
    print('')
    print('5 '+FHIRSearch(Patient, {'birthDate': {'$gt': '1950', '$lte': '1970'}}).construct())
    print('= Patient?birthDate=>1950&birthDate=<=1970')
    print('')
    print('6 '+FHIRSearch(Patient, {'subject.name': {'$exact': 'Willis'}}).construct())
    print('= Patient?subject.name:exact=Willis')
    print('')
    srch = FHIRSearch(Patient, {'subject': {'$type': 'Patient', 'name': 'Willis', 'birthDate': {'$gt': '1950', '$lte': '1970'}}})
    print('7 '+srch.construct())
    srch = Patient.where({'subject': {'$type': 'Patient', 'name': 'Willis', 'birthDate': {'$gt': '1950', '$lte': '1970'}}})
    print('7 '+srch.construct())
    print('= Patient?subject:Patient.name=Willis&subject:Patient.birthDate=>1950&subject:Patient.birthDate=<=1970')
    print('')
    print('8 '+FHIRSearch(Patient, {"name": {"$and": ["Willis", {"$exact": "Bruce"}]}, "birthDay": {"$and": [{"$lt": "1970", "$gte": "1950"}]}}).construct())
    print('= Patient?name=Willis&name:exact=Bruce&birthDay=>=1950&birthDay=<1970')
