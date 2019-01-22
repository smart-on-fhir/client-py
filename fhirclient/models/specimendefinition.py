#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class SpecimenDefinition(domainresource.DomainResource):
    """ 
    K
    i
    n
    d
    o
    f
    s
    p
    e
    c
    i
    m
    e
    n
    .
    
    
    A
    k
    i
    n
    d
    o
    f
    s
    p
    e
    c
    i
    m
    e
    n
    w
    i
    t
    h
    a
    s
    s
    o
    c
    i
    a
    t
    e
    d
    s
    e
    t
    o
    f
    r
    e
    q
    u
    i
    r
    e
    m
    e
    n
    t
    s
    .
    
    """
    
    resource_type = "SpecimenDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collection = None
        """ 
        S
        p
        e
        c
        i
        m
        e
        n
        c
        o
        l
        l
        e
        c
        t
        i
        o
        n
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        o
        f
        a
        k
        i
        n
        d
        o
        f
        s
        p
        e
        c
        i
        m
        e
        n
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patientPreparation = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        p
        r
        e
        p
        a
        r
        a
        t
        i
        o
        n
        f
        o
        r
        c
        o
        l
        l
        e
        c
        t
        i
        o
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.timeAspect = None
        """ 
        T
        i
        m
        e
        a
        s
        p
        e
        c
        t
        f
        o
        r
        c
        o
        l
        l
        e
        c
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.typeCollected = None
        """ 
        K
        i
        n
        d
        o
        f
        m
        a
        t
        e
        r
        i
        a
        l
        t
        o
        c
        o
        l
        l
        e
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.typeTested = None
        """ 
        S
        p
        e
        c
        i
        m
        e
        n
        i
        n
        c
        o
        n
        t
        a
        i
        n
        e
        r
        i
        n
        t
        e
        n
        d
        e
        d
        f
        o
        r
        t
        e
        s
        t
        i
        n
        g
        b
        y
        l
        a
        b
        .
        List of `SpecimenDefinitionTypeTested` items (represented as `dict` in JSON). """
        
        super(SpecimenDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinition, self).elementProperties()
        js.extend([
            ("collection", "collection", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("patientPreparation", "patientPreparation", codeableconcept.CodeableConcept, True, None, False),
            ("timeAspect", "timeAspect", str, False, None, False),
            ("typeCollected", "typeCollected", codeableconcept.CodeableConcept, False, None, False),
            ("typeTested", "typeTested", SpecimenDefinitionTypeTested, True, None, False),
        ])
        return js


from . import backboneelement

class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """ 
    S
    p
    e
    c
    i
    m
    e
    n
    i
    n
    c
    o
    n
    t
    a
    i
    n
    e
    r
    i
    n
    t
    e
    n
    d
    e
    d
    f
    o
    r
    t
    e
    s
    t
    i
    n
    g
    b
    y
    l
    a
    b
    .
    
    
    S
    p
    e
    c
    i
    m
    e
    n
    c
    o
    n
    d
    i
    t
    i
    o
    n
    e
    d
    i
    n
    a
    c
    o
    n
    t
    a
    i
    n
    e
    r
    a
    s
    e
    x
    p
    e
    c
    t
    e
    d
    b
    y
    t
    h
    e
    t
    e
    s
    t
    i
    n
    g
    l
    a
    b
    o
    r
    a
    t
    o
    r
    y
    .
    
    """
    
    resource_type = "SpecimenDefinitionTypeTested"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.container = None
        """ 
        T
        h
        e
        s
        p
        e
        c
        i
        m
        e
        n
        '
        s
        c
        o
        n
        t
        a
        i
        n
        e
        r
        .
        Type `SpecimenDefinitionTypeTestedContainer` (represented as `dict` in JSON). """
        
        self.handling = None
        """ 
        S
        p
        e
        c
        i
        m
        e
        n
        h
        a
        n
        d
        l
        i
        n
        g
        b
        e
        f
        o
        r
        e
        t
        e
        s
        t
        i
        n
        g
        .
        List of `SpecimenDefinitionTypeTestedHandling` items (represented as `dict` in JSON). """
        
        self.isDerived = None
        """ 
        P
        r
        i
        m
        a
        r
        y
        o
        r
        s
        e
        c
        o
        n
        d
        a
        r
        y
        s
        p
        e
        c
        i
        m
        e
        n
        .
        Type `bool`. """
        
        self.preference = None
        """ 
        p
        r
        e
        f
        e
        r
        r
        e
        d
        |
        a
        l
        t
        e
        r
        n
        a
        t
        e
        .
        Type `str`. """
        
        self.rejectionCriterion = None
        """ 
        R
        e
        j
        e
        c
        t
        i
        o
        n
        c
        r
        i
        t
        e
        r
        i
        o
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requirement = None
        """ 
        S
        p
        e
        c
        i
        m
        e
        n
        r
        e
        q
        u
        i
        r
        e
        m
        e
        n
        t
        s
        .
        Type `str`. """
        
        self.retentionTime = None
        """ 
        S
        p
        e
        c
        i
        m
        e
        n
        r
        e
        t
        e
        n
        t
        i
        o
        n
        t
        i
        m
        e
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        i
        n
        t
        e
        n
        d
        e
        d
        s
        p
        e
        c
        i
        m
        e
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTested, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTested, self).elementProperties()
        js.extend([
            ("container", "container", SpecimenDefinitionTypeTestedContainer, False, None, False),
            ("handling", "handling", SpecimenDefinitionTypeTestedHandling, True, None, False),
            ("isDerived", "isDerived", bool, False, None, False),
            ("preference", "preference", str, False, None, True),
            ("rejectionCriterion", "rejectionCriterion", codeableconcept.CodeableConcept, True, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("retentionTime", "retentionTime", duration.Duration, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    s
    p
    e
    c
    i
    m
    e
    n
    '
    s
    c
    o
    n
    t
    a
    i
    n
    e
    r
    .
    """
    
    resource_type = "SpecimenDefinitionTypeTestedContainer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive = None
        """ 
        A
        d
        d
        i
        t
        i
        v
        e
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        c
        o
        n
        t
        a
        i
        n
        e
        r
        .
        List of `SpecimenDefinitionTypeTestedContainerAdditive` items (represented as `dict` in JSON). """
        
        self.cap = None
        """ 
        C
        o
        l
        o
        r
        o
        f
        c
        o
        n
        t
        a
        i
        n
        e
        r
        c
        a
        p
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.capacity = None
        """ 
        C
        o
        n
        t
        a
        i
        n
        e
        r
        c
        a
        p
        a
        c
        i
        t
        y
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        C
        o
        n
        t
        a
        i
        n
        e
        r
        d
        e
        s
        c
        r
        i
        p
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.material = None
        """ 
        C
        o
        n
        t
        a
        i
        n
        e
        r
        m
        a
        t
        e
        r
        i
        a
        l
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.minimumVolumeQuantity = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        v
        o
        l
        u
        m
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.minimumVolumeString = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        v
        o
        l
        u
        m
        e
        .
        Type `str`. """
        
        self.preparation = None
        """ 
        S
        p
        e
        c
        i
        m
        e
        n
        c
        o
        n
        t
        a
        i
        n
        e
        r
        p
        r
        e
        p
        a
        r
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.type = None
        """ 
        K
        i
        n
        d
        o
        f
        c
        o
        n
        t
        a
        i
        n
        e
        r
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        t
        h
        e
        k
        i
        n
        d
        o
        f
        s
        p
        e
        c
        i
        m
        e
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedContainer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainer, self).elementProperties()
        js.extend([
            ("additive", "additive", SpecimenDefinitionTypeTestedContainerAdditive, True, None, False),
            ("cap", "cap", codeableconcept.CodeableConcept, False, None, False),
            ("capacity", "capacity", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, False, None, False),
            ("minimumVolumeQuantity", "minimumVolumeQuantity", quantity.Quantity, False, "minimumVolume", False),
            ("minimumVolumeString", "minimumVolumeString", str, False, "minimumVolume", False),
            ("preparation", "preparation", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """ 
    A
    d
    d
    i
    t
    i
    v
    e
    a
    s
    s
    o
    c
    i
    a
    t
    e
    d
    w
    i
    t
    h
    c
    o
    n
    t
    a
    i
    n
    e
    r
    .
    
    
    S
    u
    b
    s
    t
    a
    n
    c
    e
    i
    n
    t
    r
    o
    d
    u
    c
    e
    d
    i
    n
    t
    h
    e
    k
    i
    n
    d
    o
    f
    c
    o
    n
    t
    a
    i
    n
    e
    r
    t
    o
    p
    r
    e
    s
    e
    r
    v
    e
    ,
    m
    a
    i
    n
    t
    a
    i
    n
    o
    r
    e
    n
    h
    a
    n
    c
    e
    t
    h
    e
    s
    p
    e
    c
    i
    m
    e
    n
    .
    E
    x
    a
    m
    p
    l
    e
    s
    :
    F
    o
    r
    m
    a
    l
    i
    n
    ,
    C
    i
    t
    r
    a
    t
    e
    ,
    E
    D
    T
    A
    .
    
    """
    
    resource_type = "SpecimenDefinitionTypeTestedContainerAdditive"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveCodeableConcept = None
        """ 
        A
        d
        d
        i
        t
        i
        v
        e
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        c
        o
        n
        t
        a
        i
        n
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference = None
        """ 
        A
        d
        d
        i
        t
        i
        v
        e
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        c
        o
        n
        t
        a
        i
        n
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedContainerAdditive, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainerAdditive, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", True),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", True),
        ])
        return js


