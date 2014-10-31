# These are settings for the FHIR class generator

from Python.mappings import *
from Python.settings import *

# where to load the specification archive from
specification_url = 'http://hl7.org/documentcenter/public/standards/FHIR/fhir-spec.zip'

# classes/resources
write_resources = True
tpl_resource_target_ptrn = '../fhirclient/models/{}.py'     # where to write the generated class files to, with one placeholder for the class name
resource_base_target = '../fhirclient/models/'              # resource target directory, likely the same as `tpl_resource_target_ptrn` without the filename pattern

# factory methods
write_factory = False
tpl_factory_target = '../models/fhirelement+factory.py'

# search parameters
write_searchparams = True
tpl_searchparams_target = '../fhirclient/models/fhirsearchelement.py'

# unit tests
write_unittests = True
tpl_unittest_target_ptrn = '../fhirclient/models/{}_tests.py'
unittest_filename_prefix = '../../fhir-parser/downloads/site'
