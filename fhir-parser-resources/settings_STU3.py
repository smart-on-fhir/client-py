# Settings for generating FHIR STU-3 model classes.
# All paths are relative to the `fhir-parser` directory.

from Default.settings import *

# Base URL for where to load specification data from
specification_url = 'http://hl7.org/fhir/STU3'

# In which directory to find the templates.
tpl_base = '../fhir-parser-resources'

# classes/resources - generated into the STU3 versioned subdirectory
write_resources = True
tpl_resource_target = '../fhirclient/models/STU3'
tpl_codesystems_source = None

# factory methods
write_factory = True
tpl_factory_target = '../fhirclient/models/STU3/fhirelementfactory.py'

# unit tests
write_unittests = True
tpl_unittest_target = '../tests/models_stu3'

# Version identifier used in generated test imports
fhir_version = 'STU3'

# Shared base classes already live in fhirclient/models/ (not versioned).
manual_profiles = []
