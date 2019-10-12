# These are settings for the FHIR class generator

from Python.settings import *

# classes/resources
write_resources = True
tpl_resource_target_ptrn = '../fhirclient/models/DSTU2/{}.py'     # where to write the generated class files to, with one placeholder for the class name
resource_base_target = '../fhirclient/models/DSTU2/'              # resource target directory, likely the same as `tpl_resource_target_ptrn` without the filename pattern

# factory methods
write_factory = True
tpl_factory_target = '../fhirclient/models/DSTU2/fhirelementfactory.py'

# unit tests
write_unittests = True
tpl_unittest_target_ptrn = '../fhirclient/models/DSTU2/{}_tests.py'

# jinja2 doesn't support '..', generate_models.sh copies this file here
tpl_unittest_source = 'env/template-unittest.py'
