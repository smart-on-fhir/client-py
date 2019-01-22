#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class GuidanceResponse(domainresource.DomainResource):
    """ 
    T
    h
    e
    f
    o
    r
    m
    a
    l
    r
    e
    s
    p
    o
    n
    s
    e
    t
    o
    a
    g
    u
    i
    d
    a
    n
    c
    e
    r
    e
    q
    u
    e
    s
    t
    .
    
    
    A
    g
    u
    i
    d
    a
    n
    c
    e
    r
    e
    s
    p
    o
    n
    s
    e
    i
    s
    t
    h
    e
    f
    o
    r
    m
    a
    l
    r
    e
    s
    p
    o
    n
    s
    e
    t
    o
    a
    g
    u
    i
    d
    a
    n
    c
    e
    r
    e
    q
    u
    e
    s
    t
    ,
    i
    n
    c
    l
    u
    d
    i
    n
    g
    a
    n
    y
    o
    u
    t
    p
    u
    t
    p
    a
    r
    a
    m
    e
    t
    e
    r
    s
    r
    e
    t
    u
    r
    n
    e
    d
    b
    y
    t
    h
    e
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
    ,
    a
    s
    w
    e
    l
    l
    a
    s
    t
    h
    e
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
    o
    f
    a
    n
    y
    p
    r
    o
    p
    o
    s
    e
    d
    a
    c
    t
    i
    o
    n
    s
    t
    o
    b
    e
    t
    a
    k
    e
    n
    .
    
    """
    
    resource_type = "GuidanceResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dataRequirement = None
        """ 
        A
        d
        d
        i
        t
        i
        o
        n
        a
        l
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
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ 
        E
        n
        c
        o
        u
        n
        t
        e
        r
        d
        u
        r
        i
        n
        g
        w
        h
        i
        c
        h
        t
        h
        e
        r
        e
        s
        p
        o
        n
        s
        e
        w
        a
        s
        r
        e
        t
        u
        r
        n
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.evaluationMessage = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        s
        r
        e
        s
        u
        l
        t
        i
        n
        g
        f
        r
        o
        m
        t
        h
        e
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
        o
        f
        t
        h
        e
        a
        r
        t
        i
        f
        a
        c
        t
        o
        r
        a
        r
        t
        i
        f
        a
        c
        t
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.moduleCanonical = None
        """ 
        W
        h
        a
        t
        g
        u
        i
        d
        a
        n
        c
        e
        w
        a
        s
        r
        e
        q
        u
        e
        s
        t
        e
        d
        .
        Type `str`. """
        
        self.moduleCodeableConcept = None
        """ 
        W
        h
        a
        t
        g
        u
        i
        d
        a
        n
        c
        e
        w
        a
        s
        r
        e
        q
        u
        e
        s
        t
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.moduleUri = None
        """ 
        W
        h
        a
        t
        g
        u
        i
        d
        a
        n
        c
        e
        w
        a
        s
        r
        e
        q
        u
        e
        s
        t
        e
        d
        .
        Type `str`. """
        
        self.note = None
        """ 
        A
        d
        d
        i
        t
        i
        o
        n
        a
        l
        n
        o
        t
        e
        s
        a
        b
        o
        u
        t
        t
        h
        e
        r
        e
        s
        p
        o
        n
        s
        e
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        g
        u
        i
        d
        a
        n
        c
        e
        r
        e
        s
        p
        o
        n
        s
        e
        w
        a
        s
        p
        r
        o
        c
        e
        s
        s
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.outputParameters = None
        """ 
        T
        h
        e
        o
        u
        t
        p
        u
        t
        p
        a
        r
        a
        m
        e
        t
        e
        r
        s
        o
        f
        t
        h
        e
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
        ,
        i
        f
        a
        n
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ 
        D
        e
        v
        i
        c
        e
        r
        e
        t
        u
        r
        n
        i
        n
        g
        t
        h
        e
        g
        u
        i
        d
        a
        n
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        W
        h
        y
        g
        u
        i
        d
        a
        n
        c
        e
        i
        s
        n
        e
        e
        d
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        g
        u
        i
        d
        a
        n
        c
        e
        i
        s
        n
        e
        e
        d
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requestIdentifier = None
        """ 
        T
        h
        e
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
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
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
        i
        s
        r
        e
        s
        p
        o
        n
        s
        e
        ,
        i
        f
        a
        n
        y
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.result = None
        """ 
        P
        r
        o
        p
        o
        s
        e
        d
        a
        c
        t
        i
        o
        n
        s
        ,
        i
        f
        a
        n
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        s
        u
        c
        c
        e
        s
        s
        |
        d
        a
        t
        a
        -
        r
        e
        q
        u
        e
        s
        t
        e
        d
        |
        d
        a
        t
        a
        -
        r
        e
        q
        u
        i
        r
        e
        d
        |
        i
        n
        -
        p
        r
        o
        g
        r
        e
        s
        s
        |
        f
        a
        i
        l
        u
        r
        e
        |
        e
        n
        t
        e
        r
        e
        d
        -
        i
        n
        -
        e
        r
        r
        o
        r
        .
        Type `str`. """
        
        self.subject = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        w
        a
        s
        p
        e
        r
        f
        o
        r
        m
        e
        d
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("moduleCanonical", "moduleCanonical", str, False, "module", True),
            ("moduleCodeableConcept", "moduleCodeableConcept", codeableconcept.CodeableConcept, False, "module", True),
            ("moduleUri", "moduleUri", str, False, "module", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, None, False),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, None, False),
            ("result", "result", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
