#!/bin/bash

set -o errexit

git submodule update --init --recursive

for FHIR_VERSION in R4; do
    FHIR_PARSER=fhir-parser
    sed s/{FHIR_VERSION}/$FHIR_VERSION/g fhir-parser-resources/settings.py > $FHIR_PARSER/settings.py
    (
        cd $FHIR_PARSER
        ./generate.py -f $1
    )
done
