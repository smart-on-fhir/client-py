#!/bin/bash

export PYTHONPATH=.

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
    tests=(fhirclient/models/$FHIR_VERSION/*_tests.py)
    python -m unittest ${tests[@]}
done

# couple of custom tests
echo 'import requests' | python 2>/dev/null
if [ $? -eq 0 ]; then
	python -m unittest fhirclient/server_tests.py fhirclient/fhirreference_tests.py
else
	echo "You don't have the 'requests' module installed, will skip extra tests"
fi

echo 'import flake8' | python 2>/dev/null
if [ $? -eq 0 ]; then
	flake8 --max-line-length=200 *.py fhirclient/*.py
else
	echo "You don't have the 'flake8' module installed, will skip checks"
fi