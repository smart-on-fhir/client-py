#!/bin/bash

# set this to a relative path, from inside the fhirclient/models directory, to the downloaded FHIR spec directory
export FHIR_UNITTEST_DATADIR="../fhir-parser/downloads"

cd fhirclient

if [ ! -e $FHIR_UNITTEST_DATADIR ]; then
	echo Unit tests depend on the downloaded FHIR spec, which is not present at $FHIR_UNITTEST_DATADIR. Cannot run unit tests.
	exit 1
fi
echo 'import isodate' | python 2>/dev/null
if [ $? -ne 0 ]; then
	echo You need to have the 'isodate' module installed in order to run the tests
	exit 1
fi

#python -m unittest discover ./models '*_tests.py'		# ImportError
tests=(models/*_tests.py)
python -m unittest ${tests[@]}

# couple of custom tests
echo 'import requests' | python 2>/dev/null
if [ $? -eq 0 ]; then
	python -m unittest server_tests.py fhirreference_tests.py
else
	echo "You don't have the 'requests' module installed, will skip extra tests"
fi

cd ..
