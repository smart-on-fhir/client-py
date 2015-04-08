#!/bin/bash

# set this to a relative path, from inside the fhirclient/models directory, to the downloaded FHIR spec directory
export FHIR_UNITTEST_DATADIR="../../fhir-parser/downloads"

cd fhirclient
cd models

if [ ! -e $FHIR_UNITTEST_DATADIR ]; then
	echo Unit tests depend on the downloaded FHIR spec, which is not present at $FHIR_UNITTEST_DATADIR. Cannot run unit tests.
	exit 1
fi

python -m unittest discover . '*_tests.py'

cd ..
cd ..
