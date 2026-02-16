# Settings for generating FHIR R4 model classes.
# All paths are relative to the `fhir-parser` directory.

from Default.settings import *

# Base URL for where to load specification data from
specification_url = 'http://hl7.org/fhir/R4'

# In which directory to find the templates.
tpl_base = '../fhir-parser-resources'

# classes/resources - generated into the R4 versioned subdirectory
write_resources = True
tpl_resource_target = '../fhirclient/models/R4'
tpl_codesystems_source = None

# factory methods
write_factory = True
tpl_factory_target = '../fhirclient/models/R4/fhirelementfactory.py'

# unit tests
write_unittests = True
tpl_unittest_target = '../tests/models'

# Version identifier used in generated test imports
fhir_version = 'R4'

# Shared base classes already live in fhirclient/models/ (not versioned).
# They are NOT copied into the version subdirectory.
# The generator's manual_profiles mechanism copies files to the target dir,
# but since shared bases are already in models/, we provide an empty list.
manual_profiles = []