class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """ 
    S
    p
    e
    c
    i
    m
    e
    n
    h
    a
    n
    d
    l
    i
    n
    g
    b
    e
    f
    o
    r
    e
    t
    e
    s
    t
    i
    n
    g
    .
    
    
    S
    e
    t
    o
    f
    i
    n
    s
    t
    r
    u
    c
    t
    i
    o
    n
    s
    f
    o
    r
    p
    r
    e
    s
    e
    r
    v
    a
    t
    i
    o
    n
    /
    t
    r
    a
    n
    s
    p
    o
    r
    t
    o
    f
    t
    h
    e
    s
    p
    e
    c
    i
    m
    e
    n
    a
    t
    a
    d
    e
    f
    i
    n
    e
    d
    t
    e
    m
    p
    e
    r
    a
    t
    u
    r
    e
    i
    n
    t
    e
    r
    v
    a
    l
    ,
    p
    r
    i
    o
    r
    t
    h
    e
    t
    e
    s
    t
    i
    n
    g
    p
    r
    o
    c
    e
    s
    s
    .
    
    """
    
    resource_type = "SpecimenDefinitionTypeTestedHandling"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.instruction = None
        """ 
        P
        r
        e
        s
        e
        r
        v
        a
        t
        i
        o
        n
        i
        n
        s
        t
        r
        u
        c
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.maxDuration = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        p
        r
        e
        s
        e
        r
        v
        a
        t
        i
        o
        n
        t
        i
        m
        e
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.temperatureQualifier = None
        """ 
        T
        e
        m
        p
        e
        r
        a
        t
        u
        r
        e
        q
        u
        a
        l
        i
        f
        i
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.temperatureRange = None
        """ 
        T
        e
        m
        p
        e
        r
        a
        t
        u
        r
        e
        r
        a
        n
        g
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedHandling, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedHandling, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("maxDuration", "maxDuration", duration.Duration, False, None, False),
            ("temperatureQualifier", "temperatureQualifier", codeableconcept.CodeableConcept, False, None, False),
            ("temperatureRange", "temperatureRange", range.Range, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
