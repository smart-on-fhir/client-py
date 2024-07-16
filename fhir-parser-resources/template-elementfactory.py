#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} on {{ info.date }}.
#  {{ info.year }}, SMART Health IT.


class FHIRElementFactory(object):
    """ Factory class to instantiate resources by resource name.
    """
    
    @classmethod
    def instantiate(cls, resource_type, jsondict):
        """ Instantiate a resource of the type correlating to "resource_type".
        
        :param str resource_type: The name/type of the resource to instantiate
        :param dict jsondict: The JSON dictionary to use for data
        :returns: A resource of the respective type or `Element`
        """
        {%- for klass in classes %}
        {%- if klass.resource_type %}
        if "{{ klass.resource_type }}" == resource_type:
            from . import {{ klass.module }}
            return {{ klass.module }}.{{ klass.name }}(jsondict)
        {%- elif klass.name %}
        {#- backwards compatibility:
         # fhir-parser stopped providing resource_type for non-resources.
         # But we already shipped code that allowed creating non-resources.
         # So to avoid an API break, we keep generating this for all classes.
         # Can reconsider whether we want this once we jump to R5. (R4-QUIRK)
         #}
        if "{{ klass.name }}" == resource_type:
            from . import {{ klass.module }}
            return {{ klass.module }}.{{ klass.name }}(jsondict)
        {%- endif %}{% endfor %}
        from . import element
        return element.Element(jsondict)

