#!/bin/bash

if [ ! -e fhir-parser/downloads/site ]; then
	echo Unit tests depend on the downloaded FHIR spec, which is not present at ./fhir-parser/downloads. Cannot run unit tests.
	exit 1
fi

cd fhirclient/models
python -m unittest discover . '*_tests.py'
cd ../..

