#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DataRequirement) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class DataRequirement(element.Element):
    """ 
    D
    e
    s
    c
    r
    i
    b
    e
    s
    a
    r
    e
    q
    u
    i
    r
    e
    d
    d
    a
    t
    a
    i
    t
    e
    m
    .
    
    
    D
    e
    s
    c
    r
    i
    b
    e
    s
    a
    r
    e
    q
    u
    i
    r
    e
    d
    d
    a
    t
    a
    i
    t
    e
    m
    f
    o
    r
    e
    v
    a
    l
    u
    a
    t
    i
    o
    n
    i
    n
    t
    e
    r
    m
    s
    o
    f
    t
    h
    e
    t
    y
    p
    e
    o
    f
    d
    a
    t
    a
    ,
    a
    n
    d
    o
    p
    t
    i
    o
    n
    a
    l
    c
    o
    d
    e
    o
    r
    d
    a
    t
    e
    -
    b
    a
    s
    e
    d
    f
    i
    l
    t
    e
    r
    s
    o
    f
    t
    h
    e
    d
    a
    t
    a
    .
    
    """
    
    resource_type = "DataRequirement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeFilter = None
        """ 
        W
        h
        a
        t
        c
        o
        d
        e
        s
        a
        r
        e
        e
        x
        p
        e
        c
        t
        e
        d
        .
        List of `DataRequirementCodeFilter` items (represented as `dict` in JSON). """
        
        self.dateFilter = None
        """ 
        W
        h
        a
        t
        d
        a
        t
        e
        s
        /
        d
        a
        t
        e
        r
        a
        n
        g
        e
        s
        a
        r
        e
        e
        x
        p
        e
        c
        t
        e
        d
        .
        List of `DataRequirementDateFilter` items (represented as `dict` in JSON). """
        
        self.limit = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        r
        e
        s
        u
        l
        t
        s
        .
        Type `int`. """
        
        self.mustSupport = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        e
        s
        s
        p
        e
        c
        i
        f
        i
        c
        s
        t
        r
        u
        c
        t
        u
        r
        e
        e
        l
        e
        m
        e
        n
        t
        s
        t
        h
        a
        t
        a
        r
        e
        r
        e
        f
        e
        r
        e
        n
        c
        e
        d
        b
        y
        t
        h
        e
        k
        n
        o
        w
        l
        e
        d
        g
        e
        m
        o
        d
        u
        l
        e
        .
        List of `str` items. """
        
        self.profile = None
        """ 
        T
        h
        e
        p
        r
        o
        f
        i
        l
        e
        o
        f
        t
        h
        e
        r
        e
        q
        u
        i
        r
        e
        d
        d
        a
        t
        a
        .
        List of `str` items. """
        
        self.sort = None
        """ 
        O
        r
        d
        e
        r
        o
        f
        t
        h
        e
        r
        e
        s
        u
        l
        t
        s
        .
        List of `DataRequirementSort` items (represented as `dict` in JSON). """
        
        self.subjectCodeableConcept = None
        """ 
        E
        .
        g
        .
        P
        a
        t
        i
        e
        n
        t
        ,
        P
        r
        a
        c
        t
        i
        t
        i
        o
        n
        e
        r
        ,
        R
        e
        l
        a
        t
        e
        d
        P
        e
        r
        s
        o
        n
        ,
        O
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
        ,
        L
        o
        c
        a
        t
        i
        o
        n
        ,
        D
        e
        v
        i
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ 
        E
        .
        g
        .
        P
        a
        t
        i
        e
        n
        t
        ,
        P
        r
        a
        c
        t
        i
        t
        i
        o
        n
        e
        r
        ,
        R
        e
        l
        a
        t
        e
        d
        P
        e
        r
        s
        o
        n
        ,
        O
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
        ,
        L
        o
        c
        a
        t
        i
        o
        n
        ,
        D
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        h
        e
        t
        y
        p
        e
        o
        f
        t
        h
        e
        r
        e
        q
        u
        i
        r
        e
        d
        d
        a
        t
        a
        .
        Type `str`. """
        
        super(DataRequirement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirement, self).elementProperties()
        js.extend([
            ("codeFilter", "codeFilter", DataRequirementCodeFilter, True, None, False),
            ("dateFilter", "dateFilter", DataRequirementDateFilter, True, None, False),
            ("limit", "limit", int, False, None, False),
            ("mustSupport", "mustSupport", str, True, None, False),
            ("profile", "profile", str, True, None, False),
            ("sort", "sort", DataRequirementSort, True, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("type", "type", str, False, None, True),
        ])
        return js


class DataRequirementCodeFilter(element.Element):
    """ 
    W
    h
    a
    t
    c
    o
    d
    e
    s
    a
    r
    e
    e
    x
    p
    e
    c
    t
    e
    d
    .
    
    
    C
    o
    d
    e
    f
    i
    l
    t
    e
    r
    s
    s
    p
    e
    c
    i
    f
    y
    a
    d
    d
    i
    t
    i
    o
    n
    a
    l
    c
    o
    n
    s
    t
    r
    a
    i
    n
    t
    s
    o
    n
    t
    h
    e
    d
    a
    t
    a
    ,
    s
    p
    e
    c
    i
    f
    y
    i
    n
    g
    t
    h
    e
    v
    a
    l
    u
    e
    s
    e
    t
    o
    f
    i
    n
    t
    e
    r
    e
    s
    t
    f
    o
    r
    a
    p
    a
    r
    t
    i
    c
    u
    l
    a
    r
    e
    l
    e
    m
    e
    n
    t
    o
    f
    t
    h
    e
    d
    a
    t
    a
    .
    E
    a
    c
    h
    c
    o
    d
    e
    f
    i
    l
    t
    e
    r
    d
    e
    f
    i
    n
    e
    s
    a
    n
    a
    d
    d
    i
    t
    i
    o
    n
    a
    l
    c
    o
    n
    s
    t
    r
    a
    i
    n
    t
    o
    n
    t
    h
    e
    d
    a
    t
    a
    ,
    i
    .
    e
    .
    c
    o
    d
    e
    f
    i
    l
    t
    e
    r
    s
    a
    r
    e
    A
    N
    D
    '
    e
    d
    ,
    n
    o
    t
    O
    R
    '
    e
    d
    .
    
    """
    
    resource_type = "DataRequirementCodeFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        W
        h
        a
        t
        c
        o
        d
        e
        i
        s
        e
        x
        p
        e
        c
        t
        e
        d
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.path = None
        """ 
        A
        c
        o
        d
        e
        -
        v
        a
        l
        u
        e
        d
        a
        t
        t
        r
        i
        b
        u
        t
        e
        t
        o
        f
        i
        l
        t
        e
        r
        o
        n
        .
        Type `str`. """
        
        self.searchParam = None
        """ 
        A
        c
        o
        d
        e
        d
        (
        t
        o
        k
        e
        n
        )
        p
        a
        r
        a
        m
        e
        t
        e
        r
        t
        o
        s
        e
        a
        r
        c
        h
        o
        n
        .
        Type `str`. """
        
        self.valueSet = None
        """ 
        V
        a
        l
        u
        e
        s
        e
        t
        f
        o
        r
        t
        h
        e
        f
        i
        l
        t
        e
        r
        .
        Type `str`. """
        
        super(DataRequirementCodeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementCodeFilter, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, True, None, False),
            ("path", "path", str, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
        ])
        return js


