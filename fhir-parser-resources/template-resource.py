# Generated from FHIR {{ info.version }} ({{ profile.url }}).
# {{ info.year }}, SMART Health IT.

{%- set imported = {} %}
{#- NOTE: shared_modules must be kept in sync with _SHARED_MODULES in fhirclient/models/__init__.py -#}
{%- set shared_modules = ['fhirabstractbase', 'fhirabstractresource', 'fhirreference', 'fhirsearch', 'fhirdate', 'fhirdatetime', 'fhirinstant', 'fhirtime'] %}
{%- for klass in classes %}


{% if klass.superclass in imports and klass.superclass.module not in imported -%}
{% if klass.superclass.module in shared_modules -%}
from .. import {{ klass.superclass.module }}
{% else -%}
from . import {{ klass.superclass.module }}
{% endif -%}
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
{%- elif klass.name %}
{#- backwards compatibility:
# fhir-parser stopped providing resource_type for non-resources.
# But we already shipped code that had this property for all classes.
# So to avoid an API break, we keep generating this for all classes.
# Can remove once we jump to R5. (R4-QUIRK)
#}
    
    resource_type = "{{ klass.name }}"
{%- endif %}
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
    {#- sorted just to avoid churn during another update - can remove as its own PR at some point #}
    {%- for prop in klass.properties|sort(attribute="name", case_sensitive=True) %}
        
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
        {% if imp.module in shared_modules -%}
        from .. import {{ imp.module }}
        {%- else -%}
        from . import {{ imp.module }}
        {%- endif %}
        {%- set _ = imported.update({imp.module: True}) %}
        {%- endif %}{% endfor %}
        {%- endif %}
        js.extend([
        {#- sorted just to avoid churn during another update - can remove as its own PR at some point #}
        {%- for prop in klass.properties|sort(attribute="name", case_sensitive=True) %}
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
{% if imp.module in shared_modules -%}
from .. import {{ imp.module }}
{%- else -%}
from . import {{ imp.module }}
{%- endif %}
{%- endif %}{% endfor %}

