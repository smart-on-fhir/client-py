This folder holds test code and data.

To re-generate the test models, run `./generate_models.sh` from the project root.

To re-generate the example test data, after re-generating the models,
run:
- `git rm tests/data/examples/*`
- `cp fhir-parser/downloads/*example*.json tests/data/examples/`
- `git add tests/data/examples/*`
