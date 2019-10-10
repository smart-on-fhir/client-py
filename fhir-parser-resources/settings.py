# These are settings for the FHIR class generator.
# All paths are relative to the `fhir-parser` directory. You may want to use
# os.path.join() if the generator should work on Windows, too.

from Default.settings import *

# Base URL for where to load specification data from
specification_url = 'http://hl7.org/fhir/{FHIR_VERSION}'

# In which directory to find the templates. See below for settings that start with `tpl_`: these are the template names.
tpl_base = '../fhir-parser-resources'

# classes/resources
write_resources = True
tpl_resource_target = '../fhirclient/models/{FHIR_VERSION}'    # target directory to write the generated class files to
tpl_codesystems_source = None                   # the template to use as source when writing enums for CodeSystems; can be `None`

# factory methods
write_factory = True
tpl_factory_target = '../fhirclient/models/{FHIR_VERSION}/fhirelementfactory.py'    # where to write the generated factory to

# unit tests
write_unittests = True
tpl_unittest_target = '../fhirclient/models/{FHIR_VERSION}'    # target directory to write the generated unit test files to


# all these files should be copied to dirname(`tpl_resource_target_ptrn`): tuples of (path/to/file, module, array-of-class-names)
manual_profiles = [
    ('../fhir-parser-resources/fhirabstractbase.py', 'fhirabstractbase', [
        'boolean',
        'string', 'base64Binary', 'code', 'id',
        'decimal', 'integer', 'unsignedInt', 'positiveInt',
        'uri', 'oid', 'uuid',
        'FHIRAbstractBase',
    ]),
    ('../fhir-parser-resources/fhirabstractresource.py', 'fhirabstractresource', ['FHIRAbstractResource']),
    ('../fhir-parser-resources/fhirreference.py', 'fhirreference', ['FHIRReference']),
    ('../fhir-parser-resources/fhirdate.py', 'fhirdate', ['date', 'dateTime', 'instant', 'time']),
    ('../fhir-parser-resources/fhirsearch.py', 'fhirsearch', ['FHIRSearch']),
]