class DataRequirementDateFilter(element.Element):
    """ 
    W
    h
    a
    t
    d
    a
    t
    e
    s
    /
    d
    a
    t
    e
    r
    a
    n
    g
    e
    s
    a
    r
    e
    e
    x
    p
    e
    c
    t
    e
    d
    .
    
    
    D
    a
    t
    e
    f
    i
    l
    t
    e
    r
    s
    s
    p
    e
    c
    i
    f
    y
    a
    d
    d
    i
    t
    i
    o
    n
    a
    l
    c
    o
    n
    s
    t
    r
    a
    i
    n
    t
    s
    o
    n
    t
    h
    e
    d
    a
    t
    a
    i
    n
    t
    e
    r
    m
    s
    o
    f
    t
    h
    e
    a
    p
    p
    l
    i
    c
    a
    b
    l
    e
    d
    a
    t
    e
    r
    a
    n
    g
    e
    f
    o
    r
    s
    p
    e
    c
    i
    f
    i
    c
    e
    l
    e
    m
    e
    n
    t
    s
    .
    E
    a
    c
    h
    d
    a
    t
    e
    f
    i
    l
    t
    e
    r
    s
    p
    e
    c
    i
    f
    i
    e
    s
    a
    n
    a
    d
    d
    i
    t
    i
    o
    n
    a
    l
    c
    o
    n
    s
    t
    r
    a
    i
    n
    t
    o
    n
    t
    h
    e
    d
    a
    t
    a
    ,
    i
    .
    e
    .
    d
    a
    t
    e
    f
    i
    l
    t
    e
    r
    s
    a
    r
    e
    A
    N
    D
    '
    e
    d
    ,
    n
    o
    t
    O
    R
    '
    e
    d
    .
    
    """
    
    resource_type = "DataRequirementDateFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ 
        A
        d
        a
        t
        e
        -
        v
        a
        l
        u
        e
        d
        a
        t
        t
        r
        i
        b
        u
        t
        e
        t
        o
        f
        i
        l
        t
        e
        r
        o
        n
        .
        Type `str`. """
        
        self.searchParam = None
        """ 
        A
        d
        a
        t
        e
        v
        a
        l
        u
        e
        d
        p
        a
        r
        a
        m
        e
        t
        e
        r
        t
        o
        s
        e
        a
        r
        c
        h
        o
        n
        .
        Type `str`. """
        
        self.valueDateTime = None
        """ 
        T
        h
        e
        v
        a
        l
        u
        e
        o
        f
        t
        h
        e
        f
        i
        l
        t
        e
        r
        ,
        a
        s
        a
        P
        e
        r
        i
        o
        d
        ,
        D
        a
        t
        e
        T
        i
        m
        e
        ,
        o
        r
        D
        u
        r
        a
        t
        i
        o
        n
        v
        a
        l
        u
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDuration = None
        """ 
        T
        h
        e
        v
        a
        l
        u
        e
        o
        f
        t
        h
        e
        f
        i
        l
        t
        e
        r
        ,
        a
        s
        a
        P
        e
        r
        i
        o
        d
        ,
        D
        a
        t
        e
        T
        i
        m
        e
        ,
        o
        r
        D
        u
        r
        a
        t
        i
        o
        n
        v
        a
        l
        u
        e
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ 
        T
        h
        e
        v
        a
        l
        u
        e
        o
        f
        t
        h
        e
        f
        i
        l
        t
        e
        r
        ,
        a
        s
        a
        P
        e
        r
        i
        o
        d
        ,
        D
        a
        t
        e
        T
        i
        m
        e
        ,
        o
        r
        D
        u
        r
        a
        t
        i
        o
        n
        v
        a
        l
        u
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(DataRequirementDateFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementDateFilter, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
        ])
        return js


class DataRequirementSort(element.Element):
    """ 
    O
    r
    d
    e
    r
    o
    f
    t
    h
    e
    r
    e
    s
    u
    l
    t
    s
    .
    
    
    S
    p
    e
    c
    i
    f
    i
    e
    s
    t
    h
    e
    o
    r
    d
    e
    r
    o
    f
    t
    h
    e
    r
    e
    s
    u
    l
    t
    s
    t
    o
    b
    e
    r
    e
    t
    u
    r
    n
    e
    d
    .
    
    """
    
    resource_type = "DataRequirementSort"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.direction = None
        """ 
        a
        s
        c
        e
        n
        d
        i
        n
        g
        |
        d
        e
        s
        c
        e
        n
        d
        i
        n
        g
        .
        Type `str`. """
        
        self.path = None
        """ 
        T
        h
        e
        n
        a
        m
        e
        o
        f
        t
        h
        e
        a
        t
        t
        r
        i
        b
        u
        t
        e
        t
        o
        p
        e
        r
        f
        o
        r
        m
        t
        h
        e
        s
        o
        r
        t
        .
        Type `str`. """
        
        super(DataRequirementSort, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DataRequirementSort, self).elementProperties()
        js.extend([
            ("direction", "direction", str, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
