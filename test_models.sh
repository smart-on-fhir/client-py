#!/bin/bash

export PYTHONPATH=.
EXITCODE=0

# couple of custom tests
echo 'import requests' | python 2>/dev/null
if [ $? -eq 0 ]; then
	python -m unittest fhirclient.server_tests fhirclient.fhirreference_tests fhirclient.integration_tests || EXITCODE=1
else
	echo "You don't have the 'requests' module installed, will skip tests"
fi

exit $EXITCODE
