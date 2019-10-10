#!/bin/bash

set -o errexit

git submodule update --init --recursive

for FHIR_VERSION in DSTU2 STU3 R4; do
    if [ -d fhir-parser-$FHIR_VERSION ]; then
        FHIR_PARSER=fhir-parser-$FHIR_VERSION
        sed s/{FHIR_VERSION}/$FHIR_VERSION/g fhir-parser-resources/settings-$FHIR_VERSION.py > $FHIR_PARSER/settings.py
    else
        FHIR_PARSER=fhir-parser
        sed s/{FHIR_VERSION}/$FHIR_VERSION/g fhir-parser-resources/settings.py > $FHIR_PARSER/settings.py
    fi
    (
        cd $FHIR_PARSER
        # We can't use the cache since it changes for each version
        rm -rf ./downloads/*
        ./generate.py -f $1
    )
done
