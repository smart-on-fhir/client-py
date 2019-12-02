#!/bin/bash

set -o errexit

git submodule update --init --recursive

# set this to the downloaded FHIR spec directory
export FHIR_UNITTEST_DATADIR="./fhir-parser/downloads"

export SKIP_TESTS=0
echo 'import isodate' | python 2>/dev/null
if [ $? -ne 0 ]; then
	echo You need to have the 'isodate' module installed in order to run the tests
    SKIP_TESTS=1
fi

for FHIR_VERSION in R4; do
    FHIR_PARSER=fhir-parser
    sed s/{FHIR_VERSION}/$FHIR_VERSION/g fhir-parser-resources/settings.py > $FHIR_PARSER/settings.py
    (
        cd $FHIR_PARSER
        ./generate.py -f $1
    )
    if [ $SKIP_TESTS -eq 0 ]; then
        python -m unittest discover -s fhirclient.models.$FHIR_VERSION -p '*_tests.py'
    fi
done
