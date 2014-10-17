# These are settings for the FHIR class generator

from Python.mappings import *

# where to load the specification archive from
specification_url = 'http://hl7.org/documentcenter/public/standards/FHIR/fhir-spec.zip'

# classes/resources
write_resources = True
ptrn_filenames_lowercase = True                             # whether all pattern resource paths should be lowercase
tpl_resource_source = 'Python/template-resource.py'         # the template to use as source
tpl_resource_target_ptrn = '../fhirclient/models/{}.py'     # where to write the generated class files to, with one placeholder for the class name
resource_base_target = '../fhirclient/models/'              # resource target directory, likely the same as `tpl_resource_target_ptrn` without the filename pattern
resource_default_base = 'FHIRElement'                   # the default superclass to use
resource_baseclasses = [                                # all these files should be copied to `resource_base_target`
    'Python/fhirelement.py',
    'Python/fhirresource.py',
    'Python/fhircontainedresource.py',
    'Python/fhirreference.py',
    'Python/fhirdate.py',
    'Python/fhirsearch.py',
]

# factory methods
write_factory = False
tpl_factory_source = 'Python/template-elementfactory.py'
tpl_factory_target = '../models/fhirelement+factory.py'

# search parameters
write_searchparams = True
search_generate_camelcase = False
tpl_searchparams_source = 'Python/template-searchparams.py'
tpl_searchparams_target = '../fhirclient/models/fhirsearchelement.py'

# unit tests
write_unittests = True
tpl_unittest_source = 'Python/template-unittest.py'
tpl_unittest_target_ptrn = '../fhirclient/models/{}_tests.py'
unittest_filename_prefix = '../../fhir-parser/downloads/site'
unittest_format_path_prepare = '{}'             # used to format `path` before appending another path element - one placeholder for `path`
unittest_format_path_key = '{}.{}'              # used to create property paths by appending `key` to the existing `path` - two placeholders
unittest_format_path_index = '{}[{}]'           # used for array properties - two placeholders, `path` and the array index
