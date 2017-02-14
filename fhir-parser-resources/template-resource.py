#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} ({{ profile.url }}) on {{ info.date }}.
#  {{ info.year }}, SMART Health IT.

{%- set imported = {} %}
{%- for klass in classes %}


{% if klass.superclass in imports and klass.superclass.module not in imported -%}
from . import {{ klass.superclass.module }}
{% set _ = imported.update({klass.superclass.module: True}) %}
{% endif -%}

class {{ klass.name }}({% if klass.superclass in imports %}{{ klass.superclass.module }}.{% endif -%}
    {{ klass.superclass.name|default('object')}}):
    """ {{ klass.short|wordwrap(width=75, wrapstring="\n    ") }}.
{%- if klass.formal %}
    
    {{ klass.formal|wordwrap(width=75, wrapstring="\n    ") }}
{%- endif %}
    """
{%- if klass.resource_type %}
    
    resource_type = "{{ klass.resource_type }}"
{%- endif %}
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
    {%- for prop in klass.properties %}
        
        self.{{ prop.name }} = None
        """ {{ prop.short|wordwrap(67, wrapstring="\n        ") }}.
        {% if prop.is_array %}List of{% else %}Type{% endif %} `{{ prop.class_name }}`{% if prop.is_array %} items{% endif %}
        {%- if prop.reference_to_names|length > 0 %} referencing `{{ prop.reference_to_names|join(', ') }}`{% endif %}
        {%- if prop.json_class != prop.class_name %} (represented as `{{ prop.json_class }}` in JSON){% endif %}. """
    {%- endfor %}
        
        super({{ klass.name }}, self).__init__(jsondict=jsondict, strict=strict)
    
{%- if klass.properties %}
    
    def elementProperties(self):
        js = super({{ klass.name }}, self).elementProperties()
        {%- if 'element' == klass.module and 'Element' == klass.name %}
        {%- for imp in imports %}{% if imp.module not in imported %}
        from . import {{ imp.module }}
        {%- set _ = imported.update({imp.module: True}) %}
        {%- endif %}{% endfor %}
        {%- endif %}
        js.extend([
        {%- for prop in klass.properties %}
            ("{{ prop.name }}", "{{ prop.orig_name }}",
            {%- if prop.module_name %} {{ prop.module_name }}.{% else %} {% endif %}{{ prop.class_name }}, {# #}
            {{- prop.is_array }},
            {%- if prop.one_of_many %} "{{ prop.one_of_many }}"{% else %} None{% endif %}, {# #}
            {{- prop.nonoptional }}),
        {%- endfor %}
        ])
        return js
    
{%- endif %}
{%- endfor %}

{% for imp in imports %}{% if imp.module not in imported %}
from . import {{ imp.module }}
{%- endif %}{% endfor %}

