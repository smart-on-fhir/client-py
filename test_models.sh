#!/bin/bash

export PYTHONPATH=.
EXITCODE=0

# set this to the downloaded FHIR spec directory
export FHIR_UNITTEST_DATADIR="./fhir-parser/downloads"

echo 'import isodate' | python 2>/dev/null
if [ $? -ne 0 ]; then
	echo You need to have the 'isodate' module installed in order to run the tests
	exit 1
fi

for FHIR_VERSION in R4; do
    # Download into cache for this version
    rm -rf $FHIR_UNITTEST_DATADIR/*
    mkdir -p $FHIR_UNITTEST_DATADIR
    # We can't download because the spec version changes, so copy from cache
    # e.g. http://hl7.org/fhir/R4 could be 4.0.0 or 4.0.1 etc.
    # ./generate.py -f -l
    cp fhir-parser-resources/$FHIR_VERSION/version.info $FHIR_UNITTEST_DATADIR
    python -m zipfile -e fhir-parser-resources/$FHIR_VERSION/examples-json.zip $FHIR_UNITTEST_DATADIR

    python -m unittest discover -s fhirclient.models.$FHIR_VERSION -p '*_tests.py' || EXITCODE=1
done

# couple of custom tests
echo 'import requests' | python 2>/dev/null
if [ $? -eq 0 ]; then
	python -m unittest fhirclient.server_tests fhirclient.fhirreference_tests fhirclient.integration_tests || EXITCODE=1
else
	echo "You don't have the 'requests' module installed, will skip extra tests"
fi

exit $EXITCODE
