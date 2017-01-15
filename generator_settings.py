# These are settings for the FHIR class generator

from Python.settings import *

# Base URL for where to load specification data from
specification_url = 'http://hl7.org/fhir/2017Jan/'

# classes/resources
write_resources = True
tpl_resource_target_ptrn = '../fhirclient/models/{}.py'     # where to write the generated class files to, with one placeholder for the class name
resource_base_target = '../fhirclient/models/'              # resource target directory, likely the same as `tpl_resource_target_ptrn` without the filename pattern

# factory methods
write_factory = True
tpl_factory_target = '../fhirclient/models/fhirelementfactory.py'

# unit tests
write_unittests = True
tpl_unittest_target_ptrn = '../fhirclient/models/{}_tests.py'
