#!/bin/bash

set -o errexit

git submodule update --init --recursive

for FHIR_VERSION in DSTU2 STU3 R4; do
    if [ -d fhir-parser-$FHIR_VERSION ]; then
        FHIR_PARSER=fhir-parser-$FHIR_VERSION
        sed s/{FHIR_VERSION}/$FHIR_VERSION/g fhir-parser-resources/settings-$FHIR_VERSION.py > $FHIR_PARSER/settings.py
        # We can't use tpl_unittest_source in settings because jinja2 won't load templates outside current dir,
        # So we copy our template into the submodule in env which is .gitignored
        mkdir -p $FHIR_PARSER/env
        cp fhir-parser-resources/template-unittest.py $FHIR_PARSER/env
    else
        FHIR_PARSER=fhir-parser
        sed s/{FHIR_VERSION}/$FHIR_VERSION/g fhir-parser-resources/settings.py > $FHIR_PARSER/settings.py
    fi
    (
        cd $FHIR_PARSER
        #XXX this rmtrees with -f
        ./generate.py -f $1
    )
done
