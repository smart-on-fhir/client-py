#  Generated from FHIR {{ info.version }}, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import {{ class.module }}
from fhirclient.models.fhirdate import FHIRDate


class {{ class.name }}Tests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("{{ class.name }}", js["resourceType"])
        return {{ class.module }}.{{ class.name }}(js)
    
{%- for tcase in tests %}
    
    def test{{ class.name }}{{ loop.index }}(self):
        inst = self.instantiate_from("{{ tcase.filename }}")
        self.assertIsNotNone(inst, "Must have instantiated a {{ class.name }} instance")
        self.impl{{ class.name }}{{ loop.index }}(inst)
        
        js = inst.as_json()
        self.assertEqual("{{ class.name }}", js["resourceType"])
        inst2 = {{ class.module }}.{{ class.name }}(js)
        self.impl{{ class.name }}{{ loop.index }}(inst2)
    
    def impl{{ class.name }}{{ loop.index }}(self, inst):
    {%- for onetest in tcase.tests %}
    {%- if "str" == onetest.klass.name %}
        self.assertEqual(inst.{{ onetest.path }}, "{{ onetest.value|replace('\\', '\\\\')|replace('"', '\\"') }}")
    {%- else %}{% if "int" == onetest.klass.name or "float" == onetest.klass.name or "NSDecimalNumber" == onetest.klass.name %}
        self.assertEqual(inst.{{ onetest.path }}, {{ onetest.value }})
    {%- else %}{% if "bool" == onetest.klass.name %}
        {%- if onetest.value %}
        self.assertTrue(inst.{{ onetest.path }})
        {%- else %}
        self.assertFalse(inst.{{ onetest.path }})
        {%- endif %}
    {%- else %}{% if "FHIRDate" == onetest.klass.name %}
        self.assertEqual(inst.{{ onetest.path }}.date, FHIRDate("{{ onetest.value }}").date)
        self.assertEqual(inst.{{ onetest.path }}.as_json(), "{{ onetest.value }}")
    {%- else %}
        # Don't know how to create unit test for "{{ onetest.path }}", which is a {{ onetest.klass.name }}
    {%- endif %}{% endif %}{% endif %}{% endif %}
    {%- endfor %}
{%- endfor %}


