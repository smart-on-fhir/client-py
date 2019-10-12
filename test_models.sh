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

for FHIR_VERSION in DSTU2 STU3 R4; do

cat > fhir-parser/settings.py  <<EOF
from Default.mappings import *
specification_url = 'http://hl7.org/fhir/$FHIR_VERSION/'
EOF
    (
        cd fhir-parser
        # Download only into cache for this version
        rm -rf ./downloads/*
        ./generate.py -f -l
    )
    python -m unittest discover -s fhirclient.models.$FHIR_VERSION -p '*_tests.py' || EXITCODE=1
done

# couple of custom tests
echo 'import requests' | python 2>/dev/null
if [ $? -eq 0 ]; then
	python -m unittest fhirclient.server_tests fhirclient.fhirreference_tests fhirclient.integration_tests || EXITCODE=1
else
	echo "You don't have the 'requests' module installed, will skip extra tests"
fi

echo 'import flake8' | python 2>/dev/null
if [ $? -eq 0 ]; then
	flake8 --max-line-length=200 *.py fhirclient/*.py || EXITCODE=1
else
	echo "You don't have the 'flake8' module installed, will skip checks"
fi

exit $EXITCODE
